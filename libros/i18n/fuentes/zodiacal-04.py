# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · los siete regentes y los treinta y seis decanatos
===================================================================
Los metales conservan el nombre antiguo que ya se fijó en las láminas: azogue
es quicksilver y vif-argent, no mercury ni mercure, porque el planeta se llama
Mercurio en el mismo párrafo y confundirlos borra la distinción que el sistema
hace entre el astro y el metal.

«Caras» es el nombre antiguo del decanato: faces en inglés, faces en francés.
Va entrecomillado en el original y se queda entrecomillado.

La aritmética del desfase —36 decanatos, 7 planetas, 36 no es múltiplo de 7—
se traduce con las cifras intactas. Es el argumento entero del apartado.
"""

T = {
    "Antes del telescopio, la astrología trabajaba con los siete cuerpos visibles a ojo "
    "desnudo. Este libro se mantiene en ese sistema clásico por una razón práctica: es "
    "coherente, cerrado y directamente utilizable, y las correspondencias de metal, piedra y "
    "órgano que verás en cada capítulo están construidas sobre él.": {
        "en": "Before the telescope, astrology worked with the seven bodies visible to the "
              "naked eye. This book stays inside that classical system for a practical reason: "
              "it is coherent, closed and directly usable, and the correspondences of metal, "
              "stone and organ you will see in every chapter are built on it.",
        "fr": "Avant le télescope, l'astrologie travaillait avec les sept corps visibles à l'œil "
              "nu. Ce livre s'en tient à ce système classique pour une raison pratique : il est "
              "cohérent, clos et directement utilisable, et les correspondances de métal, de "
              "pierre et d'organe que vous verrez dans chaque chapitre sont bâties dessus."},

    "Los siete y lo que gobiernan": {
        "en": "The seven and what they rule", "fr": "Les sept et ce qu'ils gouvernent"},

    "Leo · Oro · Identidad, vitalidad, corazón": {
        "en": "Leo · Gold · Identity, vitality, heart",
        "fr": "Lion · Or · Identité, vitalité, cœur"},

    "Cáncer · Plata · Memoria, ritmo, estómago": {
        "en": "Cancer · Silver · Memory, rhythm, stomach",
        "fr": "Cancer · Argent · Mémoire, rythme, estomac"},

    "Géminis y Virgo · Azogue · Palabra, análisis, sistema nervioso": {
        "en": "Gemini and Virgo · Quicksilver · Word, analysis, nervous system",
        "fr": "Gémeaux et Vierge · Vif-argent · Parole, analyse, système nerveux"},

    "Tauro y Libra · Cobre · Valor, vínculo, riñón y garganta": {
        "en": "Taurus and Libra · Copper · Worth, bond, kidney and throat",
        "fr": "Taureau et Balance · Cuivre · Valeur, lien, rein et gorge"},

    "Aries y Escorpio · Hierro · Impulso, deseo, sangre y músculo": {
        "en": "Aries and Scorpio · Iron · Impulse, desire, blood and muscle",
        "fr": "Bélier et Scorpion · Fer · Élan, désir, sang et muscle"},

    "Sagitario y Piscis · Estaño · Sentido, expansión, hígado": {
        "en": "Sagittarius and Pisces · Tin · Meaning, expansion, liver",
        "fr": "Sagittaire et Poissons · Étain · Sens, expansion, foie"},

    "Capricornio y Acuario · Plomo · Límite, tiempo, hueso y piel": {
        "en": "Capricorn and Aquarius · Lead · Limit, time, bone and skin",
        "fr": "Capricorne et Verseau · Plomb · Limite, temps, os et peau"},

    '<span class="fig-n">Lám. 6</span> Los siete regentes en orden caldeo, de Saturno —el más '
    "lento en su recorrido aparente— a la Luna. A la derecha, los signos que gobierna cada "
    "uno. Este orden manda también en los decanatos y en las horas planetarias.": {
        "en": '<span class="fig-n">Pl. 6</span> The seven rulers in Chaldean order, from Saturn '
              "—the slowest in its apparent course— to the Moon. On the right, the signs each "
              "one rules. This order also governs the decans and the planetary hours.",
        "fr": '<span class="fig-n">Pl. 6</span> Les sept régents dans l\'ordre chaldéen, de '
              "Saturne —le plus lent dans sa course apparente— à la Lune. À droite, les signes "
              "que chacun gouverne. Cet ordre commande aussi aux décans et aux heures "
              "planétaires."},

    "Por qué cada planeta gobierna dos signos": {
        "en": "Why each planet rules two signs",
        "fr": "Pourquoi chaque planète gouverne deux signes"},

    "El Sol y la Luna gobiernan un signo cada uno: son los dos luminares y no se reparten. Los "
    "otros cinco gobiernan dos, uno de naturaleza diurna y otro nocturna, y esa doble regencia "
    "explica parentescos que de otro modo parecen arbitrarios.": {
        "en": "The Sun and the Moon rule one sign each: they are the two luminaries and they do "
              "not divide themselves. The other five rule two, one of a diurnal and one of a "
              "nocturnal nature, and that double rulership explains kinships that otherwise "
              "look arbitrary.",
        "fr": "Le Soleil et la Lune gouvernent un signe chacun : ce sont les deux luminaires et "
              "ils ne se partagent pas. Les cinq autres en gouvernent deux, l'un de nature "
              "diurne et l'autre nocturne, et cette double régence explique des parentés qui "
              "paraîtraient autrement arbitraires."},

    "Mercurio en Géminis habla y conecta; en Virgo ordena y depura. La misma inteligencia, "
    "primero hacia fuera y luego hacia dentro.": {
        "en": "Mercury in Gemini speaks and connects; in Virgo it orders and refines. The same "
              "intelligence, first outwards and then inwards.",
        "fr": "Mercure aux Gémeaux parle et relie ; à la Vierge il ordonne et épure. La même "
              "intelligence, d'abord vers le dehors puis vers le dedans."},

    "Venus en Tauro disfruta y posee; en Libra armoniza y comparte. El mismo sentido del "
    "valor, primero en la materia y luego en la relación.": {
        "en": "Venus in Taurus enjoys and possesses; in Libra it harmonises and shares. The "
              "same sense of worth, first in matter and then in relation.",
        "fr": "Vénus au Taureau jouit et possède ; à la Balance elle harmonise et partage. Le "
              "même sens de la valeur, d'abord dans la matière puis dans la relation."},

    "Marte en Aries ataca de frente; en Escorpio persiste en silencio. La misma fuerza, "
    "primero visible y luego subterránea.": {
        "en": "Mars in Aries attacks head-on; in Scorpio it persists in silence. The same "
              "force, first visible and then underground.",
        "fr": "Mars au Bélier attaque de front ; au Scorpion il persiste en silence. La même "
              "force, d'abord visible puis souterraine."},

    "Júpiter en Sagitario busca horizonte; en Piscis busca compasión. El mismo impulso de "
    "sentido, primero hacia lo lejano y luego hacia lo profundo.": {
        "en": "Jupiter in Sagittarius looks for a horizon; in Pisces it looks for compassion. "
              "The same impulse towards meaning, first towards the far and then towards the "
              "deep.",
        "fr": "Jupiter au Sagittaire cherche l'horizon ; aux Poissons il cherche la compassion. "
              "Le même élan de sens, d'abord vers le lointain puis vers le profond."},

    "Saturno en Capricornio construye estructuras; en Acuario las cuestiona. El mismo rigor, "
    "primero para levantar y luego para revisar.": {
        "en": "Saturn in Capricorn builds structures; in Aquarius it questions them. The same "
              "rigour, first for raising and then for reviewing.",
        "fr": "Saturne au Capricorne bâtit des structures ; au Verseau il les met en question. "
              "La même rigueur, d'abord pour élever puis pour réviser."},

    "Una nota de honestidad": {
        "en": "A note of honesty", "fr": "Une note d'honnêteté"},

    "La astrología moderna asignó Urano a Acuario, Neptuno a Piscis y Plutón a Escorpio. Es "
    "una tradición válida y muy extendida, pero rompe la simetría del sistema de siete y "
    "complica las correspondencias corporales. Aquí se usa el esquema clásico. Si trabajas con "
    "el moderno, todo lo que sigue sigue siendo compatible: solo añade una capa más.": {
        "en": "Modern astrology assigned Uranus to Aquarius, Neptune to Pisces and Pluto to "
              "Scorpio. It is a valid and very widespread tradition, but it breaks the symmetry "
              "of the system of seven and complicates the bodily correspondences. The classical "
              "scheme is used here. If you work with the modern one, everything that follows "
              "remains compatible: it just adds one more layer.",
        "fr": "L'astrologie moderne a attribué Uranus au Verseau, Neptune aux Poissons et Pluton "
              "au Scorpion. C'est une tradition valable et très répandue, mais elle rompt la "
              "symétrie du système des sept et complique les correspondances corporelles. On "
              "emploie ici le schéma classique. Si vous travaillez avec le moderne, tout ce qui "
              "suit reste compatible : cela ne fait qu'ajouter une couche."},

    # ── Los treinta y seis decanatos ───────────────────────────────────────
    "Aquí empieza la parte del sistema que casi ningún libro divulgativo explica, y que sin "
    "embargo resuelve la objeción más común que se le hace a la astrología: «no me parezco a "
    "mi signo».": {
        "en": "Here begins the part of the system that hardly any popular book explains, and "
              "that nevertheless answers the commonest objection made to astrology: «I am not "
              "like my sign».",
        "fr": "Ici commence la partie du système que presque aucun livre de vulgarisation "
              "n'explique, et qui pourtant répond à l'objection la plus courante faite à "
              "l'astrologie : « je ne ressemble pas à mon signe »."},

    "La respuesta tradicional es que un signo no es un bloque uniforme. Ocupa treinta grados "
    "de la rueda, y esos treinta grados se dividen en tres tramos de diez que se llaman "
    "decanatos —o, en los tratados antiguos, «caras». Cada tramo tiene un planeta al frente "
    "que matiza el signo sin cambiar su naturaleza. Un Tauro de la primera cara y un Tauro de "
    "la tercera comparten elemento, modalidad y regente, y se comportan de forma "
    "perceptiblemente distinta.": {
        "en": "The traditional answer is that a sign is not a uniform block. It occupies thirty "
              "degrees of the wheel, and those thirty degrees are divided into three stretches "
              "of ten called decans —or, in the old treatises, «faces». Each stretch has a "
              "planet at its head that shades the sign without changing its nature. A Taurus of "
              "the first face and a Taurus of the third share element, modality and ruler, and "
              "behave perceptibly differently.",
        "fr": "La réponse traditionnelle est qu'un signe n'est pas un bloc uniforme. Il occupe "
              "trente degrés de la roue, et ces trente degrés se divisent en trois tronçons de "
              "dix appelés décans —ou, dans les vieux traités, « faces ». Chaque tronçon a une "
              "planète à sa tête qui nuance le signe sans changer sa nature. Un Taureau de la "
              "première face et un Taureau de la troisième partagent élément, modalité et "
              "régent, et se comportent de façon perceptiblement différente."},

    "Cómo se reparten": {
        "en": "How they are shared out", "fr": "Comment ils se répartissent"},

    "El reparto no es arbitrario: sigue el orden caldeo, la secuencia de los siete planetas "
    "ordenados del más lento al más rápido en su recorrido aparente. Saturno, Júpiter, Marte, "
    "Sol, Venus, Mercurio, Luna. La serie arranca en Marte, que rige el primer decanato de "
    "Aries, y desde ahí avanza un paso por cada tramo de diez grados, dando la vuelta cuando "
    "se agota.": {
        "en": "The distribution is not arbitrary: it follows the Chaldean order, the sequence "
              "of the seven planets arranged from slowest to fastest in their apparent course. "
              "Saturn, Jupiter, Mars, Sun, Venus, Mercury, Moon. The series starts at Mars, "
              "which rules the first decan of Aries, and from there it advances one step for "
              "each stretch of ten degrees, coming round again when it runs out.",
        "fr": "La répartition n'est pas arbitraire : elle suit l'ordre chaldéen, la séquence des "
              "sept planètes rangées de la plus lente à la plus rapide dans leur course "
              "apparente. Saturne, Jupiter, Mars, Soleil, Vénus, Mercure, Lune. La série "
              "démarre à Mars, qui régit le premier décan du Bélier, et de là elle avance d'un "
              "pas par tronçon de dix degrés, en repartant du début quand elle s'épuise."},

    "Por qué la serie se desfasa": {
        "en": "Why the series drifts out of step", "fr": "Pourquoi la série se décale"},

    "Treinta y seis decanatos y siete planetas: 36 no es múltiplo de 7. La serie no cierra, y "
    "por eso cada signo empieza con un planeta distinto al que le tocaría si el reparto fuera "
    "regular. No es un error de transmisión: es la mecánica del propio reparto, y es la razón "
    "de que la tabla haya que aprenderla y no deducirla.": {
        "en": "Thirty-six decans and seven planets: 36 is not a multiple of 7. The series does "
              "not close, and that is why each sign begins with a planet other than the one it "
              "would get if the distribution were regular. It is not an error of transmission: "
              "it is the mechanics of the distribution itself, and it is the reason the table "
              "has to be learnt and not deduced.",
        "fr": "Trente-six décans et sept planètes : 36 n'est pas un multiple de 7. La série ne "
              "se referme pas, et c'est pourquoi chaque signe commence par une planète autre que "
              "celle qui lui reviendrait si la répartition était régulière. Ce n'est pas une "
              "erreur de transmission : c'est la mécanique même de la répartition, et c'est la "
              "raison pour laquelle la table doit s'apprendre et non se déduire."},

    '<span class="fig-n">Lám. 1</span> Los treinta y seis decanatos. Cada fila es un signo; '
    "cada columna, un tramo de diez grados con el planeta que lo rige. La serie recorre el "
    "orden caldeo sin interrupción de Aries a Piscis.": {
        "en": '<span class="fig-n">Pl. 1</span> The thirty-six decans. Each row is a sign; each '
              "column, a stretch of ten degrees with the planet that rules it. The series runs "
              "through the Chaldean order without interruption from Aries to Pisces.",
        "fr": '<span class="fig-n">Pl. 1</span> Les trente-six décans. Chaque ligne est un '
              "signe ; chaque colonne, un tronçon de dix degrés avec la planète qui le régit. La "
              "série parcourt l'ordre chaldéen sans interruption du Bélier aux Poissons."},

    "Cómo usar tu decanato": {
        "en": "How to use your decan", "fr": "Comment utiliser votre décan"},

    "Localiza tu signo por la fecha de nacimiento.": {
        "en": "Locate your sign by your date of birth.",
        "fr": "Repérez votre signe par votre date de naissance."},

    "Dentro del capítulo de tu signo, busca la sección «Los tres decanatos» y encuentra el "
    "tramo que contiene tu fecha.": {
        "en": "Inside your sign's chapter, look for the section «The three decans» and find the "
              "stretch that contains your date.",
        "fr": "Dans le chapitre de votre signe, cherchez la section « Les trois décans » et "
              "trouvez le tronçon qui contient votre date."},

    "Lee la descripción general del signo y luego el matiz del decanato. El primero te da el "
    "material; el segundo, el acabado.": {
        "en": "Read the general description of the sign and then the shading of the decan. The "
              "first gives you the material; the second, the finish.",
        "fr": "Lisez la description générale du signe puis la nuance du décan. La première vous "
              "donne le matériau ; la seconde, la finition."},
}
