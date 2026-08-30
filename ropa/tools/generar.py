#!/usr/bin/env python3
"""
VILLUMINATIONS — El generador de las láminas de espalda
=======================================================

    python3 ropa/tools/generar.py          # rehace ropa/partials/signos.svg
    python3 ropa/tools/generar.py --hoja   # y además el contacto para mirarlas

Doce láminas de espalda, una por signo, dibujadas aquí y no copiadas de
ningún sitio. Se generan con código por la misma razón por la que los libros
se componen con código: para que las doce compartan gramática y para que
cambiar el grosor de un trazo no sean doce ficheros abiertos a mano.

La gramática, en cinco piezas
-----------------------------
Todas las láminas están hechas de lo mismo, y eso es lo que las hace una
familia en vez de doce dibujos sueltos:

1. **El eje.** Una pila de galones en V que baja por la columna, estrechándose.
   Es la letra de la marca repetida hasta volverse anatomía. Nadie más puede
   usarla porque nadie más se llama así.
2. **La envergadura.** Dos brazos que salen de los omóplatos con el mismo
   ángulo del galón. No son alas de nadie: son el mismo ángulo llevado afuera.
3. **Los filamentos.** Ramas finas que se desprenden de la envergadura y se
   apagan. Dan el peso visual que pide una espalda sin llenarla de tinta.
4. **La corona.** El glifo del signo, entre los omóplatos, dibujado con el
   mismo grosor que el eje.
5. **Los tres decanos.** Tres rombos en la columna. Están porque el sistema de
   decanos es nuestro terreno —hay un libro y un artículo— y porque tres
   marcas leen a diez metros mejor que un párrafo.

El color no es decorativo
-------------------------
Un acento por signo, heredado de su elemento: fuego, tierra, aire y agua. Los
doce no son doce colores sueltos; son cuatro familias con tres tonos cada una,
así que la parrilla del año se lee como una parrilla y no como un muestrario.

Lo que este fichero no decide
-----------------------------
En qué prenda va cada lámina, a qué tamaño y con qué método se estampa. Eso
sale de la hoja del proveedor de estampación y **no se puede inventar**:
`tienda/ropa.py` lo exige y aborta sin ello.
"""

import math
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
DESTINO = RAIZ / "ropa" / "partials" / "signos.svg"

ANCHO, ALTO = 800, 1000
EJE = ANCHO / 2

# ---------------------------------------------------------------------------
# Los doce, en orden de rueda. Cada uno con su elemento, sus fechas y el
# nombre en las tres lenguas. Las fechas son las de la temporada tropical y
# varían un día según el año; por eso se dicen como aproximadas.
# ---------------------------------------------------------------------------
SIGNOS = [
    ("aries",       "fuego",  (3, 21), (4, 19),  "Aries",       "Aries",       "Bélier"),
    ("tauro",       "tierra", (4, 20), (5, 20),  "Tauro",       "Taurus",      "Taureau"),
    ("geminis",     "aire",   (5, 21), (6, 20),  "Géminis",     "Gemini",      "Gémeaux"),
    ("cancer",      "agua",   (6, 21), (7, 22),  "Cáncer",      "Cancer",      "Cancer"),
    ("leo",         "fuego",  (7, 23), (8, 22),  "Leo",         "Leo",         "Lion"),
    ("virgo",       "tierra", (8, 23), (9, 22),  "Virgo",       "Virgo",       "Vierge"),
    ("libra",       "aire",   (9, 23), (10, 22), "Libra",       "Libra",       "Balance"),
    ("escorpio",    "agua",   (10, 23), (11, 21), "Escorpio",   "Scorpio",     "Scorpion"),
    ("sagitario",   "fuego",  (11, 22), (12, 21), "Sagitario",  "Sagittarius", "Sagittaire"),
    ("capricornio", "tierra", (12, 22), (1, 19), "Capricornio", "Capricorn",   "Capricorne"),
    ("acuario",     "aire",   (1, 20), (2, 18),  "Acuario",     "Aquarius",    "Verseau"),
    ("piscis",      "agua",   (2, 19), (3, 20),  "Piscis",      "Pisces",      "Poissons"),
]

# Cuatro familias, tres tonos cada una. El tercer tono de cada familia es el
# más apagado a propósito: el año no puede ir a grito constante.
ACENTO = {
    "fuego":  ["#ff3b2f", "#ff7a18", "#c81e3a"],
    "tierra": ["#c9a227", "#8fae4b", "#a3711f"],
    "aire":   ["#7cc4ff", "#b4a7ff", "#5ad2c4"],
    "agua":   ["#2f6bff", "#6c4cff", "#1f9ea8"],
}
_usados = {}

# El elemento no cambia solo el color: cambia el dibujo. Doce láminas idénticas
# salvo el tono son un muestrario, no una serie. Cada familia tiene su número
# de costillas, su largo, su grosor y su curvatura, y eso se ve a un metro sin
# leer el pie.
TEMPERAMENTO = {
    #          costillas  largo  grosor  curva  vértebras
    "fuego":  (21,        1.14,  0.86,   0.62,  13),   # muchas, largas, finas
    "tierra": (12,        0.84,  1.42,   0.30,   9),   # pocas, cortas, gruesas
    "aire":   (23,        1.02,  0.62,   1.05,  14),   # abanico ancho y leve
    "agua":   (16,        1.08,  0.94,   1.55,  11),   # ondulantes, largas
}


def acento(elemento: str) -> str:
    i = _usados.get(elemento, 0)
    _usados[elemento] = i + 1
    return ACENTO[elemento][i % 3]


# ---------------------------------------------------------------------------
# El trazo básico: la púa que se afila
# ---------------------------------------------------------------------------
# Un `stroke` de SVG tiene grosor constante, y un grosor constante da dibujo
# de cable. Todo lo que hay aquí está construido como **silueta rellena**: dos
# curvas que salen de una base ancha y se juntan en la punta. Es lo que
# distingue una filigrana de un esquema, y es más trabajo de calcular, pero es
# el trabajo que se ve.
def pua(x, y, ang, largo, grueso, curva=0.42, filo=1.0) -> str:
    """Una púa afilada: base ancha en (x,y), punta a `largo` en dirección `ang`."""
    dx, dy = math.cos(ang), math.sin(ang)
    nx, ny = -dy, dx                                   # normal a la dirección
    xp, yp = x + dx * largo, y + dy * largo            # la punta
    # el arco: se desvía hacia la normal a mitad de camino
    cx = x + dx * largo * 0.5 + nx * largo * curva * 0.5
    cy = y + dy * largo * 0.5 + ny * largo * curva * 0.5
    g = grueso / 2
    return (f'<path d="M{x + nx * g:.1f},{y + ny * g:.1f} '
            f'Q{cx + nx * g * filo:.1f},{cy + ny * g * filo:.1f} '
            f'{xp:.1f},{yp:.1f} '
            f'Q{cx - nx * g * filo * 0.35:.1f},{cy - ny * g * filo * 0.35:.1f} '
            f'{x - nx * g:.1f},{y - ny * g:.1f} Z" fill="var(--tinta)"/>')


# ---------------------------------------------------------------------------
# Las cinco piezas de la gramática
# ---------------------------------------------------------------------------
def envergadura(lado=1, elemento="fuego", y=286, semilla=0) -> str:
    """El abanico que cruza los omóplatos.

    Antes era una sola forma rellena y se leía como mancha: en la primera
    prueba impresa habría salido un babero. Ahora son quince púas que salen
    del mismo origen con ángulos y largos escalonados, cada una con su
    ramita. La densidad la dan los trazos, no el área.
    """
    costillas, k_largo, k_grueso, k_curva, _v = TEMPERAMENTO[elemento]
    partes = []
    for i in range(costillas):
        t = i / (costillas - 1)
        # Las bases se reparten por la línea del hombro en vez de salir todas
        # del mismo punto. Cuando salían del mismo punto, quince bases de
        # treinta unidades se fundían en una plancha blanca y se comían el
        # glifo: el defecto se vio en la primera hoja de contacto.
        ox = EJE + lado * (14 + 104 * (t ** 0.80))
        oy = y + 52 - 86 * (t ** 0.85)
        ang = math.radians(-9 - 68 * t + 7 * math.sin(t * 7 + semilla))
        if lado < 0:
            ang = math.pi - ang
        largo = 272 * k_largo * (1 - 0.40 * (t ** 1.9)) * (0.78 + 0.30 * math.sin(t * 4.3 + semilla))
        # El grosor máximo va a media envergadura, no en la base. Cuando la
        # base era la más gruesa, las primeras costillas —que salen casi del
        # mismo punto y casi al mismo ángulo— se solapaban en una cuña maciza.
        grueso = (4 + 13 * math.sin(math.pi * (t ** 0.75))) * k_grueso
        curva = (0.24 + 0.30 * math.sin(t * 2.6 + semilla * 0.4)) * k_curva
        partes.append(pua(ox, oy, ang, largo, grueso, curva * lado))
        # una ramita a media púa: es lo que convierte el abanico en filigrana
        if i % 2 == 0:
            mx = ox + math.cos(ang) * largo * 0.58
            my = oy + math.sin(ang) * largo * 0.58
            partes.append(pua(mx, my, ang - lado * 0.55, largo * 0.36,
                              grueso * 0.46, curva * lado * 1.5))
        if i % 3 == 1:
            mx = ox + math.cos(ang) * largo * 0.34
            my = oy + math.sin(ang) * largo * 0.34
            partes.append(pua(mx, my, ang + lado * 0.44, largo * 0.26,
                              grueso * 0.34, -curva * lado))
    return "\n    ".join(partes)


def eje(elemento="fuego", y0=378, y1=858, semilla=0) -> str:
    """La columna: pares de púas que bajan estrechándose, sobre un filo central.

    La pila de galones que había aquí antes se leía como una fila de signos
    de «menor que». Una vértebra tiene dos costados y un centro, y así está
    dibujada ahora.
    """
    _c, _l, k_grueso, k_curva, vertebras = TEMPERAMENTO[elemento]
    partes = [f'<path d="M{EJE - 7},{y0 - 26} L{EJE + 7},{y0 - 26} '
              f'L{EJE + 2.2},{y1 + 40} L{EJE - 2.2},{y1 + 40} Z" '
              f'fill="var(--tinta)"/>']
    for i in range(vertebras):
        t = i / (vertebras - 1)
        y = y0 + (y1 - y0) * (t ** 1.06)
        largo = 168 * (1 - 0.80 * (t ** 0.82))
        grueso = (26 * (1 - 0.74 * t) + 2.5) * (0.7 + 0.3 * k_grueso)
        ang = math.radians(28 + 30 * t + 6 * math.sin(t * 5 + semilla))
        for lado in (-1, 1):
            a = math.pi - ang if lado < 0 else ang
            partes.append(pua(EJE + lado * 5, y, a, largo, grueso,
                              0.30 * lado * k_curva))
    return "\n    ".join(partes)


def decanos(y0=596, paso=104) -> str:
    """Tres rombos en la columna: los tres decanos del signo.

    Tres marcas se leen a diez metros. Un párrafo no. Y los decanos son
    terreno propio: hay un libro y un artículo detrás.
    """
    partes = []
    for i in range(3):
        y = y0 + i * paso
        r = 20 - i * 4
        partes.append(
            f'<path d="M{EJE},{y - r} L{EJE + r * 0.70:.1f},{y} '
            f'L{EJE},{y + r} L{EJE - r * 0.70:.1f},{y} Z" '
            f'fill="var(--acento)"/>')
    return "\n    ".join(partes)


def cola(y=858, largo=112) -> str:
    """El remate de la columna: una púa larga hacia abajo y dos cortas.

    Sin remate el dibujo se queda colgando a media espalda. Con él baja la
    mirada hasta la firma, que es donde tiene que acabar.
    """
    return "\n    ".join([
        pua(EJE, y, math.radians(90), largo, 15, 0.0),
        pua(EJE - 4, y - 12, math.radians(112), largo * 0.46, 8, 0.30),
        pua(EJE + 4, y - 12, math.radians(68), largo * 0.46, 8, -0.30),
    ])


# ---------------------------------------------------------------------------
# Los doce glifos, dibujados aquí
# ---------------------------------------------------------------------------
# Los signos del zodiaco son marcas de tradición, transmitidas por escrito
# durante siglos y de nadie. Lo que sí es de alguien es **cada versión
# concreta**, así que estas están trazadas para esta serie: mismo grosor que
# el eje, mismos extremos redondeados, y ninguna copiada de una tipografía.
# Van en una caja de 100 centrada en el origen.
GLIFOS = {
    "aries": "M-38,26 C-38,-18 -20,-30 -6,-30 C4,-30 8,-22 8,-12 L8,30 "
             "M38,26 C38,-18 20,-30 6,-30 C-4,-30 -8,-22 -8,-12 L-8,30",
    "tauro": "M0,32 m-26,0 a26,26 0 1,0 52,0 a26,26 0 1,0 -52,0 "
             "M-34,-30 C-34,-4 -18,4 0,4 C18,4 34,-4 34,-30",
    "geminis": "M-30,-32 L30,-32 M-30,32 L30,32 M-15,-32 L-15,32 "
               "M15,-32 L15,32",
    "cancer": "M-36,-8 C-36,-26 -16,-32 6,-28 M-24,-8 m-11,0 a11,11 0 1,0 22,0 "
              "a11,11 0 1,0 -22,0 M36,10 C36,28 16,34 -6,30 "
              "M24,10 m-11,0 a11,11 0 1,0 22,0 a11,11 0 1,0 -22,0",
    "leo": "M-14,14 m-16,0 a16,16 0 1,0 32,0 a16,16 0 1,0 -32,0 "
           "M0,2 C-2,-18 4,-32 16,-32 C28,-32 32,-22 28,-12 "
           "C22,2 22,18 34,26",
    "virgo": "M-36,-26 L-36,26 M-36,-16 C-36,-28 -20,-28 -20,-16 L-20,26 "
             "M-20,-16 C-20,-28 -4,-28 -4,-16 L-4,20 "
             "C-4,30 10,30 14,20 M14,20 C22,0 34,10 30,26 "
             "C26,38 6,32 0,22",
    "libra": "M-38,30 L38,30 M-28,12 L28,12 M-22,12 C-22,-14 -10,-24 0,-24 "
             "C10,-24 22,-14 22,12",
    "escorpio": "M-38,-22 L-38,26 M-38,-12 C-38,-24 -22,-24 -22,-12 L-22,26 "
                "M-22,-12 C-22,-24 -6,-24 -6,-12 L-6,26 "
                "M-6,-12 C-6,-24 10,-24 10,-12 L10,20 L34,20 "
                "M34,20 L22,10 M34,20 L22,32",
    "sagitario": "M-32,32 L26,-26 M26,-26 L4,-26 M26,-26 L26,-4 "
                 "M-16,0 L2,18",
    "capricornio": "M-36,-24 C-36,4 -22,26 -10,26 C-2,26 0,16 0,4 L0,-18 "
                   "M0,-18 C6,-28 22,-28 26,-14 C30,0 20,12 8,10 "
                   "C0,8 -2,0 2,-6",
    "acuario": "M-36,-14 L-18,-26 L0,-14 L18,-26 L36,-14 "
               "M-36,14 L-18,2 L0,14 L18,2 L36,14",
    "piscis": "M-22,-32 C-36,-14 -36,14 -22,32 M22,-32 C36,-14 36,14 22,32 "
              "M-30,0 L30,0",
}


def corona(clave: str, y=168, escala=1.42) -> str:
    """El glifo del signo, entre los omóplatos."""
    return (f'<g transform="translate({EJE},{y}) scale({escala})">'
            f'<path d="{GLIFOS[clave]}" fill="none" stroke="var(--tinta)" '
            f'stroke-width="{10 / escala:.1f}" stroke-linecap="round" '
            f'stroke-linejoin="round"/></g>')


def halo(y=168, r=124) -> str:
    """El aro tenue detrás de la corona.

    Está por una razón aprendida en el vídeo de la cabecera: una forma suelta
    en medio de la nada se lee como mancha. Con un aro detrás se lee como
    centro.
    """
    return (f'<circle cx="{EJE}" cy="{y}" r="{r}" fill="none" '
            f'stroke="var(--acento)" stroke-width="3" opacity="0.55"/>'
            f'<circle cx="{EJE}" cy="{y}" r="{r - 13}" fill="none" '
            f'stroke="var(--tinta)" stroke-width="1.5" opacity="0.35"/>')


def firma(nombre: str) -> str:
    """El pie: la marca y el signo. Se escribe una vez y va en las doce."""
    return (
        f'<text x="{EJE}" y="944" text-anchor="middle" fill="var(--tinta)" '
        f'font-family="Georgia, \'Times New Roman\', serif" font-size="30" '
        f'letter-spacing="11">VILLUMINATIONS</text>\n    '
        f'<text x="{EJE}" y="978" text-anchor="middle" fill="var(--acento)" '
        f'font-family="Georgia, \'Times New Roman\', serif" font-size="19" '
        f'letter-spacing="7">{nombre.upper()}</text>')


# ---------------------------------------------------------------------------
# El montaje
# ---------------------------------------------------------------------------
def lamina(clave: str, elemento: str, nombre: str, tinta: str,
           color: str) -> str:
    """Una lámina entera, como <symbol> reutilizable.

    El color va por variable CSS y no incrustado: la misma lámina se estampa
    en blanco sobre negro y en negro sobre blanco sin generar dos ficheros.
    """
    n = sum(ord(c) for c in clave) % 17
    return f"""  <symbol id="vi-{clave}" viewBox="0 0 {ANCHO} {ALTO}"
      style="--tinta:{tinta}; --acento:{color}">
    {halo()}
    {envergadura(-1, elemento, semilla=n)}
    {envergadura(1, elemento, semilla=n)}
    {eje(elemento, semilla=n)}
    {cola()}
    {corona(clave)}
    {decanos()}
    {firma(nombre)}
  </symbol>"""


def construir(tinta="#f2f0ea") -> str:
    _usados.clear()
    piezas = [lamina(c, el, es, tinta, acento(el))
              for c, el, _d, _h, es, _en, _fr in SIGNOS]
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {ANCHO} {ALTO}" width="0" height="0" '
        'style="position:absolute">\n'
        "<!-- VILLUMINATIONS · láminas de espalda, una por signo.\n"
        "     Generado por ropa/tools/generar.py. No se edita a mano:\n"
        "     lo que se escriba aquí se pierde en la siguiente pasada. -->\n"
        + "\n".join(piezas) + "\n</svg>\n")


def main() -> int:
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(construir(), encoding="utf-8")
    print(f"\n  {len(SIGNOS)} láminas en {DESTINO.relative_to(RAIZ)} "
          f"({DESTINO.stat().st_size // 1024} KB)\n")
    for clave, elemento, d, h, es, _en, _fr in SIGNOS:
        print(f"    vi-{clave:12} {elemento:7} {es:12} "
              f"{d[0]:02}-{d[1]:02} → {h[0]:02}-{h[1]:02}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
