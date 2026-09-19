#!/usr/bin/env python3
"""
LOCALIZACIÓN — segmentador y catálogo de traducciones
=====================================================
El problema: los once planes son HTML escrito a mano, con la prosa mezclada
con el marcado. Traducir eso duplicando ficheros garantiza que a la tercera
corrección el francés diga una cosa y el español otra.

La solución de este módulo es la que usan las herramientas de localización
profesionales: el marcado vive UNA vez, y las traducciones son datos.

  1. `segmentar()` recorre el HTML y devuelve los segmentos traducibles. Un
     segmento es el contenido de un elemento que no tiene dentro ningún otro
     elemento de bloque, de modo que «...con macros de <b>atleta</b> y 28
     días...» viaja entero, con su negrita dentro, en vez de partirse en tres
     trozos intraducibles.
  2. Cada segmento se identifica por el hash de su texto en español. Dos
     cadenas iguales en dos planes distintos comparten traducción por
     construcción, y una corrección en el original invalida su traducción en
     vez de dejarla desincronizada en silencio.
  3. `traducir()` reescribe el HTML sustituyendo cada segmento por su versión
     en el idioma pedido, y devuelve además la cobertura, que es el dato que
     decide si un PDF se puede publicar o no.

Nada de esto adivina: si falta una traducción, se sabe, se cuenta y se
informa. Un producto a la venta no puede tener frases sueltas en otro idioma.
"""

import hashlib
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = RAIZ / "i18n" / "catalogo.json"

IDIOMAS = {
    "es": ("Español", "es-ES"),
    "en": ("English", "en-US"),
    "fr": ("Français", "fr-FR"),
}

# Elementos cuyo contenido NO se toca nunca. El SVG NO está aquí: su
# geometría es intocable, pero los rótulos de las ilustraciones son texto que
# el comprador lee, y dejarlos en español dentro de una edición inglesa fue
# exactamente el fallo que obligó a reescribir esta parte.
OPACOS = {"style", "script"}

# Elementos que llevan texto y que pueden contener marcado en línea. El
# contenido de uno de estos es un segmento SI no lleva dentro otro de la lista
# de bloques.
CONTENEDORES = {
    "p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "td", "th", "caption",
    "figcaption", "dt", "dd", "small", "strong", "em", "b", "i", "span",
    "div", "summary", "blockquote", "label", "legend",
    "text", "tspan", "title",          # rótulos de las láminas y título del PDF
}
BLOQUES = {
    "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "table",
    "thead", "tbody", "tr", "td", "th", "section", "header", "footer", "main",
    "div", "figure", "figcaption", "blockquote", "dl", "dt", "dd", "nav",
}

# Atributos con texto visible o indexable.
ATRIBUTOS = ("alt", "title", "aria-label", "data-etiqueta")

_ETIQUETA = re.compile(r"<(/?)([a-zA-Z][\w:-]*)((?:\s[^<>]*?)?)(/?)>", re.S)
_SOLO_MARCA = re.compile(r"^(?:\s|&[a-z]+;|&#\d+;|<[^>]+>|[·—–…|/\\+×°%$€£0-9.,:;()\[\]{}«»\"'@#*_-])*$")

# Un precio sí se traduce, aunque no lleve una sola letra. «9,99 $» en inglés
# se escribe «$9.99»: cambia el separador decimal y cambia de lado el símbolo.
# La regla de las dos letras dejaba fuera exactamente esto, y la escalera de
# precios salía en formato español dentro de la edición inglesa, tres líneas
# por debajo de la insignia que sí estaba traducida. La cobertura no lo veía
# porque el segmento nunca llegó a contarse.
_PRECIO = re.compile(r"(?:[$€£]\s*\d|\d+(?:[.,]\d{2})?\s*[$€£])")


def clave(texto: str) -> str:
    """Identificador estable de un segmento: hash de su forma normalizada."""
    norm = re.sub(r"\s+", " ", texto).strip()
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:16]


def traducible(contenido: str) -> bool:
    """¿Este contenido tiene algo que traducir?

    Descarta lo que es solo marcado, cifras, símbolos o entidades: un «10» o
    un «·» no se traduce, y meterlo en el catálogo solo añade ruido que luego
    baja la cobertura sin motivo.

    La excepción es el precio. No lleva letras y aun así cambia de una lengua a
    otra —«9,99 $» es «$9.99» en inglés—, así que entra aunque la regla de las
    dos letras lo rechace.
    """
    if not contenido.strip():
        return False
    plano = re.sub(r"<[^>]+>", "", contenido)
    if _PRECIO.search(plano):
        return True
    if _SOLO_MARCA.match(contenido):
        return False
    # tiene que quedar alguna letra tras quitar el marcado
    return bool(re.search(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑçÇàèùâêîôûëïœ]{2,}", plano))


def _tramos_opacos(html: str) -> list[tuple[int, int]]:
    """Rangos del documento que hay que dejar intactos."""
    fuera = []
    for tag in OPACOS:
        for m in re.finditer(rf"<{tag}\b.*?</{tag}\s*>", html, re.S | re.I):
            fuera.append((m.start(), m.end()))
    return fuera


def _dentro(pos: int, tramos: list[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in tramos)


def segmentar(html: str) -> list[tuple[int, int, str]]:
    """Devuelve (inicio, fin, contenido) de cada segmento traducible.

    Recorre las etiquetas llevando una pila. Cuando se cierra un contenedor,
    se mira su contenido: si no lleva dentro ninguna etiqueta de bloque, es un
    segmento; si la lleva, se descarta porque sus hijos ya se habrán recogido
    por su cuenta. Así «<div><p>a</p><p>b</p></div>» da dos segmentos y no
    tres solapados.
    """
    opacos = _tramos_opacos(html)
    pila, segmentos = [], []
    for m in _ETIQUETA.finditer(html):
        cierre, nombre, _attrs, auto = m.groups()
        nombre = nombre.lower()
        if _dentro(m.start(), opacos) or auto or nombre in ("br", "hr", "img",
                                                            "meta", "link",
                                                            "input"):
            continue
        if not cierre:
            pila.append((nombre, m.end()))
            continue
        # etiqueta de cierre: se desapila hasta encontrar su pareja
        while pila:
            abierto, fin_apertura = pila.pop()
            if abierto != nombre:
                continue
            if nombre in CONTENEDORES:
                contenido = html[fin_apertura:m.start()]
                hijos = {t.lower() for t in
                         re.findall(r"<([a-zA-Z][\w:-]*)", contenido)}
                if not (hijos & BLOQUES) and traducible(contenido):
                    segmentos.append((fin_apertura, m.start(), contenido))
            break
    # sin solapes y en orden
    segmentos.sort()
    limpios, ultimo = [], -1
    for a, b, c in segmentos:
        if a >= ultimo:
            limpios.append((a, b, c))
            ultimo = b
    return limpios


def atributos(html: str) -> list[tuple[int, int, str]]:
    """Los atributos con texto visible, para no dejarlos sin traducir."""
    opacos = _tramos_opacos(html)
    fuera = []
    for attr in ATRIBUTOS:
        for m in re.finditer(rf'{attr}="([^"]*)"', html):
            if _dentro(m.start(), opacos):
                continue
            if traducible(m.group(1)):
                fuera.append((m.start(1), m.end(1), m.group(1)))
    return sorted(fuera)


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
    """Reescribe el HTML al idioma pedido.

    Devuelve (html, traducidos, totales). La cobertura es lo que decide si el
    PDF se publica: por debajo del 100 % quedarían frases en español dentro de
    un producto vendido como inglés o francés, y eso no sale a la venta.
    """
    if idioma == "es":
        return html, 0, 0
    cat = cat if cat is not None else cargar()
    piezas = segmentar(html) + atributos(html)
    piezas.sort(reverse=True)          # de atrás hacia delante: no desplaza
    hechos = 0
    for ini, fin, original in piezas:
        entrada = cat.get(clave(original))
        destino = (entrada or {}).get(idioma)
        if destino:
            html = html[:ini] + destino + html[fin:]
            hechos += 1
    return html, hechos, len(piezas)


def inventario(documentos) -> dict:
    """Todos los segmentos de un conjunto de documentos YA ENSAMBLADOS.

    Se inventaría el documento ensamblado y no el fuente porque las
    ilustraciones se inyectan al ensamblar: sobre el fuente, los rótulos de las
    láminas no aparecen y la cobertura mentiría.
    """
    fuera = {}
    for doc in documentos:
        html = doc if (isinstance(doc, str) and "<" in doc) \
            else Path(doc).read_text(encoding="utf-8")
        for _, _, texto in segmentar(html) + atributos(html):
            fuera.setdefault(clave(texto), texto)
    return fuera


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(RAIZ))
    from build import assemble
    ficheros = sorted((RAIZ / "src").glob("*.html"))
    inv = inventario([assemble(f.read_text(encoding="utf-8")) for f in ficheros])
    palabras = sum(len(re.sub(r"<[^>]+>", " ", t).split()) for t in inv.values())
    cat = cargar()
    print(f"  {len(ficheros)} planes · {len(inv)} segmentos únicos · "
          f"{palabras:,} palabras")
    for cod, (nombre, _) in IDIOMAS.items():
        if cod == "es":
            continue
        hechos = sum(1 for k in inv if cat.get(k, {}).get(cod))
        print(f"    {nombre:<10} {hechos:>4}/{len(inv)}  "
              f"{100*hechos/max(len(inv),1):5.1f} %")
