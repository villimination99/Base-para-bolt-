#!/usr/bin/env python3
"""
VILLUMINATIONS — Exportar a impresión bajo demanda (Printful y compañía)
========================================================================

    python3 ropa/tools/exportar-pod.py                # la lámina modelo
    python3 ropa/tools/exportar-pod.py --todas        # la serie entera
    python3 ropa/tools/exportar-pod.py --previa       # y el montaje para mirar

Un fichero para Printful no es un SVG bonito: es un PNG con **restricciones
físicas**, y un dibujo que se ve perfecto en pantalla puede salir roto de la
plancha. Este fichero es el que traduce de lo uno a lo otro, y las reglas que
hace cumplir vienen de cómo funciona la impresión directa sobre prenda (DTG),
no de un gusto.

Las cinco reglas, y por qué cada una
-------------------------------------
1. **300 ppp al tamaño real de estampación.** A 28 cm de ancho eso son 3307
   píxeles. Menos de 150 ppp se ve pixelado en la prenda; Printful rechaza por
   debajo de su mínimo y avisa entre 150 y 300.

2. **Fondo transparente, sin excepción.** Un PNG con fondo blanco se estampa
   con un recuadro blanco alrededor. Es el fallo más común y el más caro.

3. **Nada de opacidad parcial.** La DTG no hace medias tintas como una
   pantalla: el tramado de un 92 % sale sucio o se pierde. Todo va a opacidad
   1, y `endurecer()` lo fuerza. La lámina de pantalla llevaba el halo al
   0,92 y habría llegado así a la plancha.

4. **Ningún trazo por debajo de 1 mm impreso.** A 300 ppp son 11,8 píxeles.
   La serie llevaba el arco a 2,4 unidades y las marcas de decanato a 1,1, o
   sea 0,67 y 0,31 mm: el arco habría salido débil y **las marcas se habrían
   caído enteras**. Se ve calculándolo, no mirándolo.

5. **Dentro del área de estampación.** El área de espalda de una camiseta
   estándar son 12 × 16 pulgadas. Lo que se salga, se recorta.

El color no sale como en la pantalla
------------------------------------
La DTG sobre prenda oscura imprime primero una base blanca y el color encima.
Esa base **levanta y desatura**: un cian de neón como el `#00f0ff` de la marca
sale pálido y tizoso. Por eso el fichero de impresión no lleva el cian de
pantalla, lleva uno **más hondo** (`CIAN_POD`), para que lo impreso caiga cerca
de lo que la marca es en pantalla.

Esto es compensación, no certeza: cada máquina y cada tela tiran a un lado.
**Antes de una tirada hay que pedir una muestra** y cotejarla. Lo que este
fichero garantiza es lo comprobable —resolución, transparencia, opacidad,
grosor, encaje—; el color exacto lo dice la muestra.
"""

import math
import re
import struct
import subprocess
import sys
import zlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "pod"
sys.path.insert(0, str(Path(__file__).resolve().parent))

PPP = 300                       # puntos por pulgada del fichero de impresión
MM_MINIMO = 1.0                 # trazo mínimo que la DTG sostiene, en mm
AREA_PULGADAS = (12.0, 16.0)    # espalda de camiseta estándar

# --- la paleta de impresión ------------------------------------------------
# El hueso es casi blanco: sobre negro es el máximo contraste que da la base.
# El cian va más hondo que el de pantalla por lo dicho arriba.
HUESO_POD = "#ECEFF6"
CIAN_POD = "#00C4D6"
ACENTOS_POD = {
    "cian": CIAN_POD,
    "purpura": "#6A2ADB",
    "magenta": "#D400BE",
    "hielo": "#8FA6C4",
}

# La lámina modelo: la que se manda a aprobar antes de hacer las demás.
MODELO = ("es-dorsal", "cian", 28.0, "Camiseta negra · espalda")


def _piezas():
    import importlib.util
    ruta = Path(__file__).resolve().parent / "dibujar-espinas.py"
    spec = importlib.util.spec_from_file_location("espinas", ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def px_por_unidad(ancho_cm, ancho_viewbox):
    return (ancho_cm / 2.54 * PPP) / ancho_viewbox


def endurecer(svg: str, escala: float) -> tuple:
    """Aplica las reglas 3 y 4 al contenido, y dice qué tocó.

    No se hace a ojo ni se corrige en el generador: el dibujo de pantalla es
    legítimo como está. Lo que cambia es el destino, y es el destino el que
    impone sus mínimos.
    """
    tocado = []
    # Un 3 % de margen. Endurecer a exactamente el mínimo dejaba el valor en
    # el filo y la comprobación posterior lo rechazaba por redondeo: la guarda
    # se mordía a sí misma.
    minimo_u = (MM_MINIMO * 1.03 / 25.4 * PPP) / escala

    def _op(m):
        tocado.append(f"opacidad {m.group(1)} → 1")
        return 'opacity="1"'
    svg = re.sub(r'opacity="(0\.\d+)"', _op, svg)

    def _sw(m):
        v = float(m.group(1))
        if v >= minimo_u:
            return m.group(0)
        tocado.append(f"trazo {v} → {minimo_u:.2f} u "
                      f"({v * escala / (PPP / 25.4):.2f} mm era menos de "
                      f"{MM_MINIMO} mm)")
        return f'stroke-width="{minimo_u:.2f}"'
    svg = re.sub(r'stroke-width="([\d.]+)"', _sw, svg)
    return svg, tocado


def comprobar(svg: str, W, H, ancho_cm) -> list:
    """Lo que impide mandar un fichero a la estampadora."""
    malos = []
    escala = px_por_unidad(ancho_cm, W)
    ancho_px = ancho_cm / 2.54 * PPP
    alto_px = ancho_px * H / W

    if ancho_px / (ancho_cm / 2.54) < 150:
        malos.append("por debajo de 150 ppp: se vería pixelado en la prenda")
    if ancho_cm / 2.54 > AREA_PULGADAS[0]:
        malos.append(f"{ancho_cm} cm ({ancho_cm / 2.54:.1f}\") no cabe en el "
                     f"área de {AREA_PULGADAS[0]}\" de ancho")
    if alto_px / PPP > AREA_PULGADAS[1]:
        malos.append(f"{alto_px / PPP:.1f}\" de alto no cabe en el área de "
                     f"{AREA_PULGADAS[1]}\"")
    if re.search(r'opacity="0\.\d+"', svg):
        malos.append("queda opacidad parcial: la DTG no hace medias tintas")
    for v in {float(x) for x in re.findall(r'stroke-width="([\d.]+)"', svg)}:
        mm = v * escala / (PPP / 25.4)
        if mm < MM_MINIMO - 0.005:
            malos.append(f"trazo de {mm:.2f} mm: por debajo de {MM_MINIMO} mm "
                         f"se cae en la plancha")
    if "#fff" in svg.lower() or 'fill="white"' in svg.lower():
        malos.append("hay blanco puro declarado: sobre prenda blanca "
                     "desaparece; usa el hueso")
    return malos


# ---------------------------------------------------------------------------
# El PNG y su metadato de densidad
# ---------------------------------------------------------------------------
def sellar_ppp(ruta: Path, ppp: int = PPP) -> None:
    """Escribe el trozo `pHYs` para que el fichero declare sus 300 ppp.

    Sin él, el PNG solo dice cuántos píxeles tiene y quien lo abra decide el
    tamaño físico. Printful lo lee para saber a qué centímetros corresponde la
    imagen, así que un fichero correcto sin `pHYs` puede acabar colocado a otra
    escala. Son nueve bytes de datos y evita esa discusión.

    El trozo va **antes** de `IDAT`, que es lo que manda la norma, y lleva su
    propio CRC-32 sobre el nombre más los datos.
    """
    datos = ruta.read_bytes()
    if b"pHYs" in datos[:2048]:
        return
    ppm = int(round(ppp / 0.0254))                 # píxeles por metro
    cuerpo = struct.pack(">IIB", ppm, ppm, 1)      # 1 = la unidad es el metro
    trozo = (struct.pack(">I", len(cuerpo)) + b"pHYs" + cuerpo
             + struct.pack(">I", zlib.crc32(b"pHYs" + cuerpo) & 0xFFFFFFFF))
    i = datos.index(b"IDAT") - 4
    ruta.write_bytes(datos[:i] + trozo + datos[i:])


def exportar(sid: str, acento: str, ancho_cm: float) -> dict:
    """Saca el PNG de impresión de una pieza. Devuelve el parte."""
    m = _piezas()
    W, H, contenido = m.PIEZAS[sid][0]()
    escala = px_por_unidad(ancho_cm, W)
    contenido, tocado = endurecer(contenido, escala)

    malos = comprobar(contenido, W, H, ancho_cm)
    ancho_px = int(round(ancho_cm / 2.54 * PPP))
    alto_px = int(round(ancho_px * H / W))

    DESTINO.mkdir(parents=True, exist_ok=True)
    base = f"villuminations-{sid.replace('es-', '')}-{acento}"
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{ancho_px}" height="{alto_px}" '
           f'style="--hueso:{HUESO_POD};--acento:{ACENTOS_POD[acento]}">\n'
           f'{contenido}\n</svg>\n')
    (DESTINO / f"{base}.svg").write_text(svg, encoding="utf-8")

    # El PNG se saca con el navegador y **sin fondo**: `omitBackground` es lo
    # que deja el alfa a cero donde no hay tinta. Sin eso el fichero sale con
    # el fondo del navegador y se estampa un recuadro.
    S = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
             "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")
    S.mkdir(parents=True, exist_ok=True)
    (S / "pod.html").write_text(
        f'<!doctype html><meta charset=utf-8>'
        f'<style>html,body{{margin:0;background:transparent}}</style>{svg}',
        encoding="utf-8")
    (S / "pod.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        f"const p = await b.newPage({{viewport:{{width:{ancho_px},"
        f"height:{alto_px}}},deviceScaleFactor:1}});\n"
        f"await p.goto('file://{S}/pod.html');\n"
        f"await p.screenshot({{path:'{DESTINO / (base + '.png')}',"
        f"omitBackground:true}});\n"
        "await b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(S / "pod.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        malos.append(f"no se pudo rasterizar: {r.stderr.strip()[:120]}")
        return {"base": base, "malos": malos, "tocado": tocado}

    png = DESTINO / f"{base}.png"
    sellar_ppp(png)
    return {
        "base": base, "malos": malos, "tocado": tocado,
        "px": (ancho_px, alto_px),
        "cm": (ancho_cm, round(ancho_cm * H / W, 1)),
        "pulgadas": (round(ancho_px / PPP, 2), round(alto_px / PPP, 2)),
        "kb": png.stat().st_size // 1024,
    }


def ficha(p: dict, sid: str, acento: str, prenda: str) -> str:
    """La hoja de especificación que se sube con el fichero.

    Una app de impresión bajo demanda pide colocación y tamaño aparte del
    dibujo. Escribirlo aquí y no en un correo evita que la segunda tirada salga
    a otro tamaño que la primera.
    """
    return f"""# {p['base']}

| Campo | Valor |
|---|---|
| Prenda | {prenda} |
| Colocación | Espalda, centrada, a 8 cm por debajo del cuello |
| Tamaño impreso | {p['cm'][0]} × {p['cm'][1]} cm  ({p['pulgadas'][0]}" × {p['pulgadas'][1]}") |
| Fichero | {p['px'][0]} × {p['px'][1]} px · {PPP} ppp · PNG con alfa |
| Área de la prenda | {AREA_PULGADAS[0]}" × {AREA_PULGADAS[1]}" |
| Tinta hueso | `{HUESO_POD}` |
| Tinta acento | `{ACENTOS_POD[acento]}` ({acento}) |
| Método | Impresión directa sobre prenda (DTG) |

**El color de pantalla no es el color impreso.** La base blanca que la DTG pone
debajo levanta y desatura, así que el fichero lleva un acento más hondo que el
de la marca para que lo impreso caiga cerca. **Pedir una muestra y cotejarla
antes de cualquier tirada.**

Trazo mínimo del fichero: {MM_MINIMO} mm. Por debajo, la plancha lo pierde.
"""


def main() -> int:
    piezas = _piezas()
    if "--todas" in sys.argv:
        trabajos = [(sid, "cian", 28.0 if sid == "es-dorsal" else 11.0
                     if sid == "es-pecho" else 9.0)
                    for sid in piezas.PIEZAS]
    else:
        trabajos = [(MODELO[0], MODELO[1], MODELO[2])]

    print(f"\n  IMPRESIÓN BAJO DEMANDA · {PPP} ppp · mínimo {MM_MINIMO} mm\n")
    fallos = 0
    for sid, acento, ancho in trabajos:
        p = exportar(sid, acento, ancho)
        print(f"  {p['base']}")
        for t in dict.fromkeys(p["tocado"]):
            print(f"      endurecido · {t}")
        if p["malos"]:
            fallos += 1
            for mal in p["malos"]:
                print(f"      NO SE PUEDE MANDAR · {mal}")
            continue
        print(f"      {p['px'][0]} × {p['px'][1]} px  ·  "
              f"{p['cm'][0]} × {p['cm'][1]} cm  ·  {p['kb']} KB")
        if (sid, acento) == (MODELO[0], MODELO[1]):
            (DESTINO / f"{p['base']}.md").write_text(
                ficha(p, sid, acento, MODELO[3]), encoding="utf-8")
            print(f"      ficha de especificación · {p['base']}.md")
        print()
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
