#!/usr/bin/env python3
"""
VILLUMINATIONS — Publicador de fichas en Shopify
------------------------------------------------
Lleva a la tienda lo que hay en descripciones.py y fichas_libros.py: crea el
producto si no existe, lo actualiza si existe, y registra las traducciones
inglesa y francesa. El texto vive en el repositorio y esto solo lo empuja; si
hay que corregir una coma se corrige allí y se vuelve a lanzar.

Dos decisiones que conviene conocer antes de lanzarlo:

· Los productos NUEVOS se crean en BORRADOR. No es prudencia excesiva: un
  producto nuevo nace con precio 0,00, y publicado eso significa que cualquiera
  se lleva el libro gratis mientras nadie mira. Se crean en borrador, se les
  pone precio en el panel y se publican a mano. Los que ya existen no se tocan
  de estado: si están activos siguen activos.

· Todos se configuran como lo que son —un PDF— y no como mercancía: sin
  inventario, sin envío y sin política de agotado. Los cinco productos que ya
  había estaban al revés, con stock finito y pidiendo dirección de envío, y eso
  los habría agotado a las pocas ventas.

Uso:  export SHOPIFY_TIENDA=villuminations.myshopify.com
      export SHOPIFY_TOKEN=shpat_...          (Admin API, scope write_products)
      python3 tienda/publicar.py --ensayo     dice qué haría, sin tocar nada
      python3 tienda/publicar.py              lo hace

El token necesita write_products y write_translations. Se saca del panel en
Configuración → Aplicaciones → Desarrollar aplicaciones.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import descripciones                                            # noqa: E402
import fichas_libros                                            # noqa: E402

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

TODAS = descripciones.FICHAS + fichas_libros.NUEVOS


def pedir(consulta: str, variables: dict) -> dict:
    """Una llamada a la Admin API. Los errores se levantan, no se cuentan.

    GraphQL responde 200 con los errores dentro, así que hay que mirar dos
    sitios: el sobre («errors») y los userErrors de cada mutación. Un
    publicador que ignore los segundos deja productos a medio escribir y dice
    que todo fue bien.
    """
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


BUSCAR = """
query($h: String!) {
  productByHandle(handle: $h) { id handle
    variants(first: 1) { nodes { id } } }
}"""

CREAR = """
mutation($p: ProductInput!) {
  productCreate(product: $p) {
    userErrors { field message }
    product { id handle variants(first: 1) { nodes { id } } }
  }
}"""

ACTUALIZAR = """
mutation($p: ProductInput!) {
  productUpdate(product: $p) {
    userErrors { field message }
    product { id handle variants(first: 1) { nodes { id } } }
  }
}"""

VARIANTE = """
mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) {
  productVariantsBulkUpdate(productId: $p, variants: $v) {
    userErrors { field message }
  }
}"""

DIGESTS = """
query($id: ID!) {
  translatableResource(resourceId: $id) {
    translatableContent { key digest }
  }
}"""

TRADUCIR = """
mutation($id: ID!, $t: [TranslationInput!]!) {
  translationsRegister(resourceId: $id, translations: $t) {
    userErrors { field message }
  }
}"""


def publicar(ficha: dict, ensayo: bool) -> str:
    handle = ficha["handle"]
    existente = pedir(BUSCAR, {"h": handle})["productByHandle"]

    entrada = {
        "handle": handle,
        "title": ficha["titulo"]["es"],
        "descriptionHtml": ficha["es"].strip(),
        "vendor": "VILLUMINATIONS",
        "productType": "Descarga digital",
        "tags": ["descarga-digital", "trilingue"],
    }

    if existente:
        accion = "actualizado"
        entrada["id"] = existente["id"]
    else:
        accion = "CREADO en borrador"
        # Solo los nuevos nacen en borrador; a los que ya están publicados no
        # se les toca el estado, que no es cosa de este script decidirlo.
        entrada["status"] = "DRAFT"

    if ensayo:
        return f"{accion} (ensayo)"

    consulta = ACTUALIZAR if existente else CREAR
    clave = "productUpdate" if existente else "productCreate"
    producto = pedir(consulta, {"p": entrada})[clave]["product"]

    # Un PDF no tiene stock ni se envía.
    variante = producto["variants"]["nodes"][0]["id"]
    pedir(VARIANTE, {"p": producto["id"], "v": [{
        "id": variante,
        "inventoryPolicy": "CONTINUE",
        "inventoryItem": {"tracked": False, "requiresShipping": False},
    }]})

    # Las traducciones van contra el digest del texto que se acaba de subir,
    # así que se piden después de escribirlo y nunca antes.
    digests = {c["key"]: c["digest"] for c in
               pedir(DIGESTS, {"id": producto["id"]})["translatableResource"]
               ["translatableContent"]}
    traducciones = []
    for idioma in ("en", "fr"):
        traducciones += [
            {"key": "title", "locale": idioma,
             "value": ficha["titulo"][idioma],
             "translatableContentDigest": digests["title"]},
            {"key": "body_html", "locale": idioma,
             "value": ficha[idioma].strip(),
             "translatableContentDigest": digests["body_html"]},
        ]
    pedir(TRADUCIR, {"id": producto["id"], "t": traducciones})
    return accion


def main() -> None:
    ensayo = "--ensayo" in sys.argv[1:]
    if not ensayo and not (TIENDA and TOKEN):
        raise SystemExit(
            "\n  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN en el entorno.\n"
            "  Con --ensayo se puede ver qué haría sin credenciales.\n")

    print(f"\n  Publicando {len(TODAS)} fichas · "
          f"{len(TODAS) * 3} textos" + ("  ·  ensayo" if ensayo else ""))
    for ficha in TODAS:
        if ensayo and not (TIENDA and TOKEN):
            estado = "sin credenciales: no se consulta la tienda"
        else:
            estado = publicar(ficha, ensayo)
        print(f"    {ficha['handle']:34} {ficha['titulo']['es']:32} {estado}")
    print()


if __name__ == "__main__":
    main()
