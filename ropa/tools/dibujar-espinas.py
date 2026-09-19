#!/usr/bin/env python3
"""
VILLUMINATIONS — Serie espina: filigrana orgánica de espalda
=============================================================
Escribe `ropa/partials/espinas.svg` y los ficheros por color en `ropa/dist/`.

    python3 ropa/tools/dibujar-espinas.py
    python3 ropa/tools/dibujar-espinas.py --hoja    # y la hoja de contacto

Qué hace bueno a este género, mirado de cerca
---------------------------------------------
No es «poner púas». Lo que separa una filigrana que se vende de una que parece
un helecho son cuatro cosas, y las cuatro estaban flojas en el intento de alas
de agosto:

1. **Cinta, no trazo.** Cada nervio es una banda rellena que nace ancha y
   muere en punta. Un `stroke` de grosor constante da dibujo de cable. Aquí
   la silueta se calcula desplazando una línea central a los dos lados con el
   ancho decreciendo, que es lo que hace que una espina parezca hueso.
2. **Ramificación de verdad.** Los nervios sueltan hijos, y los hijos sueltan
   nietos. Tres generaciones. Un abanico de costillas paralelas se lee como
   peine; una rama que se subdivide se lee como organismo.
3. **Celdas huecas.** Los huecos cerrados entre nervios —lentes, ojales— son
   la mitad del dibujo. Sin ellos la mancha es maciza y a dos metros es un
   borrón. Con ellos el ojo entra dentro.
4. **El color sale de dentro.** El acento no va encima: va **debajo y más
   ancho**, de modo que asoma por el canto del hueso. Eso es lo que da la
   sensación de que algo brilla dentro de la estructura, y es la diferencia
   entre dos tintas y una imagen.

Lo que la hace nuestra
----------------------
Dentro de la espina va el **instrumento**: el arco de treinta y seis decanatos
detrás de la masa central y los rombos de decanato bajando por la columna. Es
la imagen que los ocho libros ya tienen ganada. A tres metros es una filigrana
gótica; a medio metro es un aparato de medir con nervadura encima.

Determinismo
------------
Nada es aleatorio. Las curvas y los grosores salen de senos y cosenos con una
semilla por pieza, así que dos ejecuciones dan el mismo fichero. Una lámina
que cambia sola no se puede mandar a una estampadora.
"""

import math
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PARTIALS = RAIZ / "partials" / "espinas.svg"
DIST = RAIZ / "dist"

# Dos tintas por pieza: el hueso y el acento. El hueso es el mismo en toda la
# serie; lo que cambia de una prenda a otra es el acento.
HUESO = "#d8dae4"
ACENTOS = {
    "cian": "#00f0ff", "purpura": "#7b2fff", "magenta": "#ff00e5",
    "cardenal": "#e01b3d",       # rojo cardenal, el único cálido saturado
    "oro": "#ffc21a",            # oro viejo: el que mejor aguanta la base
    "verde": "#00ff88", "naranja": "#ff6600", "hielo": "#8fa6c4",
    "hueso": "#6d7080",          # monocromo: acento gris para prenda oscura
}

DECANOS = 36


def n(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------------------
# La cinta: una línea central convertida en banda que se afila
# ---------------------------------------------------------------------------
def _suave(pts) -> str:
    """Traza una polilínea como curva: cuadráticas por los puntos medios.

    Pasar los puntos con `L` deja la silueta facetada y se nota en cuanto la
    lámina se amplía a 28 cm. Con las cuadráticas por los medios, la curva
    entra y sale sin esquinas y no hay que calcular tangentes.
    """
    if len(pts) < 3:
        return " ".join(f"L{n(x)},{n(y)}" for x, y in pts[1:])
    d = []
    for i in range(1, len(pts) - 1):
        mx = (pts[i][0] + pts[i + 1][0]) / 2
        my = (pts[i][1] + pts[i + 1][1]) / 2
        d.append(f"Q{n(pts[i][0])},{n(pts[i][1])} {n(mx)},{n(my)}")
    d.append(f"L{n(pts[-1][0])},{n(pts[-1][1])}")
    return " ".join(d)


def cinta(pts, w0, w1=0.0) -> str:
    """Banda rellena a partir de una línea central, con el ancho decreciendo.

    Es la primitiva de la que sale todo lo demás. El ancho va de `w0` en la
    base a `w1` en la punta —normalmente cero— siguiendo una potencia, no una
    recta: una espina real conserva grosor casi hasta el final y luego se
    afila de golpe.
    """
    m = len(pts)
    izq, der = [], []
    for i, (x, y) in enumerate(pts):
        t = i / (m - 1)
        # Perfil de hoja: punta en los dos extremos, con el ancho máximo
        # cerca de la base. Antes la banda empezaba a plena anchura y dejaba
        # un corte romo; en este género nada acaba romo, y los troncos de la
        # manga y del pantalón salían como barras cortadas a sierra.
        #
        # El seno vale cero en t=0 y en t=1, y con el exponente 0,45 el máximo
        # cae en torno al primer quinto: base que se abre deprisa y afilado
        # largo hasta la punta.
        w = w0 * math.sin(math.pi * (t ** 0.45)) / 2 + w1 * t / 2
        if i == 0:
            dx, dy = pts[1][0] - x, pts[1][1] - y
        elif i == m - 1:
            dx, dy = x - pts[-2][0], y - pts[-2][1]
        else:
            dx = pts[i + 1][0] - pts[i - 1][0]
            dy = pts[i + 1][1] - pts[i - 1][1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L * w, dx / L * w
        izq.append((x + nx, y + ny))
        der.append((x - nx, y - ny))
    borde = izq + der[::-1]
    return f"M{n(borde[0][0])},{n(borde[0][1])} {_suave(borde)} Z"


def espina(x, y, ang, largo, curva, pasos=16, onda=0.0, semilla=0.0):
    """La línea central de un nervio: avanza girando.

    `curva` es el giro total en radianes a lo largo del recorrido, y `onda`
    mete una ondulación encima. Las dos juntas dan el gancho: el nervio sale
    recto, se dobla y termina enroscando.
    """
    pts, a = [(x, y)], ang
    for i in range(pasos):
        t = (i + 1) / pasos
        # El gancho: en el último tercio la curvatura se triplica, así que la
        # punta se cierra de golpe en vez de morir recta. Es lo que separa una
        # espina de una brizna.
        gancho = 1.0 + 2.6 * max(0.0, t - 0.66) / 0.34
        a += curva * gancho / pasos + onda * math.cos(t * 5.5 + semilla) / pasos
        p = largo / pasos * (1.0 - 0.25 * t)      # el paso se acorta al final
        x += p * math.cos(a)
        y += p * math.sin(a)
        pts.append((x, y))
    return pts


# ---------------------------------------------------------------------------
# La ramificación
# ---------------------------------------------------------------------------
def rama(x, y, ang, largo, grueso, curva, gen=3, semilla=0.0, lado=1):
    """Un nervio con sus hijos, y los hijos con los suyos. Devuelve cintas.

    Tres generaciones. Los hijos salen de dos puntos del recorrido del padre,
    hacia fuera, más cortos y más finos; y a cada generación se les aumenta la
    curvatura, que es lo que hace que las puntas enrosquen y el conjunto no se
    lea como un peine.
    """
    if gen <= 0 or largo < 9:
        return []
    pts = espina(x, y, ang, largo, curva, 16, 0.5 * lado, semilla)
    piezas = [cinta(pts, grueso)]

    for k, frac in enumerate((0.34, 0.62)):
        i = int(frac * (len(pts) - 1))
        px, py = pts[i]
        # el ángulo del padre en ese punto, para salir relativo a él
        dx = pts[min(i + 1, len(pts) - 1)][0] - pts[max(i - 1, 0)][0]
        dy = pts[min(i + 1, len(pts) - 1)][1] - pts[max(i - 1, 0)][1]
        base = math.atan2(dy, dx)
        giro = (0.62 + 0.20 * math.sin(semilla + k * 2.1)) * lado
        if k == 1:
            giro *= -0.72                 # el segundo hijo sale al otro lado
        piezas += rama(px, py, base + giro,
                       largo * (0.50 - 0.06 * k),
                       grueso * (0.52 - 0.06 * k),
                       curva * 1.45, gen - 1, semilla + 1.7 + k, lado)
    return piezas


def celda(x, y, ang, largo, ancho, curva=0.9):
    """Un ojal: dos nervios que salen del mismo punto y se vuelven a juntar.

    Es el hueco cerrado que deja entrar la vista. Sin estos, la masa central
    es un borrón a dos metros; con ellos el dibujo tiene interior.
    """
    a = espina(x, y, ang - 0.10, largo, curva, 10)
    b = espina(x, y, ang + 0.10, largo, -curva, 10)
    borde = a + b[::-1]
    return f"M{n(borde[0][0])},{n(borde[0][1])} {_suave(borde)} Z"


def hoja_celda(x, y, ang, largo, ancho):
    """La celda con su contorno: lente rellena menos su hueco interior.

    Se dibuja con `fill-rule="evenodd"` y dos contornos concéntricos, que es
    la manera barata de tener un anillo sin calcular el desplazamiento.
    """
    fuera = celda(x, y, ang, largo, ancho, 0.95)
    dentro = celda(x + math.cos(ang) * largo * 0.13,
                   y + math.sin(ang) * largo * 0.13,
                   ang, largo * 0.72, ancho * 0.6, 0.95)
    return f'<path d="{fuera} {dentro}" fill-rule="evenodd"/>'


# ---------------------------------------------------------------------------
# El instrumento, que es lo nuestro
# ---------------------------------------------------------------------------
def arco(cx, cy, r, desde=-72, hasta=72, grueso=2.0, marcas=DECANOS):
    p = []
    x0 = cx + r * math.sin(math.radians(desde))
    y0 = cy - r * math.cos(math.radians(desde))
    x1 = cx + r * math.sin(math.radians(hasta))
    y1 = cy - r * math.cos(math.radians(hasta))
    p.append(f'<path d="M{n(x0)},{n(y0)} A{n(r)},{n(r)} 0 0 1 {n(x1)},{n(y1)}" '
             f'fill="none" stroke="currentColor" stroke-width="{n(grueso)}"/>')
    for i in range(marcas + 1):
        a = math.radians(desde + (hasta - desde) * i / marcas)
        largo = 11.0 if i % 3 == 0 else 6.0
        g = 2.0 if i % 3 == 0 else 1.1
        sx, sy = cx + r * math.sin(a), cy - r * math.cos(a)
        ex = cx + (r + largo) * math.sin(a)
        ey = cy - (r + largo) * math.cos(a)
        p.append(f'<line x1="{n(sx)}" y1="{n(sy)}" x2="{n(ex)}" y2="{n(ey)}" '
                 f'stroke="currentColor" stroke-width="{n(g)}"/>')
    return "".join(p)


def rombos(cx, y0, y1, cuantos=5):
    """Los decanatos bajando por la columna, decreciendo."""
    p = []
    for i in range(cuantos):
        t = i / (cuantos - 1)
        y = y0 + (y1 - y0) * t
        r = 19 * (1 - 0.68 * t)
        p.append(f'<path d="M{n(cx)},{n(y - r)} L{n(cx + r * 0.62)},{n(y)} '
                 f'L{n(cx)},{n(y + r)} L{n(cx - r * 0.62)},{n(y)} Z"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# El armazón: la marca dentro del dibujo
# ---------------------------------------------------------------------------
def armazon_vi(eje, y_alto, y_vertice, y_pie, medio_ancho, grueso=58.0):
    """La **V** y la **I** de VILLUMINATIONS, como esqueleto y no como sello.

    Un logotipo pegado encima de una filigrana se ve pegado encima. Aquí la
    marca es la estructura: dos hojas rectas y gruesas bajan de los hombros y
    se juntan en un vértice —esa es la V—, y del vértice cae la columna, que
    es la I. Todo lo demás de la lámina crece colgado de ellas.

    Lo que lo hace legible a distancia no es el tamaño, es el **contraste de
    ritmo**: el armazón es recto y macizo, la filigrana es curva y fina. El
    ojo separa las dos cosas antes de leer ninguna, y por eso la V aparece a
    tres metros y desaparece a medio metro, que es justo lo que se pedía.

    `comprobar()` exige que el armazón sea al menos un tercio más grueso que
    la costilla mayor que lo rodea. Si algún día se engorda la filigrana sin
    mirar esto, la marca se pierde dentro y nadie se entera.
    """
    piezas = []
    for lado in (-1, 1):
        # El brazo: casi recto, con apenas curvatura para que no parezca un
        # triángulo dibujado con regla.
        pts = espina(eje + lado * medio_ancho, y_alto,
                     math.atan2(y_vertice - y_alto, -lado * medio_ancho),
                     math.hypot(medio_ancho, y_vertice - y_alto),
                     lado * 0.13, 14)
        piezas.append(cinta(pts, grueso, grueso * 0.12))
    # Púas finas en el canto interior. El brazo liso se leía como hoja de
    # cuchillo y no como filigrana; estas le devuelven el carácter y **no
    # llenan el hueco**, que es la condición para que la letra siga viéndose:
    # pesan poco y mueren enseguida.
    for lado in (-1, 1):
        for i in range(7):
            f = 0.16 + 0.62 * i / 6
            ox = eje + lado * medio_ancho * (1 - f)
            oy = y_alto + (y_vertice - y_alto) * f
            ang = math.radians(-118 if lado < 0 else -62) + lado * math.radians(24 * f)
            piezas.append(cinta(espina(ox, oy, ang, 62 - 26 * f,
                                       -lado * 0.55, 9), 13 - 5 * f))

    # La I: del vértice al pie, con el mismo grueso que los brazos.
    piezas.append(cinta(espina(eje, y_vertice - grueso * 0.32,
                               math.radians(90), y_pie - y_vertice, 0.0, 12),
                        grueso * 0.86))
    return piezas


ARMAZON_MINIMO = 1.33      # veces la costilla mayor de alrededor
GRUESO_ARMAZON = 62.0      # el de los brazos de la V en la pieza dorsal
GRUESO_COSTILLA = 27.0     # el de la costilla mayor que lo rodea


# ---------------------------------------------------------------------------
# Las piezas
# ---------------------------------------------------------------------------
def _esqueleto_dorsal(W, H):
    """El esqueleto de la pieza de espalda, sin color todavía.

    Devuelve (piezas_hueso, piezas_acento). El acento son los nervios que van
    solos en color —las hojas centrales— y el hueso todo lo demás. El halo se
    monta después, en `entintar`, dibujando el mismo hueso más ancho debajo.
    """
    eje = W / 2
    hombro = H * 0.235
    hueso, acento = [], []

    # --- la envergadura, colgada POR FUERA del armazón -------------------
    # Este es el cambio que hace que la marca se lea. Antes las costillas
    # salían del centro y barrían hacia afuera, o sea que llenaban justo el
    # hueco entre los brazos de la V: la letra quedaba tapada por dentro y a
    # tres metros el conjunto se leía como un ala, no como una V.
    #
    # Ahora cada costilla nace **sobre el brazo** y crece hacia afuera y hacia
    # arriba, alejándose del interior. El hueco de la V queda limpio, y un
    # hueco limpio es lo único que convierte dos trazos en una letra.
    ax, ay = W * 0.325, hombro - 76          # punta alta del brazo
    vx, vy = 0.0, hombro + 322               # vértice
    for lado in (-1, 1):
        for i in range(8):
            f = 0.06 + 0.70 * i / 7          # fracción recorrida del brazo
            ox = eje + lado * (ax + (vx - ax) * f)
            oy = ay + (vy - ay) * f
            # hacia afuera y arriba: perpendicular al brazo, no hacia el eje
            ang = math.radians(-152 if lado < 0 else -28) - lado * math.radians(26 * f)
            largo = W * (0.20 - 0.085 * f)
            grueso = GRUESO_COSTILLA - 11 * f
            hueso += rama(ox, oy, ang, largo, grueso,
                          lado * (0.62 + 0.34 * f), 3, i * 1.9, lado)

    # --- la columna ------------------------------------------------------
    # Nueve pares iguales bajando a paso constante se leían como cremallera.
    # La masa central del género no es una escalera: es un nudo que se
    # deshace hacia abajo. Siete pares, el paso crece, el tamaño cae de forma
    # desigual y los ángulos alternan, así que ningún tramo repite al de
    # arriba.
    for i in range(7):
        t = i / 6
        y = hombro + 268 + (H * 0.44) * (t ** 1.22)
        vaiven = 1.0 + 0.30 * math.sin(i * 2.4)
        largo = W * (0.165 - 0.115 * (t ** 0.70)) * vaiven
        grueso = 46 * (1 - 0.76 * t) + 4
        for lado in (-1, 1):
            ang = (math.pi if lado < 0 else 0) + lado * math.radians(
                26 + 40 * t + 9 * math.sin(i * 1.7))
            hueso += rama(eje + lado * (5 + 3 * i), y, ang, largo, grueso,
                          lado * (0.52 + 0.28 * t), 2, i * 2.3, lado)

    # --- el armazón: la V y la I de la marca -----------------------------
    # Va el último de los de hueso, así que se dibuja encima de la filigrana
    # y manda. Sustituye al filo central suelto que había aquí: aquel era una
    # hoja a plomo sin significado, esta es la I.
    # La V tiene que ser MÁS ANCHA que la filigrana, no caber dentro. En la
    # primera prueba de bizco los brazos medían 0,205 de ancho y la filigrana
    # llegaba a 0,34: la marca quedaba enterrada en el bulto. Ahora los brazos
    # salen a 0,325 y sus puntas asoman por encima del nudo, que es lo único
    # que hace que una forma se separe del fondo a tres metros.
    hueso += armazon_vi(eje, hombro - 76, hombro + 322, H * 0.93,
                        W * 0.325, GRUESO_ARMAZON)

    # --- las hojas de acento: las que salen solas en color ---------------
    for lado in (-1, 1):
        for i in range(3):
            t = i / 2
            ang = math.radians(90) + lado * math.radians(8 + 15 * t)
            acento.append(cinta(
                espina(eje + lado * (9 + 5 * t), hombro + 6 + 30 * t,
                       ang, H * (0.40 - 0.09 * t), lado * 0.16, 12),
                15 - 4 * t))
    for lado in (-1, 1):
        for i in range(4):
            t = i / 3
            ang = math.radians(-168 if lado < 0 else -12)
            ang += lado * math.radians(-16 - 46 * t)
            acento.append(cinta(
                espina(eje + lado * (26 + 30 * t), hombro - 6 - 16 * t,
                       ang, W * (0.19 - 0.05 * t), lado * 0.42, 12),
                11 - 3 * t))

    # --- las celdas: en el nudo de los omóplatos -------------------------
    celdas = []
    for lado in (-1, 1):
        for i in range(4):
            t = i / 3
            ang = math.radians(-170 if lado < 0 else -10)
            ang += lado * math.radians(-22 - 44 * t)
            celdas.append(hoja_celda(eje + lado * (34 + 46 * t),
                                     hombro + 4 - 30 * t, ang,
                                     W * (0.15 - 0.035 * t), 1.0))
    return hueso, acento, celdas


def entintar(hueso, acento, celdas, instrumento=""):
    """Monta las tres capas. El orden es el dibujo.

    Primero el acento **más ancho por debajo** —de ahí que asome por el canto y
    parezca que algo brilla dentro—, luego el hueso encima, y al final las
    celdas y el instrumento. Poner el color encima da dos tintas planas; ponerlo
    debajo da profundidad, y es la diferencia entre esto y un calco.
    """
    halo = "".join(f'<path d="{d}"/>' for d in hueso)
    cuerpo = "".join(f'<path d="{d}"/>' for d in hueso)
    hojas = "".join(f'<path d="{d}"/>' for d in acento)
    return (
        f'<g fill="var(--acento)" opacity="0.92" '
        f'stroke="var(--acento)" stroke-width="7" stroke-linejoin="round">'
        f'{halo}</g>'
        f'<g fill="var(--acento)">{hojas}</g>'
        f'<g fill="var(--hueso)">{cuerpo}</g>'
        f'<g fill="var(--acento)">{"".join(celdas)}</g>'
        f'<g color="var(--hueso)" fill="var(--hueso)">{instrumento}</g>')


def p_dorsal():
    W, H = 1000, 1150
    hombro = H * 0.235
    hueso, acento, celdas = _esqueleto_dorsal(W, H)
    inst = (arco(W / 2, hombro + 268, 178, -66, 66, 2.4)
            + rombos(W / 2, H * 0.62, H * 0.90, 5))
    return W, H, entintar(hueso, acento, celdas, inst)


def p_manga():
    """La manga: una rama sola que baja por el brazo."""
    W, H = 260, 720
    hueso, acento = [], []
    for i in range(3):
        t = i / 2
        # La separación tiene que superar al grueso. Con tres troncos de 21
        # a 22 de distancia se solapaban en una plancha de borde escalonado:
        # eso no es un dibujo, es un fallo de composición, y solo se ve
        # renderizando.
        hueso += rama(W * 0.5 + (i - 1) * 62, 62 + 34 * t,
                      math.radians(78 + (i - 1) * 19),
                      H * (0.60 - 0.12 * t), 16 - 4 * t,
                      (1 if i % 2 else -1) * 0.5, 3, i * 3.1,
                      1 if i % 2 else -1)
    for i in range(2):
        acento.append(cinta(espina(W * 0.5 + (i * 2 - 1) * 9, 74,
                                   math.radians(86 + (i * 2 - 1) * 6),
                                   H * 0.46, (i * 2 - 1) * 0.18, 12), 12))
    celdas = [hoja_celda(W * 0.5 + (i * 2 - 1) * 40, 150 + i * 40,
                         math.radians(80 + (i * 2 - 1) * 26), 92, 1.0)
              for i in range(2)]
    return W, H, entintar(hueso, acento, celdas,
                          rombos(W / 2, H * 0.70, H * 0.93, 4))


def p_pierna():
    """El pantalón: la rama sube por el muslo, asimétrica, como en el género."""
    W, H = 420, 1100
    hueso, acento = [], []
    for i in range(4):
        t = i / 3
        hueso += rama(W * 0.20 + 68 * t, H * 0.88 - 96 * t,
                      math.radians(-84 - 13 * t),
                      H * (0.42 - 0.07 * t), 20 - 5 * t,
                      0.62 + 0.3 * t, 3, i * 2.7, 1)
    for i in range(2):
        hueso += rama(W * 0.62 + 20 * i, H * 0.40 - 40 * i,
                      math.radians(-104 - 12 * i), H * 0.24, 15 - 4 * i,
                      -0.7, 2, 9 + i * 1.3, -1)
    for i in range(2):
        acento.append(cinta(espina(W * 0.34 + 22 * i, H * 0.80 - 40 * i,
                                   math.radians(-86 - 7 * i), H * 0.36,
                                   0.26, 12), 13 - 3 * i))
    celdas = [hoja_celda(W * 0.44 + 40 * i, H * 0.56 - 90 * i,
                         math.radians(-74 - 20 * i), 105, 1.0)
              for i in range(2)]
    return W, H, entintar(hueso, acento, celdas, "")


def p_pecho():
    """El pecho: el mismo armazón, en pequeño.

    A 10 cm no caben tres generaciones de rama: se empastan y sale un borrón.
    Aquí la V manda todavía más que en la espalda —es lo único que tiene que
    leerse a esta escala— y la filigrana se reduce a un plumaje corto colgado
    de los brazos. La proporción del armazón respecto a la costilla es la
    misma que en la dorsal, y `comprobar()` la vigila igual.
    """
    W, H = 380, 400
    eje = W / 2
    hueso, acento, celdas = [], [], []

    alto, vertice = 42.0, 214.0
    medio = W * 0.345
    hueso += armazon_vi(eje, alto, vertice, H * 0.94, medio,
                        GRUESO_ARMAZON * 0.42)

    # plumaje corto, colgado del brazo y hacia afuera
    for lado in (-1, 1):
        for i in range(4):
            f = 0.10 + 0.62 * i / 3
            ox = eje + lado * medio * (1 - f)
            oy = alto + (vertice - alto) * f
            ang = math.radians(-150 if lado < 0 else -30) - lado * math.radians(24 * f)
            hueso += rama(ox, oy, ang, W * (0.155 - 0.05 * f),
                          GRUESO_COSTILLA * 0.42 - 4 * f,
                          lado * (0.62 + 0.3 * f), 2, i * 2.4, lado)

    # dos hojas de acento a los lados de la I
    for lado in (-1, 1):
        acento.append(cinta(espina(eje + lado * 6, vertice - 18,
                                   math.radians(90) + lado * math.radians(9),
                                   H * 0.30, lado * 0.13, 10), 8))

    return W, H, entintar(hueso, acento, celdas,
                          arco(eje, 186, 104, -58, 58, 1.8, 18))


PIEZAS = {
    "es-dorsal": (p_dorsal, "Filigrana de espalda · la pieza mayor"),
    "es-pecho": (p_pecho, "Pecho · la misma gramática a 11 cm"),
    "es-manga": (p_manga, "Manga · rama que baja por el brazo"),
    "es-pierna": (p_pierna, "Pantalón · muslo y rodilla, asimétrica"),
}


# ---------------------------------------------------------------------------
# La prenda
# ---------------------------------------------------------------------------
# Una lámina suelta no dice si el dibujo funciona: lo que decide es a qué
# tamaño va sobre la tela. El torso son 32 cm, no los 52 de la prenda —las
# mangas se comen diez por lado—, y una lámina más ancha que el torso se
# estampa cortada. Eso no se ve hasta tener la prenda encima.
ANCHO_CM, ALTO_CM = 52.0, 72.0
PRENDA = {
    "espalda": ("es-dorsal", 28, 8, "Espalda · 28 cm, a 8 cm del cuello"),
    "pecho": ("es-pecho", 11, 14, "Pecho izquierdo · 11 cm, a 14 cm del hombro"),
}


def _silueta(px):
    W, H = ANCHO_CM * px, ALTO_CM * px
    h, c = W * 0.19, W * 0.115
    return (W, H, f'<path d="M{n(h)},{n(H * .07)} L{n(W / 2 - c)},{n(H * .035)} '
            f'Q{n(W / 2)},{n(H * .105)} {n(W / 2 + c)},{n(H * .035)} '
            f'L{n(W - h)},{n(H * .07)} L{n(W)},{n(H * .34)} '
            f'L{n(W - h * .72)},{n(H * .40)} L{n(W - h * .80)},{n(H)} '
            f'L{n(h * .80)},{n(H)} L{n(h * .72)},{n(H * .40)} L0,{n(H * .34)} Z" '
            f'fill="#101018" stroke="#2a2a38" stroke-width="1.6"/>')


def croquis(clave, px=11.0) -> str:
    sid, ancho_cm, arriba_cm, _t = PRENDA[clave]
    W, H, cuerpo = _silueta(px)
    pw, ph, _c = PIEZAS[sid][0]()
    ancho = ancho_cm * px
    x = (W - ancho) / 2 if clave != "pecho" else W * 0.585
    y = H * 0.07 + arriba_cm * px
    # Escala explícita y no <svg> anidado: dentro de un anidado el <use> no se
    # escala al hueco y la pieza sale a tamaño completo y recortada.
    return (f'<svg viewBox="0 0 {n(W)} {n(H)}">{cuerpo}'
            f'<g transform="translate({n(x)},{n(y)}) scale({n(ancho / pw)})">'
            f'<use href="#{sid}"/></g></svg>')


def construir() -> str:
    cuerpos = []
    for sid, (fn, _d) in PIEZAS.items():
        W, H, c = fn()
        # El símbolo NO fija el acento. Lo fijaba, y como el estilo en línea
        # gana al del contenedor, las tres columnas de la hoja salían cian.
        # Los valores por defecto viven en el <svg> de fuera.
        cuerpos.append(f'  <symbol id="{sid}" viewBox="0 0 {W} {H}">\n'
                       f'    {c}\n  </symbol>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0"\n'
            f'     style="position:absolute;--hueso:{HUESO};'
            f'--acento:{ACENTOS["cian"]}">\n'
            "<!-- VILLUMINATIONS · serie espina. Generado por\n"
            "     ropa/tools/dibujar-espinas.py. No se edita a mano. -->\n"
            + "\n".join(cuerpos) + "\n</svg>\n")


def sueltos() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    k = 0
    for sid, (fn, _d) in PIEZAS.items():
        W, H, c = fn()
        for nombre, hexa in ACENTOS.items():
            (DIST / f"{sid}-{nombre}.svg").write_text(
                f'<svg xmlns="http://www.w3.org/2000/svg" '
                f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
                f'style="--hueso:{HUESO}; --acento:{hexa}">\n{c}\n</svg>\n',
                encoding="utf-8")
            k += 1
    return k


def comprobar() -> list:
    malos = []
    # Lo que hace legible la marca a tres metros no es su tamaño: es que el
    # armazón sea claramente más macizo que la filigrana que lo rodea. Si
    # algún día se engorda la costilla sin mirar esto, la V se pierde dentro
    # del bulto y nadie se entera hasta ver la prenda impresa.
    if GRUESO_ARMAZON < GRUESO_COSTILLA * ARMAZON_MINIMO:
        malos.append(
            f"el armazón ({GRUESO_ARMAZON}) no llega a {ARMAZON_MINIMO}× la "
            f"costilla mayor ({GRUESO_COSTILLA}): la V dejaría de leerse")
    torso = ANCHO_CM * (1 - 0.19 * 2)
    for clave, (sid, ancho_cm, _a, _t) in PRENDA.items():
        if ancho_cm > torso - 2:
            malos.append(f"{clave} · {ancho_cm} cm sobre un torso de "
                         f"{torso:.0f} cm: se estamparía cortada")
    for sid, (fn, _d) in PIEZAS.items():
        W, H, c = fn()
        if "var(--acento)" not in c or "var(--hueso)" not in c:
            malos.append(f"{sid} · no usa las dos variables: no se podría "
                         f"sacar en los siete acentos desde un solo dibujo")
        # El halo tiene que ir DEBAJO del hueso o el color queda encima y son
        # dos tintas planas. Se comprueba por el orden en la cadena.
        if c.index("var(--hueso)") < c.index("var(--acento)"):
            malos.append(f"{sid} · el hueso se dibuja antes que el acento: "
                         f"el color quedaría encima y se pierde el brillo")
        if "NaN" in c:
            malos.append(f"{sid} · hay NaN en el trazado")
    return malos


def hoja() -> int:
    S = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
             "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")
    S.mkdir(parents=True, exist_ok=True)
    celdas = []
    for clave, (sid, _w, _a, titulo) in PRENDA.items():
        celdas.append(f'<figure style="--hueso:{HUESO};'
                      f'--acento:{ACENTOS["cian"]}">{croquis(clave)}'
                      f'<figcaption>{sid}<span>{titulo}</span></figcaption>'
                      f'</figure>')
    for sid, (fn, desc) in PIEZAS.items():
        W, H, _c = fn()
        for color in ("cian", "purpura", "magenta"):
            celdas.append(
                f'<figure style="--hueso:{HUESO};--acento:{ACENTOS[color]}">'
                f'<svg viewBox="0 0 {W} {H}"><use href="#{sid}"/></svg>'
                f'<figcaption>{sid} · {color}<span>{desc}</span></figcaption>'
                f'</figure>')
    html = f"""<!doctype html><meta charset=utf-8><style>
body{{margin:0;background:#050508;color:#eef2ff;font:12px/1.5 Georgia,serif;
 padding:20px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px;
 align-items:start}}
figure{{margin:0;background:#0a0a0f;padding:16px;border:1px solid #17171f}}
svg{{width:100%;height:auto;max-height:640px}}
figcaption{{margin-top:10px;letter-spacing:.1em;font-size:11px}}
figcaption span{{display:block;opacity:.4;letter-spacing:.02em;margin-top:3px}}
</style>{PARTIALS.read_text(encoding="utf-8")}{"".join(celdas)}"""
    (S / "espinas.html").write_text(html, encoding="utf-8")
    (S / "espinas.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        "const p = await b.newPage({viewport:{width:1700,height:1200}});\n"
        f"await p.goto('file://{S}/espinas.html');\n"
        f"await p.screenshot({{path:'{S}/espinas.png',fullPage:true}});\n"
        "await b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(S / "espinas.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        print(f"    no se pudo renderizar:\n{r.stderr}")
        return 1
    print(f"    {S}/espinas.png")
    return 0


def main() -> int:
    malos = comprobar()
    print(f"\n  {len(PIEZAS)} piezas · {len(ACENTOS)} acentos · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if malos:
        return 1
    PARTIALS.parent.mkdir(parents=True, exist_ok=True)
    PARTIALS.write_text(construir(), encoding="utf-8")
    print(f"    {PARTIALS.relative_to(RAIZ.parent)}  "
          f"{PARTIALS.stat().st_size // 1024} KB")
    print(f"    {sueltos()} ficheros en {DIST.relative_to(RAIZ.parent)}/\n")
    for sid, (fn, desc) in PIEZAS.items():
        W, H, _c = fn()
        print(f"    {sid:12} {W:>5} × {H:<5} {desc}")
    print()
    if "--hoja" in sys.argv:
        return hoja()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
