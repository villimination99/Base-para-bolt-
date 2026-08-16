#!/usr/bin/env python3
"""
VILLUMINATIONS — Portadas de producto para la tienda
-----------------------------------------------------
Genera la imagen de cada ficha: cuadrada, 1600×1600, con la paleta de la marca.
Los tres niveles de planes no tenían imagen ninguna —la ficha salía con el
hueco gris del tema— y los libros mostraban una foto que no era su cubierta.

Dos maneras de componer, según lo que el producto sea:

· Un libro tiene cubierta de verdad, así que la portada del producto la
  enseña. Se rasteriza la primera página del PDF ya auditado y se monta sobre
  el fondo de marca. Lo que ve el comprador es exactamente lo que se descarga,
  que es la única promesa que una portada debería hacer.

· Un nivel de planes no es un documento sino un paquete de varios, y no hay
  una cubierta que lo represente sin mentir. Se compone una tarjeta
  tipográfica con el acento del nivel —cian el básico, magenta el pro, verde
  el elite, los mismos que ya usan los PDF por dentro— y la cuenta de lo que
  lleva. Nada de imágenes de archivo ni de fotos de gimnasio: el producto es
  un documento y la portada lo dice.

Las cifras no se escriben a mano. El número de páginas sale de contar el PDF y
el de documentos de contar los ficheros; si mañana un libro crece, la portada
crece con él en cuanto se relance esto.

Uso:  python3 tienda/portadas.py            escribe tienda/portadas/*.png
      python3 tienda/portadas.py --html     deja también el HTML, para mirarlo
"""

import base64
import json
import re
import subprocess
import sys
from pathlib import Path

import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parent.parent
SALIDA = Path(__file__).resolve().parent / "portadas"
ASSETS = ROOT / "planes" / "assets"
NODE = "/opt/node22/bin/node"

LADO = 1600          # Shopify recorta a cuadrado en la rejilla; se le da cuadrado
ESCALA = 4           # rasterizado de la cubierta: 4× sobre 148 mm da holgura de sobra

# Los tres niveles, con el acento que ya llevan por dentro sus PDF.
NIVELES = [
    {"archivo": "plan-basico", "acento": "#00f0ff", "acento2": "#0066ff",
     "nivel": "Básico", "titulo": "Volumen Limpio",
     "docs": ["01-basico"]},
    {"archivo": "plan-pro", "acento": "#ff00e5", "acento2": "#7b2fff",
     "nivel": "Pro", "titulo": "Definición + Volumen",
     "docs": ["01-basico", "02-pro", "03-pro", "04-pro", "05-pro"]},
    {"archivo": "plan-elite", "acento": "#00ff88", "acento2": "#ff6600",
     "nivel": "Elite", "titulo": "Todo Incluido",
     "docs": ["01-basico", "02-pro", "03-pro", "04-pro", "05-pro", "06-elite",
              "07-elite", "08-elite", "09-elite", "10-elite", "11-elite"]},
]

CSS_COMUN = """
@font-face{font-family:'Orbitron';font-weight:700;src:url(FUENTES/orbitron-700.ttf)}
@font-face{font-family:'Orbitron';font-weight:900;src:url(FUENTES/orbitron-900.ttf)}
@font-face{font-family:'Rajdhani';font-weight:400;src:url(FUENTES/rajdhani-400.ttf)}
@font-face{font-family:'Rajdhani';font-weight:600;src:url(FUENTES/rajdhani-600.ttf)}
@font-face{font-family:'Rajdhani';font-weight:700;src:url(FUENTES/rajdhani-700.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:LADOpx;height:LADOpx}
body{
  font-family:'Rajdhani',system-ui,sans-serif;color:#eef2ff;
  display:flex;align-items:center;justify-content:center;
  background:
    radial-gradient(115% 78% at 50% -8%, rgba(RGB1,.16) 0%, transparent 56%),
    radial-gradient(88% 58% at 108% 106%, rgba(RGB2,.13) 0%, transparent 62%),
    #050510;
}
/* Retícula tenue: da profundidad sin competir con el texto. */
.malla{position:absolute;inset:0;opacity:.055;
  background-image:linear-gradient(#fff 1px,transparent 1px),
                   linear-gradient(90deg,#fff 1px,transparent 1px);
  background-size:80px 80px}
.marca{position:absolute;left:0;right:0;bottom:74px;text-align:center;
  font-family:'Orbitron';font-weight:700;font-size:26px;letter-spacing:.34em;
  color:#8b95b5}
.filete{position:absolute;left:50%;transform:translateX(-50%);bottom:130px;
  width:190px;height:2px;
  background:linear-gradient(90deg,transparent,var(--a),transparent)}
"""

LIBRO_HTML = """<!doctype html><meta charset="utf-8"><style>
{css}
:root{{--a:{acento}}}
.centro{{position:relative;display:flex;flex-direction:column;align-items:center;
  gap:44px}}
.cubierta{{width:790px;border-radius:10px;display:block;
  box-shadow:0 40px 90px rgba(0,0,0,.62),
             0 0 0 1px rgba(255,255,255,.10),
             0 0 78px rgba({rgb1},.30)}}
.datos{{display:flex;gap:30px;align-items:center;
  font-weight:600;font-size:29px;letter-spacing:.05em;color:#c3cbe4}}
.datos b{{color:var(--a);font-weight:700}}
.punto{{width:6px;height:6px;border-radius:50%;background:#3a4166}}
.idiomas{{font-family:'Orbitron';font-weight:700;font-size:22px;
  letter-spacing:.26em;color:var(--a);opacity:.92}}
</style>
<div class="malla"></div>
<div class="centro">
  <img class="cubierta" src="data:image/png;base64,{cubierta}">
  <div class="idiomas">ES · EN · FR</div>
  <div class="datos">
    <span><b>{paginas}</b> páginas</span><i class="punto"></i>
    <span><b>{capitulos}</b> capítulos</span><i class="punto"></i>
    <span><b>{laminas}</b> láminas</span>
  </div>
</div>
<div class="filete"></div>
<div class="marca">VILLUMINATIONS</div>
"""

NIVEL_HTML = """<!doctype html><meta charset="utf-8"><style>
{css}
:root{{--a:{acento};--a2:{acento2}}}
.centro{{position:relative;width:100%;padding:0 130px;text-align:center}}
.nivel{{font-family:'Orbitron';font-weight:900;font-size:150px;line-height:1;
  letter-spacing:.02em;
  background:linear-gradient(115deg,var(--a) 34%,var(--a2) 118%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 0 40px rgba({rgb1},.42))}}
.titulo{{margin-top:34px;font-weight:700;font-size:64px;line-height:1.12;
  letter-spacing:.005em;color:#eef2ff}}
.regla{{margin:52px auto 0;width:300px;height:3px;
  background:linear-gradient(90deg,transparent,var(--a),transparent)}}
.cuenta{{margin-top:52px;display:flex;justify-content:center;gap:34px;
  align-items:center;font-weight:600;font-size:33px;letter-spacing:.05em;
  color:#c3cbe4}}
.cuenta b{{color:var(--a);font-weight:700}}
.punto{{width:7px;height:7px;border-radius:50%;background:#3a4166}}
.idiomas{{margin-top:44px;font-family:'Orbitron';font-weight:700;font-size:24px;
  letter-spacing:.26em;color:var(--a);opacity:.92}}
</style>
<div class="malla"></div>
<div class="centro">
  <div class="nivel">{nivel}</div>
  <div class="titulo">{titulo}</div>
  <div class="regla"></div>
  <div class="cuenta">
    <span><b>{docs}</b> {palabra}</span><i class="punto"></i>
    <span><b>{paginas}</b> páginas</span>
  </div>
  <div class="idiomas">ES · EN · FR</div>
</div>
<div class="marca">VILLUMINATIONS</div>
"""

DISPARO = """
import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;
const [html, png] = process.argv.slice(2);
const navegador = await chromium.launch();
const pagina = await navegador.newPage({
  viewport: { width: LADO, height: LADO }, deviceScaleFactor: 1 });
await pagina.goto('file://' + html, { waitUntil: 'networkidle' });
await pagina.evaluate(() => document.fonts.ready);
await pagina.screenshot({ path: png });
await navegador.close();
"""


ACENTOS_CSS = ROOT / "libros" / "assets" / "libro.css"
_ACENTO = re.compile(
    r"\.acento-(\w+)\s*\{[^}]*--acento:\s*(#[0-9a-fA-F]{6})[^}]*"
    r"--acento-2:\s*(#[0-9a-fA-F]{6})")


def acentos() -> dict[str, tuple[str, str]]:
    """El mapa de acentos, leído de la hoja de estilo de los libros.

    No se copia aquí: cada libro declara su acento por nombre en su JSON y el
    color de ese nombre vive en libro.css. Duplicarlo significaría que un día
    la portada del producto y la cubierta del libro dejarían de ser del mismo
    color sin que nadie lo hubiera decidido.
    """
    mapa = {n: (a, b) for n, a, b
            in _ACENTO.findall(ACENTOS_CSS.read_text())}
    if not mapa:
        raise SystemExit(f"  Sin acentos en {ACENTOS_CSS}: ¿cambió el formato?")
    return mapa


def rgb(hexa: str) -> str:
    h = hexa.lstrip("#")
    return ",".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))


def css(acento: str, acento2: str) -> str:
    return (CSS_COMUN
            .replace("FUENTES", str(ASSETS / "fonts"))
            .replace("LADO", str(LADO))
            .replace("RGB1", rgb(acento))
            .replace("RGB2", rgb(acento2)))


def cubierta_png(pdf: Path) -> str:
    """La primera página del PDF, en base64 y a resolución de sobra."""
    pagina = pdfium.PdfDocument(str(pdf))[0]
    imagen = pagina.render(scale=ESCALA).to_pil()
    tmp = SALIDA / "_tmp.png"
    imagen.save(tmp)
    dato = base64.b64encode(tmp.read_bytes()).decode()
    tmp.unlink()
    return dato


def disparar(html: str, png: Path, guardar_html: bool) -> None:
    ruta = SALIDA / (png.stem + ".html")
    ruta.write_text(html)
    guion = SALIDA / "_disparo.mjs"
    guion.write_text(DISPARO.replace("LADO", str(LADO)))
    subprocess.run([NODE, str(guion), str(ruta), str(png)], check=True)
    guion.unlink()
    if not guardar_html:
        ruta.unlink()


def main() -> None:
    guardar_html = "--html" in sys.argv[1:]
    SALIDA.mkdir(exist_ok=True)

    mapa = acentos()
    print(f"\n  Portadas de producto · {LADO}×{LADO}\n")

    for src in sorted((ROOT / "libros" / "src").glob("*.json")):
        libro = json.loads(src.read_text())
        pdf = ROOT / "libros" / "dist" / f"{libro['id']}.pdf"
        laminas = {b["x"] for c in libro["capitulos"]
                   for b in c["bloques"] if b.get("t") == "figura"}
        # Se cuenta el archivo entero, cubierta incluida, que es lo que el
        # comprador ve al abrirlo y la cifra que da la ficha de la tienda.
        paginas = len(pdfium.PdfDocument(str(pdf)))
        acento, acento2 = mapa[libro["acento"]]
        html = LIBRO_HTML.format(
            css=css(acento, acento2), acento=acento, rgb1=rgb(acento),
            cubierta=cubierta_png(pdf), paginas=paginas,
            capitulos=len(libro["capitulos"]), laminas=len(laminas))
        png = SALIDA / f"{libro['id']}.png"
        disparar(html, png, guardar_html)
        print(f"    {png.name:30} {paginas:3} pág · "
              f"{len(libro['capitulos']):2} cap · {len(laminas)} lám  {acento}")

    for n in NIVELES:
        pdfs = [p for p in sorted((ROOT / "planes" / "dist").glob("*.pdf"))
                if any(p.name.startswith(d) for d in n["docs"])]
        paginas = sum(len(pdfium.PdfDocument(str(p))) for p in pdfs)
        html = NIVEL_HTML.format(
            css=css(n["acento"], n["acento2"]),
            acento=n["acento"], acento2=n["acento2"], rgb1=rgb(n["acento"]),
            nivel=n["nivel"].upper(), titulo=n["titulo"],
            docs=len(pdfs), palabra="documento" if len(pdfs) == 1 else "documentos",
            paginas=paginas)
        png = SALIDA / f"{n['archivo']}.png"
        disparar(html, png, guardar_html)
        print(f"    {png.name:30} {len(pdfs):3} doc · {paginas} pág")

    print()


if __name__ == "__main__":
    main()
