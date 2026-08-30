# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · el vocabulario y el registro de observación
=============================================================
El vocabulario va ordenado alfabéticamente por la entrada castellana, y ese
orden es del documento, no del traductor: las entradas se traducen en su sitio
y no se reordenan. En inglés y en francés la secuencia sigue siendo alfabética
casi de principio a fin —Ascendant, Aspect, Chaldean, Cardinal…— porque los
términos son cultos y comparten raíz en las tres lenguas; las dos o tres
entradas que se salen de sitio no estorban a un capítulo que, como él mismo
dice, es para volver y no para leer de corrido.

Las definiciones conservan sus grados —180°, 120°, 90°, 60°— y la advertencia
de la melotesia: sistema simbólico y mnemotécnico, nunca diagnóstico. Esa
coma final es la que mantiene el vocabulario dentro de lo que el libro
sostiene.

La última pregunta del cuaderno se declara «la única trampa del libro» y su
explicación cierra la obra. Se traduce entera, incluida la frase final: el
zodiaco no es una etiqueta que se recibe al nacer sino un repertorio que se
aprende a usar.
"""

T = {
    "Capítulo 30": {"en": "Chapter 30", "fr": "Chapitre 30"},

    "Los términos que aparecen en este libro, definidos con la precisión suficiente para leer "
    "cualquier otro tratado sin perderse. Van en orden alfabético y no de aparición: es un "
    "capítulo para volver, no para leer de corrido.": {
        "en": "The terms that appear in this book, defined precisely enough to read any other "
              "treatise without getting lost. They go in alphabetical order and not in order of "
              "appearance: it is a chapter to come back to, not to read straight through.",
        "fr": "Les termes qui paraissent dans ce livre, définis avec assez de précision pour lire "
              "n'importe quel autre traité sans s'y perdre. Ils vont dans l'ordre alphabétique "
              "et non dans celui de leur apparition : c'est un chapitre où revenir, non à lire "
              "d'une traite."},

    "Ascendente": {"en": "Ascendant", "fr": "Ascendant"},
    "Signo que asomaba por el horizonte este en el momento del nacimiento. Cambia cada dos "
    "horas aproximadamente y describe la manera de aparecer y de entrar en las situaciones. "
    "Requiere hora exacta.": {
        "en": "The sign rising over the eastern horizon at the moment of birth. It changes "
              "roughly every two hours and describes the way of appearing and of entering "
              "situations. It requires an exact time.",
        "fr": "Signe qui pointait à l'horizon est au moment de la naissance. Il change environ "
              "toutes les deux heures et décrit la façon d'apparaître et d'entrer dans les "
              "situations. Il exige l'heure exacte."},

    "Aspecto": {"en": "Aspect", "fr": "Aspect"},
    "Distancia angular entre dos puntos de la rueda, medida en grados. Los cuatro mayores son "
    "oposición (180°), trígono (120°), cuadratura (90°) y sextil (60°).": {
        "en": "Angular distance between two points on the wheel, measured in degrees. The four "
              "major ones are the opposition (180°), the trine (120°), the square (90°) and the "
              "sextile (60°).",
        "fr": "Distance angulaire entre deux points de la roue, mesurée en degrés. Les quatre "
              "majeurs sont l'opposition (180°), le trigone (120°), le carré (90°) et le sextile "
              "(60°)."},

    "Caldeo (orden)": {"en": "Chaldean (order)", "fr": "Chaldéen (ordre)"},
    "Los siete planetas clásicos ordenados por lentitud aparente: Saturno, Júpiter, Marte, "
    "Sol, Venus, Mercurio, Luna. Rige el reparto de decanatos y de horas planetarias.": {
        "en": "The seven classical planets arranged by apparent slowness: Saturn, Jupiter, "
              "Mars, Sun, Venus, Mercury, Moon. It governs the distribution of decans and of "
              "planetary hours.",
        "fr": "Les sept planètes classiques rangées par lenteur apparente : Saturne, Jupiter, "
              "Mars, Soleil, Vénus, Mercure, Lune. Il régit la répartition des décans et des "
              "heures planétaires."},

    "Modalidad de los cuatro signos que abren estación: Aries, Cáncer, Libra, Capricornio. "
    "Inician.": {
        "en": "Modality of the four signs that open a season: Aries, Cancer, Libra, Capricorn. "
              "They initiate.",
        "fr": "Modalité des quatre signes qui ouvrent une saison : Bélier, Cancer, Balance, "
              "Capricorne. Ils initient."},

    "Cuadratura": {"en": "Square", "fr": "Carré"},
    "Aspecto de 90°. Une signos de la misma modalidad y elementos discordes. Roce que obliga a "
    "crecer.": {
        "en": "Aspect of 90°. It joins signs of the same modality and discordant elements. "
              "Friction that compels growth.",
        "fr": "Aspect de 90°. Il unit des signes de même modalité et d'éléments discordants. "
              "Friction qui oblige à grandir."},

    "Cada uno de los tres tramos de diez grados en que se divide un signo. También llamado "
    "«cara». Cada uno tiene un planeta regente propio.": {
        "en": "Each of the three stretches of ten degrees into which a sign is divided. Also "
              "called a «face». Each has a ruling planet of its own.",
        "fr": "Chacun des trois tronçons de dix degrés en lesquels se divise un signe. Appelé "
              "aussi « face ». Chacun a une planète régente propre."},

    "Diurno": {"en": "Diurnal", "fr": "Diurne"},
    "Sinónimo tradicional de polaridad activa: los signos de Fuego y Aire. Su movimiento va "
    "del interior hacia el mundo.": {
        "en": "Traditional synonym for active polarity: the signs of Fire and Air. Their "
              "movement goes from the inside towards the world.",
        "fr": "Synonyme traditionnel de polarité active : les signes de Feu et d'Air. Leur "
              "mouvement va du dedans vers le monde."},

    "Eje": {"en": "Axis", "fr": "Axe"},
    "Pareja de signos opuestos, a 180°. Hay seis en la rueda, y cada uno plantea una pregunta "
    "que sus dos extremos responden por mitades.": {
        "en": "A pair of opposite signs, 180° apart. There are six on the wheel, and each poses "
              "a question that its two ends answer by halves.",
        "fr": "Couple de signes opposés, à 180°. Il y en a six sur la roue, et chacun pose une "
              "question à laquelle ses deux extrémités répondent par moitiés."},

    "Fuego, Tierra, Aire o Agua. Describe de qué está hecha la energía de un signo. Tres "
    "signos por elemento.": {
        "en": "Fire, Earth, Air or Water. It describes what a sign's energy is made of. Three "
              "signs per element.",
        "fr": "Feu, Terre, Air ou Eau. Décrit de quoi est faite l'énergie d'un signe. Trois "
              "signes par élément."},

    "Modalidad de los cuatro signos que sostienen la estación: Tauro, Leo, Escorpio, Acuario. "
    "Mantienen.": {
        "en": "Modality of the four signs that sustain a season: Taurus, Leo, Scorpio, "
              "Aquarius. They maintain.",
        "fr": "Modalité des quatre signes qui soutiennent la saison : Taureau, Lion, Scorpion, "
              "Verseau. Ils maintiennent."},

    "Luminares": {"en": "Luminaries", "fr": "Luminaires"},
    "El Sol y la Luna, los dos únicos cuerpos clásicos que gobiernan un solo signo cada uno.": {
        "en": "The Sun and the Moon, the only two classical bodies that rule one sign each.",
        "fr": "Le Soleil et la Lune, les deux seuls corps classiques à gouverner un seul signe "
              "chacun."},

    "Melotesia": {"en": "Melothesia", "fr": "Mélothésie"},
    "Reparto tradicional del cuerpo humano entre los doce signos, de la cabeza a los pies. "
    "Sistema simbólico y mnemotécnico, nunca diagnóstico.": {
        "en": "Traditional distribution of the human body among the twelve signs, from head to "
              "feet. A symbolic and mnemonic system, never a diagnostic one.",
        "fr": "Répartition traditionnelle du corps humain entre les douze signes, de la tête aux "
              "pieds. Système symbolique et mnémotechnique, jamais diagnostique."},

    "Cardinal, Fijo o Mutable. Describe cómo se mueve la energía de un signo. Cuatro signos "
    "por modalidad.": {
        "en": "Cardinal, Fixed or Mutable. It describes how a sign's energy moves. Four signs "
              "per modality.",
        "fr": "Cardinal, Fixe ou Mutable. Décrit comment se meut l'énergie d'un signe. Quatre "
              "signes par modalité."},

    "Modalidad de los cuatro signos que cierran estación: Géminis, Virgo, Sagitario, Piscis. "
    "Adaptan y transforman.": {
        "en": "Modality of the four signs that close a season: Gemini, Virgo, Sagittarius, "
              "Pisces. They adapt and transform.",
        "fr": "Modalité des quatre signes qui closent la saison : Gémeaux, Vierge, Sagittaire, "
              "Poissons. Ils adaptent et transforment."},

    "Nocturno": {"en": "Nocturnal", "fr": "Nocturne"},
    "Sinónimo tradicional de polaridad receptiva: los signos de Tierra y Agua. Su movimiento "
    "va del mundo hacia el interior.": {
        "en": "Traditional synonym for receptive polarity: the signs of Earth and Water. Their "
              "movement goes from the world towards the inside.",
        "fr": "Synonyme traditionnel de polarité réceptive : les signes de Terre et d'Eau. Leur "
              "mouvement va du monde vers le dedans."},

    "Oposición": {"en": "Opposition", "fr": "Opposition"},
    "Aspecto de 180°. Une signos de la misma modalidad y elementos complementarios. Tensión "
    "fértil, no conflicto.": {
        "en": "Aspect of 180°. It joins signs of the same modality and complementary elements. "
              "Fertile tension, not conflict.",
        "fr": "Aspect de 180°. Il unit des signes de même modalité et d'éléments "
              "complémentaires. Tension féconde, non conflit."},

    "Activa o receptiva. Alterna signo a signo alrededor de la rueda.": {
        "en": "Active or receptive. It alternates sign by sign around the wheel.",
        "fr": "Active ou réceptive. Elle alterne signe par signe tout autour de la roue."},

    "Planeta que gobierna un signo. En el sistema clásico de siete, cinco planetas rigen dos "
    "signos cada uno y los luminares uno.": {
        "en": "The planet that rules a sign. In the classical system of seven, five planets "
              "rule two signs each and the luminaries one.",
        "fr": "Planète qui gouverne un signe. Dans le système classique des sept, cinq planètes "
              "en régissent deux chacune et les luminaires un."},

    "Sextil": {"en": "Sextile", "fr": "Sextile"},
    "Aspecto de 60°. Une signos de elementos afines y la misma polaridad. Oportunidad que hay "
    "que tomar activamente.": {
        "en": "Aspect of 60°. It joins signs of kindred elements and the same polarity. An "
              "opportunity that has to be taken actively.",
        "fr": "Aspect de 60°. Il unit des signes d'éléments apparentés et de même polarité. Une "
              "occasion qu'il faut saisir activement."},

    "Signo solar": {"en": "Sun sign", "fr": "Signe solaire"},
    "El signo que ocupaba el Sol en la fecha de nacimiento. Es el que se pregunta en la "
    "conversación corriente, y solo una de las tres piezas del retrato clásico.": {
        "en": "The sign the Sun occupied on the date of birth. It is the one asked about in "
              "ordinary conversation, and only one of the three pieces of the classical "
              "portrait.",
        "fr": "Le signe qu'occupait le Soleil à la date de naissance. C'est celui que l'on "
              "demande dans la conversation courante, et seulement l'une des trois pièces du "
              "portrait classique."},

    "Trígono": {"en": "Trine", "fr": "Trigone"},
    "Aspecto de 120°. Une signos del mismo elemento. Fluidez, con el riesgo de que la "
    "comodidad impida aprender.": {
        "en": "Aspect of 120°. It joins signs of the same element. Fluency, with the risk that "
              "comfort prevents learning.",
        "fr": "Aspect de 120°. Il unit des signes du même élément. Fluidité, avec le risque que "
              "le confort empêche d'apprendre."},

    "Triplicidad": {"en": "Triplicity", "fr": "Triplicité"},
    "Los tres signos que comparten elemento. Sinónimo de trígono cuando se habla de grupos y "
    "no de ángulos.": {
        "en": "The three signs that share an element. A synonym for trine when speaking of "
              "groups and not of angles.",
        "fr": "Les trois signes qui partagent un élément. Synonyme de trigone quand on parle de "
              "groupes et non d'angles."},

    "Sobre lo que este vocabulario no incluye": {
        "en": "On what this vocabulary does not include",
        "fr": "Sur ce que ce vocabulaire n'inclut pas"},

    "No aparecen aquí las casas, los planetas transaturninos, los nodos lunares ni las "
    "técnicas predictivas. No es un olvido: este libro trabaja deliberadamente con el sistema "
    "de siete planetas y doce signos, que es cerrado, coherente y suficiente para todo lo que "
    "aquí se propone. Si sigues por tu cuenta, esos términos son el paso siguiente.": {
        "en": "The houses, the trans-Saturnian planets, the lunar nodes and the predictive "
              "techniques do not appear here. It is not an oversight: this book works "
              "deliberately with the system of seven planets and twelve signs, which is closed, "
              "coherent and sufficient for everything proposed here. If you go on by yourself, "
              "those terms are the next step.",
        "fr": "Ne figurent pas ici les maisons, les planètes transsaturniennes, les nœuds "
              "lunaires ni les techniques prédictives. Ce n'est pas un oubli : ce livre "
              "travaille délibérément avec le système de sept planètes et douze signes, qui est "
              "clos, cohérent et suffisant pour tout ce qui est proposé ici. Si vous poursuivez "
              "de votre côté, ces termes sont le pas suivant."},

    # ── Registro de observación ────────────────────────────────────────────
    "Capítulo 31": {"en": "Chapter 31", "fr": "Chapitre 31"},

    "Estas páginas son para escribir. La parte del libro que produce resultados no es la que "
    "se lee: es la que se rellena.": {
        "en": "These pages are for writing on. The part of the book that produces results is "
              "not the part you read: it is the part you fill in.",
        "fr": "Ces pages sont faites pour être écrites. La partie du livre qui produit des "
              "résultats n'est pas celle qu'on lit : c'est celle qu'on remplit."},

    "Antes de empezar el recorrido": {
        "en": "Before beginning the journey", "fr": "Avant de commencer le parcours"},

    "Mi signo solar": {"en": "My sun sign", "fr": "Mon signe solaire"},
    "El signo cuya práctica me parece más innecesaria": {
        "en": "The sign whose practice seems most unnecessary to me",
        "fr": "Le signe dont la pratique me paraît la plus inutile"},
    "El signo cuya práctica me da más pereza": {
        "en": "The sign whose practice I least feel like doing",
        "fr": "Le signe dont la pratique me rebute le plus"},
    "Lo que quiero observar este año": {
        "en": "What I want to observe this year",
        "fr": "Ce que je veux observer cette année"},

    "Una pista sobre las dos preguntas del medio": {
        "en": "A hint about the two middle questions",
        "fr": "Un indice sur les deux questions du milieu"},

    "El signo que te parece innecesario y el que te da pereza suelen ser el mismo, y suele ser "
    "el que trabaja justo la cualidad que te falta. Anótalos ahora, antes de empezar, y vuelve "
    "a leerlos dentro de un año.": {
        "en": "The sign that seems unnecessary to you and the one you least feel like doing are "
              "usually the same, and it is usually the one that works precisely the quality you "
              "lack. Write them down now, before you begin, and read them again a year from "
              "now.",
        "fr": "Le signe qui vous paraît inutile et celui qui vous rebute sont d'ordinaire le "
              "même, et c'est d'ordinaire celui qui travaille justement la qualité qui vous "
              "manque. Notez-les maintenant, avant de commencer, et relisez-les dans un an."},

    "Registro mensual": {"en": "Monthly record", "fr": "Registre mensuel"},

    "Para cada mes del recorrido, anota lo mismo: el signo, la práctica, si la cumpliste y qué "
    "observaste. Cuatro líneas por mes bastan. Lo importante no es la extensión: es que exista "
    "el registro y que sea honesto.": {
        "en": "For each month of the journey, write down the same things: the sign, the "
              "practice, whether you kept it and what you observed. Four lines a month are "
              "enough. What matters is not the length: it is that the record exists and that it "
              "is honest.",
        "fr": "Pour chaque mois du parcours, notez la même chose : le signe, la pratique, si vous "
              "l'avez tenue et ce que vous avez observé. Quatre lignes par mois suffisent. Ce "
              "qui importe n'est pas la longueur : c'est que le registre existe et qu'il soit "
              "honnête."},

    "Plantilla mensual": {"en": "Monthly template", "fr": "Modèle mensuel"},
    "Signo del mes": {"en": "Sign of the month", "fr": "Signe du mois"},
    "Práctica": {"en": "Practice", "fr": "Pratique"},
    "Semanas cumplidas": {"en": "Weeks kept", "fr": "Semaines tenues"},
    "Lo que me costó": {"en": "What cost me", "fr": "Ce qui m'a coûté"},
    "Lo que descubrí": {"en": "What I discovered", "fr": "Ce que j'ai découvert"},

    "Al terminar los doce meses": {
        "en": "On finishing the twelve months", "fr": "À la fin des douze mois"},

    "Práctica que más me costó": {
        "en": "The practice that cost me most", "fr": "La pratique qui m'a le plus coûté"},
    "Práctica que más me sirvió": {
        "en": "The practice that served me most", "fr": "La pratique qui m'a le plus servi"},
    "El signo que resultó ser el mío de verdad": {
        "en": "The sign that turned out to be really mine",
        "fr": "Le signe qui s'est révélé être vraiment le mien"},

    "Esa última pregunta es la única trampa del libro, y conviene explicarla. Después de un "
    "año recorriendo los doce signos, muchos lectores descubren que la cualidad que más les ha "
    "transformado no era la de su signo solar, sino la de otro que al principio les resultaba "
    "ajeno. No significa que su signo esté mal calculado. Significa que el zodiaco no es una "
    "etiqueta que se recibe al nacer, sino un repertorio que se aprende a usar.": {
        "en": "That last question is the book's only trick, and it deserves explaining. After a "
              "year going through the twelve signs, many readers discover that the quality that "
              "transformed them most was not that of their sun sign, but that of another which "
              "at the start felt alien to them. It does not mean their sign has been calculated "
              "wrongly. It means the zodiac is not a label received at birth, but a repertoire "
              "one learns to use.",
        "fr": "Cette dernière question est le seul piège du livre, et il convient de l'expliquer. "
              "Après une année à parcourir les douze signes, bien des lecteurs découvrent que la "
              "qualité qui les a le plus transformés n'était pas celle de leur signe solaire, "
              "mais celle d'un autre qui leur était d'abord étranger. Cela ne veut pas dire que "
              "leur signe est mal calculé. Cela veut dire que le zodiaque n'est pas une "
              "étiquette reçue à la naissance, mais un répertoire que l'on apprend à employer."},

    "Y con eso, el libro ha hecho su trabajo.": {
        "en": "And with that, the book has done its work.",
        "fr": "Et avec cela, le livre a fait son travail."},
}
