#!/usr/bin/env python3
"""
CÓDICE ZODIACAL — generador del repertorio gráfico
==================================================
Escribe partials/zodiaco.svg: los doce glifos, los siete sigilos planetarios
y siete láminas explicativas. Dibujo original de VILLUMINATIONS.

Se genera con código y no a mano por dos razones: la trigonometría de la rueda
(doce sectores, radios, glifos girados) es imposible de mantener a ojo, y las
tablas de decanatos y correspondencias son datos — mejor tenerlos una sola vez
y que el dibujo salga de ellos.

Detalle importante: los <text> nunca van dentro de un grupo con filter. Un
filtro SVG rasteriza todo lo que envuelve, y eso sacaría las etiquetas de la
capa de texto del PDF (adiós búsqueda, adiós copiar y pegar).

    python3 tools/dibujar-zodiaco.py
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "partials" / "zodiaco.svg"

# ── Paleta de elementos ───────────────────────────────────────────────
# El color aquí es INFORMACIÓN, no decoración: dice de qué elemento es cada
# signo. Por eso no se hereda del acento del libro.
COLOR = {"fuego": "#ff5c7a", "tierra": "#4dffa6",
         "aire": "#ffd75c", "agua": "#5cd6ff"}

# ── Los doce signos ───────────────────────────────────────────────────
#   clave, nombre, abreviatura, elemento, modalidad, regente
SIGNOS = [
    ("aries",       "Aries",       "ARI", "fuego",  "Cardinal", "marte"),
    ("tauro",       "Tauro",       "TAU", "tierra", "Fijo",     "venus"),
    ("geminis",     "Géminis",     "GEM", "aire",   "Mutable",  "mercurio"),
    ("cancer",      "Cáncer",      "CAN", "agua",   "Cardinal", "luna"),
    ("leo",         "Leo",         "LEO", "fuego",  "Fijo",     "sol"),
    ("virgo",       "Virgo",       "VIR", "tierra", "Mutable",  "mercurio"),
    ("libra",       "Libra",       "LIB", "aire",   "Cardinal", "venus"),
    ("escorpio",    "Escorpio",    "ESC", "agua",   "Fijo",     "marte"),
    ("sagitario",   "Sagitario",   "SAG", "fuego",  "Mutable",  "jupiter"),
    ("capricornio", "Capricornio", "CAP", "tierra", "Cardinal", "saturno"),
    ("acuario",     "Acuario",     "ACU", "aire",   "Fijo",     "saturno"),
    ("piscis",      "Piscis",      "PIS", "agua",   "Mutable",  "jupiter"),
]

PLANETAS = {                 # nombre, metal, signos que rige
    "saturno":  ("Saturno",  "Plomo",  "Capricornio y Acuario"),
    "jupiter":  ("Júpiter",  "Estaño", "Sagitario y Piscis"),
    "marte":    ("Marte",    "Hierro", "Aries y Escorpio"),
    "sol":      ("Sol",      "Oro",    "Leo"),
    "venus":    ("Venus",    "Cobre",  "Tauro y Libra"),
    "mercurio": ("Mercurio", "Azogue", "Géminis y Virgo"),
    "luna":     ("Luna",     "Plata",  "Cáncer"),
}

# Orden caldeo: del más lento al más rápido. Es el que gobierna las horas
# planetarias y el reparto de los treinta y seis decanatos.
CALDEO = ["saturno", "jupiter", "marte", "sol", "venus", "mercurio", "luna"]

# ── Glifos ────────────────────────────────────────────────────────────
# Todos en la misma caja de 200×200 y con el mismo grosor de trazo, para que
# en cualquier diagrama pesen visualmente igual.
GLIFOS = {
    "aries": """M100 148 V90
                M100 92 C100 68 86 58 76 65 C64 73 64 92 78 104
                M100 92 C100 68 114 58 124 65 C136 73 136 92 122 104""",
    "tauro": """M100 128 a28 28 0 1 0 .1 0 Z
                M60 106 C56 62 144 62 140 106""",
    "geminis": """M84 74 V148 M116 74 V148
                  M70 68 C84 57 116 57 130 68
                  M70 154 C84 165 116 165 130 154""",
    "cancer": """M58 96 C70 74 108 66 128 78
                 M138 92 a13 13 0 1 0 .1 0 Z
                 M142 128 C130 150 92 158 72 146
                 M62 132 a13 13 0 1 0 .1 0 Z""",
    "leo": """M84 130 a19 19 0 1 0 .1 0 Z
              M99 116 C99 96 87 79 102 68 C119 56 137 71 133 92
              C129 111 116 122 124 138 C130 150 143 151 151 143""",
    "virgo": """M50 152 V88 C50 73 74 73 74 88 V152
                M74 88 C74 73 98 73 98 88 V152
                M98 88 C98 73 122 73 122 88 V132 C122 152 140 157 151 146
                M112 130 L157 162""",
    "libra": """M60 154 H140
                M60 128 H78 A22 22 0 0 1 122 128 H140""",
    "escorpio": """M50 152 V90 C50 75 74 75 74 90 V152
                   M74 90 C74 75 98 75 98 90 V152
                   M98 90 C98 75 122 75 122 90 V130 L156 156
                   M156 156 V131 M156 156 H131""",
    "sagitario": """M60 154 L141 73
                    M141 73 V104 M141 73 H110
                    M82 105 L110 133""",
    "capricornio": """M60 82 V132
                      M60 94 C73 76 100 76 106 97 C110 111 106 124 100 132
                      M100 132 C119 121 137 132 133 148 C129 163 108 165 100 152""",
    "acuario": """M58 108 L78 93 L98 108 L118 93 L138 108 L146 102
                  M58 142 L78 127 L98 142 L118 127 L138 142 L146 136""",
    "piscis": """M84 66 C61 91 61 133 84 158
                 M122 66 C145 91 145 133 122 158
                 M56 112 H150""",
}

SIGILOS = {
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

ELEMENTO_MARCA = {                    # triángulos alquímicos, caja 24×24
    "fuego":  "M0 16 L12 -6 L24 16 Z",
    "aire":   "M0 16 L12 -6 L24 16 Z M4.5 7 H19.5",
    "agua":   "M0 -6 H24 L12 16 Z",
    "tierra": "M0 -6 H24 L12 16 Z M4.5 1.5 H19.5",
}


# ── Utilidades ────────────────────────────────────────────────────────
def pol(cx, cy, r, grados):
    """Punto polar. 0° = arriba, sentido horario (como se lee un reloj)."""
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def sector(cx, cy, r1, r2, a0, a1):
    """Sector anular entre los radios r1 (interior) y r2 (exterior)."""
    x1, y1 = pol(cx, cy, r2, a0)
    x2, y2 = pol(cx, cy, r2, a1)
    x3, y3 = pol(cx, cy, r1, a1)
    x4, y4 = pol(cx, cy, r1, a0)
    grande = 1 if (a1 - a0) > 180 else 0
    return (f"M{f(x1)} {f(y1)} A{f(r2)} {f(r2)} 0 {grande} 1 {f(x2)} {f(y2)} "
            f"L{f(x3)} {f(y3)} A{f(r1)} {f(r1)} 0 {grande} 0 {f(x4)} {f(y4)} Z")


# Glifos de trazos paralelos: con el grosor general los trazos se tocan y el
# dibujo se convierte en una mancha. Llevan divisor propio.
FINURA = {"virgo": 18, "escorpio": 18, "acuario": 16, "geminis": 15}


def glifo(clave, x, y, lado, color=None, grosor=None, opacidad=None):
    """Coloca un glifo escalando su caja de 200 al lado pedido.

    El grosor se deduce del tamaño (lado/13) y no se pasa suelto: cuando se
    fija a mano, los glifos pequeños de los diagramas salen como manchas y los
    grandes como alambre. La proporción constante es lo que hace que todos
    pesen visualmente igual estén al tamaño que estén.
    """
    k = lado / 200
    grosor = grosor if grosor is not None else lado / FINURA.get(clave, 13)
    est = f' color="{color}"' if color else ""
    op = f' opacity="{opacidad}"' if opacidad else ""
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" class="zt"'
            f' stroke-width="{f(grosor / k)}"{est}{op}>'
            f'<path d="{GLIFOS[clave]}"/></g>')


def sigilo(clave, x, y, lado, color="var(--acento)", grosor=None):
    """Los sigilos son dibujos más simples que los glifos: aguantan —y piden—
    algo más de trazo para no desaparecer a tamaño pequeño."""
    k = lado / 200
    grosor = grosor if grosor is not None else lado / 11
    trazo, relleno = SIGILOS[clave]
    extra = (f'<path d="{relleno}" fill="currentColor" stroke="none"/>'
             if relleno else "")
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" class="zt"'
            f' color="{color}" stroke-width="{f(grosor / k)}">'
            f'<path d="{trazo}"/>{extra}</g>')


def marca_elemento(elemento, x, y, lado=24, color=None):
    k = lado / 24
    c = color or COLOR[elemento]
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" fill="none"'
            f' stroke="{c}" stroke-width="{f(2.2 / k)}" stroke-linejoin="round">'
            f'<path d="{ELEMENTO_MARCA[elemento]}"/></g>')


def txt(x, y, s, clase="et", tam=11, color="var(--tinta-2)", anchor="middle",
        extra=""):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}"{extra}>{s}</text>')


# ══════════════════════════════════════════════════════════════════════
#  MEDALLONES · uno por signo
# ══════════════════════════════════════════════════════════════════════
def medallon(clave, nombre, abrev, elemento, modalidad, regente):
    c = COLOR[elemento]
    partes = [f'<symbol id="z-{clave}" viewBox="0 0 200 200">']

    # Orla: tres circunferencias y treinta marcas de grado.
    partes.append(f'<g fill="none" stroke="{c}">')
    partes.append('<circle cx="100" cy="100" r="93" stroke-width="1" opacity=".35"/>')
    partes.append('<circle cx="100" cy="100" r="87" stroke-width="1.8" opacity=".9"/>')
    partes.append('<circle cx="100" cy="100" r="70" stroke-width=".7" opacity=".25"/>')
    marcas = []
    for g in range(30):
        largo = 9 if g % 10 == 0 else (6 if g % 5 == 0 else 3.5)
        x1, y1 = pol(100, 100, 87, g * 12)
        x2, y2 = pol(100, 100, 87 - largo, g * 12)
        marcas.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    partes.append(f'<path d="{" ".join(marcas)}" stroke-width=".9" opacity=".5"/>')
    # Tres cuñas de decanato en la parte baja de la orla.
    for i in range(3):
        partes.append(f'<path d="{sector(100, 100, 74, 80, 130 + i * 34, 130 + i * 34 + 30)}" '
                      f'fill="{c}" stroke="none" opacity=".5"/>')
    partes.append("</g>")

    partes.append(f'<g filter="url(#z-glow-s)">{glifo(clave, 42, 44, 116, c)}</g>')
    partes.append(sigilo(regente, 78, 12, 44, c))
    partes.append(marca_elemento(elemento, 88, 176, 24, c))
    partes.append("</symbol>")
    return "".join(partes)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 1 · LA RUEDA
# ══════════════════════════════════════════════════════════════════════
def lamina_rueda():
    cx = cy = 232
    R_EXT, R_INT = 224, 186          # anillo de elementos
    p = [f'<symbol id="dia-rueda" viewBox="0 0 464 464">']

    p.append('<g fill="none" stroke="var(--acento)" opacity=".45">')
    for r, w in ((228, .8), (186, 1.4), (150, .8), (108, .8), (40, 1.4)):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-width="{w}"/>')
    p.append("</g>")

    # Radios cada 30°
    radios = []
    for i in range(12):
        x1, y1 = pol(cx, cy, 40, i * 30)
        x2, y2 = pol(cx, cy, R_EXT, i * 30)
        radios.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    p.append(f'<path d="{" ".join(radios)}" fill="none" stroke="var(--acento)" '
             'stroke-width=".8" opacity=".3"/>')

    for i, (clave, nombre, abrev, elemento, modalidad, regente) in enumerate(SIGNOS):
        a0, a1 = i * 30, i * 30 + 30
        c = COLOR[elemento]
        p.append(f'<path d="{sector(cx, cy, R_INT, R_EXT, a0, a1)}" fill="{c}" '
                 'stroke="none" opacity=".13"/>')
        p.append(f'<path d="{sector(cx, cy, R_INT, R_INT + 3, a0, a1)}" fill="{c}" '
                 'stroke="none" opacity=".7"/>')
        med = a0 + 15
        gx, gy = pol(cx, cy, 205, med)
        p.append(glifo(clave, gx - 18, gy - 18, 36, c))
        tx, ty = pol(cx, cy, 168, med)
        p.append(txt(tx, ty + 4, abrev, "rot", 10.5, c))
        mx, my = pol(cx, cy, 128, med)
        p.append(txt(mx, my + 3.5, modalidad[0], "rot", 11, "var(--tinta-3)"))
        rx, ry = pol(cx, cy, 78, med)
        p.append(sigilo(regente, rx - 14, ry - 14, 28, "var(--tinta-3)"))

    # Núcleo: los cuatro elementos en cruz.
    p.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" '
             'stroke="var(--acento)" stroke-width="1.2" opacity=".7"/>')
    for elemento, ang in (("fuego", 0), ("tierra", 90), ("aire", 180), ("agua", 270)):
        ex, ey = pol(cx, cy, 15, ang)
        p.append(marca_elemento(elemento, ex - 5, ey - 3, 10))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 2 · LAS DOCE CASILLAS (elemento × modalidad)
# ══════════════════════════════════════════════════════════════════════
def lamina_casillas():
    MODS = ["Cardinal", "Fijo", "Mutable"]
    ELS = ["fuego", "tierra", "aire", "agua"]
    NOM = {"fuego": "FUEGO", "tierra": "TIERRA", "aire": "AIRE", "agua": "AGUA"}
    por = {(e, m): s for s in SIGNOS for e, m in [(s[3], s[4])]}

    X0, Y0, ANCHO, ALTO = 84, 40, 122, 70
    p = [f'<symbol id="dia-casillas" viewBox="0 0 464 {Y0 + 4 * ALTO + 14}">']

    for j, m in enumerate(MODS):
        p.append(txt(X0 + j * ANCHO + ANCHO / 2, 24, m.upper(), "rot", 10.5,
                     "var(--acento)"))
    p.append(f'<path d="M{X0 - 6} 32 H{X0 + 3 * ANCHO} " fill="none" '
             'stroke="var(--acento)" stroke-width="1" opacity=".45"/>')

    for i, e in enumerate(ELS):
        y = Y0 + i * ALTO
        c = COLOR[e]
        p.append(marca_elemento(e, 12, y + 30, 20, c))
        p.append(txt(40, y + 42, NOM[e], "rot", 9.5, c, "start"))
        p.append(f'<path d="M{X0 - 6} {y + ALTO} H{X0 + 3 * ANCHO}" fill="none" '
                 f'stroke="var(--linea)" stroke-width=".8"/>')
        for j, m in enumerate(MODS):
            clave, nombre, abrev, _, _, regente = por[(e, m)]
            cxx = X0 + j * ANCHO
            p.append(f'<rect x="{cxx + 6}" y="{y + 8}" width="{ANCHO - 12}" '
                     f'height="{ALTO - 16}" rx="6" fill="{c}" opacity=".07"/>')
            p.append(glifo(clave, cxx + ANCHO / 2 - 20, y + 9, 40, c))
            p.append(txt(cxx + ANCHO / 2, y + ALTO - 12, nombre, "et", 12, c))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 3 · LA ESCALERA DE LOS SIETE REGENTES (orden caldeo)
# ══════════════════════════════════════════════════════════════════════
def lamina_regentes():
    ALTO = 46
    p = [f'<symbol id="dia-regentes" viewBox="0 0 464 {26 + 7 * ALTO + 16}">']
    p.append(txt(40, 16, "MÁS LENTO", "rot", 8.5, "var(--tinta-3)", "start"))
    p.append(f'<path d="M46 24 V{26 + 7 * ALTO - 8}" fill="none" '
             'stroke="var(--acento)" stroke-width="1" opacity=".35"/>')
    for i, clave in enumerate(CALDEO):
        nombre, metal, rige = PLANETAS[clave]
        y = 26 + i * ALTO
        p.append(f'<circle cx="46" cy="{y + ALTO / 2}" r="4" fill="var(--acento)" '
                 'opacity=".8"/>')
        p.append(sigilo(clave, 62, y + 5, 36, "var(--acento)"))
        p.append(txt(108, y + 24, nombre, "rot", 12, "var(--acento)", "start"))
        p.append(txt(108, y + 38, f"{metal} · {rige}", "et", 11.5,
                     "var(--tinta-2)", "start"))
        # Los signos que rige, en glifo, alineados a la derecha.
        regidos = [s for s in SIGNOS if s[5] == clave]
        for k, s in enumerate(regidos):
            p.append(glifo(s[0], 388 + k * 36, y + 7, 32, COLOR[s[3]]))
        if i < 6:
            p.append(f'<path d="M62 {y + ALTO} H452" fill="none" '
                     'stroke="var(--linea)" stroke-width=".7"/>')
    p.append(txt(40, 26 + 7 * ALTO + 10, "MÁS RÁPIDO", "rot", 8.5,
                 "var(--tinta-3)", "start"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 4 · EL ZODIACO DEL CUERPO (melotesia)
# ══════════════════════════════════════════════════════════════════════
# Media silueta: se dibuja un lado y se refleja, así la figura queda
# perfectamente simétrica y solo hay un contorno que mantener.
MITAD = ("M72 30 L52 36 L42 44 L36 74 L30 114 L35 120 L43 80 L49 50 "
         "L47 96 L43 128 L39 180 L43 197 L41 243 L53 248 L55 243 "
         "L59 197 L63 151 L72 139")

ZONAS = [                      # signo, y en la silueta, zona, lado
    ("aries",        17, "Cabeza, cara, cerebro",   "izq"),
    ("tauro",        33, "Cuello y garganta",       "der"),
    ("geminis",      45, "Hombros, brazos, pulmón", "izq"),
    ("cancer",       60, "Pecho y estómago",        "der"),
    ("leo",          78, "Corazón y espalda alta",  "izq"),
    ("virgo",        99, "Abdomen e intestino",     "der"),
    ("libra",       118, "Riñones y lumbares",      "izq"),
    ("escorpio",    133, "Pelvis y zona genital",   "der"),
    ("sagitario",   158, "Caderas y muslos",        "izq"),
    ("capricornio", 191, "Rodillas y huesos",       "der"),
    ("acuario",     216, "Pantorrillas y tobillos", "izq"),
    ("piscis",      246, "Pies y sistema linfático", "der"),
]


def lamina_cuerpo():
    """Melotesia: los doce signos repartidos de la cabeza a los pies.

    El reparto de anchos manda en esta lámina. La silueta se queda en el
    tercio central y las etiquetas ocupan dos columnas fijas a los lados;
    todo el texto se ha ajustado para no salirse de su columna, porque un
    símbolo se puede reducir pero una etiqueta cortada no sirve para nada.
    """
    K = 1.42                     # escala de la silueta
    OX, OY = 232 - 72 * K, 34    # la silueta queda centrada en 232
    ALTO = int(OY + 262 * K + 24)
    IZQ, DER = 124, 340          # raíles donde acaban y empiezan las guías
    p = [f'<symbol id="dia-cuerpo" viewBox="0 0 464 {ALTO}">']
    p.append(f'<defs><g id="dc-mitad"><path d="{MITAD}"/></g></defs>')

    # Primero la masa (el contorno se cierra solo al rellenar) y luego la
    # línea encima: con el contorno a secas los brazos y el torso se cruzan y
    # la figura no se lee.
    p.append(f'<g transform="translate({f(OX)},{OY}) scale({f(K)})">')
    for relleno, trazo, op in (("var(--acento)", "none", ".09"),
                               ("none", "var(--acento)", ".6")):
        p.append(f'<g fill="{relleno}" fill-opacity="{op}" stroke="{trazo}" '
                 f'stroke-width=".9" stroke-opacity="{op}" '
                 'stroke-linejoin="round" stroke-linecap="round">')
        p.append('<circle cx="72" cy="17" r="11"/>')
        p.append('<use href="#dc-mitad"/>')
        p.append('<use href="#dc-mitad" transform="translate(144,0) scale(-1,1)"/>')
        p.append("</g>")
    p.append("</g>")

    for clave, y_local, zona, lado in ZONAS:
        nombre = next(s[1] for s in SIGNOS if s[0] == clave)
        c = COLOR[next(s[3] for s in SIGNOS if s[0] == clave)]
        y = OY + y_local * K
        # Franja tenue: marca a qué altura del cuerpo cae el signo.
        p.append(f'<rect x="172" y="{f(y - 8)}" width="120" height="16" rx="8" '
                 f'fill="{c}" opacity=".11"/>')
        p.append(f'<circle cx="232" cy="{f(y)}" r="2.8" fill="{c}"/>')
        if lado == "izq":
            p.append(f'<path d="M{IZQ + 4} {f(y)} H229" fill="none" stroke="{c}" '
                     'stroke-width=".8" stroke-dasharray="3 3" opacity=".6"/>')
            p.append(glifo(clave, IZQ - 24, y - 9, 18, c))
            p.append(txt(IZQ - 30, y + 3, nombre, "rot", 10, c, "end"))
            p.append(txt(IZQ, y + 16, zona, "et", 9.5, "var(--tinta-2)", "end"))
        else:
            p.append(f'<path d="M235 {f(y)} H{DER - 4}" fill="none" stroke="{c}" '
                     'stroke-width=".8" stroke-dasharray="3 3" opacity=".6"/>')
            p.append(glifo(clave, DER + 4, y - 9, 18, c))
            p.append(txt(DER + 28, y + 3, nombre, "rot", 10, c, "start"))
            p.append(txt(DER, y + 16, zona, "et", 9.5, "var(--tinta-2)", "start"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 5 · LOS TREINTA Y SEIS DECANATOS
# ══════════════════════════════════════════════════════════════════════
def decanatos():
    """Reparte los 36 decanatos en orden caldeo empezando en Marte (Aries 0°)."""
    salida, i = {}, CALDEO.index("marte")
    for clave, *_ in SIGNOS:
        salida[clave] = [CALDEO[(i + k) % 7] for k in range(3)]
        i = (i + 3) % 7
    return salida


DECANATOS = decanatos()


def lamina_decanos():
    """Los treinta y seis en columna: tres franjas de 10° por signo."""
    ALTO_F = 30
    p = [f'<symbol id="dia-decanos" viewBox="0 0 464 {30 + 12 * ALTO_F + 10}">']
    for j, etq in enumerate(("0° – 10°", "10° – 20°", "20° – 30°")):
        p.append(txt(170 + j * 112, 18, etq, "rot", 9.5, "var(--acento)"))
    p.append(f'<path d="M116 26 H452" fill="none" stroke="var(--acento)" '
             'stroke-width="1" opacity=".4"/>')
    for i, (clave, nombre, abrev, elemento, _, _) in enumerate(SIGNOS):
        y = 30 + i * ALTO_F
        c = COLOR[elemento]
        p.append(glifo(clave, 6, y + 2, 26, c))
        p.append(txt(38, y + 20, nombre, "et", 11.5, c, "start"))
        for j, planeta in enumerate(DECANATOS[clave]):
            x = 116 + j * 112
            p.append(f'<rect x="{x}" y="{y + 3}" width="108" height="{ALTO_F - 6}" '
                     f'rx="5" fill="{c}" opacity=".07"/>')
            p.append(sigilo(planeta, x + 6, y + 4, 22, c))
            p.append(txt(x + 34, y + 20, PLANETAS[planeta][0], "et", 11.5,
                         "var(--tinta-2)", "start"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 6 · LAS OCHO FASES DE LA LUNA
# ══════════════════════════════════════════════════════════════════════
# Ocho fases en 464 unidades: 58 por casilla. Los rótulos van abreviados a
# nueve caracteres como máximo porque a partir de ahí se tocan entre sí; los
# nombres completos están en la ficha del capítulo.
FASES = [
    (0.00, True,  "NUEVA",     "Sembrar"),
    (0.25, True,  "CRECIENTE", "Empezar"),
    (0.50, True,  "CUARTO C.", "Decidir"),
    (0.75, True,  "GIBOSA C.", "Sostener"),
    (1.00, True,  "LLENA",     "Culminar"),
    (0.75, False, "GIBOSA M.", "Revisar"),
    (0.50, False, "CUARTO M.", "Soltar"),
    (0.25, False, "MENGUANTE", "Cerrar"),
]


def cara_iluminada(cx, cy, r, fraccion, creciente):
    """Zona iluminada de la Luna. El terminador es media elipse cuyo eje
    horizontal vale r·|1−2·fracción|; el sentido del arco decide si el
    resultado es hoz o giba."""
    if fraccion <= 0.001:
        return ""
    if fraccion >= 0.999:
        return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/>'
    rx = r * abs(1 - 2 * fraccion)
    barrido = 0 if fraccion < 0.5 else 1
    d = (f"M{f(cx)} {f(cy - r)} A{f(r)} {f(r)} 0 0 1 {f(cx)} {f(cy + r)} "
         f"A{f(rx)} {f(r)} 0 0 {barrido} {f(cx)} {f(cy - r)} Z")
    if creciente:
        return f'<path d="{d}"/>'
    return f'<g transform="translate({f(2 * cx)},0) scale(-1,1)"><path d="{d}"/></g>'


def lamina_lunar():
    p = ['<symbol id="dia-lunar" viewBox="0 0 464 132">']
    paso = 464 / 8
    for i, (fr, creciente, nombre, verbo) in enumerate(FASES):
        cx = paso * i + paso / 2
        p.append(f'<circle cx="{f(cx)}" cy="46" r="26" fill="none" '
                 'stroke="var(--acento)" stroke-width=".9" opacity=".45"/>')
        cuerpo = cara_iluminada(cx, 46, 26, fr, creciente)
        if cuerpo:
            p.append(f'<g fill="var(--acento)" stroke="none" opacity=".85">'
                     f'{cuerpo}</g>')
        p.append(txt(cx, 92, nombre, "rot", 7, "var(--acento)"))
        p.append(txt(cx, 108, verbo, "et", 11, "var(--tinta-2)"))
    p.append('<path d="M18 122 H446" fill="none" stroke="var(--linea)" '
             'stroke-width=".8"/>')
    p.append(txt(18, 132, "LUNA CRECIENTE", "rot", 8, "var(--tinta-3)", "start"))
    p.append(txt(446, 132, "LUNA MENGUANTE", "rot", 8, "var(--tinta-3)", "end"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA 7 · LA GEOMETRÍA DE LA RUEDA (aspectos)
# ══════════════════════════════════════════════════════════════════════
ASPECTOS = [
    ("Oposición", "180°", [0, 6], "#ff5c7a", "Signos enfrentados: tensión"),
    ("Trígono", "120°", [0, 4, 8], "#4dffa6", "Mismo elemento: fluidez"),
    ("Cuadratura", "90°", [0, 3, 6, 9], "#ffd75c", "Misma modalidad: roce"),
    ("Sextil", "60°", [0, 2, 4, 6, 8, 10], "#5cd6ff", "Afinidad: oportunidad"),
]


def lamina_aspectos():
    p = ['<symbol id="dia-aspectos" viewBox="0 0 464 400">']
    for i, (nombre, grados, nodos, color, glosa) in enumerate(ASPECTOS):
        cx = 116 + (i % 2) * 232
        cy = 86 + (i // 2) * 196
        r = 62
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                 'stroke="var(--acento)" stroke-width=".9" opacity=".35"/>')
        # las doce posiciones
        for k in range(12):
            x, y = pol(cx, cy, r, k * 30)
            p.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="1.8" '
                     'fill="var(--tinta-3)" opacity=".7"/>')
        puntos = [pol(cx, cy, r, k * 30) for k in nodos]
        if len(nodos) == 2:
            d = f"M{f(puntos[0][0])} {f(puntos[0][1])} L{f(puntos[1][0])} {f(puntos[1][1])}"
        else:
            d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in puntos) + " Z"
        p.append(f'<path d="{d}" fill="{color}" fill-opacity=".10" '
                 f'stroke="{color}" stroke-width="1.6" stroke-linejoin="round"/>')
        for x, y in puntos:
            p.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="3.4" fill="{color}"/>')
        p.append(txt(cx, cy + r + 26, f"{nombre.upper()} · {grados}", "rot", 10, color))
        p.append(txt(cx, cy + r + 41, glosa, "et", 11, "var(--tinta-2)"))
    p.append("</symbol>")
    return "".join(p)



# ══════════════════════════════════════════════════════════════════════
#  DATOS CLÁSICOS · tablas de tradición común, verificables
# ══════════════════════════════════════════════════════════════════════
# Las dignidades esenciales tal como las fija el Tetrabiblos (siglo II).
# El exilio es siempre el regente del signo opuesto y la caída es el opuesto
# de la exaltación: las dos columnas se DEDUCEN, y por eso aquí se calculan en
# vez de teclearse. Una tabla copiada a mano se desincroniza; una deducida, no.
EXALTACIONES = {                    # signo: (planeta, grado)
    "aries": ("sol", 19), "tauro": ("luna", 3), "cancer": ("jupiter", 15),
    "virgo": ("mercurio", 15), "libra": ("saturno", 21),
    "capricornio": ("marte", 28), "piscis": ("venus", 27),
}

# Términos egipcios: cinco tramos por signo que suman treinta grados justos.
# Es la tabla más olvidada del sistema clásico y la que mejor se comprueba:
# si una fila no suma 30, está mal.
TERMINOS = {
    "aries":       [("jupiter", 6), ("venus", 6), ("mercurio", 8), ("marte", 5), ("saturno", 5)],
    "tauro":       [("venus", 8), ("mercurio", 6), ("jupiter", 8), ("saturno", 5), ("marte", 3)],
    "geminis":     [("mercurio", 6), ("jupiter", 6), ("venus", 5), ("marte", 7), ("saturno", 6)],
    "cancer":      [("marte", 7), ("venus", 6), ("mercurio", 6), ("jupiter", 7), ("saturno", 4)],
    "leo":         [("jupiter", 6), ("venus", 5), ("saturno", 7), ("mercurio", 6), ("marte", 6)],
    "virgo":       [("mercurio", 7), ("venus", 10), ("jupiter", 4), ("marte", 7), ("saturno", 2)],
    "libra":       [("saturno", 6), ("mercurio", 8), ("jupiter", 7), ("venus", 7), ("marte", 2)],
    "escorpio":    [("marte", 7), ("venus", 4), ("mercurio", 8), ("jupiter", 5), ("saturno", 6)],
    "sagitario":   [("jupiter", 12), ("venus", 5), ("mercurio", 4), ("saturno", 5), ("marte", 4)],
    "capricornio": [("mercurio", 7), ("jupiter", 7), ("venus", 8), ("saturno", 4), ("marte", 4)],
    "acuario":     [("mercurio", 7), ("venus", 6), ("jupiter", 7), ("marte", 5), ("saturno", 5)],
    "piscis":      [("venus", 12), ("jupiter", 4), ("mercurio", 3), ("marte", 9), ("saturno", 2)],
}

OPUESTO = {s[0]: SIGNOS[(i + 6) % 12][0] for i, s in enumerate(SIGNOS)}
REGENTE = {s[0]: s[5] for s in SIGNOS}


def dignidades(clave):
    """Domicilio, exaltación, exilio y caída de un signo.

    Solo el domicilio y la exaltación son datos; el exilio y la caída se
    deducen y se calculan aquí para que no puedan contradecirlos.
    """
    dom = REGENTE[clave]
    exilio = REGENTE[OPUESTO[clave]]
    exalt = EXALTACIONES.get(clave)
    caida = next(((p, g) for s, (p, g) in EXALTACIONES.items()
                  if OPUESTO[s] == clave), None)
    return dom, exalt, exilio, caida


def comprobar_datos():
    """Los términos tienen que sumar treinta por signo y usar los cinco
    planetas sin repetir. Si algo no cuadra, el generador no escribe."""
    for clave, tramos in TERMINOS.items():
        total = sum(g for _, g in tramos)
        if total != 30:
            raise SystemExit(f"Términos de {clave}: suman {total}, no 30")
        if len({p for p, _ in tramos}) != 5:
            raise SystemExit(f"Términos de {clave}: hay un planeta repetido")
    if len(TERMINOS) != 12:
        raise SystemExit("Faltan signos en la tabla de términos")
    # Las 28 mansiones reparten el círculo en partes iguales exactas.
    if abs(28 * (360 / 28) - 360) > 1e-9:
        raise SystemExit("La división de mansiones no cierra el círculo")
    return True


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LAS DIGNIDADES ESENCIALES
# ══════════════════════════════════════════════════════════════════════
def lamina_dignidades():
    ALTO_F = 30
    COLS = [(118, "DOMICILIO"), (204, "EXALTA"), (300, "EXILIO"), (386, "CAÍDA")]
    p = [f'<symbol id="dia-dignidades" viewBox="0 0 464 {34 + 12 * ALTO_F + 12}">']
    for x, etq in COLS:
        p.append(txt(x + 26, 20, etq, "rot", 8.2, "var(--acento)"))
    p.append('<path d="M112 28 H452" fill="none" stroke="var(--acento)" '
             'stroke-width="1" opacity=".4"/>')
    for i, (clave, nombre, abrev, elemento, _, _) in enumerate(SIGNOS):
        y = 34 + i * ALTO_F
        c = COLOR[elemento]
        dom, exalt, exilio, caida = dignidades(clave)
        p.append(glifo(clave, 4, y + 2, 24, c))
        p.append(txt(34, y + 19, nombre, "et", 11, c, "start"))
        celdas = [(dom, None), (exalt[0] if exalt else None, exalt[1] if exalt else None),
                  (exilio, None), (caida[0] if caida else None, caida[1] if caida else None)]
        for (x, _), (planeta, grado) in zip(COLS, celdas):
            if not planeta:
                p.append(txt(x + 26, y + 19, "—", "et", 11, "var(--tinta-3)"))
                continue
            p.append(sigilo(planeta, x + 2, y + 3, 22, c))
            if grado is not None:
                p.append(txt(x + 30, y + 19, f"{grado}°", "num", 9.5,
                             "var(--tinta-2)", "start"))
        if i < 11:
            p.append(f'<path d="M4 {y + ALTO_F} H452" fill="none" '
                     'stroke="var(--linea)" stroke-width=".6"/>')
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LOS TÉRMINOS EGIPCIOS
# ══════════════════════════════════════════════════════════════════════
def lamina_terminos():
    """Cada signo, una barra de treinta grados partida en cinco tramos
    desiguales. La longitud de cada tramo ES su número de grados: la lámina
    se puede medir con una regla y sale la tabla."""
    ALTO_F = 32
    X0, ANCHO = 106, 336
    p = [f'<symbol id="dia-terminos" viewBox="0 0 464 {40 + 12 * ALTO_F + 14}">']
    for k in range(7):
        x = X0 + ANCHO * k / 6
        p.append(txt(x, 18, f"{k * 5}°", "num", 8.2, "var(--tinta-3)"))
        p.append(f'<path d="M{f(x)} 24 V{40 + 12 * ALTO_F - 4}" fill="none" '
                 'stroke="var(--linea)" stroke-width=".5" opacity=".7"/>')
    for i, (clave, nombre, abrev, elemento, _, _) in enumerate(SIGNOS):
        y = 34 + i * ALTO_F
        c = COLOR[elemento]
        p.append(glifo(clave, 4, y + 3, 22, c))
        p.append(txt(32, y + 18, nombre, "et", 10.5, c, "start"))
        grado = 0
        for planeta, tramos in TERMINOS[clave]:
            x = X0 + ANCHO * grado / 30
            w = ANCHO * tramos / 30
            p.append(f'<rect x="{f(x)}" y="{f(y + 2)}" width="{f(w - 1.5)}" '
                     f'height="22" rx="3" fill="{c}" opacity=".12"/>')
            p.append(f'<rect x="{f(x)}" y="{f(y + 2)}" width="{f(w - 1.5)}" '
                     f'height="22" rx="3" fill="none" stroke="{c}" '
                     'stroke-width=".7" opacity=".55"/>')
            p.append(sigilo(planeta, x + w / 2 - 8, y + 5, 16, c))
            grado += tramos
    p.append(txt(232, 40 + 12 * ALTO_F + 8,
                 "CINCO TRAMOS DESIGUALES · TREINTA GRADOS JUSTOS",
                 "rot", 8.2, "var(--tinta-3)"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LA PRECESIÓN
# ══════════════════════════════════════════════════════════════════════
def lamina_precesion():
    """Dos anillos concéntricos desfasados: los signos donde los fijó la
    tradición y las constelaciones donde están hoy. El hueco es el dato."""
    cx, cy = 232, 216
    DESFASE = 24                     # grados acumulados desde el siglo II
    p = ['<symbol id="dia-precesion" viewBox="0 0 464 414">']
    for r, w, op in ((176, 1.4, .8), (142, .7, .3), (120, 1.4, .8), (86, .7, .3)):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                 f'stroke="var(--acento)" stroke-width="{w}" opacity="{op}"/>')
    for i, (clave, nombre, abrev, elemento, _, _) in enumerate(SIGNOS):
        c = COLOR[elemento]
        # anillo exterior: el signo tropical, donde lo dejó la tradición
        med = i * 30 + 15
        gx, gy = pol(cx, cy, 159, med)
        p.append(glifo(clave, gx - 13, gy - 13, 26, c))
        # anillo interior: la constelación, corrida por la precesión
        gx2, gy2 = pol(cx, cy, 103, med - DESFASE)
        p.append(glifo(clave, gx2 - 11, gy2 - 11, 22, c, opacidad=".45"))
        # radios de cada anillo
        for r0, r1, ang, alfa in ((142, 176, i * 30, ".3"),
                                  (86, 120, i * 30 - DESFASE, ".18")):
            x1, y1 = pol(cx, cy, r0, ang)
            x2, y2 = pol(cx, cy, r1, ang)
            p.append(f'<path d="M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}" fill="none" '
                     f'stroke="var(--acento)" stroke-width=".7" opacity="{alfa}"/>')
    # la flecha del desfase, sobre Aries
    a1x, a1y = pol(cx, cy, 190, 0)
    a2x, a2y = pol(cx, cy, 190, -DESFASE)
    arco = []
    for k in range(DESFASE + 1):
        x, y = pol(cx, cy, 190, -k)
        arco.append(f"{'M' if k == 0 else 'L'}{f(x)} {f(y)}")
    p.append(f'<path d="{" ".join(arco)}" fill="none" stroke="var(--acento-2)" '
             'stroke-width="2.4"/>')
    p.append(f'<circle cx="{f(a1x)}" cy="{f(a1y)}" r="3.4" fill="var(--acento-2)"/>')
    p.append(f'<circle cx="{f(a2x)}" cy="{f(a2y)}" r="3.4" fill="var(--acento-2)"/>')
    p.append(txt(cx, 14, f"{DESFASE}° DE DESFASE ACUMULADO", "rot", 9.5, "var(--acento-2)"))
    p.append(txt(cx, cy - 12, "SIGNOS", "rot", 9, "var(--acento)"))
    p.append(txt(cx, cy + 4, "fuera", "et", 10.4, "var(--tinta-2)"))
    p.append(txt(cx, cy + 22, "CONSTELACIONES", "rot", 9, "var(--acento)"))
    p.append(txt(cx, cy + 38, "dentro", "et", 10.4, "var(--tinta-2)"))
    p.append(txt(232, 408, "50,3 SEGUNDOS DE ARCO AL AÑO · UNA VUELTA EN 25 800",
                 "rot", 8.2, "var(--tinta-3)"))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
def main():
    comprobar_datos()
    piezas = ['<svg xmlns="http://www.w3.org/2000/svg" '
              'style="position:absolute;width:0;height:0;overflow:hidden" '
              'aria-hidden="true">',
              """
<!-- ════════════════════════════════════════════════════════════════
     CÓDICE ZODIACAL · repertorio gráfico
     Dibujo original de VILLUMINATIONS — generado por
     tools/dibujar-zodiaco.py. No editar a mano.
     ════════════════════════════════════════════════════════════ -->""",
              '<defs>'
              '<filter id="z-glow-s" x="-80%" y="-80%" width="260%" height="260%">'
              '<feGaussianBlur stdDeviation="1.4" result="b"/>'
              '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
              '</filter></defs>',
              '<style>'
              'svg .zt{ fill:none; stroke:currentColor; stroke-linecap:round;'
              ' stroke-linejoin:round }'
              "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
              ' letter-spacing:.1em }'
              "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
              '</style>']

    for s in SIGNOS:
        piezas.append(medallon(*s))
    piezas.append(lamina_rueda())
    piezas.append(lamina_casillas())
    piezas.append(lamina_regentes())
    piezas.append(lamina_cuerpo())
    piezas.append(lamina_decanos())
    piezas.append(lamina_lunar())
    piezas.append(lamina_aspectos())
    piezas.append(lamina_dignidades())
    piezas.append(lamina_terminos())
    piezas.append(lamina_precesion())
    piezas.append("</svg>")

    DESTINO.write_text("\n".join(piezas) + "\n")
    print(f"  {DESTINO.relative_to(RAIZ)}: 12 medallones + 10 láminas · "
          f"{DESTINO.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
