# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · las seis pruebas y la batería casera
=========================================================
Las descripciones largas de las pruebas repiten, ampliadas, lo que ya dice la
lámina en versión corta. Son segmentos distintos y llevan traducción distinta:
allí el rótulo estaba recortado para caber en su recuadro y aquí la frase se
completa. Los términos elegidos coinciden para que el lector reconozca la
misma prueba en los dos sitios.

La carrera se llama «de dos millas» y conserva las millas, con los 3,2 km al
lado; el balón pesa 4,5 kg con coma en español y en francés y punto en inglés.
"""

T = {
    "Peso muerto máximo": {"en": "Maximum deadlift", "fr": "Soulevé de terre maximal"},
    "Tres repeticiones con la barra hexagonal · mide fuerza máxima de la cadena posterior": {
        "en": "Three repetitions with the hex bar · it measures maximum strength of the "
              "posterior chain",
        "fr": "Trois répétitions à la barre hexagonale · mesure la force maximale de la chaîne "
              "postérieure"},

    "Lanzamiento de balón": {"en": "Medicine ball throw", "fr": "Lancer de médecine-ball"},
    "Balón de 4,5 kg lanzado hacia atrás por encima de la cabeza · mide potencia explosiva "
    "de todo el cuerpo": {
        "en": "A 4.5 kg ball thrown backwards over the head · it measures explosive power of "
              "the whole body",
        "fr": "Ballon de 4,5 kg lancé en arrière par-dessus la tête · mesure la puissance "
              "explosive de tout le corps"},

    "Flexión con liberación de manos": {
        "en": "Hand-release push-up", "fr": "Pompe avec mains décollées"},
    "Pecho al suelo y manos fuera en cada repetición · mide resistencia del tren superior, "
    "sin recorrido a medias": {
        "en": "Chest to the floor and hands off on every repetition · it measures upper-body "
              "endurance, with no half range",
        "fr": "Poitrine au sol et mains décollées à chaque répétition · mesure l'endurance du "
              "haut du corps, sans demi-amplitude"},

    "Sprint, arrastre y acarreo": {
        "en": "Sprint, drag and carry", "fr": "Sprint, traction et porté"},
    "250 m: esprintar, arrastrar trineo, desplazamiento lateral y acarreo de dos pesas · "
    "mide potencia anaeróbica y agarre": {
        "en": "250 m: sprint, sled drag, lateral shuffle and a two-weight carry · it measures "
              "anaerobic power and grip",
        "fr": "250 m : sprinter, tirer un traîneau, déplacement latéral et porté de deux "
              "poids · mesure la puissance anaérobie et la préhension"},

    "Plancha": {"en": "Plank", "fr": "Gainage"},
    "Sostenida, con el cuerpo alineado · mide resistencia del tronco en isometría": {
        "en": "Held, with the body in line · it measures trunk endurance in isometry",
        "fr": "Tenu, le corps aligné · mesure l'endurance du tronc en isométrie"},

    "Carrera de dos millas": {"en": "Two-mile run", "fr": "Course de deux milles"},
    "3,2 km cronometrados · mide capacidad aeróbica": {
        "en": "3.2 km timed · it measures aerobic capacity",
        "fr": "3,2 km chronométrés · mesure la capacité aérobie"},

    "Cada prueba puntúa de 0 a 100 y hay que sacar al menos 60 en cada una: no se compensa "
    "una prueba mala con otra excelente. Esa regla es la lección transferible.": {
        "en": "Each test scores from 0 to 100 and you have to get at least 60 in every one: a "
              "bad test is not offset by an excellent one. That rule is the transferable "
              "lesson.",
        "fr": "Chaque épreuve est notée de 0 à 100 et il faut obtenir au moins 60 à chacune : "
              "une mauvaise épreuve ne se compense pas par une excellente. Cette règle est la "
              "leçon transférable."},

    "Por qué esto es interesante para alguien que no es militar": {
        "en": "Why this is interesting for someone who is not in the military",
        "fr": "Pourquoi cela intéresse quelqu'un qui n'est pas militaire"},

    "Por el diseño, no por las pruebas concretas. Una batería que exige un mínimo en seis "
    "cualidades distintas está diciendo algo que el gimnasio medio ignora: que un cuerpo "
    "bien preparado no es el que destaca en una cosa, sino el que no falla en ninguna. "
    "Alguien que levanta mucho y no puede correr dos millas tiene un hueco, y ese hueco no "
    "se tapa levantando más.": {
        "en": "For the design, not for the particular tests. A battery that demands a minimum "
              "in six different qualities is saying something the average gym ignores: that a "
              "well-prepared body is not the one that stands out in one thing, but the one "
              "that fails in none. Someone who lifts a lot and cannot run two miles has a gap, "
              "and that gap is not filled by lifting more.",
        "fr": "Pour la conception, pas pour les épreuves elles-mêmes. Une batterie qui exige "
              "un minimum dans six qualités différentes dit quelque chose que la salle moyenne "
              "ignore : qu'un corps bien préparé n'est pas celui qui excelle en une chose, "
              "mais celui qui ne faiblit en aucune. Qui soulève beaucoup et ne peut pas courir "
              "deux milles a un trou, et ce trou ne se comble pas en soulevant davantage."},

    "El segundo motivo es que es un objetivo de proceso disfrazado de resultado. Puntuar "
    "mejor en seis pruebas es una diana clara, medible y que depende enteramente de lo que "
    "hagas, a diferencia del peso corporal, que depende de media docena de cosas que no "
    "controlas.": {
        "en": "The second reason is that it is a process goal disguised as an outcome. Scoring "
              "better in six tests is a clear, measurable target that depends entirely on what "
              "you do, unlike body weight, which depends on half a dozen things you do not "
              "control.",
        "fr": "La deuxième raison est que c'est un objectif de processus déguisé en résultat. "
              "Mieux noter à six épreuves est une cible claire, mesurable et qui dépend "
              "entièrement de ce que vous faites, à la différence du poids du corps, qui "
              "dépend d'une demi-douzaine de choses que vous ne contrôlez pas."},

    "Una versión casera de la misma idea": {
        "en": "A home version of the same idea",
        "fr": "Une version maison de la même idée"},

    "No hace falta un trineo ni una barra hexagonal. Lo que hace falta es elegir cinco o "
    "seis pruebas que cubran cualidades distintas, medirlas hoy y repetirlas cada tres "
    "meses en las mismas condiciones:": {
        "en": "You need no sled and no hex bar. What you need is to choose five or six tests "
              "covering different qualities, measure them today and repeat them every three "
              "months under the same conditions:",
        "fr": "Nul besoin de traîneau ni de barre hexagonale. Ce qu'il faut, c'est choisir cinq "
              "ou six épreuves qui couvrent des qualités différentes, les mesurer aujourd'hui "
              "et les répéter tous les trois mois dans les mêmes conditions :"},

    "Batería casera": {"en": "Home battery", "fr": "Batterie maison"},

    "Fuerza de piernas": {"en": "Leg strength", "fr": "Force des jambes"},
    "Sentadillas en un minuto, o peso de tu serie de cinco repeticiones": {
        "en": "Squats in one minute, or the weight of your five-repetition set",
        "fr": "Squats en une minute, ou le poids de votre série de cinq répétitions"},

    "Fuerza de empuje": {"en": "Pushing strength", "fr": "Force de poussée"},
    "Flexiones máximas con técnica completa": {
        "en": "Maximum push-ups with full technique",
        "fr": "Pompes maximales avec une technique complète"},

    "Fuerza de tirón": {"en": "Pulling strength", "fr": "Force de tirage"},
    "Dominadas, o remo invertido máximo": {
        "en": "Pull-ups, or maximum inverted rows",
        "fr": "Tractions, ou rowing inversé maximal"},

    "Tronco": {"en": "Trunk", "fr": "Tronc"},
    "Plancha sostenida, en segundos": {
        "en": "Plank held, in seconds", "fr": "Gainage tenu, en secondes"},

    "Distancia en doce minutos, o tiempo en un recorrido fijo que puedas repetir": {
        "en": "Distance in twelve minutes, or time over a fixed route you can repeat",
        "fr": "Distance en douze minutes, ou temps sur un parcours fixe que vous pouvez "
              "répéter"},

    "Segundos sobre una pierna con los ojos cerrados": {
        "en": "Seconds on one leg with your eyes closed",
        "fr": "Secondes sur une jambe, les yeux fermés"},

    "Anota los seis números y guárdalos. Dentro de tres meses tendrás algo que ninguna "
    "báscula da: seis pruebas de que el trabajo hizo algo, o seis señales de dónde no lo "
    "hizo. Y a diferencia del peso, estos números no oscilan tres kilos según lo que "
    "cenaste.": {
        "en": "Write the six numbers down and keep them. In three months you will have "
              "something no set of scales gives: six pieces of evidence that the work did "
              "something, or six signals of where it did not. And unlike weight, these numbers "
              "do not swing three kilos depending on what you had for dinner.",
        "fr": "Notez les six nombres et gardez-les. Dans trois mois vous aurez quelque chose "
              "qu'aucune balance ne donne : six preuves que le travail a fait quelque chose, "
              "ou six signaux de là où il n'en a pas fait. Et contrairement au poids, ces "
              "nombres n'oscillent pas de trois kilos selon ce que vous avez dîné."},
}
