# -*- coding: utf-8 -*-
"""
VILLUMINATIONS — Metadatos de buscador
--------------------------------------
Título y descripción de buscador de cada ficha, en las tres lenguas, más el
texto alternativo de la portada y las etiquetas de cada producto.

Vive aparte de las descripciones por una razón práctica: son campos con límite
duro y conviene poder medirlos todos de una pasada. Google recorta el título
alrededor de los 60 caracteres y la descripción alrededor de los 155; lo que
pase de ahí no es que se penalice, es que no se lee. comprobar() mide los
sesenta y seis textos y se niega a pasar si alguno se sale, que es más fiable
que contar a ojo.

Qué lleva cada uno, y por qué:

· El título repite el nombre del producto, añade en qué consiste y cierra con
  la marca. Nada de «comprar», «barato» ni «el mejor»: eso no lo busca nadie
  y ensucia la línea que sí se lee.

· La descripción da las cifras del producto —páginas, láminas, capítulos— y
  las tres lenguas. Son datos verificables y son exactamente lo que decide una
  compra de un PDF de referencia: cuánto hay dentro y en qué idioma.

· El texto alternativo describe la imagen para quien no la ve y para el
  buscador de imágenes. Es distinto en cada ficha, así que además sirve de
  marca para no subir la portada dos veces.

Las cifras de aquí tienen que coincidir con las de descripciones.py, y ambas
con las de los PDF. comprobar() no puede verificar eso —son frases, no
tablas—, así que si un libro crece hay que tocar los dos sitios.
"""

# handle -> {idioma: (título de buscador, descripción de buscador)}
META = {
    "basico-volumen-limpio": {
        "es": ("Básico · Volumen Limpio — guía en PDF | VILLUMINATIONS",
               "Guía rápida de volumen limpio en PDF: el punto de partida, "
               "cuánto superávit tiene sentido y qué se mide cada semana. En "
               "español, inglés y francés."),
        "en": ("Basic · Clean Bulk — PDF guide | VILLUMINATIONS",
               "Quick clean-bulk guide in PDF: the starting point, how much of "
               "a surplus makes sense and what to measure each week. In "
               "English, Spanish and French."),
        "fr": ("Basique · Prise de masse propre — PDF | VILLUMINATIONS",
               "Guide rapide de prise de masse propre en PDF : le point de "
               "départ, le surplus utile et ce que l'on mesure chaque "
               "semaine. En trois langues."),
    },
    "pro-definicion-volumen": {
        "es": ("Pro · Definición + Volumen — 5 PDF | VILLUMINATIONS",
               "Cinco documentos para un ciclo completo: ciclado de "
               "carbohidratos, suplementación, plan de ocho semanas y registro "
               "de progreso. En tres idiomas."),
        "en": ("Pro · Cutting + Bulking — 5 PDFs | VILLUMINATIONS",
               "Five documents for a full cycle: carbohydrate cycling, "
               "supplementation, an eight-week plan and a weekly progress "
               "record. In English, Spanish and French."),
        "fr": ("Pro · Sèche + Prise de masse — 5 PDF | VILLUMINATIONS",
               "Cinq documents pour un cycle complet : cyclage des glucides, "
               "supplémentation, plan de huit semaines et relevé de "
               "progression. En trois langues."),
    },
    "elite-todo-incluido-coaching": {
        "es": ("Elite · Todo Incluido + Coaching — 11 PDF | VILLUMINATIONS",
               "Los once documentos del catálogo: alimentación, entrenamiento, "
               "HIIT, sueño, meditación y coaching semanal. Treinta y tres PDF "
               "en español, inglés y francés."),
        "en": ("Elite · Everything Included — 11 PDFs | VILLUMINATIONS",
               "All eleven documents: food, training, HIIT, sleep, meditation "
               "and weekly coaching. Thirty-three PDFs in English, Spanish and "
               "French."),
        "fr": ("Elite · Tout inclus + Coaching — 11 PDF | VILLUMINATIONS",
               "Les onze documents : alimentation, entraînement, HIIT, "
               "sommeil, méditation et coaching hebdomadaire. Trente-trois PDF "
               "en français, espagnol et anglais."),
    },
    "codice-zodiacal": {
        "es": ("Códice Zodiacal — los doce signos en PDF | VILLUMINATIONS",
               "144 páginas, 31 capítulos y 10 láminas: decanatos, dignidades, "
               "términos egipcios y un programa de doce meses. En español, "
               "inglés y francés."),
        "en": ("Zodiacal Codex — the twelve signs in PDF | VILLUMINATIONS",
               "145 pages, 31 chapters and 10 plates: decans, dignities, "
               "Egyptian terms and a twelve-month programme. In English, "
               "Spanish and French."),
        "fr": ("Codex Zodiacal — les douze signes en PDF | VILLUMINATIONS",
               "149 pages, 31 chapitres et 10 planches : décans, dignités, "
               "termes égyptiens et un programme de douze mois. En français, "
               "espagnol et anglais."),
    },
    "codice-de-las-invocaciones": {
        "es": ("Códice de las Invocaciones — rito diario | VILLUMINATIONS",
               "88 páginas, 25 capítulos y 8 láminas: el círculo, las cuatro "
               "armas, el rito diario y el diario de práctica. En español, "
               "inglés y francés."),
        "en": ("Codex of Invocations — ritual practice | VILLUMINATIONS",
               "91 pages, 25 chapters and 8 plates: the circle, the four "
               "weapons, the daily rite and the practice journal. In English, "
               "Spanish and French."),
        "fr": ("Codex des Invocations — pratique rituelle | VILLUMINATIONS",
               "92 pages, 25 chapitres et 8 planches : le cercle, les quatre "
               "armes, le rite quotidien et le journal de pratique. En trois "
               "langues."),
    },
    "codice-de-la-mesa": {
        "es": ("Códice de la Mesa — nutrición en PDF | VILLUMINATIONS",
               "78 páginas y 7 láminas: macronutrientes, diecinueve "
               "micronutrientes con sus dos columnas, etiquetas y seguridad "
               "alimentaria. En tres idiomas."),
        "en": ("Codex of the Table — nutrition reference | VILLUMINATIONS",
               "76 pages and 7 plates: macronutrients, nineteen micronutrients "
               "with both columns, labels and food safety. In English, Spanish "
               "and French."),
        "fr": ("Codex de la Table — nutrition de référence | VILLUMINATIONS",
               "80 pages et 7 planches : macronutriments, dix-neuf "
               "micronutriments avec leurs deux colonnes, étiquettes et "
               "sécurité alimentaire."),
    },
    "codice-de-la-carga": {
        "es": ("Códice de la Carga — entrenamiento en PDF | VILLUMINATIONS",
               "70 páginas y 7 láminas: la dosis de actividad, los ocho "
               "patrones, la ecuación del NIOSH y cómo comprobarlo tú mismo. "
               "En tres idiomas."),
        "en": ("Codex of the Load — training reference | VILLUMINATIONS",
               "70 pages and 7 plates: the dose of activity, the eight "
               "patterns, the NIOSH lifting equation and how to check it "
               "yourself. In three languages."),
        "fr": ("Codex de la Charge — entraînement en PDF | VILLUMINATIONS",
               "73 pages et 7 planches : la dose d'activité, les huit schémas, "
               "l'équation du NIOSH et comment le vérifier soi-même. En trois "
               "langues."),
    },
    "codice-del-descanso": {
        "es": ("Códice del Descanso — higiene del sueño | VILLUMINATIONS",
               "53 páginas y 6 láminas: la arquitectura de una noche, la deuda "
               "de sueño, la siesta bien hecha y los turnos. En español, "
               "inglés y francés."),
        "en": ("Codex of Rest — sleep hygiene in PDF | VILLUMINATIONS",
               "52 pages and 6 plates: the architecture of a night, sleep "
               "debt, the nap done properly and shift work. In English, "
               "Spanish and French."),
        "fr": ("Codex du Repos — hygiène du sommeil | VILLUMINATIONS",
               "55 pages et 6 planches : l'architecture d'une nuit, la dette "
               "de sommeil, la sieste bien faite et le travail posté. En trois "
               "langues."),
    },
    "codice-de-la-voluntad": {
        "es": ("Códice de la Voluntad — adherencia en PDF | VILLUMINATIONS",
               "56 páginas y 5 láminas: por qué se abandona un plan correcto, "
               "el bucle del hábito y cómo volver después de meses. En tres "
               "idiomas."),
        "en": ("Codex of the Will — adherence and habit | VILLUMINATIONS",
               "55 pages and 5 plates: why a correct plan gets abandoned, the "
               "habit loop and how to come back after months away. In three "
               "languages."),
        "fr": ("Codex de la Volonté — adhésion et habitude | VILLUMINATIONS",
               "59 pages et 5 planches : pourquoi un bon plan est abandonné, "
               "la boucle de l'habitude et comment revenir après des mois. En "
               "trois langues."),
    },
    "codice-de-los-arcanos": {
        "es": ("Códice de los Arcanos — tarot en PDF | VILLUMINATIONS",
               "62 páginas y 5 láminas: los veintidós mayores, los cuatro "
               "palos, los treinta y seis decanatos y las tiradas. En español, "
               "inglés y francés."),
        "en": ("Codex of the Arcana — tarot in PDF | VILLUMINATIONS",
               "67 pages and 5 plates: the twenty-two major arcana, the four "
               "suits, the thirty-six decans and the spreads. In English, "
               "Spanish and French."),
        "fr": ("Codex des Arcanes — tarot en PDF | VILLUMINATIONS",
               "64 pages et 5 planches : les vingt-deux majeurs, les quatre "
               "couleurs, les trente-six décans et les tirages. En trois "
               "langues."),
    },
    "codice-del-si-mismo": {
        "es": ("Códice del Sí Mismo — observación interior | VILLUMINATIONS",
               "77 páginas y 7 láminas: la atención dividida, los tres "
               "centros, el inventario nocturno y un año de observación. En "
               "tres idiomas."),
        "en": ("Codex of the Self — inner observation | VILLUMINATIONS",
               "81 pages and 7 plates: divided attention, the three centres, "
               "the nightly inventory and a year of observation. In three "
               "languages."),
        "fr": ("Codex du Soi — observation intérieure | VILLUMINATIONS",
               "82 pages et 7 planches : l'attention divisée, les trois "
               "centres, l'inventaire du soir et une année d'observation."),
    },
}

# handle -> {idioma: texto alternativo de la portada}
ALT = {
    "basico-volumen-limpio": {
        "es": "Portada del plan Básico · Volumen Limpio de VILLUMINATIONS",
        "en": "Cover of the Basic · Clean Bulk plan by VILLUMINATIONS",
        "fr": "Couverture du plan Basique · Prise de masse propre de VILLUMINATIONS",
    },
    "pro-definicion-volumen": {
        "es": "Portada del plan Pro · Definición + Volumen de VILLUMINATIONS",
        "en": "Cover of the Pro · Cutting + Bulking plan by VILLUMINATIONS",
        "fr": "Couverture du plan Pro · Sèche + Prise de masse de VILLUMINATIONS",
    },
    "elite-todo-incluido-coaching": {
        "es": "Portada del plan Elite · Todo Incluido + Coaching de VILLUMINATIONS",
        "en": "Cover of the Elite · Everything Included + Coaching plan by VILLUMINATIONS",
        "fr": "Couverture du plan Elite · Tout inclus + Coaching de VILLUMINATIONS",
    },
    "codice-zodiacal": {
        "es": "Cubierta del Códice Zodiacal, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Zodiacal Codex, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex Zodiacal, livre en PDF de VILLUMINATIONS",
    },
    "codice-de-las-invocaciones": {
        "es": "Cubierta del Códice de las Invocaciones, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of Invocations, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex des Invocations, livre en PDF de VILLUMINATIONS",
    },
    "codice-de-la-mesa": {
        "es": "Cubierta del Códice de la Mesa, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of the Table, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex de la Table, livre en PDF de VILLUMINATIONS",
    },
    "codice-de-la-carga": {
        "es": "Cubierta del Códice de la Carga, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of the Load, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex de la Charge, livre en PDF de VILLUMINATIONS",
    },
    "codice-del-descanso": {
        "es": "Cubierta del Códice del Descanso, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of Rest, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex du Repos, livre en PDF de VILLUMINATIONS",
    },
    "codice-de-la-voluntad": {
        "es": "Cubierta del Códice de la Voluntad, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of the Will, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex de la Volonté, livre en PDF de VILLUMINATIONS",
    },
    "codice-de-los-arcanos": {
        "es": "Cubierta del Códice de los Arcanos, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of the Arcana, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex des Arcanes, livre en PDF de VILLUMINATIONS",
    },
    "codice-del-si-mismo": {
        "es": "Cubierta del Códice del Sí Mismo, libro en PDF de VILLUMINATIONS",
        "en": "Cover of the Codex of the Self, a PDF book by VILLUMINATIONS",
        "fr": "Couverture du Codex du Soi, livre en PDF de VILLUMINATIONS",
    },
}

# Etiquetas de tienda. No son SEO de buscador —Shopify no las publica— pero
# son lo que hace que el filtro lateral y el buscador interno encuentren algo.
ETIQUETAS = {
    "basico-volumen-limpio": ["planes", "nutrición", "volumen"],
    "pro-definicion-volumen": ["planes", "nutrición", "definición", "volumen"],
    "elite-todo-incluido-coaching": ["planes", "nutrición", "entrenamiento",
                                     "sueño", "meditación", "coaching"],
    "codice-zodiacal": ["códices", "astrología", "zodiaco", "simbolismo"],
    "codice-de-las-invocaciones": ["códices", "ritual", "simbolismo",
                                   "práctica"],
    "codice-de-la-mesa": ["códices", "nutrición", "referencia"],
    "codice-de-la-carga": ["códices", "entrenamiento", "referencia"],
    "codice-del-descanso": ["códices", "sueño", "recuperación"],
    "codice-de-la-voluntad": ["códices", "hábito", "adherencia"],
    "codice-de-los-arcanos": ["códices", "tarot", "simbolismo"],
    "codice-del-si-mismo": ["códices", "atención", "práctica"],
}

# Etiquetas comunes a todo: dicen lo que el producto ES, y son las que hacen
# falta para que un filtro de «descarga digital» o de idioma funcione.
COMUNES = ["descarga digital", "PDF", "trilingüe"]

TOPE_TITULO = 60
TOPE_DESCRIPCION = 155
TOPE_ALT = 125          # Shopify corta el alt en 512, pero los lectores de
                        # pantalla y el buscador de imágenes se quedan antes


def comprobar() -> list[str]:
    """Mide los textos y devuelve los que se pasan de largo.

    Se llama desde publicar.py antes de tocar la tienda. Un título recortado
    no rompe nada visible —por eso se cuela— y por eso conviene que lo mida
    una máquina y no la paciencia de quien revisa.
    """
    fallos = []
    for handle, idiomas in META.items():
        for idioma, (titulo, descripcion) in idiomas.items():
            if len(titulo) > TOPE_TITULO:
                fallos.append(f"{handle} [{idioma}] título {len(titulo)} > "
                              f"{TOPE_TITULO}: «{titulo}»")
            if len(descripcion) > TOPE_DESCRIPCION:
                fallos.append(f"{handle} [{idioma}] descripción "
                              f"{len(descripcion)} > {TOPE_DESCRIPCION}")
    for handle, idiomas in ALT.items():
        for idioma, texto in idiomas.items():
            if len(texto) > TOPE_ALT:
                fallos.append(f"{handle} [{idioma}] alt {len(texto)} > {TOPE_ALT}")
    return fallos


if __name__ == "__main__":
    problemas = comprobar()
    print()
    for p in problemas:
        print("  ", p)
    print(f"  {len(META) * 3} títulos y descripciones · "
          f"{len(ALT) * 3} textos alternativos · "
          f"{len(problemas)} fuera de medida\n")
