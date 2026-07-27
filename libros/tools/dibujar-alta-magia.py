#!/usr/bin/env python3
"""
CÓDICE DE LAS INVOCACIONES — generador del repertorio gráfico
=============================================================
Escribe partials/alta-magia.svg. Dibujo original de VILLUMINATION 99 sobre
material de tradición común: el pentagrama y el hexagrama con sus atribuciones
elementales y planetarias, el árbol de los diez números, el círculo de los
cuatro cuartos, las cuatro armas y los siete cuadrados planetarios.

Los cuadrados mágicos son aritmética pura y se calculan aquí en vez de
copiarse: así se comprueban solos. Los tres algoritmos clásicos —impar,
doblemente par y simplemente par— cubren los siete órdenes del 3 al 9.

    python3 tools/dibujar-alta-magia.py
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "partials" / "alta-magia.svg"

ORO = "#ffd75c"       # el color del oficio en este libro
PLATA = "#9fb0d8"

SIGILOS = {           # los mismos trazos que en el Códice Zodiacal
    "sol": ('M100 58 a42 42 0 1 0 .1 0 Z', 'M100 100 m-7 0 a7 7 0 1 0 14 0 a7 7 0 1 0 -14 0'),
    "luna": ('M116 56 A46 46 0 1 0 116 144 A36 36 0 1 1 116 56 Z', None),
    "mercurio": ('M100 70 a26 26 0 1 0 .1 0 Z M100 122 V154 M80 140 H120 '
                 'M74 56 A32 32 0 0 0 126 56', None),
    "venus": ('M100 54 a28 28 0 1 0 .1 0 Z M100 110 V158 M78 136 H122', None),
    "marte": ('M88 84 a30 30 0 1 0 .1 0 Z M110 92 L150 52 M150 52 H117 M150 52 V85', None),
    "jupiter": ('M52 76 C63 48 92 53 92 78 V150 M66 150 H134 M52 76 H60', None),
    "saturno": ('M54 66 H104 M79 52 V116 C79 148 130 150 134 116 '
                'C137 90 108 82 96 102', None),
}

# Orden caldeo: del más lento al más rápido en su recorrido aparente. Manda en
# el reparto de las horas planetarias y de los decanatos.
CALDEO = ["saturno", "jupiter", "marte", "sol", "venus", "mercurio", "luna"]

PLANETAS = {                 # nombre y metal
    "saturno":  ("Saturno",  "Plomo"),
    "jupiter":  ("Júpiter",  "Estaño"),
    "marte":    ("Marte",    "Hierro"),
    "sol":      ("Sol",      "Oro"),
    "venus":    ("Venus",    "Cobre"),
    "mercurio": ("Mercurio", "Azogue"),
    "luna":     ("Luna",     "Plata"),
}

ELEMENTO_MARCA = {
    "fuego":  "M0 16 L12 -6 L24 16 Z",
    "aire":   "M0 16 L12 -6 L24 16 Z M4.5 7 H19.5",
    "agua":   "M0 -6 H24 L12 16 Z",
    "tierra": "M0 -6 H24 L12 16 Z M4.5 1.5 H19.5",
}


# ── Utilidades ────────────────────────────────────────────────────────
def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, grados):
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def txt(x, y, s, clase="et", tam=11, color=PLATA, anchor="middle"):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}">{s}</text>')


def sigilo(clave, x, y, lado, color=ORO):
    k = lado / 200
    trazo, relleno = SIGILOS[clave]
    extra = (f'<path d="{relleno}" fill="currentColor" stroke="none"/>'
             if relleno else "")
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" class="tz" '
            f'color="{color}" stroke-width="{f((lado / 11) / k)}">'
            f'<path d="{trazo}"/>{extra}</g>')


def marca(elemento, x, y, lado=24, color=ORO):
    k = lado / 24
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" fill="none" '
            f'stroke="{color}" stroke-width="{f(2.2 / k)}" stroke-linejoin="round">'
            f'<path d="{ELEMENTO_MARCA[elemento]}"/></g>')


# ══════════════════════════════════════════════════════════════════════
#  CUADRADOS MÁGICOS · se calculan, no se copian
# ══════════════════════════════════════════════════════════════════════
def kamea(n):
    """Cuadrado mágico de orden n. Tres algoritmos según la paridad."""
    if n % 2 == 1:
        return _impar(n)
    if n % 4 == 0:
        return _doblemente_par(n)
    return _simplemente_par(n)


def _impar(n):
    """Método siamés: se avanza en diagonal arriba-derecha y, cuando la
    casilla está ocupada, se baja una."""
    m = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for k in range(1, n * n + 1):
        m[i][j] = k
        ni, nj = (i - 1) % n, (j + 1) % n
        if m[ni][nj]:
            ni, nj = (i + 1) % n, j
        i, j = ni, nj
    return m


def _doblemente_par(n):
    """n divisible por 4: se rellena en orden y se invierten las casillas
    de las diagonales de cada bloque de 4×4."""
    m = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i % 4 in (0, 3)) == (j % 4 in (0, 3)):
                m[i][j] = n * n + 1 - m[i][j]
    return m


def _simplemente_par(n):
    """n ≡ 2 (mod 4): método LUX de Conway sobre un cuadrado impar de n/2."""
    mitad = n // 2
    base = _impar(mitad)
    k = (mitad - 1) // 2
    m = [[0] * n for _ in range(n)]
    # L en las k+1 primeras filas, U en la siguiente, X en el resto;
    # la fila central intercambia su L por una U.
    patron = ["L"] * (k + 1) + ["U"] + ["X"] * (mitad - k - 2)
    for i in range(mitad):
        for j in range(mitad):
            tipo = patron[i]
            if i == k and j == k:
                tipo = "U"
            elif i == k + 1 and j == k:
                tipo = "L"
            base4 = 4 * (base[i][j] - 1)
            cuadrantes = {
                "L": [(4, 1), (2, 3)],
                "U": [(1, 4), (2, 3)],
                "X": [(1, 4), (3, 2)],
            }[tipo]
            m[2 * i][2 * j] = base4 + cuadrantes[0][0]
            m[2 * i][2 * j + 1] = base4 + cuadrantes[0][1]
            m[2 * i + 1][2 * j] = base4 + cuadrantes[1][0]
            m[2 * i + 1][2 * j + 1] = base4 + cuadrantes[1][1]
    return m


KAMEAS = [
    ("saturno", 3, "Saturno"), ("jupiter", 4, "Júpiter"),
    ("marte", 5, "Marte"), ("sol", 6, "Sol"),
    ("venus", 7, "Venus"), ("mercurio", 8, "Mercurio"),
    ("luna", 9, "Luna"),
]


def comprobar():
    """Un cuadrado mágico que no suma no es un cuadrado mágico. Si algún
    algoritmo falla, mejor que el generador se niegue a escribir el fichero."""
    for _, n, nombre in KAMEAS:
        m = kamea(n)
        objetivo = n * (n * n + 1) // 2
        sumas = ([sum(fila) for fila in m]
                 + [sum(c) for c in zip(*m)]
                 + [sum(m[i][i] for i in range(n))]
                 + [sum(m[i][n - 1 - i] for i in range(n))])
        if set(sumas) != {objetivo} or sorted(x for fila in m for x in fila) != list(range(1, n * n + 1)):
            raise SystemExit(f"El cuadrado de {nombre} ({n}×{n}) no cuadra: {sorted(set(sumas))}")
    return True


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · EL PENTAGRAMA
# ══════════════════════════════════════════════════════════════════════
PUNTAS = [   # ángulo, elemento, etiqueta
    (0,   None,     "ESPÍRITU"),
    (72,  "agua",   "AGUA"),
    (144, "fuego",  "FUEGO"),
    (216, "tierra", "TIERRA"),
    (288, "aire",   "AIRE"),
]


def lamina_pentagrama():
    """Las dos direcciones del trazo. No se dibuja la estrella y encima el
    recorrido: el recorrido ES la estrella, trazada de un tirón en un orden
    concreto. Lo único que cambia entre invocar y despedir es por dónde se
    empieza y hacia dónde se va, y eso lo marcan el punto y la flecha."""
    p = ['<symbol id="am-pentagrama" viewBox="0 0 464 288">']
    for lado, (titulo, glosa, orden) in enumerate((
            ("INVOCAR", "de Tierra a Espíritu", [3, 0, 2, 4, 1, 3]),
            ("DESPEDIR", "de Espíritu a Tierra", [0, 3, 1, 4, 2, 0]))):
        cx, cy, r = 118 + lado * 228, 118, 66
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 14}" fill="none" '
                 f'stroke="{ORO}" stroke-width=".9" opacity=".28"/>')
        est = [pol(cx, cy, r, a) for a, _, _ in PUNTAS]
        traz = "M" + " L".join(f"{f(est[i][0])} {f(est[i][1])}" for i in orden)
        p.append(f'<path d="{traz}" fill="{ORO}" fill-opacity=".05" '
                 f'stroke="{ORO}" stroke-width="2" stroke-linejoin="round"/>')
        # Punto de arranque y flecha a mitad del primer trazo.
        (x0, y0), (x1, y1) = est[orden[0]], est[orden[1]]
        p.append(f'<circle cx="{f(x0)}" cy="{f(y0)}" r="5" fill="{ORO}"/>')
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        p.append(f'<g transform="translate({f(mx)},{f(my)}) rotate({f(ang)})" '
                 f'fill="{ORO}"><path d="M7 0 L-4 5 L-4 -5 Z"/></g>')
        for a, elemento, etiqueta in PUNTAS:
            ex, ey = pol(cx, cy, r + 22, a)
            if a == 0:                       # arriba
                if elemento:
                    p.append(marca(elemento, ex - 6, ey - 6, 12))
                p.append(txt(cx, cy - r - 24, etiqueta, "rot", 8.4, ORO))
            elif a in (72, 288):
                # Los dos brazos horizontales van rotulados POR DENTRO. Fuera
                # no caben: dos ruedas de este tamaño más sus etiquetas se
                # comen los 464 de ancho y las de en medio se solapan.
                bx, by = pol(cx, cy, r, a)
                if elemento:
                    p.append(marca(elemento, bx - 6, by + 22, 12))
                p.append(txt(bx, by - 12, etiqueta, "rot", 8.4, ORO))
            else:                            # las dos patas, debajo
                if elemento:
                    p.append(marca(elemento, ex - 6, ey + 6, 12))
                p.append(txt(ex, ey + 26, etiqueta, "rot", 8.4, ORO))
        p.append(txt(cx, 252, titulo, "rot", 11.5, ORO))
        p.append(txt(cx, 270, glosa, "et", 11, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · EL HEXAGRAMA
# ══════════════════════════════════════════════════════════════════════
HEXA = [(0, "saturno", "SATURNO"), (60, "jupiter", "JÚPITER"),
        (120, "marte", "MARTE"), (180, "luna", "LUNA"),
        (240, "mercurio", "MERCURIO"), (300, "venus", "VENUS")]


def lamina_hexagrama():
    cx, cy, r = 232, 160, 116
    p = ['<symbol id="am-hexagrama" viewBox="0 0 464 348">']
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="none" '
             f'stroke="{ORO}" stroke-width=".9" opacity=".3"/>')
    for base in (0, 180):
        pts = [pol(cx, cy, r, base + k * 120) for k in range(3)]
        d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
        p.append(f'<path d="{d}" fill="{ORO}" fill-opacity=".05" stroke="{ORO}" '
                 'stroke-width="1.6" stroke-linejoin="round"/>')
    for a, planeta, etiqueta in HEXA:
        sx, sy = pol(cx, cy, r, a)
        p.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="15" fill="#080810" '
                 f'stroke="{ORO}" stroke-width="1"/>')
        p.append(sigilo(planeta, sx - 10, sy - 10, 20))
        ex, ey = pol(cx, cy, r + 32, a)
        p.append(txt(ex, ey + (11 if 90 < a < 270 else 0), etiqueta, "rot", 8.4, ORO))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#080810" stroke="{ORO}" '
             'stroke-width="1.2"/>')
    p.append(sigilo("sol", cx - 16, cy - 16, 32))
    p.append(txt(cx, 342, "EL SOL EN EL CENTRO · LOS SEIS ALREDEDOR", "rot", 8.6, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · EL ÁRBOL DE LOS DIEZ NÚMEROS
# ══════════════════════════════════════════════════════════════════════
#   n, nombre, traducción, columna (-1 izq, 0 centro, 1 der), y
ARBOL = [
    (1,  "Kéter",   "La corona",     0, 46),
    (2,  "Jojmá",   "La sabiduría",  1, 122),
    (3,  "Biná",    "La inteligencia", -1, 122),
    (4,  "Jésed",   "La clemencia",  1, 218),
    (5,  "Guevurá", "el rigor",     -1, 218),
    (6,  "Tiféret", "La belleza",    0, 296),
    (7,  "Nétsaj",  "La victoria",   1, 372),
    (8,  "Hod",     "La gloria",    -1, 372),
    (9,  "Yesod",   "El fundamento", 0, 442),
    (10, "Maljut",  "El reino",      0, 504),
]

SENDEROS = [(1, 2), (1, 3), (1, 6), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6),
            (4, 5), (4, 6), (4, 7), (5, 6), (5, 8), (6, 7), (6, 8), (6, 9),
            (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]


def lamina_arbol():
    R, CX, DX = 25, 232, 80
    pos = {n: (CX + col * DX, y) for n, _, _, col, y in ARBOL}
    p = ['<symbol id="am-arbol" viewBox="0 0 464 552">']
    # Los tres pilares, al fondo
    for col, etiqueta in ((-1, "RIGOR"), (0, "EQUILIBRIO"), (1, "CLEMENCIA")):
        x = CX + col * DX
        p.append(f'<path d="M{x} 30 V520" fill="none" stroke="{PLATA}" '
                 'stroke-width="14" opacity=".05"/>')
        p.append(txt(x, 20, etiqueta, "rot", 8, PLATA))
    # Los veintidós senderos
    d = " ".join(f"M{pos[a][0]} {pos[a][1]} L{pos[b][0]} {pos[b][1]}"
                 for a, b in SENDEROS)
    p.append(f'<path d="{d}" fill="none" stroke="{ORO}" stroke-width=".9" '
             'opacity=".38"/>')
    for n, nombre, trad, col, y in ARBOL:
        x = CX + col * DX
        p.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="#080810" '
                 f'stroke="{ORO}" stroke-width="1.4"/>')
        p.append(f'<circle cx="{x}" cy="{y}" r="{R - 5}" fill="none" '
                 f'stroke="{ORO}" stroke-width=".6" opacity=".4"/>')
        p.append(txt(x, y + 6, str(n), "num", 15, ORO))
        # Etiqueta: fuera del pilar en los laterales, y a la derecha con más
        # separación en el central (donde no hay nada que estorbe).
        if col == -1:
            ax, an = x - R - 12, "end"
        elif col == 1:
            ax, an = x + R + 12, "start"
        else:
            ax, an = x + R + 34, "start"
        p.append(txt(ax, y - 2, nombre, "rot", 10.4, ORO, an))
        p.append(txt(ax, y + 12, trad, "et", 10.4, PLATA, an))
    p.append(txt(CX, 546, "DIEZ NÚMEROS · VEINTIDÓS SENDEROS", "rot", 8.6, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · EL CÍRCULO Y LOS CUATRO CUARTOS
# ══════════════════════════════════════════════════════════════════════
CUARTOS = [   # ángulo, punto cardinal, elemento, custodio, hora
    (0,   "NORTE", "tierra", "El cuerpo",   "Medianoche"),
    (90,  "ESTE",  "aire",   "El aliento",  "Amanecer"),
    (180, "SUR",   "fuego",  "La voluntad", "Mediodía"),
    (270, "OESTE", "agua",   "La memoria",  "Atardecer"),
]


def lamina_circulo():
    """La rueda no puede ocupar el ancho entero: el triángulo va fuera del
    círculo, al este, y necesita su sitio a la derecha."""
    cx, cy = 156, 176
    p = ['<symbol id="am-circulo" viewBox="0 0 464 372">']
    for r, w, op in ((146, 1.4, .8), (130, .8, .32), (96, .8, .28), (28, 1.2, .7)):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                 f'stroke="{ORO}" stroke-width="{w}" opacity="{op}"/>')
    p.append(f'<path d="M{cx} {cy - 146} V{cy + 146} M{cx - 146} {cy} H{cx + 146}" '
             f'fill="none" stroke="{ORO}" stroke-width=".8" opacity=".22"/>')
    for a, cardinal, elemento, custodio, hora in CUARTOS:
        px, py = pol(cx, cy, 138, a)
        p.append(f'<circle cx="{f(px)}" cy="{f(py)}" r="12" fill="#080810" '
                 f'stroke="{ORO}" stroke-width="1"/>')
        p.append(marca(elemento, px - 5.5, py + 3.5, 11))
        ex, ey = pol(cx, cy, 111, a)
        ancho = len(cardinal) * 6.4 + 8
        p.append(f'<rect x="{f(ex - ancho / 2)}" y="{f(ey - 8)}" '
                 f'width="{f(ancho)}" height="16" rx="3" fill="#080810"/>')
        p.append(txt(ex, ey + 3.5, cardinal, "rot", 8.4, ORO))
        gx, gy = pol(cx, cy, 66, a)
        p.append(txt(gx, gy - 1, custodio, "rot", 8.8, PLATA))
        p.append(txt(gx, gy + 11, hora, "et", 10, PLATA))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{ORO}"/>')
    p.append(txt(cx, cy + 19, "AQUÍ", "rot", 7.4, ORO))
    # El triángulo de trabajo, fuera del círculo y al este.
    tx = 386
    p.append(f'<path d="M{tx} {cy - 46} L{tx + 46} {cy + 34} L{tx - 46} {cy + 34} Z" '
             f'fill="{ORO}" fill-opacity=".05" stroke="{ORO}" stroke-width="1.2" '
             'stroke-linejoin="round"/>')
    p.append(f'<path d="M{cx + 150} {cy} H{tx - 50}" fill="none" stroke="{ORO}" '
             'stroke-width=".8" stroke-dasharray="4 4" opacity=".5"/>')
    p.append(txt(tx, cy + 54, "LO QUE SE EXAMINA", "rot", 8, PLATA))
    p.append(txt(tx, cy + 68, "queda fuera", "et", 10.4, PLATA))
    p.append(txt(232, 366, "EL CÍRCULO ES EL LÍMITE DE LO PROPIO", "rot", 8.6, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LAS CUATRO ARMAS
# ══════════════════════════════════════════════════════════════════════
ARMAS = [
    ("fuego", "LA VARA", "Voluntad",
     "M20 118 L88 34 M84 30 l10 -4 -4 10 Z M20 118 l-8 8 12 4 Z"),
    ("agua", "LA COPA", "Sentimiento",
     "M22 34 H86 M24 34 C24 74 40 92 54 94 C68 92 84 74 84 34 M54 94 V116 "
     "M34 122 H74"),
    ("aire", "LA ESPADA", "Pensamiento",
     "M54 26 V96 M34 96 H74 M54 96 V118 M44 118 H64"),
    ("tierra", "EL DISCO", "Cuerpo",
     "M54 30 a34 34 0 1 0 .1 0 Z M54 30 L54 98 M20 64 H88 M30 40 L78 88 "
     "M78 40 L30 88"),
]


def lamina_armas():
    p = ['<symbol id="am-armas" viewBox="0 0 464 210">']
    for i, (elemento, nombre, glosa, trazo) in enumerate(ARMAS):
        ox = i * 116
        p.append(f'<rect x="{ox + 8}" y="6" width="100" height="150" rx="8" '
                 f'fill="{ORO}" opacity=".04"/>')
        p.append(f'<g transform="translate({ox + 4},14)" fill="none" '
                 f'stroke="{ORO}" stroke-width="2" stroke-linecap="round" '
                 'stroke-linejoin="round">'
                 f'<path d="{trazo}"/></g>')
        p.append(marca(elemento, ox + 46, 148, 16))
        p.append(txt(ox + 58, 178, nombre, "rot", 9.6, ORO))
        p.append(txt(ox + 58, 194, glosa, "et", 11, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LOS CUADRADOS PLANETARIOS
# ══════════════════════════════════════════════════════════════════════
def cuadro(m, x, y, lado, planeta, nombre):
    n = len(m)
    c = lado / n
    salida = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(lado)}" '
              f'height="{f(lado)}" rx="3" fill="{ORO}" opacity=".05"/>']
    rejilla = []
    for k in range(n + 1):
        rejilla.append(f"M{f(x)} {f(y + k * c)} H{f(x + lado)}")
        rejilla.append(f"M{f(x + k * c)} {f(y)} V{f(y + lado)}")
    salida.append(f'<path d="{" ".join(rejilla)}" fill="none" stroke="{ORO}" '
                  'stroke-width=".5" opacity=".35"/>')
    tam = min(11.5, c * 0.62)
    for i, fila in enumerate(m):
        for j, v in enumerate(fila):
            salida.append(txt(x + j * c + c / 2, y + i * c + c / 2 + tam * .36,
                              str(v), "num", tam, PLATA))
    salida.append(sigilo(planeta, x - 2, y - 30, 26))
    salida.append(txt(x + 30, y - 12, nombre.upper(), "rot", 9, ORO, "start"))
    suma = n * (n * n + 1) // 2
    salida.append(txt(x + lado, y - 12, f"{n}×{n} · SUMA {suma}", "rot", 8, PLATA, "end"))
    return "".join(salida)


def lamina_kameas():
    """Los cuatro primeros, que son los que caben legibles en una página A5."""
    p = ['<symbol id="am-kameas" viewBox="0 0 464 480">']
    for k, (planeta, n, nombre) in enumerate(KAMEAS[:4]):
        x = 26 + (k % 2) * 232
        y = 46 + (k // 2) * 232
        p.append(cuadro(kamea(n), x, y, 176, planeta, nombre))
    p.append(txt(232, 474, "CADA FILA, CADA COLUMNA Y CADA DIAGONAL SUMAN LO MISMO",
                 "rot", 8.4, PLATA))
    p.append("</symbol>")
    return "".join(p)



# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LA TABLA COMPLETA DE LAS HORAS PLANETARIAS
# ══════════════════════════════════════════════════════════════════════
DIAS = [("Domingo", "sol"), ("Lunes", "luna"), ("Martes", "marte"),
        ("Miércoles", "mercurio"), ("Jueves", "jupiter"), ("Viernes", "venus"),
        ("Sábado", "saturno")]

# Iniciales para la rejilla. Se usan letras y no sigilos porque ciento sesenta
# y ocho sigilos a este tamaño serían una mancha; el sigilo se reserva para la
# columna del regente del día, que es donde se lee.
INICIAL = {"saturno": "♄", "jupiter": "♃", "marte": "♂", "sol": "☉",
           "venus": "♀", "mercurio": "☿", "luna": "☾"}
LETRA = {"saturno": "SA", "jupiter": "JU", "marte": "MA", "sol": "SO",
         "venus": "VE", "mercurio": "ME", "luna": "LU"}


def horas_del_dia(regente):
    """Las veinticuatro horas de un día, en orden caldeo descendente desde su
    propio regente. La hora 1 es siempre la del planeta que da nombre al día."""
    i = CALDEO.index(regente)
    return [CALDEO[(i + k) % 7] for k in range(24)]


def comprobar_horas():
    """La prueba de que el reparto explica la semana: la hora 25 —la primera
    del día siguiente— tiene que caer en el regente del día siguiente. Si esto
    falla, el capítulo entero del libro es falso y el generador no escribe."""
    for k, (nombre, regente) in enumerate(DIAS):
        siguiente = DIAS[(k + 1) % 7]
        i = CALDEO.index(regente)
        hora25 = CALDEO[(i + 24) % 7]
        if hora25 != siguiente[1]:
            raise SystemExit(
                f"{nombre}: la hora 25 cae en {hora25} y debería caer en "
                f"{siguiente[1]} ({siguiente[0]})")
    return True


def lamina_horas():
    FILA, X0, CELDA = 42, 92, 15.2
    ALTO = 46 + 7 * FILA + 16
    p = [f'<symbol id="am-horas" viewBox="0 0 464 {ALTO}">']
    # cabecera de horas
    for h in range(24):
        x = X0 + h * CELDA + CELDA / 2
        if (h + 1) % 3 == 0 or h == 0:
            p.append(txt(x, 16, str(h + 1), "num", 7.4, PLATA))
    p.append(txt(X0 + 12 * CELDA, 32, "HORA DEL DÍA · 1 AL AMANECER · 13 AL ATARDECER",
                 "rot", 7, ORO))
    p.append(f'<path d="M{f(X0)} 38 H{f(X0 + 24 * CELDA)}" fill="none" '
             f'stroke="{ORO}" stroke-width=".9" opacity=".45"/>')
    for k, (nombre, regente) in enumerate(DIAS):
        y = 46 + k * FILA
        p.append(sigilo(regente, 6, y + 6, 26))
        p.append(txt(38, y + 16, nombre, "et", 11, ORO, "start"))
        p.append(txt(38, y + 29, PLANETAS[regente][0], "et", 10, PLATA, "start"))
        for h, planeta in enumerate(horas_del_dia(regente)):
            x = X0 + h * CELDA
            noche = h >= 12
            # La hora que coincide con el regente del día se resalta: son las
            # cuatro veces al día en que «manda» el planeta del día.
            propia = planeta == regente
            p.append(f'<rect x="{f(x)}" y="{f(y + 4)}" width="{f(CELDA - 1)}" '
                     f'height="30" rx="2" fill="{ORO}" '
                     f'opacity="{.22 if propia else (.05 if noche else .09)}"/>')
            p.append(txt(x + CELDA / 2 - .5, y + 15, LETRA[planeta][0], "rot", 8,
                         ORO if propia else PLATA))
            p.append(txt(x + CELDA / 2 - .5, y + 27, LETRA[planeta][1], "rot", 8,
                         ORO if propia else PLATA))
        # separación entre día y noche
        p.append(f'<path d="M{f(X0 + 12 * CELDA - .5)} {f(y + 2)} '
                 f'V{f(y + 36)}" fill="none" stroke="{ORO}" stroke-width="1.2" '
                 'opacity=".6"/>')
    p.append(txt(232, ALTO - 4,
                 "24 ÷ 7 = 3 Y SOBRAN 3 · POR ESO LA SEMANA VA DE TRES EN TRES",
                 "rot", 7.6, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LAS VEINTIDÓS LETRAS Y SUS NÚMEROS
# ══════════════════════════════════════════════════════════════════════
# Reparto del Sefer Yetsirá: tres madres para los elementos, siete dobles para
# los planetas y doce simples para los signos. Los valores son los del alfabeto
# hebreo y su suma es un dato comprobable.
LETRAS = [
    ("Álef", 1, "madre", "Aire"),        ("Bet", 2, "doble", "Saturno"),
    ("Guímel", 3, "doble", "Júpiter"),   ("Dálet", 4, "doble", "Marte"),
    ("He", 5, "simple", "Aries"),        ("Vav", 6, "simple", "Tauro"),
    ("Zayin", 7, "simple", "Géminis"),   ("Jet", 8, "simple", "Cáncer"),
    ("Tet", 9, "simple", "Leo"),         ("Yod", 10, "simple", "Virgo"),
    ("Kaf", 20, "doble", "Sol"),         ("Lámed", 30, "simple", "Libra"),
    ("Mem", 40, "madre", "Agua"),        ("Nun", 50, "simple", "Escorpio"),
    ("Sámej", 60, "simple", "Sagitario"), ("Ayin", 70, "simple", "Capricornio"),
    ("Pe", 80, "doble", "Venus"),        ("Tsade", 90, "simple", "Acuario"),
    ("Qof", 100, "simple", "Piscis"),    ("Resh", 200, "doble", "Mercurio"),
    ("Shin", 300, "madre", "Fuego"),     ("Tav", 400, "doble", "Luna"),
]

TONO = {"madre": ORO, "doble": "#ff9d5c", "simple": PLATA}


def comprobar_letras():
    if len(LETRAS) != 22:
        raise SystemExit(f"El alfabeto tiene {len(LETRAS)} letras, no 22")
    cuenta = {"madre": 0, "doble": 0, "simple": 0}
    for _, _, clase, _ in LETRAS:
        cuenta[clase] += 1
    if cuenta != {"madre": 3, "doble": 7, "simple": 12}:
        raise SystemExit(f"El reparto 3-7-12 no cuadra: {cuenta}")
    total = sum(v for _, v, _, _ in LETRAS)
    if total != 1495:
        raise SystemExit(f"Los valores suman {total} y deberían sumar 1495")
    return True


def lamina_alfabeto():
    FILA, COL = 30, 232
    ALTO = 40 + 11 * FILA + 36
    p = [f'<symbol id="am-alfabeto" viewBox="0 0 464 {ALTO}">']
    for c in range(2):
        x = 8 + c * COL
        p.append(txt(x + 4, 18, "LETRA", "rot", 7.4, ORO, "start"))
        p.append(txt(x + 78, 18, "VALOR", "rot", 7.4, ORO, "end"))
        p.append(txt(x + 90, 18, "LE CORRESPONDE", "rot", 7.4, ORO, "start"))
        p.append(f'<path d="M{x} 24 H{x + 214}" fill="none" stroke="{ORO}" '
                 'stroke-width=".8" opacity=".45"/>')
    for i, (nombre, valor, clase, corresp) in enumerate(LETRAS):
        c, fila = i // 11, i % 11
        x = 8 + c * COL
        y = 40 + fila * FILA
        col = TONO[clase]
        p.append(f'<rect x="{x}" y="{f(y - 12)}" width="214" height="26" rx="4" '
                 f'fill="{col}" opacity=".06"/>')
        p.append(f'<circle cx="{x + 8}" cy="{f(y + 1)}" r="3" fill="{col}"/>')
        p.append(txt(x + 18, y + 5, nombre, "et", 11.5, col, "start"))
        p.append(txt(x + 78, y + 5, str(valor), "num", 10.5, PLATA, "end"))
        p.append(txt(x + 90, y + 5, corresp, "et", 11, PLATA, "start"))
    leyenda = [("madre", "3 madres · elementos"), ("doble", "7 dobles · planetas"),
               ("simple", "12 simples · signos")]
    for k, (clase, etq) in enumerate(leyenda):
        x = 20 + k * 150
        p.append(f'<circle cx="{x}" cy="{ALTO - 26}" r="3.4" fill="{TONO[clase]}"/>')
        p.append(txt(x + 10, ALTO - 22, etq, "rot", 7.4, TONO[clase], "start"))
    p.append(txt(232, ALTO - 4, "LOS VEINTIDÓS VALORES SUMAN 1 495", "rot", 7.6, PLATA))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
def main():
    comprobar()
    comprobar_horas()
    comprobar_letras()
    piezas = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'style="position:absolute;width:0;height:0;overflow:hidden" '
        'aria-hidden="true">',
        """
<!-- ════════════════════════════════════════════════════════════════
     CÓDICE DE LAS INVOCACIONES · repertorio gráfico
     Dibujo original de VILLUMINATION 99 — generado por
     tools/dibujar-alta-magia.py. No editar a mano.
     ════════════════════════════════════════════════════════════ -->""",
        '<style>'
        'svg .tz{ fill:none; stroke:currentColor; stroke-linecap:round;'
        ' stroke-linejoin:round }'
        "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
        ' letter-spacing:.1em }'
        "svg .num{ font-family:'Orbitron',sans-serif; font-weight:600 }"
        "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
        '</style>',
        lamina_pentagrama(),
        lamina_hexagrama(),
        lamina_arbol(),
        lamina_circulo(),
        lamina_armas(),
        lamina_kameas(),
        lamina_horas(),
        lamina_alfabeto(),
        "</svg>",
    ]
    DESTINO.write_text("\n".join(piezas) + "\n")
    print(f"  {DESTINO.relative_to(RAIZ)}: 8 láminas · "
          f"cuadrados, horas y alfabeto comprobados · "
          f"{DESTINO.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
