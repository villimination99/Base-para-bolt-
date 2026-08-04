# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · las horas propias y las veintidós letras
=====================================================================
Los nombres de las letras se transliteran con la grafía habitual de cada
lengua, la misma que ya se usó en el libro de los arcanos: álef es Aleph,
guímel es Gimel y Guimel, dálet es Daleth. Las dos obras comparten catálogo
donde comparten cadena, y donde no la comparten conviene que digan lo mismo de
todos modos.

«Sefer Yetsirá» conserva su transliteración. La regla del reparto —tres, siete
y doce— se enuncia con las tres cifras porque son las mismas sobre las que
está construido el resto del libro, y el párrafo lo dice.
"""

T = {
    "Hora 8": {"en": "Hour 8", "fr": "Heure 8"},
    "Media mañana o mediodía según la estación.": {
        "en": "Mid-morning or noon depending on the season.",
        "fr": "Milieu de matinée ou midi selon la saison."},

    "Hora 15": {"en": "Hour 15", "fr": "Heure 15"},
    "Ya de noche: la tercera hora tras el atardecer.": {
        "en": "Already night: the third hour after sunset.",
        "fr": "Déjà la nuit : la troisième heure après le coucher du soleil."},

    "Hora 22": {"en": "Hour 22", "fr": "Heure 22"},
    "Noche cerrada. La que la tradición reserva para el trabajo largo.": {
        "en": "Deep night. The one the tradition reserves for long work.",
        "fr": "Nuit noire. Celle que la tradition réserve au travail long."},

    "Y la honestidad de este capítulo": {
        "en": "And this chapter's honesty", "fr": "Et l'honnêteté de ce chapitre"},

    "Ninguna de estas horas tiene propiedad alguna. Lo que tiene es estructura: un reparto "
    "fijo, público y verificable que permite decidir cuándo se hace qué sin volver a "
    "decidirlo cada semana. Ese es el valor, y por eso este libro da la tabla completa en "
    "vez de insinuar que hay algo más.": {
        "en": "None of these hours has any property whatever. What it has is structure: a "
              "fixed, public and verifiable distribution that lets you decide when to do what "
              "without having to decide it again every week. That is the value, and that is "
              "why this book gives the complete table instead of hinting that there is "
              "something more.",
        "fr": "Aucune de ces heures n'a la moindre propriété. Ce qu'elle a, c'est une "
              "structure : une répartition fixe, publique et vérifiable qui permet de décider "
              "quand on fait quoi sans avoir à en redécider chaque semaine. Voilà la valeur, et "
              "c'est pourquoi ce livre donne la table complète au lieu d'insinuer qu'il y a "
              "autre chose."},

    # ── Las veintidós letras ───────────────────────────────────────────────
    "El sistema occidental hereda de la cábala un alfabeto de veintidós letras que son a la "
    "vez signos, números y categorías. Es la pieza que permite pasar de una palabra a un "
    "número y de un número a un trazo sobre el cuadrado planetario, y sin ella el capítulo "
    "de los kameas queda a medias.": {
        "en": "The Western system inherits from kabbalah an alphabet of twenty-two letters "
              "that are at once signs, numbers and categories. It is the piece that allows you "
              "to go from a word to a number and from a number to a stroke on the planetary "
              "square, and without it the chapter on the kameas is left half done.",
        "fr": "Le système occidental hérite de la kabbale un alphabet de vingt-deux lettres qui "
              "sont à la fois des signes, des nombres et des catégories. C'est la pièce qui "
              "permet de passer d'un mot à un nombre et d'un nombre à un tracé sur le carré "
              "planétaire, et sans elle le chapitre des kameas reste à moitié fait."},

    '<span class="fig-n">Lám. 8</span> Las veintidós letras con su valor numérico y su '
    "correspondencia según el reparto tres-siete-doce. En amarillo las tres madres, en "
    "naranja las siete dobles y en gris las doce simples.": {
        "en": '<span class="fig-n">Pl. 8</span> The twenty-two letters with their numerical '
              "value and their correspondence according to the three-seven-twelve division. In "
              "yellow the three mothers, in orange the seven doubles and in grey the twelve "
              "simples.",
        "fr": '<span class="fig-n">Pl. 8</span> Les vingt-deux lettres avec leur valeur '
              "numérique et leur correspondance selon la répartition trois-sept-douze. En jaune "
              "les trois mères, en orange les sept doubles et en gris les douze simples."},

    "El reparto tres, siete y doce": {
        "en": "The three, seven and twelve division",
        "fr": "La répartition trois, sept et douze"},

    "El «Sefer Yetsirá» —un texto brevísimo, de fecha discutida y en cualquier caso muy "
    "anterior al año 1000— divide las veintidós letras en tres grupos, y la división es de "
    "una economía notable: tres madres para los tres elementos que no son la tierra, siete "
    "dobles para los siete planetas y doce simples para los doce signos. Tres, siete y doce: "
    "exactamente las tres cifras sobre las que está construido todo lo demás en este libro.": {
        "en": "The «Sefer Yetzirah» —a very short text, of disputed date and in any case much "
              "earlier than the year 1000— divides the twenty-two letters into three groups, "
              "and the division is of a remarkable economy: three mothers for the three "
              "elements that are not earth, seven doubles for the seven planets and twelve "
              "simples for the twelve signs. Three, seven and twelve: exactly the three "
              "figures on which everything else in this book is built.",
        "fr": "Le « Sefer Yetsira » —un texte très bref, de date discutée et en tout cas bien "
              "antérieur à l'an 1000— divise les vingt-deux lettres en trois groupes, et la "
              "division est d'une économie remarquable : trois mères pour les trois éléments "
              "qui ne sont pas la terre, sept doubles pour les sept planètes et douze simples "
              "pour les douze signes. Trois, sept et douze : exactement les trois chiffres sur "
              "lesquels est bâti tout le reste de ce livre."},

    "Los tres grupos": {"en": "The three groups", "fr": "Les trois groupes"},

    "Tres madres": {"en": "Three mothers", "fr": "Trois mères"},
    "Álef, Mem y Shin · Aire, Agua y Fuego. La tierra no recibe letra: en este esquema es lo "
    "que resulta de las otras tres, no un cuarto elemento.": {
        "en": "Aleph, Mem and Shin · Air, Water and Fire. Earth receives no letter: in this "
              "scheme it is what results from the other three, not a fourth element.",
        "fr": "Aleph, Mem et Shin · Air, Eau et Feu. La terre ne reçoit pas de lettre : dans ce "
              "schéma elle est ce qui résulte des trois autres, non un quatrième élément."},

    "Siete dobles": {"en": "Seven doubles", "fr": "Sept doubles"},
    "Bet, Guímel, Dálet, Kaf, Pe, Resh y Tav · los siete planetas. Se llaman dobles porque "
    "en hebreo admiten dos pronunciaciones, una dura y una suave.": {
        "en": "Beth, Gimel, Daleth, Kaph, Pe, Resh and Tav · the seven planets. They are "
              "called doubles because in Hebrew they admit two pronunciations, one hard and "
              "one soft.",
        "fr": "Beth, Guimel, Daleth, Kaph, Pé, Resh et Tav · les sept planètes. On les appelle "
              "doubles parce qu'en hébreu elles admettent deux prononciations, une dure et une "
              "douce."},

    "Doce simples": {"en": "Twelve simples", "fr": "Douze simples"},
    "Las doce restantes · los doce signos, en el orden de la rueda, de He para Aries a Qof "
    "para Piscis.": {
        "en": "The remaining twelve · the twelve signs, in the order of the wheel, from He for "
              "Aries to Qoph for Pisces.",
        "fr": "Les douze restantes · les douze signes, dans l'ordre de la roue, de Hé pour le "
              "Bélier à Qoph pour les Poissons."},

    "Los números": {"en": "The numbers", "fr": "Les nombres"},

    "Cada letra vale un número, y la serie es de una regularidad total: las nueve primeras "
    "van del uno al nueve, las nueve siguientes de diez en diez hasta el noventa, y las "
    "cuatro últimas de cien en cien hasta el cuatrocientos. Nueve unidades, nueve decenas, "
    "cuatro centenas: veintidós letras que cubren todo el sistema de numeración.": {
        "en": "Each letter is worth a number, and the series is of total regularity: the first "
              "nine run from one to nine, the next nine in tens up to ninety, and the last "
              "four in hundreds up to four hundred. Nine units, nine tens, four hundreds: "
              "twenty-two letters covering the whole system of numeration.",
        "fr": "Chaque lettre vaut un nombre, et la série est d'une régularité totale : les neuf "
              "premières vont de un à neuf, les neuf suivantes de dix en dix jusqu'à "
              "quatre-vingt-dix, et les quatre dernières de cent en cent jusqu'à quatre cents. "
              "Neuf unités, neuf dizaines, quatre centaines : vingt-deux lettres qui couvrent "
              "tout le système de numération."},

    "La suma de los veintidós valores es 1 495. Es un dato comprobable con una calculadora y "
    "sirve como verificación: si copias la tabla a tu diario y no te sale esa cifra, has "
    "copiado mal alguna fila.": {
        "en": "The sum of the twenty-two values is 1,495. It is a fact checkable with a "
              "calculator and it serves as a verification: if you copy the table into your "
              "journal and do not get that figure, you have copied a row wrongly.",
        "fr": "La somme des vingt-deux valeurs vaut 1 495. C'est une donnée vérifiable à la "
              "calculatrice et elle sert de contrôle : si vous recopiez la table dans votre "
              "journal et que vous n'obtenez pas ce chiffre, vous avez mal recopié une ligne."},

    "Para qué sirve, en concreto": {
        "en": "What it is for, specifically", "fr": "À quoi cela sert, concrètement"},

    "Escribe la palabra o el nombre de tu operación en letras hebreas transliteradas, o "
    "simplemente asigna a cada letra de tu alfabeto el valor de la letra hebrea equivalente. "
    "Lo segundo es menos ortodoxo y perfectamente utilizable.": {
        "en": "Write the word or the name of your operation in transliterated Hebrew letters, "
              "or simply assign to each letter of your own alphabet the value of the "
              "equivalent Hebrew letter. The second is less orthodox and perfectly usable.",
        "fr": "Écrivez le mot ou le nom de votre opération en lettres hébraïques translittérées, "
              "ou attribuez simplement à chaque lettre de votre alphabet la valeur de la lettre "
              "hébraïque équivalente. La seconde façon est moins orthodoxe et parfaitement "
              "utilisable."},

    "Suma los valores. Obtienes un número.": {
        "en": "Add up the values. You get a number.",
        "fr": "Additionnez les valeurs. Vous obtenez un nombre."},

    "Reduce ese número al rango del cuadrado del planeta con el que trabajas: si el cuadrado "
    "es de 3×3, los números van del 1 al 9; si es de 9×9, del 1 al 81.": {
        "en": "Reduce that number to the range of the square of the planet you are working "
              "with: if the square is 3×3, the numbers run from 1 to 9; if it is 9×9, from 1 "
              "to 81.",
        "fr": "Réduisez ce nombre à l'intervalle du carré de la planète avec laquelle vous "
              "travaillez : si le carré est 3×3, les nombres vont de 1 à 9 ; s'il est 9×9, de 1 "
              "à 81."},
}
