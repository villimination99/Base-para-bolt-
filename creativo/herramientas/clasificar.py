"""Mira los clips de una carpeta y dice por que camino va cada uno: con voz o de
producto. Es lo primero que corre el equipo, para no tener que decidirlo a ojo.

  python3 herramientas/clasificar.py [carpeta]        # por defecto, inbox/

Decide asi:
  - sin pista de audio                          -> producto
  - con pista pero sin nada por encima del ruido -> producto
  - menos de 1,2 s de sonido, o menos del 12 %   -> producto (ambiente, no voz)
  - el resto                                     -> voz

No viene del repositorio original: alli se da por hecho que todos los clips
llevan voz. Aqui hace falta porque el catalogo es casi todo producto mudo.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from medios import escenas, probe, report, segmentos_voz

EXT = (".mp4", ".mov", ".m4v", ".webm", ".mkv")
carpeta = sys.argv[1] if len(sys.argv) > 1 else "inbox"
if not os.path.isdir(carpeta):
    raise SystemExit(f"no existe la carpeta {carpeta!r}")

clips = sorted(f for f in os.listdir(carpeta) if f.lower().endswith(EXT) and not f.startswith("."))
fichas = []
for nombre in clips:
    ruta = os.path.join(carpeta, nombre)
    try:
        info = probe(ruta)
    except Exception as e:
        fichas.append({"clip": nombre, "camino": "ilegible", "motivo": str(e)[:200]})
        continue

    dur = info["duration"]
    if not info["audio"]:
        seg, son, motivo = [], 0.0, "no trae pista de audio"
    else:
        seg = segmentos_voz(ruta)
        son = sum(e - s for s, e in seg)
        if not seg:
            motivo = "tiene pista de audio pero todo esta por debajo del umbral de ruido"
        elif son < 1.2 or son / max(dur, 0.01) < 0.12:
            motivo = f"solo {son:.1f} s de sonido en {dur:.1f} s: suena a ambiente, no a voz"
        else:
            motivo = f"{son:.1f} s de voz en {dur:.1f} s ({son / dur * 100:.0f} %)"

    hay_voz = bool(seg) and son >= 1.2 and son / max(dur, 0.01) >= 0.12
    ficha = {
        "clip": nombre,
        "camino": "voz" if hay_voz else "producto",
        "motivo": motivo,
        "segundos": round(dur, 1),
        "audio": info["audio"],
        "tamano": f"{info['width']}x{info['height']}",
        "vertical": info["height"] >= info["width"],
    }
    if not hay_voz:                      # al de producto le sirve saber cuantos planos hay
        cortes = escenas(ruta)
        ficha["cambios_de_plano"] = len(cortes)
        ficha["ritmo"] = "planos" if len(cortes) >= 2 else "plano fijo"
    fichas.append(ficha)

report(tool="clasificar", carpeta=carpeta, clips=len(fichas),
       voz=sum(1 for f in fichas if f["camino"] == "voz"),
       producto=sum(1 for f in fichas if f["camino"] == "producto"),
       fichas=fichas)
