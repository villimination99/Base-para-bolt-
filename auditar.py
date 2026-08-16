#!/usr/bin/env python3
"""
VILLUMINATIONS — Auditoría cruzada del texto de la tienda
==========================================================
Cada módulo se comprueba a sí mismo: `catalogo.py` mide sus 29 fichas,
`articulos.py` sus artículos, `seo.py` los once propios. Ninguno puede ver lo
que solo aparece al mirarlos juntos.

    python3 auditar.py

Esto busca eso: los defectos que no están dentro de un fichero sino entre
varios.

· **Metaetiquetas repetidas.** Dos páginas con la misma descripción compiten
  entre ellas por el mismo hueco del buscador, y Google se queda con una. Es el
  fallo de SEO más común en una tienda que ha crecido a trozos, y ningún
  comprobador de un solo fichero lo puede ver.

· **Descripciones cortas.** El buscador da unos 155 caracteres; una de 60
  desperdicia la mitad del anuncio gratuito que te está regalando.

· **Artículos huérfanos.** Un artículo al que no apunta ningún producto ni
  ninguna colección solo recibe visitas del buscador. Enlazado desde una ficha,
  además convierte.

· **Colecciones sin salida.** Una colección que no manda a ningún artículo
  desaprovecha lo único que la distingue de la de la competencia.

· **Handles repetidos** entre superficies distintas, que en Shopify se pisan.

· **El precio escrito dentro de los documentos.** Las once láminas de planes
  llevan la escalera de los tres niveles impresa. Ese precio no lo sirve
  Shopify: está dibujado en 66 PDF, en tres lenguas y dos ediciones. Si alguien
  cambia el precio en la tienda, los documentos ya vendidos siguen diciendo el
  viejo. Aquí no se puede comprobar contra la tienda —eso pide credenciales—,
  pero sí que las once láminas digan todas lo mismo, y se imprime la tabla para
  poder cotejarla de un vistazo.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "tienda"))

MINIMO_DESCRIPCION = 110      # por debajo de esto se desperdicia el fragmento
TOPE_DESCRIPCION = 155


def recoger() -> tuple:
    """Todas las superficies con texto de buscador.

    Devuelve (metas, cuerpos). `metas` es [(superficie, clave, lengua, título,
    descripción)]: la lengua importa porque un duplicado solo lo es dentro de
    la misma. Que el título castellano y el inglés se parezcan no es un fallo;
    que dos productos compartan descripción castellana, sí.

    Los cuerpos de las colecciones no están en el repositorio —se escribieron
    directamente contra la API—, así que sus enlaces de salida no se pueden
    auditar desde aquí. Se dice, no se finge.
    """
    metas, cuerpos = [], {}

    import catalogo
    for handle, (titulo, descripcion, _alt, _fam, _etq) in catalogo.FICHAS.items():
        metas.append(("producto", handle, "es", titulo, descripcion))
    for handle, lenguas in getattr(catalogo, "METAS", {}).items():
        for lengua, (titulo, descripcion) in lenguas.items():
            metas.append(("producto", handle, lengua, titulo, descripcion))
    for handle, cuerpo in catalogo.CUERPOS.items():
        cuerpos[f"producto:{handle}"] = cuerpo
    for handle, datos in catalogo.COLECCIONES.items():
        metas.append(("colección", handle, "es", datos[0], datos[1]))

    import seo
    for handle, lenguas in seo.META.items():
        for lengua, (titulo, descripcion) in lenguas.items():
            metas.append(("producto propio", handle, lengua, titulo, descripcion))

    import descripciones
    import fichas_libros
    for f in list(descripciones.FICHAS) + list(fichas_libros.NUEVOS):
        cuerpos[f"producto propio:{f['handle']}"] = f["es"]

    import articulos
    for a in articulos.ARTICULOS:
        titulo, descripcion = a["meta"]
        metas.append(("artículo", a["handle"], "es", titulo, descripcion))
        cuerpos[f"artículo:{a['handle']}"] = a["cuerpo"]
    metas.append(("blog", articulos.BLOG["handle"], "es",
                  articulos.BLOG["meta_titulo"],
                  articulos.BLOG["meta_descripcion"]))

    try:
        import faq
        for lengua in faq.LENGUAS:
            titulo, descripcion = faq.META[lengua]
            metas.append(("página", faq.MANGO, lengua, titulo, descripcion))
            cuerpos[f"página:{faq.MANGO}"] = faq.cuerpo("es")
    except Exception as e:                                   # pragma: no cover
        print(f"    (faq.py no se pudo leer: {e})")

    return metas, cuerpos


def enlaces(html: str) -> set:
    """Los destinos internos a los que apunta un cuerpo."""
    return set(re.findall(r'href="(/[^"#?]+)', html or ""))


def auditar() -> dict:
    metas, cuerpos = recoger()
    hallazgos = defaultdict(list)

    # --- metaetiquetas repetidas, dentro de cada lengua
    por_titulo, por_descripcion = defaultdict(list), defaultdict(list)
    for superficie, clave, lengua, titulo, descripcion in metas:
        por_titulo[(lengua, titulo.strip().lower())].append(
            f"{superficie} {clave}")
        por_descripcion[(lengua, descripcion.strip().lower())].append(
            f"{superficie} {clave}")
    for (lengua, texto), quienes in sorted(por_titulo.items()):
        if len(quienes) > 1:
            hallazgos["títulos repetidos"].append(
                f"[{lengua}] «{texto[:46]}…» × {len(quienes)}: "
                f"{', '.join(q[:40] for q in quienes[:3])}")
    for (lengua, texto), quienes in sorted(por_descripcion.items()):
        if len(quienes) > 1:
            hallazgos["descripciones repetidas"].append(
                f"[{lengua}] «{texto[:46]}…» × {len(quienes)}: "
                f"{', '.join(q[:40] for q in quienes[:3])}")

    # --- descripciones que desperdician el fragmento
    for superficie, clave, lengua, _t, descripcion in metas:
        n = len(descripcion)
        if n < MINIMO_DESCRIPCION:
            hallazgos["descripciones cortas"].append(
                f"[{lengua}] {superficie} {clave[:42]} · "
                f"{n}/{TOPE_DESCRIPCION}")

    # --- handles repetidos entre superficies
    por_handle = defaultdict(list)
    for superficie, clave, *_r in metas:
        por_handle[clave].append(superficie)
    for handle, superficies in por_handle.items():
        if len(set(superficies)) > 1:
            hallazgos["handles compartidos"].append(
                f"{handle[:50]} · {', '.join(sorted(set(superficies)))}")

    # --- enlaces internos
    articulos_ = {c.split(":", 1)[1] for c in cuerpos if c.startswith("artículo:")}
    apuntados = set()
    salidas = defaultdict(set)
    for clave, html in cuerpos.items():
        for destino in enlaces(html):
            salidas[clave].add(destino)
            m = re.match(r"/blogs/[^/]+/([^/]+)", destino)
            if m:
                apuntados.add(m.group(1))

    for handle in sorted(articulos_ - apuntados):
        hallazgos["artículos huérfanos"].append(
            f"{handle} · no lo enlaza ninguna ficha ni colección")

    for linea in precios_incoherentes():
        hallazgos["precios de las láminas"].append(linea)

    return hallazgos


# La insignia de nivel y la escalera de upsell, dentro de cada lámina.
_INSIGNIA = re.compile(
    r'class="tier-badge">.*?</span>\s*Plan\s+(\w+)\s*·\s*([^<]+)<', re.S)
_ESCALON = re.compile(
    r'<div class="n">([^<]+)</div>\s*<div class="pz">([^<]+)</div>')


def precios_declarados() -> dict:
    """nivel -> {precio: [láminas que lo dicen]}, leyendo las once fuentes."""
    tabla = defaultdict(lambda: defaultdict(list))
    for src in sorted((RAIZ / "planes" / "src").glob("*.html")):
        html = src.read_text(encoding="utf-8")
        for nivel, precio in _INSIGNIA.findall(html):
            tabla[nivel.upper()][precio.strip()].append(f"{src.stem} · insignia")
        for nivel, precio in _ESCALON.findall(html):
            tabla[nivel.upper()][precio.strip()].append(f"{src.stem} · escalera")
    return tabla


_PERIODO = re.compile(r"\s*/\s*\w+\s*$")
_MONEDA = re.compile(r"\s*\b(CAD|CA|USD)\b")


def precios_incoherentes() -> list:
    """Tres cosas: que la cifra sea la misma, que todas digan si es al mes, y
    que la moneda se declare en alguna parte.

    Comparar las cadenas tal cual no vale: «9,99 $ CAD/mes» y «9,99 $/mes» son
    el mismo precio, uno con la moneda dicha y otro sin ella. Se compara la
    cifra desnuda y se miran aparte el periodo y la moneda.
    """
    fuera = []
    for nivel, precios in sorted(precios_declarados().items()):
        desnuda = {_MONEDA.sub("", _PERIODO.sub("", p)).strip() for p in precios}
        if len(desnuda) > 1:
            fuera.append(f"{nivel} · dice {len(desnuda)} cifras distintas: "
                         f"{', '.join(sorted(desnuda))}")
            continue
        sin_periodo = sorted(p for p in precios if not _PERIODO.search(p))
        if sin_periodo:
            fuera.append(f"{nivel} · no dice si es al mes en "
                         f"{', '.join(sin_periodo)}")
        if not any(_MONEDA.search(p) for p in precios):
            fuera.append(f"{nivel} · el símbolo va suelto y no se dice la "
                         f"moneda en ninguna parte")
    return fuera


if __name__ == "__main__":
    hallazgos = auditar()
    total = sum(len(v) for v in hallazgos.values())
    print(f"\n  Auditoría cruzada · {total} hallazgos\n")
    if not total:
        print("    Nada que corregir entre superficies.\n")
    for titulo in sorted(hallazgos):
        print(f"  {titulo.upper()}  ({len(hallazgos[titulo])})")
        for linea in hallazgos[titulo][:12]:
            print(f"    {linea}")
        if len(hallazgos[titulo]) > 12:
            print(f"    … y {len(hallazgos[titulo]) - 12} más")
        print()

    print("  PRECIO ESCRITO EN LAS LÁMINAS  (a cotejar con la tienda a mano)")
    for nivel, precios in sorted(precios_declarados().items()):
        for precio, donde in sorted(precios.items()):
            n = len(donde)
            print(f"    {nivel:8} {precio:14} en {n} "
                  f"{'sitio' if n == 1 else 'sitios'}")
    print()
