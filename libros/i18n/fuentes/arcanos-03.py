# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · la cronología y la estructura de las setenta y ocho
===========================================================================
El «Sefer Yetsirá» conserva su transliteración en las tres lenguas, con la
grafía habitual de cada una. «Tarocchi» se queda en italiano por el mismo
motivo que «trionfi» en el módulo anterior: el párrafo trata precisamente de
cuándo una palabra sustituyó a la otra.

Los nombres de las personas —Court de Gébelin, Etteilla, Lévi, Papus— y las
fechas no se tocan. Son la prueba del capítulo: un lector que quiera
desmentirlo tiene que poder buscar exactamente esos nombres y esos años.
"""

T = {
    "Siglo XVI": {"en": "Sixteenth century", "fr": "XVIe siècle"},
    "El juego se difunde. La palabra «tarocchi» sustituye a «trionfi». No hay una sola "
    "mención a adivinación en doscientos años de documentos.": {
        "en": "The game spreads. The word «tarocchi» replaces «trionfi». There is not a single "
              "mention of divination in two hundred years of documents.",
        "fr": "Le jeu se diffuse. Le mot « tarocchi » remplace « trionfi ». Il n'y a pas une "
              "seule mention de divination en deux cents ans de documents."},

    "Siglos XVII–XVIII": {
        "en": "Seventeenth–eighteenth centuries", "fr": "XVIIe–XVIIIe siècles"},
    "Se estabiliza en Francia el patrón que hoy llamamos de Marsella: los mismos veintidós "
    "triunfos, con los mismos nombres y en el mismo orden, grabados en madera y baratos.": {
        "en": "The pattern we now call Marseille settles in France: the same twenty-two "
              "trumps, with the same names and in the same order, woodcut and cheap.",
        "fr": "Se stabilise en France le patron que nous appelons aujourd'hui de Marseille : "
              "les mêmes vingt-deux triomphes, avec les mêmes noms et dans le même ordre, "
              "gravés sur bois et bon marché."},

    "Antoine Court de Gébelin publica un ensayo donde afirma que el tarot es un libro "
    "egipcio superviviente. No aporta ninguna prueba. Es el momento en que nace todo lo "
    "demás.": {
        "en": "Antoine Court de Gébelin publishes an essay claiming that tarot is a surviving "
              "Egyptian book. He offers no evidence at all. That is the moment everything else "
              "is born.",
        "fr": "Antoine Court de Gébelin publie un essai où il affirme que le tarot est un "
              "livre égyptien rescapé. Il n'apporte aucune preuve. C'est le moment où naît "
              "tout le reste."},

    "Etteilla convierte esa idea en oficio y publica el primer método de lectura "
    "cartomántica.": {
        "en": "Etteilla turns that idea into a trade and publishes the first method of "
              "cartomantic reading.",
        "fr": "Etteilla fait de cette idée un métier et publie la première méthode de lecture "
              "cartomancienne."},

    "Éliphas Lévi ata los veintidós mayores a las veintidós letras hebreas. Es la "
    "aportación estructural decisiva, y es una invención del siglo XIX, no una tradición "
    "antigua.": {
        "en": "Éliphas Lévi ties the twenty-two major arcana to the twenty-two Hebrew letters. "
              "It is the decisive structural contribution, and it is a nineteenth-century "
              "invention, not an ancient tradition.",
        "fr": "Éliphas Lévi lie les vingt-deux majeurs aux vingt-deux lettres hébraïques. "
              "C'est l'apport structurel décisif, et c'est une invention du XIXe siècle, non "
              "une tradition ancienne."},

    "Papus sistematiza el conjunto en un libro que sigue siendo la referencia continental.": {
        "en": "Papus systematises the whole in a book that remains the continental reference.",
        "fr": "Papus systématise l'ensemble dans un livre qui reste la référence continentale."},

    "Las dos consecuencias de saber esto": {
        "en": "The two consequences of knowing this",
        "fr": "Les deux conséquences de savoir cela"},

    "La primera es de honestidad: cualquiera que te venda el tarot como sabiduría milenaria "
    "egipcia está repitiendo, sin saberlo, una afirmación que un erudito francés hizo sin "
    "pruebas en 1781. Los mazos son europeos, renacentistas y empezaron siendo un juego de "
    "mesa.": {
        "en": "The first is a matter of honesty: anyone selling you tarot as millennia-old "
              "Egyptian wisdom is repeating, without knowing it, a claim a French scholar made "
              "without evidence in 1781. The decks are European, Renaissance, and they started "
              "out as a parlour game.",
        "fr": "La première relève de l'honnêteté : quiconque vous vend le tarot comme une "
              "sagesse égyptienne millénaire répète, sans le savoir, une affirmation qu'un "
              "érudit français a faite sans preuve en 1781. Les jeux sont européens, "
              "renaissants, et ils ont commencé comme un jeu de société."},

    "La segunda es más útil y bastante liberadora: si la estructura simbólica del tarot se "
    "construyó en el siglo XIX, entonces es una construcción deliberada, hecha por gente "
    "que sabía lo que hacía y con un criterio que se puede examinar. Y una construcción "
    "examinable es infinitamente más utilizable que una revelación. Se puede aprender, "
    "discutir, y corregir donde falle.": {
        "en": "The second is more useful and rather liberating: if tarot's symbolic structure "
              "was built in the nineteenth century, then it is a deliberate construction, made "
              "by people who knew what they were doing and to a criterion that can be "
              "examined. And an examinable construction is infinitely more usable than a "
              "revelation. It can be learnt, argued with, and corrected where it fails.",
        "fr": "La seconde est plus utile et assez libératrice : si la structure symbolique du "
              "tarot a été construite au XIXe siècle, alors c'est une construction délibérée, "
              "faite par des gens qui savaient ce qu'ils faisaient et selon un critère que "
              "l'on peut examiner. Et une construction examinable est infiniment plus "
              "utilisable qu'une révélation. On peut l'apprendre, la discuter, et la corriger "
              "là où elle faiblit."},

    "Lo que sí es antiguo": {"en": "What is genuinely old", "fr": "Ce qui est bien ancien"},

    "El material con el que Lévi construyó. Las veintidós letras y su reparto vienen del "
    "«Sefer Yetsirá», anterior al año mil. Los cuatro elementos y los treinta y seis "
    "decanatos vienen de la astrología helenística, siglo II. Las figuras de los triunfos "
    "—la Muerte, la Rueda de la Fortuna, la Templanza— son iconografía medieval corriente, "
    "de la que había en iglesias y en libros. Antiguo es el material; moderno es el "
    "montaje. Y el montaje es bueno.": {
        "en": "The material Lévi built with. The twenty-two letters and their division come "
              "from the «Sefer Yetzirah», earlier than the year one thousand. The four "
              "elements and the thirty-six decans come from Hellenistic astrology, second "
              "century. The trump figures —Death, the Wheel of Fortune, Temperance— are "
              "ordinary medieval iconography, the kind found in churches and in books. The "
              "material is old; the assembly is modern. And the assembly is good.",
        "fr": "Le matériau avec lequel Lévi a construit. Les vingt-deux lettres et leur "
              "répartition viennent du « Sefer Yetsira », antérieur à l'an mil. Les quatre "
              "éléments et les trente-six décans viennent de l'astrologie hellénistique, "
              "IIe siècle. Les figures des triomphes —la Mort, la Roue de Fortune, la "
              "Tempérance— sont de l'iconographie médiévale courante, celle qu'on trouvait "
              "dans les églises et dans les livres. Le matériau est ancien ; le montage est "
              "moderne. Et le montage est bon."},

    # ── Capítulo 3 · la estructura ─────────────────────────────────────────
    "Antes de una sola lectura, la arquitectura. Un mazo de tarot no son setenta y ocho "
    "cartas sueltas: son dos sistemas encajados, y confundirlos es el primer error del "
    "principiante.": {
        "en": "Before a single reading, the architecture. A tarot deck is not seventy-eight "
              "loose cards: it is two systems fitted together, and confusing them is the "
              "beginner's first mistake.",
        "fr": "Avant la moindre lecture, l'architecture. Un jeu de tarot n'est pas "
              "soixante-dix-huit cartes éparses : ce sont deux systèmes emboîtés, et les "
              "confondre est la première erreur du débutant."},

    '<span class="fig-n">Lám. 1</span> Las setenta y ocho. Arriba, los veintidós mayores '
    "como serie única. Abajo, los cuatro palos, cada uno con su as, sus nueve numerales y "
    "sus cuatro figuras.": {
        "en": '<span class="fig-n">Pl. 1</span> The seventy-eight. Above, the twenty-two '
              "major arcana as a single series. Below, the four suits, each with its ace, its "
              "nine numerals and its four court cards.",
        "fr": '<span class="fig-n">Pl. 1</span> Les soixante-dix-huit. En haut, les '
              "vingt-deux majeurs comme série unique. En bas, les quatre couleurs, chacune "
              "avec son as, ses neuf numérales et ses quatre figures."},

    "Los dos sistemas": {"en": "The two systems", "fr": "Les deux systèmes"},

    "22 arcanos mayores": {"en": "22 major arcana", "fr": "22 arcanes majeurs"},
    "Una serie numerada de I a XXI más El Loco. No hay palos ni repeticiones: cada uno es "
    "único y ocupa un lugar en un itinerario.": {
        "en": "A series numbered I to XXI plus The Fool. There are no suits and no "
              "repetitions: each one is unique and occupies a place on a journey.",
        "fr": "Une série numérotée de I à XXI plus Le Mat. Ni couleurs ni répétitions : chacun "
              "est unique et occupe une place dans un parcours."},

    "56 arcanos menores": {"en": "56 minor arcana", "fr": "56 arcanes mineurs"},
    "Cuatro palos de catorce cartas: as, del dos al diez, y cuatro figuras. Estructura de "
    "baraja corriente, con una figura más.": {
        "en": "Four suits of fourteen cards: ace, two to ten, and four court cards. The "
              "structure of an ordinary pack, with one extra court card.",
        "fr": "Quatre couleurs de quatorze cartes : as, du deux au dix, et quatre figures. La "
              "structure d'un jeu ordinaire, avec une figure de plus."},

    "Qué hace cada mitad": {"en": "What each half does", "fr": "Ce que fait chaque moitié"},

    "Los mayores hablan de procesos: etapas, umbrales, cambios de estado. Son pocos y "
    "grandes, y cuando salen en una tirada indican que lo que está en juego no es una "
    "circunstancia sino un tramo del camino.": {
        "en": "The major arcana speak of processes: stages, thresholds, changes of state. They "
              "are few and large, and when they come up in a spread they indicate that what is "
              "at stake is not a circumstance but a stretch of the road.",
        "fr": "Les majeurs parlent de processus : étapes, seuils, changements d'état. Ils sont "
              "peu nombreux et grands, et lorsqu'ils sortent dans un tirage ils indiquent que "
              "ce qui est en jeu n'est pas une circonstance mais un tronçon du chemin."},

    "Los menores hablan de circunstancias: lo concreto, lo cotidiano, lo que está pasando "
    "esta semana en un área identificable de la vida. Son muchos y pequeños, y por eso una "
    "tirada de solo menores describe una situación y una tirada cargada de mayores "
    "describe un momento.": {
        "en": "The minor arcana speak of circumstances: the concrete, the everyday, what is "
              "happening this week in an identifiable area of life. They are many and small, "
              "and that is why a spread of minors alone describes a situation and a spread "
              "loaded with majors describes a moment.",
        "fr": "Les mineurs parlent de circonstances : le concret, le quotidien, ce qui se passe "
              "cette semaine dans un domaine identifiable de la vie. Ils sont nombreux et "
              "petits, et c'est pourquoi un tirage de mineurs seuls décrit une situation et un "
              "tirage chargé de majeurs décrit un moment."},

    "La proporción como dato de lectura": {
        "en": "The proportion as a reading in itself",
        "fr": "La proportion comme donnée de lecture"},

    "Con veintidós mayores en setenta y ocho cartas, la proporción esperada es de algo "
    "menos de tres por cada diez. Si en una tirada de diez cartas salen seis mayores, eso "
    "ya es información antes de leer ninguna: el asunto es más de fondo de lo que la "
    "pregunta suponía. Y si en una pregunta que parecía vital no sale ninguno, también: "
    "probablemente no era tan vital.": {
        "en": "With twenty-two majors in seventy-eight cards, the expected proportion is a "
              "little under three in every ten. If six majors come up in a ten-card spread, "
              "that is already information before reading any of them: the matter runs deeper "
              "than the question assumed. And if not one comes up in a question that seemed "
              "vital, that is information too: it probably was not that vital.",
        "fr": "Avec vingt-deux majeurs sur soixante-dix-huit cartes, la proportion attendue est "
              "d'un peu moins de trois sur dix. Si dans un tirage de dix cartes il en sort six "
              "majeurs, c'est déjà une information avant d'en lire aucune : l'affaire est plus "
              "profonde que ne le supposait la question. Et si dans une question qui semblait "
              "vitale il n'en sort aucun, c'est une information aussi : elle n'était sans doute "
              "pas si vitale."},

    "El número de cartas y por qué es ese": {
        "en": "The number of cards and why it is that one",
        "fr": "Le nombre de cartes et pourquoi c'est celui-là"},
}
