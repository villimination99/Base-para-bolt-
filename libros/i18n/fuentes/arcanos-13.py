# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · las tres reglas del lector y las tres tiradas
=====================================================================
Los nombres de las posiciones se repiten en la lámina y en el capítulo, pero
en formas distintas: allí van sin numerar y aquí llevan «1 ·», «2 ·». Son
segmentos separados y llevan traducción separada; lo que tiene que coincidir
es la palabra elegida, porque el lector coloca las cartas mirando el dibujo y
lee el significado en el texto.

«Qué falta» no es «qué pasará», y el propio libro lo aclara en la línea
siguiente. La traducción evita en los tres idiomas cualquier verbo en futuro
en esa posición: es la diferencia entre este mazo y uno que promete adivinar.
"""

T = {
    "«Si es azar, entonces cualquier carta serviría para cualquier cosa.» No: eso pasaría "
    "si las cartas no tuvieran contorno. El aparato de este libro —letras, elementos, "
    "decanatos, escala del número— existe precisamente para que cada figura signifique algo "
    "bastante concreto y no admita cualquier lectura. Cuando una carta no encaja con lo que "
    "quieres oír, la estructura te impide estirarla, y ahí es donde el instrumento hace su "
    "mejor trabajo.": {
        "en": "«If it is chance, then any card would do for anything.» No: that would happen "
              "if the cards had no outline. This book's apparatus —letters, elements, decans, "
              "the scale of number— exists precisely so that each figure means something "
              "fairly specific and does not admit just any reading. When a card does not fit "
              "what you want to hear, the structure stops you stretching it, and that is where "
              "the instrument does its best work.",
        "fr": "« Si c'est le hasard, alors n'importe quelle carte ferait l'affaire pour "
              "n'importe quoi. » Non : cela arriverait si les cartes n'avaient pas de contour. "
              "L'appareil de ce livre —lettres, éléments, décans, échelle du nombre— existe "
              "justement pour que chaque figure signifie quelque chose d'assez précis et "
              "n'admette pas n'importe quelle lecture. Quand une carte ne s'accorde pas avec "
              "ce que vous voulez entendre, la structure vous empêche de l'étirer, et c'est là "
              "que l'instrument fait son meilleur travail."},

    "Las tres reglas del que lee bien": {
        "en": "The three rules of the good reader",
        "fr": "Les trois règles de qui lit bien"},

    "Se lee lo que hay, no lo que se esperaba. Si la tirada no dice nada, se dice que no "
    "dice nada. Un lector que siempre encuentra un mensaje está fabricándolos.": {
        "en": "You read what is there, not what was expected. If the spread says nothing, you "
              "say it says nothing. A reader who always finds a message is manufacturing them.",
        "fr": "On lit ce qu'il y a, non ce qu'on attendait. Si le tirage ne dit rien, on dit "
              "qu'il ne dit rien. Un lecteur qui trouve toujours un message est en train d'en "
              "fabriquer."},

    "Se lee el conjunto antes que las cartas. Cuántos mayores, qué palos dominan, qué "
    "números se repiten: eso dice más que cualquier carta individual, y se ve en cinco "
    "segundos.": {
        "en": "You read the whole before the cards. How many majors, which suits dominate, "
              "which numbers repeat: that says more than any individual card, and it is seen "
              "in five seconds.",
        "fr": "On lit l'ensemble avant les cartes. Combien de majeurs, quelles couleurs "
              "dominent, quels nombres se répètent : cela dit plus que n'importe quelle carte "
              "isolée, et cela se voit en cinq secondes."},

    "Se termina en una acción concreta. Una tirada que acaba en una interpretación bonita "
    "no ha servido. Una que acaba en «voy a decirle esto a esta persona esta semana», sí.": {
        "en": "You finish with a concrete action. A spread that ends in a pretty interpretation "
              "has been no use. One that ends in «I am going to say this to this person this "
              "week» has.",
        "fr": "On termine sur une action concrète. Un tirage qui s'achève sur une belle "
              "interprétation n'a servi à rien. Un tirage qui s'achève sur « je vais dire ceci "
              "à cette personne cette semaine », si."},

    # ── Las tiradas ────────────────────────────────────────────────────────
    "Tres tiradas, diseñadas para este libro y pensadas para lo que el instrumento sí hace. "
    "Ninguna de las tres pregunta por el futuro.": {
        "en": "Three spreads, designed for this book and thought out for what the instrument "
              "actually does. None of the three asks about the future.",
        "fr": "Trois tirages, conçus pour ce livre et pensés pour ce que l'instrument fait "
              "réellement. Aucun des trois ne demande l'avenir."},

    '<span class="fig-n">Lám. 5</span> Las tres disposiciones con el orden en que se saca '
    "cada carta.": {
        "en": '<span class="fig-n">Pl. 5</span> The three layouts with the order in which each '
              "card is drawn.",
        "fr": '<span class="fig-n">Pl. 5</span> Les trois dispositions avec l\'ordre dans '
              "lequel chaque carte est tirée."},

    "Las Tres": {"en": "The Three", "fr": "Les Trois"},
    "La básica, tres cartas en fila. Es la que se usa el noventa por ciento de las veces y "
    "la que conviene dominar antes de cualquier otra.": {
        "en": "The basic one, three cards in a row. It is the one used ninety per cent of the "
              "time and the one worth mastering before any other.",
        "fr": "Le tirage de base, trois cartes en ligne. C'est celui qu'on emploie neuf fois "
              "sur dix et celui qu'il vaut mieux maîtriser avant tout autre."},

    "Las Tres · posiciones": {
        "en": "The Three · positions", "fr": "Les Trois · positions"},

    "1 · Qué había": {"en": "1 · What was there", "fr": "1 · Ce qu'il y avait"},
    "El punto de partida real del asunto, no el que se cuenta.": {
        "en": "The real starting point of the matter, not the one that gets told.",
        "fr": "Le vrai point de départ de l'affaire, non celui qu'on raconte."},

    "2 · Qué hay": {"en": "2 · What is there", "fr": "2 · Ce qu'il y a"},
    "La situación tal como está ahora.": {
        "en": "The situation as it stands now.", "fr": "La situation telle qu'elle est."},

    "3 · Qué falta": {"en": "3 · What is missing", "fr": "3 · Ce qui manque"},
    "Lo que no se ha puesto todavía. No lo que pasará: lo que falta.": {
        "en": "What has not been put in yet. Not what will happen: what is missing.",
        "fr": "Ce qui n'a pas encore été mis. Non pas ce qui arrivera : ce qui manque."},

    "La Cruz de Cuatro": {"en": "The Cross of Four", "fr": "La Croix de Quatre"},
    "Para cuando hay una decisión que tomar y no se avanza. La tercera posición es la que "
    "suele resolver la tirada.": {
        "en": "For when there is a decision to be made and nothing is moving. The third "
              "position is usually the one that resolves the spread.",
        "fr": "Pour quand il y a une décision à prendre et que rien n'avance. La troisième "
              "position est celle qui résout d'ordinaire le tirage."},

    "La Cruz de Cuatro · posiciones": {
        "en": "The Cross of Four · positions", "fr": "La Croix de Quatre · positions"},

    "1 · El hecho": {"en": "1 · The fact", "fr": "1 · Le fait"},
    "Al centro. Qué está pasando de verdad, sin interpretación.": {
        "en": "In the centre. What is really happening, with no interpretation.",
        "fr": "Au centre. Ce qui se passe vraiment, sans interprétation."},

    "2 · Lo que aporto": {"en": "2 · What I bring", "fr": "2 · Ce que j'apporte"},
    "Arriba. Con qué cuento en esto.": {
        "en": "Above. What I have going for me in this.",
        "fr": "En haut. Ce sur quoi je peux compter là-dedans."},

    "3 · Lo que estorba": {"en": "3 · What hinders", "fr": "3 · Ce qui gêne"},
    "A la izquierda. Y suele ser algo propio.": {
        "en": "On the left. And it is usually something of one's own.",
        "fr": "À gauche. Et c'est en général quelque chose de soi."},

    "4 · El paso": {"en": "4 · The step", "fr": "4 · Le pas"},
}
