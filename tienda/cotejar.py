#!/usr/bin/env python3
"""
VILLUMINATIONS — Cotejar la tienda contra el repositorio
=========================================================
`auditar.py` cruza ficheros del repositorio. Ninguna comprobación cruzaba el
repositorio con **lo que la tienda dice de verdad**, y por ahí se coló todo lo
que este fichero busca ahora.

    export SHOPIFY_TIENDA=villuminations.myshopify.com
    export SHOPIFY_TOKEN=shpat_...
    python3 tienda/cotejar.py

**Solo lee.** Ni una mutación. Se puede lanzar cuando sea.

Qué mira, y por qué cada cosa se le escapaba a lo que ya había
---------------------------------------------------------------
· **El original castellano, sin descargarlo.** El `digest` que devuelve
  `translatableContent` es el SHA-256 del valor, tal cual. Así que basta con
  comparar `sha256(lo que compone el repositorio)` contra el digest para saber
  si la tienda tiene el texto vivo, y cuesta una consulta en vez de bajarse
  todos los cuerpos.

· **La traducción, byte a byte.** Las traducciones no llevan digest, así que
  esas sí hay que pedirlas; se comparan por SHA-256 contra lo que compone
  `articulos_en_fr` y `faq`. Media palabra distinta salta.

· **El prefijo de idioma en cada enlace.** Un `href="/pages/contact"` dentro
  de un cuerpo inglés manda al comprador a la página castellana: Shopify no
  reescribe lo que va en el cuerpo, sale tal cual. Estuvo publicado así en la
  FAQ, en la página de «cómo se hace» y en la colección de suplementos —ocho
  enlaces— sin que nada lo viera, porque la única guarda que existía vivía en
  `articulos_en_fr` y enumeraba tres prefijos conocidos en vez de comprobar la
  regla.

· **`outdated`.** Es un booleano por clave y por lengua que dice si el
  original cambió después de la traducción. Contesta gratis la pregunta de si
  algún registro entró contra un digest caducado.

· **Lo que la tienda tiene y el repositorio no.** Las colecciones y la página
  de «cómo se hace» tienen cuerpo traducido escrito directamente en la tienda:
  no hay fuente aquí que los regenere ni comprobación que los mida. Eso no es
  un fallo que arreglar en un commit, pero **hay que saberlo**, porque de esos
  textos nadie responde. Se enumeran al final.
"""

import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import articulos                                                  # noqa: E402
import articulos_en_fr as traducidos                              # noqa: E402
import faq                                                        # noqa: E402

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

LENGUAS = ("en", "fr")
ENLACE = re.compile(r'href="(/[^"]*)"')

# La página de preguntas. El identificador es fijo porque la página ya existe;
# si algún día se recrea, se cambia aquí.
PAGINA_FAQ = "preguntas"

# De dónde sale, en el repositorio, cada clave traducible de un artículo.
DE_DONDE = {
    "title": lambda h, l: traducidos.CUERPOS[h][l]["titulo"],
    "body_html": lambda h, l: traducidos.cuerpo(h, l),
    "summary_html": lambda h, l: traducidos.CUERPOS[h][l]["resumen"],
    "meta_title": lambda h, l: traducidos.CUERPOS[h][l]["meta"][0],
    "meta_description": lambda h, l: traducidos.CUERPOS[h][l]["meta"][1],
}


def sha(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()


def pedir(consulta: str, variables: dict | None = None) -> dict:
    cuerpo = json.dumps({"query": consulta,
                         "variables": variables or {}}).encode()
    peticion = urllib.request.Request(
        f"https://{TIENDA}/admin/api/{API}/graphql.json",
        data=cuerpo,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": TOKEN},
    )
    with urllib.request.urlopen(peticion) as r:
        datos = json.loads(r.read())
    if "errors" in datos:
        raise RuntimeError("; ".join(e.get("message", "?")
                                     for e in datos["errors"]))
    return datos["data"]


ARTICULOS = """
query($handle: String!) {
  blogs(first: 1, query: $handle) {
    nodes { articles(first: 250) { nodes {
      handle
      translatableContent { key digest }
      en: translations(locale: "en") { key value outdated }
      fr: translations(locale: "fr") { key value outdated }
    } } }
  }
}"""

PAGINAS = """
query {
  pages(first: 50) { nodes {
    handle
    translatableContent { key digest }
    en: translations(locale: "en") { key value outdated }
    fr: translations(locale: "fr") { key value outdated }
  } }
}"""

COLECCIONES = """
query {
  collections(first: 50) { nodes {
    handle
    en: translations(locale: "en") { key value outdated }
    fr: translations(locale: "fr") { key value outdated }
  } }
}"""

PRODUCTOS = """
query($cursor: String) {
  products(first: 50, after: $cursor) {
    nodes {
      handle
      en: translations(locale: "en") { key value outdated }
      fr: translations(locale: "fr") { key value outdated }
    }
    pageInfo { hasNextPage endCursor }
  }
}"""


def enlaces_sin_prefijo(nodos: list, que: str) -> list:
    """Un enlace de un texto traducido tiene que llevar su prefijo de idioma.

    No se enumeran prefijos conocidos —así fue como se escapó `/pages/`—:
    vale cualquier ruta absoluta.
    """
    malos = []
    for n in nodos:
        for lengua in LENGUAS:
            for tr in n.get(lengua) or []:
                for destino in sorted(set(ENLACE.findall(tr.get("value") or ""))):
                    if not destino.startswith(f"/{lengua}/"):
                        malos.append(f"{que} {n['handle']} [{lengua}] "
                                     f"{tr['key']} → {destino}")
    return malos


def desiguales(nodos: list, que: str) -> list:
    """Un recurso traducido a una lengua y no a la otra.

    Media traducción es peor que ninguna: la página sale mezclando dos
    lenguas, o el buscador ve una versión inglesa que no existe en francés.
    `traducir_blog.py` ya se niega a registrar un artículo a medias; esto
    encuentra los que se registraron a medias antes de que existiera esa
    regla, o desde el panel.
    """
    malos = []
    for n in nodos:
        claves = {l: {t["key"] for t in (n.get(l) or [])} for l in LENGUAS}
        if claves["en"] == claves["fr"]:
            continue
        for l, otra in (("en", "fr"), ("fr", "en")):
            faltan = claves[l] - claves[otra]
            if faltan:
                malos.append(f"{que} {n['handle']} · está en {l} y no en "
                             f"{otra}: {', '.join(sorted(faltan))}")
    return malos


def caducadas(nodos: list, que: str) -> list:
    return [f"{que} {n['handle']} [{lengua}] {tr['key']}"
            for n in nodos for lengua in LENGUAS
            for tr in (n.get(lengua) or []) if tr.get("outdated")]


def main() -> int:
    if not (TIENDA and TOKEN):
        print("\n  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN. Este fichero"
              " pregunta a la tienda; sin credenciales no hay nada que"
              " cotejar.\n")
        return 2

    hallazgos, sin_fuente = [], []

    # --- artículos del Diario -------------------------------------------
    nodos = pedir(ARTICULOS, {"handle": f"handle:{articulos.BLOG['handle']}"})
    arts = nodos["blogs"]["nodes"][0]["articles"]["nodes"]
    cotejadas = 0
    for a in arts:
        h = a["handle"]
        if h not in traducidos.CUERPOS:
            continue
        for lengua in LENGUAS:
            for tr in a[lengua]:
                if tr["key"] not in DE_DONDE:
                    continue
                cotejadas += 1
                if sha(tr["value"] or "") != sha(DE_DONDE[tr["key"]](h, lengua)):
                    hallazgos.append(f"artículo {h} [{lengua}] {tr['key']} ·"
                                     f" la tienda no dice lo que dice el"
                                     f" repositorio")
    hallazgos += enlaces_sin_prefijo(arts, "artículo")
    hallazgos += desiguales(arts, "artículo")
    hallazgos += caducadas(arts, "artículo")

    # --- páginas ---------------------------------------------------------
    pags = pedir(PAGINAS)["pages"]["nodes"]
    for p in pags:
        if p["handle"] != PAGINA_FAQ:
            if any(t["key"] == "body_html"
                   for l in LENGUAS for t in (p.get(l) or [])):
                sin_fuente.append(f"página {p['handle']}")
            continue
        digest = {c["key"]: c["digest"] for c in p["translatableContent"]}
        if digest.get("body_html") != sha(faq.cuerpo("es")):
            hallazgos.append("página preguntas [es] body_html · el original de"
                             " la tienda no es el que compone faq.py")
        for lengua in LENGUAS:
            for tr in p[lengua]:
                if tr["key"] == "body_html" and \
                        sha(tr["value"] or "") != sha(faq.cuerpo(lengua)):
                    hallazgos.append(f"página preguntas [{lengua}] body_html ·"
                                     f" no coincide con faq.py")
                cotejadas += 1
    hallazgos += enlaces_sin_prefijo(pags, "página")
    hallazgos += desiguales(pags, "página")
    hallazgos += caducadas(pags, "página")

    # --- colecciones y productos ----------------------------------------
    cols = pedir(COLECCIONES)["collections"]["nodes"]
    hallazgos += enlaces_sin_prefijo(cols, "colección")
    hallazgos += desiguales(cols, "colección")
    hallazgos += caducadas(cols, "colección")
    sin_fuente += [f"colección {c['handle']}" for c in cols
                   if any(t["key"] == "body_html" for l in LENGUAS
                          for t in (c.get(l) or []))]

    prods, cursor = [], None
    while True:
        d = pedir(PRODUCTOS, {"cursor": cursor})["products"]
        prods += d["nodes"]
        if not d["pageInfo"]["hasNextPage"]:
            break
        cursor = d["pageInfo"]["endCursor"]
    hallazgos += enlaces_sin_prefijo(prods, "producto")
    hallazgos += desiguales(prods, "producto")
    hallazgos += caducadas(prods, "producto")

    # --- informe ---------------------------------------------------------
    print(f"\n  Cotejo tienda ↔ repositorio · {cotejadas} traducciones"
          f" comparadas byte a byte")
    print(f"  {len(arts)} artículos · {len(pags)} páginas ·"
          f" {len(cols)} colecciones · {len(prods)} productos\n")
    if hallazgos:
        print(f"  {len(hallazgos)} hallazgos:\n")
        for m in hallazgos:
            print(f"    {m}")
    else:
        print("    La tienda dice exactamente lo que dice el repositorio.")

    if sin_fuente:
        print(f"\n  CUERPO TRADUCIDO SIN FUENTE EN EL REPOSITORIO"
              f" ({len(sin_fuente)})")
        print("    Se escribió directamente en la tienda: nada de aquí lo"
              " regenera\n    ni lo mide, y su redacción no la responde"
              " nadie.")
        for s in sorted(set(sin_fuente)):
            print(f"      {s}")
    print()
    return 1 if hallazgos else 0


if __name__ == "__main__":
    raise SystemExit(main())
