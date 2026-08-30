# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · capítulos 5 (cierre), 6 y arranque del 7
============================================================
El capítulo 6 dice, con todas las letras, que el hidrato de carbono no es
esencial en sentido estricto, y acto seguido explica por qué eso no convierte
en recomendable bajar del mínimo. Las dos mitades del argumento se traducen
con el mismo cuidado: quitarle fuerza a cualquiera de ellas cambiaría lo que
el libro sostiene.
"""

T = {
    # ── Capítulo 5 · cierre ────────────────────────────────────────────────
    "La proteína no se guarda. A diferencia de la grasa y, en pequeña medida, del hidrato, "
    "no hay un depósito de aminoácidos de reserva. Lo que no se usa se oxida o se convierte. "
    "De ahí que repartirla a lo largo del día tenga más sentido que concentrarla, aunque el "
    "total sea igual.": {
        "en": "Protein is not stored. Unlike fat and, to a small extent, carbohydrate, "
              "there is no reserve depot of amino acids. What is not used is oxidised or "
              "converted. Hence spreading it across the day makes more sense than "
              "concentrating it, even when the total is the same.",
        "fr": "Les protéines ne se stockent pas. Contrairement aux lipides et, dans une "
              "faible mesure, aux glucides, il n'existe pas de réserve d'acides aminés. Ce "
              "qui n'est pas utilisé est oxydé ou converti. D'où le fait que les répartir "
              "sur la journée ait plus de sens que de les concentrer, même à total égal."},

    "La calidad se mide por lo que falta. Una fuente proteica se juzga por el aminoácido "
    "esencial en el que es más pobre. Las de origen animal raramente cojean; las vegetales "
    "cojean de forma predecible —los cereales de lisina, las legumbres de metionina— y por "
    "eso combinarlas resuelve el problema sin necesidad de hacerlo en la misma comida.": {
        "en": "Quality is measured by what is missing. A protein source is judged by the "
              "essential amino acid it is poorest in. Animal sources rarely fall short; "
              "plant sources fall short predictably —cereals in lysine, pulses in "
              "methionine— and that is why combining them solves the problem without having "
              "to do it in the same meal.",
        "fr": "La qualité se mesure à ce qui manque. Une source de protéines se juge à "
              "l'acide aminé essentiel dont elle est la plus pauvre. Les sources animales "
              "sont rarement en défaut ; les végétales le sont de façon prévisible —les "
              "céréales en lysine, les légumineuses en méthionine— et c'est pourquoi les "
              "combiner règle le problème sans avoir à le faire au même repas."},

    "El peso que se usa en la fórmula es el peso corporal. En obesidad importante esa "
    "cuenta sobreestima la necesidad, porque el tejido adiposo no demanda aminoácidos como "
    "el músculo. Es una de las situaciones en las que la fórmula general deja de servir y "
    "hay que individualizar con ayuda.": {
        "en": "The weight used in the formula is body weight. In significant obesity that "
              "sum overestimates the need, because adipose tissue does not demand amino "
              "acids the way muscle does. It is one of the situations where the general "
              "formula stops working and you have to individualise with help.",
        "fr": "Le poids utilisé dans la formule est le poids corporel. En cas d'obésité "
              "importante, ce calcul surestime le besoin, car le tissu adipeux ne réclame "
              "pas d'acides aminés comme le muscle. C'est l'une des situations où la formule "
              "générale cesse de servir et où il faut individualiser avec de l'aide."},

    "Lo que legalmente se puede afirmar en Europa": {
        "en": "What may legally be claimed in Europe",
        "fr": "Ce que l'on peut légalement affirmer en Europe"},

    "El registro europeo de declaraciones de propiedades saludables autoriza decir que la "
    "proteína contribuye al mantenimiento y al crecimiento de la masa muscular, y también "
    "al mantenimiento de los huesos. No autoriza decir que un batido concreto construya "
    "músculo por sí mismo, ni que queme grasa. La diferencia entre las dos frases es "
    "exactamente la diferencia entre nutrición y publicidad.": {
        "en": "The European register of health claims authorises saying that protein "
              "contributes to the maintenance and growth of muscle mass, and also to the "
              "maintenance of bone. It does not authorise saying that a particular shake "
              "builds muscle by itself, or that it burns fat. The difference between those "
              "two sentences is exactly the difference between nutrition and advertising.",
        "fr": "Le registre européen des allégations de santé autorise à dire que les "
              "protéines contribuent au maintien et à la croissance de la masse musculaire, "
              "ainsi qu'au maintien des os. Il n'autorise pas à dire qu'une boisson précise "
              "construit du muscle par elle-même, ni qu'elle brûle de la graisse. La "
              "différence entre ces deux phrases est exactement celle qui sépare la "
              "nutrition de la publicité."},

    # ── Capítulo 6 · los hidratos ──────────────────────────────────────────
    "El mínimo de hidratos de carbono es la cifra que mejor ilustra cómo se construye una "
    "recomendación, porque no viene de una teoría sobre la dieta: viene de medir lo que "
    "consume un órgano.": {
        "en": "The carbohydrate minimum is the figure that best illustrates how a "
              "recommendation is built, because it does not come from a theory about diet: "
              "it comes from measuring what one organ consumes.",
        "fr": "Le minimum de glucides est le chiffre qui illustre le mieux comment se "
              "construit une recommandation, car il ne vient pas d'une théorie sur "
              "l'alimentation : il vient de la mesure de ce que consomme un organe."},

    "El mínimo y de dónde sale": {
        "en": "The minimum and where it comes from",
        "fr": "Le minimum et d'où il vient"},
    "130 g al día, para cualquier adulto": {
        "en": "130 g a day, for any adult", "fr": "130 g par jour, pour tout adulte"},
    "del 45 al 65 % de la energía": {
        "en": "45 to 65 % of energy", "fr": "de 45 à 65 % de l'énergie"},
    "Origen de la cifra": {
        "en": "Origin of the figure", "fr": "Origine du chiffre"},
    "El consumo de glucosa del cerebro. Ese órgano gasta del orden de 100 a 140 gramos "
    "diarios y no negocia.": {
        "en": "The brain's glucose consumption. That organ spends of the order of 100 to "
              "140 grams a day and does not negotiate.",
        "fr": "La consommation de glucose du cerveau. Cet organe dépense de l'ordre de 100 "
              "à 140 grammes par jour et ne négocie pas."},
    "Fibra aparte": {"en": "Fibre apart", "fr": "Les fibres à part"},
    "La fibra es hidrato de carbono, pero tiene su propia cifra de referencia y su propio "
    "capítulo.": {
        "en": "Fibre is a carbohydrate, but it has its own reference figure and its own "
              "chapter.",
        "fr": "Les fibres sont des glucides, mais elles ont leur propre chiffre de "
              "référence et leur propre chapitre."},

    "Y aquí la parte que casi nadie cuenta": {
        "en": "And here is the part almost nobody tells you",
        "fr": "Et voici la part que presque personne ne dit"},

    "El propio marco de referencia reconoce que el hidrato de carbono no es un nutriente "
    "esencial en el sentido estricto, porque el cuerpo puede fabricar glucosa a partir de "
    "aminoácidos y del glicerol de las grasas, y porque el cerebro puede cubrir buena parte "
    "de su gasto con cuerpos cetónicos cuando se le entrena a ello. Eso es lo que hace "
    "fisiológicamente posibles las dietas muy bajas en hidratos, y es honesto decirlo en un "
    "libro que da una cifra mínima.": {
        "en": "The reference framework itself acknowledges that carbohydrate is not an "
              "essential nutrient in the strict sense, because the body can manufacture "
              "glucose from amino acids and from the glycerol of fats, and because the "
              "brain can cover a good part of its expenditure with ketone bodies when it is "
              "trained to. That is what makes very low-carbohydrate diets physiologically "
              "possible, and it is honest to say so in a book that gives a minimum figure.",
        "fr": "Le cadre de référence lui-même reconnaît que les glucides ne sont pas un "
              "nutriment essentiel au sens strict, parce que le corps peut fabriquer du "
              "glucose à partir d'acides aminés et du glycérol des lipides, et parce que le "
              "cerveau peut couvrir une bonne part de sa dépense avec des corps cétoniques "
              "quand on l'y habitue. C'est ce qui rend physiologiquement possibles les "
              "régimes très pauvres en glucides, et il est honnête de le dire dans un livre "
              "qui donne un chiffre minimal."},

    "Lo que se dice a continuación es igual de importante: que algo sea posible no lo "
    "convierte en recomendable por defecto, y el mínimo de ciento treinta gramos está "
    "puesto para el adulto medio en condiciones ordinarias, no como veredicto sobre una "
    "estrategia dietética concreta. Quien baja de ahí a propósito está fuera del rango "
    "donde la seguridad está establecida por consenso, y eso no es una condena: es "
    "información que merece conocer antes de decidir, y una razón de peso para hacerlo "
    "acompañado.": {
        "en": "What follows matters just as much: that something is possible does not make "
              "it recommendable by default, and the minimum of a hundred and thirty grams "
              "is set for the average adult in ordinary conditions, not as a verdict on a "
              "particular dietary strategy. Anyone who deliberately goes below it is "
              "outside the range where safety is established by consensus, and that is not "
              "a condemnation: it is information worth having before deciding, and a strong "
              "reason to do it with support.",
        "fr": "Ce qui suit compte tout autant : qu'une chose soit possible ne la rend pas "
              "recommandable par défaut, et le minimum de cent trente grammes est fixé pour "
              "l'adulte moyen en conditions ordinaires, non comme un verdict sur une "
              "stratégie alimentaire précise. Qui descend en dessous délibérément se place "
              "hors de la plage où la sécurité est établie par consensus, et ce n'est pas "
              "une condamnation : c'est une information qui mérite d'être connue avant de "
              "décider, et une bonne raison de le faire accompagné."},

    "Azúcares añadidos: el único límite duro de las guías": {
        "en": "Added sugars: the guidelines' one hard limit",
        "fr": "Sucres ajoutés : la seule limite ferme des recommandations"},

    "Las guías alimentarias oficiales ponen un tope explícito a los azúcares añadidos: "
    "menos del diez por ciento de la energía diaria. En una dieta de 2 000 kilocalorías son "
    "200 kilocalorías, es decir unos cincuenta gramos, que es aproximadamente lo que lleva "
    "una lata y media de refresco.": {
        "en": "The official dietary guidelines set an explicit cap on added sugars: less "
              "than ten per cent of daily energy. In a 2,000 kilocalorie diet that is 200 "
              "kilocalories, that is about fifty grams, which is roughly what a can and a "
              "half of soft drink contains.",
        "fr": "Les recommandations alimentaires officielles posent un plafond explicite aux "
              "sucres ajoutés : moins de dix pour cent de l'énergie quotidienne. Dans un "
              "régime à 2 000 kilocalories, cela fait 200 kilocalories, soit environ "
              "cinquante grammes, à peu près ce que contient une canette et demie de soda."},

    "Conviene notar la palabra «añadidos». El azúcar de una pieza de fruta entera no cuenta "
    "en ese límite, y el de un zumo sí cuenta en la práctica porque se comporta como "
    "añadido aunque la etiqueta no lo llame así. Esa distinción —matriz del alimento frente "
    "a molécula— es la que explica por qué las guías hablan de alimentos y no solo de "
    "nutrientes.": {
        "en": "It is worth noticing the word “added”. The sugar in a whole piece of fruit "
              "does not count towards that limit, and the sugar in a juice does count in "
              "practice, because it behaves like added sugar even though the label does not "
              "call it that. That distinction —the food matrix versus the molecule— is what "
              "explains why the guidelines talk about foods and not only about nutrients.",
        "fr": "Il faut remarquer le mot « ajoutés ». Le sucre d'un fruit entier ne compte "
              "pas dans cette limite, et celui d'un jus y compte en pratique, parce qu'il se "
              "comporte comme un sucre ajouté même si l'étiquette ne le nomme pas ainsi. "
              "Cette distinction —la matrice de l'aliment face à la molécule— explique "
              "pourquoi les recommandations parlent d'aliments et pas seulement de "
              "nutriments."},

    "Índice glucémico: por qué no aparece en las tablas oficiales": {
        "en": "Glycaemic index: why it does not appear in the official tables",
        "fr": "Index glycémique : pourquoi il ne figure pas dans les tables officielles"},

    "El índice glucémico mide la respuesta a un alimento aislado, en ayunas y en cantidad "
    "estandarizada, y esas tres condiciones no se dan casi nunca en una comida real: la "
    "grasa, la proteína, la fibra, el procesado y hasta el orden en que se come alteran la "
    "respuesta. Por eso el marco de referencia no fija objetivos de índice glucémico. Es "
    "útil como concepto y malo como criterio de compra.": {
        "en": "The glycaemic index measures the response to an isolated food, fasted and in "
              "a standardised amount, and those three conditions almost never hold in a "
              "real meal: fat, protein, fibre, processing and even the order in which you "
              "eat all alter the response. That is why the reference framework sets no "
              "glycaemic index targets. It is useful as a concept and poor as a shopping "
              "criterion.",
        "fr": "L'index glycémique mesure la réponse à un aliment isolé, à jeun et en "
              "quantité normalisée, et ces trois conditions ne sont presque jamais réunies "
              "dans un vrai repas : les lipides, les protéines, les fibres, la "
              "transformation et jusqu'à l'ordre dans lequel on mange modifient la réponse. "
              "C'est pourquoi le cadre de référence ne fixe pas d'objectifs d'index "
              "glycémique. C'est utile comme concept et mauvais comme critère d'achat."},

    # ── Capítulo 7 · las grasas ────────────────────────────────────────────
    "El rango de la grasa tiene el suelo más interesante de los tres, porque no está puesto "
    "por la grasa en sí. Está puesto por lo que la grasa transporta.": {
        "en": "The fat range has the most interesting floor of the three, because it is not "
              "set by the fat itself. It is set by what the fat carries.",
        "fr": "La plage des lipides a le plancher le plus intéressant des trois, parce "
              "qu'il n'est pas fixé par les lipides eux-mêmes. Il est fixé par ce que les "
              "lipides transportent."},

    "El rango y sus dos extremos": {
        "en": "The range and its two ends", "fr": "La plage et ses deux extrémités"},
    "del 20 al 35 % de la energía": {
        "en": "20 to 35 % of energy", "fr": "de 20 à 35 % de l'énergie"},
    "Por qué no menos del 20 %": {
        "en": "Why not below 20 %", "fr": "Pourquoi pas moins de 20 %"},
    "Por debajo de ahí cuesta cubrir los ácidos grasos esenciales y las vitaminas "
    "liposolubles, que necesitan grasa en la misma comida para absorberse.": {
        "en": "Below that it is hard to cover the essential fatty acids and the fat-soluble "
              "vitamins, which need fat in the same meal in order to be absorbed.",
        "fr": "En dessous, il devient difficile de couvrir les acides gras essentiels et "
              "les vitamines liposolubles, qui ont besoin de lipides dans le même repas "
              "pour être absorbées."},
    "Grasa saturada": {"en": "Saturated fat", "fr": "Graisses saturées"},
    "Las guías la limitan a menos del 10 % de la energía.": {
        "en": "The guidelines limit it to less than 10 % of energy.",
        "fr": "Les recommandations la limitent à moins de 10 % de l'énergie."},
}
