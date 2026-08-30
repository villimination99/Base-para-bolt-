#!/usr/bin/env python3
"""
VILLUMINATIONS — El vídeo del hero
===================================
Cinco segundos en bucle para la cabecera de la tienda, dibujados con nuestra
propia lámina. Sin metraje de banco, sin música de banco: el sigilo VI de
`ropa/dist/`, quieto y legible, con el barrido y la retícula moviéndose
alrededor.

    python3 tienda/hero.py            # el WebM y su fotograma de póster
    python3 tienda/hero.py --fps 30   # más suave y más pesado

**Fotograma a fotograma, no grabando la pantalla.** Grabar da una duración
aproximada, fotogramas perdidos y un bucle que salta al volver al principio.
Aquí cada fotograma se pide con su instante exacto —`?t=` de 0 a 1— y todo lo
que se mueve vuelve a su sitio en t=1. El bucle cierra sin costura porque está
construido para cerrar, no porque haya salido bien.

**Por qué WebM y no MP4.** El ffmpeg que trae Playwright solo lleva VP8; no hay
H.264 en esta máquina. WebM lo reproducen Chrome, Firefox, Edge y Safari 16 en
adelante, que es casi todo el tráfico, pero **el selector de vídeo de Shopify
pide .mp4 o .mov**. Dos salidas honestas:

· Subir el WebM a Contenido → Archivos y ponerlo con una etiqueta `<video>` en
  una sección de HTML personalizado. Funciona hoy.
· Convertirlo a MP4 donde haya H.264 (`ffmpeg -i hero.webm -c:v libx264
  -crf 20 -pix_fmt yuv420p hero.mp4`) y usar la sección de vídeo del tema.

El póster NO sale del primer fotograma: en t=0 la marca todavía no ha entrado
y la cabecera saldría sin nombre mientras carga el vídeo. Sale de un instante
con todo ya en su sitio. Sin póster se ve un rectángulo negro al cargar, y eso
Google lo mide como salto de diseño.
"""

import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LAMINA = RAIZ / "ropa" / "dist" / "vi-sigilo-cian.svg"
SALIDA = RAIZ / "tienda" / "hero"

FFMPEG = "/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux"
CHROMIUM = "/opt/pw-browsers/chromium"

ANCHO, ALTO = 1920, 1080
SEGUNDOS = 5

# La paleta de la marca, la misma de brand.css.
CIAN = "#00f0ff"
FONDO = "#05060a"

PAGINA = """<!doctype html><meta charset="utf-8">
<style>
  html,body{margin:0;padding:0;width:%(ancho)spx;height:%(alto)spx;
            overflow:hidden;background:%(fondo)s}
  .escena{position:relative;width:100%%;height:100%%;
          background:
            radial-gradient(120%% 90%% at 50%% 45%%, #0b1a22 0%%, %(fondo)s 62%%),
            %(fondo)s;
          display:grid;place-items:center}
  /* la retícula, la misma que llevan las portadas */
  .rejilla{position:absolute;inset:0;
    background-image:linear-gradient(rgba(0,240,255,.055) 1px, transparent 1px),
                     linear-gradient(90deg, rgba(0,240,255,.055) 1px, transparent 1px);
    background-size:96px 96px}
  .sigilo{position:relative;width:660px;height:660px;margin-bottom:70px;
          filter:drop-shadow(0 0 26px rgba(0,240,255,.34))}
  .sigilo svg{width:100%%;height:100%%;display:block}
  /* el aro por el que corre el barrido. Sin él, el barrido flota suelto y
     parece una mancha en vez de un radar recorriendo la circunferencia. */
  .aro{position:absolute;inset:0;border-radius:50%%;
    border:1px solid rgba(0,240,255,.11)}
  /* el barrido: una sola vuelta en los cinco segundos */
  .barrido{position:absolute;inset:0;border-radius:50%%;
    background:conic-gradient(from var(--giro),
      rgba(0,240,255,0) 0deg, rgba(0,240,255,0) 258deg,
      rgba(0,240,255,.10) 320deg, rgba(0,240,255,.38) 352deg,
      rgba(0,240,255,.85) 360deg);
    -webkit-mask:radial-gradient(circle, transparent 47.4%%, #000 48.6%%, #000 50%%, transparent 50.4%%);
            mask:radial-gradient(circle, transparent 47.4%%, #000 48.6%%, #000 50%%, transparent 50.4%%)}
  .marca{position:absolute;left:0;right:0;bottom:96px;text-align:center;
    font-family:ui-sans-serif,system-ui,sans-serif;font-weight:600;
    color:#dbe9ee;font-size:30px;letter-spacing:.62em;text-indent:.62em}
  .lema{position:absolute;left:0;right:0;bottom:56px;text-align:center;
    font-family:ui-sans-serif,system-ui,sans-serif;
    color:#7f97a1;font-size:15px;letter-spacing:.24em;text-indent:.24em}
</style>
<div class="escena">
  <div class="rejilla"></div>
  <div class="sigilo">%(svg)s<div class="aro"></div><div class="barrido"></div></div>
  <div class="marca">VILLUMINATIONS</div>
  <div class="lema">%(lema)s</div>
</div>
"""

LEMA = "CADA CIFRA CON SU FUENTE"


def lamina() -> str:
    """El SVG del sigilo, sin su cabecera de documento."""
    svg = LAMINA.read_text(encoding="utf-8")
    return re.sub(r'\swidth="\d+"\s+height="\d+"', "", svg, count=1)


def pagina() -> str:
    return PAGINA % {"ancho": ANCHO, "alto": ALTO, "fondo": FONDO,
                     "svg": lamina(), "lema": LEMA}


# Playwright vive en Node en esta máquina, no en Python: el paquete de Python
# no está instalado. El renderizador va en JavaScript y se lanza con node.
GUION = r'''
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [ruta, destino, ancho, alto, cuadros] = process.argv.slice(2);
const W = +ancho, H = +alto, N = +cuadros;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const pg = await b.newPage({ viewport: { width: W, height: H } });
await pg.goto('file://' + ruta);
for (let i = 0; i < N; i++) {
  const t = i / N;                       // 0 <= t < 1, cierra en 1
  await pg.evaluate((t) => {
    const dosPi = Math.PI * 2;
    // El sigilo NO gira. Se probo girandolo y a mitad de vuelta la V deja de
    // leerse como una V: en una cabecera lo unico que no se puede perder es
    // que la marca se reconozca. Lo que se mueve es lo de alrededor.
    // La reticula deriva una casilla entera, asi que en t=1 esta igual.
    document.querySelector('.rejilla').style.backgroundPosition =
        (t * 96) + 'px ' + (t * 96) + 'px';
    // el barrido da una vuelta entera
    document.querySelector('.barrido').style.setProperty(
        '--giro', (t * 360) + 'deg');
    // el halo respira dos veces
    const halo = 22 + 14 * (1 - Math.cos(dosPi * 2 * t)) / 2;
    document.querySelector('.sigilo').style.filter =
        'drop-shadow(0 0 ' + halo.toFixed(1) + 'px rgba(0,240,255,.36))';
    // la marca entra al principio y se queda; el lema, un poco despues
    const e = Math.min(1, t / 0.18);
    const m = document.querySelector('.marca');
    m.style.opacity = e.toFixed(3);
    m.style.transform = 'translateY(' + ((1 - e) * 14).toFixed(2) + 'px)';
    const e2 = Math.max(0, Math.min(1, (t - 0.12) / 0.18));
    document.querySelector('.lema').style.opacity = e2.toFixed(3);
  }, t);
  // JPEG y no PNG: el ffmpeg de Playwright viene pelado y su único
  // decodificador de imagen es MJPEG. Calidad alta para que el degradado
  // del fondo no salga a bandas.
  await pg.screenshot({ path: `${destino}/f${String(i).padStart(4, '0')}.jpg`,
                        type: 'jpeg', quality: 94 });
}
await b.close();
'''


def main() -> int:
    fps = 25
    if "--fps" in sys.argv:
        fps = int(sys.argv[sys.argv.index("--fps") + 1])
    cuadros = fps * SEGUNDOS

    if not LAMINA.exists():
        raise SystemExit(f"  Falta la lámina {LAMINA}. "
                         f"python3 ropa/tools/dibujar-marca.py la rehace.")

    SALIDA.mkdir(parents=True, exist_ok=True)
    trabajo = SALIDA / "cuadros"
    trabajo.mkdir(exist_ok=True)
    for viejo in trabajo.glob("f*.jpg"):
        viejo.unlink()

    html = SALIDA / "_hero.html"
    html.write_text(pagina(), encoding="utf-8")
    guion = SALIDA / "_hero.mjs"
    guion.write_text(GUION, encoding="utf-8")

    print(f"\n  {cuadros} fotogramas a {fps} por segundo · {ANCHO}×{ALTO}")
    r = subprocess.run(
        ["node", str(guion), str(html), str(trabajo),
         str(ANCHO), str(ALTO), str(cuadros)],
        capture_output=True, text=True, timeout=1800)
    if r.returncode:
        raise SystemExit(f"  Playwright: {r.stderr[-1200:]}")

    hechos = sorted(trabajo.glob("f*.jpg"))
    if len(hechos) != cuadros:
        raise SystemExit(f"  Salieron {len(hechos)} de {cuadros} fotogramas.")

    # Este ffmpeg no tiene el demuxer de secuencias de fichero ni
    # decodificador de PNG: solo image2pipe y MJPEG. Los fotogramas entran
    # concatenados por la entrada estándar.
    webm = SALIDA / "hero-villuminations.webm"
    tubo = b"".join(f.read_bytes() for f in hechos)
    r = subprocess.run(
        [FFMPEG, "-y", "-f", "image2pipe", "-vcodec", "mjpeg",
         "-framerate", str(fps), "-i", "pipe:0",
         "-c:v", "libvpx", "-b:v", "2600k", "-crf", "22",
         "-auto-alt-ref", "0", "-pix_fmt", "yuv420p", str(webm)],
        input=tubo, capture_output=True, timeout=1800)
    if r.returncode:
        raise SystemExit(f"  ffmpeg: {r.stderr.decode()[-1200:]}")

    # El póster NO es el primer fotograma: en t=0 la marca todavía no ha
    # entrado y saldría una cabecera sin nombre mientras carga el vídeo. Se
    # coge un instante con todo ya en su sitio.
    poster = SALIDA / "hero-poster.jpg"
    poster.write_bytes(hechos[int(len(hechos) * 0.42)].read_bytes())

    html.unlink(missing_ok=True)
    guion.unlink(missing_ok=True)
    for f in hechos:
        f.unlink()
    trabajo.rmdir()

    print(f"    {webm.name:32} {webm.stat().st_size/1024:.0f} KB · "
          f"{SEGUNDOS} s en bucle")
    print(f"    {poster.name:32} {poster.stat().st_size/1024:.0f} KB · "
          f"póster, para que no salga un rectángulo negro al cargar\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
