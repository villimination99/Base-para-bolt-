#!/usr/bin/env python3
"""
VILLUMINATIONS — Maquetas de prenda para la tienda y los anuncios
=================================================================

    python3 ropa/tools/maqueta.py            # las maquetas en ropa/maquetas/
    python3 ropa/tools/maqueta.py --una      # solo la dorsal, para mirar

Qué es esto y qué NO es
-----------------------
**No es una fotografía y no pretende serlo.** Printful genera maquetas
fotográficas solas a partir del fichero de impresión, gratis y con la prenda
real: para la ficha de producto, esas son mejores y hay que usarlas.

Esto es lo otro, lo que Printful no da: **la composición de marca**. Prenda
sobre fondo, encuadre plano, la lámina a su tamaño real y el aire alrededor
que hace que parezca una marca y no un catálogo de imprenta. Es lo que se pone
en un anuncio, en una publicación y en la cabecera de la colección, y es lo
único de esta cadena que distingue una tienda de otra que vende el mismo
producto del mismo proveedor.

Por qué el estampado no se pega encima y ya
-------------------------------------------
Una lámina pegada sobre un dibujo de camiseta se ve pegada: flota. Aquí pasa
por tres cosas que la meten dentro de la tela:

1. **La sombra va encima, no debajo.** Los pliegues se pintan como una capa
   de degradados por encima del conjunto, de modo que oscurecen prenda y
   tinta a la vez y **atraviesan** el estampado, que es lo que hace la tela
   de verdad. Una lámina pegada encima de todo se ve pegada.
2. **La tinta va en normal, no en `screen`.** La primera versión la ponía en
   `screen` por lo mismo —para que los pliegues la atravesaran—, pero eso ya
   lo hace la capa de sombra de arriba, así que `screen` solo sumaba: sumaba
   el tono de la tela al de la tinta y **aclaraba todos los acentos oscuros**.
   El rojo cardenal `#BC1733` salía en la maqueta como `#C63A57`, o sea
   frambuesa, y la maqueta enseñaba un color que la plancha no imprime. Con
   la tinta en normal, lo que se ve es el valor del fichero.
3. **La lámina va a su tamaño real**, calculado desde los centímetros de
   `exportar-pod.COLOCACION`, no a ojo. Una maqueta con el estampado más
   grande de lo que se imprime es publicidad engañosa barata.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "maquetas"
S = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
         "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")


def _pod():
    spec = importlib.util.spec_from_file_location(
        "pod", Path(__file__).resolve().parent / "exportar-pod.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# Prenda: ancho de pecho y alto en cm, y los tonos de la tela.
#
# UN NEGRO FOTOGRAFIADO NO ES NEGRO. Una camiseta negra en una foto de catálogo
# cae entre #1c1c20 y #2e2e36, con brillos hasta #3a3a44. En la primera pasada
# la tela iba a #141419 sobre fondo #07070a y la prenda desaparecía: no se veía
# la silueta, solo el estampado flotando en el vacío.
PRENDAS = {
    "camiseta": {"w": 52, "h": 72, "tono": "#26262d", "sombra": "#15151a",
                 "brillo": "#3a3a44", "nombre": "Camiseta"},
    "sudadera": {"w": 60, "h": 70, "tono": "#222229", "sombra": "#131318",
                 "brillo": "#34343d", "nombre": "Sudadera"},
}

# Fondo claro, como las composiciones del género. El contraste lo pone la
# prenda oscura contra él, no el estampado contra la prenda.
FONDO = "#ececed"

# A qué altura de la prenda empieza el área de estampación, en centímetros
# bajo el cuello. Es lo único que la maqueta pone de su parte: el fichero de
# impresión mide desde el borde del área y no tiene por qué saber dónde cae
# ese borde sobre la tela. Es aproximado y depende del modelo.
AREA_BAJO_CUELLO = {"espalda": 5.0, "frontal": 5.0, "manga": 0.0,
                    "pierna": 0.0}


def _tela(W, H, tipo, p):
    """La silueta, con el degradado de volumen ya dentro del relleno."""
    h, c = W * 0.19, W * 0.115
    cuello = (f'<ellipse cx="{W/2}" cy="{H*0.075}" rx="{W*0.155}" '
              f'ry="{H*0.052}" fill="{p["sombra"]}"/>' if tipo == "sudadera"
              else "")
    cuerpo = (f'M{h},{H*.07} L{W/2-c},{H*.035} Q{W/2},{H*.105} {W/2+c},{H*.035} '
              f'L{W-h},{H*.07} L{W},{H*.34} L{W-h*.72},{H*.40} '
              f'L{W-h*.80},{H} L{h*.80},{H} L{h*.72},{H*.40} L0,{H*.34} Z')
    return f"""<path d="{cuerpo}" fill="#000" opacity="0.13"
   transform="translate({W*0.012},{H*0.012})" filter="url(#difuso)"/>
{cuello}
<path d="{cuerpo}" fill="url(#cuerpo)"/>
<path d="{cuerpo}" fill="url(#canto)" opacity="0.85"/>
<path d="M{W/2-c*1.25},{H*.045} Q{W/2},{H*.118} {W/2+c*1.25},{H*.045}
 L{W/2+c},{H*.030} Q{W/2},{H*.100} {W/2-c},{H*.030} Z" fill="{p['brillo']}"
 opacity="0.55"/>"""


def _pliegues(W, H, p):
    """Los pliegues: líneas suaves, no manchas.

    La primera versión ponía tres elipses enormes en `multiply` con un
    degradado radial de blanco a gris: sobre la prenda salían como dos óvalos
    negros gigantes que se comían la silueta. Un pliegue es una línea de sombra
    de unos pocos centímetros, no media prenda.
    """
    lineas = []
    for i, (x, y, w, alto, rot, op) in enumerate((
            (0.30, 0.55, 0.030, 0.30, -6, 0.30),
            (0.70, 0.58, 0.026, 0.27, 7, 0.28),
            (0.38, 0.80, 0.022, 0.16, -3, 0.22),
            (0.63, 0.76, 0.020, 0.18, 4, 0.20))):
        lineas.append(
            f'<ellipse cx="{W*x}" cy="{H*y}" rx="{W*w}" ry="{H*alto}" '
            f'fill="{p["sombra"]}" opacity="{op}" filter="url(#difuso)" '
            f'transform="rotate({rot} {W*x} {H*y})"/>')
    return "".join(lineas)


def maqueta(sid, acento, prenda="camiseta", px=13.0) -> str:
    pod = _pod()
    esp = pod._piezas()
    area, ancho_cm, x_frac, y_cm, _pr = pod.COLOCACION[sid]
    pw, ph, cont = esp.PIEZAS[sid][0]()
    cont, _ = pod.endurecer(cont, (ancho_cm / 2.54 * pod.PPP) / pw)
    cont = (cont.replace("var(--acento)", pod.ACENTOS_POD[acento])
                .replace("var(--hueso)", pod.HUESO_POD))

    p = PRENDAS[prenda]
    # La prenda va DENTRO de un lienzo mayor. Sin margen la camiseta se salía
    # del encuadre por abajo y por los lados, que es el error de encuadre más
    # visible que puede tener una foto de producto.
    MARGEN = 0.10
    W, H = p["w"] * px, p["h"] * px
    LW, LH = W * (1 + MARGEN * 2), H * (1 + MARGEN * 2)
    ox, oy = W * MARGEN, H * MARGEN
    ancho = ancho_cm * px
    # La maqueta coloca la lámina donde la coloca el fichero de impresión, y
    # no con sus propios números: si los dos sitios tuvieran su constante,
    # llegaría el día en que la maqueta enseña un estampado en un sitio y la
    # prenda sale con él en otro. Lo único que la maqueta añade es a qué
    # altura de la prenda empieza el área de estampación, que el fichero no
    # sabe porque es cosa del producto.
    x = (W - ancho) / 2 + (x_frac - 0.5) * pod.AREAS[area][0] * px
    y = H * 0.07 + (AREA_BAJO_CUELLO[area] + y_cm) * px

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LW} {LH}"
 width="{int(LW)}" height="{int(LH)}">
<defs>
 <linearGradient id="cuerpo" x1="0" y1="0" x2="1" y2="0.25">
  <stop offset="0" stop-color="{p['sombra']}"/>
  <stop offset="0.30" stop-color="{p['tono']}"/>
  <stop offset="0.55" stop-color="{p['brillo']}"/>
  <stop offset="0.75" stop-color="{p['tono']}"/>
  <stop offset="1" stop-color="{p['sombra']}"/>
 </linearGradient>
 <linearGradient id="canto" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{p['brillo']}" stop-opacity="0.45"/>
  <stop offset="0.45" stop-color="{p['tono']}" stop-opacity="0"/>
  <stop offset="1" stop-color="{p['sombra']}" stop-opacity="0.55"/>
 </linearGradient>
 <filter id="difuso" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur stdDeviation="{W*0.02}"/></filter>
</defs>
<rect width="{LW}" height="{LH}" fill="{FONDO}"/>
<g transform="translate({ox},{oy})">
{_tela(W, H, prenda, p)}
<g transform="translate({x},{y}) scale({ancho/pw})">{cont}</g>
{_pliegues(W, H, p)}
</g>
</svg>"""


# ---------------------------------------------------------------------------
# Qué se genera. Se deja explícito y no en un bucle sobre todo: una tienda con
# dieciséis fichas del mismo dibujo se lee como un catálogo de imprenta, no
# como una marca.
# ---------------------------------------------------------------------------
CATALOGO = [
    ("es-dorsal", "cardenal", "camiseta"),
    ("es-dorsal", "cian", "camiseta"),
    ("es-dorsal", "oro", "camiseta"),
    ("es-dorsal", "hielo", "camiseta"),
    ("es-dorsal", "purpura", "sudadera"),
    ("es-dorsal", "magenta", "camiseta"),
    ("es-pecho", "cardenal", "camiseta"),
    ("es-pecho", "cian", "camiseta"),
    ("es-pecho", "hielo", "camiseta"),
]


def rasterizar(trabajos, ancho=1400) -> int:
    """Pasa los SVG a PNG con el navegador, a resolución de tienda."""
    S.mkdir(parents=True, exist_ok=True)
    DESTINO.mkdir(parents=True, exist_ok=True)
    lineas = []
    for sid, acento, prenda in trabajos:
        base = f"maqueta-{sid.replace('es-','')}-{acento}-{prenda}"
        svg = maqueta(sid, acento, prenda)
        (S / f"{base}.html").write_text(
            f'<!doctype html><meta charset=utf-8>'
            f'<style>html,body{{margin:0;background:#07070a}}'
            f'svg{{display:block;width:{ancho}px;height:auto}}</style>{svg}',
            encoding="utf-8")
        lineas.append(
            f"{{const p = await b.newPage({{viewport:{{width:{ancho},"
            f"height:{int(ancho * 1.45)}}},deviceScaleFactor:2}});"
            f"await p.goto('file://{S}/{base}.html');"
            f"const el = await p.$('svg');"
            f"await el.screenshot({{path:'{DESTINO}/{base}.png'}});}}")
    (S / "maq.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        + "\n".join(lineas) + "\nawait b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(S / "maq.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        print(f"    no se pudo rasterizar:\n{r.stderr[:300]}")
        return 1
    return 0


def main() -> int:
    trabajos = CATALOGO[:1] if "--una" in sys.argv else CATALOGO
    print(f"\n  MAQUETAS DE PRENDA · {len(trabajos)}\n")
    if rasterizar(trabajos):
        return 1
    for sid, acento, prenda in trabajos:
        f = DESTINO / f"maqueta-{sid.replace('es-','')}-{acento}-{prenda}.png"
        print(f"    {f.name:46} {f.stat().st_size // 1024:>4} KB")
    print(f"\n    Para la FICHA de producto usa las de Printful, que salen de\n"
          f"    la prenda real. Estas son para anuncio, publicación y cabecera\n"
          f"    de colección, que es lo que Printful no da.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
