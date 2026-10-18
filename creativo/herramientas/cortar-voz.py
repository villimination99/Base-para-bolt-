"""Corte para clips CON voz: quita las pausas, tira las muletillas, limita la
duracion y reencuadra a vertical 1080x1920.

  python3 herramientas/cortar-voz.py <clip> <salida.mp4> [--max 45] [--idioma es]
                                     [--pausa 0.45] [--marco recorte|difuminado]
                                     [--dejar-muletillas]

Derivado de `tools/cut.py` de https://github.com/bekhruztbx/ai-creative-team
(MIT, (c) 2026 Bekhruz AI). Cambios: el idioma es un parametro y las muletillas
salen de la lista de ese idioma, y si el clip viene mudo lo dice y manda a
`cortar-producto.py` en vez de pasarle a ffmpeg un concat de cero trozos, que
es lo que hacia el original.
"""
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import SR, STT, audio, probe, report, run, segmentos_voz, solo_muletillas

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--max", type=float, default=45, help="duracion maxima de la edicion, en segundos")
ap.add_argument("--idioma", default="es", choices=["es", "en", "fr", "de", "ja"], help="idioma de la voz")
ap.add_argument("--pausa", type=float, default=0.45, help="corta las pausas mas largas que esto (s)")
ap.add_argument("--aire", type=float, default=0.12, help="aire que se deja alrededor de cada frase (s)")
ap.add_argument("--marco", choices=["recorte", "difuminado"], default="recorte", help="como se hace vertical un clip ancho")
ap.add_argument("--dejar-muletillas", action="store_true", help="no quitar las frases que son solo eh/um")
a = ap.parse_args()

info = probe(a.src)
if not info["audio"]:
    raise SystemExit(
        f"{a.src} no tiene pista de audio, asi que aqui no hay voz que cortar.\n"
        "Para un clip de producto usa: python3 herramientas/cortar-producto.py"
    )

segs = segmentos_voz(a.src, silencio_min=a.pausa)
if not segs:
    raise SystemExit(
        f"{a.src} tiene pista de audio pero no se ha detectado ni una frase (todo por debajo del umbral de ruido).\n"
        "Si es un clip de producto con ambiente, usa: python3 herramientas/cortar-producto.py"
    )

muletillas = []
if not a.dejar_muletillas:                           # una frase corta que solo es "eh"/"um" se va
    stt, pcm, dejados = STT(a.idioma), audio(a.src), []
    for s, e in segs:
        txt = stt.texto(pcm[int(s * SR):int(e * SR)]) if e - s < 1.6 else ""
        if txt and solo_muletillas(txt, a.idioma, e - s):
            muletillas.append((round(s, 2), txt))
        else:
            dejados.append((s, e))
    segs = dejados
    if not segs:
        raise SystemExit("despues de quitar las muletillas no queda nada: revisa el clip o pasa --dejar-muletillas")

keep = []
for s, e in segs:                                    # aire a cada frase, une lo que se solape
    s, e = max(0.0, s - a.aire), min(info["duration"], e + a.aire)
    if keep and s <= keep[-1][1]:
        keep[-1] = (keep[-1][0], e)
    else:
        keep.append((s, e))

out, total = [], 0.0
for s, e in keep:                                    # y se para en --max
    if total + (e - s) > a.max:
        e = s + (a.max - total)
    if e - s > 0.2:
        out.append((s, e)); total += e - s
    if total >= a.max - 0.05:
        break

partes = "".join(
    f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[a{i}];"
    for i, (s, e) in enumerate(out))
cat = "".join(f"[v{i}][a{i}]" for i in range(len(out))) + f"concat=n={len(out)}:v=1:a=1[cv][ca]"
if a.marco == "recorte":
    marco = "[cv]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v]"
else:
    marco = ("[cv]split[b][f];[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40[bg];"
             "[f]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]")

os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
run(["-i", a.src, "-filter_complex", partes + cat + ";" + marco + ";[ca]loudnorm=I=-14:TP=-1.5[a]",
     "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
     "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", a.out])

report(tool="cortar-voz", out=a.out, idioma=a.idioma, segundos_bruto=round(info["duration"], 1),
       segundos_edicion=round(total, 1), segundos_quitados=round(info["duration"] - total, 1),
       frases=len(out), muletillas_quitadas=[f"{t}s {w}" for t, w in muletillas])
