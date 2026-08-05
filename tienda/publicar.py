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

PORTADAS = Path(__file__).resolve().parent / "portadas"

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

MEDIA = """
query($id: ID!) {
  product(id: $id) { media(first: 20) { nodes { alt } } }
}"""

SUBIDA = """
mutation($i: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $i) {
    userErrors { field message }
    stagedTargets { url resourceUrl parameters { name value } }
  }
}"""

ADJUNTAR = """
mutation($id: ID!, $m: [CreateMediaInput!]!) {
  productCreateMedia(productId: $id, media: $m) {
    mediaUserErrors { field message }
    media { alt }
  }
}"""

COLECCION = """
mutation($c: CollectionInput!) {
  collectionCreate(input: $c) {
    userErrors { field message }
    collection { id handle }
  }
}"""

BUSCAR_COL = """
query($h: String!) {
  collectionByHandle(handle: $h) { id handle }
}"""

METER = """
mutation($id: ID!, $p: [ID!]!) {
  collectionAddProducts(id: $id, productIds: $p) {
    userErrors { field message }
  }
}"""

TRADUCIR = """
mutation($id: ID!, $t: [TranslationInput!]!) {
  translationsRegister(resourceId: $id, translations: $t) {
    userErrors { field message }
  }
}"""


def multipart(url: str, parametros: list, nombre: str, datos: bytes) -> None:
    """Sube el fichero al destino que Shopify acaba de firmar.

    Se monta el multipart a mano porque urllib no lo trae y añadir una
    dependencia entera para cuatro líneas de frontera no compensa. El orden
    importa: los parámetros firmados van ANTES del fichero o S3 rechaza la
    petición sin decir por qué.
    """
    frontera = "----villuminations"
    cuerpo = b""
    for par in parametros:
        cuerpo += (f"--{frontera}\r\n"
                   f'Content-Disposition: form-data; name="{par["name"]}"\r\n\r\n'
                   f"{par['value']}\r\n").encode()
    cuerpo += (f"--{frontera}\r\n"
               f'Content-Disposition: form-data; name="file"; filename="{nombre}"\r\n'
               f"Content-Type: image/png\r\n\r\n").encode()
    cuerpo += datos + f"\r\n--{frontera}--\r\n".encode()
    peticion = urllib.request.Request(url, data=cuerpo, headers={
        "Content-Type": f"multipart/form-data; boundary={frontera}"})
    urllib.request.urlopen(peticion).read()


def portada(producto: str, ficha: dict) -> str:
    """Sube la portada, si la hay y si no está ya puesta.

    El alt hace de marca: si ya existe una imagen con el alt de esta ficha,
    no se vuelve a subir. Sin eso, cada pasada añadiría otra copia y la ficha
    acabaría con seis portadas iguales en la galería.
    """
    png = PORTADAS / (ficha.get("portada") or "")
    if not ficha.get("portada") or not png.exists():
        return "sin portada"

    marca = f"VILLUMINATIONS · {ficha['handle']}"
    puestas = pedir(MEDIA, {"id": producto})["product"]["media"]["nodes"]
    if any(m.get("alt") == marca for m in puestas):
        return "portada ya puesta"

    destino = pedir(SUBIDA, {"i": [{
        "filename": png.name, "mimeType": "image/png",
        "resource": "IMAGE", "httpMethod": "POST",
    }]})["stagedUploadsCreate"]["stagedTargets"][0]
    multipart(destino["url"], destino["parameters"], png.name, png.read_bytes())
    pedir(ADJUNTAR, {"id": producto, "m": [{
        "mediaContentType": "IMAGE",
        "originalSource": destino["resourceUrl"],
        "alt": marca,
    }]})
    return "portada subida"


def coleccion(handle: str, titulo: str, cuerpo: str, gids: list) -> None:
    existente = pedir(BUSCAR_COL, {"h": handle})["collectionByHandle"]
    if existente:
        cid = existente["id"]
    else:
        cid = pedir(COLECCION, {"c": {
            "handle": handle, "title": titulo, "descriptionHtml": cuerpo,
        }})["collectionCreate"]["collection"]["id"]
    if gids:
        pedir(METER, {"id": cid, "p": gids})


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
    ficha["_gid"] = producto["id"]
    return f"{accion} · {portada(producto['id'], ficha)}"


COLECCIONES = {
    "planes": ("Planes de entrenamiento",
               "<p>Alimentación, entrenamiento, descanso y seguimiento, en tres "
               "niveles. Cada nivel es una descarga digital en español, inglés y "
               "francés, con versión de pantalla y versión preparada para "
               "imprimir.</p>"),
    "codices": ("Biblioteca · Los ocho códices",
                "<p>Ocho libros de referencia y de práctica, cada uno con sus "
                "láminas dibujadas para la edición y su cuaderno de trabajo. "
                "Todos se descargan en las tres lenguas: español, inglés y "
                "francés.</p>"),
}


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

    # Las colecciones van al final: hasta aquí no se sabe el gid de los que
    # se acaban de crear, y una colección sin sus productos no sirve de nada.
    if not ensayo:
        print()
        for clave, (titulo, cuerpo) in COLECCIONES.items():
            gids = [f["_gid"] for f in TODAS
                    if f.get("coleccion") == clave and f.get("_gid")]
            coleccion(clave, titulo, cuerpo, gids)
            print(f"    colección {clave:12} {titulo:34} {len(gids)} productos")
    print()


if __name__ == "__main__":
    main()
