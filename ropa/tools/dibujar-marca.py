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
    """La pieza de espalda: **la V que se abre**.

    La composición —simétrica, naciendo del eje y abriéndose sobre los
    omóplatos— es del género, no de nadie: la usan todas las marcas del ramo
    porque es la que sigue el cuerpo. Lo que aquí es propio es el trazo: en vez
    de alas de espinas, los dos brazos **son la V del monograma**, cintas
    cónicas graduadas, y de su vértice cae la I a plomo. A diez metros se lee
    una V enorme; de cerca, un instrumento.

    1200 × 1600, proporción de estampado de espalda.
    """
    W, H = 1200, 1600
    cx = 600
    vert = (cx, 905)                        # el vértice de la V, media espalda
    p = []

    # --- brazo mayor: casi recto, con un quiebro al final. Una bézier con
    # el control lejos del acorde curva el brazo hasta que la V se convierte
    # en golondrina; pegado al acorde, se lee la letra.
    for lado in (-1, 1):
        tip = (cx + 468 * lado, 212)
        ctl = (cx + 250 * lado, 566)
        p.append(hoja(vert, ctl, tip, 132, afila=1.5, travesanos=19))
        p.append(graduar(vert, ctl, tip, 132, n=12, lado=lado, afila=1.5,
                         desde=.30))

    # --- brazo interior, más empinado: da la segunda capa sin repetir ángulo
    for lado in (-1, 1):
        tip = (cx + 236 * lado, 318)
        ctl = (cx + 128 * lado, 640)
        p.append(hoja(vert, ctl, tip, 62, afila=1.8, nucleo=.46,
                      travesanos=10))

    # --- plumas: trazo fino que prolonga la silueta más allá de las puntas
    for lado in (-1, 1):
        for k, (dx, dy) in enumerate(((556, 268), (516, 372), (452, 470))):
            tip = (cx + dx * lado, dy)
            ctl = (cx + (dx - 150) * lado, dy + 330)
            p.append(cinta(vert, ctl, tip, 17 - k * 4, afila=2.2))

    # --- la I: la plomada que cae del vértice a la cintura
    p.append(escala(cx, 975, 1345, ancho=86, paso=26, cada=4))
    for dx in (-15, 15):
        p.append(linea(cx + dx, 1000, cx + dx, 1300, 1.6, .7))
    for y, r in ((1046, 78), (1206, 52), (1318, 30)):
        p.append(circulo(cx, y, r, 2, opacidad=.95))
        for i in range(DIVISIONES):
            g = i * 360 / DIVISIONES
            x1, y1 = pol(cx, y, r, g)
            x2, y2 = pol(cx, y, r - 12, g)
            p.append(linea(x1, y1, x2, y2, 1.4, .8))
    p.append(linea(cx, 1345, cx, 1424, 3.2))
    p.append(f'<path d="M{cx} 1462 L{cx - 16} 1418 L{cx + 16} 1418 Z" '
             f'fill="currentColor" stroke="none"/>')

    # --- el nudo del vértice, que es de donde nace todo
    p.append(circulo(cx, 905, 96, 3))
    p.append(roseta(cx, 905, 74))
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
