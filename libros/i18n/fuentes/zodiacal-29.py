# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · el calendario del recorrido y el ciclo lunar
==============================================================
Las doce prácticas del calendario son de dos o tres palabras cada una y van en
la columna estrecha de la tabla, enfrentadas al mes y al signo. Se traducen
igual de escuetas: son etiquetas, no frases.

La tercera regla del recorrido —no se salta el signo incómodo— dice que la
práctica que parezca innecesaria o ridícula es casi con total seguridad la que
más falta hace. La certeza es del original y se conserva sin rebajarla.

El capítulo de la Luna se abre declarando lo que no afirma: nada sobre la
influencia física de la Luna, ese debate pertenece a la ciencia y no a este
libro. La delimitación va entera, porque es lo que permite dar el calendario
sin prometer nada con él.
"""

T = {
    "Pedir en voz alta": {"en": "Asking aloud", "fr": "Demander à voix haute"},

    "Mes 5 · Leo": {"en": "Month 5 · Leo", "fr": "Mois 5 · Lion"},
    "Hacer sin público": {"en": "Doing with no audience", "fr": "Faire sans public"},

    "Mes 6 · Virgo": {"en": "Month 6 · Virgo", "fr": "Mois 6 · Vierge"},
    "Entregar imperfecto": {
        "en": "Delivering imperfect", "fr": "Rendre imparfait"},

    "Mes 7 · Libra": {"en": "Month 7 · Libra", "fr": "Mois 7 · Balance"},
    "Decidir y sostener": {
        "en": "Deciding and holding to it", "fr": "Décider et tenir"},

    "Mes 8 · Escorpio": {"en": "Month 8 · Scorpio", "fr": "Mois 8 · Scorpion"},
    "Mostrar algo propio": {
        "en": "Showing something of your own", "fr": "Montrer quelque chose de soi"},

    "Mes 9 · Sagitario": {"en": "Month 9 · Sagittarius", "fr": "Mois 9 · Sagittaire"},
    "Sostener cuatro semanas": {
        "en": "Sustaining four weeks", "fr": "Tenir quatre semaines"},

    "Mes 10 · Capricornio": {"en": "Month 10 · Capricorn", "fr": "Mois 10 · Capricorne"},
    "Descansar sin producir": {
        "en": "Resting without producing", "fr": "Se reposer sans produire"},

    "Mes 11 · Acuario": {"en": "Month 11 · Aquarius", "fr": "Mois 11 · Verseau"},
    "Estar presente con alguien": {
        "en": "Being present with somebody", "fr": "Être présent avec quelqu'un"},

    "Mes 12 · Piscis": {"en": "Month 12 · Pisces", "fr": "Mois 12 · Poissons"},
    "Decir no": {"en": "Saying no", "fr": "Dire non"},

    "Puedes empezar en el mes zodiacal que corresponda a la fecha en que abras el libro, o "
    "empezar por Aries en marzo para que el recorrido coincida con el ciclo natural. La "
    "segunda opción tiene una ventaja: el signo del mes está «en el aire», y el trabajo se "
    "apoya en la estación.": {
        "en": "You can begin in whichever zodiacal month corresponds to the date you open the "
              "book, or begin with Aries in March so that the journey coincides with the "
              "natural cycle. The second option has an advantage: the month's sign is «in the "
              "air», and the work leans on the season.",
        "fr": "Vous pouvez commencer au mois zodiacal qui correspond à la date où vous ouvrez le "
              "livre, ou commencer par le Bélier en mars pour que le parcours coïncide avec le "
              "cycle naturel. La seconde option a un avantage : le signe du mois est « dans "
              "l'air », et le travail s'appuie sur la saison."},

    "Las tres reglas del recorrido": {
        "en": "The three rules of the journey", "fr": "Les trois règles du parcours"},

    "Una práctica por mes. No dos. La tentación de acelerar es exactamente el patrón que este "
    "método corrige.": {
        "en": "One practice a month. Not two. The temptation to speed up is exactly the pattern "
              "this method corrects.",
        "fr": "Une pratique par mois. Pas deux. La tentation d'accélérer est exactement le schéma "
              "que cette méthode corrige."},

    "Se escribe. Las tres preguntas del final de cada signo se responden por escrito, a mano, "
    "el último día del mes. Sin escribir no hay recorrido: hay buenas intenciones.": {
        "en": "It gets written. The three questions at the end of each sign are answered in "
              "writing, by hand, on the last day of the month. Without writing there is no "
              "journey: there are good intentions.",
        "fr": "On écrit. Les trois questions de la fin de chaque signe se répondent par écrit, à "
              "la main, le dernier jour du mois. Sans écrire il n'y a pas de parcours : il y a "
              "de bonnes intentions."},

    "No se salta el signo incómodo. El signo cuya práctica te parezca innecesaria o ridícula "
    "es, casi con total seguridad, el que más te hace falta.": {
        "en": "The uncomfortable sign does not get skipped. The sign whose practice strikes you "
              "as unnecessary or ridiculous is, almost certainly, the one you most need.",
        "fr": "On ne saute pas le signe inconfortable. Le signe dont la pratique vous paraît "
              "inutile ou ridicule est, presque à coup sûr, celui dont vous avez le plus besoin."},

    "Este recorrido no cambia tu carácter, y desconfía de cualquier libro que prometa eso. Lo "
    "que hace es más modesto y más real: te muestra doce formas de operar, te obliga a "
    "practicar las que no usas y te deja un registro escrito de lo que observaste. Al final "
    "del año tendrás doce páginas de tu puño y letra sobre ti mismo. Vale más que cualquier "
    "interpretación ajena.": {
        "en": "This journey does not change your character, and be wary of any book that "
              "promises it will. What it does is more modest and more real: it shows you twelve "
              "ways of operating, obliges you to practise the ones you do not use and leaves "
              "you a written record of what you observed. At the end of the year you will have "
              "twelve pages in your own hand about yourself. That is worth more than anybody "
              "else's interpretation.",
        "fr": "Ce parcours ne change pas votre caractère, et méfiez-vous de tout livre qui "
              "promettrait cela. Ce qu'il fait est plus modeste et plus réel : il vous montre "
              "douze façons d'opérer, vous oblige à pratiquer celles que vous n'employez pas et "
              "vous laisse une trace écrite de ce que vous avez observé. À la fin de l'année "
              "vous aurez douze pages de votre main sur vous-même. Cela vaut mieux que "
              "n'importe quelle interprétation venue d'autrui."},

    # ── La Luna y sus ocho fases ───────────────────────────────────────────
    "Capítulo 27": {"en": "Chapter 27", "fr": "Chapitre 27"},

    "De los siete cuerpos clásicos, la Luna es el único cuyo ciclo se puede seguir a simple "
    "vista sin instrumentos y sin tablas. Veintinueve días y medio, ocho fases reconocibles, y "
    "una correspondencia con el ritmo del trabajo humano que llevó a repartir las tareas del "
    "campo según su curso en casi todas las culturas agrícolas conocidas.": {
        "en": "Of the seven classical bodies, the Moon is the only one whose cycle can be "
              "followed with the naked eye, with no instruments and no tables. Twenty-nine and "
              "a half days, eight recognisable phases, and a correspondence with the rhythm of "
              "human work that led almost every known agricultural culture to distribute the "
              "tasks of the fields according to its course.",
        "fr": "Des sept corps classiques, la Lune est le seul dont le cycle se suive à l'œil nu, "
              "sans instruments et sans tables. Vingt-neuf jours et demi, huit phases "
              "reconnaissables, et une correspondance avec le rythme du travail humain qui a "
              "conduit presque toutes les cultures agricoles connues à répartir les travaux des "
              "champs selon sa course."},

    "Lo que sigue no es una afirmación sobre la influencia física de la Luna en las plantas ni "
    "en el cuerpo — ese debate pertenece a la ciencia y no a este libro. Es algo distinto y "
    "perfectamente utilizable: un calendario de cuatro semanas con un verbo distinto en cada "
    "tramo. Su valor no está en la Luna: está en tener una estructura de veintinueve días que "
    "se repite sin que haya que decidirla.": {
        "en": "What follows is not a claim about the physical influence of the Moon on plants "
              "or on the body — that debate belongs to science and not to this book. It is "
              "something different and perfectly usable: a four-week calendar with a different "
              "verb in each stretch. Its value does not lie in the Moon: it lies in having a "
              "twenty-nine-day structure that repeats without having to be decided.",
        "fr": "Ce qui suit n'est pas une affirmation sur l'influence physique de la Lune sur les "
              "plantes ni sur le corps — ce débat appartient à la science et non à ce livre. "
              "C'est autre chose et parfaitement utilisable : un calendrier de quatre semaines "
              "avec un verbe différent à chaque tronçon. Sa valeur n'est pas dans la Lune : elle "
              "est dans le fait d'avoir une structure de vingt-neuf jours qui se répète sans "
              "qu'il faille la décider."},

    '<span class="fig-n">Lám. 7</span> Las ocho fases y el verbo que la tradición asocia a cada '
    "una. De izquierda a derecha: cuatro fases crecientes y cuatro menguantes.": {
        "en": '<span class="fig-n">Pl. 7</span> The eight phases and the verb the tradition '
              "associates with each. From left to right: four waxing phases and four waning.",
        "fr": '<span class="fig-n">Pl. 7</span> Les huit phases et le verbe que la tradition '
              "associe à chacune. De gauche à droite : quatre phases croissantes et quatre "
              "décroissantes."},

    "El ciclo como estructura de trabajo": {
        "en": "The cycle as a working structure",
        "fr": "Le cycle comme structure de travail"},

    "Los ocho tramos y su tarea": {
        "en": "The eight stretches and their task",
        "fr": "Les huit tronçons et leur tâche"},

    "Luna nueva": {"en": "New moon", "fr": "Nouvelle lune"},
}
