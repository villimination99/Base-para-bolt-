#!/usr/bin/env python3
"""
VILLUMINATIONS — Grafismos de marca para estampar
==================================================
Escribe `ropa/partials/marca.svg` y los ficheros sueltos listos para la
estampadora, en `ropa/dist/`.

    python3 ropa/tools/dibujar-marca.py

**Por qué no se parece a lo que se ve por ahí.** El género de la ropa oscura
está lleno de alas espinosas simétricas que gotean, y las hacen todas las
marcas a la vez: no distinguen a nadie. Esta serie parte del sitio contrario y
del que ya es vuestro: los libros están ilustrados con **instrumentos** —ruedas
de grados, anillos de conteo, escalas que se pueden contar con el dedo—, y esa
es la única imagen que esta tienda tiene ganada. Lo que se estampa aquí es eso,
a tamaño de espalda.

La idea del monograma es de la casa: **VI**, de VILLUMINATIONS. Se construye
como un sextante —los dos brazos en V son el arco graduado, la I es la barra
índice que cae a plomo—, así que a tres metros se lee como unas letras y de
cerca es un aparato de medir. Un signo que aguanta las dos distancias.

Tres piezas, la misma gramática:

· `vi-sigilo`   — el monograma. Pecho, gorra, etiqueta.
· `vi-dorsal`   — la pieza de espalda: la V abierta sobre los omóplatos y la
                  columna de grados cayendo por el centro.
· `vi-manga`    — la tira vertical de la manga.

Todo en **un solo color sobre negro**, que es lo que mejor aguanta la
estampación digital directa y lo que menos cuesta serigrafiar. Los colores
salen de `planes/assets/brand.css`: no hay una paleta nueva.
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PARTIALS = RAIZ / "partials" / "marca.svg"
DIST = RAIZ / "dist"

# Los mismos tokens neón del resto del sistema. Una paleta nueva sería la
# cuarta, y ya sobra con tres.
COLORES = {
    "cian": "#00f0ff",
    "magenta": "#ff00e5",
    "verde": "#00ff88",
    "naranja": "#ff6600",
    "purpura": "#a97bff",
    "hueso": "#eef2ff",
    # para prenda clara: los neones no se ven sobre blanco
    "tinta": "#0a0a12",
}

DIVISIONES = 12          # los doce signos
DECANOS = 36             # los treinta y seis decanatos


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, grados):
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def linea(x1, y1, x2, y2, ancho=2, opacidad=1.0):
    return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" '
            f'stroke-width="{f(ancho)}"'
            + (f' opacity="{f(opacidad)}"' if opacidad < 1 else "") + "/>")


def circulo(cx, cy, r, ancho=2, relleno="none", opacidad=1.0):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{relleno}" '
            f'stroke-width="{f(ancho)}"'
            + (f' opacity="{f(opacidad)}"' if opacidad < 1 else "") + "/>")


# ---------------------------------------------------------------------------
# Piezas comunes
# ---------------------------------------------------------------------------
def roseta(cx, cy, r, spokes=DIVISIONES, marcas=DECANOS):
    """El nudo del que cuelga todo: dos anillos, doce radios, treinta y seis
    marcas. Es la misma construcción que las rosetas de los códices."""
    p = [circulo(cx, cy, r), circulo(cx, cy, r * 0.62, 1.2, opacidad=.75),
         circulo(cx, cy, r * 0.16, 1.6)]
    for i in range(spokes):
        g = i * 360 / spokes
        x1, y1 = pol(cx, cy, r * 0.16, g)
        x2, y2 = pol(cx, cy, r * 0.62, g)
        p.append(linea(x1, y1, x2, y2, 1.1, .8))
    for i in range(marcas):
        g = i * 360 / marcas
        largo = r * 0.14 if i % 3 == 0 else r * 0.07
        x1, y1 = pol(cx, cy, r, g)
        x2, y2 = pol(cx, cy, r - largo, g)
        p.append(linea(x1, y1, x2, y2, 1.6 if i % 3 == 0 else 1, 1 if i % 3 == 0 else .7))
    return "".join(p)


def escala(x, y1, y2, ancho=26, paso=22, cada=5):
    """La columna de grados: la barra índice del sextante, con su ladder.

    Se puede contar con el dedo, que es la gracia de todo lo que dibujamos.
    """
    p = [linea(x, y1, x, y2, 2.4)]
    n = int(abs(y2 - y1) / paso)
    for i in range(n + 1):
        y = y1 + i * paso * (1 if y2 > y1 else -1)
        largo = ancho if i % cada == 0 else ancho * 0.45
        p.append(linea(x - largo / 2, y, x + largo / 2, y,
                       1.5 if i % cada == 0 else 1,
                       1 if i % cada == 0 else .6))
    return "".join(p)


def arco(cx, cy, r, g1, g2, marcas, ancho=2.6, hacia=1):
    """Un limbo graduado: el arco y sus marcas radiales.

    Es la pieza que hace que esto se lea como un instrumento y no como un
    adorno. `hacia` dice si las marcas salen hacia fuera (1) o hacia dentro.
    """
    puntos = [pol(cx, cy, r, g1 + (g2 - g1) * i / 60) for i in range(61)]
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
                 for i, (x, y) in enumerate(puntos))
    p = [f'<path d="{d}" fill="none" stroke-width="{f(ancho)}"/>']
    for i in range(marcas + 1):
        g = g1 + (g2 - g1) * i / marcas
        largo = 20 if i % 3 == 0 else 9
        x1, y1 = pol(cx, cy, r, g)
        x2, y2 = pol(cx, cy, r + largo * hacia, g)
        p.append(linea(x1, y1, x2, y2,
                       1.7 if i % 3 == 0 else 1,
                       1 if i % 3 == 0 else .65))
        if i % 6 == 0:
            xc, yc = pol(cx, cy, r + (largo + 8) * hacia, g)
            p.append(circulo(xc, yc, 3.4, 1.3))
    return "".join(p)


def abanico(cx, cy, r1, r2, g1, g2, n):
    """Los radios entre dos limbos. Da densidad sin inventar formas nuevas."""
    p = []
    for i in range(n + 1):
        g = g1 + (g2 - g1) * i / n
        x1, y1 = pol(cx, cy, r1, g)
        x2, y2 = pol(cx, cy, r2, g)
        p.append(linea(x1, y1, x2, y2, 1.5 if i % 3 == 0 else 0.9,
                       .95 if i % 3 == 0 else .5))
    return "".join(p)


def _bez(p0, p1, p2, t):
    u = 1 - t
    return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
            u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])


def _tan(p0, p1, p2, t):
    u = 1 - t
    dx = 2 * u * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
    dy = 2 * u * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
    n = math.hypot(dx, dy) or 1
    return dx / n, dy / n


def _perfil(t, entra=0.42, sale=1.55):
    """Ancho del brazo a lo largo de su recorrido, normalizado a 1.

    Nace en punta, engorda en el primer cuarto y muere en punta. La primera
    versión salía del vértice a todo ancho y los dos brazos se fundían allí en
    un pegote que se comía la roseta: un brazo que no nace afilado no es un
    brazo, es una mancha con dos puntas.
    """
    cima = entra / (entra + sale)                    # dónde está el máximo
    maximo = cima ** entra * (1 - cima) ** sale
    return (t ** entra) * ((1 - t) ** sale) / maximo


def cinta(p0, p1, p2, ancho, afila=1.7, pasos=64):
    """Un brazo macizo, afilado por los dos extremos.

    Una línea de dos píxeles se pierde en la tela: a tamaño de espalda hace
    falta masa. El brazo se traza como cinta sobre una bézier, así que la
    silueta se lee a diez metros y la graduación aparece de cerca.
    """
    izq, der = [], []
    for i in range(pasos + 1):
        t = i / pasos
        x, y = _bez(p0, p1, p2, t)
        dx, dy = _tan(p0, p1, p2, t)
        w = ancho * _perfil(t, sale=afila) / 2
        izq.append((x - dy * w, y + dx * w))
        der.append((x + dy * w, y - dx * w))
    puntos = izq + der[::-1]
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
                 for i, (x, y) in enumerate(puntos)) + " Z"
    return f'<path d="{d}" fill="currentColor" stroke="none"/>'


def hoja(p0, p1, p2, ancho, afila=1.55, nucleo=.40, travesanos=17,
         pasos=72):
    """Un brazo con estructura por dentro, no una silueta plana.

    La primera versión era una mancha maciza: se leía la forma y se perdía la
    marca. Un brazo de esta casa tiene contorno, un núcleo macizo más estrecho
    y travesaños entre los dos —la misma escala graduada de los códices, pero
    dentro del trazo, que es donde se ve.
    """
    def borde(k):
        izq, der = [], []
        for i in range(pasos + 1):
            t = i / pasos
            x, y = _bez(p0, p1, p2, t)
            dx, dy = _tan(p0, p1, p2, t)
            w = ancho * _perfil(t, sale=afila) * k / 2
            izq.append((x - dy * w, y + dx * w))
            der.append((x + dy * w, y - dx * w))
        return izq, der

    p = []
    izq, der = borde(1.0)
    puntos = izq + der[::-1]
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
                 for i, (x, y) in enumerate(puntos)) + " Z"
    p.append(f'<path d="{d}" fill="none" stroke-width="2.6"/>')

    ni, nd = borde(nucleo)
    puntos = ni + nd[::-1]
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)} {f(y)}"
                 for i, (x, y) in enumerate(puntos)) + " Z"
    p.append(f'<path d="{d}" fill="currentColor" stroke="none"/>')

    for j in range(1, travesanos + 1):
        i = round(pasos * j / (travesanos + 1))
        for a, b in ((izq[i], ni[i]), (der[i], nd[i])):
            p.append(linea(a[0], a[1], b[0], b[1],
                           2 if j % 3 == 0 else 1.2,
                           1 if j % 3 == 0 else .55))
    return "".join(p)


def graduar(p0, p1, p2, ancho, n=13, lado=1, afila=1.7, desde=.12):
    """Las marcas que salen del canto del brazo. Es lo que lo convierte en
    instrumento en vez de en mancha."""
    p = []
    for i in range(1, n + 1):
        t = desde + (1 - desde) * i / (n + 1)
        x, y = _bez(p0, p1, p2, t)
        dx, dy = _tan(p0, p1, p2, t)
        w = ancho * _perfil(t, sale=afila) / 2
        bx, by = x - dy * w * lado, y + dx * w * lado
        largo = 30 if i % 3 == 0 else 15
        p.append(linea(bx, by, bx - dy * largo * lado, by + dx * largo * lado,
                       2.2 if i % 3 == 0 else 1.3,
                       1 if i % 3 == 0 else .6))
        if i % 4 == 0:
            cx2 = bx - dy * (largo + 11) * lado
            cy2 = by + dx * (largo + 11) * lado
            p.append(circulo(cx2, cy2, 5, 1.6))
    return "".join(p)


def _rot(v, grados):
    a = math.radians(grados)
    return (v[0] * math.cos(a) - v[1] * math.sin(a),
            v[0] * math.sin(a) + v[1] * math.cos(a))


def _azar(semilla):
    """Generador propio, reproducible. Un dibujo que cambia en cada pasada no
    se puede corregir: hay que poder volver al mismo trazo."""
    x = semilla
    while True:
        x = (1103515245 * x + 12345) % (1 << 31)
        yield x / (1 << 31)


def diente(p0, p1, p2, ancho, lado, n=26, alto=26, afila=1.5):
    """Dentado del canto: triángulos que crecen y menguan con el brazo.

    Es de donde sale la agresividad. Un canto liso es un pétalo; un canto
    dentado es un arma, y sigue siendo la misma silueta.
    """
    p = []
    for i in range(1, n + 1):
        t = i / (n + 1)
        x, y = _bez(p0, p1, p2, t)
        dx, dy = _tan(p0, p1, p2, t)
        w = ancho * _perfil(t, sale=afila) / 2
        bx, by = x - dy * w * lado, y + dx * w * lado
        h = alto * _perfil(t, entra=.6, sale=1.2) * (1.35 if i % 3 == 0 else .7)
        # el diente se peina hacia la punta, no sale perpendicular
        ux, uy = -dy * lado, dx * lado
        px, py = ux * .78 + dx * .62, uy * .78 + dy * .62
        p.append(f'<path d="M{f(bx)} {f(by)} '
                 f'L{f(bx + px * h)} {f(by + py * h)} '
                 f'L{f(bx + dx * h * .5)} {f(by + dy * h * .5)} Z" '
                 f'fill="currentColor" stroke="none"/>')
    return "".join(p)


# El ritmo de las barbas. Un patrón corto que se repite da cadencia; el azar
# da pelusa. Es la diferencia entre un dibujo compuesto y una textura.
RITMO = (1.0, .46, .82, .34, .95, .52, .70, .30)


def barbas(p0, p1, p2, largo, lado, n=8, ancho=54, abre=46, cierra=11,
           afila=1.5, sub=True, desde=.22, ritmo=RITMO):
    """Las barbas del raquis, peinadas casi paralelas a la punta.

    Dos correcciones sobre la primera versión, las dos visibles en el render:
    salían perpendiculares y con longitudes al azar, y el resultado era una
    espiga —textura uniforme que se comía la silueta de la V—. Ahora salen muy
    cerradas, siguen un patrón de longitudes que se repite, y entre ellas queda
    negro. El negro es parte del dibujo.
    """
    p = []
    for i in range(n):
        t = desde + (0.94 - desde) * i / max(n - 1, 1)
        base = _bez(p0, p1, p2, t)
        tan = _tan(p0, p1, p2, t)
        ang = (abre - (abre - cierra) * t) * lado
        d = _rot(tan, ang)
        env = math.sin(math.pi * min(max(t, 0), 1)) ** 0.55
        L = largo * env * ritmo[i % len(ritmo)]
        tip = (base[0] + d[0] * L, base[1] + d[1] * L)
        curva = _rot(d, -13 * lado)
        ctl = (base[0] + curva[0] * L * .5, base[1] + curva[1] * L * .5)
        p.append(cinta(base, ctl, tip, ancho * env * (.6 + .5 * ritmo[i % len(ritmo)]),
                       afila=1.85))
        # muescas sobre el canto: de cerca, cada hoja es una regla
        for k in range(1, 6):
            tk = .22 + .62 * k / 6
            bm = _bez(base, ctl, tip, tk)
            dm = _tan(base, ctl, tip, tk)
            wm = ancho * env * (.6 + .5 * ritmo[i % len(ritmo)]) \
                * _perfil(tk, sale=1.85) / 2
            ox, oy = -dm[1] * wm * lado, dm[0] * wm * lado
            ln = 13 if k % 2 == 0 else 7
            p.append(linea(bm[0] + ox, bm[1] + oy,
                           bm[0] + ox - dm[1] * ln * lado,
                           bm[1] + oy + dm[0] * ln * lado,
                           1.5 if k % 2 == 0 else 1, .9 if k % 2 == 0 else .5))
        if sub and ritmo[i % len(ritmo)] > .6:
            b2 = _bez(base, ctl, tip, .52)
            d2 = _rot(_tan(base, ctl, tip, .52), 26 * lado)
            L2 = L * .42
            t2 = (b2[0] + d2[0] * L2, b2[1] + d2[1] * L2)
            p.append(cinta(b2, ((b2[0] + t2[0]) / 2, (b2[1] + t2[1]) / 2),
                           t2, ancho * env * .22, afila=2.1))
    return "".join(p)


def esquirlas(cx, cy, r1, r2, g1, g2, n=34, semilla=11, largo=52,
              sesgo=26):
    """Astillas sueltas alrededor de la silueta.

    No gotean: caen hacia fuera siguiendo el radio, como fragmentos de la
    propia escala que se hubieran desprendido. Añaden densidad en el borde sin
    tocar la forma principal.
    """
    p = []
    az = _azar(semilla)
    for _ in range(n):
        g = g1 + (g2 - g1) * next(az)
        r = r1 + (r2 - r1) * next(az)
        L = largo * (0.25 + 0.9 * next(az))
        w = 2.5 + 7 * next(az)
        # la astilla se peina hacia fuera siguiendo el barrido del brazo,
        # no cae a plomo: nada aquí gotea
        x1, y1 = pol(cx, cy, r, g)
        x2, y2 = pol(cx, cy, r + L, g + sesgo * (1 if g > 0 else -1) * .35)
        mx, my = pol(cx, cy, r + L * .45, g + sesgo * (1 if g > 0 else -1) * .15)
        p.append(cinta((x1, y1), (mx, my), (x2, y2), w, afila=1.9))
    return "".join(p)


# ---------------------------------------------------------------------------
# Las tres piezas
# ---------------------------------------------------------------------------
def vi_sigilo() -> tuple:
    """El monograma VI: arco graduado arriba, dos brazos en V, plomada al
    centro. 600 × 600."""
    W = H = 600
    cx = 300
    p = []

    # el arco graduado del sextante, arriba
    y_arco = 132
    p.append(linea(120, y_arco, 480, y_arco, 2.6))
    for i in range(25):
        x = 120 + i * 15
        largo = 15 if i % 6 == 0 else 7
        p.append(linea(x, y_arco, x, y_arco - largo,
                       1.6 if i % 6 == 0 else 1,
                       1 if i % 6 == 0 else .6))
    p.append(circulo(120, y_arco, 6, 1.8))
    p.append(circulo(480, y_arco, 6, 1.8))

    # la V: dos brazos que bajan a un vértice
    vx, vy = cx, 452
    for x0 in (146, 454):
        p.append(linea(x0, y_arco + 12, vx, vy, 3))
        # graduación de cada brazo
        for i in range(1, 13):
            t = i / 13
            x = x0 + (vx - x0) * t
            y = (y_arco + 12) + (vy - (y_arco + 12)) * t
            dx, dy = vx - x0, vy - (y_arco + 12)
            n = math.hypot(dx, dy)
            px, py = -dy / n, dx / n
            s = 1 if x0 < cx else -1
            largo = 14 if i % 3 == 0 else 7
            p.append(linea(x, y, x - px * largo * s, y - py * largo * s,
                           1.5 if i % 3 == 0 else 1,
                           1 if i % 3 == 0 else .6))

    # la I: la plomada, que baja por el eje y pasa del vértice
    p.append(escala(cx, y_arco + 34, 430, ancho=22, paso=20, cada=4))
    p.append(linea(cx, 430, cx, 520, 2.4))
    p.append(f'<path d="M{cx} 545 L{cx - 9} 518 L{cx + 9} 518 Z" '
             f'fill="currentColor" stroke="none"/>')

    p.append(roseta(cx, y_arco + 8, 26))
    return W, H, "".join(p)


def vi_dorsal() -> tuple:
    """La pieza de espalda: **la V que se abre**, en su versión elaborada.

    La composición —simétrica, naciendo del eje y abriéndose sobre los
    omóplatos— es del género y la usan todas las marcas del ramo porque es la
    que sigue el cuerpo. Lo propio es todo lo demás: los dos brazos son la V
    del monograma, de su vértice cae la I a plomo, y el detalle no es adorno
    sino la escala graduada de los códices ramificada.

    La jerarquía es deliberada: dos formas enormes, catorce medianas por lado,
    cien finas y treinta astillas. Nada de tamaño intermedio, que es lo que
    convierte lo elaborado en emborronado.

    1200 × 1600, proporción de estampado de espalda.
    """
    W, H = 1200, 1600
    cx = 600
    vert = (cx, 920)
    p = []

    # el limbo graduado, por detrás: devuelve la lectura de instrumento que
    # las hojas tapaban. Va fino a propósito, para no competir con la V.
    p.append(arco(cx, 1010, 812, -58, 58, 36, ancho=2.0))
    p.append(abanico(cx, 1010, 812, 762, -54, 54, 30))
    p.append(arco(cx, 1010, 762, -54, 54, 24, ancho=1.5, hacia=-1))
    for g in (-58, 58):
        x1, y1 = pol(cx, 1010, 812, g)
        p.append(circulo(x1, y1, 9, 2))
        p.append(roseta(x1, y1, 34))

    for lado in (-1, 1):
        tip = (cx + 466 * lado, 196)
        ctl = (cx + 246 * lado, 560)

        # las barbas van debajo del raquis para que este las corte limpio
        p.append(barbas(vert, ctl, tip, 452, lado, n=8, ancho=52,
                        abre=44, cierra=10, desde=.31))

        # el raquis: contorno, núcleo y travesaños
        p.append(hoja(vert, ctl, tip, 94, afila=1.48, travesanos=23))
        p.append(diente(vert, ctl, tip, 94, -lado, n=32, alto=34, afila=1.48))
        p.append(graduar(vert, ctl, tip, 94, n=13, lado=lado, afila=1.48,
                         desde=.30))

        # brazo interior, más empinado
        tip2 = (cx + 232 * lado, 300)
        ctl2 = (cx + 124 * lado, 636)
        p.append(barbas(vert, ctl2, tip2, 168, lado, n=5, ancho=22,
                        abre=38, cierra=10, sub=False, desde=.38,
                        ritmo=(1.0, .42, .78, .36, .62)))
        p.append(hoja(vert, ctl2, tip2, 48, afila=1.8, nucleo=.46,
                      travesanos=11))
        p.append(diente(vert, ctl2, tip2, 48, -lado, n=20, alto=17, afila=1.8))

        # plumas exteriores: prolongan la silueta más allá de las puntas
        for k, (dx, dy) in enumerate(((572, 236), (534, 344), (470, 452))):
            tipf = (cx + dx * lado, dy)
            ctlf = (cx + (dx - 156) * lado, dy + 336)
            # arrancan ya despegadas del nudo, no del punto exacto
            pie = _bez(vert, ctlf, tipf, .16 + k * .05)
            p.append(cinta(pie, ctlf, tipf, 19 - k * 4, afila=2.3))

    # astillas sueltas en el borde superior, a los dos lados
    p.append(esquirlas(cx, 900, 500, 640, -92, -46, n=9, semilla=13, largo=96))
    p.append(esquirlas(cx, 900, 500, 640, 46, 92, n=9, semilla=29, largo=96))

    # --- la I: columna vertebrada
    p.append(escala(cx, 985, 1352, ancho=92, paso=26, cada=4))
    for dx in (-19, 19):
        p.append(linea(cx + dx, 1000, cx + dx, 1330, 1.8, .7))
    for j, (y, r) in enumerate(((1046, 82), (1206, 56), (1320, 32))):
        p.append(circulo(cx, y, r, 2.4, opacidad=.95))
        p.append(circulo(cx, y, r * .58, 1.4, opacidad=.7))
        for i in range(DIVISIONES):
            g = i * 360 / DIVISIONES
            x1, y1 = pol(cx, y, r, g)
            x2, y2 = pol(cx, y, r - 13, g)
            p.append(linea(x1, y1, x2, y2, 1.5, .85))
        # barbas laterales de la vértebra
        for lado in (-1, 1):
            for k in (0, 1):
                g = (74 + k * 26) * lado
                x1, y1 = pol(cx, y, r, g)
                x2, y2 = pol(cx, y, r + (56 - j * 12) - k * 20, g + 6 * lado)
                p.append(cinta((x1, y1), ((x1 + x2) / 2, (y1 + y2) / 2 + 8),
                               (x2, y2), 13 - j * 3, afila=2.0))

    p.append(linea(cx, 1352, cx, 1430, 3.2))
    p.append(f'<path d="M{cx} 1470 L{cx - 17} 1424 L{cx + 17} 1424 Z" '
             f'fill="currentColor" stroke="none"/>')

    # --- el nudo del vértice
    p.append(circulo(cx, 920, 104, 3.4))
    p.append(roseta(cx, 920, 80))
    for i in range(DECANOS):
        g = i * 360 / DECANOS
        if abs(((g + 180) % 360) - 180) > 128:      # solo el arco de abajo
            x1, y1 = pol(cx, 920, 104, g)
            x2, y2 = pol(cx, 920, 104 + (26 if i % 3 == 0 else 13), g)
            p.append(linea(x1, y1, x2, y2, 1.8 if i % 3 == 0 else 1.1,
                           1 if i % 3 == 0 else .6))
    return W, H, "".join(p)


def vi_manga() -> tuple:
    """La tira de manga: dos raíles graduados y tres nudos. 300 × 1100.

    Una sola línea con puntos se pierde en la tela; hacen falta dos raíles y
    marcas a los dos lados para que se lea a un metro de distancia.
    """
    W, H = 300, 1100
    cx = 150
    p = []
    for dx in (-26, 26):
        p.append(linea(cx + dx, 150, cx + dx, 950, 2.2))
    n = int((950 - 150) / 24)
    for i in range(n + 1):
        y = 150 + i * 24
        largo = 20 if i % 4 == 0 else 9
        p.append(linea(cx - 26 - largo, y, cx - 26, y,
                       1.5 if i % 4 == 0 else 1, 1 if i % 4 == 0 else .55))
        p.append(linea(cx + 26, y, cx + 26 + largo, y,
                       1.5 if i % 4 == 0 else 1, 1 if i % 4 == 0 else .55))
        if i % 4 == 0:
            p.append(linea(cx - 26, y, cx + 26, y, 1, .35))
    for y in (150, 950):
        p.append(roseta(cx, y, 52))
    p.append(circulo(cx, 550, 34, 1.6, opacidad=.95))
    for i in range(DECANOS):
        g = i * 360 / DECANOS
        x1, y1 = pol(cx, 550, 34, g)
        x2, y2 = pol(cx, 550, 34 - (10 if i % 3 == 0 else 5), g)
        p.append(linea(x1, y1, x2, y2, 1.3 if i % 3 == 0 else .9,
                       1 if i % 3 == 0 else .6))
    return W, H, "".join(p)


PIEZAS = {
    "vi-sigilo": (vi_sigilo, "Monograma VI · pecho, gorra o etiqueta"),
    "vi-dorsal": (vi_dorsal, "Pieza de espalda · estampado grande"),
    "vi-manga": (vi_manga, "Tira de manga"),
}


# ---------------------------------------------------------------------------
def suelto(nombre: str, color: str) -> str:
    """Un SVG independiente, con su color escrito: lo que se manda a estampar.

    Nada de variables CSS aquí. Una estampadora abre el fichero con cualquier
    programa y el color tiene que estar dentro, no heredarse de una hoja que no
    va a viajar con él.
    """
    dibuja, _ = PIEZAS[nombre]
    w, h, cuerpo = dibuja()
    tinta = COLORES[color]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n'
            f'  <g fill="none" stroke="{tinta}" color="{tinta}" '
            f'stroke-linecap="round" stroke-linejoin="round">\n'
            f'    {cuerpo}\n  </g>\n</svg>\n')


def hoja_partials() -> str:
    """Las tres piezas como <symbol>, para que `tienda/ropa.py` las cuente
    igual que cuenta las de los libros."""
    trozos = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
    for nombre, (dibuja, _) in PIEZAS.items():
        w, h, cuerpo = dibuja()
        trozos.append(
            f'  <symbol id="{nombre}" viewBox="0 0 {w} {h}">\n'
            f'    <g fill="none" stroke="currentColor" stroke-linecap="round" '
            f'stroke-linejoin="round">{cuerpo}</g>\n  </symbol>')
    trozos.append("</svg>")
    return "\n".join(trozos) + "\n"


if __name__ == "__main__":
    PARTIALS.parent.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    PARTIALS.write_text(hoja_partials(), encoding="utf-8")
    print(f"\n  {PARTIALS.relative_to(RAIZ.parent)} · "
          f"{len(PIEZAS)} piezas")

    n = 0
    for nombre in PIEZAS:
        for color in COLORES:
            destino = DIST / f"{nombre}-{color}.svg"
            destino.write_text(suelto(nombre, color), encoding="utf-8")
            n += 1
    print(f"  {DIST.relative_to(RAIZ.parent)} · {n} ficheros "
          f"({len(PIEZAS)} piezas × {len(COLORES)} colores)\n")
    for nombre, (_, que) in PIEZAS.items():
        print(f"    {nombre:12} {que}")
    print()
