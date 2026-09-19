#!/usr/bin/env python3
"""
VILLUMINATIONS — El calendario de lanzamientos
==============================================

    python3 tienda/calendario.py              # el año entero y sus problemas
    python3 tienda/calendario.py --hoy        # qué está vivo ahora mismo
    python3 tienda/calendario.py --ical       # el año en .ics para el móvil

Doce lanzamientos, uno por signo, y **cada uno abre el día que abre su
temporada**. No el día 1 del mes.

Por qué eso importa, y no es un capricho
----------------------------------------
Un calendario de doce meses lo puede montar cualquiera: se eligen doce colores
y se reparten. Lo hace todo el mundo y por eso no distingue a nadie.

Aquí la rejilla no es el mes, es **la rueda**. El lanzamiento de Aries abre el
21 de marzo porque ese día empieza Aries, y cierra el 19 de abril porque ese
día se acaba. Eso hace tres cosas que el mes no hace:

· **La fecha la pone el cielo, no nosotros.** Nadie tiene que creerse que el
  drop de marzo es especial. Empieza cuando empieza, y se puede comprobar.
· **Hay una razón para volver.** Quien compra el suyo tiene una fecha propia
  al año, y las otras once son de otros. Un mes no es de nadie.
· **Nos sale gratis y a ellos no.** Nosotros ya teníamos los doce signos
  dibujados, un libro entero sobre ellos y un artículo sobre los decanos. Una
  marca que solo vende ropa tendría que inventarse el contenido, y se le
  notaría.

Las fechas se mueven un día según el año
----------------------------------------
La entrada del Sol en cada signo cae un 20 o un 21 según el año bisiesto. Aquí
se guarda la fecha civil que se anuncia, no la efeméride exacta, y `NOTA_FECHA`
lo dice en las tres lenguas. Prometer una hora exacta obligaría a recalcularla
cada año y a corregir la tienda cuando fallara.

Lo que este fichero no decide
-----------------------------
En qué prenda va cada lámina, a qué tamaño y con qué método se estampa. Eso
sale de la hoja del proveedor de estampación y no se puede inventar:
`tienda/ropa.py` lo exige y aborta sin ello. Este calendario dice **qué sale y
cuándo**; el qué es una prenda concreta todavía no.
"""

import datetime as dt
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tienda"))
sys.path.insert(0, str(RAIZ / "ropa" / "tools"))

LAMINA = "ropa/partials/signos.svg"

# ---------------------------------------------------------------------------
# Los doce lanzamientos. El nombre de cada uno no es el del signo: es lo que
# hace ese trozo del año. El signo va debajo, en el pie de la lámina.
# ---------------------------------------------------------------------------
DROPS = [
    ("aries", "Primer Filo", "First Edge", "Premier Fil",
     "Abre la rueda el día del equinoccio. La temporada de empezar otra vez."),
    ("tauro", "Peso Muerto", "Dead Weight", "Poids Mort",
     "Lo que se sostiene sin moverse: la fuerza que no sale en la foto."),
    ("geminis", "Dos Voces", "Two Voices", "Deux Voix",
     "El glifo son dos barras iguales. Es el único que no se puede leer solo."),
    ("cancer", "Marea Alta", "High Tide", "Marée Haute",
     "Abre en el solsticio de verano, el día más largo del año."),
    ("leo", "Corona Solar", "Solar Crown", "Couronne Solaire",
     "El acento más caliente de los doce. Se lleva a plena luz o no se lleva."),
    ("virgo", "Cuenta Exacta", "Exact Count", "Compte Exact",
     "La temporada de medir. Es la que menos gusta y la que más cambia."),
    ("libra", "Punto de Equilibrio", "Balance Point", "Point d'Équilibre",
     "Abre en el equinoccio de otoño: doce horas de luz y doce de sombra."),
    ("escorpio", "Fondo Negro", "Black Depth", "Fond Noir",
     "La temporada en que el día se acorta más deprisa."),
    ("sagitario", "Tiro Largo", "Long Shot", "Tir Long",
     "El glifo es una flecha, y es el único de los doce que apunta afuera."),
    ("capricornio", "Ascenso Frío", "Cold Ascent", "Ascension Froide",
     "Abre en el solsticio de invierno, el día más corto. Se sube cuando peor "
     "se está."),
    ("acuario", "Corriente", "Current", "Courant",
     "El glifo son dos ondas. La temporada de romper el patrón."),
    ("piscis", "Última Vuelta", "Last Turn", "Dernier Tour",
     "Cierra la rueda y devuelve al primero. Se agota cuando entra Aries."),
]

# Lo que distingue a una lámina de otra **no se escribe a mano**. Se dice una
# vez por elemento y se compone, porque escribirlo doce veces es escribir doce
# veces algo que puede dejar de ser verdad. Ya pasó una vez en los libros: la
# prosa prometía siete láminas y había seis, y en tres idiomas.
DIBUJO = {
    "fuego": ("Veintiuna costillas largas y finas: el abanico más denso de "
              "los cuatro.",
              "Twenty-one long, fine ribs: the densest fan of the four.",
              "Vingt et une côtes longues et fines : l'éventail le plus dense "
              "des quatre."),
    "tierra": ("Doce costillas cortas y gruesas: la más pesada de tinta y la "
               "que menos se abre.",
               "Twelve short, thick ribs: the heaviest in ink and the least "
               "spread.",
               "Douze côtes courtes et épaisses : la plus lourde en encre et "
               "la moins ouverte."),
    "aire": ("Veintitrés costillas, el abanico más ancho y el trazo más leve "
             "de la serie.",
             "Twenty-three ribs, the widest fan and the lightest stroke in "
             "the series.",
             "Vingt-trois côtes, l'éventail le plus large et le trait le plus "
             "léger de la série."),
    "agua": ("Dieciséis costillas que se rizan: es la de curvatura más "
             "marcada, y por eso la que más se mueve.",
             "Sixteen curling ribs: the most strongly curved of the four, and "
             "so the one that moves most.",
             "Seize côtes qui s'enroulent : la plus courbée des quatre, donc "
             "celle qui bouge le plus."),
}

# La entrada del Sol en cada signo, en fecha civil. Copiadas de generar.SIGNOS
# para no tener dos verdades: `comprobar()` exige que coincidan.
NOTA_FECHA = {
    "es": ("La entrada del Sol en cada signo cae un día antes o después según "
           "el año. Las fechas anunciadas son las civiles."),
    "en": ("The Sun's entry into each sign falls a day earlier or later "
           "depending on the year. The dates announced are the civil ones."),
    "fr": ("L'entrée du Soleil dans chaque signe tombe un jour plus tôt ou "
           "plus tard selon l'année. Les dates annoncées sont les civiles."),
}

ANUNCIO = {
    "es": "Abre el {inicio} y cierra el {fin}. Después no vuelve hasta el año que viene.",
    "en": "Opens {inicio} and closes {fin}. After that it does not return until next year.",
    "fr": "Ouvre le {inicio} et ferme le {fin}. Ensuite il ne revient pas avant l'an prochain.",
}

MES = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
           "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"],
}


# ---------------------------------------------------------------------------
# Para que la guarda pueda leer una cifra escrita con letras. Solo los
# números que la serie usa: inventar una tabla entera sería inventar trabajo.
_NUMERO = {
    12: "doce", 16: "dieciséis", 21: "veintiuna", 23: "veintitrés",
}


def temporadas() -> dict:
    """signo -> ((mes, día) de apertura, (mes, día) de cierre).

    Vienen del generador de láminas, que es donde ya estaban. Tener las fechas
    en dos sitios es tener dos fechas: tarde o temprano una se corrige y la
    otra no.
    """
    import generar
    return {c: (d, h) for c, _el, d, h, _es, _en, _fr in generar.SIGNOS}


def fecha(par: tuple, lengua: str) -> str:
    mes, dia = par
    if lengua == "en":
        return f"{MES['en'][mes - 1]} {dia}"
    if lengua == "fr":
        return f"{dia} {MES['fr'][mes - 1]}"
    return f"{dia} de {MES['es'][mes - 1]}"


def vivo(hoy: dt.date = None) -> str:
    """Qué lanzamiento está abierto en esa fecha. Siempre hay uno."""
    hoy = hoy or dt.date.today()
    for signo, ((m0, d0), (m1, d1)) in temporadas().items():
        inicio, fin = (m0, d0), (m1, d1)
        if inicio <= fin:                       # temporada dentro del año
            if inicio <= (hoy.month, hoy.day) <= fin:
                return signo
        else:                                   # la de Capricornio, que cruza
            if (hoy.month, hoy.day) >= inicio or (hoy.month, hoy.day) <= fin:
                return signo
    return ""


def dias(par: tuple, anio=2001) -> int:
    """Día del año, en un año no bisiesto de referencia."""
    return dt.date(anio, par[0], par[1]).timetuple().tm_yday


def comprobar() -> list:
    """Lo que impide anunciar el calendario. Vacío es lo correcto."""
    import re
    malos = []
    temp = temporadas()

    # 1. Cada lanzamiento tiene que señalar una lámina que exista de verdad.
    #    Es la misma regla que ropa.py aplica a los diseños: un lanzamiento sin
    #    dibujo propio es un anuncio de nada.
    fichero = RAIZ / LAMINA
    disponibles = set(re.findall(r'<symbol[^>]*\bid="([^"]+)"',
                                 fichero.read_text(encoding="utf-8"))
                      ) if fichero.exists() else set()
    for signo, *_ in DROPS:
        if f"vi-{signo}" not in disponibles:
            malos.append(f"{signo} · la lámina «{LAMINA}#vi-{signo}» no está "
                         f"en el repositorio")

    # 2. Los doce tienen que ser los doce, sin repetir ni faltar.
    if len(DROPS) != 12 or len({d[0] for d in DROPS}) != 12:
        malos.append("no hay doce lanzamientos distintos")
    if {d[0] for d in DROPS} != set(temp):
        malos.append("los lanzamientos y los signos del generador no coinciden")

    # 3. Las doce temporadas tienen que embaldosar el año: sin huecos y sin
    #    solapes. Un día descubierto es un día en que la tienda no sabe qué
    #    está vendiendo, y con doce pares de fechas escritas a mano eso pasa
    #    a la primera.
    cubierto = {}
    for signo, (ini, fin) in temp.items():
        d0, d1 = dias(ini), dias(fin)
        rango = (list(range(d0, d1 + 1)) if d0 <= d1
                 else list(range(d0, 366)) + list(range(1, d1 + 1)))
        for d in rango:
            if d in cubierto:
                malos.append(f"el día {d} del año lo reclaman «{cubierto[d]}» "
                             f"y «{signo}» a la vez")
            cubierto[d] = signo
    huecos = [d for d in range(1, 366) if d not in cubierto]
    if huecos:
        malos.append(f"{len(huecos)} días del año sin lanzamiento asignado "
                     f"(el primero, el día {huecos[0]})")

    # 4. Las cifras que DIBUJO dice tienen que ser las que el generador
    #    dibuja. Es la misma guarda que comprobar_laminas() en los libros: allí
    #    la prosa prometía siete láminas y había seis, en tres idiomas. Aquí
    #    prometería veintiuna costillas y habría doce.
    import generar
    for elemento, (es, en, fr) in DIBUJO.items():
        costillas = generar.TEMPERAMENTO[elemento][0]
        letras = _NUMERO.get(costillas)
        if letras is None:
            malos.append(f"{elemento} · no sé escribir {costillas} con "
                         f"letras; añádelo a _NUMERO")
        elif letras not in es.lower():
            malos.append(f"{elemento} · el texto no dice «{letras}» y el "
                         f"generador dibuja {costillas} costillas")
        if not (es and en and fr):
            malos.append(f"{elemento} · falta el dibujo en alguna lengua")

    # 5. Cada elemento tiene que tener tres signos. Si no, el reparto de
    #    tonos de generar.ACENTO se repite y dos láminas salen iguales.
    reparto = {}
    for _c, el, *_r in generar.SIGNOS:
        reparto[el] = reparto.get(el, 0) + 1
    for elemento, n in sorted(reparto.items()):
        if n != 3:
            malos.append(f"{elemento} · {n} signos en vez de 3: los tonos de "
                         f"ACENTO se repetirían")

    # 6. Nada de prometer prenda hasta que haya hoja del proveedor.
    import ropa
    if not ropa.PRENDAS:
        for signo, es, *_ in DROPS:
            if any(p in es.lower() for p in
                   ("camiseta", "sudadera", "pantalón", "hoodie", "tee")):
                malos.append(f"{signo} · el nombre nombra una prenda y "
                             f"todavía no hay hoja del proveedor")
    return malos


def dibujo(signo: str) -> tuple:
    """Qué distingue esta lámina, dicho por su elemento y no a mano."""
    import generar
    elemento = next(el for c, el, *_r in generar.SIGNOS if c == signo)
    return DIBUJO[elemento]


def anuncio(signo: str, lengua: str) -> str:
    ini, fin = temporadas()[signo]
    return ANUNCIO[lengua].format(inicio=fecha(ini, lengua),
                                  fin=fecha(fin, lengua))


def ical() -> str:
    """El año en .ics, para no depender de que nadie se acuerde.

    Doce eventos de día completo con repetición anual. Se abre en el móvil y
    ya está: las fechas de apertura dejan de vivir en la cabeza de alguien.
    """
    lineas = ["BEGIN:VCALENDAR", "VERSION:2.0",
              "PRODID:-//VILLUMINATIONS//calendario//ES",
              "X-WR-CALNAME:VILLUMINATIONS · lanzamientos"]
    for signo, es, _en, _fr, _nota in DROPS:
        ini, fin = temporadas()[signo]
        d0 = dt.date(2001, *ini)
        # DTEND de un evento de día completo es exclusivo: el día siguiente.
        d1 = dt.date(2001 if dias(fin) >= dias(ini) else 2002, *fin) + \
            dt.timedelta(days=1)
        lineas += [
            "BEGIN:VEVENT",
            f"UID:{signo}@villuminations.com",
            f"SUMMARY:{es} · {signo.capitalize()}",
            f"DTSTART;VALUE=DATE:{d0:%Y%m%d}",
            f"DTEND;VALUE=DATE:{d1:%Y%m%d}",
            "RRULE:FREQ=YEARLY",
            "END:VEVENT",
        ]
    lineas.append("END:VCALENDAR")
    return "\r\n".join(lineas) + "\r\n"


def main() -> int:
    if "--ical" in sys.argv:
        destino = RAIZ / "ropa" / "lanzamientos.ics"
        destino.write_text(ical(), encoding="utf-8")
        print(f"\n  {destino.relative_to(RAIZ)}\n")
        return 0

    hoy = dt.date.today()
    ahora = vivo(hoy)

    if "--hoy" in sys.argv:
        es = next(d[1] for d in DROPS if d[0] == ahora)
        print(f"\n  {hoy:%d/%m/%Y} · {es} ({ahora})")
        print(f"    {anuncio(ahora, 'es')}\n")
        return 0

    malos = comprobar()
    print(f"\n  12 lanzamientos · {len(malos)} problemas · "
          f"hoy está vivo «{ahora}»\n")
    for signo, es, en, fr, nota in DROPS:
        ini, fin = temporadas()[signo]
        marca = "→" if signo == ahora else " "
        print(f"  {marca} {fecha(ini,'es'):>18} — {fecha(fin,'es'):<18} "
              f"{es}")
        print(f"      {en} · {fr}")
        print(f"      {nota}")
        print(f"      {dibujo(signo)[0]}")
        print(f"      {LAMINA}#vi-{signo}")
    print()
    for m in malos:
        print(f"    {m}")
    if not malos:
        print("    Las doce temporadas embaldosan el año sin huecos ni "
              "solapes.")
    print(f"\n    Falta, y no se puede inventar: la hoja del proveedor de\n"
          f"    estampación y qué lámina va en qué prenda. Lo exige\n"
          f"    tienda/ropa.py y aborta sin ello.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
