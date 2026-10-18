"""Transcribe un clip con voz, escribe el .srt y quema los subtitulos palabra
por palabra, con la palabra que se esta diciendo en el color de la marca.

  python3 herramientas/subtitulos.py <entrada.mp4> <salida.mp4>
         [--srt subtitulos.srt] [--idioma es] [--color cian] [--palabras 3]
         [--y 0.70] [--cuerpo 92] [--cambiar "mal=bien" ...]

Derivado de `tools/captions.py` de https://github.com/bekhruztbx/ai-creative-team
(MIT, (c) 2026 Bekhruz AI). Cambios: el idioma es un parametro y llega al
modelo, el color por defecto es el cian de la marca y acepta nombres de la
paleta, la tipografia se resuelve en vez de apuntar a un archivo fijo, y si el
clip viene mudo lo dice en una linea en vez de fallar dentro de ffmpeg.

El contorno negro de las letras NO es decorativo: el cian da 1,77:1 sobre
blanco, asi que sobre un fotograma claro las letras sin contorno no se leen.
"""
import argparse, os, re, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import FFMPEG, SR, STT, audio, fuente, probe, report, rgb, segmentos_voz

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--srt", default=None)
ap.add_argument("--idioma", default="es", choices=["es", "en", "fr", "de", "ja"])
ap.add_argument("--color", default="cian", help="color de la palabra que suena (nombre de la paleta o #rrggbb)")
ap.add_argument("--palabras", type=int, default=3, help="palabras por rotulo")
ap.add_argument("--y", type=float, default=0.70, help="posicion vertical (0 arriba .. 1 abajo)")
ap.add_argument("--cuerpo", type=int, default=92, help="cuerpo de la letra en px")
ap.add_argument("--cambiar", action="append", default=[], help='arregla una palabra mal oida: --cambiar "Vilu=Villuminations"')
a = ap.parse_args()

info = probe(a.src)
if not info["audio"]:
    raise SystemExit(
        f"{a.src} no tiene pista de audio, asi que no hay nada que transcribir.\n"
        "Para un clip de producto usa: python3 herramientas/rotulos.py"
    )


def palabras_faster_whisper(path, idioma):
    """Tiempos por palabra, que es lo que permite encender una sola palabra."""
    from faster_whisper import WhisperModel
    modelo = os.environ.get("WHISPER_MODEL", "small.en" if idioma == "en" else "small")
    m = WhisperModel(modelo, compute_type="int8")
    segs, _ = m.transcribe(path, language=idioma, word_timestamps=True, vad_filter=True)
    return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()], f"faster-whisper {modelo}"


def palabras_por_frase(path, idioma):
    """Respaldo: transcribe frase a frase y reparte el tiempo entre sus palabras por longitud."""
    stt, pcm, out = STT(idioma), audio(path, SR), []
    for s, e in segmentos_voz(path, ruido_db=-35, silencio_min=0.2):
        toks = stt.texto(pcm[int(s * SR):int(e * SR)]).split()
        if not toks:
            continue
        pesos = [len(re.sub(r"\W", "", t, flags=re.UNICODE)) + 2 for t in toks]
        tot, t, tramo = sum(pesos), s + 0.05, (e - s) - 0.1
        for tok, p in zip(toks, pesos):
            dur = tramo * p / tot
            out.append((tok, t, t + dur * 0.92)); t += dur
    return out, stt.motor


try:
    import faster_whisper  # noqa: F401
    palabras, motor = palabras_faster_whisper(a.src, a.idioma)
except ImportError:
    palabras, motor = palabras_por_frase(a.src, a.idioma)

if not palabras:
    raise SystemExit(f"no se ha reconocido ni una palabra en {a.src}. Revisa el idioma (--idioma) o el audio del clip.")

# Correcciones de palabras mal oidas, conservando el signo de puntuacion final.
arreglos = dict(r.split("=", 1) for r in a.cambiar if "=" in r)


def arreglar(w):
    limpio = re.sub(r"[.,!?;:]+$", "", w)
    return arreglos[limpio] + w[len(limpio):] if limpio in arreglos else w


palabras = [(arreglar(w), s, e) for w, s, e in palabras]

# Rotulos de N palabras, sin cruzar un final de frase.
rotulos, actual = [], []
for w in palabras:
    actual.append(w)
    if len(actual) >= a.palabras or re.search(r"[.!?]$", w[0]):
        rotulos.append(actual); actual = []
if actual:
    rotulos.append(actual)
if len(rotulos) > 1 and len(rotulos[-1]) == 1:        # que la ultima palabra no quede sola
    if len(rotulos[-2]) > 1:
        rotulos[-1].insert(0, rotulos[-2].pop())
    else:
        rotulos[-2].extend(rotulos.pop())


def ts(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


srt = a.srt or os.path.splitext(a.out)[0] + ".srt"
os.makedirs(os.path.dirname(os.path.abspath(srt)), exist_ok=True)
with open(srt, "w", encoding="utf-8") as f:
    for i, c in enumerate(rotulos):
        fin = c[-1][2] + 0.15 if i + 1 == len(rotulos) else min(c[-1][2] + 0.15, rotulos[i + 1][0][1] - 0.02)
        f.write(f"{i + 1}\n{ts(c[0][1])} --> {ts(fin)}\n{' '.join(w[0] for w in c)}\n\n")

# Quemado: palabras blancas con contorno negro, la que suena en el color de marca.
W, H, FPS = info["width"], info["height"], info["fps"] or 30
tipo, nombre_fuente = fuente(a.cuerpo, 850)
alto = rgb(a.color)
cache = {}


def capa(ri, wi):
    clave = (ri, wi)
    if clave in cache:
        return cache[clave]
    c = rotulos[ri]
    txt = [re.sub(r"[.,!?;:]+$", "", w[0]).upper() for w in c]
    hueco = a.cuerpo * 0.28
    anchos = [tipo.getlength(t) for t in txt]
    total = sum(anchos) + hueco * (len(anchos) - 1)
    im = Image.new("RGBA", (W, int(a.cuerpo * 2.2)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = (W - total) / 2
    for i, (t, w) in enumerate(zip(txt, anchos)):
        d.text((x, a.cuerpo * 0.4), t, font=tipo, fill=(alto + (255,)) if i == wi else (255, 255, 255, 255),
               stroke_width=max(4, a.cuerpo // 12), stroke_fill=(0, 0, 0, 255))
        x += w + hueco
    cache[clave] = np.asarray(im).astype(np.float32) / 255
    return cache[clave]


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
    ri = next((i for i, c in enumerate(rotulos)
               if c[0][1] - 0.05 <= t < (rotulos[i + 1][0][1] - 0.05 if i + 1 < len(rotulos) else c[-1][2] + 0.4)), None)
    if ri is not None:
        wi = max([j for j, w in enumerate(rotulos[ri]) if w[1] - 0.03 <= t] or [0])
        ov = capa(ri, wi); h = ov.shape[0]
        ya, yb = max(0, y0 - h // 2), min(H, y0 - h // 2 + h)
        region = fr[ya:yb].astype(np.float32) / 255
        al = ov[: yb - ya, :, 3:4]
        fr = fr.copy()
        fr[ya:yb] = ((region * (1 - al) + ov[: yb - ya, :, :3] * al) * 255 + .5).astype(np.uint8)
    enc.stdin.write(fr.tobytes())
enc.stdin.close(); enc.wait(); dec.wait()

report(tool="subtitulos", out=a.out, srt=srt, motor=motor, idioma=a.idioma, fuente=nombre_fuente,
       palabras=len(palabras), rotulos=len(rotulos), cambiadas=arreglos,
       transcripcion=" ".join(w[0] for w in palabras)[:600])
