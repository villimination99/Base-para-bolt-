# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · la rueda, los elementos, las modalidades y las polaridades
============================================================================
Los nombres de los doce signos quedan fijados aquí en la forma de cada lengua
—Bélier, Gémeaux, Vierge, Balance, Verseau, Poissons— y se usarán así en todo
el libro. El resto de capítulos los repite cientos de veces y conviene que no
haya dos formas de decirlos.

Las tres letras del anillo intermedio de la rueda —C, F, M— no son un segmento
traducible: el dibujo toma la inicial del nombre castellano de la modalidad.
Da igual, porque Cardinal, Fixed y Mutable en inglés y Cardinal, Fixe y
Mutable en francés empiezan por esas mismas tres letras. La glosa de la lámina
las nombra tal cual.

«Soy así porque soy Escorpio» es la frase que el capítulo desmonta, y en las
tres lenguas se dice como la diría alguien que la usa de excusa.
"""

T = {
    "No es un manual de predicción, no calcula cartas natales y no promete resultados. Tampoco "
    "es un texto médico ni psicológico: cuando en estas páginas se habla del cuerpo, se habla "
    "de hábitos de cuidado, no de diagnósticos ni de tratamientos. Si algo te duele, la "
    "respuesta está en una consulta, no en un signo.": {
        "en": "It is not a manual of prediction, it does not calculate birth charts and it "
              "promises no results. Nor is it a medical or psychological text: when these pages "
              "speak of the body, they speak of habits of care, not of diagnoses or treatments. "
              "If something hurts, the answer is in a consulting room, not in a sign.",
        "fr": "Ce n'est pas un manuel de prédiction, il ne calcule pas de thèmes de naissance et "
              "il ne promet aucun résultat. Ce n'est pas davantage un texte médical ou "
              "psychologique : quand ces pages parlent du corps, elles parlent d'habitudes de "
              "soin, non de diagnostics ni de traitements. Si quelque chose vous fait mal, la "
              "réponse est dans un cabinet, pas dans un signe."},

    "Puedes leerlo entero de una vez para tener el mapa completo, o ir directo a tu signo. Pero "
    "el mayor provecho está en el uso que propone la tercera parte: recorrer los doce signos a "
    "lo largo de un año, un mes cada uno, trabajando la cualidad que le corresponde. Nadie es "
    "solo su signo solar; todos llevamos los doce dentro, unos desarrollados y otros "
    "dormidos.": {
        "en": "You can read it all at once to have the complete map, or go straight to your "
              "sign. But the greatest benefit lies in the use the third part proposes: going "
              "through the twelve signs over the course of a year, a month for each, working on "
              "the quality that belongs to it. Nobody is only their sun sign; we all carry the "
              "twelve inside, some of them developed and others asleep.",
        "fr": "Vous pouvez le lire d'un bout à l'autre pour avoir la carte complète, ou aller "
              "droit à votre signe. Mais le plus grand profit tient à l'usage que propose la "
              "troisième partie : parcourir les douze signes au long d'une année, un mois "
              "chacun, en travaillant la qualité qui lui revient. Personne n'est seulement son "
              "signe solaire ; nous portons tous les douze en nous, les uns développés et les "
              "autres endormis."},

    "Una última advertencia, y va en serio. Si usas este sistema para justificarte —«soy así "
    "porque soy Escorpio»— lo has convertido en una jaula y habrás perdido el tiempo. El signo "
    "describe la materia prima con la que trabajas, no la sentencia. Todo lo que sigue está "
    "escrito para lo contrario: para que reconozcas tu patrón y luego decidas qué haces con "
    "él.": {
        "en": "One last warning, and it is meant seriously. If you use this system to excuse "
              "yourself —«I'm like this because I'm a Scorpio»— you have turned it into a cage "
              "and you will have wasted your time. The sign describes the raw material you work "
              "with, not the sentence. Everything that follows is written for the opposite: so "
              "that you recognise your pattern and then decide what you do with it.",
        "fr": "Un dernier avertissement, et il est sérieux. Si vous vous servez de ce système "
              "pour vous justifier —« je suis comme ça parce que je suis Scorpion »— vous en "
              "avez fait une cage et vous aurez perdu votre temps. Le signe décrit la matière "
              "première avec laquelle vous travaillez, non la sentence. Tout ce qui suit est "
              "écrit pour l'inverse : pour que vous reconnaissiez votre schéma et que vous "
              "décidiez ensuite quoi en faire."},

    # ── La rueda y sus cuatro elementos ────────────────────────────────────
    "La rueda zodiacal no es una lista de doce categorías sueltas. Es una estructura con tres "
    "clasificaciones que se cruzan, y entender ese cruce vale más que memorizar los doce "
    "signos por separado.": {
        "en": "The zodiacal wheel is not a list of twelve loose categories. It is a structure "
              "with three classifications that cross one another, and understanding that "
              "crossing is worth more than memorising the twelve signs separately.",
        "fr": "La roue zodiacale n'est pas une liste de douze catégories éparses. C'est une "
              "structure à trois classifications qui se croisent, et comprendre ce croisement "
              "vaut mieux que mémoriser les douze signes séparément."},

    "Los cuatro elementos: la materia del temperamento": {
        "en": "The four elements: the matter of temperament",
        "fr": "Les quatre éléments : la matière du tempérament"},

    "Cada signo pertenece a un elemento, y el elemento describe de qué está hecha su energía "
    "antes de cualquier otra consideración.": {
        "en": "Each sign belongs to an element, and the element describes what its energy is "
              "made of before any other consideration.",
        "fr": "Chaque signe appartient à un élément, et l'élément décrit de quoi son énergie est "
              "faite avant toute autre considération."},

    "Los cuatro elementos": {"en": "The four elements", "fr": "Les quatre éléments"},

    "Aries, Leo, Sagitario · Impulso, iniciativa, entusiasmo, calor": {
        "en": "Aries, Leo, Sagittarius · Impulse, initiative, enthusiasm, heat",
        "fr": "Bélier, Lion, Sagittaire · Élan, initiative, enthousiasme, chaleur"},

    "Tauro, Virgo, Capricornio · Forma, constancia, resultado, cuerpo": {
        "en": "Taurus, Virgo, Capricorn · Form, constancy, result, body",
        "fr": "Taureau, Vierge, Capricorne · Forme, constance, résultat, corps"},

    "Géminis, Libra, Acuario · Idea, relación, palabra, distancia": {
        "en": "Gemini, Libra, Aquarius · Idea, relation, word, distance",
        "fr": "Gémeaux, Balance, Verseau · Idée, relation, parole, distance"},

    "Cáncer, Escorpio, Piscis · Emoción, memoria, vínculo, profundidad": {
        "en": "Cancer, Scorpio, Pisces · Emotion, memory, bond, depth",
        "fr": "Cancer, Scorpion, Poissons · Émotion, mémoire, lien, profondeur"},

    '<span class="fig-n">Lám. 4</span> Las doce casillas: cuatro elementos por tres '
    "modalidades. Ninguna combinación se repite, y ahí está la razón de que el sistema "
    "funcione como clasificación.": {
        "en": '<span class="fig-n">Pl. 4</span> The twelve cells: four elements by three '
              "modalities. No combination repeats, and there lies the reason the system works "
              "as a classification.",
        "fr": '<span class="fig-n">Pl. 4</span> Les douze cases : quatre éléments par trois '
              "modalités. Aucune combinaison ne se répète, et c'est là la raison pour laquelle "
              "le système fonctionne comme classification."},

    "Los elementos se ordenan en dos parejas naturales. Fuego y Aire son expansivos: salen "
    "hacia fuera, se comunican, se gastan rápido. Tierra y Agua son receptivos: acumulan, "
    "conservan, tardan en moverse y tardan en parar. Casi todos los conflictos de convivencia "
    "que verás descritos en este libro salen de esa diferencia de ritmo, no de mala voluntad.": {
        "en": "The elements arrange themselves in two natural pairs. Fire and Air are "
              "expansive: they go outwards, they communicate, they spend themselves quickly. "
              "Earth and Water are receptive: they accumulate, they conserve, they are slow to "
              "start moving and slow to stop. Almost every conflict of living together you will "
              "see described in this book comes out of that difference of pace, not out of ill "
              "will.",
        "fr": "Les éléments s'ordonnent en deux couples naturels. Le Feu et l'Air sont "
              "expansifs : ils vont vers le dehors, ils communiquent, ils se dépensent vite. La "
              "Terre et l'Eau sont réceptives : elles accumulent, elles conservent, elles "
              "mettent du temps à se mettre en mouvement et du temps à s'arrêter. Presque tous "
              "les conflits de vie commune que vous verrez décrits dans ce livre naissent de "
              "cette différence de rythme, non d'une mauvaise volonté."},

    "Las tres modalidades: cómo se mueve esa energía": {
        "en": "The three modalities: how that energy moves",
        "fr": "Les trois modalités : comment cette énergie se meut"},

    "Las tres modalidades": {"en": "The three modalities", "fr": "Les trois modalités"},

    "Cardinal": {"en": "Cardinal", "fr": "Cardinal"},
    "Aries, Cáncer, Libra, Capricornio · Inician. Abren estación": {
        "en": "Aries, Cancer, Libra, Capricorn · They initiate. They open a season",
        "fr": "Bélier, Cancer, Balance, Capricorne · Ils initient. Ils ouvrent la saison"},

    "Fijo": {"en": "Fixed", "fr": "Fixe"},
    "Tauro, Leo, Escorpio, Acuario · Sostienen. Mantienen el centro": {
        "en": "Taurus, Leo, Scorpio, Aquarius · They sustain. They hold the centre",
        "fr": "Taureau, Lion, Scorpion, Verseau · Ils soutiennent. Ils tiennent le centre"},

    "Mutable": {"en": "Mutable", "fr": "Mutable"},
    "Géminis, Virgo, Sagitario, Piscis · Adaptan. Cierran y transforman": {
        "en": "Gemini, Virgo, Sagittarius, Pisces · They adapt. They close and transform",
        "fr": "Gémeaux, Vierge, Sagittaire, Poissons · Ils adaptent. Ils closent et transforment"},

    "La modalidad explica por qué dos signos del mismo elemento se comportan de forma tan "
    "distinta. Aries, Leo y Sagitario son los tres de Fuego, pero Aries enciende, Leo mantiene "
    "la llama y Sagitario la reparte. El elemento dice «qué»; la modalidad dice «cómo».": {
        "en": "Modality explains why two signs of the same element behave so differently. "
              "Aries, Leo and Sagittarius are the three of Fire, but Aries lights, Leo keeps "
              "the flame and Sagittarius hands it round. The element says «what»; the modality "
              "says «how».",
        "fr": "La modalité explique pourquoi deux signes du même élément se comportent de façon "
              "si différente. Bélier, Lion et Sagittaire sont les trois du Feu, mais le Bélier "
              "allume, le Lion entretient la flamme et le Sagittaire la distribue. L'élément dit "
              "« quoi » ; la modalité dit « comment »."},

    "Las dos polaridades: hacia dónde apunta": {
        "en": "The two polarities: which way it points",
        "fr": "Les deux polarités : vers où cela pointe"},

    "La tercera clasificación alterna signo a signo alrededor de la rueda. Los signos de Fuego "
    "y Aire se llaman tradicionalmente activos o diurnos: su movimiento natural va del "
    "interior hacia el mundo. Los de Tierra y Agua son receptivos o nocturnos: su movimiento "
    "va del mundo hacia el interior.": {
        "en": "The third classification alternates sign by sign around the wheel. The signs of "
              "Fire and Air are traditionally called active or diurnal: their natural movement "
              "goes from the inside towards the world. Those of Earth and Water are receptive "
              "or nocturnal: their movement goes from the world towards the inside.",
        "fr": "La troisième classification alterne signe par signe tout autour de la roue. Les "
              "signes de Feu et d'Air sont traditionnellement dits actifs ou diurnes : leur "
              "mouvement naturel va du dedans vers le monde. Ceux de Terre et d'Eau sont "
              "réceptifs ou nocturnes : leur mouvement va du monde vers le dedans."},

    "El cruce es lo que individualiza": {
        "en": "The crossing is what individualises",
        "fr": "C'est le croisement qui individualise"},

    "Doce signos = cuatro elementos × tres modalidades. Ninguna combinación se repite, y por "
    "eso el sistema funciona como clasificación: cada signo es el único que ocupa su casilla. "
    "Capricornio es el único Tierra Cardinal, Escorpio el único Agua Fijo. Cuando dudes de la "
    "naturaleza de un signo, reconstruye su casilla y saldrá solo.": {
        "en": "Twelve signs = four elements × three modalities. No combination repeats, and "
              "that is why the system works as a classification: each sign is the only one "
              "occupying its cell. Capricorn is the only Cardinal Earth, Scorpio the only Fixed "
              "Water. When you are in doubt about the nature of a sign, rebuild its cell and it "
              "will come out on its own.",
        "fr": "Douze signes = quatre éléments × trois modalités. Aucune combinaison ne se "
              "répète, et c'est pourquoi le système fonctionne comme classification : chaque "
              "signe est le seul à occuper sa case. Le Capricorne est la seule Terre Cardinale, "
              "le Scorpion la seule Eau Fixe. Quand vous doutez de la nature d'un signe, "
              "reconstruisez sa case et elle sortira toute seule."},

    "La rueda como año y como proceso": {
        "en": "The wheel as a year and as a process",
        "fr": "La roue comme année et comme processus"},

    "La secuencia de los doce signos describe un ciclo completo, y esa es la clave que "
    "convierte el zodiaco en herramienta de trabajo. Empieza en Aries con el impulso puro —la "
    "semilla que rompe la tierra—, gana cuerpo en Tauro, se hace consciente en Géminis, se "
    "interioriza en Cáncer. Llega a su expresión plena en Leo, se depura en Virgo, se abre al "
    "otro en Libra, se transforma en Escorpio. Busca sentido en Sagitario, lo estructura en "
    "Capricornio, lo comparte en Acuario y lo disuelve en Piscis para que Aries pueda volver a "
    "empezar.": {
        "en": "The sequence of the twelve signs describes a complete cycle, and that is the key "
              "that turns the zodiac into a working tool. It begins in Aries with pure impulse "
              "—the seed breaking through the soil—, it gains body in Taurus, it becomes "
              "conscious in Gemini, it turns inward in Cancer. It reaches full expression in "
              "Leo, it is refined in Virgo, it opens to the other in Libra, it is transformed "
              "in Scorpio. It looks for meaning in Sagittarius, it gives it structure in "
              "Capricorn, it shares it in Aquarius and it dissolves it in Pisces so that Aries "
              "can begin again.",
        "fr": "La séquence des douze signes décrit un cycle complet, et c'est là la clé qui fait "
              "du zodiaque un outil de travail. Elle commence au Bélier par l'élan pur —la "
              "graine qui rompt la terre—, prend corps au Taureau, devient consciente aux "
              "Gémeaux, s'intériorise au Cancer. Elle atteint sa pleine expression au Lion, "
              "s'épure à la Vierge, s'ouvre à l'autre à la Balance, se transforme au Scorpion. "
              "Elle cherche un sens au Sagittaire, le structure au Capricorne, le partage au "
              "Verseau et le dissout aux Poissons pour que le Bélier puisse recommencer."},

    '<span class="fig-n">Lám. 5</span> La rueda completa. Anillo exterior: los doce signos con '
    "su glifo y su color de elemento. Anillo intermedio: la modalidad (C, F, M). Anillo "
    "interior: el sigilo del planeta regente. En el centro, los cuatro elementos en cruz.": {
        "en": '<span class="fig-n">Pl. 5</span> The complete wheel. Outer ring: the twelve '
              "signs with their glyph and their element colour. Middle ring: the modality (C, "
              "F, M). Inner ring: the sigil of the ruling planet. At the centre, the four "
              "elements in a cross.",
        "fr": '<span class="fig-n">Pl. 5</span> La roue complète. Anneau extérieur : les douze '
              "signes avec leur glyphe et leur couleur d'élément. Anneau intermédiaire : la "
              "modalité (C, F, M). Anneau intérieur : le sceau de la planète régente. Au "
              "centre, les quatre éléments en croix."},

    "Leído así, el zodiaco deja de ser una etiqueta de nacimiento y se convierte en un "
    "itinerario. Es exactamente el uso que propone la tercera parte de este libro.": {
        "en": "Read this way, the zodiac stops being a birth label and becomes an itinerary. "
              "That is exactly the use the third part of this book proposes.",
        "fr": "Lu ainsi, le zodiaque cesse d'être une étiquette de naissance et devient un "
              "itinéraire. C'est exactement l'usage que propose la troisième partie de ce "
              "livre."},
}
