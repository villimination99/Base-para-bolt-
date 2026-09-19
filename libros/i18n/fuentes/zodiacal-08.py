# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · las cuatro dignidades y los sesenta términos
==============================================================
Los grados exactos de las siete exaltaciones —19 de Aries, 3 de Tauro, 15 de
Cáncer, 15 de Virgo, 21 de Libra, 28 de Capricornio, 27 de Piscis— son datos y
se copian sin tocarlos. Lo mismo con los pares de exilio y caída de Marte y de
Venus: el texto los da para que el lector compruebe la deducción.

«Términos, o límites, o confines según la traducción» enumera los nombres que
la palabra recibió al pasar de lengua en lengua, así que cada versión da los
suyos: terms, bounds, confines en inglés; termes, limites, confins en francés.
El griego horoi se queda como está, en cursiva del original.

La cita de Ptolomeo —que la tabla egipcia no seguía «ningún orden natural»— va
entrecomillada porque es suya, y se traduce como cita, no como paráfrasis.
"""

T = {
    "Domicilio": {"en": "Domicile", "fr": "Domicile"},
    "El planeta está en el signo que rige. En su casa: hace lo que sabe hacer sin "
    "resistencia.": {
        "en": "The planet is in the sign it rules. At home: it does what it knows how to do "
              "with no resistance.",
        "fr": "La planète est dans le signe qu'elle régit. Chez elle : elle fait ce qu'elle sait "
              "faire sans résistance."},

    "Exaltación": {"en": "Exaltation", "fr": "Exaltation"},
    "Está en el signo donde la tradición dice que se le honra. Rinde más de lo que le "
    "corresponde, y en un grado exacto —no en todo el signo—.": {
        "en": "It is in the sign where the tradition says it is honoured. It yields more than "
              "its due, and at an exact degree —not throughout the whole sign—.",
        "fr": "Elle est dans le signe où la tradition dit qu'on l'honore. Elle rend plus que ce "
              "qui lui revient, et à un degré exact —non dans tout le signe—."},

    "Exilio": {"en": "Detriment", "fr": "Exil"},
    "Está en el signo opuesto al que rige. Trabaja al revés de su naturaleza y le cuesta el "
    "doble.": {
        "en": "It is in the sign opposite the one it rules. It works against the grain of its "
              "nature and it costs it twice as much.",
        "fr": "Elle est dans le signe opposé à celui qu'elle régit. Elle travaille à rebours de "
              "sa nature et cela lui coûte le double."},

    "Caída": {"en": "Fall", "fr": "Chute"},
    "Está en el signo opuesto al de su exaltación. Ni se le honra ni se le atiende.": {
        "en": "It is in the sign opposite its exaltation. It is neither honoured nor attended "
              "to.",
        "fr": "Elle est dans le signe opposé à celui de son exaltation. On ne l'honore ni ne "
              "l'écoute."},

    '<span class="fig-n">Lám. 8</span> Las cuatro dignidades signo por signo. Con el grado '
    "exacto donde cae cada exaltación y cada caída. Los guiones no son huecos por olvido: hay "
    "signos que no albergan ninguna exaltación.": {
        "en": '<span class="fig-n">Pl. 8</span> The four dignities sign by sign. With the exact '
              "degree where each exaltation and each fall lands. The dashes are not gaps left "
              "by oversight: there are signs that house no exaltation at all.",
        "fr": '<span class="fig-n">Pl. 8</span> Les quatre dignités signe par signe. Avec le '
              "degré exact où tombent chaque exaltation et chaque chute. Les tirets ne sont pas "
              "des trous par oubli : il y a des signes qui n'abritent aucune exaltation."},

    "Dos columnas son datos y dos se deducen": {
        "en": "Two columns are data and two are deduced",
        "fr": "Deux colonnes sont des données et deux se déduisent"},

    "Merece la pena ver la mecánica, porque explica por qué la tabla es coherente y no un "
    "catálogo arbitrario. Los domicilios y las exaltaciones son lo que la tradición fija: hay "
    "que aprenderlos. El exilio y la caída no hace falta aprenderlos, porque salen solos — el "
    "exilio de un planeta está siempre en el signo opuesto a su domicilio, y su caída en el "
    "opuesto a su exaltación. Media tabla es deducción.": {
        "en": "It is worth seeing the mechanics, because they explain why the table is coherent "
              "and not an arbitrary catalogue. The domiciles and the exaltations are what the "
              "tradition fixes: they have to be learnt. Detriment and fall do not have to be "
              "learnt, because they come out on their own — a planet's detriment is always in "
              "the sign opposite its domicile, and its fall in the one opposite its exaltation. "
              "Half the table is deduction.",
        "fr": "Il vaut la peine de voir la mécanique, car elle explique pourquoi la table est "
              "cohérente et non un catalogue arbitraire. Les domiciles et les exaltations sont "
              "ce que la tradition fixe : il faut les apprendre. L'exil et la chute n'ont pas "
              "besoin d'être appris, car ils sortent tout seuls — l'exil d'une planète est "
              "toujours dans le signe opposé à son domicile, et sa chute dans celui opposé à son "
              "exaltation. La moitié de la table est une déduction."},

    "Un detalle que casi nunca se dice": {
        "en": "A detail that is hardly ever mentioned",
        "fr": "Un détail que l'on ne dit presque jamais"},

    "Las exaltaciones llevan grado exacto: el Sol en el 19 de Aries, la Luna en el 3 de Tauro, "
    "Júpiter en el 15 de Cáncer, Mercurio en el 15 de Virgo, Saturno en el 21 de Libra, Marte "
    "en el 28 de Capricornio y Venus en el 27 de Piscis. Siete planetas, siete grados, siete "
    "signos. Los cinco signos restantes —Géminis, Leo, Escorpio, Sagitario y Acuario— no "
    "albergan ninguna exaltación, y esa asimetría es original: la tradición nunca la rellenó.": {
        "en": "The exaltations carry an exact degree: the Sun at 19 Aries, the Moon at 3 "
              "Taurus, Jupiter at 15 Cancer, Mercury at 15 Virgo, Saturn at 21 Libra, Mars at "
              "28 Capricorn and Venus at 27 Pisces. Seven planets, seven degrees, seven signs. "
              "The remaining five signs —Gemini, Leo, Scorpio, Sagittarius and Aquarius— house "
              "no exaltation at all, and that asymmetry is original: the tradition never filled "
              "it in.",
        "fr": "Les exaltations portent un degré exact : le Soleil au 19 du Bélier, la Lune au 3 "
              "du Taureau, Jupiter au 15 du Cancer, Mercure au 15 de la Vierge, Saturne au 21 de "
              "la Balance, Mars au 28 du Capricorne et Vénus au 27 des Poissons. Sept planètes, "
              "sept degrés, sept signes. Les cinq signes restants —Gémeaux, Lion, Scorpion, "
              "Sagittaire et Verseau— n'abritent aucune exaltation, et cette asymétrie est "
              "d'origine : la tradition ne l'a jamais comblée."},

    "Para qué sirve esto sin carta natal": {
        "en": "What this is for with no birth chart",
        "fr": "À quoi cela sert sans thème de naissance"},

    "Para leer el libro con más precisión, y para una cosa muy concreta. Cuando en la segunda "
    "parte se dice que Marte en Aries ataca de frente y en Escorpio persiste en silencio, esa "
    "diferencia no es literaria: Marte gobierna los dos signos, pero uno es diurno y otro "
    "nocturno. Y cuando se dice que Saturno en Libra construye acuerdos, es porque ahí está "
    "exaltado — el mismo Saturno que en Aries, su caída, no sabe hacer otra cosa que frenar.": {
        "en": "For reading the book with more precision, and for one very concrete thing. When "
              "the second part says that Mars in Aries attacks head-on and in Scorpio persists "
              "in silence, that difference is not literary: Mars rules both signs, but one is "
              "diurnal and the other nocturnal. And when it says that Saturn in Libra builds "
              "agreements, it is because it is exalted there — the same Saturn that in Aries, "
              "its fall, knows how to do nothing but put on the brakes.",
        "fr": "À lire le livre avec plus de précision, et à une chose très concrète. Quand la "
              "deuxième partie dit que Mars au Bélier attaque de front et qu'au Scorpion il "
              "persiste en silence, cette différence n'est pas littéraire : Mars gouverne les "
              "deux signes, mais l'un est diurne et l'autre nocturne. Et quand elle dit que "
              "Saturne à la Balance bâtit des accords, c'est parce qu'il y est exalté — le même "
              "Saturne qui au Bélier, sa chute, ne sait rien faire d'autre que freiner."},

    "Marte está en domicilio en Aries y en Escorpio, en exilio en Tauro y Libra, exaltado en "
    "el 28 de Capricornio y caído en el 28 de Cáncer.": {
        "en": "Mars is in domicile in Aries and Scorpio, in detriment in Taurus and Libra, "
              "exalted at 28 Capricorn and fallen at 28 Cancer.",
        "fr": "Mars est en domicile au Bélier et au Scorpion, en exil au Taureau et à la "
              "Balance, exalté au 28 du Capricorne et en chute au 28 du Cancer."},

    "Venus está en domicilio en Tauro y Libra, en exilio en Aries y Escorpio, exaltada en el "
    "27 de Piscis y caída en el 27 de Virgo.": {
        "en": "Venus is in domicile in Taurus and Libra, in detriment in Aries and Scorpio, "
              "exalted at 27 Pisces and fallen at 27 Virgo.",
        "fr": "Vénus est en domicile au Taureau et à la Balance, en exil au Bélier et au "
              "Scorpion, exaltée au 27 des Poissons et en chute au 27 de la Vierge."},

    "Mercurio es el único que tiene domicilio y exaltación en el mismo signo —Virgo—, y por "
    "eso Virgo es el signo más mercurial de los dos que rige.": {
        "en": "Mercury is the only one with domicile and exaltation in the same sign —Virgo— "
              "and that is why Virgo is the more mercurial of the two signs it rules.",
        "fr": "Mercure est le seul à avoir domicile et exaltation dans le même signe —la "
              "Vierge—, et c'est pourquoi la Vierge est le plus mercuriel des deux signes qu'il "
              "régit."},

    "Saturno rige Capricornio y Acuario, y está exaltado en Libra: el rigor encuentra su mejor "
    "versión en el signo del equilibrio, que es una de las afirmaciones más finas de todo el "
    "sistema.": {
        "en": "Saturn rules Capricorn and Aquarius, and is exalted in Libra: rigour finds its "
              "best version in the sign of balance, which is one of the finest statements in "
              "the whole system.",
        "fr": "Saturne régit le Capricorne et le Verseau, et il est exalté à la Balance : la "
              "rigueur trouve sa meilleure version dans le signe de l'équilibre, ce qui est "
              "l'une des affirmations les plus fines de tout le système."},

    # ── Los términos ───────────────────────────────────────────────────────
    "Si el capítulo anterior recuperaba una tabla poco impresa, este recupera una que ha "
    "desaparecido casi por completo de la divulgación — y es, probablemente, la pieza más "
    "sofisticada del sistema clásico.": {
        "en": "If the previous chapter recovered a table that is seldom printed, this one "
              "recovers one that has disappeared almost entirely from popular writing — and it "
              "is probably the most sophisticated piece of the classical system.",
        "fr": "Si le chapitre précédent récupérait une table peu imprimée, celui-ci en récupère "
              "une qui a presque entièrement disparu de la vulgarisation — et c'est "
              "probablement la pièce la plus sophistiquée du système classique."},

    "La tradición no se detuvo en dividir cada signo en tres decanatos de diez grados. Hizo "
    "una segunda división, más fina y deliberadamente irregular: cinco tramos por signo, de "
    "longitud desigual, uno para cada planeta excepto los luminares. Se llaman términos, o "
    "límites, o confines según la traducción; en griego, horoi.": {
        "en": "The tradition did not stop at dividing each sign into three decans of ten "
              "degrees. It made a second division, finer and deliberately irregular: five "
              "stretches per sign, of unequal length, one for each planet except the "
              "luminaries. They are called terms, or bounds, or confines depending on the "
              "translation; in Greek, horoi.",
        "fr": "La tradition ne s'est pas arrêtée à diviser chaque signe en trois décans de dix "
              "degrés. Elle a fait une seconde division, plus fine et délibérément irrégulière : "
              "cinq tronçons par signe, de longueur inégale, un pour chaque planète sauf les "
              "luminaires. On les appelle termes, ou limites, ou confins selon la traduction ; "
              "en grec, horoi."},

    '<span class="fig-n">Lám. 9</span> Los sesenta términos. Cada barra son los treinta grados '
    "de un signo partidos en cinco tramos desiguales; la longitud dibujada es su número de "
    "grados, así que la lámina se puede medir con una regla.": {
        "en": '<span class="fig-n">Pl. 9</span> The sixty terms. Each bar is the thirty degrees '
              "of a sign split into five unequal stretches; the length drawn is its number of "
              "degrees, so the plate can be measured with a ruler.",
        "fr": '<span class="fig-n">Pl. 9</span> Les soixante termes. Chaque barre représente les '
              "trente degrés d'un signe partagés en cinq tronçons inégaux ; la longueur dessinée "
              "est son nombre de degrés, de sorte que la planche se mesure à la règle."},

    "Lo que hace especial a esta tabla": {
        "en": "What makes this table special", "fr": "Ce qui rend cette table particulière"},

    "Es irregular a propósito. Los decanatos son tres tramos iguales de diez grados; los "
    "términos son cinco tramos que van de dos a doce grados. La irregularidad no es descuido: "
    "es información.": {
        "en": "It is irregular on purpose. The decans are three equal stretches of ten degrees; "
              "the terms are five stretches running from two to twelve degrees. The "
              "irregularity is not carelessness: it is information.",
        "fr": "Elle est irrégulière exprès. Les décans sont trois tronçons égaux de dix degrés ; "
              "les termes sont cinq tronçons allant de deux à douze degrés. L'irrégularité n'est "
              "pas une négligence : c'est de l'information."},

    "Solo intervienen cinco planetas. El Sol y la Luna quedan fuera del reparto de términos, "
    "igual que quedan fuera de la doble regencia. Los luminares no se subdividen.": {
        "en": "Only five planets take part. The Sun and the Moon are left out of the "
              "distribution of terms, just as they are left out of the double rulership. The "
              "luminaries are not subdivided.",
        "fr": "Seules cinq planètes interviennent. Le Soleil et la Lune restent hors de la "
              "répartition des termes, comme ils restent hors de la double régence. Les "
              "luminaires ne se subdivisent pas."},

    "Cada fila suma exactamente treinta. Es la única tabla de este libro que se puede "
    "verificar aritméticamente, y por eso las de estas páginas se calculan y se comprueban en "
    "lugar de copiarse.": {
        "en": "Each row adds up to exactly thirty. It is the only table in this book that can "
              "be verified arithmetically, and that is why the ones on these pages are "
              "calculated and checked instead of copied.",
        "fr": "Chaque ligne fait exactement trente. C'est la seule table de ce livre que l'on "
              "puisse vérifier arithmétiquement, et c'est pourquoi celles de ces pages sont "
              "calculées et contrôlées au lieu d'être recopiées."},

    "El planeta que abre cada signo tiene sentido: Júpiter abre Aries, Venus abre Tauro, "
    "Mercurio abre Géminis, Marte abre Cáncer. No es el regente del signo, y ese desajuste es "
    "la parte que más discutieron los antiguos.": {
        "en": "The planet that opens each sign makes sense: Jupiter opens Aries, Venus opens "
              "Taurus, Mercury opens Gemini, Mars opens Cancer. It is not the sign's ruler, and "
              "that mismatch is the part the ancients argued about most.",
        "fr": "La planète qui ouvre chaque signe a du sens : Jupiter ouvre le Bélier, Vénus "
              "ouvre le Taureau, Mercure ouvre les Gémeaux, Mars ouvre le Cancer. Ce n'est pas "
              "le régent du signe, et ce décalage est la partie dont les anciens ont le plus "
              "discuté."},

    "Los dos repartos que llegaron hasta nosotros": {
        "en": "The two distributions that reached us",
        "fr": "Les deux répartitions qui nous sont parvenues"},

    "Existen dos tablas de términos en la tradición: la egipcia, que es la que este libro usa "
    "y la más antigua, y la de Ptolomeo, que la corrigió para hacerla más regular. Ptolomeo "
    "declaró que la egipcia no seguía «ningún orden natural» y propuso la suya. La egipcia le "
    "sobrevivió y es la que siguieron usando los astrólogos árabes y medievales. Se elige aquí "
    "por eso y porque es la que aparece en más manuscritos.": {
        "en": "There are two tables of terms in the tradition: the Egyptian, which is the one "
              "this book uses and the older, and Ptolemy's, which corrected it to make it more "
              "regular. Ptolemy declared that the Egyptian one followed «no natural order» and "
              "proposed his own. The Egyptian one outlived him and is the one the Arab and "
              "medieval astrologers went on using. It is chosen here for that reason and "
              "because it is the one that appears in more manuscripts.",
        "fr": "Il existe deux tables de termes dans la tradition : l'égyptienne, celle qu'emploie "
              "ce livre et la plus ancienne, et celle de Ptolémée, qui l'a corrigée pour la "
              "rendre plus régulière. Ptolémée a déclaré que l'égyptienne ne suivait « aucun "
              "ordre naturel » et a proposé la sienne. L'égyptienne lui a survécu et c'est celle "
              "que les astrologues arabes et médiévaux ont continué d'employer. On la choisit "
              "ici pour cette raison et parce que c'est celle qui figure dans le plus de "
              "manuscrits."},

    "Cómo se usa": {"en": "How it is used", "fr": "Comment on s'en sert"},
}
