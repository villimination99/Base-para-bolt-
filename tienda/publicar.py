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
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import descripciones                                            # noqa: E402
import fichas_libros                                            # noqa: E402
import seo                                                      # noqa: E402

PORTADAS = Path(__file__).resolve().parent / "portadas"

TIPO = {"es": "Descarga digital",
        "en": "Digital download",
        "fr": "Téléchargement numérique"}

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

TODAS = descripciones.FICHAS + fichas_libros.NUEVOS


def rebanada(titulo: str) -> str:
    """El handle que le toca a un título traducido.

    Shopify solo admite letras sin tilde, cifras y guiones, así que «Codex de
    la Volonté» tiene que salir como «codex-de-la-volonte».
    """
    plano = unicodedata.normalize("NFKD", titulo)
    plano = plano.encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", plano).strip("-").lower()


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

# Ojo con los dos tipos de entrada: crear y actualizar no comparten el mismo.
# `productCreate` pide ProductCreateInput y `productUpdate` pide
# ProductUpdateInput; pasarles ProductInput, que es lo que aceptaban las
# versiones viejas de la API, se rechaza con «Type mismatch on variable».
CREAR = """
mutation($p: ProductCreateInput!) {
  productCreate(product: $p) {
    userErrors { field message }
    product { id handle status variants(first: 1) { nodes { id } } }
  }
}"""

ACTUALIZAR = """
mutation($p: ProductUpdateInput!) {
  productUpdate(product: $p) {
    userErrors { field message }
    product { id handle status variants(first: 1) { nodes { id } } }
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

CANALES = """
query { publications(first: 20) { nodes { id name } } }"""

# Un producto en borrador no admite canales: Shopify acepta la mutación sin
# quejarse y no la aplica. Por eso esto se lanza siempre después de ponerlo
# en ACTIVE, nunca antes.
PUBLICAR_EN = """
mutation($id: ID!, $c: [PublicationInput!]!) {
  publishablePublish(id: $id, input: $c) {
    userErrors { field message }
  }
}"""

COLECCION = """
mutation($c: CollectionInput!) {
  collectionCreate(input: $c) {
    userErrors { field message }
    collection { id handle }
  }
}"""

ACTUALIZAR_COL = """
mutation($c: CollectionInput!) {
  collectionUpdate(input: $c) {
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

REDIRIGIR = """
mutation($r: UrlRedirectInput!) {
  urlRedirectCreate(urlRedirect: $r) {
    userErrors { field message }
    urlRedirect { path target }
  }
}"""

TRADUCIR = """
mutation($id: ID!, $t: [TranslationInput!]!) {
  translationsRegister(resourceId: $id, translations: $t) {
    userErrors { field message }
  }
}"""


_CANALES: list = []


def canales() -> list:
    """Los canales de venta de la tienda, preguntados una sola vez."""
    if not _CANALES:
        _CANALES.extend({"publicationId": n["id"]} for n in
                        pedir(CANALES, {})["publications"]["nodes"])
    return _CANALES


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

    El alt describe la imagen para quien no la ve y para el buscador de
    imágenes, y de paso hace de marca: si ya hay una imagen con el alt de esta
    ficha, no se vuelve a subir. Sin eso, cada pasada añadiría otra copia y la
    galería acabaría con seis portadas iguales.
    """
    png = PORTADAS / (ficha.get("portada") or "")
    if not ficha.get("portada") or not png.exists():
        return "sin portada"

    marca = seo.ALT[ficha["handle"]]["es"]
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


def coleccion(handle: str, textos: dict, gids: list) -> None:
    """Crea o actualiza la colección, con su SEO y sus dos traducciones."""
    titulo, cuerpo, t_seo, d_seo = textos["es"]
    entrada = {"handle": handle, "title": titulo, "descriptionHtml": cuerpo,
               "seo": {"title": t_seo, "description": d_seo}}

    existente = pedir(BUSCAR_COL, {"h": handle})["collectionByHandle"]
    if existente:
        entrada["id"] = existente["id"]
        cid = pedir(ACTUALIZAR_COL, {"c": entrada})["collectionUpdate"]["collection"]["id"]
    else:
        cid = pedir(COLECCION, {"c": entrada})["collectionCreate"]["collection"]["id"]

    if gids:
        pedir(METER, {"id": cid, "p": gids})

    digests = {c["key"]: c["digest"] for c in
               pedir(DIGESTS, {"id": cid})["translatableResource"]
               ["translatableContent"]}
    traducciones = []
    for idioma in ("en", "fr"):
        t_i, c_i, ts_i, ds_i = textos[idioma]
        for clave, valor in (("title", t_i), ("body_html", c_i),
                             ("meta_title", ts_i), ("meta_description", ds_i)):
            if clave in digests:
                traducciones.append({
                    "key": clave, "locale": idioma, "value": valor,
                    "translatableContentDigest": digests[clave]})
    if traducciones:
        pedir(TRADUCIR, {"id": cid, "t": traducciones})


def publicar(ficha: dict, ensayo: bool) -> str:
    """Crea o actualiza la ficha, y devuelve qué hizo.

    Si el producto cambia de handle se busca primero por el nuevo y luego por
    el viejo. Sin ese segundo intento, renombrar significaría crear un
    duplicado y dejar huérfano el original con sus pedidos dentro.
    """
    handle = ficha["handle"]
    viejo = ficha.get("handle_viejo")
    existente = pedir(BUSCAR, {"h": handle})["productByHandle"]
    renombrado = False
    if not existente and viejo:
        existente = pedir(BUSCAR, {"h": viejo})["productByHandle"]
        renombrado = bool(existente)

    titulo_seo, descripcion_seo = seo.META[handle]["es"]
    entrada = {
        "handle": handle,
        "title": ficha["titulo"]["es"],
        "descriptionHtml": ficha["es"].strip(),
        "vendor": "VILLUMINATIONS",
        "productType": TIPO["es"],
        "tags": seo.ETIQUETAS[handle] + seo.COMUNES,
        "seo": {"title": titulo_seo, "description": descripcion_seo},
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
        t_seo, d_seo = seo.META[handle][idioma]
        traducciones += [
            {"key": "title", "locale": idioma,
             "value": ficha["titulo"][idioma],
             "translatableContentDigest": digests["title"]},
            {"key": "body_html", "locale": idioma,
             "value": ficha[idioma].strip(),
             "translatableContentDigest": digests["body_html"]},
            # El handle también se traduce: sin esto la ficha inglesa vive en
            # una dirección castellana y el buscador la lee como tal.
            {"key": "handle", "locale": idioma,
             "value": rebanada(ficha["titulo"][idioma]),
             "translatableContentDigest": digests["handle"]},
            {"key": "product_type", "locale": idioma,
             "value": TIPO[idioma],
             "translatableContentDigest": digests["product_type"]},
        ]
        # Shopify solo declara meta_title y meta_description como traducibles
        # cuando el producto ya los tiene puestos. Se acaban de escribir en la
        # misma pasada, así que estarán; se comprueba de todos modos para no
        # reventar si algún día cambia el orden de las cosas.
        for clave, valor in (("meta_title", t_seo),
                             ("meta_description", d_seo)):
            if clave in digests:
                traducciones.append({
                    "key": clave, "locale": idioma, "value": valor,
                    "translatableContentDigest": digests[clave]})
    pedir(TRADUCIR, {"id": producto["id"], "t": traducciones})
    ficha["_gid"] = producto["id"]

    # Estar en ACTIVE no basta para que se vea: hay que darlo de alta en cada
    # canal. Un producto creado por la API nace sin ninguno, así que si nadie
    # hace esto se publica y no aparece en la tienda.
    if producto["status"] == "ACTIVE":
        pedir(PUBLICAR_EN, {"id": producto["id"], "c": canales()})

    # Renombrar sin redirigir tira a la basura los enlaces que ya existan y
    # todo lo que el buscador tuviera indexado del handle anterior.
    if renombrado:
        pedir(REDIRIGIR, {"r": {"path": f"/products/{viejo}",
                                "target": f"/products/{handle}"}})
        accion += f" · /{viejo} → /{handle}"

    return f"{accion} · {portada(producto['id'], ficha)}"


COLECCIONES = {
    "planes": {
        "es": ("Planes de entrenamiento",
               "<p>Alimentación, entrenamiento, descanso y seguimiento, en tres "
               "niveles. Cada nivel es una descarga digital en español, inglés y "
               "francés, con versión de pantalla y versión preparada para "
               "imprimir.</p>",
               "Planes de entrenamiento en PDF | VILLUMINATIONS",
               "Tres niveles de planes en PDF: alimentación, entrenamiento, "
               "descanso y seguimiento semanal. Español, inglés y francés."),
        "en": ("Training plans",
               "<p>Food, training, rest and follow-up, in three tiers. Each "
               "tier is a digital download in English, Spanish and French, with "
               "a screen version and a print-ready version.</p>",
               "Training plans in PDF | VILLUMINATIONS",
               "Three tiers of plans in PDF: food, training, rest and weekly "
               "follow-up. In English, Spanish and French."),
        "fr": ("Plans d'entraînement",
               "<p>Alimentation, entraînement, repos et suivi, en trois "
               "niveaux. Chaque niveau est un téléchargement numérique en "
               "français, espagnol et anglais, avec une version écran et une "
               "version prête à imprimer.</p>",
               "Plans d'entraînement en PDF | VILLUMINATIONS",
               "Trois niveaux de plans en PDF : alimentation, entraînement, "
               "repos et suivi hebdomadaire. En trois langues."),
    },
    "conocimiento": {
        "es": ("Conocimiento",
               "<p>Ocho libros de referencia y de práctica, cada uno con sus "
               "láminas dibujadas para la edición y su cuaderno de trabajo. "
               "Nutrición, carga, descanso y voluntad para el cuerpo; tarot, "
               "zodiaco, ritual y observación interior para lo demás. Todos se "
               "descargan en las tres lenguas: español, inglés y francés.</p>",
               "Conocimiento — ocho libros en PDF | VILLUMINATIONS",
               "Ocho libros en PDF con sus láminas y su cuaderno: nutrición, "
               "carga, descanso, voluntad, tarot, zodiaco y práctica interior."),
        "en": ("Knowledge",
               "<p>Eight books of reference and of practice, each with its own "
               "plates drawn for the edition and its working notebook. "
               "Nutrition, load, rest and will for the body; tarot, zodiac, "
               "ritual and inner observation for the rest. All of them download "
               "in three languages: English, Spanish and French.</p>",
               "Knowledge — eight PDF books | VILLUMINATIONS",
               "Eight PDF books with their plates and notebooks: nutrition, "
               "load, rest, will, tarot, zodiac and inner practice."),
        "fr": ("Connaissance",
               "<p>Huit livres de référence et de pratique, chacun avec ses "
               "planches dessinées pour l'édition et son cahier de travail. "
               "Nutrition, charge, repos et volonté pour le corps ; tarot, "
               "zodiaque, rituel et observation intérieure pour le reste. Tous "
               "se téléchargent en trois langues.</p>",
               "Connaissance — huit livres en PDF | VILLUMINATIONS",
               "Huit livres en PDF avec leurs planches et leurs cahiers : "
               "nutrition, charge, repos, volonté, tarot, zodiaque, pratique."),
    },
}


def main() -> None:
    ensayo = "--ensayo" in sys.argv[1:]
    if not ensayo and not (TIENDA and TOKEN):
        raise SystemExit(
            "\n  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN en el entorno.\n"
            "  Con --ensayo se puede ver qué haría sin credenciales.\n")

    fuera = seo.comprobar()
    if fuera:
        raise SystemExit("\n  SEO fuera de medida; no se publica:\n    "
                         + "\n    ".join(fuera) + "\n")

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
        for clave, textos in COLECCIONES.items():
            gids = [f["_gid"] for f in TODAS
                    if f.get("coleccion") == clave and f.get("_gid")]
            coleccion(clave, textos, gids)
            print(f"    colección {clave:12} {textos['es'][0]:34} "
                  f"{len(gids)} productos")
    print()


if __name__ == "__main__":
    main()
