"""Hoja de contactos: seis fotogramas de un video en una sola imagen, para que
un agente pueda MIRAR una edicion con la herramienta Read.

  python3 herramientas/fotogramas.py <video> <salida.jpg>

Derivado de `tools/frames.py` de https://github.com/bekhruztbx/ai-creative-team
(MIT, (c) 2026 Bekhruz AI). Cambios: el fondo y la hora de cada fotograma van en
los colores de la marca, y avisa si un fotograma sale vacio en vez de reventar
al construir la imagen.
"""
import os, subprocess, sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import FFMPEG, probe, report, rgb

if len(sys.argv) < 3:
    raise SystemExit("uso: python3 herramientas/fotogramas.py <video> <salida.jpg>")
src, out = sys.argv[1], sys.argv[2]

info = probe(src)
W, H = info["width"], info["height"]
tw = 270
th = max(1, int(tw * H / W))
hoja = Image.new("RGB", (tw * 3 + 40, th * 2 + 30), rgb("negro"))

vacios = []
for i in range(6):
    t = info["duration"] * (i + 0.5) / 6
    raw = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", src,
                          "-frames:v", "1", "-vf", f"scale={tw}:{th}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True).stdout
    x, y = 10 + (i % 3) * (tw + 10), 10 + (i // 3) * (th + 10)
    if len(raw) < tw * th * 3:
        vacios.append(round(t, 2))                     # pasa en el ultimo fotograma de algunos clips
        ImageDraw.Draw(hoja).rectangle([x, y, x + tw, y + th], fill=rgb("fondo2"))
    else:
        hoja.paste(Image.frombuffer("RGB", (tw, th), raw), (x, y))
    # La hora va sobre una placa oscura, no suelta: el cian sobre un fotograma
    # cian o verde no se lee, y la hoja de contactos existe precisamente para
    # mirarla. La placa da 10,9:1 pase lo que pase debajo.
    d = ImageDraw.Draw(hoja)
    etiqueta = f"{t:.1f}s"
    cja = d.textbbox((0, 0), etiqueta)
    d.rectangle([x + 4, y + 4, x + 14 + cja[2] - cja[0], y + 12 + cja[3] - cja[1]], fill=rgb("negro"))
    d.text((x + 9, y + 7), etiqueta, fill=rgb("cian"))

os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
hoja.save(out, quality=85)
report(tool="fotogramas", out=out, fotogramas=6, segundos=round(info["duration"], 1), vacios=vacios)
