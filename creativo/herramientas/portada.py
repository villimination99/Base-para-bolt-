"""Portada: elige el fotograma mas nitido y mejor iluminado y le pone un texto
corto y gordo encima.

  python3 herramientas/portada.py <video> <salida.jpg> --texto "TRES PALABRAS"
         [--color cian] [--acento 3] [--en SEGUNDOS] [--sitio arriba|medio|abajo]

--acento N pinta la palabra N (empezando en 1) en --color; las demas en blanco.
Sin --acento, la ultima.

Derivado de `tools/thumbnail.py` de https://github.com/bekhruztbx/ai-creative-team
(MIT, (c) 2026 Bekhruz AI). Cambios: color por defecto el cian de la marca y
acepta nombres de la paleta, y la tipografia se resuelve en vez de apuntar a un
archivo fijo. La eleccion automatica del fotograma, que es la parte buena del
original, se queda igual.
"""
import argparse, os, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import FFMPEG, fuente, probe, report, rgb

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--texto", required=True)
ap.add_argument("--color", default="cian", help="nombre de la paleta o #rrggbb")
ap.add_argument("--acento", type=int, default=0, help="que palabra lleva el color (0 = la ultima)")
ap.add_argument("--en", type=float, default=None, help="usa el fotograma de este segundo en vez del automatico")
ap.add_argument("--sitio", choices=["arriba", "medio", "abajo"], default="arriba", help="donde va el texto")
a = ap.parse_args()

info = probe(a.src)
W, H = info["width"], info["height"]
n = max(8, int(info["duration"] * 2))
raw = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", a.src,
                      "-vf", f"fps={n / max(info['duration'], 0.1):.4f},scale={W // 4}:{H // 4}",
                      "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
fot = np.frombuffer(raw, np.uint8).reshape(-1, H // 4, W // 4, 3).astype(np.float32)
if len(fot) == 0:
    raise SystemExit(f"no se ha podido sacar ningun fotograma de {a.src}")


def nota(f):
    g = f.mean(axis=2)
    nitidez = np.abs(4 * g[1:-1, 1:-1] - g[:-2, 1:-1] - g[2:, 1:-1] - g[1:-1, :-2] - g[1:-1, 2:]).mean()
    luz = 1 - abs(g.mean() - 128) / 128                  # ni muy oscuro ni quemado
    color = f.std(axis=2).mean() / 64                    # con color
    return nitidez * (0.6 + luz) * (0.8 + color)


salto = max(1, len(fot) // 10)                           # se evitan el principio y el final
rango = range(salto, len(fot) - salto) or range(len(fot))
mejor = max(rango, key=lambda i: nota(fot[i]))
t = mejor / len(fot) * info["duration"] if a.en is None else min(max(0.0, a.en), max(0.0, info["duration"] - 0.05))

pleno = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", a.src,
                        "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
im = Image.frombuffer("RGB", (W, H), pleno).convert("RGBA")

palabras = a.texto.upper().split()
if not palabras:
    raise SystemExit("--texto esta vacio")
acc = (a.acento or len(palabras)) - 1
alto = rgb(a.color)

cuerpo = int(W * 0.2)
tipo, nombre_fuente = fuente(cuerpo, 900)
while max(tipo.getlength(w) for w in palabras) > W * 0.86 and cuerpo > 40:
    cuerpo -= 6
    tipo, nombre_fuente = fuente(cuerpo, 900)

bloque = len(palabras) * int(cuerpo * 1.02)
y0 = {"arriba": int(H * 0.08), "medio": (H - bloque) // 2, "abajo": H - bloque - int(H * 0.1)}[a.sitio]

# Se oscurece la banda donde cae el texto. El original usaba una curva fija
# segun arriba/medio/abajo, y se apagaba antes de llegar a las ultimas lineas:
# con un texto de tres palabras, la ultima -- que es la que va en cian --
# aterrizaba sobre el fotograma sin oscurecer. El cian da 1,77:1 sobre claro,
# asi que ahi se perdia. Ahora la banda se calcula desde el bloque de texto, y
# cubre lo que de verdad hay que cubrir.
centro = (y0 + bloque / 2) / H
radio = max(0.30, (bloque / H) * 1.15)
grad = Image.new("L", (1, H))
for y in range(H):
    grad.putpixel((0, y), int(215 * max(0.0, 1 - abs(y / H - centro) / radio) ** 1.2))
im = Image.composite(Image.new("RGBA", (W, H), (0, 0, 0, 255)), im, grad.resize((W, H)))

sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(sombra)
y = y0
for w in palabras:
    d.text(((W - tipo.getlength(w)) / 2, y + cuerpo * 0.06), w, font=tipo, fill=(0, 0, 0, 180))
    y += int(cuerpo * 1.02)
im.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(cuerpo * 0.06)))

d = ImageDraw.Draw(im)
y = y0
for i, w in enumerate(palabras):
    d.text(((W - tipo.getlength(w)) / 2, y), w, font=tipo,
           fill=(alto + (255,)) if i == acc else (255, 255, 255, 255))
    y += int(cuerpo * 1.02)

os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
im.convert("RGB").save(a.out, quality=92)
report(tool="portada", out=a.out, fotograma_en=round(t, 2), texto=" ".join(palabras),
       palabra_en_color=palabras[acc] if 0 <= acc < len(palabras) else None,
       sitio=a.sitio, fuente=nombre_fuente, tamano=f"{W}x{H}")
