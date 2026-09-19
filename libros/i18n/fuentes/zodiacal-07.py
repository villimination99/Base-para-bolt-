# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · las tres piezas, las once claves y la entrada a las dignidades
================================================================================
Las once claves son los once epígrafes que se repiten en los doce capítulos de
signo: el sello, la ficha, el símbolo, la fuerza, la sombra, el eje, los tres
decanatos, el cuerpo, la mesa, la práctica y las relaciones. Se fijan aquí
porque van a aparecer ciento treinta y dos veces y tienen que decirse igual
todas ellas.

«La mesa» es la mesa de comer y se traduce The table / La table, la misma
forma que ya lleva el capítulo de los cuatro temperamentos. Su párrafo de
descargo —no afirma que la fecha de nacimiento determine lo que se debe
comer— es la línea que mantiene la sección dentro de lo defendible y va
entera.

La entrada de las dignidades reconoce que la parte es árida y que se aprende
con la tabla delante. No se le sube el tono: es la razón por la que el
capítulo existe.
"""

T = {
    "El Ascendente": {"en": "The Ascendant", "fr": "L'Ascendant"},

    "Cómo apareces y cómo entras en las situaciones. La puerta de la casa. Depende de la hora "
    "exacta de nacimiento y cambia cada dos horas.": {
        "en": "How you appear and how you enter situations. The front door of the house. It "
              "depends on the exact time of birth and changes every two hours.",
        "fr": "Comment vous apparaissez et comment vous entrez dans les situations. La porte de "
              "la maison. Il dépend de l'heure exacte de naissance et change toutes les deux "
              "heures."},

    "La distinción es más útil de lo que parece. Explica, por ejemplo, por qué alguien se "
    "describe como reservado y sus conocidos lo describen como expansivo: el Sol y el "
    "Ascendente pueden apuntar a lados distintos. O por qué una persona ordenadísima en el "
    "trabajo es un desastre emocional: el Sol en Tierra y la Luna en Agua conviven sin "
    "problema en el mismo cuerpo.": {
        "en": "The distinction is more useful than it looks. It explains, for instance, why "
              "somebody describes themselves as reserved and their acquaintances describe them "
              "as expansive: the Sun and the Ascendant can point in different directions. Or "
              "why a person who is extremely orderly at work is an emotional disaster: the Sun "
              "in Earth and the Moon in Water live together in the same body with no trouble at "
              "all.",
        "fr": "La distinction est plus utile qu'il n'y paraît. Elle explique, par exemple, "
              "pourquoi quelqu'un se décrit comme réservé et que ses connaissances le décrivent "
              "comme expansif : le Soleil et l'Ascendant peuvent pointer de deux côtés "
              "différents. Ou pourquoi une personne extrêmement ordonnée au travail est un "
              "désastre émotionnel : le Soleil en Terre et la Lune en Eau cohabitent sans "
              "problème dans le même corps."},

    "Este libro no calcula tu carta": {
        "en": "This book does not calculate your chart",
        "fr": "Ce livre ne calcule pas votre thème"},

    "Averiguar la Luna y el Ascendente requiere la fecha, la hora y el lugar de nacimiento, y "
    "un cálculo que no cabe en un libro. Hay calculadoras gratuitas y fiables en cualquier "
    "parte. Lo que este libro te da es lo otro, y es lo que casi nunca se da: los doce signos "
    "descritos con la profundidad suficiente para que, cuando sepas cuáles son tus tres, sepas "
    "qué hacer con ellos.": {
        "en": "Finding out the Moon and the Ascendant requires the date, the time and the place "
              "of birth, and a calculation that does not fit in a book. There are free and "
              "reliable calculators everywhere. What this book gives you is the other thing, "
              "and it is what almost never gets given: the twelve signs described in enough "
              "depth that, once you know which your three are, you know what to do with them.",
        "fr": "Trouver la Lune et l'Ascendant demande la date, l'heure et le lieu de naissance, "
              "et un calcul qui ne tient pas dans un livre. Il existe partout des calculateurs "
              "gratuits et fiables. Ce que ce livre vous donne, c'est l'autre chose, et c'est ce "
              "qu'on ne donne presque jamais : les douze signes décrits avec assez de profondeur "
              "pour que, une fois que vous saurez quels sont vos trois, vous sachiez quoi en "
              "faire."},

    "Cómo leer el libro cuando ya conoces tus tres signos": {
        "en": "How to read the book once you know your three signs",
        "fr": "Comment lire le livre quand on connaît ses trois signes"},

    "Lee tu Sol como el capítulo de la dirección: lo que intentas construir.": {
        "en": "Read your Sun as the chapter of direction: what you are trying to build.",
        "fr": "Lisez votre Soleil comme le chapitre de la direction : ce que vous tentez de "
              "bâtir."},

    "Lee tu Luna como el capítulo del cuerpo y del hábito: la sección «La mesa» de tu Luna "
    "suele describirte mucho mejor que la de tu Sol.": {
        "en": "Read your Moon as the chapter of body and habit: the section «The table» of your "
              "Moon usually describes you far better than that of your Sun.",
        "fr": "Lisez votre Lune comme le chapitre du corps et de l'habitude : la section « La "
              "table » de votre Lune vous décrit d'ordinaire bien mieux que celle de votre "
              "Soleil."},

    "Lee tu Ascendente como el capítulo de la primera impresión: si alguien te describe de una "
    "forma que no reconoces, mira ahí.": {
        "en": "Read your Ascendant as the chapter of first impressions: if somebody describes "
              "you in a way you do not recognise, look there.",
        "fr": "Lisez votre Ascendant comme le chapitre de la première impression : si quelqu'un "
              "vous décrit d'une façon que vous ne reconnaissez pas, regardez là."},

    "Lee el opuesto de tu Sol como el capítulo de la tarea pendiente. Es incómodo a propósito.": {
        "en": "Read the opposite of your Sun as the chapter of unfinished business. It is "
              "uncomfortable on purpose.",
        "fr": "Lisez l'opposé de votre Soleil comme le chapitre de la tâche en attente. Il est "
              "inconfortable exprès."},

    "Y si no sabes ninguno de los tres y no te apetece averiguarlo, el libro sigue "
    "funcionando. Los doce capítulos describen doce formas de estar en el mundo, y todas están "
    "dentro de ti en alguna proporción. La tercera parte propone recorrerlas una por mes, y "
    "ese recorrido no necesita ninguna carta: necesita un cuaderno.": {
        "en": "And if you know none of the three and do not feel like finding out, the book "
              "still works. The twelve chapters describe twelve ways of being in the world, and "
              "all of them are inside you in some proportion. The third part proposes going "
              "through them one a month, and that journey needs no chart: it needs a notebook.",
        "fr": "Et si vous n'en connaissez aucun des trois et que vous n'avez pas envie de le "
              "savoir, le livre fonctionne quand même. Les douze chapitres décrivent douze "
              "façons d'être au monde, et toutes sont en vous dans une certaine proportion. La "
              "troisième partie propose de les parcourir une par mois, et ce parcours n'a besoin "
              "d'aucun thème : il a besoin d'un cahier."},

    # ── Las once claves de cada signo ──────────────────────────────────────
    "Los doce capítulos de la segunda parte tienen exactamente la misma estructura. Se hizo "
    "así a propósito: cuando todos los signos se describen con las mismas claves, las "
    "diferencias reales entre ellos se vuelven visibles y dejan de depender del entusiasmo del "
    "que escribe. Es también la única forma de que el libro se pueda usar como obra de "
    "consulta y no solo de lectura.": {
        "en": "The twelve chapters of the second part have exactly the same structure. It was "
              "done that way on purpose: when all the signs are described with the same keys, "
              "the real differences between them become visible and stop depending on the "
              "enthusiasm of whoever is writing. It is also the only way the book can be used "
              "as a work of reference and not only of reading.",
        "fr": "Les douze chapitres de la deuxième partie ont exactement la même structure. Cela "
              "a été fait exprès : quand tous les signes sont décrits avec les mêmes clés, les "
              "différences réelles entre eux deviennent visibles et cessent de dépendre de "
              "l'enthousiasme de celui qui écrit. C'est aussi la seule façon pour que le livre "
              "puisse servir d'ouvrage de consultation et non seulement de lecture."},

    "El sello. El medallón del signo, con su glifo, el sigilo de su regente y la marca de su "
    "elemento. Los colores no decoran: dicen el elemento.": {
        "en": "The seal. The sign's medallion, with its glyph, the sigil of its ruler and the "
              "mark of its element. The colours do not decorate: they state the element.",
        "fr": "Le sceau. Le médaillon du signe, avec son glyphe, le sceau de son régent et la "
              "marque de son élément. Les couleurs ne décorent pas : elles disent l'élément."},

    "La ficha. Fechas, elemento, modalidad, polaridad, regente, metal, piedra, color, zona "
    "corporal y palabra clave. La tarjeta de identidad clásica.": {
        "en": "The entry. Dates, element, modality, polarity, ruler, metal, stone, colour, "
              "bodily zone and key word. The classical identity card.",
        "fr": "La fiche. Dates, élément, modalité, polarité, régent, métal, pierre, couleur, "
              "zone corporelle et mot-clé. La carte d'identité classique."},

    "El símbolo. De dónde viene la imagen y qué contiene. El símbolo no es adorno: es la forma "
    "comprimida de todo lo demás.": {
        "en": "The symbol. Where the image comes from and what it contains. The symbol is no "
              "ornament: it is the compressed form of everything else.",
        "fr": "Le symbole. D'où vient l'image et ce qu'elle contient. Le symbole n'est pas un "
              "ornement : il est la forme comprimée de tout le reste."},

    "La fuerza. Lo que el signo hace bien cuando está en su mejor versión.": {
        "en": "The strength. What the sign does well when it is at its best.",
        "fr": "La force. Ce que le signe fait bien quand il est dans sa meilleure version."},

    "La sombra. La misma cualidad llevada al exceso o al defecto. Nunca es un rasgo distinto: "
    "siempre es la fuerza desbordada.": {
        "en": "The shadow. The same quality taken to excess or to deficiency. It is never a "
              "different trait: it is always the strength overflowing.",
        "fr": "L'ombre. La même qualité poussée à l'excès ou au défaut. Ce n'est jamais un trait "
              "différent : c'est toujours la force qui déborde."},

    "El eje. El signo opuesto y la pregunta que los dos comparten. Es la clave que más "
    "incomoda y la que más rinde.": {
        "en": "The axis. The opposite sign and the question the two of them share. It is the "
              "key that discomfits most and the one that yields most.",
        "fr": "L'axe. Le signe opposé et la question que tous deux partagent. C'est la clé qui "
              "dérange le plus et celle qui rapporte le plus."},

    "Los tres decanatos. Los treinta grados divididos en tres caras, con las fechas y el "
    "planeta de cada una. Aquí está la explicación de por qué mucha gente no se reconoce en la "
    "descripción general.": {
        "en": "The three decans. The thirty degrees divided into three faces, with the dates "
              "and the planet of each. Here is the explanation of why many people do not "
              "recognise themselves in the general description.",
        "fr": "Les trois décans. Les trente degrés divisés en trois faces, avec les dates et la "
              "planète de chacune. C'est ici qu'est l'explication du fait que bien des gens ne "
              "se reconnaissent pas dans la description générale."},

    "El cuerpo. La zona que la tradición asigna al signo y el cuidado que realmente le "
    "corresponde.": {
        "en": "The body. The zone the tradition assigns to the sign and the care that actually "
              "belongs to it.",
        "fr": "Le corps. La zone que la tradition assigne au signe et le soin qui lui revient "
              "réellement."},

    "La mesa. Alimentos y hábitos afines a su temperamento, en clave de compensación y no de "
    "superstición.": {
        "en": "The table. Foods and habits akin to its temperament, in terms of compensation "
              "and not of superstition.",
        "fr": "La table. Aliments et habitudes proches de son tempérament, sous l'angle de la "
              "compensation et non de la superstition."},

    "La práctica. Un ejercicio concreto de cuatro semanas para desarrollar la cualidad del "
    "signo, sea o no tu signo solar.": {
        "en": "The practice. A concrete four-week exercise for developing the sign's quality, "
              "whether or not it is your sun sign.",
        "fr": "La pratique. Un exercice concret de quatre semaines pour développer la qualité du "
              "signe, qu'il soit ou non votre signe solaire."},

    "Las relaciones y el trabajo del mes. Con qué temperamentos encaja sin esfuerzo y con "
    "cuáles hay que traducir; y tres preguntas para el cuaderno, que son la parte que de "
    "verdad cambia algo.": {
        "en": "Relations and the month's work. Which temperaments it fits with effortlessly and "
              "with which ones translation is needed; and three questions for the notebook, "
              "which are the part that really changes something.",
        "fr": "Les relations et le travail du mois. Avec quels tempéraments il s'accorde sans "
              "effort et avec lesquels il faut traduire ; et trois questions pour le cahier, qui "
              "sont la partie qui change vraiment quelque chose."},

    "Sobre «la mesa»": {"en": "On «the table»", "fr": "Sur « la table »"},

    "La sección de alimentación de cada signo no afirma que tu fecha de nacimiento determine "
    "lo que debes comer. Lo que hace es más razonable: cada temperamento tiene tendencias "
    "reconocibles —el que va acelerado suele comer deprisa, el que es constante tiende a "
    "repetir el mismo plato durante años— y esas tendencias sí se pueden compensar. Son "
    "recomendaciones de sentido común nutricional aplicadas al patrón de cada signo, y en "
    "ningún caso una pauta dietética individualizada.": {
        "en": "Each sign's food section does not claim that your date of birth determines what "
              "you should eat. What it does is more reasonable: every temperament has "
              "recognisable tendencies —whoever runs fast tends to eat fast, whoever is "
              "constant tends to repeat the same dish for years— and those tendencies can "
              "indeed be compensated for. They are recommendations of nutritional common sense "
              "applied to each sign's pattern, and in no case an individualised dietary plan.",
        "fr": "La section alimentation de chaque signe n'affirme pas que votre date de naissance "
              "détermine ce que vous devez manger. Ce qu'elle fait est plus raisonnable : chaque "
              "tempérament a des tendances reconnaissables —celui qui va vite mange d'ordinaire "
              "vite, celui qui est constant tend à répéter le même plat pendant des années— et "
              "ces tendances-là peuvent se compenser. Ce sont des recommandations de bon sens "
              "nutritionnel appliquées au schéma de chaque signe, et en aucun cas un régime "
              "individualisé."},

    "Ninguna sección es un veredicto": {
        "en": "No section is a verdict", "fr": "Aucune section n'est un verdict"},

    "Conviene repetirlo antes de entrar en los doce capítulos: lo que sigue describe "
    "tendencias, no destinos. Si al leer tu signo encuentras una sombra que reconoces, eso es "
    "información útil. Si encuentras una que no reconoces, no la fuerces: el sistema es un "
    "espejo, y un espejo que no devuelve nada simplemente no está enfocando ahí.": {
        "en": "It is worth repeating before entering the twelve chapters: what follows "
              "describes tendencies, not destinies. If on reading your sign you find a shadow "
              "you recognise, that is useful information. If you find one you do not recognise, "
              "do not force it: the system is a mirror, and a mirror that gives nothing back is "
              "simply not pointed there.",
        "fr": "Il vaut la peine de le répéter avant d'entrer dans les douze chapitres : ce qui "
              "suit décrit des tendances, non des destins. Si en lisant votre signe vous trouvez "
              "une ombre que vous reconnaissez, c'est une information utile. Si vous en trouvez "
              "une que vous ne reconnaissez pas, ne la forcez pas : le système est un miroir, et "
              "un miroir qui ne renvoie rien n'est simplement pas dirigé de ce côté."},

    # ── Las dignidades esenciales ──────────────────────────────────────────
    "Aquí empieza la parte del sistema clásico que la divulgación moderna ha dejado caer casi "
    "por completo, y no por mala fe: porque es árida, se aprende con tabla delante y no cabe "
    "en un horóscopo de revista. Es también la parte que convierte el zodiaco en un sistema "
    "con reglas en lugar de una colección de descripciones.": {
        "en": "Here begins the part of the classical system that modern popularisation has let "
              "drop almost entirely, and not out of bad faith: because it is arid, it is learnt "
              "with a table in front of you and it does not fit in a magazine horoscope. It is "
              "also the part that turns the zodiac into a system with rules instead of a "
              "collection of descriptions.",
        "fr": "Ici commence la partie du système classique que la vulgarisation moderne a "
              "laissée tomber presque entièrement, et non par mauvaise foi : parce qu'elle est "
              "aride, qu'elle s'apprend avec la table sous les yeux et qu'elle ne tient pas dans "
              "un horoscope de magazine. C'est aussi la partie qui fait du zodiaque un système à "
              "règles au lieu d'une collection de descriptions."},

    "La idea es sencilla. Un planeta no se comporta igual en los doce signos. En unos está en "
    "su terreno y opera con facilidad; en otros trabaja incómodo, contra su propia naturaleza. "
    "La tradición fijó cuatro grados de esa comodidad y les puso nombre.": {
        "en": "The idea is simple. A planet does not behave the same way in all twelve signs. "
              "In some it is on its own ground and operates easily; in others it works "
              "uncomfortably, against its own nature. The tradition fixed four degrees of that "
              "comfort and gave them names.",
        "fr": "L'idée est simple. Une planète ne se comporte pas de la même façon dans les douze "
              "signes. Dans certains elle est sur son terrain et opère avec facilité ; dans "
              "d'autres elle travaille mal à l'aise, contre sa propre nature. La tradition a "
              "fixé quatre degrés de cette aisance et leur a donné un nom."},

    "Las cuatro dignidades": {
        "en": "The four dignities", "fr": "Les quatre dignités"},
}
