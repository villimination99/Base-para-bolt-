#!/usr/bin/env python3
"""
VILLUMINATIONS — Registrar el Diario en inglés y en francés
============================================================
Lo mismo que `traducir.py` hace con los productos, con los artículos del
blog: busca cada entrada **por su handle**, pide los digests recién escritos y
manda el texto de `articulos_en_fr.py` sin que pase por un teclado.

    python3 tienda/traducir_blog.py --ensayo   qué se registraría
    python3 tienda/traducir_blog.py            lo registra

Tres cosas que este publicador hace a propósito
-----------------------------------------------
**No traduce el handle.** Shopify deja traducirlo y crea una URL localizada,
como se hizo con las colecciones. Aquí no: `lecturas.py` escribe los enlaces
de las cuarenta fichas como `/en/blogs/diario/<handle-castellano>`, y traducir
el handle los convertiría todos en 404 de golpe. Está en `PROHIBIDAS`, y si
algún día se decide traducirlos hay que cambiar las dos cosas a la vez.

**No inventa nombres de campo.** Las claves traducibles de un artículo las
dice la propia tienda en `translatableContent`. Este fichero pide la lista y
solo manda las que existen de verdad; las que no reconoce las enumera al
final en vez de fallar. `blog.py` se escribió a ciegas con la referencia
delante y hubo que corregirlo; esta vez se pregunta.

**No registra un artículo a medio traducir.** Si falta el cuerpo, o el título,
o la descripción de buscador, ese artículo se salta entero. Media traducción
en la tienda es peor que ninguna: la página sale mezclando dos lenguas.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import articulos                                                # noqa: E402
import articulos_en_fr as traducidos                            # noqa: E402

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

BLOG = articulos.BLOG["handle"]

# clave traducible de Shopify -> de dónde sale el texto
DE_DONDE = {
    "title": lambda h, l: traducidos.CUERPOS[h][l]["titulo"],
    "body_html": lambda h, l: traducidos.cuerpo(h, l),
    "body": lambda h, l: traducidos.cuerpo(h, l),
    "summary_html": lambda h, l: traducidos.CUERPOS[h][l]["resumen"],
    "summary": lambda h, l: traducidos.CUERPOS[h][l]["resumen"],
    "meta_title": lambda h, l: traducidos.CUERPOS[h][l]["meta"][0],
    "meta_description": lambda h, l: traducidos.CUERPOS[h][l]["meta"][1],
}

# El handle no se traduce: rompería los cuarenta enlaces de lecturas.py.
PROHIBIDAS = {"handle"}

# `body` y `body_html` son la misma cosa con dos nombres según la versión de
# la API; igual `summary` y `summary_html`. Solo puede venir una de cada par.
PAREJAS = (("body", "body_html"), ("summary", "summary_html"))


def pedir(consulta: str, variables: dict) -> dict:
    cuerpo = json.dumps({"query": consulta, "variables": variables}).encode()
    peticion = urllib.request.Request(
        f"https://{TIENDA}/admin/api/{API}/graphql.json",
        data=cuerpo,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": TOKEN},
    )
    with urllib.request.urlopen(peticion) as r:
        datos = json.loads(r.read())
    if "errors" in datos:
        raise SystemExit(f"  GraphQL: {datos['errors']}")
    for bloque in datos.get("data", {}).values():
        if isinstance(bloque, dict) and bloque.get("userErrors"):
            raise SystemExit(f"  Shopify: {bloque['userErrors']}")
    return datos["data"]


# `blogByHandle` ya no existe en la API 2025-01: se quitó del QueryRoot y
# devuelve «Field 'blogByHandle' doesn't exist». Se busca con `blogs(query:)`,
# que es lo que queda. Se descubrió ejecutándolo, no leyendo la referencia.
ARTICULOS = """
query($handle: String!, $cursor: String) {
  blogs(first: 1, query: $handle) {
    nodes {
      handle
      articles(first: 250, after: $cursor) {
        nodes { id handle }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}"""

DIGESTS = """
query($id: ID!) {
  translatableResource(resourceId: $id) {
    translatableContent { key value digest }
  }
}"""

REGISTRAR = """
mutation($id: ID!, $t: [TranslationInput!]!) {
  translationsRegister(resourceId: $id, translations: $t) {
    userErrors { field message }
  }
}"""


def por_handle() -> dict:
    """handle del artículo -> gid."""
    mapa, cursor = {}, None
    while True:
        blog = pedir(ARTICULOS, {"handle": f"handle:{BLOG}", "cursor": cursor})
        nodos = blog.get("blogs", {}).get("nodes") or []
        if not nodos:
            raise SystemExit(f"  No existe el blog /{BLOG} en la tienda.")
        d = nodos[0]["articles"]
        mapa.update({n["handle"]: n["id"] for n in d["nodes"]})
        if not d["pageInfo"]["hasNextPage"]:
            return mapa
        cursor = d["pageInfo"]["endCursor"]


def entradas(handle: str, contenido: list) -> tuple:
    """(traducciones que registrar, claves que la tienda ofrece y no sé llenar).

    Se recorre lo que dice la tienda, no una lista escrita de memoria.
    """
    digest = {c["key"]: c["digest"] for c in contenido}
    fuera, salida = [], []
    for clave in digest:
        if clave in PROHIBIDAS:
            continue
        if clave not in DE_DONDE:
            fuera.append(clave)
            continue
        for lengua in traducidos.LENGUAS:
            if lengua not in traducidos.CUERPOS.get(handle, {}):
                continue
            salida.append({
                "locale": lengua,
                "key": clave,
                "value": DE_DONDE[clave](handle, lengua),
                "translatableContentDigest": digest[clave],
            })
    # de cada pareja solo debería haber llegado una; si llegan las dos, se
    # registran las dos y no pasa nada, pero conviene verlo
    for a, b in PAREJAS:
        if a in digest and b in digest:
            fuera.append(f"{a} y {b} a la vez")
    return salida, fuera


def main() -> int:
    ensayo = "--ensayo" in sys.argv

    malos = traducidos.comprobar()
    if malos:
        print("\n  No se registra nada: las traducciones no pasan la"
              " comprobación.\n")
        for m in malos:
            print(f"    {m}")
        return 1

    listos = sorted(traducidos.CUERPOS)
    if not listos:
        print("\n  No hay ningún artículo traducido todavía.\n")
        return 0

    if not (TIENDA and TOKEN):
        if not ensayo:
            raise SystemExit("  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN.")
        print(f"\n  Ensayo sin credenciales: {len(listos)} artículos "
              f"traducidos y comprobados, listos para registrar.\n")
        for h in listos:
            lenguas = ", ".join(sorted(traducidos.CUERPOS[h]))
            print(f"    {h[:50]:52} {lenguas}")
        pendientes = traducidos.faltan()
        if pendientes:
            print(f"\n    faltan {len(pendientes)} por traducir:")
            for h in pendientes:
                print(f"      {h}")
        print()
        return 0

    mapa = por_handle()
    hechos = perdidos = 0
    desconocidas = set()
    for handle in listos:
        gid = mapa.get(handle)
        if not gid:
            print(f"    ¿? no está en el blog: {handle}")
            perdidos += 1
            continue
        contenido = pedir(DIGESTS, {"id": gid})["translatableResource"]
        registrar, fuera = entradas(handle, contenido["translatableContent"])
        desconocidas.update(fuera)
        if not registrar:
            print(f"    -- nada que registrar: {handle}")
            continue
        if ensayo:
            claves = sorted({e['key'] for e in registrar})
            print(f"    ~~ {handle[:44]} · {', '.join(claves)}")
        else:
            pedir(REGISTRAR, {"id": gid, "t": registrar})
            print(f"    ok {handle}")
        hechos += 1

    print(f"\n  {hechos} artículos "
          f"{'se registrarían' if ensayo else 'registrados'}"
          f"{f' · {perdidos} sin encontrar' if perdidos else ''}")
    if desconocidas:
        print(f"  claves traducibles que la tienda ofrece y aquí no se "
              f"llenan: {', '.join(sorted(desconocidas))}")
    pendientes = traducidos.faltan()
    if pendientes:
        print(f"  faltan {len(pendientes)} artículos por traducir")
    print()
    return 1 if perdidos else 0


if __name__ == "__main__":
    raise SystemExit(main())
