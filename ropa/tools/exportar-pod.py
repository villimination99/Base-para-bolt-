#!/usr/bin/env python3
"""
VILLUMINATIONS — Exportar a impresión bajo demanda (Printful y compañía)
========================================================================

    python3 ropa/tools/exportar-pod.py                # la lámina modelo
    python3 ropa/tools/exportar-pod.py --todas        # la serie entera
    python3 ropa/tools/exportar-pod.py --medir        # y mide el ráster

Un fichero para Printful no es un SVG bonito: es un PNG con **restricciones
físicas**, y un dibujo que se ve perfecto en pantalla puede salir roto de la
plancha. Este fichero es el que traduce de lo uno a lo otro, y las reglas que
hace cumplir vienen de cómo funciona la impresión directa sobre prenda (DTG),
no de un gusto.

El lienzo ES el área de estampación
-----------------------------------
Esta es la regla que costó una tirada mal escalada, y es la que manda sobre
todas las demás. La primera versión sacaba el fichero **al tamaño del dibujo**:
la pieza de pecho salía a 9 cm, o sea 1063 píxeles. Al subirla, la aplicación
la encaja en su área de estampación —30,5 × 40,6 cm en el frente de una
camiseta— y al estirar 1063 píxeles a 30,5 cm quedan 88 ppp, así que avisa de
resolución insuficiente y hay que **encogerla a mano hasta que deje de
avisar**. Eso no es un fichero, es una negociación, y la segunda tirada sale a
otro tamaño que la primera porque nadie apuntó a cuánto se encogió.

Ahora el PNG mide **exactamente el área de estampación a 300 ppp** y el dibujo
va dentro, a su tamaño y en su sitio, con transparencia alrededor. Encajar al
área —que es lo que la aplicación hace sola— deja el dibujo donde tiene que
estar y a 300 ppp exactos. No hay nada que escalar y no hay nada que recordar.

Las reglas, y por qué cada una
------------------------------
1. **300 ppp sobre el área completa.** Por lo de arriba. Deja de ser una
   propiedad del dibujo y pasa a ser una propiedad del fichero.

2. **Fondo transparente, sin excepción.** Un PNG con fondo blanco se estampa
   con un recuadro blanco alrededor. Es el fallo más común y el más caro.

3. **Nada de opacidad parcial declarada.** La DTG no hace medias tintas como
   una pantalla: el tramado de un 92 % sale sucio o se pierde. Todo va a
   opacidad 1, y `endurecer()` lo fuerza. (El antialiasing del borde es otra
   cosa y sí hace falta: es lo que le da el filo a la curva.)

4. **Ningún rasgo por debajo de 1 mm impreso.** A 300 ppp son 11,8 píxeles.
   Y **no basta con mirar los `stroke-width`**: la serie espina está hecha de
   cintas rellenas, que no son trazos, así que la comprobación por atributo no
   veía el 90 % del dibujo. Por eso `medir()` abre el ráster y mide el grosor
   de verdad, píxel a píxel.

5. **El hueco también tiene un mínimo.** Dos nervios a medio milímetro se
   empastan en la plancha y salen como una mancha. Un dibujo puede tener todos
   los rasgos por encima del mínimo y aun así imprimirse cerrado; el hueco es
   una medida distinta y se mide aparte.

El color no sale como en la pantalla
------------------------------------
La DTG sobre prenda oscura imprime primero una base blanca y el color encima.
Esa base **levanta y desatura**: un cian de neón como el `#00f0ff` de la marca
sale pálido y tizoso. Por eso el fichero de impresión no lleva el color de
pantalla, lleva uno **más hondo**.

Y no se retecléa a mano: se **deriva** del color de pantalla con `_compensar()`,
que baja el valor un 16 % y deja el tono y la saturación donde estaban. La
regla no es un invento nuevo: reproduce, dentro de dos o tres pasos, los tres
acentos que ya se habían ajustado a ojo antes de que existiera, y por eso se
puede confiar en ella para los que vengan. Un acento nuevo se añade una sola
vez, en el dibujo, y aquí sale solo.

**El hueso es la excepción y va al revés.** No se compensa hacia abajo: se
empuja hacia arriba, porque la base blanca levantándolo es justo lo que se
quiere de él. El hueso es quien pone el contraste contra la prenda negra; el
acento solo asoma por el canto. Compensar los dos igual sería aplicar la regla
sin mirar para qué está cada tinta.

Esto es compensación, no certeza: cada máquina y cada tela tiran a un lado.
**Antes de una tirada hay que pedir una muestra** y cotejarla. Lo que este
fichero garantiza es lo comprobable —resolución, transparencia, opacidad,
grosor, hueco, encaje—; el color exacto lo dice la muestra.
"""

import colorsys
import json
import re
import struct
import subprocess
import sys
import zlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "pod"
sys.path.insert(0, str(Path(__file__).resolve().parent))
SCRATCH = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
               "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")

PPP = 300                       # puntos por pulgada del fichero de impresión
MM_MINIMO = 1.0                 # rasgo mínimo que la DTG sostiene, en mm
HUECO_MINIMO = 0.9              # hueco mínimo antes de que se empaste, en mm

# Cuánta tinta puede quedar por debajo del mínimo sin que sea un problema.
# No puede ser cero: **toda cinta acaba en punta**, y una punta pasa por todos
# los grosores hasta el cero antes de terminarse. Una punta que se desvanece
# es correcta en DTG; lo que no lo es son nervios largos y finos de punta a
# punta. El umbral separa una cosa de la otra y está puesto por encima de lo
# que mide la serie tal como está, para que muerda cuando algo se adelgace de
# verdad y no cada vez que se dibuja una espina.
# Medido sobre la serie tal como está: la tinta fina va del 0,98 % de la
# dorsal al 1,60 % de la manga, y el hueco fino del 0,73 % al 1,15 %. Los
# umbrales están puestos a dos veces y media el peor, que es holgura de sobra
# para dibujar y sigue mordiendo si algún día la filigrana se adelgaza.
FINO_MAXIMO = 0.04              # fracción de la tinta en rasgos < MM_MINIMO
HUECO_MAXIMO = 0.03             # fracción del hueco interior < HUECO_MINIMO

# El área de estampación NO es la misma en toda la prenda, y darle a todas la
# de la espalda es la manera de mandar a producción una lámina que no cabe.
# Estas son las zonas estándar de un catálogo de impresión bajo demanda, en
# centímetros. Antes de una tirada **hay que cotejarlas con el producto
# concreto**: varían entre modelos y el catálogo las publica una por una.
#
# Ojo con «pecho»: en DTG no existe como área propia. El pecho es un dibujo
# pequeño **dentro del área frontal**, y por eso su lienzo es el frontal
# entero. Tratarlo como un área de 10 × 10 cm es exactamente lo que producía
# el aviso de resolución.
AREAS = {
    "espalda":  (30.5, 40.6, "Espalda · 12″ × 16″"),
    "frontal":  (30.5, 40.6, "Frente · 12″ × 16″"),
    "manga":    (10.0, 40.0, "Manga de sudadera"),
    "pierna":   (24.0, 30.0, "Pernera de pantalón de chándal"),
}

# pieza -> (área, ancho impreso en cm, centro en x como fracción del área,
#           borde superior en cm desde arriba del área, prenda)
#
# El centro en x va a 0,5 en todas **a propósito**. Un pecho descentrado se
# puede poner, pero el lado no se deduce del fichero: en la industria «pecho
# izquierdo» se coloca unas veces a la izquierda de lo que se ve y otras a la
# del que lleva la prenda, que son lados contrarios. Centrado no tiene lado
# que equivocar, y si algún día se decide descentrarlo es esta constante y
# nada más.
COLOCACION = {
    "es-dorsal": ("espalda", 28.0, 0.5, 2.5, "Camiseta negra"),
    "es-pecho":  ("frontal", 9.0, 0.5, 6.0, "Camiseta negra"),
    "es-manga":  ("manga", 8.0, 0.5, 6.0, "Sudadera negra"),
    # La pernera iba a 10 cm de ancho y 4 del borde: 26,2 + 4 son 30,2 en un
    # área de 30, o sea que se salía por abajo por dos milímetros. Lo cazó la
    # guarda de encaje en la primera pasada. A 9,2 cm quedan casi tres de
    # margen por arriba y por abajo, que es lo que hace falta cuando el área
    # del producto concreto resulte ser un poco menor que la del catálogo.
    "es-pierna": ("pierna", 9.2, 0.5, 3.0, "Pantalón de chándal negro"),
}

# --- la paleta de impresión ------------------------------------------------
# El hueso va MÁS CLARO que en pantalla, no más oscuro: es quien tiene que
# contrastar con la prenda negra y la base blanca que lo levanta juega a su
# favor. Los acentos van al revés y salen de `_compensar()`.
HUESO_POD = "#ECEFF6"
BAJADA = 0.84                   # cuánto se baja el valor de un acento vivo
VIVO = 0.85                     # de este valor para arriba se compensa

# Los acentos que se sacan a impresión, del catálogo de pantalla. No están
# todos: seis colores ya son veinticuatro ficheros, y el problema de un
# catálogo de ropa no es tener pocos colores sino repartir la atención entre
# demasiados.
ACENTOS = ("cian", "cardenal", "oro", "purpura", "magenta", "hielo")

# Cómo se comporta cada tinta en la plancha. Se dice por color en su ficha
# porque no es lo mismo un cian, que la base sostiene bien, que un rojo o un
# oro, que son los dos que más se mueven entre la pantalla y la tela.
NOTA_TINTA = {
    "cian": "El cian es de los que mejor aguantan la base blanca. Aun así "
            "sale un punto más claro que en pantalla.",
    "cardenal": "El rojo es la tinta que más se mueve en DTG: la base blanca "
                "lo tira a rosa. El fichero va más hondo de lo que se quiere "
                "ver; la muestra es aquí más necesaria que en ningún otro.",
    "oro": "El oro no es un color de tinta, es un amarillo cálido: no brilla, "
           "no es metálico y sobre negro sale más apagado de lo que parece "
           "en pantalla.",
    "purpura": "El púrpura se sostiene bien, pero pierde el filo del violeta "
               "y tira a azul.",
    "magenta": "El magenta es el más vivo de la serie sobre prenda negra y "
               "casi no pierde saturación.",
    "hielo": "El hielo es casi neutro, así que la base apenas lo cambia: es "
             "el más predecible de los seis.",
}

# La lámina modelo: la que se manda a aprobar antes de hacer las demás.
MODELO = ("es-dorsal", "cian")


def _compensar(hexa: str) -> str:
    """Baja el valor de un color vivo para que la base blanca no lo lave.

    Tono y saturación se quedan donde están: lo que la base hace es levantar,
    no girar. Por debajo de `VIVO` la tinta ya es honda y la base la mueve
    mucho menos, así que se deja tal cual antes que oscurecer por sistema un
    color que no lo necesita.
    """
    r, g, b = (int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    if v < VIVO:
        return hexa.upper()
    r, g, b = colorsys.hsv_to_rgb(h, s, v * BAJADA)
    return "#%02X%02X%02X" % tuple(round(c * 255) for c in (r, g, b))


def _piezas():
    import importlib.util
    ruta = Path(__file__).resolve().parent / "dibujar-espinas.py"
    spec = importlib.util.spec_from_file_location("espinas", ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ACENTOS_POD = {c: _compensar(_piezas().ACENTOS[c]) for c in ACENTOS}


def px(cm: float) -> int:
    return int(round(cm / 2.54 * PPP))


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


def comprobar(svg: str, W, H, ancho_cm, area, x_frac, y_cm) -> list:
    """Lo que impide mandar un fichero a la estampadora."""
    malos = []
    escala = (ancho_cm / 2.54 * PPP) / W
    alto_cm = ancho_cm * H / W
    area_w, area_h, area_n = AREAS[area]

    if ancho_cm > area_w:
        malos.append(f"{ancho_cm} cm de ancho no cabe en {area_n} "
                     f"({area_w} cm)")
    izq = area_w * x_frac - ancho_cm / 2
    if izq < -0.01 or izq + ancho_cm > area_w + 0.01:
        malos.append(f"colocado en x={x_frac} se sale del área por el lado")
    if y_cm + alto_cm > area_h + 0.01:
        malos.append(f"{alto_cm:.1f} cm de alto a {y_cm} cm del borde no cabe "
                     f"en {area_n} ({area_h} cm de alto)")
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


# ---------------------------------------------------------------------------
# Medir el ráster: el grosor de verdad, no el declarado
# ---------------------------------------------------------------------------
# Esto es lo que la comprobación por atributos no podía hacer. La serie espina
# está hecha de **cintas rellenas** —siluetas calculadas, no trazos—, así que
# `stroke-width` no dice nada del 90 % del dibujo. Aquí se rasteriza y se mide
# píxel a píxel: para cada punto de tinta, el grosor local es el menor de su
# recorrido horizontal y su recorrido vertical, que es la manera barata y
# estable de estimar la anchura de una forma sin saber su geometría.
#
# El hueco se mide igual pero al revés, y solo cuenta el **interior**: un claro
# con tinta a los dos lados. El que toca el borde del lienzo no es un hueco del
# dibujo, es el aire de alrededor.
#
# Lo que se vigila es la **fracción**, no el mínimo. El hueco más estrecho sale
# siempre en torno a un píxel porque en algún cruce dos cintas se rozan, y eso
# no es un defecto: es un empalme. Convertir ese mínimo en guarda haría abortar
# cualquier dibujo con dos nervios que se tocan, que son todos. Se imprime para
# poder mirarlo, y nada más.
MEDIDOR = r"""
async ({svg, W, H, min_px, hueco_px}) => {
  const url = URL.createObjectURL(new Blob([svg], {type: 'image/svg+xml'}));
  const img = new Image();
  img.src = url; await img.decode();
  const c = new OffscreenCanvas(W, H), x = c.getContext('2d', {willReadFrequently: true});
  x.drawImage(img, 0, 0, W, H);
  const d = x.getImageData(0, 0, W, H).data;
  const N = W * H, tinta = new Uint8Array(N);
  let n_tinta = 0;
  for (let i = 0, j = 3; i < N; i++, j += 4) if (d[j] >= 128) { tinta[i] = 1; n_tinta++; }
  if (!n_tinta) return {error: 'el ráster salió vacío'};

  // recorrido horizontal y vertical de cada píxel, dentro de su propia clase
  const rh = new Uint16Array(N), rv = new Uint16Array(N);
  const borde_h = new Uint8Array(N), borde_v = new Uint8Array(N);
  for (let y = 0; y < H; y++) {
    let i = y * W;
    while (i < (y + 1) * W) {
      const v = tinta[i]; let j = i;
      while (j < (y + 1) * W && tinta[j] === v) j++;
      const L = Math.min(j - i, 65535), toca = (i === y * W) || (j === (y + 1) * W);
      for (let k = i; k < j; k++) { rh[k] = L; borde_h[k] = toca ? 1 : 0; }
      i = j;
    }
  }
  for (let X = 0; X < W; X++) {
    let i = X;
    while (i < N) {
      const v = tinta[i]; let j = i;
      while (j < N && tinta[j] === v) j += W;
      const L = Math.min((j - i) / W, 65535), toca = (i === X) || (j >= N);
      for (let k = i; k < j; k += W) { rv[k] = L; borde_v[k] = toca ? 1 : 0; }
      i = j;
    }
  }

  let finos = 0, hueco_n = 0, hueco_fino = 0, hueco_min = 1e9;
  let x0 = W, y0 = H, x1 = 0, y1 = 0;
  for (let i = 0; i < N; i++) {
    const g = Math.min(rh[i], rv[i]);
    if (tinta[i]) {
      if (g < min_px) finos++;
      const px_ = i % W, py = (i / W) | 0;
      if (px_ < x0) x0 = px_; if (px_ > x1) x1 = px_;
      if (py < y0) y0 = py; if (py > y1) y1 = py;
    } else {
      // interior: al menos un eje cerrado por tinta a los dos lados
      const gh = borde_h[i] ? 1e9 : rh[i], gv = borde_v[i] ? 1e9 : rv[i];
      const gi = Math.min(gh, gv);
      if (gi < 1e9) {
        hueco_n++;
        if (gi < hueco_px) hueco_fino++;
        if (gi < hueco_min) hueco_min = gi;
      }
    }
  }
  const caja = (x1 - x0 + 1) * (y1 - y0 + 1);
  return {
    tinta: n_tinta,
    cobertura: n_tinta / caja,
    finos: finos / n_tinta,
    huecos: hueco_n ? hueco_fino / hueco_n : 0,
    hueco_min: hueco_min < 1e9 ? hueco_min : null,   // informativo, no guarda
  };
}
"""


def exportar(sid: str, acento: str, medir: bool = False) -> dict:
    """Saca el PNG de impresión de una pieza. Devuelve el parte."""
    area, ancho_cm, x_frac, y_cm, prenda = COLOCACION[sid]
    area_w, area_h, area_n = AREAS[area]
    m = _piezas()
    W, H, contenido = m.PIEZAS[sid][0]()
    escala = (ancho_cm / 2.54 * PPP) / W
    contenido, tocado = endurecer(contenido, escala)
    malos = comprobar(contenido, W, H, ancho_cm, area, x_frac, y_cm)

    alto_cm = ancho_cm * H / W
    izq_cm = area_w * x_frac - ancho_cm / 2
    lienzo_w, lienzo_h = px(area_w), px(area_h)
    dis_w, dis_h = px(ancho_cm), px(alto_cm)

    DESTINO.mkdir(parents=True, exist_ok=True)
    base = f"villuminations-{sid.replace('es-', '')}-{acento}"
    tintas = f"--hueso:{HUESO_POD};--acento:{ACENTOS_POD[acento]}"

    # El dibujo solo, a su tamaño: es lo que se mide y lo que se coloca.
    solo = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{dis_w}" height="{dis_h}" style="{tintas}">\n'
            f'{contenido}\n</svg>\n')

    # El fichero de impresión: el lienzo es el área, el dibujo va dentro.
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="0 0 {lienzo_w} {lienzo_h}" '
           f'width="{lienzo_w}" height="{lienzo_h}" style="{tintas}">\n'
           f'  <g transform="translate({px(izq_cm)},{px(y_cm)}) '
           f'scale({dis_w / W:.6f})">\n{contenido}\n  </g>\n</svg>\n')
    (DESTINO / f"{base}.svg").write_text(svg, encoding="utf-8")

    # El PNG se saca con el navegador y **sin fondo**: `omitBackground` es lo
    # que deja el alfa a cero donde no hay tinta. Sin eso el fichero sale con
    # el fondo del navegador y se estampa un recuadro.
    SCRATCH.mkdir(parents=True, exist_ok=True)
    (SCRATCH / "pod.html").write_text(
        f'<!doctype html><meta charset=utf-8>'
        f'<style>html,body{{margin:0;background:transparent}}</style>{svg}',
        encoding="utf-8")
    (SCRATCH / "solo.svg").write_text(solo, encoding="utf-8")
    (SCRATCH / "pod.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "import { readFileSync } from 'node:fs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        f"const p = await b.newPage({{viewport:{{width:{lienzo_w},"
        f"height:{lienzo_h}}},deviceScaleFactor:1}});\n"
        f"await p.goto('file://{SCRATCH}/pod.html');\n"
        f"await p.screenshot({{path:'{DESTINO / (base + '.png')}',"
        f"omitBackground:true}});\n"
        + (f"const svg = readFileSync('{SCRATCH}/solo.svg','utf8');\n"
           f"const m = await p.evaluate({MEDIDOR}, {{svg, W:{dis_w}, "
           f"H:{dis_h}, min_px:{MM_MINIMO / 25.4 * PPP:.3f}, "
           f"hueco_px:{HUECO_MINIMO / 25.4 * PPP:.3f}}});\n"
           "console.log('MEDIDA ' + JSON.stringify(m));\n" if medir else "")
        + "await b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(SCRATCH / "pod.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        malos.append(f"no se pudo rasterizar: {r.stderr.strip()[:160]}")
        return {"base": base, "malos": malos, "tocado": tocado}

    medida = None
    for linea in r.stdout.splitlines():
        if linea.startswith("MEDIDA "):
            medida = json.loads(linea[7:])
    if medida:
        if medida.get("error"):
            malos.append(medida["error"])
        else:
            if medida["finos"] > FINO_MAXIMO:
                malos.append(
                    f"{medida['finos']:.0%} de la tinta está en rasgos de "
                    f"menos de {MM_MINIMO} mm (máximo {FINO_MAXIMO:.0%}): "
                    f"buena parte del dibujo se caería de la plancha")
            if medida["huecos"] > HUECO_MAXIMO:
                malos.append(
                    f"{medida['huecos']:.0%} del hueco interior mide menos de "
                    f"{HUECO_MINIMO} mm (máximo {HUECO_MAXIMO:.0%}): se "
                    f"empastaría y saldría como mancha")

    png = DESTINO / f"{base}.png"
    sellar_ppp(png)
    return {
        "base": base, "malos": malos, "tocado": tocado, "medida": medida,
        "lienzo": (lienzo_w, lienzo_h), "dibujo": (dis_w, dis_h),
        "cm": (round(ancho_cm, 1), round(alto_cm, 1)),
        "pulgadas": (round(dis_w / PPP, 2), round(dis_h / PPP, 2)),
        "sitio": (round(izq_cm, 1), round(y_cm, 1)),
        "kb": png.stat().st_size // 1024, "area": area,
    }


def verificar(png: Path, lienzo=None) -> list:
    """Abre el PNG escrito y comprueba lo que se ha prometido de él.

    No basta con haberlo pedido: hay que mirar el fichero. Se decodifica la
    primera fila de píxeles de verdad —descomprimiendo y deshaciendo el filtro
    del PNG— porque el fondo transparente es el fallo más caro de este flujo y
    un metadato no prueba nada sobre los píxeles.
    """
    d = png.read_bytes()
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        return ["no es un PNG"]
    malos, i, idat, ancho, alto, color, tiene_phys = [], 8, b"", 0, 0, None, 0
    while i < len(d):
        n = struct.unpack(">I", d[i:i + 4])[0]
        t = d[i + 4:i + 8]
        if t == b"IHDR":
            ancho, alto, _p, color = struct.unpack(">IIBB", d[i + 8:i + 18])
        elif t == b"pHYs":
            ppm = struct.unpack(">I", d[i + 8:i + 12])[0]
            tiene_phys = True
            if abs(ppm * 0.0254 - PPP) > 1:
                malos.append(f"declara {ppm * 0.0254:.0f} ppp y no {PPP}")
        elif t == b"IDAT":
            idat += d[i + 8:i + 8 + n]
        elif t == b"IEND":
            break
        i += 12 + n

    if color != 6:
        malos.append("no tiene canal alfa: se estamparía con recuadro")
        return malos
    if not tiene_phys:
        malos.append("sin pHYs: quien lo abra decidirá el tamaño físico")
    # El lienzo tiene que ser el área. Si no lo es, la aplicación volverá a
    # pedir que se escale a mano y estamos donde estábamos.
    if lienzo and (ancho, alto) != tuple(lienzo):
        malos.append(f"el lienzo mide {ancho} × {alto} y el área pide "
                     f"{lienzo[0]} × {lienzo[1]}")

    cruda = zlib.decompress(idat)
    bpp, paso = 4, ancho * 4 + 1
    filtro, linea = cruda[0], bytearray(cruda[1:paso])
    for x in range(len(linea)):                     # fila 0: prev son ceros
        a = linea[x - bpp] if x >= bpp else 0
        if filtro == 1:
            linea[x] = (linea[x] + a) & 255
        elif filtro in (3, 4):
            linea[x] = (linea[x] + (a // 2 if filtro == 3 else a)) & 255
    for x in (0, ancho // 2, ancho - 1):
        if linea[x * 4 + 3] != 0:
            malos.append(f"la fila 0 no es transparente en x={x}")
            break
    return malos


def ficha(p: dict, sid: str, acento: str) -> str:
    """La hoja de especificación que se sube junto al fichero.

    Una app de impresión bajo demanda pide colocación y tamaño aparte del
    dibujo. Escribirlo aquí y no en un correo es lo que evita que la segunda
    tirada salga a otro tamaño que la primera.
    """
    area, _an, _xf, _yc, prenda = COLOCACION[sid]
    area_w, area_h, area_n = AREAS[area]
    med = p.get("medida") or {}
    linea_med = ""
    if med and not med.get("error"):
        linea_med = (
            f"| Tinta bajo {MM_MINIMO} mm | {med['finos']:.1%} "
            f"(máximo {FINO_MAXIMO:.0%}) |\n"
            f"| Hueco bajo {HUECO_MINIMO} mm | {med['huecos']:.1%} "
            f"(máximo {HUECO_MAXIMO:.0%}) |\n"
            f"| Cobertura de tinta | {med['cobertura']:.0%} del recuadro "
            f"del dibujo |\n")
    return f"""# {p['base']}

| Campo | Valor |
|---|---|
| Prenda | {prenda} |
| Área de estampación | {area_n} · {area_w} × {area_h} cm |
| Fichero | **{p['lienzo'][0]} × {p['lienzo'][1]} px** · {PPP} ppp · PNG con alfa |
| Dibujo dentro del lienzo | {p['cm'][0]} × {p['cm'][1]} cm ({p['pulgadas'][0]}" × {p['pulgadas'][1]}") |
| Colocación | a {p['sitio'][0]} cm del borde izquierdo y {p['sitio'][1]} cm del superior |
| Tinta hueso | `{HUESO_POD}` |
| Tinta acento | `{ACENTOS_POD[acento]}` ({acento}) |
{linea_med}| Método | Impresión directa sobre prenda (DTG) |

## Cómo se sube

**El lienzo del fichero ES el área de estampación.** Súbelo y dile a la
aplicación que lo **encaje al área** —no lo escales a mano—: el dibujo cae
solo en su tamaño y en su sitio, y el fichero queda a {PPP} ppp exactos.
Si en vez de eso se estira el dibujo hasta llenar el área, la aplicación
avisará de resolución insuficiente, y ese aviso tiene razón.

## El color

{NOTA_TINTA[acento]}

La base blanca que la DTG pone debajo levanta y desatura, así que el fichero
lleva un acento más hondo que el de la marca para que lo impreso caiga cerca.
Es compensación, no certeza: **pedir una muestra y cotejarla antes de
cualquier tirada.**

Rasgo mínimo {MM_MINIMO} mm, hueco mínimo {HUECO_MINIMO} mm — medidos sobre el
ráster, no sobre los atributos del dibujo. El área es la estándar del catálogo;
conviene cotejarla con el producto concreto, que varían entre modelos.
"""


def main() -> int:
    medir = "--medir" in sys.argv or "--todas" in sys.argv
    if "--todas" in sys.argv:
        trabajos = [(sid, ac) for sid in COLOCACION for ac in ACENTOS]
    else:
        trabajos = [(MODELO[0], MODELO[1])]

    print(f"\n  IMPRESIÓN BAJO DEMANDA · {PPP} ppp · rasgo ≥ {MM_MINIMO} mm · "
          f"hueco ≥ {HUECO_MINIMO} mm")
    print(f"  el lienzo es el área de estampación, no el dibujo\n")
    fallos = 0
    for sid, acento in trabajos:
        p = exportar(sid, acento, medir)
        print(f"  {p['base']}")
        for t in dict.fromkeys(p["tocado"]):
            print(f"      endurecido · {t}")
        if p["malos"]:
            fallos += 1
            for mal in p["malos"]:
                print(f"      NO SE PUEDE MANDAR · {mal}")
            continue
        area_w, area_h, area_n = AREAS[p["area"]]
        print(f"      lienzo {p['lienzo'][0]} × {p['lienzo'][1]} px "
              f"= {area_w} × {area_h} cm  ·  dibujo {p['cm'][0]} × "
              f"{p['cm'][1]} cm a ({p['sitio'][0]}, {p['sitio'][1]})  ·  "
              f"{p['kb']} KB")
        if p.get("medida") and not p["medida"].get("error"):
            m = p["medida"]
            print(f"      ráster · fino {m['finos']:.1%} · "
                  f"hueco fino {m['huecos']:.1%} · "
                  f"hueco más estrecho {m['hueco_min'] / (PPP / 25.4):.2f} mm "
                  f"· cobertura {m['cobertura']:.0%}")
        (DESTINO / f"{p['base']}.md").write_text(
            ficha(p, sid, acento), encoding="utf-8")
        for mal in verificar(DESTINO / f"{p['base']}.png", p["lienzo"]):
            fallos += 1
            print(f"      EL FICHERO ESCRITO NO CUMPLE · {mal}")
    print(f"\n  {len(trabajos) - fallos} de {len(trabajos)} listos en "
          f"{DESTINO.relative_to(RAIZ.parent)}/\n")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
