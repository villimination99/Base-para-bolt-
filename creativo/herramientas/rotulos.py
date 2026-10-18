"""Rotulos escritos sobre un clip SIN voz. Es el reemplazo de los subtitulos
para el catalogo: si no hay nada que transcribir, el mensaje lo pones tu.

  python3 herramientas/rotulos.py <entrada.mp4> <salida.mp4> \\
         --rotulo "0.3=LUZ QUE RESPIRA" --rotulo "4.0=HECHA A MANO" \\
         [--color cian] [--y 0.72] [--cuerpo 86] [--duracion 2.5] [--fundido 0.25]

  # o, si te da igual donde caigan, repartidos solos a lo largo del clip:
  python3 herramientas/rotulos.py e.mp4 s.mp4 --reparte "LUZ QUE RESPIRA|HECHA A MANO|VILLUMINATIONS"

Esto NO viene del repositorio original, que solo trae subtitulos de voz. La
ultima palabra de cada rotulo va en el color de la marca, igual que en la
portada, para que las dos piezas hablen el mismo idioma.
"""
import argparse, os, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import FFMPEG, fuente, probe, report, rgb

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--rotulo", action="append", default=[], help='"SEGUNDO=TEXTO", repetible')
ap.add_argument("--reparte", default=None, help='textos separados por "|", repartidos solos por el clip')
ap.add_argument("--color", default="cian", help="color de la ultima palabra (nombre de la paleta o #rrggbb)")
ap.add_argument("--y", type=float, default=0.72, help="posicion vertical (0 arriba .. 1 abajo)")
ap.add_argument("--cuerpo", type=int, default=86, help="cuerpo de la letra en px")
ap.add_argument("--duracion", type=float, default=2.5, help="cuanto aguanta cada rotulo (s)")
ap.add_argument("--fundido", type=float, default=0.25, help="entrada y salida en fundido (s)")
a = ap.parse_args()

info = probe(a.src)
W, H, FPS, DUR = info["width"], info["height"], info["fps"] or 30, info["duration"]

# De donde salen los rotulos y cuando entra cada uno.
entradas = []
if a.rotulo:
    for r in a.rotulo:
        if "=" not in r:
            raise SystemExit(f'--rotulo mal escrito: {r!r}. Tiene que ser "SEGUNDO=TEXTO", por ejemplo "0.3=LUZ QUE RESPIRA"')
        t, txt = r.split("=", 1)
        try:
            t = float(t)
        except ValueError:
            raise SystemExit(f"el segundo de {r!r} no es un numero")
        if txt.strip():
            entradas.append((t, txt.strip()))
elif a.reparte:
    textos = [t.strip() for t in a.reparte.split("|") if t.strip()]
    if not textos:
        raise SystemExit("--reparte no trae ningun texto")
    hueco = DUR / len(textos)
    entradas = [(i * hueco + hueco * 0.15, t) for i, t in enumerate(textos)]
else:
    raise SystemExit("hace falta --rotulo o --reparte. Mira el encabezado del archivo para los ejemplos.")

entradas.sort()
if entradas[-1][0] >= DUR:
    raise SystemExit(f"el ultimo rotulo entra en {entradas[-1][0]} s y el clip dura {DUR:.1f} s")

# Cada rotulo aguanta --duracion, o hasta que entra el siguiente.
tramos = []
for i, (t, txt) in enumerate(entradas):
    fin = min(t + a.duracion, DUR, entradas[i + 1][0] if i + 1 < len(entradas) else DUR)
    if fin - t > 0.1:
        tramos.append((max(0.0, t), fin, txt))

tipo, nombre_fuente = fuente(a.cuerpo, 850)
alto = rgb(a.color)
ANCHO_MAX = W * 0.84


def en_lineas(texto):
    """Parte el texto en lineas que caben, sin cortar palabras."""
    lineas, actual = [], []
    for p in texto.upper().split():
        prueba = " ".join(actual + [p])
        if actual and tipo.getlength(prueba) > ANCHO_MAX:
            lineas.append(actual); actual = [p]
        else:
            actual.append(p)
    if actual:
        lineas.append(actual)
    return lineas


cache = {}


def capa(idx):
    """La imagen RGBA del rotulo, cacheada: solo cambia su opacidad por fotograma."""
    if idx in cache:
        return cache[idx]
    lineas = en_lineas(tramos[idx][2])
    paso = int(a.cuerpo * 1.18)
    im = Image.new("RGBA", (W, paso * len(lineas) + a.cuerpo), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    ultima = (len(lineas) - 1, len(lineas[-1]) - 1)     # la ultima palabra, en color de marca
    y = a.cuerpo * 0.4
    for li, linea in enumerate(lineas):
        hueco = a.cuerpo * 0.26
        anchos = [tipo.getlength(p) for p in linea]
        x = (W - (sum(anchos) + hueco * (len(anchos) - 1))) / 2
        for pi, (p, w) in enumerate(zip(linea, anchos)):
            color = alto if (li, pi) == ultima else (255, 255, 255)
            d.text((x, y), p, font=tipo, fill=color + (255,),
                   stroke_width=max(4, a.cuerpo // 12), stroke_fill=(0, 0, 0, 255))
            x += w + hueco
        y += paso
    cache[idx] = np.asarray(im).astype(np.float32) / 255
    return cache[idx]


os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
dec = subprocess.Popen([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", a.src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       stdout=subprocess.PIPE)
enc = subprocess.Popen([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", a.src, "-map", "0:v", "-map", "1:a?",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                        "-c:a", "copy", "-shortest", a.out], stdin=subprocess.PIPE)
y0, n = int(H * a.y), 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3:
        break
    t = n / FPS; n += 1
    fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
    idx = next((i for i, (s, e, _) in enumerate(tramos) if s <= t < e), None)
    if idx is not None:
        s, e, _ = tramos[idx]
        op = 1.0
        if a.fundido > 0:                               # entra y sale en fundido
            op = min(1.0, (t - s) / a.fundido, (e - t) / a.fundido)
        if op > 0.01:
            ov = capa(idx); h = ov.shape[0]
            ya, yb = max(0, y0 - h // 2), min(H, y0 - h // 2 + h)
            region = fr[ya:yb].astype(np.float32) / 255
            al = ov[: yb - ya, :, 3:4] * op
            fr = fr.copy()
            fr[ya:yb] = ((region * (1 - al) + ov[: yb - ya, :, :3] * al) * 255 + .5).astype(np.uint8)
    enc.stdin.write(fr.tobytes())
enc.stdin.close(); enc.wait(); dec.wait()

report(tool="rotulos", out=a.out, fuente=nombre_fuente, color=a.color,
       rotulos=[{"entra": round(s, 2), "sale": round(e, 2), "texto": txt} for s, e, txt in tramos])
