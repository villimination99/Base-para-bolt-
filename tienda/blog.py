#!/usr/bin/env python3
"""
VILLUMINATIONS — Publicador del blog
-------------------------------------
Lleva a Shopify lo que hay en articulos.py: crea el blog si no existe, crea o
actualiza cada entrada y le pone sus metaetiquetas de buscador. Re-ejecutable:
dos pasadas seguidas dejan la tienda en el mismo estado.

Uso:  export SHOPIFY_TIENDA=villuminations.myshopify.com
      export SHOPIFY_TOKEN=shpat_...     (Admin API: write_content)
      python3 tienda/blog.py --esquema   comprueba los campos contra la API
      python3 tienda/blog.py --ensayo    dice qué haría, sin tocar nada
      python3 tienda/blog.py             lo hace

**Lanza `--esquema` la primera vez.** Este publicador se escribió sin poder
hablar con la tienda —el servidor estaba caído—, así que los nombres de campo
de `ArticleCreateInput` y `BlogCreateInput` están puestos según la referencia y
no comprobados contra la API real. `--esquema` los pregunta e imprime lo que
sobra o falta; es un comando y evita descubrirlo a base de errores.

Dos cosas que Shopify hace distinto en el blog que en los productos:

· El SEO de un artículo **no es un campo**, son dos metacampos:
  `global.title_tag` y `global.description_tag`. Es la misma pareja que usa el
  panel cuando editas «Listado en motores de búsqueda».

· `isPublished` decide si la entrada es visible. Aquí se publica directamente
  porque un artículo, a diferencia de un producto, no tiene precio que se pueda
  quedar a cero por descuido.

Los artículos van solo en castellano. Traducirlos es trabajo aparte y se hace
como el de los productos: pidiendo el digest después de escribir el original.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import articulos                                                # noqa: E402

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

AUTOR = "VILLUMINATIONS"


def pedir(consulta: str, variables: dict) -> dict:
    """Una llamada a la Admin API. Los errores se levantan, no se cuentan.

    GraphQL responde 200 con los errores dentro, así que hay que mirar en dos
    sitios: el sobre («errors») y los userErrors de cada mutación.
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


BUSCAR_BLOG = """
query { blogs(first: 50) { nodes { id handle title } } }"""

CREAR_BLOG = """
mutation($b: BlogCreateInput!) {
  blogCreate(blog: $b) {
    userErrors { field message }
    blog { id handle }
  }
}"""

BUSCAR_ARTICULOS = """
query($id: ID!) {
  blog(id: $id) { articles(first: 100) { nodes { id handle title } } }
}"""

CREAR_ARTICULO = """
mutation($a: ArticleCreateInput!) {
  articleCreate(article: $a) {
    userErrors { field message }
    article { id handle }
  }
}"""

ACTUALIZAR_ARTICULO = """
mutation($id: ID!, $a: ArticleUpdateInput!) {
  articleUpdate(id: $id, article: $a) {
    userErrors { field message }
    article { id handle }
  }
}"""

ESQUEMA = """
query($t: String!) {
  __type(name: $t) { name inputFields { name type { name kind ofType { name } } } }
}"""


def esquema() -> None:
    """Compara los campos que usamos con los que la API dice aceptar.

    Existe porque este fichero se escribió a ciegas. Antes de la primera pasada
    real conviene lanzarlo: si Shopify ha renombrado un campo, sale aquí en vez
    de a mitad de la publicación con tres artículos escritos y dos no.
    """
    usados = {
        "BlogCreateInput": {"title", "handle"},
        "ArticleCreateInput": {"blogId", "title", "handle", "body", "summary",
                               "author", "tags", "isPublished", "metafields"},
        "ArticleUpdateInput": {"title", "body", "summary", "tags",
                               "isPublished", "metafields"},
    }
    for tipo, nuestros in usados.items():
        datos = pedir(ESQUEMA, {"t": tipo})["__type"]
        if not datos:
            print(f"  {tipo:22} NO EXISTE en la API {API}")
            continue
        suyos = {c["name"] for c in datos["inputFields"]}
        sobran = sorted(nuestros - suyos)
        print(f"  {tipo:22} {len(suyos):3} campos · usamos {len(nuestros)}")
        if sobran:
            print(f"      NO EXISTEN: {', '.join(sobran)}")
            print(f"      disponibles: {', '.join(sorted(suyos))}")
    print()


def metacampos(titulo: str, descripcion: str) -> list:
    """Las dos metaetiquetas de buscador, que en Shopify no son un campo."""
    return [
        {"namespace": "global", "key": "title_tag",
         "type": "single_line_text_field", "value": titulo},
        {"namespace": "global", "key": "description_tag",
         "type": "single_line_text_field", "value": descripcion},
    ]


def blog(ensayo: bool) -> str:
    """El identificador del blog, creándolo si hace falta."""
    b = articulos.BLOG
    existentes = {n["handle"]: n["id"]
                  for n in pedir(BUSCAR_BLOG, {})["blogs"]["nodes"]}
    if b["handle"] in existentes:
        print(f"  blog /{b['handle']} ya existe")
        return existentes[b["handle"]]
    if ensayo:
        print(f"  blog /{b['handle']} se crearía")
        return "gid://ensayo/Blog/0"
    creado = pedir(CREAR_BLOG, {"b": {"title": b["titulo"],
                                      "handle": b["handle"]}})
    gid = creado["blogCreate"]["blog"]["id"]
    print(f"  blog /{b['handle']} CREADO")
    return gid


def publicar(gid_blog: str, existentes: dict, art: dict, ensayo: bool) -> str:
    titulo_seo, descripcion_seo = art["meta"]
    campos = {
        "title": art["titulo"],
        "body": art["cuerpo"].strip(),
        "summary": art["resumen"],
        "tags": art["etiquetas"],
        "isPublished": True,
        "metafields": metacampos(titulo_seo, descripcion_seo),
    }
    viejo = existentes.get(art["handle"])
    if ensayo:
        return "actualizada (ensayo)" if viejo else "SE CREARÍA"
    if viejo:
        pedir(ACTUALIZAR_ARTICULO, {"id": viejo, "a": campos})
        return "actualizada"
    campos["blogId"] = gid_blog
    campos["handle"] = art["handle"]
    campos["author"] = {"name": AUTOR}
    pedir(CREAR_ARTICULO, {"a": campos})
    return "CREADA"


def main() -> None:
    ensayo = "--ensayo" in sys.argv

    malos = articulos.comprobar()
    if malos:
        print("\n  No se publica nada: hay textos fuera de medida.\n")
        for m in malos:
            print(f"    {m}")
        raise SystemExit(1)

    if not TIENDA or not TOKEN:
        raise SystemExit(
            "\n  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN en el entorno.\n"
            "  El token necesita el permiso write_content.\n")

    if "--esquema" in sys.argv:
        print(f"\n  Campos de entrada según la API {API}\n")
        esquema()
        return

    print(f"\n  {len(articulos.ARTICULOS)} artículos"
          f"{' · ENSAYO, no se escribe nada' if ensayo else ''}\n")

    gid = blog(ensayo)
    existentes = {}
    if not gid.startswith("gid://ensayo"):
        existentes = {n["handle"]: n["id"] for n in
                      pedir(BUSCAR_ARTICULOS, {"id": gid})
                      ["blog"]["articles"]["nodes"]}

    for art in articulos.ARTICULOS:
        estado = publicar(gid, existentes, art, ensayo)
        print(f"    /{art['handle']:42} {estado}")
    print()


if __name__ == "__main__":
    main()
