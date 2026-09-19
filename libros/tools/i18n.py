#!/usr/bin/env python3
"""
LOCALIZACIÓN DE LOS LIBROS
==========================
Los ocho códices se componen desde JSON, no desde HTML escrito a mano, pero el
problema de traducirlos es el mismo que el de los planes y por eso la solución
es la misma: el marcado vive una vez y las traducciones son datos, indexadas
por el hash del original en español.

Este módulo NO reimplementa el segmentador. Lo importa del de los planes, y lo
hace a propósito: dos segmentadores parecidos pero no idénticos producirían
hashes distintos para el mismo párrafo, y esa clase de fallo no da la cara
hasta que media traducción aparece sin aplicar en un PDF ya publicado.

Lo único propio de los libros es DÓNDE vive el catálogo, así que aquí solo se
redefinen `cargar`, `guardar`, `traducir` e `inventario`, que son envoltorios
de cuatro líneas sobre las piezas importadas.
"""

import importlib.util
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = RAIZ / "i18n" / "catalogo.json"

_RUTA_NUCLEO = RAIZ.parent / "planes" / "tools" / "i18n.py"
if not _RUTA_NUCLEO.exists():                       # pragma: no cover
    raise SystemExit(
        f"Falta el segmentador compartido en {_RUTA_NUCLEO}. Los libros y los "
        "planes usan el mismo a propósito: no lo dupliques, muévelo.")
_spec = importlib.util.spec_from_file_location("i18n_nucleo", _RUTA_NUCLEO)
_nucleo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nucleo)

# Piezas compartidas, tal cual.
IDIOMAS = _nucleo.IDIOMAS
clave = _nucleo.clave
segmentar = _nucleo.segmentar
atributos = _nucleo.atributos
traducible = _nucleo.traducible


def cargar() -> dict:
    if CATALOGO.exists():
        return json.loads(CATALOGO.read_text(encoding="utf-8"))
    return {}


def guardar(cat: dict) -> None:
    CATALOGO.parent.mkdir(parents=True, exist_ok=True)
    CATALOGO.write_text(
        json.dumps(cat, ensure_ascii=False, indent=1, sort_keys=True),
        encoding="utf-8")


def traducir(html: str, idioma: str, cat: dict | None = None):
    """Reescribe el HTML al idioma pedido. Devuelve (html, hechos, totales)."""
    if idioma == "es":
        return html, 0, 0
    cat = cat if cat is not None else cargar()
    piezas = sorted(segmentar(html) + atributos(html), reverse=True)
    hechos = 0
    for ini, fin, original in piezas:
        destino = (cat.get(clave(original)) or {}).get(idioma)
        if destino:
            html = html[:ini] + destino + html[fin:]
            hechos += 1
    return html, hechos, len(piezas)


def cadena(texto: str, idioma: str, cat: dict) -> str:
    """Traduce una cadena suelta (título del libro, título de capítulo).

    El titulillo de página, los marcadores y la búsqueda del folio de cada
    capítulo trabajan con texto plano, no con HTML. Se resuelven contra el
    MISMO catálogo para que no puedan decir una cosa mientras la página dice
    otra. Si falta, se devuelve el español: la puerta de cobertura del
    generador ya habrá impedido publicar ese idioma.
    """
    if idioma == "es":
        return texto
    return (cat.get(clave(texto)) or {}).get(idioma, texto)


def inventario(documentos) -> dict:
    """Todos los segmentos de un conjunto de documentos ya compuestos."""
    fuera = {}
    for doc in documentos:
        html = doc if (isinstance(doc, str) and "<" in doc) \
            else Path(doc).read_text(encoding="utf-8")
        for _, _, texto in segmentar(html) + atributos(html):
            fuera.setdefault(clave(texto), texto)
    return fuera


def claves_de_lamina() -> dict:
    """Los segmentos que viven DENTRO de una lámina, con su ancho original.

    Un rótulo de lámina no es prosa: ocupa un hueco de ancho fijo dentro de un
    SVG, y a diferencia del HTML no hay nada que lo reajuste. Si la traducción
    es bastante más larga que el original, el texto se sale del recuadro y el
    fallo no se ve hasta tener el PDF delante.

    Con esta lista, el cargador puede comprobar la longitud de cada traducción
    de rótulo y negarse a aceptarla. Es la misma disciplina que el resto: si se
    puede comprobar, se comprueba.
    """
    fuera = {}
    for ruta in sorted((RAIZ / "partials").glob("*.svg")):
        html = ruta.read_text(encoding="utf-8")
        for _, _, texto in segmentar(html):
            fuera.setdefault(clave(texto), texto)
    return fuera


def _documentos_es():
    """Los ocho libros compuestos en español.

    Devuelve los DOS documentos de cada libro por separado —cubierta e
    interior— y no concatenados, porque el generador también los traduce por
    separado. Segmentar una concatenación empareja mal las etiquetas del final
    de uno con las del principio del otro y produce un inventario que no
    corresponde a lo que se va a componer.
    """
    import sys
    sys.path.insert(0, str(RAIZ))
    from build import cubierta, documento          # noqa: E402

    for ruta in sorted((RAIZ / "src").glob("*.json")):
        libro = json.loads(ruta.read_text(encoding="utf-8"))
        yield ruta.stem, [cubierta(libro), documento(libro, None)]


if __name__ == "__main__":
    cat = cargar()
    total = {}
    print("  Segmentos por libro")
    for nombre, docs in _documentos_es():
        inv = inventario(docs)
        total.update(inv)
        hechos = {c: sum(1 for k in inv if cat.get(k, {}).get(c))
                  for c in IDIOMAS if c != "es"}
        marcas = "  ".join(f"{c} {n:>4}/{len(inv):<4}" for c, n in hechos.items())
        print(f"    {nombre:<24} {len(inv):>4} segmentos    {marcas}")
    palabras = sum(len(re.sub(r"<[^>]+>", " ", t).split()) for t in total.values())
    print(f"\n  {len(total)} segmentos únicos · {palabras:,} palabras")
