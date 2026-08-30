#!/usr/bin/env python3
"""
VILLUMINATIONS — Qué ve el buscador, y qué no
==============================================
Cuenta la superficie indexable de la tienda y dice qué le falta a cada trozo
para poder salir en un resultado.

    python3 tienda/visibilidad.py

Los otros comprobadores miden el texto de una superficie. Este mide **cuántas
URL hay**, en cuántas lenguas, cuáles llevan datos estructurados y cuáles
están vacías o duplicadas. Es la diferencia entre «la ficha está bien escrita»
y «la ficha existe en el mapa del sitio y no compite consigo misma».

El sitemap no se escribe aquí
-----------------------------
Shopify genera `/sitemap.xml` solo, con un índice por tipo de recurso, y no
hay API para tocarlo: entra lo que esté **publicado en el canal Tienda
online**, y nada más. Así que lo útil no es escribir un sitemap sino saber
qué entrará en el suyo, y eso es lo que se cuenta abajo.

Lo que este fichero no puede saber
----------------------------------
Sin hablar con la tienda no se ve qué está publicado en el canal, ni qué
locales están activos, ni si un producto está en borrador. Cuando algo
dependa de eso, se dice; no se supone.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Locales publicados en la tienda. El castellano es el primario y va sin
# prefijo; los demás cuelgan de /xx/.
PRIMARIO = "es"
PUBLICADOS = ("es", "en", "fr", "de", "ja")

# Locales con traducción escrita de verdad. Los que están publicados y no
# están aquí sirven castellano bajo una URL que dice otra cosa.
TRADUCIDOS = ("es", "en", "fr")


def superficie() -> dict:
    """Cuántas URL de cada tipo, y en cuántas lenguas tienen texto propio."""
    import articulos
    import articulos_en_fr
    import catalogo
    import seo

    traducidos_diario = {
        lengua
        for lenguas in articulos_en_fr.CUERPOS.values()
        for lengua in lenguas
    }

    return {
        "producto de proveedor": {
            "urls": len(catalogo.FICHAS),
            "lenguas": {"es"} | {
                l for v in catalogo.METAS.values() for l in v},
        },
        "producto propio": {
            "urls": len(seo.META),
            "lenguas": {l for v in seo.META.values() for l in v},
        },
        "colección": {
            "urls": len(catalogo.COLECCIONES),
            "lenguas": {"es"},          # las traducciones viven solo en la API
        },
        "artículo del Diario": {
            "urls": len(articulos.ARTICULOS),
            "lenguas": {"es"} | traducidos_diario,
        },
        "blog": {"urls": 1, "lenguas": {"es"}},
    }


def datos_estructurados() -> list:
    """Qué tiene JSON-LD escrito y qué no.

    Un resultado enriquecido —el desplegable de preguntas, la estrella de
    valoración, la miga de pan— solo aparece si la página lleva el marcado.
    El tema pone el de producto; lo demás hay que ponerlo.
    """
    salida = []
    try:
        import faq
        salida.append(("FAQPage", "página de preguntas", True,
                       "pegado en el cuerpo por faq.cuerpo(), en las tres "
                       "lenguas; falta volver a publicar la página"))
    except Exception:                                        # pragma: no cover
        salida.append(("FAQPage", "página de preguntas", False, "no hay"))

    salida.append(("Article", "los 9 artículos del Diario", None,
                   "casi todos los temas lo emiten ya en la plantilla de "
                   "artículo. Añadir un segundo daría dos Article en la "
                   "misma página, que es un aviso de validación: hay que "
                   "mirar el tema antes de tocarlo"))
    salida.append(("Product", "los 40 productos", None,
                   "lo emite el tema; no consta aquí y hay que mirarlo en "
                   "el panel"))
    salida.append(("BreadcrumbList", "todas las páginas", None,
                   "lo emite el tema; ídem"))
    salida.append(("Organization", "la tienda", None,
                   "lo emite el tema, y con el nombre mal: la cuenta sigue "
                   "llamándose «VIllumination»"))
    return salida


def problemas() -> list:
    """Lo que resta visibilidad, no lo que falta por hacer."""
    fuera = []

    huecos = [l for l in PUBLICADOS if l not in TRADUCIDOS]
    if huecos:
        fuera.append(
            f"{len(huecos)} locales publicados sin una sola traducción "
            f"({', '.join(huecos)}). Shopify emite hreflang apuntando a "
            f"/{huecos[0]}/… y sirve castellano: para el buscador son copias "
            f"del mismo contenido bajo URL distintas. O se traducen o se "
            f"despublican; dejarlos así reparte la fuerza entre cinco "
            f"direcciones que dicen lo mismo.")

    fuera.append(
        "El blog «suplementos» está vacío y es indexable. Cero artículos, "
        "ninguna entrada de menú, y aun así /blogs/suplementos existe. Una "
        "página sin contenido en el mapa del sitio no suma: resta.")

    fuera.append(
        "Los dos jabones están sin publicar (UNLISTED). No entran en el "
        "mapa del sitio y su colección se queda vacía, que es la razón por "
        "la que menus.py no la enlaza.")

    fuera.append(
        "Once productos cobran y no entregan archivo. Eso no es SEO, pero "
        "una devolución pesa más que cualquier posición ganada.")

    return fuera


def crm() -> list:
    """El otro lado: qué pasa con quien ya ha llegado."""
    import correos
    n = len(correos.SECUENCIAS) if hasattr(correos, "SECUENCIAS") else 0
    return [
        (f"{n or 5} secuencias de correo escritas en tres lenguas", True,
         "correos.py, con las mismas prohibiciones que las fichas"),
        ("Ninguna está montada todavía en la tienda", False,
         "las automatizaciones se crean en Marketing → Automatizaciones y "
         "el texto se pega allí; no hay API"),
        ("Formulario de captura escrito, con consentimiento CASL", True,
         "captura.py: texto en tres lenguas y el bloque Liquid listo. Falta "
         "pegarlo en el tema, que es donde vive"),
        ("Cada secuencia sabe ya con qué plantilla se monta", True,
         "correos.AUTOMATIZACION: plantilla, disparador, espera y si se "
         "puede activar hoy"),
        ("Sin píxel de Meta ni etiqueta de Google", False,
         "sin ellos no se puede medir qué anuncio vende, y correr anuncios "
         "sin medir es pagar por no enterarse"),
        ("Sin recuperación de carrito activa", False,
         "el texto de las dos de carrito está escrito y esperando"),
    ]


def main() -> int:
    s = superficie()
    total = sum(v["urls"] for v in s.values())
    print(f"\n  SUPERFICIE INDEXABLE · {total} URL en castellano\n")
    for nombre, datos in s.items():
        lenguas = ", ".join(sorted(datos["lenguas"]))
        print(f"    {datos['urls']:3} {nombre:24} {lenguas}")

    completos = sum(v["urls"] for v in s.values()
                    if {"es", "en", "fr"} <= v["lenguas"])
    print(f"\n    {completos} de {total} existen en las tres lenguas "
          f"con texto propio")

    print(f"\n  DATOS ESTRUCTURADOS\n")
    for tipo, donde, hay, nota in datos_estructurados():
        marca = {True: "sí ", False: "NO ", None: "¿? "}[hay]
        print(f"    {marca} {tipo:16} {donde}")
        print(f"        {nota}")

    print(f"\n  LO QUE RESTA VISIBILIDAD\n")
    for p in problemas():
        print(f"    · {p}")

    print(f"\n  CRM\n")
    for que, hay, nota in crm():
        print(f"    {'sí ' if hay else 'NO '} {que}")
        print(f"        {nota}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
