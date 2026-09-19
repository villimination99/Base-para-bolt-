# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · cierre de las láminas, cubierta, créditos e índice
=======================================================================
Los créditos de este libro citan sus propias fuentes —el FM 7-22 y los
criterios del NIOSH— y no las de ningún otro volumen. La base legal, el
17 U.S.C. § 105, se copia con la misma redacción en los tres idiomas porque es
una cita de una norma, no una frase de estilo.

El nombre del sexto factor de la ecuación es «coupling» en el documento
original, no «grip»: mide lo bien que la caja se deja agarrar, no la fuerza de
la mano. En español el libro lo llama AGARRE y en inglés vuelve a su nombre.
"""

T = {
    # ── Cierre de la ecuación de levantamiento ─────────────────────────────
    "VERTICAL": {"en": "VERTICAL", "fr": "VERTICAL"},
    "Altura de las manos al empezar": {
        "en": "Height of the hands at the start",
        "fr": "Hauteur des mains au départ"},

    "DM": {"en": "DM", "fr": "DM"},
    "DISTANCIA": {"en": "DISTANCE", "fr": "DISTANCE"},
    "Cuánto sube la carga": {
        "en": "How far the load travels", "fr": "De combien la charge monte"},

    "AM": {"en": "AM", "fr": "AM"},
    "ASIMETRÍA": {"en": "ASYMMETRY", "fr": "ASYMÉTRIE"},
    "Cuánto se gira el tronco": {
        "en": "How much the trunk twists", "fr": "De combien le tronc pivote"},

    "FM": {"en": "FM", "fr": "FM"},
    "Levantamientos por minuto y duración de…": {
        "en": "Lifts per minute and duration of…",
        "fr": "Levers par minute et durée de…"},

    "CM": {"en": "CM", "fr": "CM"},
    "AGARRE": {"en": "COUPLING", "fr": "PRISE"},
    "Bueno, regular o malo": {
        "en": "Good, fair or poor", "fr": "Bonne, moyenne ou mauvaise"},

    "ALEJAR LA CARGA DEL CUERPO ES LO QUE MÁS PENALIZA": {
        "en": "MOVING THE LOAD AWAY FROM THE BODY PENALISES MOST",
        "fr": "ÉLOIGNER LA CHARGE DU CORPS EST CE QUI PÉNALISE LE PLUS"},

    # ── Cubierta ───────────────────────────────────────────────────────────
    "Códice de la Carga": {
        "en": "Codex of the Load", "fr": "Codex de la Charge"},

    "La dosis oficial de actividad, la escala que la mide, la ecuación de levantar y lo "
    "que le pasa a un cuerpo sin peso": {
        "en": "The official dose of activity, the scale that measures it, the lifting "
              "equation, and what happens to a body with no weight on it",
        "fr": "La dose officielle d'activité, l'échelle qui la mesure, l'équation du "
              "levage et ce qui arrive à un corps sans poids"},

    # ── Créditos ───────────────────────────────────────────────────────────
    "<strong>Códice de la Carga</strong> es una obra original de Villuminations,\n"
    "     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.\n"
    "     Obra original · Primera edición, 2026.": {
        "en": "<strong>Codex of the Load</strong> is an original work by Villuminations, "
              "written and typeset entirely for <strong>villuminations.com</strong>. "
              "Original work · First edition, 2026.",
        "fr": "<strong>Codex de la Charge</strong> est une œuvre originale de "
              "Villuminations, écrite et composée intégralement pour "
              "<strong>villuminations.com</strong>. Œuvre originale · Première édition, "
              "2026."},

    "El material del que parte pertenece al <strong>dominio público</strong>:\n"
    "     los manuales de acondicionamiento físico y los criterios de manejo de\n"
    "     cargas publicados por organismos del Gobierno de los Estados Unidos\n"
    "     —entre ellos el FM 7-22 y las guías del NIOSH— no están sujetos a\n"
    "     derechos de autor conforme al 17 U.S.C. § 105. Lo que aquí se ofrece —la\n"
    "     redacción, la estructura de capítulos, las progresiones, las tablas y las\n"
    "     ilustraciones— es trabajo propio y está protegido como tal.": {
        "en": "The material it starts from is in the <strong>public domain</strong>: the "
              "physical-conditioning manuals and the load-handling criteria published by "
              "agencies of the Government of the United States —among them FM 7-22 and "
              "the NIOSH guidance— are not subject to copyright under 17 U.S.C. § 105. "
              "What is offered here —the writing, the chapter structure, the "
              "progressions, the tables and the illustrations— is original work and is "
              "protected as such.",
        "fr": "Le matériau dont il part relève du <strong>domaine public</strong> : les "
              "manuels de conditionnement physique et les critères de manutention de "
              "charges publiés par des organismes du gouvernement des États-Unis —dont le "
              "FM 7-22 et les recommandations du NIOSH— ne sont pas soumis au droit "
              "d'auteur en vertu du 17 U.S.C. § 105. Ce qui est proposé ici —la "
              "rédaction, la structure des chapitres, les progressions, les tableaux et "
              "les illustrations— est un travail propre et protégé comme tel."},

    "<strong>Cómo leer este libro.</strong> Es un libro sobre\n"
    "     <em>carga y adaptación</em>: sobre cuánto trabajo se puede acumular y a\n"
    "     qué ritmo. El entrenamiento con cargas conlleva riesgo de lesión. Nada de\n"
    "     lo que sigue diagnostica ni trata ninguna dolencia, y no sustituye la\n"
    "     valoración de un profesional sanitario colegiado ni la supervisión\n"
    "     presencial de un entrenador cualificado. Si tienes una patología\n"
    "     articular, cardiovascular o respiratoria, consúltalo antes de empezar.": {
        "en": "<strong>How to read this book.</strong> It is a book about <em>load and "
              "adaptation</em>: about how much work can be accumulated and at what rate. "
              "Training with loads carries a risk of injury. Nothing that follows "
              "diagnoses or treats any complaint, and it does not replace assessment by a "
              "registered health professional or the in-person supervision of a qualified "
              "coach. If you have a joint, cardiovascular or respiratory condition, take "
              "advice before you start.",
        "fr": "<strong>Comment lire ce livre.</strong> C'est un livre sur la <em>charge et "
              "l'adaptation</em> : sur la quantité de travail que l'on peut accumuler et à "
              "quel rythme. L'entraînement avec charges comporte un risque de blessure. "
              "Rien de ce qui suit ne diagnostique ni ne traite quoi que ce soit, et cela "
              "ne remplace ni l'évaluation d'un professionnel de santé inscrit à l'ordre "
              "ni la supervision sur place d'un entraîneur qualifié. Si vous avez une "
              "pathologie articulaire, cardiovasculaire ou respiratoire, demandez conseil "
              "avant de commencer."},

    # ── Índice ─────────────────────────────────────────────────────────────
    "Existe una dosis, y está escrita": {
        "en": "There is a dose, and it is written down",
        "fr": "Il existe une dose, et elle est écrite"},
    "La forma de la curva": {
        "en": "The shape of the curve", "fr": "La forme de la courbe"},
    "La moneda de la intensidad": {
        "en": "The currency of intensity", "fr": "La monnaie de l'intensité"},
    "El corazón y la zona que no existe": {
        "en": "The heart and the zone that does not exist",
        "fr": "Le cœur et la zone qui n'existe pas"},
    "La fuerza no es opcional": {
        "en": "Strength is not optional", "fr": "La force n'est pas facultative"},
    "Los ocho patrones": {
        "en": "The eight patterns", "fr": "Les huit schémas"},
    "Las seis variables": {
        "en": "The six variables", "fr": "Les six variables"},
    "Calentar, enfriar y lo que no sirve": {
        "en": "Warming up, cooling down and what is no use",
        "fr": "S'échauffer, récupérer et ce qui ne sert à rien"},
    "El aerobio por dentro": {
        "en": "Aerobic work from the inside",
        "fr": "L'aérobie vue de l'intérieur"},
    "El experimento de quitar el peso": {
        "en": "The experiment of taking the weight away",
        "fr": "L'expérience qui retire le poids"},
    "Perder y recuperar": {
        "en": "Losing and regaining", "fr": "Perdre et récupérer"},
}
