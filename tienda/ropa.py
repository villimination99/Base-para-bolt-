#!/usr/bin/env python3
"""
VILLUMINATIONS — Ropa estampada bajo demanda
---------------------------------------------
El molde para las prendas que se estampen con dibujos propios, antes de que
exista la primera. Se escribe ahora, y no después, por lo que costó la vez
anterior: los 29 productos de proveedor entraron sin estructura y hubo que
reescribirlos enteros, traducirlos a dos lenguas y volver a registrarlos.

    python3 tienda/ropa.py              # inventario de láminas y comprobación
    python3 tienda/ropa.py --laminas    # las 95 láminas propias, una por una

**La ventaja que ya tenéis y no se está usando.** Un negocio de estampación
bajo demanda se atasca siempre en lo mismo: de dónde salen los dibujos. Cogerlos
de internet es infracción, encargarlos cuesta, y generarlos deja la propiedad en
duda. Aquí no hace falta nada de eso: los libros se ilustraron con **láminas
dibujadas para la edición**, en SVG, vectoriales y de propiedad entera. Están en
`libros/partials/` y `planes/partials/`, y una lámina vectorial es exactamente
lo que pide una estampadora: escala a cualquier tamaño sin perder filo.

Tres reglas que este fichero hace cumplir, y las tres vienen de un fallo real:

· **El dibujo tiene que ser propio.** `comprobar()` exige que cada diseño
  señale su lámina de origen dentro del repositorio. Un diseño sin lámina no
  pasa. Ni se busca en internet ni se encarga fuera.

· **La ficha se escribe en tres lenguas desde el primer día.** Traducir 29
  fichas a posteriori costó varias sesiones. Una prenda nueva no se publica
  coja.

· **No se promete lo que la prenda blanca no da.** El proveedor de estampación
  vende un tejido con unas propiedades; el estampado no añade ninguna. Si la
  camiseta no está certificada para nada, la ficha no lo insinúa.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TOPE_TITULO, TOPE_DESCRIPCION, TOPE_ALT = 60, 155, 125

# Las carpetas de dibujo propio. Todo lo que se estampe sale de aquí.
LAMINAS = (RAIZ / "libros" / "partials", RAIZ / "planes" / "partials",
           RAIZ / "ropa" / "partials")

# Prefijo de identificador -> de qué serie viene. Sirve para agrupar la oferta.
# El orden importa: «dia-» va antes que «de-» porque los diagramas del zodiaco
# empiezan por «dia-» y caerían en Descanso si se mirara al revés.
SERIES = {
    "dia-": "Zodiaco · diagramas", "z-": "Zodiaco",
    "ar-": "Arcanos", "am-": "Alta magia",
    "ca-": "Carga", "de-": "Descanso", "me-": "Mesa",
    "sm-": "Sí mismo", "vo-": "Voluntad", "si-": "Símbolos",
    "em-": "Emblemas", "fig-": "Figuras", "r-": "Rosetas",
    "vi-": "Marca VI",
    "filigrana": "Ornamentos",
}

# ---------------------------------------------------------------------------
# La prenda blanca. Se rellena con la hoja de especificaciones del proveedor de
# estampación, no de memoria: son las cifras que acaban impresas en la ficha.
# ---------------------------------------------------------------------------
PRENDAS = {
    # "camiseta-algodon": {
    #     "nombre": ("Camiseta de algodón", "Cotton T-shirt", "T-shirt en coton"),
    #     "composicion": ("100 % algodón peinado", ...),
    #     "gramaje": "180 g/m²",
    #     "tallas": ["S", "M", "L", "XL", "2XL"],
    #     "colores": ["Negro", "Blanco", "Gris jaspeado"],
    #     "estampado": "serigrafía digital directa sobre prenda",
    #     "origen": "…",
    # },
}

# ---------------------------------------------------------------------------
# Los diseños. Cada uno señala la lámina propia de la que sale.
# ---------------------------------------------------------------------------
# Lo que se puede decir ya está escrito; lo que depende de la prenda, no.
# `prenda` apunta a una clave que NO existe en PRENDAS a propósito: mientras
# falte la hoja del proveedor, `comprobar()` sigue fallando y estos diseños no
# se publican. No es un descuido, es el freno.
#
# El texto NO habla del tejido —ni transpirable, ni de secado rápido, ni
# nada—: eso sale de la hoja y no de la imaginación. Habla del dibujo, que es
# lo que sí es nuestro y lo que de verdad se compra.
def _exportador():
    """El módulo que sabe a qué tamaño y en qué sitio se imprime cada pieza."""
    import importlib.util
    ruta = (Path(__file__).resolve().parent.parent / "ropa" / "tools"
            / "exportar-pod.py")
    spec = importlib.util.spec_from_file_location("pod", ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def colocacion(sid: str) -> str:
    """La colocación, dicha por el fichero de impresión y no por la memoria.

    Estaba escrita a mano —«a 8 cm del cuello», «9 cm de ancho»— al lado de
    un exportador que tenía sus propios números, y en cuanto los suyos
    cambiaron esta frase pasó a describir una prenda que ya no se fabrica.
    Una ficha que miente sobre dónde va el estampado es una devolución.
    """
    m = _exportador()
    area, ancho, x_frac, y_cm, _pr = m.COLOCACION[sid]
    aw, ah, an = m.AREAS[area]
    donde = "centrado" if abs(x_frac - 0.5) < 1e-6 else f"a {x_frac:.0%} del ancho"
    return (f"{an.split(' · ')[0].lower()}, {donde}, {ancho} cm de ancho, "
            f"a {y_cm} cm del borde superior del área de estampación")


DISENOS = {
    "espina-dorsal": {
        "lamina": "ropa/partials/espinas.svg#es-dorsal",
        "titulo": ("Espina · pieza de espalda",
                   "Thorn · back piece",
                   "Épine · pièce de dos"),
        "concepto": (
            "Filigrana de espalda dibujada entera para esta serie. La V y la "
            "I de VILLUMINATIONS no van estampadas encima: son el esqueleto "
            "del que cuelga todo lo demás, así que a tres metros se lee la "
            "marca y de cerca se lee el dibujo. Dentro va el arco de los "
            "treinta y seis decanatos, que se puede contar con el dedo.",
            "A back filigree drawn from scratch for this series. The V and "
            "the I of VILLUMINATIONS are not printed on top of it: they are "
            "the armature everything else hangs from, so from three metres "
            "you read the mark and up close you read the drawing. Inside sits "
            "the arc of the thirty-six decans, and you can count them.",
            "Une filigrane de dos dessinée entièrement pour cette série. Le V "
            "et le I de VILLUMINATIONS ne sont pas imprimés par-dessus : ils "
            "sont l'ossature à laquelle tout le reste est suspendu, de sorte "
            "qu'à trois mètres on lit la marque et de près le dessin. À "
            "l'intérieur, l'arc des trente-six décans, que l'on peut compter."),
        "prenda": "PENDIENTE-hoja-del-proveedor",
        "pieza": "es-dorsal",
    },
    "espina-pecho": {
        "lamina": "ropa/partials/espinas.svg#es-pecho",
        "titulo": ("Espina · pecho",
                   "Thorn · chest",
                   "Épine · poitrine"),
        "concepto": (
            "La misma gramática en nueve centímetros. A este tamaño no cabe "
            "la filigrana entera, así que manda la V y el plumaje se reduce a "
            "lo que aguanta la escala. Es la pieza de diario: se ve a un "
            "metro y no grita.",
            "The same grammar in nine centimetres. At this size the full "
            "filigree does not fit, so the V leads and the feathering is cut "
            "back to what the scale can hold. It is the everyday piece: it "
            "reads at one metre and it does not shout.",
            "La même grammaire en neuf centimètres. À cette taille la "
            "filigrane entière ne tient pas : le V commande et le plumage se "
            "réduit à ce que l'échelle supporte. C'est la pièce de tous les "
            "jours : elle se lit à un mètre et ne crie pas."),
        "prenda": "PENDIENTE-hoja-del-proveedor",
        "pieza": "es-pecho",
    },
}

TIPO = "Ropa deportiva"          # ya traducido: Sportswear · Vêtements de sport
COLECCION = "ropa"
VENDEDOR = "VILLUMINATIONS"

CUIDADO = {
    "es": ("<strong>Cuidados:</strong> del revés, a máquina en frío y con "
           "colores parecidos. Secar al aire. No planchar sobre el estampado."),
    "en": ("<strong>Care:</strong> inside out, machine wash cold with similar "
           "colours. Air dry. Do not iron over the print."),
    "fr": ("<strong>Entretien :</strong> à l'envers, en machine à froid avec "
           "des couleurs proches. Séchage à l'air. Ne pas repasser sur "
           "l'impression."),
}

ORIGEN = {
    "es": ("<strong>El dibujo es nuestro.</strong> Esta lámina se dibujó para "
           "la edición de nuestros libros, en vectorial. No es una imagen de "
           "banco ni un encargo de fuera."),
    "en": ("<strong>The drawing is ours.</strong> This plate was drawn in "
           "vector form for the edition of our books. It is not a stock image "
           "or outside commission."),
    "fr": ("<strong>Le dessin est le nôtre.</strong> Cette planche a été "
           "dessinée en vectoriel pour l'édition de nos livres. Ce n'est ni "
           "une image de banque ni une commande extérieure."),
}


# ---------------------------------------------------------------------------
def inventario() -> dict:
    """Las láminas propias disponibles: fichero -> [identificadores]."""
    salida = {}
    for carpeta in LAMINAS:
        if not carpeta.is_dir():
            continue
        for svg in sorted(carpeta.glob("*.svg")):
            simbolos = re.findall(r'<symbol[^>]*\bid="([^"]+)"',
                                  svg.read_text(encoding="utf-8"))
            if simbolos:
                salida[str(svg.relative_to(RAIZ))] = simbolos
    return salida


def serie(identificador: str) -> str:
    for prefijo, nombre in SERIES.items():
        if identificador.startswith(prefijo):
            return nombre
    return "sin serie"


def comprobar() -> list:
    """Lo que impide publicar una prenda. Vacío es lo correcto."""
    malos = []
    disponibles = {f"{f}#{s}"
                   for f, simbolos in inventario().items() for s in simbolos}

    for mango, d in DISENOS.items():
        if d.get("lamina") not in disponibles:
            malos.append(f"{mango} · la lámina «{d.get('lamina')}» no está en "
                         f"el repositorio: un diseño sin dibujo propio no se "
                         f"publica")
        if d.get("pieza") not in _exportador().COLOCACION:
            malos.append(f"{mango} · la pieza «{d.get('pieza')}» no la exporta "
                         f"ropa/tools/exportar-pod.py: sin eso la ficha no "
                         f"puede decir a qué tamaño va el estampado")
        if d.get("prenda") not in PRENDAS:
            malos.append(f"{mango} · la prenda «{d.get('prenda')}» no está "
                         f"especificada")
        for campo in ("titulo", "concepto"):
            valores = d.get(campo)
            if not valores or len(valores) != 3 or not all(valores):
                malos.append(f"{mango} · «{campo}» tiene que venir en las "
                             f"tres lenguas")

    for mango, p in PRENDAS.items():
        for campo in ("nombre", "composicion", "gramaje", "tallas",
                      "colores", "estampado"):
            if not p.get(campo):
                malos.append(f"prenda {mango} · falta «{campo}», que sale de "
                             f"la hoja del proveedor y no de la memoria")
    return malos


def resumen() -> str:
    inv = inventario()
    total = sum(len(v) for v in inv.values())
    por_serie = {}
    for simbolos in inv.values():
        for s in simbolos:
            por_serie[serie(s)] = por_serie.get(serie(s), 0) + 1
    lineas = [f"  {total} láminas propias en {len(inv)} ficheros\n"]
    for nombre, n in sorted(por_serie.items(), key=lambda kv: -kv[1]):
        lineas.append(f"    {nombre:14} {n:3}")
    return "\n".join(lineas)


if __name__ == "__main__":
    malos = comprobar()
    print()
    print(resumen())
    print(f"\n  {len(PRENDAS)} prendas blancas · {len(DISENOS)} diseños · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")

    if "--laminas" in sys.argv:
        for fichero, simbolos in inventario().items():
            print(f"\n  {fichero}")
            for s in simbolos:
                print(f"    {fichero}#{s}")
    elif not DISENOS:
        print("    Todavía no hay ningún diseño. Para dar de alta el primero\n"
              "    hacen falta dos cosas, y ninguna se puede inventar:\n"
              "      · la hoja de especificaciones de la prenda blanca del\n"
              "        proveedor de estampación (composición, gramaje, tallas,\n"
              "        colores y método de estampado)\n"
              "      · qué lámina va en qué prenda y en qué tamaño\n"
              "    `--laminas` enseña de cuáles se puede elegir.\n")
