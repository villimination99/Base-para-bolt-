#!/usr/bin/env python3
"""
VILLUMINATIONS — Preguntas frecuentes
======================================
La página que contesta lo que frena una compra, en las tres lenguas.

    python3 tienda/faq.py             # comprueba y enseña qué falta
    python3 tienda/faq.py --esquema   # el JSON-LD que gana el resultado rico
    python3 tienda/faq.py --publicar  # (con credenciales) la crea o actualiza

**Por qué esta página y no otro artículo.** Un artículo trae visitas; una página
de preguntas convierte las que ya han llegado. Quien está a punto de pagar tiene
tres o cuatro dudas concretas —en qué idioma viene, qué recibo, de dónde salen
las cifras, qué pasa si no me sirve— y si no las encuentra contestadas se va.
Además Google la puede enseñar desplegada en el resultado de búsqueda, que es
espacio gratis en una página donde compites por centímetros.

**Lo que este fichero se niega a publicar.** Hay preguntas cuya respuesta no
está en el repositorio ni en ningún sitio que yo pueda comprobar: si hay envío
a una zona, si la descarga llega, qué talla equivale a qué. Contestarlas «por
si acaso» sería inventar, y en una página de preguntas eso se paga en
devoluciones. Van en `PENDIENTES` con lo que hace falta para poder escribirlas,
y `comprobar()` no deja publicar ninguna hasta que su dato exista.
"""

import json
import os
import sys
import urllib.request

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")

MANGO = "preguntas"
LENGUAS = ("es", "en", "fr")

TITULO = {
    "es": "Preguntas frecuentes",
    "en": "Frequently asked questions",
    "fr": "Questions fréquentes",
}
MANGO_TRADUCIDO = {"en": "faq", "fr": "questions"}

META = {
    "es": ("Preguntas frecuentes | VILLUMINATIONS",
           "En qué idioma vienen los libros, qué recibes al comprar, de dónde "
           "salen las cifras y por qué aquí no se promete nada."),
    "en": ("Frequently asked questions | VILLUMINATIONS",
           "What language the books come in, what you get when you buy, where "
           "the figures come from and why nothing is promised here."),
    "fr": ("Questions fréquentes | VILLUMINATIONS",
           "En quelle langue viennent les livres, ce que vous recevez, d'où "
           "viennent les chiffres et pourquoi rien n'est promis ici."),
}

# ---------------------------------------------------------------------------
# Lo que se puede contestar hoy, porque está comprobado en el repositorio.
# ---------------------------------------------------------------------------
PREGUNTAS = [

("idiomas", {
 "es": ("¿En qué idioma vienen los libros y los planes?",
        "En los tres a la vez. Cada documento es <strong>un solo archivo con "
        "las ediciones en español, inglés y francés</strong>, con marcadores "
        "para saltar de una a otra. No hay que elegir lengua al comprar ni "
        "pagar dos veces por leerlo en otra."),
 "en": ("What language do the books and plans come in?",
        "All three at once. Each document is <strong>a single file with the "
        "Spanish, English and French editions</strong> inside, with bookmarks "
        "to jump between them. There is no language to choose when you buy, "
        "and no paying twice to read it in another."),
 "fr": ("En quelle langue viennent les livres et les programmes ?",
        "Dans les trois à la fois. Chaque document est <strong>un seul "
        "fichier contenant les éditions espagnole, anglaise et "
        "française</strong>, avec des signets pour passer de l'une à l'autre. "
        "Aucune langue à choisir à l'achat, et rien à payer deux fois."),
}),

("que-recibo", {
 "es": ("¿Qué recibo exactamente al comprar un documento?",
        "Un PDF con marcadores de navegación y su vocabulario al final. Los "
        "libros llevan <strong>láminas dibujadas para la edición</strong>, no "
        "imágenes de banco: se dibujaron con la misma geometría que las "
        "tablas del interior. Los planes traen además una versión preparada "
        "para imprimir, con los márgenes ya puestos."),
 "en": ("What exactly do I get when I buy a document?",
        "A PDF with navigation bookmarks and its glossary at the end. The "
        "books carry <strong>plates drawn for the edition</strong>, not stock "
        "images: they were drawn with the same geometry as the tables inside. "
        "The plans also come with a version prepared for printing, margins "
        "already set."),
 "fr": ("Que reçois-je exactement en achetant un document ?",
        "Un PDF avec des signets de navigation et son lexique à la fin. Les "
        "livres portent des <strong>planches dessinées pour l'édition</strong>, "
        "non des images de banque : elles ont été dessinées avec la même "
        "géométrie que les tableaux à l'intérieur. Les programmes ont en plus "
        "une version prête à imprimer, marges comprises."),
}),

("cifras", {
 "es": ("¿De dónde salen las cifras?",
        "De dos sitios distintos, y no se mezclan. Las tablas de nutrición, "
        "entrenamiento y descanso vienen de <strong>organismos públicos del "
        "Gobierno de los Estados Unidos</strong>, cuyas obras no están "
        "sujetas a derechos de autor conforme al 17 U.S.C. § 105: se pueden "
        "comprobar una por una. Los libros esotéricos se apoyan en la "
        "<strong>tradición común y el dominio público</strong>, que es otra "
        "cosa y se dice como tal."),
 "en": ("Where do the figures come from?",
        "From two different places, and they are not mixed. The nutrition, "
        "training and rest tables come from <strong>public bodies of the "
        "United States Government</strong>, whose works are not subject to "
        "copyright under 17 U.S.C. § 105: they can be checked one by one. The "
        "esoteric books rest on <strong>common tradition and the public "
        "domain</strong>, which is a different thing and is stated as such."),
 "fr": ("D'où viennent les chiffres ?",
        "De deux endroits distincts, et ils ne se mélangent pas. Les tableaux "
        "de nutrition, d'entraînement et de repos viennent d'<strong>organismes "
        "publics du gouvernement des États-Unis</strong>, dont les œuvres ne "
        "sont pas soumises au droit d'auteur en vertu du 17 U.S.C. § 105 : ils "
        "se vérifient un par un. Les livres ésotériques reposent sur la "
        "<strong>tradition commune et le domaine public</strong>, ce qui est "
        "autre chose et se dit comme tel."),
}),

("promesas", {
 "es": ("¿Prometéis algún resultado?",
        "No, y es deliberado. Ni los libros ni las fichas de los suplementos "
        "dicen lo que un producto hace por tu salud. Se dice <strong>qué "
        "lleva, cuánto y en qué formato</strong>. La diferencia no es de tono: "
        "un complemento alimenticio se vende sin autorización previa, así que "
        "la frase «está a la venta» no informa de si funciona. Quien te "
        "promete resultados te está vendiendo otra cosa."),
 "en": ("Do you promise any results?",
        "No, and that is deliberate. Neither the books nor the supplement "
        "listings say what a product does for your health. They say "
        "<strong>what it contains, how much and in what format</strong>. The "
        "difference is not one of tone: a food supplement goes on sale "
        "without prior authorisation, so «it is for sale» tells you nothing "
        "about whether it works. Anyone promising you results is selling you "
        "something else."),
 "fr": ("Promettez-vous des résultats ?",
        "Non, et c'est délibéré. Ni les livres ni les fiches des compléments "
        "ne disent ce qu'un produit fait pour votre santé. On dit <strong>ce "
        "qu'il contient, en quelle quantité et sous quelle forme</strong>. La "
        "différence n'est pas de ton : un complément alimentaire est mis en "
        "vente sans autorisation préalable, donc « c'est en vente » "
        "n'informe en rien sur son efficacité. Qui vous promet des résultats "
        "vous vend autre chose."),
}),

("medidas", {
 "es": ("¿Son fiables las medidas y las cargas del equipo?",
        "Publicamos <strong>solo lo que declara el fabricante</strong>, y "
        "nada más. Cuando su documentación se contradice a sí misma —pasa más "
        "de lo que parece— el dato no se publica y se dice que no está. Hay un "
        "banco en el catálogo cuya capacidad máxima no aparece por eso: el "
        "proveedor da cuatro cifras distintas para el mismo modelo. Si "
        "necesitas una en concreto, escríbenos y la confirmamos con él "
        "<em>antes</em> de que compres."),
 "en": ("Are the equipment measurements and load ratings reliable?",
        "We publish <strong>only what the manufacturer states</strong>, and "
        "nothing else. When their documentation contradicts itself — which "
        "happens more than you would think — the figure is not published and "
        "we say it is missing. There is a bench in the catalogue whose maximum "
        "capacity is absent for exactly that reason: the supplier gives four "
        "different numbers for the same model. If you need a specific one, "
        "write to us and we will confirm it with them <em>before</em> you buy."),
 "fr": ("Les dimensions et les charges de l'équipement sont-elles fiables ?",
        "Nous publions <strong>uniquement ce que déclare le fabricant</strong>, "
        "et rien d'autre. Quand sa documentation se contredit — cela arrive "
        "plus souvent qu'on ne croit — la donnée n'est pas publiée et nous le "
        "disons. Un banc du catalogue n'affiche pas sa charge maximale pour "
        "cette raison précise : le fournisseur donne quatre chiffres "
        "différents pour le même modèle. S'il vous en faut un, écrivez-nous et "
        "nous le confirmerons auprès de lui <em>avant</em> votre achat."),
}),

("suplementos", {
 "es": ("¿Los suplementos están aprobados por alguna autoridad?",
        "No, y conviene saber por qué. A diferencia de un medicamento, un "
        "complemento alimenticio <strong>no pasa por una autorización previa "
        "que verifique que hace lo que dice</strong>. El fabricante responde de "
        "que sea seguro y de que la etiqueta no engañe, y la autoridad actúa "
        "sobre todo después, si algo sale mal. Eso no los hace inútiles ni "
        "peligrosos: hace que haya que mirar la evidencia producto por "
        "producto, y eso está desarrollado en el Diario."),
 "en": ("Are the supplements approved by any authority?",
        "No, and it is worth knowing why. Unlike a medicine, a food "
        "supplement <strong>does not go through a prior authorisation that "
        "verifies it does what it says</strong>. The manufacturer is "
        "responsible for it being safe and for the label not misleading, and "
        "the authority acts mostly afterwards, if something goes wrong. That "
        "does not make them useless or dangerous: it means the evidence has "
        "to be looked at product by product, and that is set out in the "
        "Journal."),
 "fr": ("Les compléments sont-ils approuvés par une autorité ?",
        "Non, et il vaut la peine de savoir pourquoi. Contrairement à un "
        "médicament, un complément alimentaire <strong>ne passe pas par une "
        "autorisation préalable vérifiant qu'il fait ce qu'il annonce</strong>. "
        "Le fabricant répond de sa sécurité et de l'honnêteté de l'étiquette, "
        "et l'autorité intervient surtout après coup, si quelque chose tourne "
        "mal. Cela ne les rend ni inutiles ni dangereux : cela oblige à "
        "regarder les preuves produit par produit, ce qui est développé dans "
        "le Journal."),
}),

("errata", {
 "es": ("He encontrado un error en un documento. ¿Qué hago?",
        "Escríbenos y se corrige. Y se corrige de verdad: el texto no vive en "
        "el PDF sino en su fuente, así que <strong>el arreglo entra en el "
        "original y el documento se vuelve a componer entero</strong>, en las "
        "tres lenguas a la vez. No hay parches sobre un PDF. Si encuentras una "
        "cifra que no cuadra con su fuente, nos estás haciendo un favor."),
 "en": ("I found a mistake in a document. What do I do?",
        "Write to us and it gets corrected. And properly corrected: the text "
        "does not live in the PDF but in its source, so <strong>the fix goes "
        "into the original and the document is typeset again from "
        "scratch</strong>, in all three languages at once. There are no "
        "patches on top of a PDF. If you find a figure that does not match its "
        "source, you are doing us a favour."),
 "fr": ("J'ai trouvé une erreur dans un document. Que faire ?",
        "Écrivez-nous et elle sera corrigée. Et vraiment corrigée : le texte "
        "ne vit pas dans le PDF mais dans sa source, donc <strong>la "
        "correction entre dans l'original et le document est recomposé en "
        "entier</strong>, dans les trois langues à la fois. Aucun rustine sur "
        "un PDF. Si vous trouvez un chiffre qui ne correspond pas à sa source, "
        "vous nous rendez service."),
}),

("preguntar", {
 "es": ("Tengo una duda que no está aquí.",
        "Escríbenos desde <a href=\"/pages/contact\">Contacto</a> o responde a "
        "cualquiera de nuestros correos: <strong>los lee una persona</strong>. "
        "Si la duda es sobre una medida, una talla o si un documento cubre lo "
        "que buscas, pregunta antes de comprar; contestar eso es más barato "
        "para todos que una devolución."),
 "en": ("I have a question that is not here.",
        "Write to us from <a href=\"/pages/contact\">Contact</a> or reply to "
        "any of our emails: <strong>a person reads them</strong>. If it is "
        "about a measurement, a size or whether a document covers what you are "
        "after, ask before buying; answering that is cheaper for everyone than "
        "a return."),
 "fr": ("J'ai une question qui n'est pas ici.",
        "Écrivez-nous depuis <a href=\"/pages/contact\">Contact</a> ou "
        "répondez à l'un de nos courriels : <strong>une personne les "
        "lit</strong>. Si cela concerne une dimension, une taille ou si un "
        "document couvre ce que vous cherchez, demandez avant d'acheter ; y "
        "répondre coûte moins cher à tout le monde qu'un retour."),
}),
]

# ---------------------------------------------------------------------------
# Lo que NO se puede contestar todavía. Cada una dice qué hace falta.
# ---------------------------------------------------------------------------
PENDIENTES = {
    "descarga": (
        "¿Cómo recibo el documento después de pagar?",
        "Hoy no llega: no hay app de descargas instalada, así que once "
        "productos cobran y no entregan archivo. Contestar esta pregunta "
        "antes de instalarla sería prometer algo que no ocurre."),
    "envio": (
        "¿Hacéis envíos a mi zona y cuánto tardan?",
        "No he podido comprobar por API qué zonas de envío hay configuradas. "
        "`python3 tienda/despegue.py` lo dice en un comando."),
    "devolucion": (
        "¿Puedo devolver un producto?",
        "La política actual niega remedio incluso para producto defectuoso o "
        "no entregado, lo que en Quebec es dudoso que se sostenga. Repetirla "
        "aquí sería amplificar el problema. Hay que arreglarla primero en el "
        "panel."),
    "tallas": (
        "¿Qué talla elijo?",
        "Hace falta la tabla de medidas del proveedor de cada prenda. "
        "Inventar equivalencias de talla es la primera causa de devolución "
        "en ropa."),
}

PROHIBIDAS = ("cura", "mejora tu salud", "quema grasa", "garantizado",
              "milagro", "boost", "burns fat", "guaranteed", "miracle",
              "brûle les graisses", "garanti", "miracle")


def comprobar() -> list:
    malos = []
    vistos = set()
    for clave, versiones in PREGUNTAS:
        if clave in vistos:
            malos.append(f"{clave} · repetida")
        vistos.add(clave)
        if clave in PENDIENTES:
            malos.append(f"{clave} · está en PENDIENTES y no se puede "
                         f"publicar: {PENDIENTES[clave][1]}")
        for lengua in LENGUAS:
            if lengua not in versiones:
                malos.append(f"{clave} · falta la versión en {lengua}")
                continue
            pregunta, respuesta = versiones[lengua]
            if not pregunta.strip() or not respuesta.strip():
                malos.append(f"{clave}/{lengua} · vacía")
            texto = (pregunta + " " + respuesta).lower()
            for frase in PROHIBIDAS:
                if frase in texto:
                    malos.append(f"{clave}/{lengua} · promesa: «{frase}»")
            for mal in ("VIllumination", "Villuminations"):
                if mal in pregunta + respuesta:
                    malos.append(f"{clave}/{lengua} · marca mal escrita")
    for lengua in LENGUAS:
        t, d = META[lengua]
        if len(t) > 60:
            malos.append(f"meta/{lengua} · título {len(t)}/60")
        if len(d) > 155:
            malos.append(f"meta/{lengua} · descripción {len(d)}/155")
    return malos


def cuerpo(lengua: str, con_esquema: bool = True) -> str:
    """El HTML de la página, en la lengua que toque.

    Lleva pegado su JSON-LD, que es lo que permite que el buscador enseñe las
    preguntas desplegadas debajo del resultado. Va dentro del cuerpo y no en
    el tema porque **Shopify sí conserva `<script>` en el cuerpo de una
    página**: la prueba es VI.P, cuyo cuerpo lleva 337 KB de JavaScript
    publicado por la misma vía. Aquí se creyó lo contrario y por eso el
    esquema estuvo escrito sin usarse.

    Ponerlo en el cuerpo tiene además una ventaja: viaja con la traducción.
    El esquema francés se registra como parte del `body_html` francés, sin
    tocar el tema ni depender de que alguien se acuerde.
    """
    intro = {
        "es": "<p>Lo que más se pregunta antes de comprar. Si tu duda no está, "
              "escríbenos: contestar antes es más barato que devolver "
              "después.</p>",
        "en": "<p>What gets asked most before buying. If your question is not "
              "here, write to us: answering beforehand is cheaper than "
              "returning afterwards.</p>",
        "fr": "<p>Ce qu'on demande le plus avant d'acheter. Si votre question "
              "n'y est pas, écrivez-nous : répondre avant coûte moins cher "
              "que retourner après.</p>",
    }[lengua]
    trozos = [intro]
    for _, versiones in PREGUNTAS:
        pregunta, respuesta = versiones[lengua]
        trozos.append(f"<h2>{pregunta}</h2>\n<p>{respuesta}</p>")
    if con_esquema:
        trozos.append(esquema(lengua))
    return "\n\n".join(trozos)


def esquema(lengua: str = "es") -> str:
    """El JSON-LD de tipo FAQPage.

    Solo cuenta lo que se publica: si una pregunta está en `PENDIENTES`
    —porque hoy no se puede contestar sin prometer algo que no ocurre— no
    entra aquí tampoco. Un FAQPage que anuncia una respuesta que la página no
    tiene es marcado que no coincide con el contenido, y eso Google lo trata
    como spam de datos estructurados.
    """
    import re
    limpiar = lambda h: re.sub(r"<[^>]+>", "", h)
    datos = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question",
             "name": limpiar(versiones[lengua][0]),
             "acceptedAnswer": {"@type": "Answer",
                                "text": limpiar(versiones[lengua][1])}}
            for _, versiones in PREGUNTAS
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(datos, ensure_ascii=False, indent=2)
            + "\n</script>")


def pedir(consulta: str, variables: dict) -> dict:
    cuerpo_ = json.dumps({"query": consulta, "variables": variables}).encode()
    peticion = urllib.request.Request(
        f"https://{TIENDA}/admin/api/{API}/graphql.json", data=cuerpo_,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": TOKEN})
    with urllib.request.urlopen(peticion) as r:
        datos = json.loads(r.read())
    if "errors" in datos:
        raise SystemExit(f"  GraphQL: {datos['errors']}")
    for bloque in datos.get("data", {}).values():
        if isinstance(bloque, dict) and bloque.get("userErrors"):
            raise SystemExit(f"  Shopify: {bloque['userErrors']}")
    return datos["data"]


if __name__ == "__main__":
    malos = comprobar()
    print(f"\n  {len(PREGUNTAS)} preguntas × {len(LENGUAS)} lenguas · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")

    if "--esquema" in sys.argv:
        print(esquema("es"))
        raise SystemExit(0)

    for clave, versiones in PREGUNTAS:
        print(f"    {clave:14} {versiones['es'][0]}")
    print(f"\n  {len(PENDIENTES)} preguntas que NO se pueden contestar aún:\n")
    for clave, (pregunta, porque) in PENDIENTES.items():
        print(f"    {clave}")
        print(f"      {pregunta}")
        print(f"      → {porque}\n")
