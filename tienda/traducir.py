#!/usr/bin/env python3
"""
VILLUMINATIONS — Publicador de traducciones
--------------------------------------------
Lleva a Shopify las traducciones al inglés y al francés de los 29 productos de
proveedor: el cuerpo de la ficha y el tipo de producto.

Uso:  export SHOPIFY_TIENDA=villuminations.myshopify.com
      export SHOPIFY_TOKEN=shpat_...     (Admin API: write_translations)
      python3 tienda/traducir.py --ensayo   dice qué haría, sin tocar nada
      python3 tienda/traducir.py            lo hace

Re-ejecutable: dos pasadas seguidas dejan la tienda igual.

**Por qué existe este fichero.** Hasta ahora las traducciones se registraban a
mano, copiando el JSON dentro de una mutación. En una de esas copias se coló un
«veintivún» que no estaba en el original, y hubo que cotejar los ocho artículos
carácter a carácter para encontrarlo. El texto sale de `cuerpos_en_fr.py` y
llega a la API sin pasar por ningún teclado.

Dos cosas de la API que hay que respetar y no son evidentes:

· El **digest se pide después** de escribir el original y describe el texto
  castellano actual. Si el cuerpo en castellano cambia, los digests viejos ya
  no valen y Shopify rechaza la traducción. Por eso se piden en la misma
  pasada, nunca se guardan.

· Los productos **se buscan por handle**, no por identificador. Los handles no
  cambian —están indexados— y una lista de IDs a mano envejece mal.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalogo                                                 # noqa: E402
import cuerpos_en_fr                                            # noqa: E402

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

# El tipo de producto de catalogo.TIPOS, en las otras dos lenguas.
TIPOS_EN = {
    "Suplemento": "Supplement",
    "Equipo de entrenamiento": "Training equipment",
    "Ropa deportiva": "Sportswear",
    "Accesorio": "Accessory",
    "Cuidado personal": "Personal care",
}
TIPOS_FR = {
    "Suplemento": "Complément alimentaire",
    "Equipo de entrenamiento": "Équipement d'entraînement",
    "Ropa deportiva": "Vêtements de sport",
    "Accesorio": "Accessoire",
    "Cuidado personal": "Soins du corps",
}


def pedir(consulta: str, variables: dict) -> dict:
    """Una llamada a la Admin API. GraphQL responde 200 con los errores dentro,
    así que hay que mirar en dos sitios: el sobre y los userErrors."""
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


PRODUCTOS = """
query($cursor: String) {
  products(first: 250, after: $cursor) {
    nodes { id handle }
    pageInfo { hasNextPage endCursor }
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
    """handle -> gid, recorriendo las páginas que haga falta."""
    mapa, cursor = {}, None
    while True:
        d = pedir(PRODUCTOS, {"cursor": cursor})["products"]
        for n in d["nodes"]:
            mapa[n["handle"]] = n["id"]
        if not d["pageInfo"]["hasNextPage"]:
            return mapa
        cursor = d["pageInfo"]["endCursor"]


def traducciones(handle: str, contenido: list) -> list:
    """Las entradas de TranslationInput para un producto, con sus digests
    recién pedidos. Devuelve lista vacía si no hay nada que registrar."""
    digest = {c["key"]: c["digest"] for c in contenido}
    valor = {c["key"]: c["value"] for c in contenido}
    salida = []

    if handle in cuerpos_en_fr.CUERPOS_EN and "body_html" in digest:
        salida += [
            {"locale": "en", "key": "body_html",
             "value": cuerpos_en_fr.CUERPOS_EN[handle],
             "translatableContentDigest": digest["body_html"]},
            {"locale": "fr", "key": "body_html",
             "value": cuerpos_en_fr.CUERPOS_FR[handle],
             "translatableContentDigest": digest["body_html"]},
        ]

    tipo = valor.get("product_type")
    if tipo in TIPOS_EN and "product_type" in digest:
        salida += [
            {"locale": "en", "key": "product_type", "value": TIPOS_EN[tipo],
             "translatableContentDigest": digest["product_type"]},
            {"locale": "fr", "key": "product_type", "value": TIPOS_FR[tipo],
             "translatableContentDigest": digest["product_type"]},
        ]
    return salida


def main() -> int:
    ensayo = "--ensayo" in sys.argv
    malos = cuerpos_en_fr.comprobar()
    if malos:
        print("\n  No se publica nada: las traducciones no pasan la"
              " comprobación.\n")
        for m in malos:
            print(f"    {m}")
        return 1

    if not ensayo and not (TIENDA and TOKEN):
        raise SystemExit("  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN.")

    if ensayo and not (TIENDA and TOKEN):
        # Sin credenciales el ensayo sigue valiendo para contar el trabajo.
        print(f"\n  Ensayo sin credenciales: {len(cuerpos_en_fr.CUERPOS_EN)} "
              f"productos traducidos y comprobados, listos para registrar.\n")
        for h in sorted(cuerpos_en_fr.CUERPOS_EN):
            print(f"    {h[:64]}")
        print()
        return 0

    mapa = por_handle()
    hechos = perdidos = 0
    for handle in sorted(cuerpos_en_fr.CUERPOS_EN):
        gid = mapa.get(handle)
        if not gid:
            print(f"    ¿? no está en la tienda: {handle[:56]}")
            perdidos += 1
            continue
        contenido = pedir(DIGESTS, {"id": gid})["translatableResource"]
        entradas = traducciones(handle, contenido["translatableContent"])
        if not entradas:
            print(f"    -- nada que registrar: {handle[:56]}")
            continue
        if ensayo:
            claves = sorted({e["key"] for e in entradas})
            print(f"    ~~ {handle[:52]} · {', '.join(claves)}")
        else:
            pedir(REGISTRAR, {"id": gid, "t": entradas})
            print(f"    ok {handle[:56]}")
        hechos += 1

    print(f"\n  {hechos} productos {'se registrarían' if ensayo else 'registrados'}"
          f"{f' · {perdidos} sin encontrar' if perdidos else ''}\n")
    return 1 if perdidos else 0


if __name__ == "__main__":
    raise SystemExit(main())
