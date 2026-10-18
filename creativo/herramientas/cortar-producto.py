"""Corte para clips SIN voz: lamparas, montajes, primeros planos.

Donde el corte de voz usa las frases para marcar el ritmo, este usa los
**cambios de plano**. Si el clip es un plano fijo y no hay ninguno, se queda con
un tramo limpio del medio en vez de inventarse cortes.

  python3 herramientas/cortar-producto.py <clip> <salida.mp4>
         [--max 20] [--pulso 2.0] [--umbral 0.30] [--entrada 0.3]
         [--marco recorte|difuminado] [--audio silencio|origen|<archivo.mp3>]

Esto NO viene del repositorio original: alli `cut.py` depende de
`speech_segments`, asi que con un clip mudo devuelve cero trozos y le pasa a
ffmpeg un `concat=n=0` que revienta. Esta herramienta es la que hace falta para
el catalogo, que es casi todo producto sin voz.
"""
import argparse, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import FFMPEG, escenas, probe, report, run

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--max", type=float, default=20, help="duracion maxima de la edicion, en segundos")
ap.add_argument("--pulso", type=float, default=2.0, help="cuanto dura cada plano que se conserva (s)")
ap.add_argument("--umbral", type=float, default=0.30, help="sensibilidad del cambio de plano (0.1 mucho, 0.6 poco)")
ap.add_argument("--entrada", type=float, default=0.3, help="se salta este arranque, que suele venir movido (s)")
ap.add_argument("--marco", choices=["recorte", "difuminado"], default="recorte", help="como se hace vertical un clip ancho")
ap.add_argument("--audio", default="silencio",
                help="'silencio' (pista muda, para poner musica en la app), 'origen' (el audio del clip) o la ruta de un mp3/wav")
a = ap.parse_args()

info = probe(a.src)
cortes = [t for t in escenas(a.src, a.umbral) if a.entrada <= t <= info["duration"] - 0.4]

# Los tramos que se conservan. Con cambios de plano, uno por cambio; sin
# ninguno, un solo tramo, porque picar un plano fijo en trozos no da ritmo: da
# saltos sin motivo.
tramos = []
if len(cortes) >= 2:
    arranque = [a.entrada] if cortes[0] > a.entrada + a.pulso else []
    for t in arranque + cortes:
        s, e = t, min(t + a.pulso, info["duration"])
        if e - s < 0.35:
            continue
        if tramos and s <= tramos[-1][1] + 0.05:
            tramos[-1] = (tramos[-1][0], max(tramos[-1][1], e))
        else:
            tramos.append((s, e))
    modo = f"{len(cortes)} cambios de plano"
else:
    s = min(a.entrada, max(0.0, info["duration"] - 0.5))
    tramos = [(s, min(s + a.max, info["duration"]))]
    modo = "plano fijo, un solo tramo"

salida, total = [], 0.0
for s, e in tramos:
    if total + (e - s) > a.max:
        e = s + (a.max - total)
    if e - s > 0.2:
        salida.append((s, e)); total += e - s
    if total >= a.max - 0.05:
        break
if not salida:
    raise SystemExit(f"{a.src} es demasiado corto para sacar nada ({info['duration']:.1f} s)")

if a.audio == "origen" and not info["audio"]:
    raise SystemExit(f"pediste --audio origen pero {a.src} no trae pista de audio. Usa --audio silencio o pasa un archivo.")

# Paso 1: el video, sin audio. Si el audio sale del propio clip se hace de una
# vez, porque los tramos son los mismos y no hay nada que volver a juntar.
con_audio_origen = a.audio == "origen"
partes = "".join(f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS[v{i}];" for i, (s, e) in enumerate(salida))
cat = "".join(f"[v{i}]" for i in range(len(salida))) + f"concat=n={len(salida)}:v=1:a=0[cv]"
if a.marco == "recorte":
    marco = "[cv]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v]"
else:
    marco = ("[cv]split[b][f];[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40[bg];"
             "[f]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]")

os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
comun = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30"]

if con_audio_origen:
    pa = "".join(f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[a{i}];" for i, (s, e) in enumerate(salida))
    ca = "".join(f"[a{i}]" for i in range(len(salida))) + f"concat=n={len(salida)}:v=0:a=1[ca]"
    run(["-i", a.src, "-filter_complex", partes + pa + cat + ";" + ca + ";" + marco + ";[ca]loudnorm=I=-14:TP=-1.5[a]",
         "-map", "[v]", "-map", "[a]"] + comun + ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", a.out])
else:
    tmp = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False); tmp.close()
    try:
        run(["-i", a.src, "-filter_complex", partes + cat + ";" + marco, "-map", "[v]", "-an"] + comun + [tmp.name])
        # Paso 2: se le pega la pista de audio. El video se copia tal cual, asi
        # que no se recomprime dos veces.
        if a.audio == "silencio":
            run(["-i", tmp.name, "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
                 "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", a.out])
        else:
            if not os.path.exists(a.audio):
                raise SystemExit(f"no encuentro el audio {a.audio!r}. Usa 'silencio', 'origen' o la ruta de un mp3/wav.")
            run(["-i", tmp.name, "-stream_loop", "-1", "-i", a.audio, "-map", "0:v", "-map", "1:a",
                 "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-shortest", a.out])
    finally:
        os.remove(tmp.name)          # el temporal es de la herramienta, no del usuario

report(tool="cortar-producto", out=a.out, ritmo=modo, segundos_bruto=round(info["duration"], 1),
       segundos_edicion=round(total, 1), planos=len(salida), audio=a.audio,
       cortes_detectados=[round(t, 2) for t in cortes[:20]])
