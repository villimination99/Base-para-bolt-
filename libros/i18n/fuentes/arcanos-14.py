# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · el Espejo y el capítulo de la carta invertida
=====================================================================
La cifra de 156 posiciones sale de multiplicar las setenta y ocho cartas por
sus dos orientaciones, y va idéntica en los tres idiomas: es una cuenta que el
lector puede rehacer, no una manera de decir «muchas».

Las cuatro formas de leer una inversión —exceso, defecto, bloqueo y la cuarta—
se nombran con sustantivos secos en las tres lenguas. Son etiquetas de una
lista que se consulta con la carta delante, y un giro más literario las haría
menos localizables.
"""

T = {
    "Abajo. La acción concreta que toca ahora.": {
        "en": "Below. The concrete action called for now.",
        "fr": "En bas. L'action concrète qui s'impose maintenant."},

    "El Espejo": {"en": "The Mirror", "fr": "Le Miroir"},
    "La más incómoda y la más útil en conflictos con otra persona. Tres cartas.": {
        "en": "The most uncomfortable and the most useful in conflicts with another person. "
              "Three cards.",
        "fr": "Le plus inconfortable et le plus utile dans les conflits avec une autre "
              "personne. Trois cartes."},

    "El Espejo · posiciones": {
        "en": "The Mirror · positions", "fr": "Le Miroir · positions"},

    "1 · Como lo veo": {"en": "1 · As I see it", "fr": "1 · Comme je le vois"},
    "Mi versión del asunto.": {
        "en": "My version of the matter.", "fr": "Ma version de l'affaire."},

    "2 · Como lo ve el otro": {
        "en": "2 · As the other sees it", "fr": "2 · Comme l'autre le voit"},
    "Su versión. Esta carta se lee entera antes de discutirla.": {
        "en": "Their version. This card is read all the way through before being argued with.",
        "fr": "Sa version. Cette carte se lit en entier avant d'être discutée."},

    "3 · Lo que ninguno ve": {
        "en": "3 · What neither sees", "fr": "3 · Ce qu'aucun ne voit"},
    "El punto ciego compartido. Es la posición que justifica la tirada.": {
        "en": "The shared blind spot. It is the position that justifies the spread.",
        "fr": "L'angle mort partagé. C'est la position qui justifie le tirage."},

    "Sobre la segunda posición del Espejo": {
        "en": "On the Mirror's second position",
        "fr": "Sur la deuxième position du Miroir"},

    "No informa de lo que la otra persona piensa: no hay manera de que un mazo sepa eso. Lo "
    "que hace es obligarte a construir su versión con material que no has elegido, y eso "
    "produce un ejercicio de perspectiva que la reflexión espontánea casi nunca produce. Es "
    "la misma lógica de cualquier examen de conciencia con estructura, con otras "
    "herramientas.": {
        "en": "It does not report what the other person thinks: there is no way a deck could "
              "know that. What it does is force you to build their version out of material you "
              "did not choose, and that produces an exercise in perspective that spontaneous "
              "reflection almost never produces. It is the same logic as any structured "
              "examination of conscience, with different tools.",
        "fr": "Elle ne renseigne pas sur ce que pense l'autre personne : un jeu n'a aucun moyen "
              "de le savoir. Ce qu'elle fait, c'est vous obliger à construire sa version avec "
              "un matériau que vous n'avez pas choisi, et cela produit un exercice de "
              "perspective que la réflexion spontanée ne produit presque jamais. C'est la même "
              "logique que n'importe quel examen de conscience structuré, avec d'autres "
              "outils."},

    "La regla del número de cartas": {
        "en": "The rule about the number of cards",
        "fr": "La règle du nombre de cartes"},

    "Pocas. Tres o cuatro para casi todo, y nunca más de siete. Una tirada de diez u once "
    "cartas da tanta información que se puede construir con ella cualquier relato, y ahí se "
    "pierde el instrumento. La restricción es lo que obliga a la precisión — la misma razón "
    "por la que un buen diagnóstico usa pocas pruebas bien elegidas.": {
        "en": "Few. Three or four for almost everything, and never more than seven. A spread of "
              "ten or eleven cards gives so much information that any story at all can be "
              "built from it, and there the instrument is lost. The constraint is what forces "
              "precision — the same reason a good diagnosis uses few well-chosen tests.",
        "fr": "Peu. Trois ou quatre pour presque tout, et jamais plus de sept. Un tirage de dix "
              "ou onze cartes donne tant d'information qu'on peut en construire n'importe quel "
              "récit, et l'instrument s'y perd. La contrainte est ce qui oblige à la précision "
              "— la même raison pour laquelle un bon diagnostic emploie peu d'examens bien "
              "choisis."},

    # ── La carta invertida ─────────────────────────────────────────────────
    "Un capítulo corto sobre una cuestión que divide a los lectores y que conviene resolver "
    "antes de empezar, porque hay que elegir y mantenerse.": {
        "en": "A short chapter on a question that divides readers and is worth settling before "
              "you start, because you have to choose and stick to it.",
        "fr": "Un court chapitre sur une question qui divise les lecteurs et qu'il vaut mieux "
              "trancher avant de commencer, parce qu'il faut choisir et s'y tenir."},

    "Las dos escuelas": {"en": "The two schools", "fr": "Les deux écoles"},
    "Con inversiones y sin ellas": {
        "en": "With reversals and without", "fr": "Avec inversions et sans"},

    "Con inversiones": {"en": "With reversals", "fr": "Avec inversions"},
    "Cada carta tiene dos lecturas según su orientación. Duplica el vocabulario a 156 "
    "posiciones y afina mucho, a costa de complicar el aprendizaje.": {
        "en": "Each card has two readings according to its orientation. It doubles the "
              "vocabulary to 156 positions and sharpens things considerably, at the cost of "
              "complicating the learning.",
        "fr": "Chaque carte a deux lectures selon son orientation. Cela double le vocabulaire à "
              "156 positions et affine beaucoup, au prix d'un apprentissage plus compliqué."},

    "Sin inversiones": {"en": "Without reversals", "fr": "Sans inversions"},
    "Todas las cartas se leen derechas y el matiz lo dan las cartas vecinas. Más simple, y "
    "algunos lectores muy buenos no usan otra cosa.": {
        "en": "All cards are read upright and the nuance comes from the neighbouring cards. "
              "Simpler, and some very good readers use nothing else.",
        "fr": "Toutes les cartes se lisent à l'endroit et la nuance vient des cartes voisines. "
              "Plus simple, et certains très bons lecteurs n'emploient rien d'autre."},

    "Este libro trabaja con inversiones, y da la lectura invertida de los veintidós mayores "
    "en los capítulos 5 al 8. Se elige así porque una carta invertida obliga a mirar el "
    "lado incómodo de la figura, y ese lado es justo el que un lector complaciente se "
    "salta.": {
        "en": "This book works with reversals, and gives the reversed reading of the "
              "twenty-two majors in chapters 5 to 8. It is chosen this way because a reversed "
              "card forces you to look at the uncomfortable side of the figure, and that side "
              "is precisely the one an indulgent reader skips.",
        "fr": "Ce livre travaille avec les inversions, et donne la lecture inversée des "
              "vingt-deux majeurs aux chapitres 5 à 8. Ce choix vient de ce qu'une carte "
              "inversée oblige à regarder le côté inconfortable de la figure, et ce côté est "
              "justement celui qu'un lecteur complaisant saute."},

    "Las cuatro formas de leer una inversión": {
        "en": "The four ways of reading a reversal",
        "fr": "Les quatre façons de lire une inversion"},

    "El exceso. La misma cualidad pasada de punto: la Fuerza que ya es terquedad, la "
    "Templanza que ya es tibieza. Es la lectura más frecuente y la que casi siempre "
    "funciona.": {
        "en": "Excess. The same quality taken too far: Strength that has become stubbornness, "
              "Temperance that has become lukewarmness. It is the commonest reading and the "
              "one that almost always works.",
        "fr": "L'excès. La même qualité poussée trop loin : la Force devenue entêtement, la "
              "Tempérance devenue tiédeur. C'est la lecture la plus fréquente et celle qui "
              "fonctionne presque toujours."},

    "El defecto. La cualidad que falta o no llega: el Emperador invertido como ausencia de "
    "estructura.": {
        "en": "Deficiency. The quality that is missing or falls short: the Emperor reversed as "
              "an absence of structure.",
        "fr": "Le défaut. La qualité qui manque ou n'arrive pas : l'Empereur inversé comme "
              "absence de structure."},

    "El bloqueo. La energía de la carta existe y no circula. Muy útil en posiciones de «lo "
    "que estorba».": {
        "en": "Blockage. The card's energy exists and does not circulate. Very useful in «what "
              "hinders» positions.",
        "fr": "Le blocage. L'énergie de la carte existe et ne circule pas. Très utile dans les "
              "positions « ce qui gêne »."},
}
