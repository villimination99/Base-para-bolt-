#!/usr/bin/env python3
"""
VILLUMINATIONS — Serie gótica: la letra quebrada
=================================================
Escribe `ropa/partials/gotico.svg` y los ficheros por color en `ropa/dist/`.

    python3 ropa/tools/dibujar-gotico.py
    python3 ropa/tools/dibujar-gotico.py --hoja   # y la hoja de contacto

De qué va el género, de verdad
------------------------------
La ropa oscura que funciona en este nicho **no va de espinas**: va de
**letra**. Las alas simétricas que gotean las dibuja todo el mundo y no
distinguen a nadie —eso ya está escrito en `dibujar-marca.py` y sigue siendo
verdad—. Lo que sí distingue es la **tipografía negra**: asta gruesa de pluma
cortada, remates en rombo, densidad vertical. Ahí el dibujo *es* la letra.

Y «abstracto» no quiere decir añadir púas. Quiere decir **quebrar la forma**:
cortarla en bandas y desplazarlas, de modo que el ojo la reconstruya. Una letra
entera se lee; una letra quebrada se mira. Eso es lo que hace esta serie.

Lo que la hace nuestra y no de cualquiera
-----------------------------------------
Dentro de la letra va el **instrumento**: el arco graduado, los treinta y seis
decanatos, la escala que se cuenta con el dedo. Es la única imagen que esta
tienda tiene ganada —los ocho libros están ilustrados así— y aquí vive en los
huecos del monograma. A tres metros es un signo gótico; a medio metro es un
aparato de medir. Un dibujo que aguanta las dos distancias es un dibujo que se
puede vender dos veces.

La letra está dibujada aquí
---------------------------
No hay tipografía de terceros. Cada capital se compone de primitivas de pluma
—`asta`, `rombo`, `travesano`, `espuela`— en una caja de 100 de alto, que es
como se construye una textura de verdad: casi toda letra negra es un asta con
enlaces. Copiar los contornos de una fuente sería usar el trabajo de otro; esto
es del ángulo de pluma para arriba.

El lema
-------
`LEMA` es la política editorial de la tienda dicha en tres palabras. No es un
eslogan inventado para la camiseta: es lo que hacen los cuarenta artículos y
las once fichas. Por eso se puede estampar sin mentir.
"""

import math
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PARTIALS = RAIZ / "partials" / "gotico.svg"
DIST = RAIZ / "dist"

# Los mismos tokens del resto del sistema. No hay paleta nueva.
COLORES = {
    "hueso": "#eef2ff",
    "cian": "#00f0ff",
    "magenta": "#ff00e5",
    "naranja": "#ff6600",
    "purpura": "#a97bff",
    "verde": "#00ff88",
    "tinta": "#0a0a12",          # para prenda clara
}

# El lema, en las tres lenguas de la tienda. Dos palabras y una coma: cabe en
# una manga y se lee a tres metros, que es lo que se le pide a un lema.
LEMA = {
    "es": "MIDE · NO CREAS",
    "en": "MEASURE · DO NOT BELIEVE",
    "fr": "MESURE · NE CROIS PAS",
}

DECANOS = 36
DIVISIONES = 12

# --- geometría de pluma ----------------------------------------------------
ALTO = 100.0        # caja de letra
ASTA = 23.0         # grueso del asta
HUECO = 15.0        # aire entre astas
CORTE = 9.0         # desplome del corte de pluma (ángulo ~40°)
PICO = 7.0          # medio ancho del rombo de remate


def n(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def asta(x, y0=0.0, y1=ALTO, w=ASTA, corte=CORTE):
    """El asta: un paralelogramo de lados verticales y cortes de pluma.

    El corte hace que el canto de arriba caiga hacia la izquierda y el de
    abajo también: es el rastro que deja una pluma de punta ancha sostenida
    en ángulo, y es lo único que separa una letra negra de un rectángulo.
    """
    return (f"M{n(x)},{n(y0 + corte)} L{n(x + w)},{n(y0)} "
            f"L{n(x + w)},{n(y1 - corte)} L{n(x)},{n(y1)} Z")


def rombo(cx, cy, rx=PICO, ry=None):
    ry = ry if ry is not None else rx * 0.72
    return (f"M{n(cx)},{n(cy - ry)} L{n(cx + rx)},{n(cy)} "
            f"L{n(cx)},{n(cy + ry)} L{n(cx - rx)},{n(cy)} Z")


def pie(x, y=ALTO, w=ASTA):
    """El rombo de base, que sobresale a los dos lados del asta."""
    return rombo(x + w / 2, y - CORTE * 0.5, w * 0.78, CORTE * 0.92)


def flag(x, y=0.0, w=ASTA):
    """El remate de arriba: rombo escorado a la izquierda."""
    return rombo(x + w * 0.34, y + CORTE * 0.62, w * 0.62, CORTE * 0.82)


# El contraste es lo que hace negra a una letra negra: asta gruesa contra
# enlace fino. En la primera pasada el travesaño iba a 0,62 del asta y las
# letras salían como una sans angulosa con los pies en punta. Una textura de
# verdad tiene el enlace en torno a un cuarto del asta.
ENLACE = ASTA * 0.26


def travesano(x0, x1, y, grueso=ENLACE, sesgo=CORTE * 0.5):
    """Barra de enlace entre dos astas, con el mismo desplome de pluma."""
    return (f"M{n(x0)},{n(y + sesgo)} L{n(x1)},{n(y)} "
            f"L{n(x1)},{n(y + grueso)} L{n(x0)},{n(y + grueso + sesgo)} Z")


def diagonal(x0, y0, x1, y1, grueso=ENLACE):
    """Enlace en diagonal (la panza de la N, los brazos de la V)."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L * grueso / 2, dx / L * grueso / 2
    return (f"M{n(x0 + nx)},{n(y0 + ny)} L{n(x1 + nx)},{n(y1 + ny)} "
            f"L{n(x1 - nx)},{n(y1 - ny)} L{n(x0 - nx)},{n(y0 - ny)} Z")


def espuela(x, y, largo=13.0, grueso=3.0, ang=-38.0):
    """El pelo fino que sale del asta. Es lo que da el aire de manuscrito."""
    a = math.radians(ang)
    x1, y1 = x + largo * math.cos(a), y + largo * math.sin(a)
    return diagonal(x, y, x1, y1, grueso)


# --- las capitales ---------------------------------------------------------
# Cada letra devuelve (paths, ancho). La caja es 0..ancho × 0..100. Solo están
# las diez que VILLUMINATIONS necesita: V I L U M N A T O S. Dibujar el
# alfabeto entero sería dibujar quince letras que nadie va a estampar.
def L_I():
    x = 0.0
    return [asta(x), flag(x), pie(x), espuela(x + ASTA, CORTE + 3)], ASTA


def L_L():
    x = 0.0
    largo = ASTA + HUECO + 20
    return ([asta(x), flag(x),
             travesano(x + ASTA * 0.2, largo, ALTO - ASTA * 0.62,
                       ENLACE, -CORTE * 0.4),
             rombo(largo, ALTO - ASTA * 0.30, PICO * 0.9, CORTE * 0.8),
             espuela(x + ASTA, CORTE + 3)], largo)


def L_V():
    # Dos astas escoradas que se juntan abajo en un pico. La V de la marca.
    w = ASTA * 2 + HUECO + 12
    med = w / 2
    return ([diagonal(4, CORTE, med, ALTO - 6, ASTA),
             diagonal(w - 4, 0, med, ALTO - 6, ASTA * 0.72),
             flag(0), rombo(w - 4, CORTE * 0.7, PICO * 0.8, CORTE * 0.7),
             rombo(med, ALTO - 4, PICO * 1.1, CORTE * 0.9),
             espuela(ENLACE, CORTE + 4)], w)


def L_U():
    w = ASTA * 2 + HUECO
    x2 = ASTA + HUECO
    return ([asta(0, 0, ALTO - ASTA * 0.5), asta(x2, 0, ALTO),
             travesano(0, x2 + ASTA, ALTO - ASTA * 0.62, ENLACE,
                       -CORTE * 0.3),
             flag(0), flag(x2), pie(x2),
             espuela(ASTA, CORTE + 3)], w)


def L_M():
    w = ASTA * 3 + HUECO * 2
    x2, x3 = ASTA + HUECO, (ASTA + HUECO) * 2
    return ([asta(0), asta(x2), asta(x3),
             diagonal(ENLACE, CORTE, x2 + ASTA * 0.5, ALTO * 0.52,
                      ENLACE * 1.6),
             diagonal(x3 + ENLACE, CORTE, x2 + ASTA * 0.5, ALTO * 0.52,
                      ENLACE * 1.6),
             flag(0), flag(x2), flag(x3), pie(0), pie(x3),
             espuela(ASTA, CORTE + 3)], w)


def L_N():
    w = ASTA * 2 + HUECO
    x2 = ASTA + HUECO
    return ([asta(0), asta(x2),
             diagonal(ENLACE, CORTE + 4, x2 + ASTA * 0.5, ALTO - CORTE,
                      ENLACE * 1.8),
             flag(0), flag(x2), pie(0), pie(x2),
             espuela(ASTA, CORTE + 3)], w)


def L_A():
    # Capital de textura: asta derecha recta, brazo izquierdo escorado y
    # travesaño alto. No es la A romana: es la que pega con las demás.
    w = ASTA * 2 + HUECO + 6
    xd = w - ASTA
    return ([asta(xd), diagonal(xd + ENLACE, CORTE, 5, ALTO - 4, ASTA),
             travesano(8, xd + ASTA, ALTO * 0.58, ENLACE, -CORTE * 0.3),
             flag(xd), pie(xd), rombo(6, ALTO - 5, PICO, CORTE * 0.85),
             espuela(xd + ASTA, CORTE + 3)], w)


def L_T():
    w = ASTA * 2 + HUECO + 2
    xc = (w - ASTA) / 2
    return ([asta(xc, CORTE * 0.6, ALTO),
             travesano(0, w, CORTE * 0.4, ENLACE, CORTE * 0.55),
             rombo(2, CORTE * 0.9, PICO * 0.8, CORTE * 0.7),
             rombo(w - 2, CORTE * 0.5, PICO * 0.8, CORTE * 0.7),
             pie(xc)], w)


def L_O():
    # Lozenge: dos astas escoradas y dos enlaces. La O de textura es un rombo
    # alargado, no un círculo.
    w = ASTA * 2 + HUECO + 4
    x2 = w - ASTA
    return ([asta(0, ASTA * 0.45, ALTO - ASTA * 0.45),
             asta(x2, ASTA * 0.45, ALTO - ASTA * 0.45),
             travesano(0, x2 + ASTA, ASTA * 0.18, ENLACE, CORTE * 0.45),
             travesano(0, x2 + ASTA, ALTO - ASTA * 0.72, ENLACE,
                       -CORTE * 0.45),
             rombo(w / 2, ASTA * 0.26, PICO * 0.9, CORTE * 0.6),
             rombo(w / 2, ALTO - ASTA * 0.26, PICO * 0.9, CORTE * 0.6)], w)


def L_S():
    """La S: barra alta, espina en diagonal y barra baja.

    Los tres travesaños escorados de la primera versión salían como un garabato
    girado —se vio en «NATIONS» de la pieza dorsal—. El esqueleto de una S de
    textura es en realidad el de una Z comprimida: se entra por arriba a la
    derecha, se baja en diagonal y se sale por abajo a la izquierda. Con asta
    gruesa y remates en rombo, se lee como S.
    """
    w = ASTA * 2 + HUECO - 2
    return ([travesano(3, w, CORTE * 0.35, ASTA * 0.78, CORTE * 0.55),
             diagonal(ASTA * 0.5, ALTO * 0.30, w - ASTA * 0.5, ALTO * 0.68,
                      ASTA * 0.86),
             travesano(0, w - 3, ALTO - ASTA * 0.80, ASTA * 0.78,
                       -CORTE * 0.55),
             rombo(w, CORTE * 0.75, PICO * 0.95, CORTE * 0.8),
             rombo(1, ALTO - CORTE * 0.55, PICO * 0.95, CORTE * 0.8),
             espuela(w - 2, CORTE + 5, 11, 2.6, 128)], w)


def L_D():
    # Asta recta y panza en dos travesaños escorados: la D de textura no
    # lleva curva, lleva quiebro.
    w = ASTA * 2 + HUECO + 2
    xb = w - ASTA * 0.86
    return ([asta(0), flag(0), pie(0),
             travesano(ASTA * 0.4, w, CORTE * 0.5, ENLACE, CORTE * 0.5),
             asta(xb, ASTA * 0.62, ALTO - ASTA * 0.62, ENLACE,
                  CORTE * 0.8),
             travesano(ASTA * 0.4, w, ALTO - ASTA * 0.66, ENLACE,
                       -CORTE * 0.5),
             espuela(ASTA, CORTE + 3)], w)


def L_E():
    w = ASTA * 2 + HUECO - 2
    return ([asta(0), flag(0), pie(0),
             travesano(ASTA * 0.4, w, CORTE * 0.5, ENLACE, CORTE * 0.5),
             travesano(ASTA * 0.4, w - ASTA * 0.5, ALTO * 0.44, ENLACE,
                       -CORTE * 0.25),
             travesano(ASTA * 0.4, w, ALTO - ASTA * 0.68, ENLACE,
                       -CORTE * 0.5),
             rombo(w, CORTE * 0.8, PICO * 0.8, CORTE * 0.7),
             rombo(w, ALTO - CORTE * 0.7, PICO * 0.8, CORTE * 0.7),
             espuela(ASTA, CORTE + 3)], w)


ALFABETO = {"I": L_I, "L": L_L, "V": L_V, "U": L_U, "M": L_M,
            "N": L_N, "A": L_A, "T": L_T, "O": L_O, "S": L_S,
            "D": L_D, "E": L_E}

# Toda palabra que alguna pieza compone en letra negra. La guarda mira esta
# lista, no el nombre de la marca: al poner «MIDE» en la pieza del lema
# faltaban la D y la E, y el fallo salió al ejecutar y no al revisar.
PALABRAS = ("VILLUMINATIONS", "VI", "MIDE", "NO")


def palabra(texto, separacion=HUECO):
    """Compone una palabra. Devuelve (paths, ancho total)."""
    trozos, x = [], 0.0
    for c in texto:
        if c == " ":
            x += separacion * 2
            continue
        paths, w = ALFABETO[c]()
        trozos.append(f'<g transform="translate({n(x)},0)">'
                      + "".join(f'<path d="{d}"/>' for d in paths) + "</g>")
        x += w + separacion
    return "".join(trozos), max(x - separacion, 0.0)


# --- la quiebra ------------------------------------------------------------
_serie = [0]


def quebrar(contenido, ancho, alto, bandas=7, maximo=16.0, semilla=0):
    """Corta el dibujo en bandas horizontales y las desplaza.

    Esto es lo que quiere decir «abstracto» aquí. No se añade nada: se rompe
    lo que hay. Cada banda se recorta con su `clipPath` y se corre en x una
    cantidad que alterna de signo, de modo que la letra se desarma sin dejar
    de ser legible. El desplazamiento se calcula con un seno y no al azar:
    dos ejecuciones tienen que dar el mismo dibujo, porque esto se manda a una
    estampadora y una lámina que cambia sola no se puede mandar.
    """
    _serie[0] += 1
    idg = f"q{_serie[0]}"
    recortes, usos = [], []
    for i in range(bandas):
        y0 = alto * i / bandas
        h = alto / bandas
        dx = maximo * math.sin((i + 1) * 1.9 + semilla) * (1 if i % 2 else -1)
        # las bandas de los extremos se mueven menos: si no, el dibujo se
        # deshilacha por arriba y por abajo y pierde la silueta
        borde = 1.0 - abs((i + 0.5) / bandas - 0.5) * 1.1
        dx *= borde
        recortes.append(
            f'<clipPath id="{idg}-{i}"><rect x="{n(-maximo * 2)}" '
            f'y="{n(y0)}" width="{n(ancho + maximo * 4)}" '
            f'height="{n(h + 0.4)}"/></clipPath>')
        usos.append(f'<g clip-path="url(#{idg}-{i})" '
                    f'transform="translate({n(dx)},0)">{contenido}</g>')
    return f'<defs>{"".join(recortes)}</defs>{"".join(usos)}'


# --- el instrumento --------------------------------------------------------
def arco_graduado(cx, cy, r, desde=-62, hasta=62, grueso=2.2):
    """El arco con sus treinta y seis decanatos. Va dentro de la letra."""
    x0, y0 = cx + r * math.sin(math.radians(desde)), cy - r * math.cos(
        math.radians(desde))
    x1, y1 = cx + r * math.sin(math.radians(hasta)), cy - r * math.cos(
        math.radians(hasta))
    partes = [f'<path d="M{n(x0)},{n(y0)} A{n(r)},{n(r)} 0 0 1 {n(x1)},{n(y1)}" '
              f'fill="none" stroke="currentColor" stroke-width="{n(grueso)}"/>']
    for i in range(DECANOS + 1):
        a = math.radians(desde + (hasta - desde) * i / DECANOS)
        largo = 9.0 if i % 3 == 0 else 5.0
        gr = 2.0 if i % 3 == 0 else 1.1
        sx, sy = cx + r * math.sin(a), cy - r * math.cos(a)
        ex = cx + (r + largo) * math.sin(a)
        ey = cy - (r + largo) * math.cos(a)
        partes.append(f'<line x1="{n(sx)}" y1="{n(sy)}" x2="{n(ex)}" '
                      f'y2="{n(ey)}" stroke="currentColor" '
                      f'stroke-width="{n(gr)}"/>')
    return "".join(partes)


def columna_grados(cx, y0, y1, pasos=DIVISIONES, ancho=13.0):
    """La escala que cae a plomo por el centro. Se cuenta con el dedo."""
    partes = [f'<line x1="{n(cx)}" y1="{n(y0)}" x2="{n(cx)}" y2="{n(y1)}" '
              f'stroke="currentColor" stroke-width="1.6"/>']
    for i in range(pasos + 1):
        y = y0 + (y1 - y0) * i / pasos
        w = ancho if i % 3 == 0 else ancho * 0.52
        gr = 2.2 if i % 3 == 0 else 1.2
        partes.append(f'<line x1="{n(cx - w)}" y1="{n(y)}" x2="{n(cx + w)}" '
                      f'y2="{n(y)}" stroke="currentColor" '
                      f'stroke-width="{n(gr)}"/>')
    return "".join(partes)


def texto_fino(t, x, y, tam, espaciado, anclaje="middle", opacidad=1.0):
    return (f'<text x="{n(x)}" y="{n(y)}" text-anchor="{anclaje}" '
            f'font-family="Georgia,\'Times New Roman\',serif" '
            f'font-size="{n(tam)}" letter-spacing="{n(espaciado)}" '
            f'fill="currentColor" opacity="{n(opacidad)}">{t}</text>')


# --- las piezas ------------------------------------------------------------
def _linea(texto, ancho_util, x0, y0, separacion, bandas, fraccion,
            semilla):
    """Una línea de letra negra, escalada al ancho y quebrada en proporción.

    La quiebra se pide en **fracción de la altura de la línea**, no en píxeles.
    En la primera pasada era un número absoluto y la pieza dorsal se deshizo:
    nueve bandas sobre una letra de 65 px son bandas de 7 px, y eso no quiebra
    una letra, la tritura.
    """
    letras, w = palabra(texto, separacion)
    esc = ancho_util / w
    alto = ALTO * esc
    cuerpo = ('<g transform="translate(' + n(x0) + ',' + n(y0)
              + ') scale(' + n(esc) + ')">' + letras + "</g>")
    return quebrar(cuerpo, x0 + ancho_util, y0 + alto, bandas,
                   alto * fraccion, semilla), alto


def p_monograma():
    """VI a tamaño de pecho, con el arco dentro. La pieza que más se lleva."""
    W, H = 420, 430
    banda, alto = _linea("VI", 270, 75, 74, HUECO + 6, 7, 0.055, 1.2)
    return W, H, (
        f'<g color="currentColor">'
        f'{arco_graduado(W / 2, 212, 152, -54, 54, 2.4)}'
        f'{banda}'
        f'{columna_grados(W / 2, 74 + alto + 14, H - 16, 6, 13)}'
        f'</g>')


def p_dorsal():
    """La pieza de espalda: el nombre a dos líneas, que es como cabe.

    Catorce letras en una sola línea a este ancho son ilegibles por
    construcción —salió así en la primera hoja de contacto—. Partido en
    VILLUMI / NATIONS, cada línea tiene siete y el asta recupera su grueso.
    """
    W, H = 1000, 1320
    util = W - 150
    b1, a1 = _linea("VILLUMI", util, 75, 210, HUECO * 0.9, 7, 0.075, 0.4)
    b2, a2 = _linea("NATIONS", util, 75, 210 + a1 + 26, HUECO * 0.9, 7,
                    0.075, 2.7)
    fin = 210 + a1 + 26 + a2
    return W, H, (
        f'<g color="currentColor">'
        f'{arco_graduado(W / 2, 198, 168, -68, 68, 3.0)}'
        f'{b1}{b2}'
        f'{columna_grados(W / 2, fin + 56, H - 178, 12, 24)}'
        f'{texto_fino(LEMA["es"], W / 2, H - 112, 42, 14)}'
        f'{texto_fino("36 DECANATOS · 12 DIVISIONES", W / 2, H - 56, 20, 9, opacidad=0.48)}'
        f'</g>')


def p_lema():
    """El lema como pieza de espalda.

    «CREAS» pide una C y una R que no están dibujadas, y dibujar dos capitales
    para una sola palabra no se sostiene: la segunda mitad va en serif fina,
    que además da el contraste que la pieza necesitaba.
    """
    W = 1000
    b1, a1 = _linea("MIDE", W - 260, 130, 90, HUECO * 0.95, 6, 0.085, 2.1)
    y = 90 + a1
    # El alto sale del contenido. Fijarlo a mano dejaba 260 px de vacío
    # debajo del nombre, y un vacío en la lámina es tinta que la estampadora
    # cobra por centrar mal.
    H = round(y + 470)
    return W, H, (
        f'<g color="currentColor">'
        f'{b1}'
        f'<line x1="200" y1="{n(y + 54)}" x2="{n(W - 200)}" y2="{n(y + 54)}" '
        f'stroke="currentColor" stroke-width="2.4" opacity="0.8"/>'
        f'{texto_fino("NO CREAS", W / 2, y + 138, 76, 26)}'
        # El arco se centra en y+420 con radio 176, así que su parte más
        # alta cae en y+244 y no toca el «NO CREAS» de y+138. Con el radio
        # centrado en y+296 sí lo tocaba, y el nombre encima quedaba cruzado
        # por las marcas del arco.
        f'{arco_graduado(W / 2, y + 420, 176, -58, 58, 2.6)}'
        f'{texto_fino("VILLUMINATIONS", W / 2, y + 400, 34, 15, opacidad=0.9)}'
        f'</g>')


def p_manga():
    """La tira de la manga: monograma arriba, escala, lema en vertical.

    El texto girado se ancla en su propio centro y **después** se rota el
    grupo; al revés se sale de la caja, que es lo que pasó en la primera
    pasada y se comió la S de «CREAS».
    """
    W, H = 190, 1040
    banda, alto = _linea("VI", 118, 36, 44, HUECO, 6, 0.05, 5.1)
    y_texto = 710
    return W, H, (
        f'<g color="currentColor">'
        f'{banda}'
        f'{columna_grados(W / 2, 44 + alto + 42, 400, 6, 16)}'
        f'<g transform="rotate(-90 {n(W / 2)} {n(y_texto)})">'
        f'{texto_fino(LEMA["es"], W / 2, y_texto + 11, 31, 12)}</g>'
        f'</g>')


def p_sello():
    """Macizo, sin quebrar: para gorra, etiqueta y bordado.

    Un bordado no puede llevar bandas desplazadas —el hilo no salta— así que
    esta pieza es la misma letra sin romper. Es también la que vale para el
    favicon y para la marca de agua de los PDF.
    """
    W, H = 360, 310
    letras, w = palabra("VI", HUECO + 4)
    esc = 190 / ALTO
    return W, H, (
        f'<g color="currentColor">'
        f'<g transform="translate({n((W - w * esc) / 2)},38) scale({n(esc)})">'
        f'{letras}</g>'
        f'{arco_graduado(W / 2, 156, 120, -46, 46, 2.2)}'
        f'{texto_fino("VILLUMINATIONS", W / 2, 276, 22, 9)}'
        f'</g>')


PIEZAS = {
    "go-monograma": (p_monograma, "Monograma VI quebrado · pecho"),
    "go-dorsal": (p_dorsal, "El nombre entero · espalda"),
    "go-lema": (p_lema, "El lema · espalda"),
    "go-manga": (p_manga, "Tira vertical · manga"),
    "go-sello": (p_sello, "Sello macizo · gorra y etiqueta"),
}


def construir() -> str:
    cuerpos = []
    for sid, (fn, _d) in PIEZAS.items():
        W, H, contenido = fn()
        cuerpos.append(f'  <symbol id="{sid}" viewBox="0 0 {W} {H}">\n'
                       f'    {contenido}\n  </symbol>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0"\n'
            '     style="position:absolute">\n'
            "<!-- VILLUMINATIONS · serie gótica. Generado por\n"
            "     ropa/tools/dibujar-gotico.py. No se edita a mano: lo que se\n"
            "     escriba aquí se pierde en la siguiente pasada. -->\n"
            + "\n".join(cuerpos) + "\n</svg>\n")


def sueltos() -> int:
    """Un SVG por pieza y color, que es lo que pide la estampadora."""
    DIST.mkdir(parents=True, exist_ok=True)
    n_ = 0
    for sid, (fn, _d) in PIEZAS.items():
        W, H, contenido = fn()
        for nombre, hex_ in COLORES.items():
            (DIST / f"{sid}-{nombre}.svg").write_text(
                f'<svg xmlns="http://www.w3.org/2000/svg" '
                f'viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
                f'<g fill="{hex_}" color="{hex_}">{contenido}</g>\n</svg>\n',
                encoding="utf-8")
            n_ += 1
    return n_


def comprobar() -> list:
    malos = []
    # El torso es lo que limita, no el ancho de la prenda: las mangas se
    # comen casi diez centímetros por lado. Una lámina más ancha que el
    # torso se estampa cortada, y eso no se ve hasta tener la prenda encima.
    torso = ANCHO_CM * (1 - 0.19 * 2)
    for clave, d in PRENDA.items():
        if d["ancho_cm"] > torso - 2:
            malos.append(f"{clave} · {d['ancho_cm']} cm de ancho sobre un "
                         f"torso de {torso:.0f} cm: se estamparía cortada")
    for w in PALABRAS:
        for c in w:
            if c not in ALFABETO:
                malos.append(f"falta la capital «{c}», que «{w}» necesita")
    for lengua, t in LEMA.items():
        if len(t) > 26:
            malos.append(f"lema [{lengua}] de {len(t)} caracteres: no cabe en "
                         f"una manga")
    for sid, (fn, _d) in PIEZAS.items():
        W, H, contenido = fn()
        if "currentColor" not in contenido:
            malos.append(f"{sid} · no usa currentColor: no se podría sacar "
                         f"en los siete colores desde un solo dibujo")
    return malos


# --- la prenda -------------------------------------------------------------
# Una lámina suelta no dice si el dibujo funciona: lo que decide es **a qué
# tamaño va sobre la tela**. Esta silueta plana es de croquis, no de catálogo,
# y está a escala: la camiseta mide 52 cm de ancho de pecho y el dibujo de
# espalda 32 cm, que es lo que cabe en una plancha de estampación digital.
PRENDA = {
    "espalda": {
        "pieza": "go-dorsal", "ancho_cm": 28, "arriba_cm": 9,
        "titulo": "Espalda · 28 cm de ancho, a 9 cm del cuello",
    },
    "pecho": {
        "pieza": "go-monograma", "ancho_cm": 11, "arriba_cm": 14,
        "titulo": "Pecho izquierdo · 11 cm, a 14 cm del hombro",
    },
    "lema": {
        "pieza": "go-lema", "ancho_cm": 27, "arriba_cm": 11,
        "titulo": "Espalda alterna · el lema, 27 cm",
    },
}
ANCHO_CM = 52.0          # ancho de pecho de la prenda del croquis
ALTO_CM = 72.0


def silueta(px_cm):
    """Camiseta plana de croquis. Trazo fino: es un plano, no un dibujo."""
    W, H = ANCHO_CM * px_cm, ALTO_CM * px_cm
    h, c = W * 0.19, W * 0.115          # hombro y cuello
    return (W, H,
            f'<path d="M{n(h)},{n(H * 0.07)} '
            f'L{n(W / 2 - c)},{n(H * 0.035)} '
            f'Q{n(W / 2)},{n(H * 0.105)} {n(W / 2 + c)},{n(H * 0.035)} '
            f'L{n(W - h)},{n(H * 0.07)} '
            f'L{n(W)},{n(H * 0.34)} L{n(W - h * 0.72)},{n(H * 0.40)} '
            f'L{n(W - h * 0.80)},{n(H)} L{n(h * 0.80)},{n(H)} '
            f'L{n(h * 0.72)},{n(H * 0.40)} L0,{n(H * 0.34)} Z" '
            f'fill="#111119" stroke="#2c2c3c" stroke-width="1.6"/>')


def croquis(clave, px_cm=11.0) -> str:
    d = PRENDA[clave]
    W, H, cuerpo = silueta(px_cm)
    sid = d["pieza"]
    pw, ph, _c = PIEZAS[sid][0]()
    ancho = d["ancho_cm"] * px_cm
    alto = ancho * ph / pw
    x = (W - ancho) / 2 if clave != "pecho" else W * 0.585
    y = H * 0.07 + d["arriba_cm"] * px_cm
    # Escala explícita y no <svg> anidado. Con el anidado, el <use> no se
    # escalaba al hueco: el monograma de pecho salía a tamaño de espalda y
    # recortado. El croquis lo destapó; la lámina suelta no podía.
    esc = ancho / pw
    return (f'<svg viewBox="0 0 {n(W)} {n(H)}">{cuerpo}'
            f'<g transform="translate({n(x)},{n(y)}) scale({n(esc)})">'
            f'<use href="#{sid}"/></g></svg>')


def hoja() -> int:
    """La hoja de contacto. Mirarlas renderizadas es lo único que enseña si
    una lámina funciona: las dos correcciones de la serie de signos salieron
    de aquí y no de leer el código."""
    S = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
             "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")
    S.mkdir(parents=True, exist_ok=True)
    celdas = []
    for clave, d in PRENDA.items():
        celdas.append(f'<figure class=prenda>{croquis(clave)}'
                      f'<figcaption>{d["pieza"]}'
                      f'<span>{d["titulo"]}</span></figcaption></figure>')
    for sid, (fn, desc) in PIEZAS.items():
        W, H, _c = fn()
        celdas.append(
            f'<figure><svg viewBox="0 0 {W} {H}"><use href="#{sid}"/></svg>'
            f'<figcaption>{sid}<span>{desc}</span></figcaption></figure>')
    html = f"""<!doctype html><meta charset=utf-8><style>
body{{margin:0;background:#06060a;color:#eef2ff;
 font:13px/1.5 Georgia,serif;padding:26px;
 display:grid;grid-template-columns:repeat(3,1fr);gap:26px;align-items:start}}
figure{{margin:0;background:#0b0b12;padding:20px;border:1px solid #191925}}
figure.prenda{{background:#07070c}}
figure.prenda svg{{max-height:560px}}
svg{{width:100%;height:auto;max-height:620px;fill:#eef2ff;color:#eef2ff}}
figcaption{{margin-top:14px;letter-spacing:.14em;font-size:12px}}
figcaption span{{display:block;opacity:.45;letter-spacing:.04em;margin-top:4px}}
</style>{PARTIALS.read_text(encoding="utf-8")}{"".join(celdas)}"""
    (S / "gotico.html").write_text(html, encoding="utf-8")
    (S / "gotico.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        f"const p = await b.newPage({{viewport:{{width:1500,height:1200}}}});\n"
        f"await p.goto('file://{S}/gotico.html');\n"
        f"await p.screenshot({{path:'{S}/gotico.png',fullPage:true}});\n"
        "await b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(S / "gotico.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        print(f"    no se pudo renderizar:\n{r.stderr}")
        return 1
    print(f"    {S}/gotico.png")
    return 0


def main() -> int:
    malos = comprobar()
    print(f"\n  {len(PIEZAS)} piezas · {len(ALFABETO)} capitales dibujadas · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if malos:
        return 1

    PARTIALS.parent.mkdir(parents=True, exist_ok=True)
    PARTIALS.write_text(construir(), encoding="utf-8")
    print(f"    {PARTIALS.relative_to(RAIZ.parent)}  "
          f"{PARTIALS.stat().st_size // 1024} KB")
    print(f"    {sueltos()} ficheros por pieza y color en "
          f"{DIST.relative_to(RAIZ.parent)}/\n")
    for sid, (fn, desc) in PIEZAS.items():
        W, H, _c = fn()
        print(f"    {sid:16} {W:>5} × {H:<5} {desc}")
    print(f"\n    Lema: {LEMA['es']}  ·  {LEMA['en']}  ·  {LEMA['fr']}\n")
    if "--hoja" in sys.argv:
        return hoja()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
