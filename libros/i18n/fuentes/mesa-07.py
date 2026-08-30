# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · cierre del capítulo 8 y la tabla de los diecinueve
=====================================================================
Aquí conviven dos cosas que se traducen distinto. Las cifras de agua llevan
coma decimal en español y en francés y punto en inglés: «3,7 litros» frente a
«3.7 litres». Y las unidades tramposas —µg RAE, µg DFE, mg NE— no se traducen
en absoluto, porque son siglas internacionales; lo que se traduce es la glosa
que las acompaña, que es justamente lo que las hace útiles.
"""

T = {
    # ── Capítulo 8 · el agua ───────────────────────────────────────────────
    "3,7 litros al día": {
        "en": "3.7 litres a day", "fr": "3,7 litres par jour"},
    "2,7 litros al día": {
        "en": "2.7 litres a day", "fr": "2,7 litres par jour"},
    "Atención": {"en": "Careful", "fr": "Attention"},

    "Es agua TOTAL: incluye la de los alimentos y la de todas las bebidas. Alrededor del "
    "20 % suele venir de la comida, así que el agua bebida queda bastante por debajo de esa "
    "cifra.": {
        "en": "This is TOTAL water: it includes the water in food and in every drink. Around "
              "20 % usually comes from food, so water actually drunk falls well below that "
              "figure.",
        "fr": "Il s'agit de l'eau TOTALE : celle des aliments et celle de toutes les "
              "boissons. Environ 20 % provient en général de la nourriture, si bien que "
              "l'eau bue reste nettement en dessous de ce chiffre."},

    "Es agua TOTAL: la de las bebidas y la de los alimentos. Una fruta es en su mayor parte "
    "agua, y una sopa, un yogur o un plato de verdura aportan cantidades que no son "
    "marginales. Con la comida ronda un veinte por ciento del total, así que el agua que hay "
    "que beber queda claramente por debajo de esas cifras. Los ocho vasos diarios que se "
    "repiten en todas partes no salen de ningún documento oficial: son una simplificación "
    "que sobrevivió por repetición.": {
        "en": "This is TOTAL water: the water in drinks and the water in food. A piece of "
              "fruit is mostly water, and a soup, a yoghurt or a plate of vegetables "
              "contribute amounts that are anything but marginal. Food accounts for around "
              "twenty per cent of the total, so the water you actually have to drink falls "
              "clearly below those figures. The eight daily glasses repeated everywhere come "
              "from no official document: they are a simplification that survived by "
              "repetition.",
        "fr": "Il s'agit de l'eau TOTALE : celle des boissons et celle des aliments. Un "
              "fruit est en grande partie de l'eau, et une soupe, un yaourt ou une assiette "
              "de légumes apportent des quantités qui ne sont pas marginales. La nourriture "
              "représente environ vingt pour cent du total, si bien que l'eau qu'il faut "
              "réellement boire reste nettement en dessous de ces chiffres. Les huit verres "
              "quotidiens répétés partout ne sortent d'aucun document officiel : c'est une "
              "simplification qui a survécu par répétition."},

    "Y una advertencia en la otra dirección, porque existe y se olvida: se puede beber "
    "demasiada agua. Superar durante horas la capacidad de excreción del riñón diluye el "
    "sodio de la sangre, y eso es un cuadro grave. Ocurre sobre todo en pruebas de "
    "resistencia largas donde se bebe mucho y solo agua. La señal de que el equilibrio es "
    "razonable es de una banalidad tranquilizadora: orina clara varias veces al día y sed "
    "ausente.": {
        "en": "And a warning in the other direction, because it exists and gets forgotten: "
              "you can drink too much water. Exceeding the kidney's excretion capacity for "
              "hours on end dilutes the sodium in the blood, and that is a serious "
              "condition. It happens above all in long endurance events where people drink a "
              "great deal and drink only water. The sign that the balance is reasonable is "
              "reassuringly banal: clear urine several times a day and no thirst.",
        "fr": "Et un avertissement dans l'autre sens, car il existe et on l'oublie : on peut "
              "boire trop d'eau. Dépasser pendant des heures la capacité d'excrétion du rein "
              "dilue le sodium du sang, et c'est un tableau grave. Cela survient surtout lors "
              "d'épreuves d'endurance longues où l'on boit beaucoup et uniquement de l'eau. "
              "Le signe que l'équilibre est raisonnable est d'une banalité rassurante : des "
              "urines claires plusieurs fois par jour et pas de soif."},

    # ── Capítulo 9 · los diecinueve micronutrientes ────────────────────────
    "Aquí está la tabla que casi nadie imprime completa. Diecinueve micronutrientes con su "
    "valor de referencia para hombres y para mujeres y, en la misma línea, su techo. La "
    "columna de la derecha es la que falta en el resto de sitios, y es la que hace falta el "
    "día que alguien decide comprarse un bote.": {
        "en": "Here is the table almost nobody prints in full. Nineteen micronutrients with "
              "their reference value for men and for women and, on the same line, their "
              "ceiling. The right-hand column is the one missing everywhere else, and it is "
              "the one you need the day someone decides to buy themselves a tub.",
        "fr": "Voici le tableau que presque personne n'imprime en entier. Dix-neuf "
              "micronutriments avec leur valeur de référence pour les hommes et pour les "
              "femmes et, sur la même ligne, leur plafond. La colonne de droite est celle qui "
              "manque partout ailleurs, et c'est celle dont on a besoin le jour où quelqu'un "
              "décide de s'acheter un pot."},

    '<span class="fig-n">Los diecinueve nutrientes con su referencia y su techo</span> Cada '
    "fila lleva el valor recomendado y, cuando existe, el límite superior tolerable. Las "
    "filas sin techo no son las más seguras: son aquellas para las que no había datos "
    "suficientes para establecer uno, que es una situación distinta y no necesariamente "
    "mejor.": {
        "en": '<span class="fig-n">The nineteen nutrients with their reference and their '
              "ceiling</span> Each row carries the recommended value and, where one exists, "
              "the tolerable upper limit. The rows with no ceiling are not the safest ones: "
              "they are the ones for which there were not enough data to set one, which is a "
              "different situation and not necessarily a better one.",
        "fr": '<span class="fig-n">Les dix-neuf nutriments avec leur référence et leur '
              "plafond</span> Chaque ligne porte la valeur recommandée et, lorsqu'elle "
              "existe, la limite supérieure tolérable. Les lignes sans plafond ne sont pas "
              "les plus sûres : ce sont celles pour lesquelles les données étaient "
              "insuffisantes pour en fixer un, ce qui est une situation différente et pas "
              "nécessairement meilleure."},

    "Cómo leer las filas sin techo": {
        "en": "How to read the rows with no ceiling",
        "fr": "Comment lire les lignes sans plafond"},

    "Nueve de los diecinueve no tienen límite establecido. Es tentador leerlo como «este se "
    "puede tomar sin cuidado», y es lo contrario de lo que significa. Un techo se establece "
    "cuando existen datos suficientes sobre efectos adversos para fijar un punto; su "
    "ausencia indica falta de datos, no ausencia de riesgo. Los documentos oficiales lo dicen "
    "con estas palabras y aun así se malinterpreta en todas partes.": {
        "en": "Nine of the nineteen have no established limit. It is tempting to read that "
              "as «this one can be taken carelessly», and it is the opposite of what it "
              "means. A ceiling is set when there are enough data on adverse effects to fix a "
              "point; its absence indicates a lack of data, not an absence of risk. The "
              "official documents say so in these very words and it is still misread "
              "everywhere.",
        "fr": "Neuf des dix-neuf n'ont pas de limite établie. Il est tentant de le lire comme "
              "« celui-ci, on peut le prendre sans précaution », et c'est le contraire de ce "
              "que cela signifie. Un plafond s'établit lorsqu'il existe assez de données sur "
              "les effets indésirables pour fixer un point ; son absence indique un manque de "
              "données, pas une absence de risque. Les documents officiels le disent avec ces "
              "mots-là et on continue partout à le mal interpréter."},

    "Las unidades tramposas": {
        "en": "The units that trip you up", "fr": "Les unités piégeuses"},

    "Cuatro nutrientes se miden en unidades que incorporan una conversión, y si no se sabe, "
    "las cuentas salen mal por un factor grande. Son estas:": {
        "en": "Four nutrients are measured in units that build in a conversion, and if you "
              "do not know it, the arithmetic comes out wrong by a large factor. They are "
              "these:",
        "fr": "Quatre nutriments se mesurent dans des unités qui incorporent une conversion, "
              "et si on l'ignore, les calculs sont faux d'un facteur important. Les voici :"},

    "Unidades que esconden una equivalencia": {
        "en": "Units that hide an equivalence",
        "fr": "Des unités qui cachent une équivalence"},

    "µg RAE · vitamina A": {
        "en": "µg RAE · vitamin A", "fr": "µg RAE · vitamine A"},

    "Equivalentes de actividad de retinol. Un microgramo de retinol equivale a doce de "
    "betacaroteno de los alimentos y a veinticuatro de los demás carotenoides con actividad. "
    "Comer zanahorias no es lo mismo que tomar retinol, y el techo se refiere solo al "
    "segundo.": {
        "en": "Retinol activity equivalents. One microgram of retinol is equivalent to twelve "
              "of dietary beta-carotene and to twenty-four of the other active carotenoids. "
              "Eating carrots is not the same as taking retinol, and the ceiling refers only "
              "to the latter.",
        "fr": "Équivalents d'activité du rétinol. Un microgramme de rétinol équivaut à douze "
              "de bêta-carotène alimentaire et à vingt-quatre des autres caroténoïdes actifs. "
              "Manger des carottes n'est pas la même chose que prendre du rétinol, et le "
              "plafond ne concerne que le second."},

    "µg DFE · folato": {"en": "µg DFE · folate", "fr": "µg DFE · folates"},

    "Equivalentes dietéticos de folato. El ácido fólico de los suplementos y de los alimentos "
    "fortificados se absorbe bastante mejor que el folato natural, y la unidad lo corrige. El "
    "techo se refiere solo a la forma sintética.": {
        "en": "Dietary folate equivalents. The folic acid in supplements and fortified foods "
              "is absorbed considerably better than natural folate, and the unit corrects for "
              "it. The ceiling refers only to the synthetic form.",
        "fr": "Équivalents en folates alimentaires. L'acide folique des compléments et des "
              "aliments enrichis s'absorbe nettement mieux que les folates naturels, et "
              "l'unité le corrige. Le plafond ne concerne que la forme synthétique."},

    "mg NE · niacina": {"en": "mg NE · niacin", "fr": "mg NE · niacine"},

    "Equivalentes de niacina. El cuerpo fabrica niacina a partir de triptófano, a razón de "
    "unos sesenta miligramos de aminoácido por cada miligramo de vitamina, y la unidad lo "
    "incluye.": {
        "en": "Niacin equivalents. The body makes niacin from tryptophan, at a rate of about "
              "sixty milligrams of the amino acid per milligram of the vitamin, and the unit "
              "includes it.",
        "fr": "Équivalents niacine. Le corps fabrique de la niacine à partir du tryptophane, à "
              "raison d'environ soixante milligrammes d'acide aminé par milligramme de "
              "vitamine, et l'unité l'intègre."},

    "mg · vitamina E": {"en": "mg · vitamin E", "fr": "mg · vitamine E"},

    "Solo cuenta el alfa-tocoferol, y solo determinadas formas estereoisoméricas. Buena parte "
    "de la «vitamina E» de algunas etiquetas no cuenta para esta cifra.": {
        "en": "Only alpha-tocopherol counts, and only certain stereoisomeric forms. A good "
              "part of the «vitamin E» on some labels does not count towards this figure.",
        "fr": "Seul l'alpha-tocophérol compte, et seulement certaines formes "
              "stéréo-isomériques. Une bonne partie de la « vitamine E » de certaines "
              "étiquettes ne compte pas dans ce chiffre."},

    "Lo que el marco da por supuesto": {
        "en": "What the framework takes for granted",
        "fr": "Ce que le cadre tient pour acquis"},

    "Estas cifras suponen una dieta mixta y variada, porque la biodisponibilidad depende del "
    "acompañamiento. Los propios documentos señalan dos casos concretos: el hierro de origen "
    "vegetal se absorbe bastante peor, y una dieta sin carne puede requerir del orden del "
    "ochenta por ciento más de hierro; y una dieta muy rica en fitatos —legumbres y cereales "
    "integrales, que por lo demás son excelentes— puede elevar la necesidad de zinc hasta la "
    "mitad. No es un argumento contra las dietas vegetales: es la letra pequeña que hay que "
    "conocer para llevarlas bien.": {
        "en": "These figures assume a mixed and varied diet, because bioavailability depends "
              "on what comes alongside. The documents themselves point to two specific cases: "
              "iron of plant origin is absorbed considerably worse, and a meat-free diet may "
              "require on the order of eighty per cent more iron; and a diet very rich in "
              "phytates —pulses and wholegrain cereals, which are otherwise excellent— can "
              "raise the need for zinc by as much as half. This is not an argument against "
              "plant-based diets: it is the small print you have to know in order to follow "
              "them well.",
        "fr": "Ces chiffres supposent un régime mixte et varié, car la biodisponibilité dépend "
              "de l'accompagnement. Les documents eux-mêmes signalent deux cas précis : le fer "
              "d'origine végétale s'absorbe nettement moins bien, et un régime sans viande "
              "peut exiger de l'ordre de quatre-vingts pour cent de fer en plus ; et un régime "
              "très riche en phytates —légumineuses et céréales complètes, excellentes par "
              "ailleurs— peut augmenter le besoin en zinc jusqu'à moitié. Ce n'est pas un "
              "argument contre les régimes végétaux : c'est la petite ligne qu'il faut "
              "connaître pour bien les mener."},

    "Esta es la lámina que no existe en ningún otro sitio, y la razón por la que valía la "
    "pena imprimir las dos columnas. Si se divide el techo entre el valor recomendado se "
    "obtiene una cifra que dice cuántas veces la recomendación puede tomarse antes de entrar "
    "en la zona sin margen conocido. Ordenados por esa cifra, los nutrientes se separan de "
    "una manera que sorprende.": {
        "en": "This is the plate that exists nowhere else, and the reason it was worth "
              "printing both columns. Dividing the ceiling by the recommended value gives a "
              "figure that says how many times over the recommendation can be taken before "
              "entering the zone with no known margin. Sorted by that figure, the nutrients "
              "separate in a way that comes as a surprise.",
        "fr": "Voici la planche qui n'existe nulle part ailleurs, et la raison pour laquelle "
              "il valait la peine d'imprimer les deux colonnes. En divisant le plafond par la "
              "valeur recommandée on obtient un chiffre qui dit combien de fois la "
              "recommandation peut être prise avant d'entrer dans la zone sans marge connue. "
              "Classés selon ce chiffre, les nutriments se séparent d'une manière qui "
              "surprend."},

    '<span class="fig-n">Los nutrientes ordenados por lo estrecho que es su margen</span> El '
    "cociente entre el techo y el valor recomendado, en escala logarítmica. Cuanto más corta "
    "la barra, menos espacio hay entre lo que se recomienda y lo que conviene no pasar. Las "
    "barras marcadas en rojo son las de margen inferior a seis veces: ahí una suplementación "
    "a ciegas puede acercarse al techo sin que nadie se dé cuenta.": {
        "en": '<span class="fig-n">The nutrients ranked by how narrow their margin is</span> '
              "The ratio of the ceiling to the recommended value, on a logarithmic scale. The "
              "shorter the bar, the less room there is between what is recommended and what "
              "is best not exceeded. The bars marked in red are those with a margin below six "
              "times: there, blind supplementing can approach the ceiling without anyone "
              "noticing.",
        "fr": '<span class="fig-n">Les nutriments classés selon l\'étroitesse de leur '
              "marge</span> Le rapport entre le plafond et la valeur recommandée, en échelle "
              "logarithmique. Plus la barre est courte, moins il y a d'espace entre ce qui "
              "est recommandé et ce qu'il vaut mieux ne pas dépasser. Les barres marquées en "
              "rouge sont celles dont la marge est inférieure à six fois : là, une "
              "complémentation à l'aveugle peut approcher le plafond sans que personne s'en "
              "aperçoive."},

    "Los de margen estrecho, uno por uno": {
        "en": "The narrow-margin ones, one by one",
        "fr": "Ceux à marge étroite, un par un"},
}
