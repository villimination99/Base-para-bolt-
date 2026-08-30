# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · los ases, la escala del uno al diez y los decanatos
===========================================================================
La escala numérica se lee de arriba abajo y cada peldaño se apoya en el
anterior: el tres resuelve el dos, el cinco rompe el cuatro, el seis recompone
después del cinco. Esas referencias cruzadas van con el número escrito, no con
un «el anterior», porque el lector salta a la fila que le interesa y necesita
que cada línea se sostenga sola.

«Decanato» es decan en inglés y décan en francés: el tramo de diez grados de
un signo. La palabra es técnica y tiene forma fija en las tres lenguas.
"""

T = {
    "El as no es el número uno: es el elemento puro, la raíz del palo antes de manifestarse "
    "en nada concreto. Salido en una tirada, indica que el asunto está en su origen y "
    "todavía no tiene forma — y que la tiene disponible.": {
        "en": "The ace is not the number one: it is the pure element, the root of the suit "
              "before it shows itself in anything concrete. When it comes up in a spread it "
              "indicates that the matter is at its source and has no form yet — and that form "
              "is available to it.",
        "fr": "L'as n'est pas le nombre un : c'est l'élément pur, la racine de la couleur avant "
              "de se manifester en quoi que ce soit de concret. Sorti dans un tirage, il "
              "indique que l'affaire est à son origine et n'a pas encore de forme — et qu'elle "
              "en a une à disposition."},

    "Los cuatro orígenes": {"en": "The four sources", "fr": "Les quatre origines"},

    "As de Bastos": {"en": "Ace of Wands", "fr": "As de Bâtons"},
    "Fuego en bruto. Un impulso que aún no es proyecto. La gana.": {
        "en": "Raw fire. An impulse that is not yet a project. The appetite.",
        "fr": "Du feu brut. Une impulsion qui n'est pas encore un projet. L'envie."},

    "As de Copas": {"en": "Ace of Cups", "fr": "As de Coupes"},
    "Agua en bruto. Un sentimiento antes de tener objeto. La apertura.": {
        "en": "Raw water. A feeling before it has an object. The opening.",
        "fr": "De l'eau brute. Un sentiment avant d'avoir un objet. L'ouverture."},

    "As de Espadas": {"en": "Ace of Swords", "fr": "As d'Épées"},
    "Aire en bruto. Una idea antes de argumento. La claridad que corta.": {
        "en": "Raw air. An idea before it has an argument. The clarity that cuts.",
        "fr": "De l'air brut. Une idée avant l'argument. La clarté qui coupe."},

    "As de Oros": {"en": "Ace of Pentacles", "fr": "As de Deniers"},
    "Tierra en bruto. Un recurso antes de gastarse. La posibilidad material.": {
        "en": "Raw earth. A resource before it is spent. Material possibility.",
        "fr": "De la terre brute. Une ressource avant d'être dépensée. La possibilité "
              "matérielle."},

    "Las diez etapas del número": {
        "en": "The ten stages of number", "fr": "Les dix étapes du nombre"},

    "Del dos al diez, cada número describe una etapa del mismo proceso, independientemente "
    "del palo. Aprendida la escala una vez, sirve para las treinta y seis.": {
        "en": "From two to ten, each number describes a stage of the same process, whatever "
              "the suit. Learn the scale once and it serves for all thirty-six.",
        "fr": "Du deux au dix, chaque nombre décrit une étape du même processus, quelle que "
              "soit la couleur. L'échelle apprise une fois sert pour les trente-six."},

    "La escala, del dos al diez": {
        "en": "The scale, from two to ten", "fr": "L'échelle, du deux au dix"},

    "La primera relación y la primera tensión. Dos cosas frente a frente: equilibrio o "
    "elección.": {
        "en": "The first relation and the first tension. Two things face to face: balance or "
              "choice.",
        "fr": "La première relation et la première tension. Deux choses face à face : "
              "équilibre ou choix."},

    "Lo que resuelve el dos: aparece un tercero, una síntesis, un resultado inicial.": {
        "en": "What resolves the two: a third appears, a synthesis, an initial result.",
        "fr": "Ce qui résout le deux : un tiers apparaît, une synthèse, un premier résultat."},

    "La estabilidad conseguida. Se consolida, y con ella empieza el riesgo de acomodarse.": {
        "en": "Stability achieved. It consolidates, and with it begins the risk of settling.",
        "fr": "La stabilité obtenue. Elle se consolide, et avec elle commence le risque de "
              "s'installer."},

    "La rotura. El cuatro se quiebra porque tenía que quebrarse: es el número de la crisis "
    "en los cuatro palos.": {
        "en": "The break. The four breaks because it had to break: it is the number of crisis "
              "in all four suits.",
        "fr": "La rupture. Le quatre se brise parce qu'il devait se briser : c'est le nombre de "
              "la crise dans les quatre couleurs."},

    "La recomposición después del cinco. Se recupera el equilibrio, ya con información.": {
        "en": "The putting back together after the five. Balance is recovered, this time with "
              "information.",
        "fr": "La recomposition après le cinq. On retrouve l'équilibre, cette fois avec de "
              "l'information."},

    "La prueba individual. Hay que sostener solo lo recuperado, y aparece la tentación de "
    "soltarlo.": {
        "en": "The individual test. What was recovered has to be held alone, and the "
              "temptation to let go appears.",
        "fr": "L'épreuve individuelle. Il faut tenir seul ce qui a été récupéré, et la "
              "tentation de le lâcher apparaît."},

    "El movimiento y el oficio. Se trabaja, se acelera, se hace cantidad.": {
        "en": "Movement and craft. You work, you speed up, you make quantity.",
        "fr": "Le mouvement et le métier. On travaille, on accélère, on fait de la quantité."},

    "El resultado casi cerrado, con lo que ha costado a la vista. El número más ambivalente "
    "de la escala.": {
        "en": "The result almost closed, with what it cost in plain sight. The most ambivalent "
              "number on the scale.",
        "fr": "Le résultat presque clos, avec ce qu'il a coûté bien en vue. Le nombre le plus "
              "ambivalent de l'échelle."},

    "El final del ciclo: colmado o agotado, según el palo. Lo que sigue ya es otro as.": {
        "en": "The end of the cycle: brimming or exhausted, depending on the suit. What comes "
              "next is another ace.",
        "fr": "La fin du cycle : comblé ou épuisé, selon la couleur. Ce qui suit est déjà un "
              "autre as."},

    "La utilidad real de la escala": {
        "en": "What the scale is really for", "fr": "L'utilité réelle de l'échelle"},

    "Que los cincos son crisis en los cuatro palos y los dieces son finales en los cuatro. "
    "Cuando en una tirada salen dos cincos, no hace falta saber nada más para decir que el "
    "asunto está en su punto de rotura. La escala es lo que permite leer una carta que no "
    "recuerdas: número más palo, y sale.": {
        "en": "That the fives are crises in all four suits and the tens are endings in all "
              "four. When two fives come up in a spread, you need to know nothing else to say "
              "that the matter is at breaking point. The scale is what lets you read a card you "
              "do not remember: number plus suit, and out it comes.",
        "fr": "Que les cinq sont des crises dans les quatre couleurs et que les dix sont des "
              "fins dans les quatre. Quand deux cinq sortent dans un tirage, il n'est pas "
              "besoin d'en savoir plus pour dire que l'affaire est à son point de rupture. "
              "L'échelle est ce qui permet de lire une carte dont on ne se souvient pas : "
              "nombre plus couleur, et elle sort."},

    # ── Los decanatos ──────────────────────────────────────────────────────
    "Aquí está la pieza que da al tarot su capa más fina de precisión. Las treinta y seis "
    "cartas del dos al diez no son treinta y seis significados sueltos: son los treinta y "
    "seis decanatos del zodiaco, uno por carta, sin sobrar ni faltar ninguno.": {
        "en": "Here is the piece that gives tarot its finest layer of precision. The "
              "thirty-six cards from two to ten are not thirty-six loose meanings: they are "
              "the thirty-six decans of the zodiac, one per card, with none left over and none "
              "missing.",
        "fr": "Voici la pièce qui donne au tarot sa couche de précision la plus fine. Les "
              "trente-six cartes du deux au dix ne sont pas trente-six significations éparses : "
              "ce sont les trente-six décans du zodiaque, un par carte, sans qu'il en reste ni "
              "qu'il en manque un seul."},

    '<span class="fig-n">Lám. 4</span> Las treinta y seis. Cada fila es un signo con sus '
    "tres tramos de diez grados, y en cada tramo la carta que le corresponde. Ni una carta "
    "repetida, ni un decanato vacío.": {
        "en": '<span class="fig-n">Pl. 4</span> The thirty-six. Each row is a sign with its '
              "three stretches of ten degrees, and in each stretch the card that corresponds "
              "to it. Not one card repeated, not one decan empty.",
        "fr": '<span class="fig-n">Pl. 4</span> Les trente-six. Chaque ligne est un signe avec '
              "ses trois tronçons de dix degrés, et dans chaque tronçon la carte qui lui "
              "correspond. Pas une carte répétée, pas un décan vide."},
}
