#!/usr/bin/env python3
"""
VILLUMINATIONS — Menús de la tienda
------------------------------------
La navegación entera, en un sitio, con sus traducciones.

    python3 tienda/menus.py                # comprueba la estructura
    python3 tienda/menus.py --ensayo       # qué se enviaría
    python3 tienda/menus.py                # (con credenciales) lo publica

**Por qué existe este fichero.** Los menús se montaron una vez escribiendo la
mutación a mano. Eso significa que la navegación de la tienda —lo primero que
ve cualquier visita— no estaba en ninguna parte del repositorio: si alguien la
tocaba en el panel, o si el tema la reiniciaba, no había con qué compararla.
Ahora sí.

Dos cosas de la API que se pagaron con un intento fallido cada una:

· `menuUpdate` pide **`MenuItemUpdateInput`** y `menuCreate` pide
  **`MenuItemCreateInput`**. No comparten tipo, igual que los productos.

· Al reescribir un menú, **los enlaces se crean de nuevo y cambian de
  identificador**. Las traducciones viejas se quedan colgando de enlaces que ya
  no existen, así que hay que volver a registrarlas después de cada pasada.
  Este publicador lo hace en el mismo comando, emparejando por el título
  castellano.

Un enlace a una colección vacía es peor que no tener el enlace: manda a la
visita a una página que dice «no hay productos». Por eso `cuidado-personal` no
está abajo — los dos jabones siguen sin publicar. Cuando se activen, se quita
el comentario de una línea.
"""

import json
import os
import sys
import urllib.request

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

# Identificadores de la tienda. Son estables: una colección no cambia de id.
COLECCION = {
    "suplementos": "gid://shopify/Collection/275576553521",
    "ropa": "gid://shopify/Collection/275576717361",
    "equipo": "gid://shopify/Collection/275576750129",
    "conocimiento": "gid://shopify/Collection/275588186161",
    "planes": "gid://shopify/Collection/276253900849",
    "cuidado-personal": "gid://shopify/Collection/276260618289",
}
PAGINA = {
    "contact": "gid://shopify/Page/93763698737",
    "data-sharing-opt-out": "gid://shopify/Page/93968793649",
    "vi-p": "gid://shopify/Page/94354800689",
    "como-se-hace": "gid://shopify/Page/94564122673",
}
BLOG_DIARIO = "gid://shopify/Blog/82382913585"
POLITICA = {
    "privacidad": "gid://shopify/ShopPolicy/28292841521",
    "reembolso": "gid://shopify/ShopPolicy/28637626417",
    "condiciones": "gid://shopify/ShopPolicy/28637659185",
    "envios": "gid://shopify/ShopPolicy/28637724721",
    "aviso-legal": "gid://shopify/ShopPolicy/28637757489",
}

MENUS = {
    "main-menu": {
        "id": "gid://shopify/Menu/197156110385",
        "titulo": "Menú principal",
        "entradas": [
            ("Inicio", "FRONTPAGE", None, []),
            ("Libros y planes", "COLLECTION", COLECCION["conocimiento"], [
                ("Libros", "COLLECTION", COLECCION["conocimiento"]),
                ("Planes de entrenamiento", "COLLECTION", COLECCION["planes"]),
            ]),
            ("Suplementos", "COLLECTION", COLECCION["suplementos"], []),
            ("Equipo", "COLLECTION", COLECCION["equipo"], []),
            ("Ropa", "COLLECTION", COLECCION["ropa"], []),
            # El desplegable que faltaba: la misma forma que «Libros y planes»,
            # con todo el catálogo a la vista sin tener que entrar.
            ("Todo el catálogo", "COLLECTIONS", None, [
                ("Suplementos", "COLLECTION", COLECCION["suplementos"]),
                ("Equipo", "COLLECTION", COLECCION["equipo"]),
                ("Ropa", "COLLECTION", COLECCION["ropa"]),
                ("Libros", "COLLECTION", COLECCION["conocimiento"]),
                ("Planes de entrenamiento", "COLLECTION", COLECCION["planes"]),
                # ("Cuidado personal", "COLLECTION",
                #  COLECCION["cuidado-personal"]),   ← cuando se publiquen
            ]),
            ("Diario", "BLOG", BLOG_DIARIO, []),
            ("VI.P", "PAGE", PAGINA["vi-p"], []),
        ],
    },
    "footer": {
        "id": "gid://shopify/Menu/197156143153",
        "titulo": "Menú del pie de página",
        "entradas": [
            ("Cómo se hace lo que vendemos", "PAGE", PAGINA["como-se-hace"], []),
            ("Diario", "BLOG", BLOG_DIARIO, []),
            ("Contacto", "PAGE", PAGINA["contact"], []),
            ("Buscar", "SEARCH", None, []),
            ("Política de privacidad", "SHOP_POLICY", POLITICA["privacidad"], []),
            ("Política de reembolso", "SHOP_POLICY", POLITICA["reembolso"], []),
            ("Condiciones del servicio", "SHOP_POLICY", POLITICA["condiciones"], []),
            ("Envíos", "SHOP_POLICY", POLITICA["envios"], []),
            ("Aviso legal", "SHOP_POLICY", POLITICA["aviso-legal"], []),
            ("Tus opciones de privacidad", "PAGE",
             PAGINA["data-sharing-opt-out"], []),
        ],
    },
}

# Título castellano -> (inglés, francés). Un enlace repetido comparte
# traducción, que es justo lo que se quiere.
TRADUCCION = {
    "Inicio": ("Home", "Accueil"),
    "Libros y planes": ("Books and plans", "Livres et programmes"),
    "Libros": ("Books", "Livres"),
    "Planes de entrenamiento": ("Training plans", "Programmes d'entraînement"),
    "Suplementos": ("Supplements", "Compléments"),
    "Equipo": ("Equipment", "Équipement"),
    "Ropa": ("Apparel", "Vêtements"),
    "Cuidado personal": ("Personal care", "Soins du corps"),
    "Todo el catálogo": ("Everything", "Tout le catalogue"),
    "Diario": ("Journal", "Journal"),
    "VI.P": ("VI.P", "VI.P"),
    "Cómo se hace lo que vendemos": (
        "How we make what we sell",
        "Comment nous fabriquons ce que nous vendons"),
    "Contacto": ("Contact", "Contact"),
    "Buscar": ("Search", "Recherche"),
    "Política de privacidad": ("Privacy policy", "Politique de confidentialité"),
    "Política de reembolso": ("Refund policy", "Politique de remboursement"),
    "Condiciones del servicio": ("Terms of service", "Conditions d'utilisation"),
    "Envíos": ("Shipping", "Expédition"),
    "Aviso legal": ("Legal notice", "Mentions légales"),
    "Tus opciones de privacidad": ("Your privacy choices",
                                   "Vos choix de confidentialité"),
}

# Colecciones que hoy no tienen ni un producto visible. Enlazarlas manda a la
# visita a una página que dice «no hay productos».
VACIAS = {"cuidado-personal"}


# ---------------------------------------------------------------------------
def titulos(menu: dict) -> list:
    """Todos los títulos del menú, incluidos los anidados."""
    salida = []
    for titulo, _, _, hijos in menu["entradas"]:
        salida.append(titulo)
        salida += [h[0] for h in hijos]
    return salida


def comprobar() -> list:
    malos = []
    invertido = {v: k for k, v in COLECCION.items()}
    for nombre, menu in MENUS.items():
        vistos = titulos(menu)
        for titulo in vistos:
            if titulo not in TRADUCCION:
                malos.append(f"{nombre} · «{titulo}» sin traducción")
        for titulo, tipo, recurso, hijos in menu["entradas"]:
            for t, tp, r in [(titulo, tipo, recurso)] + list(hijos):
                if tp == "COLLECTION" and invertido.get(r) in VACIAS:
                    malos.append(f"{nombre} · «{t}» apunta a una colección "
                                 f"sin productos visibles")
                if tp in ("COLLECTION", "PAGE", "BLOG", "SHOP_POLICY") and not r:
                    malos.append(f"{nombre} · «{t}» es de tipo {tp} y no "
                                 f"lleva recurso")
        # La cabecera se lee de un vistazo y compite por el ancho de la
        # pantalla; el pie no. Diez enlaces arriba son ilegibles y diez abajo
        # son lo normal, así que la medida solo aplica a la cabecera.
        if nombre == "main-menu" and len(menu["entradas"]) > 9:
            malos.append(f"{nombre} · {len(menu['entradas'])} entradas de "
                         f"primer nivel; por encima de nueve no se leen")
    return malos


def entradas(menu: dict) -> list:
    """La estructura tal como la quiere MenuItemUpdateInput."""
    salida = []
    for titulo, tipo, recurso, hijos in menu["entradas"]:
        item = {"title": titulo, "type": tipo}
        if recurso:
            item["resourceId"] = recurso
        if hijos:
            item["items"] = [
                {"title": t, "type": tp, **({"resourceId": r} if r else {})}
                for t, tp, r in hijos]
        salida.append(item)
    return salida


# ---------------------------------------------------------------------------
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


ESCRIBIR = """
mutation($id: ID!, $titulo: String!, $mango: String, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $titulo, handle: $mango, items: $items) {
    menu { id items { title items { title } } }
    userErrors { field message }
  }
}"""

ENLACES = """
query {
  translatableResources(first: 100, resourceType: LINK) {
    nodes { resourceId translatableContent { key value digest } }
  }
}"""

TRADUCIR = """
mutation($id: ID!, $t: [TranslationInput!]!) {
  translationsRegister(resourceId: $id, translations: $t) {
    userErrors { field message }
  }
}"""


def publicar(ensayo: bool) -> int:
    for mango, menu in MENUS.items():
        if ensayo:
            print(f"    ~~ {mango}: {len(menu['entradas'])} entradas, "
                  f"{len(titulos(menu))} enlaces en total")
            continue
        pedir(ESCRIBIR, {"id": menu["id"], "titulo": menu["titulo"],
                         "mango": mango, "items": entradas(menu)})
        print(f"    ok {mango}")

    if ensayo:
        print(f"    ~~ y {len(TRADUCCION)} títulos por traducir, "
              f"después de reescribir los menús")
        return 0

    # Los enlaces se han creado de nuevo: hay que volver a pedirlos.
    hechos = 0
    for nodo in pedir(ENLACES, {})["translatableResources"]["nodes"]:
        contenido = {c["key"]: c for c in nodo["translatableContent"]}
        if "title" not in contenido:
            continue
        castellano = contenido["title"]["value"]
        if castellano not in TRADUCCION:
            continue
        en, fr = TRADUCCION[castellano]
        digest = contenido["title"]["digest"]
        pedir(TRADUCIR, {"id": nodo["resourceId"], "t": [
            {"locale": "en", "key": "title", "value": en,
             "translatableContentDigest": digest},
            {"locale": "fr", "key": "title", "value": fr,
             "translatableContentDigest": digest},
        ]})
        hechos += 1
    print(f"    ok {hechos} enlaces traducidos")
    return 0


if __name__ == "__main__":
    ensayo = "--ensayo" in sys.argv
    malos = comprobar()
    print(f"\n  {len(MENUS)} menús · "
          f"{sum(len(titulos(m)) for m in MENUS.values())} enlaces · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if malos:
        raise SystemExit(1)

    if not (TIENDA and TOKEN):
        for mango, menu in MENUS.items():
            print(f"    {mango}")
            for titulo, _, _, hijos in menu["entradas"]:
                print(f"      {titulo}")
                for h in hijos:
                    print(f"        · {h[0]}")
        print("\n  Sin credenciales. Con SHOPIFY_TIENDA y SHOPIFY_TOKEN "
              "esto se publica.\n")
        raise SystemExit(0)

    raise SystemExit(publicar(ensayo))
