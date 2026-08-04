# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · las dos últimas operaciones y la dedicación
========================================================================
Se cierran las siete filas de la tabla con Mercurio y la Luna, y detrás va la
regla que sostiene el capítulo entero: la bajada a lo concreto en veinticuatro
horas. Remite a «la regla de Maljut del capítulo 8» y la remisión se conserva
con el número de capítulo y la transliteración que ya usa el libro —Malkuth en
inglés, Malkhout en francés—, porque el lector tiene que poder volver allí.

Las cuatro armas se nombran con los nombres que ya tienen en el capítulo 6 y
en su lámina: vara/wand/baguette, copa/cup/coupe, espada/sword/épée,
disco/disc/disque. El orden de dedicación —disco, copa, espada, vara— es el
inverso del de las armas y va explicado en el propio párrafo, así que no se
reordena.
"""

T = {
    "Mercurio · miércoles": {"en": "Mercury · Wednesday", "fr": "Mercure · mercredi"},
    "La palabra y el orden": {
        "en": "The word and order", "fr": "La parole et l'ordre"},

    "Lo que hay que decir y no se dice; lo que está sin ordenar": {
        "en": "What has to be said and is not said; what is left unsorted",
        "fr": "Ce qu'il faut dire et que l'on ne dit pas ; ce qui reste sans ordre"},

    "«Voy a decir ___» o «voy a ordenar ___»": {
        "en": "«I am going to say ___» or «I am going to put ___ in order»",
        "fr": "« Je vais dire ___ » ou « je vais mettre ___ en ordre »"},

    "Cuadrado de 8×8 · suma 260 · color naranja o mezcla": {
        "en": "8×8 square · sum 260 · colour orange or mixed",
        "fr": "Carré 8×8 · somme 260 · couleur orange ou mélange"},

    "Luna · lunes": {"en": "Moon · Monday", "fr": "Lune · lundi"},
    "El ritmo y la repetición": {
        "en": "Rhythm and repetition", "fr": "Le rythme et la répétition"},

    "El hábito que falta y el que sobra; el sueño; la casa": {
        "en": "The habit that is missing and the one too many; sleep; the house",
        "fr": "L'habitude qui manque et celle qui est de trop ; le sommeil ; la maison"},

    "«Voy a repetir ___ durante ___ días»": {
        "en": "«I am going to repeat ___ for ___ days»",
        "fr": "« Je vais répéter ___ pendant ___ jours »"},

    "Cuadrado de 9×9 · suma 369 · color plata o blanco": {
        "en": "9×9 square · sum 369 · colour silver or white",
        "fr": "Carré 9×9 · somme 369 · couleur argent ou blanc"},

    "La regla de la comprobación": {
        "en": "The rule of verification", "fr": "La règle de la vérification"},

    "Toda operación planetaria termina con una acción concreta en el mundo, fijada antes de "
    "cerrar y ejecutada en las veinticuatro horas siguientes. Una llamada, una frase dicha, "
    "un cajón vaciado, una hora de sueño más. Sin esa bajada a lo concreto la sesión no ha "
    "ocurrido — es la regla de Maljut del capítulo 8, y es la que impide que todo esto se "
    "convierta en entretenimiento.": {
        "en": "Every planetary operation ends with a concrete action in the world, fixed "
              "before closing and carried out within the next twenty-four hours. A phone call, "
              "a sentence said, a drawer emptied, an hour more of sleep. Without that descent "
              "into the concrete the session has not happened — it is the rule of Malkuth from "
              "chapter 8, and it is what stops all this from turning into entertainment.",
        "fr": "Toute opération planétaire se termine par une action concrète dans le monde, "
              "fixée avant de clore et exécutée dans les vingt-quatre heures qui suivent. Un "
              "appel, une phrase dite, un tiroir vidé, une heure de sommeil en plus. Sans cette "
              "descente dans le concret la séance n'a pas eu lieu — c'est la règle de Malkhout "
              "du chapitre 8, et c'est elle qui empêche tout ceci de devenir un divertissement."},

    # ── La dedicación de los instrumentos ──────────────────────────────────
    "Los grimorios dedican páginas enteras a la fabricación y consagración de instrumentos: "
    "maderas cortadas en día y hora, metales fundidos, tintas preparadas, ceremonias de "
    "horas. Es material fascinante y aquí se reduce deliberadamente a lo que hace efecto.": {
        "en": "The grimoires devote whole pages to the making and consecration of instruments: "
              "woods cut on a given day and hour, molten metals, prepared inks, ceremonies "
              "lasting hours. It is fascinating material and here it is deliberately reduced to "
              "what has an effect.",
        "fr": "Les grimoires consacrent des pages entières à la fabrication et à la "
              "consécration des instruments : bois coupés au jour et à l'heure, métaux fondus, "
              "encres préparées, cérémonies de plusieurs heures. C'est un matériau fascinant et "
              "il est ici délibérément réduit à ce qui fait effet."},

    "Qué hace efecto": {"en": "What has an effect", "fr": "Ce qui fait effet"},

    "Que el objeto no se use para nada más. Eso es todo, y es mucho. Un vaso que solo se toca "
    "dentro del círculo se convierte, en cuestión de semanas, en un disparador fiable: "
    "cogerlo trae consigo el estado entero de la operación. Un vaso que además sirve para el "
    "agua de la mesilla no dispara nada, aunque lo hayas consagrado en luna nueva con siete "
    "velas.": {
        "en": "That the object is used for nothing else. That is all, and it is a great deal. A "
              "glass touched only inside the circle becomes, within a few weeks, a reliable "
              "trigger: picking it up brings with it the whole state of the operation. A glass "
              "that also holds the water on the bedside table triggers nothing, even if you "
              "consecrated it at the new moon with seven candles.",
        "fr": "Que l'objet ne serve à rien d'autre. C'est tout, et c'est beaucoup. Un verre que "
              "l'on ne touche qu'à l'intérieur du cercle devient, en quelques semaines, un "
              "déclencheur fiable : le prendre amène avec lui l'état entier de l'opération. Un "
              "verre qui sert en plus à l'eau de la table de nuit ne déclenche rien, même si "
              "vous l'avez consacré à la nouvelle lune avec sept bougies."},

    "La ceremonia mínima": {
        "en": "The minimum ceremony", "fr": "La cérémonie minimale"},

    "Elige el objeto y decide que es esa arma y no otra. Si dudas entre dos usos posibles, no "
    "es el objeto.": {
        "en": "Choose the object and decide that it is that weapon and no other. If you "
              "hesitate between two possible uses, it is not the object.",
        "fr": "Choisissez l'objet et décidez qu'il est cette arme-là et pas une autre. Si vous "
              "hésitez entre deux usages possibles, ce n'est pas le bon objet."},

    "Límpialo físicamente. Agua y un paño. No es simbólico: es que lo estás mirando de cerca "
    "por primera vez.": {
        "en": "Clean it physically. Water and a cloth. It is not symbolic: it is that you are "
              "looking at it closely for the first time.",
        "fr": "Nettoyez-le physiquement. De l'eau et un chiffon. Ce n'est pas symbolique : c'est "
              "que vous le regardez de près pour la première fois."},

    "Dentro del círculo, después del rito diario, sostenlo en el cuarto que le corresponde y "
    "di en voz alta para qué es y para qué no es. En tus propias palabras, sin fórmula "
    "prestada.": {
        "en": "Inside the circle, after the daily rite, hold it in the quarter that belongs to "
              "it and say aloud what it is for and what it is not for. In your own words, with "
              "no borrowed formula.",
        "fr": "Dans le cercle, après le rite quotidien, tenez-le dans le quartier qui lui revient "
              "et dites à voix haute à quoi il sert et à quoi il ne sert pas. Avec vos propres "
              "mots, sans formule empruntée."},

    "Vocaliza la fórmula del cuarto tres veces con el objeto en la mano.": {
        "en": "Vocalise the formula of the quarter three times with the object in your hand.",
        "fr": "Vocalisez la formule du quartier trois fois, l'objet à la main."},

    "Anótalo en el diario con la fecha. Ese apunte es la consagración: es la prueba de que "
    "hubo un antes y un después.": {
        "en": "Write it down in the journal with the date. That entry is the consecration: it "
              "is the proof that there was a before and an after.",
        "fr": "Notez-le dans le journal avec la date. Cette note est la consécration : elle est "
              "la preuve qu'il y a eu un avant et un après."},

    "Guárdalo en su sitio y no lo uses para nada más. Aquí empieza lo difícil, y es lo único "
    "que de verdad importa.": {
        "en": "Put it away in its place and use it for nothing else. This is where the hard "
              "part begins, and it is the only part that really matters.",
        "fr": "Rangez-le à sa place et ne l'employez à rien d'autre. C'est ici que commence le "
              "difficile, et c'est la seule chose qui compte vraiment."},

    "Si rompes la regla": {
        "en": "If you break the rule", "fr": "Si vous rompez la règle"},

    "Ocurre: un día se usa la copa para beber agua porque estaba a mano. No hay ninguna "
    "consecuencia mágica y sí una consecuencia real: el objeto ha perdido parte de su "
    "capacidad de disparar. Se repara del único modo posible, que es repetir la dedicación y "
    "anotar también eso. Un diario que solo registra los aciertos no sirve para nada.": {
        "en": "It happens: one day the cup gets used to drink water because it was within "
              "reach. There is no magical consequence and there is a real one: the object has "
              "lost part of its capacity to trigger. It is repaired in the only way possible, "
              "which is to repeat the dedication and to write that down too. A journal that "
              "records only the successes is of no use whatever.",
        "fr": "Cela arrive : un jour on se sert de la coupe pour boire de l'eau parce qu'elle "
              "était à portée. Il n'y a aucune conséquence magique et il y en a une réelle : "
              "l'objet a perdu une part de sa capacité à déclencher. Cela se répare de la seule "
              "façon possible, qui est de refaire la dédicace et de noter cela aussi. Un journal "
              "qui n'enregistre que les réussites ne sert à rien."},

    "El orden en que se dedican": {
        "en": "The order in which they are dedicated",
        "fr": "L'ordre dans lequel on les dédie"},

    "Una por mes, y en este orden: disco, copa, espada, vara. De lo concreto a lo abstracto. "
    "Se empieza por el cuerpo porque es donde uno está, y se acaba por la voluntad porque es "
    "la que menos se conoce. Cuatro meses para cuatro objetos parece lento y es exactamente "
    "el ritmo: el objetivo no es tener el equipo completo, es que cada objeto haya tenido "
    "tiempo de significar algo.": {
        "en": "One a month, and in this order: disc, cup, sword, wand. From the concrete to the "
              "abstract. You begin with the body because that is where you are, and you end "
              "with the will because it is the least known. Four months for four objects sounds "
              "slow and it is exactly the right pace: the aim is not to own the complete kit, "
              "it is that each object should have had time to mean something.",
        "fr": "Un par mois, et dans cet ordre : disque, coupe, épée, baguette. Du concret à "
              "l'abstrait. On commence par le corps parce que c'est là qu'on se trouve, et on "
              "finit par la volonté parce que c'est elle que l'on connaît le moins. Quatre mois "
              "pour quatre objets paraît lent et c'est exactement le rythme : le but n'est pas "
              "d'avoir l'équipement complet, c'est que chaque objet ait eu le temps de signifier "
              "quelque chose."},
}
