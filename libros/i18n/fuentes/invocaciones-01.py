# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · cuadrados, cubierta, créditos e índice
===================================================================
Las sumas de los cuadrados planetarios —15, 34, 65, 111— y la división de las
horas —24 ÷ 7 = 3 y sobran 3— van con sus cifras intactas en los tres idiomas.
Son operaciones que el generador comprueba antes de escribir y que el lector
puede rehacer mirando la lámina.

La suma de los veintidós valores, 1 495, es la misma cifra que ya aparece en
el libro de los arcanos: los dos libros la comprueban por separado y tienen
que coincidir. Solo cambia el separador de millares.
"""

T = {
    "4×4 · SUMA 34": {"en": "4×4 · SUM 34", "fr": "4×4 · SOMME 34"},
    "5×5 · SUMA 65": {"en": "5×5 · SUM 65", "fr": "5×5 · SOMME 65"},
    "SOL": {"en": "SUN", "fr": "SOLEIL"},
    "6×6 · SUMA 111": {"en": "6×6 · SUM 111", "fr": "6×6 · SOMME 111"},

    "CADA FILA, CADA COLUMNA Y CADA DIAGONAL SUMAN LO MISMO": {
        "en": "EVERY ROW, EVERY COLUMN AND EVERY DIAGONAL ADD UP THE SAME",
        "fr": "CHAQUE LIGNE, CHAQUE COLONNE ET CHAQUE DIAGONALE FONT AUTANT"},

    "HORA DEL DÍA · 1 AL AMANECER · 13 AL ATARDECER": {
        "en": "HOUR OF THE DAY · 1 AT DAWN · 13 AT DUSK",
        "fr": "HEURE DU JOUR · 1 À L'AUBE · 13 AU CRÉPUSCULE"},

    "24 ÷ 7 = 3 Y SOBRAN 3 · POR ESO LA SEMANA VA DE TRES EN TRES": {
        "en": "24 ÷ 7 = 3 REMAINDER 3 · THAT IS WHY THE WEEK MOVES IN THREES",
        "fr": "24 ÷ 7 = 3 ET IL RESTE 3 · VOILÀ POURQUOI LA SEMAINE VA DE TROIS EN TROIS"},

    "VALOR": {"en": "VALUE", "fr": "VALEUR"},
    "LE CORRESPONDE": {"en": "IT CORRESPONDS TO", "fr": "LUI CORRESPOND"},
    "3 madres · elementos": {
        "en": "3 mothers · elements", "fr": "3 mères · éléments"},
    "7 dobles · planetas": {
        "en": "7 doubles · planets", "fr": "7 doubles · planètes"},
    "12 simples · signos": {
        "en": "12 simples · signs", "fr": "12 simples · signes"},
    "LOS VEINTIDÓS VALORES SUMAN 1 495": {
        "en": "THE TWENTY-TWO VALUES ADD UP TO 1,495",
        "fr": "LES VINGT-DEUX VALEURS FONT 1 495"},

    # ── Cubierta ───────────────────────────────────────────────────────────
    "Códice de las Invocaciones": {
        "en": "Codex of Invocations", "fr": "Codex des Invocations"},

    "Manual de práctica ritual: el círculo, las armas, los nombres y el trabajo sobre uno "
    "mismo": {
        "en": "A manual of ritual practice: the circle, the weapons, the names and the work "
              "on oneself",
        "fr": "Manuel de pratique rituelle : le cercle, les armes, les noms et le travail sur "
              "soi"},

    # ── Créditos ───────────────────────────────────────────────────────────
    "<strong>Códice de las Invocaciones</strong> es una obra original de Villuminations,\n"
    "     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.\n"
    "     Obra original · Primera edición, 2026.": {
        "en": "<strong>Codex of Invocations</strong> is an original work by Villuminations, "
              "written and typeset entirely for <strong>villuminations.com</strong>. "
              "Original work · First edition, 2026.",
        "fr": "<strong>Codex des Invocations</strong> est une œuvre originale de "
              "Villuminations, écrite et composée intégralement pour "
              "<strong>villuminations.com</strong>. Œuvre originale · Première édition, 2026."},

    "El material del que parte pertenece a la <strong>tradición común</strong>:\n"
    "     las fórmulas, los nombres y las estructuras rituales que aquí se comentan\n"
    "     se transmiten por escrito desde hace siglos en obras de dominio público y\n"
    "     no son propiedad de nadie. Lo que aquí se ofrece —la redacción, la\n"
    "     estructura de capítulos, las prácticas, las fichas y las ilustraciones—\n"
    "     es trabajo propio y está protegido como tal.": {
        "en": "The material it starts from belongs to the <strong>common tradition</strong>: "
              "the formulae, the names and the ritual structures discussed here have been "
              "transmitted in writing for centuries in works in the public domain and are "
              "nobody's property. What is offered here —the writing, the chapter structure, "
              "the practices, the entries and the illustrations— is original work and is "
              "protected as such.",
        "fr": "Le matériau dont il part appartient à la <strong>tradition commune</strong> : "
              "les formules, les noms et les structures rituelles commentés ici se "
              "transmettent par écrit depuis des siècles dans des œuvres du domaine public et "
              "n'appartiennent à personne. Ce qui est proposé ici —la rédaction, la structure "
              "des chapitres, les pratiques, les fiches et les illustrations— est un travail "
              "propre et protégé comme tel."},

    "<strong>Cómo leer este libro.</strong> Lo que aquí se practica es un\n"
    "     <em>lenguaje simbólico</em>: una manera antigua de ordenar la atención y\n"
    "     la intención. No es una ciencia predictiva ni una promesa de resultados.\n"
    "     Nada de lo que sigue anuncia hechos futuros, diagnostica enfermedades ni\n"
    "     sustituye la atención de un médico o un psicólogo colegiado.": {
        "en": "<strong>How to read this book.</strong> What is practised here is a "
              "<em>symbolic language</em>: an old way of ordering attention and intention. It "
              "is not a predictive science and not a promise of results. Nothing that follows "
              "announces future events, diagnoses illnesses or replaces the care of a "
              "registered doctor or psychologist.",
        "fr": "<strong>Comment lire ce livre.</strong> Ce qui se pratique ici est un "
              "<em>langage symbolique</em> : une manière ancienne d'ordonner l'attention et "
              "l'intention. Ce n'est pas une science prédictive ni une promesse de résultats. "
              "Rien de ce qui suit n'annonce de faits futurs, ne diagnostique de maladies ni "
              "ne remplace les soins d'un médecin ou d'un psychologue inscrit à l'ordre."},

    # ── Índice ─────────────────────────────────────────────────────────────
    "Lo que este libro es": {"en": "What this book is", "fr": "Ce qu'est ce livre"},
    "La tradición de la que viene": {
        "en": "The tradition it comes from", "fr": "La tradition dont il vient"},
    "El vocabulario del oficio": {
        "en": "The vocabulary of the craft", "fr": "Le vocabulaire du métier"},
    "El círculo y los cuatro cuartos": {
        "en": "The circle and the four quarters",
        "fr": "Le cercle et les quatre quartiers"},
    "Las cuatro armas": {"en": "The four weapons", "fr": "Les quatre armes"},
    "El pentagrama: las dos direcciones": {
        "en": "The pentagram: the two directions",
        "fr": "Le pentagramme : les deux sens"},
    "El hexagrama y los siete": {
        "en": "The hexagram and the seven", "fr": "L'hexagramme et les sept"},
    "El árbol de los diez números": {
        "en": "The tree of the ten numbers", "fr": "L'arbre des dix nombres"},
    "Los cuadrados planetarios": {
        "en": "The planetary squares", "fr": "Les carrés planétaires"},
    "Los nombres y la voz": {
        "en": "The names and the voice", "fr": "Les noms et la voix"},
    "La tabla completa de las horas planetarias": {
        "en": "The complete table of planetary hours",
        "fr": "La table complète des heures planétaires"},
    "Las veintidós letras y sus números": {
        "en": "The twenty-two letters and their numbers",
        "fr": "Les vingt-deux lettres et leurs nombres"},
}
