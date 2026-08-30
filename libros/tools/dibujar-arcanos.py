#!/usr/bin/env python3
"""
CÓDICE DE LOS ARCANOS — generador del repertorio gráfico
=======================================================
Escribe partials/arcanos.svg. Dibujo original de VILLUMINATIONS sobre el
patrón de Marsella (grabados del XVII y XVIII, de dominio público) y las
correspondencias que Éliphas Lévi (1856) y Papus (1889) pusieron por escrito.

Nada aquí reproduce una baraja: los arcanos se representan con emblemas
geométricos propios. Lo que se recupera de la tradición son las TABLAS, que
son datos y no dibujo.

Y las tablas se DEDUCEN, no se copian:
  · cada arcano mayor toma su letra por posición (I ↔ Álef … 0 ↔ Tav) y de la
    letra hereda su elemento, planeta o signo por el reparto 3-7-12;
  · cada una de las 36 cartas del 2 al 10 toma su decanato por regla — el palo
    lo da el elemento del signo y el trío de números lo da la modalidad.
El generador comprueba las dos deducciones antes de escribir el fichero.

    python3 tools/dibujar-arcanos.py
"""

import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "partials" / "arcanos.svg"

CARMIN = "#ff5c8a"      # el acento de este libro
CIAN = "#5cd6ff"
CLARO = "#c9cfe0"
APAGADO = "#8a93ab"

COLOR_ELEM = {"fuego": "#ff5c7a", "tierra": "#4dffa6",
              "aire": "#ffd75c", "agua": "#5cd6ff"}

# ── Las veintidós letras, con su reparto y su valor ───────────────────
# Es la misma tabla del Códice de las Invocaciones. Se repite aquí porque este
# generador tiene que poder deducir de ella, no porque se quiera duplicar el
# dato: si alguna vez cambia, cambia en los dos sitios y el comprobador avisa.
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

# ── Los veintidós arcanos mayores, en el orden de Marsella ────────────
# La Justicia va en el VIII y la Fuerza en el XI, que es el orden histórico
# anterior al intercambio que hizo la tradición inglesa a finales del XIX.
MAYORES = [
    ("I", "El Mago"), ("II", "La Sacerdotisa"), ("III", "La Emperatriz"),
    ("IV", "El Emperador"), ("V", "El Sumo Sacerdote"), ("VI", "Los Enamorados"),
    ("VII", "El Carro"), ("VIII", "La Justicia"), ("IX", "El Ermitaño"),
    ("X", "La Rueda"), ("XI", "La Fuerza"), ("XII", "El Colgado"),
    ("XIII", "El Arcano sin Nombre"), ("XIV", "La Templanza"), ("XV", "El Diablo"),
    ("XVI", "La Torre"), ("XVII", "La Estrella"), ("XVIII", "La Luna"),
    ("XIX", "El Sol"), ("XX", "El Juicio"), ("XXI", "El Mundo"),
    ("0", "El Loco"),
]

PALOS = [                     # clave, nombre, elemento, facultad
    ("bastos", "Bastos", "fuego", "La voluntad · lo que se emprende"),
    ("copas", "Copas", "agua", "El sentimiento · lo que se vincula"),
    ("espadas", "Espadas", "aire", "El pensamiento · lo que se decide"),
    ("oros", "Oros", "tierra", "El cuerpo · lo que se sostiene"),
]

SIGNOS = [                    # nombre, elemento, modalidad
    ("Aries", "fuego", "cardinal"), ("Tauro", "tierra", "fijo"),
    ("Géminis", "aire", "mutable"), ("Cáncer", "agua", "cardinal"),
    ("Leo", "fuego", "fijo"), ("Virgo", "tierra", "mutable"),
    ("Libra", "aire", "cardinal"), ("Escorpio", "agua", "fijo"),
    ("Sagitario", "fuego", "mutable"), ("Capricornio", "tierra", "cardinal"),
    ("Acuario", "aire", "fijo"), ("Piscis", "agua", "mutable"),
]

PALO_DE_ELEMENTO = {e: c for c, _, e, _ in PALOS}
TRIO_DE_MODALIDAD = {"cardinal": (2, 3, 4), "fijo": (5, 6, 7), "mutable": (8, 9, 10)}

CALDEO = ["Saturno", "Júpiter", "Marte", "Sol", "Venus", "Mercurio", "Luna"]

GLIFO_SIGNO = {          # el mismo trazo que en el Códice Zodiacal, en caja 200
    "Aries": "M100 148 V90 M100 92 C100 68 86 58 76 65 C64 73 64 92 78 104 "
             "M100 92 C100 68 114 58 124 65 C136 73 136 92 122 104",
    "Tauro": "M100 128 a28 28 0 1 0 .1 0 Z M60 106 C56 62 144 62 140 106",
    "Géminis": "M84 74 V148 M116 74 V148 M70 68 C84 57 116 57 130 68 "
               "M70 154 C84 165 116 165 130 154",
    "Cáncer": "M58 96 C70 74 108 66 128 78 M138 92 a13 13 0 1 0 .1 0 Z "
              "M142 128 C130 150 92 158 72 146 M62 132 a13 13 0 1 0 .1 0 Z",
    "Leo": "M84 130 a19 19 0 1 0 .1 0 Z M99 116 C99 96 87 79 102 68 "
           "C119 56 137 71 133 92 C129 111 116 122 124 138 C130 150 143 151 151 143",
    "Virgo": "M50 152 V88 C50 73 74 73 74 88 V152 M74 88 C74 73 98 73 98 88 V152 "
             "M98 88 C98 73 122 73 122 88 V132 C122 152 140 157 151 146 M112 130 L157 162",
    "Libra": "M60 154 H140 M60 128 H78 A22 22 0 0 1 122 128 H140",
    "Escorpio": "M50 152 V90 C50 75 74 75 74 90 V152 M74 90 C74 75 98 75 98 90 V152 "
                "M98 90 C98 75 122 75 122 90 V130 L156 156 M156 156 V131 M156 156 H131",
    "Sagitario": "M60 154 L141 73 M141 73 V104 M141 73 H110 M82 105 L110 133",
    "Capricornio": "M60 82 V132 M60 94 C73 76 100 76 106 97 C110 111 106 124 100 132 "
                   "M100 132 C119 121 137 132 133 148 C129 163 108 165 100 152",
    "Acuario": "M58 108 L78 93 L98 108 L118 93 L138 108 L146 102 "
               "M58 142 L78 127 L98 142 L118 127 L138 142 L146 136",
    "Piscis": "M84 66 C61 91 61 133 84 158 M122 66 C145 91 145 133 122 158 M56 112 H150",
}

MARCA_PALO = {           # emblema propio de cada palo, caja 60×60
    "bastos": "M12 50 L48 12 M44 8 l8 -2 -2 8 Z M12 50 l-4 6 8 2 Z",
    "copas": "M14 16 H46 M16 16 C16 38 24 46 30 48 C36 46 44 38 44 16 "
             "M30 48 V56 M20 58 H40",
    "espadas": "M30 8 V44 M18 44 H42 M30 44 V54 M24 54 H36",
    "oros": "M30 8 a22 22 0 1 0 .1 0 Z M30 8 V52 M8 30 H52 "
            "M14 14 L46 46 M46 14 L14 46",
}

FIGURAS = [("Sota", "tierra"), ("Caballo", "aire"),
           ("Reina", "agua"), ("Rey", "fuego")]

INICIAL_ELEM = {"fuego": "F", "tierra": "T", "aire": "A", "agua": "AG"}


# ── Utilidades ────────────────────────────────────────────────────────
def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def pol(cx, cy, r, grados):
    a = math.radians(grados - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def txt(x, y, s, clase="et", tam=11, color=CLARO, anchor="middle"):
    return (f'<text x="{f(x)}" y="{f(y)}" class="{clase}" font-size="{f(tam)}" '
            f'fill="{color}" text-anchor="{anchor}">{s}</text>')


def glifo_signo(nombre, x, y, lado, color):
    k = lado / 200
    fino = {"Virgo": 18, "Escorpio": 18, "Acuario": 16, "Géminis": 15}
    grosor = lado / fino.get(nombre, 13)
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" fill="none" '
            f'stroke="{color}" stroke-width="{f(grosor / k)}" '
            'stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="{GLIFO_SIGNO[nombre]}"/></g>')


def marca_palo(clave, x, y, lado, color):
    k = lado / 60
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(k)})" fill="none" '
            f'stroke="{color}" stroke-width="{f(3.2 / k)}" '
            'stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="{MARCA_PALO[clave]}"/></g>')


# ══════════════════════════════════════════════════════════════════════
#  LAS DOS DEDUCCIONES
# ══════════════════════════════════════════════════════════════════════
def arcanos_con_letra():
    """Cada mayor recibe su letra por posición y de ella hereda su atribución.

    I va con Álef, II con Bet, y así hasta XXI con Shin; El Loco cierra con
    Tav. Es el reparto de Lévi y de Papus, y se elige porque encaja con el
    reparto 3-7-12 de las letras que ya usa el Códice de las Invocaciones.
    """
    return [(num, nombre, LETRAS[i][0], LETRAS[i][1], LETRAS[i][2], LETRAS[i][3])
            for i, (num, nombre) in enumerate(MAYORES)]


def menores_con_decanato():
    """Las 36 cartas del 2 al 10 reciben su decanato por regla.

    El palo lo da el elemento del signo; el trío de números, su modalidad:
    cardinal 2-3-4, fijo 5-6-7, mutable 8-9-10. Los tres decanatos de cada
    signo van al primer, segundo y tercer número del trío, y su regente sale
    del orden caldeo empezando en Marte, igual que en el Códice Zodiacal.
    """
    salida = []
    i = CALDEO.index("Marte")
    for nombre, elemento, modalidad in SIGNOS:
        palo = PALO_DE_ELEMENTO[elemento]
        trio = TRIO_DE_MODALIDAD[modalidad]
        for k in range(3):
            salida.append({
                "carta": trio[k], "palo": palo, "signo": nombre,
                "elemento": elemento, "decanato": k + 1,
                "regente": CALDEO[(i + k) % 7],
                "grados": f"{k * 10}° a {(k + 1) * 10}°",
            })
        i = (i + 3) % 7
    return salida


ARCANOS = arcanos_con_letra()
MENORES = menores_con_decanato()


def comprobar():
    """Si una deducción no cierra, el fichero no se escribe."""
    if len(LETRAS) != 22 or len(MAYORES) != 22:
        raise SystemExit("Mayores y letras tienen que ser 22 y 22")
    if sum(v for _, v, _, _ in LETRAS) != 1495:
        raise SystemExit("Los valores de las letras no suman 1495")
    # Reparto 3-7-12
    cuenta = {"madre": 0, "doble": 0, "simple": 0}
    for _, _, c, _ in LETRAS:
        cuenta[c] += 1
    if cuenta != {"madre": 3, "doble": 7, "simple": 12}:
        raise SystemExit(f"El reparto 3-7-12 no cuadra: {cuenta}")
    # Las 36 menores: cada par (palo, número) exactamente una vez
    if len(MENORES) != 36:
        raise SystemExit(f"Salen {len(MENORES)} decanatos y tienen que ser 36")
    pares = {(m["palo"], m["carta"]) for m in MENORES}
    if len(pares) != 36:
        raise SystemExit("Hay una carta menor repetida en el reparto de decanatos")
    for clave, _, _, _ in PALOS:
        nums = sorted(m["carta"] for m in MENORES if m["palo"] == clave)
        if nums != list(range(2, 11)):
            raise SystemExit(f"El palo de {clave} no cubre del 2 al 10: {nums}")
    # La baraja entera
    total = 22 + 4 * (1 + 9 + 4)
    if total != 78:
        raise SystemExit(f"La baraja suma {total} y tiene que sumar 78")
    return True


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LA ESTRUCTURA DE LAS SETENTA Y OCHO
# ══════════════════════════════════════════════════════════════════════
def lamina_estructura():
    p = ['<symbol id="ar-estructura" viewBox="0 0 464 336">']
    # bloque de los mayores
    p.append(f'<rect x="14" y="14" width="436" height="86" rx="10" '
             f'fill="{CARMIN}" opacity=".07"/>')
    p.append(f'<rect x="14" y="14" width="436" height="86" rx="10" fill="none" '
             f'stroke="{CARMIN}" stroke-width="1" opacity=".5"/>')
    p.append(txt(232, 36, "22 ARCANOS MAYORES", "rot", 11, CARMIN))
    p.append(txt(232, 54, "El itinerario · una letra y una atribución cada uno",
                 "et", 11, CLARO))
    for k in range(22):
        x = 26 + k * 19.6
        p.append(f'<rect x="{f(x)}" y="66" width="14" height="22" rx="2" '
                 f'fill="{CARMIN}" opacity=".3"/>')
        p.append(f'<rect x="{f(x)}" y="66" width="14" height="22" rx="2" '
                 f'fill="none" stroke="{CARMIN}" stroke-width=".6" opacity=".7"/>')
    # los cuatro palos
    for i, (clave, nombre, elemento, facultad) in enumerate(PALOS):
        c = COLOR_ELEM[elemento]
        y = 112 + i * 52
        p.append(f'<rect x="14" y="{y}" width="436" height="44" rx="8" '
                 f'fill="{c}" opacity=".06"/>')
        p.append(marca_palo(clave, 22, y + 6, 32, c))
        p.append(txt(64, y + 20, nombre, "rot", 10.4, c, "start"))
        p.append(txt(64, y + 34, facultad, "et", 10.4, APAGADO, "start"))
        # as + nueve numerales + cuatro figuras
        x = 250
        for grupo, cuantas, alto in (("as", 1, 26), ("num", 9, 22), ("fig", 4, 26)):
            for k in range(cuantas):
                p.append(f'<rect x="{f(x)}" y="{f(y + (44 - alto) / 2)}" width="10" '
                         f'height="{alto}" rx="2" fill="{c}" '
                         f'opacity="{.34 if grupo != "num" else .18}"/>')
                x += 12.4
            x += 6
    p.append(txt(232, 328, "22 + 4 × 14 = 78 · AS · DEL DOS AL DIEZ · CUATRO FIGURAS",
                 "rot", 8.2, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LOS VEINTIDÓS MAYORES CON SU LETRA
# ══════════════════════════════════════════════════════════════════════
def lamina_mayores():
    FILA, COL = 30, 232
    ALTO = 36 + 11 * FILA + 16
    p = [f'<symbol id="ar-mayores" viewBox="0 0 464 {ALTO}">']
    for c in range(2):
        x = 8 + c * COL
        p.append(txt(x + 4, 16, "N.º", "rot", 7.2, CARMIN, "start"))
        p.append(txt(x + 30, 16, "ARCANO", "rot", 7.2, CARMIN, "start"))
        p.append(txt(x + 132, 16, "LETRA", "rot", 7.2, CARMIN, "start"))
        p.append(txt(x + 214, 16, "RIGE", "rot", 7.2, CARMIN, "end"))
        p.append(f'<path d="M{x} 22 H{x + 214}" fill="none" stroke="{CARMIN}" '
                 'stroke-width=".8" opacity=".45"/>')
    for i, (num, nombre, letra, valor, clase, rige) in enumerate(ARCANOS):
        c, fila = i // 11, i % 11
        x = 8 + c * COL
        y = 36 + fila * FILA
        # el color dice de qué clase es la letra, igual que en Invocaciones
        col = {"madre": "#ffd75c", "doble": "#ff9d5c", "simple": CIAN}[clase]
        p.append(f'<rect x="{x}" y="{f(y - 12)}" width="214" height="26" rx="4" '
                 f'fill="{col}" opacity=".055"/>')
        p.append(txt(x + 4, y + 5, num, "num", 9.5, CARMIN, "start"))
        p.append(txt(x + 30, y + 5, nombre, "et", 10.8, CLARO, "start"))
        p.append(txt(x + 132, y + 5, letra, "et", 10.4, col, "start"))
        p.append(txt(x + 214, y + 5, rige, "et", 10.4, col, "end"))
    p.append(txt(232, ALTO - 4,
                 "I CON ÁLEF · XXI CON SHIN · EL LOCO CIERRA CON TAV",
                 "rot", 7.6, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LAS TREINTA Y SEIS MENORES Y SUS DECANATOS
# ══════════════════════════════════════════════════════════════════════
def lamina_decanatos():
    FILA = 30
    ALTO = 36 + 12 * FILA + 16
    p = [f'<symbol id="ar-decanatos" viewBox="0 0 464 {ALTO}">']
    for k, etq in enumerate(("0° – 10°", "10° – 20°", "20° – 30°")):
        p.append(txt(160 + k * 104, 16, etq, "rot", 8.2, CARMIN))
    p.append(f'<path d="M108 22 H452" fill="none" stroke="{CARMIN}" '
             'stroke-width=".9" opacity=".45"/>')
    for i, (signo, elemento, modalidad) in enumerate(SIGNOS):
        y = 36 + i * FILA
        c = COLOR_ELEM[elemento]
        tramos = [m for m in MENORES if m["signo"] == signo]
        p.append(glifo_signo(signo, 4, y - 8, 24, c))
        p.append(txt(34, y + 5, signo, "et", 10.8, c, "start"))
        for k, m in enumerate(tramos):
            x = 108 + k * 104
            p.append(f'<rect x="{x}" y="{f(y - 11)}" width="98" height="24" rx="4" '
                     f'fill="{c}" opacity=".08"/>')
            p.append(marca_palo(m["palo"], x + 4, y - 9, 20, c))
            p.append(txt(x + 30, y + 5, f'{m["carta"]} de {m["palo"].capitalize()}',
                         "et", 10.2, CLARO, "start"))
    p.append(txt(232, ALTO - 4,
                 "EL PALO LO DA EL ELEMENTO · EL NÚMERO, LA MODALIDAD",
                 "rot", 7.8, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · LOS CUATRO PALOS Y SUS FIGURAS
# ══════════════════════════════════════════════════════════════════════
def lamina_palos():
    ANCHO, ALTO_C = 108, 218
    p = [f'<symbol id="ar-palos" viewBox="0 0 464 {ALTO_C + 26}">']
    for i, (clave, nombre, elemento, facultad) in enumerate(PALOS):
        x = 8 + i * (ANCHO + 8)
        c = COLOR_ELEM[elemento]
        p.append(f'<rect x="{x}" y="8" width="{ANCHO}" height="{ALTO_C - 8}" rx="10" '
                 f'fill="{c}" opacity=".06"/>')
        p.append(f'<rect x="{x}" y="8" width="{ANCHO}" height="{ALTO_C - 8}" rx="10" '
                 f'fill="none" stroke="{c}" stroke-width=".9" opacity=".45"/>')
        p.append(marca_palo(clave, x + ANCHO / 2 - 22, 22, 44, c))
        p.append(txt(x + ANCHO / 2, 92, nombre.upper(), "rot", 10.4, c))
        p.append(txt(x + ANCHO / 2, 108, elemento.capitalize(), "et", 10.6, CLARO))
        p.append(f'<path d="M{x + 12} 118 H{x + ANCHO - 12}" fill="none" '
                 f'stroke="{c}" stroke-width=".7" opacity=".35"/>')
        for k, (figura, elem_fig) in enumerate(FIGURAS):
            cf = COLOR_ELEM[elem_fig]
            y = 134 + k * 20
            p.append(f'<circle cx="{x + 18}" cy="{f(y - 4)}" r="3.2" fill="{cf}"/>')
            p.append(txt(x + 28, y, figura, "et", 10.4, CLARO, "start"))
            p.append(txt(x + ANCHO - 12, y, elem_fig.capitalize(), "et", 9.6,
                         cf, "end"))
    p.append(txt(232, ALTO_C + 18,
                 "CADA FIGURA LLEVA SU PROPIO ELEMENTO DENTRO DEL PALO",
                 "rot", 7.8, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  LÁMINA · TRES TIRADAS
# ══════════════════════════════════════════════════════════════════════
TIRADAS = [
    ("LAS TRES", "Qué había · qué hay · qué falta",
     [(0, 0, "1"), (1, 0, "2"), (2, 0, "3")]),
    ("LA CRUZ DE CUATRO", "El hecho · lo que aporto · lo que estorba · el paso",
     [(1, 0, "2"), (0, 1, "3"), (1, 1, "1"), (1, 2, "4")]),
    ("EL ESPEJO", "Como lo veo · como lo ve el otro · lo que ninguno ve",
     [(0, 0, "1"), (2, 0, "2"), (1, 1, "3")]),
]


def lamina_tiradas():
    W, H, GAP = 26, 40, 6
    p = ['<symbol id="ar-tiradas" viewBox="0 0 464 216">']
    for i, (nombre, glosa, celdas) in enumerate(TIRADAS):
        ox = 14 + i * 148
        p.append(f'<rect x="{ox}" y="10" width="132" height="150" rx="10" '
                 f'fill="{CARMIN}" opacity=".05"/>')
        # se centra la retícula de la tirada dentro del panel
        cols = max(c for c, _, _ in celdas) + 1
        filas = max(r for _, r, _ in celdas) + 1
        x0 = ox + (132 - (cols * W + (cols - 1) * GAP)) / 2
        y0 = 22 + (128 - (filas * H + (filas - 1) * GAP)) / 2
        for c, r, num in celdas:
            x = x0 + c * (W + GAP)
            y = y0 + r * (H + GAP)
            p.append(f'<rect x="{f(x)}" y="{f(y)}" width="{W}" height="{H}" rx="3" '
                     f'fill="{CARMIN}" opacity=".16"/>')
            p.append(f'<rect x="{f(x)}" y="{f(y)}" width="{W}" height="{H}" rx="3" '
                     f'fill="none" stroke="{CARMIN}" stroke-width="1"/>')
            p.append(txt(x + W / 2, y + H / 2 + 4, num, "num", 12, CARMIN))
        p.append(txt(ox + 66, 176, nombre, "rot", 9.6, CARMIN))
        p.append(txt(ox + 66, 192, glosa, "et", 10, CLARO))
    p.append(txt(232, 212, "TRES TIRADAS PROPIAS · NINGUNA PREDICE NADA",
                 "rot", 7.8, APAGADO))
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
#  SÍMBOLO DE CUBIERTA
# ══════════════════════════════════════════════════════════════════════
def simbolo_cubierta():
    """Tres cartas abiertas en abanico dentro de una orla de veintidós marcas."""
    p = ['<symbol id="r-arcano" viewBox="0 0 240 240">']
    p.append(f'<circle cx="120" cy="120" r="112" fill="none" stroke="var(--acento)" '
             'stroke-width="1.2" opacity=".35"/>')
    p.append(f'<circle cx="120" cy="120" r="102" fill="none" stroke="var(--acento)" '
             'stroke-width="2.4" opacity=".85"/>')
    marcas = []
    for k in range(22):
        ang = k * 360 / 22
        x1, y1 = pol(120, 120, 102, ang)
        x2, y2 = pol(120, 120, 92, ang)
        marcas.append(f"M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}")
    p.append(f'<path d="{" ".join(marcas)}" fill="none" stroke="var(--acento)" '
             'stroke-width="1.4" opacity=".55"/>')
    for ang, esc in ((-22, .86), (22, .86), (0, 1.0)):   # la central, al final
        p.append(f'<g transform="rotate({ang} 120 190) translate(120,120) '
                 f'scale({esc}) translate(-120,-120)">'
                 f'<rect x="{120 - 30}" y="{120 - 46}" width="60" height="92" rx="5" '
                 'fill="#0a0a14" stroke="var(--acento)" stroke-width="2.4"/>'
                 f'<rect x="{120 - 23}" y="{120 - 39}" width="46" height="78" rx="3" '
                 'fill="none" stroke="var(--acento)" stroke-width=".9" opacity=".4"/>'
                 "</g>")
    # el sello de la carta central: estrella de cinco sobre círculo
    est = [pol(120, 118, 22, k * 144) for k in range(6)]
    p.append('<path d="M' + " L".join(f"{f(x)} {f(y)}" for x, y in est)
             + '" fill="none" stroke="var(--acento-2)" stroke-width="2" '
               'stroke-linejoin="round"/>')
    p.append('<circle cx="120" cy="118" r="30" fill="none" '
             'stroke="var(--acento-2)" stroke-width="1" opacity=".5"/>')
    p.append("</symbol>")
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════
def main():
    comprobar()
    piezas = [
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'style="position:absolute;width:0;height:0;overflow:hidden" '
        'aria-hidden="true">',
        """
<!-- ════════════════════════════════════════════════════════════════
     CÓDICE DE LOS ARCANOS · repertorio gráfico
     Dibujo original de VILLUMINATIONS — generado por
     tools/dibujar-arcanos.py. No editar a mano.
     ════════════════════════════════════════════════════════════ -->""",
        '<style>'
        "svg .rot{ font-family:'Orbitron',sans-serif; font-weight:700;"
        ' letter-spacing:.1em }'
        "svg .num{ font-family:'Orbitron',sans-serif; font-weight:600 }"
        "svg .et{ font-family:'Rajdhani',sans-serif; font-weight:600 }"
        '</style>',
        simbolo_cubierta(),
        lamina_estructura(),
        lamina_mayores(),
        lamina_decanatos(),
        lamina_palos(),
        lamina_tiradas(),
        "</svg>",
    ]
    DESTINO.write_text("\n".join(piezas) + "\n")
    print(f"  {DESTINO.relative_to(RAIZ)}: 5 láminas + cubierta · "
          f"22 mayores y 36 decanatos deducidos y comprobados · "
          f"{DESTINO.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
