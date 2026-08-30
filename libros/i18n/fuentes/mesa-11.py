# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · la tolerancia legal y el capítulo del momento
================================================================
Las tolerancias se dicen en fracciones —una quinta parte, cuatro quintos— y no
en porcentajes, en los tres idiomas. Es deliberado: la frase habla de una
franja alrededor del valor declarado, y escribirla como «20 %» invita a leerla
como si fuera otra cifra exacta, que es justo lo contrario de lo que el
capítulo enseña.
"""

T = {
    "Las normas de etiquetado admiten una diferencia entre lo declarado y lo medido, y las "
    "cifras son públicas. Para lo que conviene limitar —calorías, azúcares, grasas, sodio— el "
    "valor medido no debe superar en más de una quinta parte al declarado. Para lo que "
    "conviene alcanzar —vitaminas, minerales, proteína, fibra— el medido debe llegar al menos "
    "a cuatro quintos de lo declarado.": {
        "en": "Labelling rules allow a difference between what is declared and what is "
              "measured, and the figures are public. For what is best limited —calories, "
              "sugars, fats, sodium— the measured value must not exceed the declared one by "
              "more than a fifth. For what is best reached —vitamins, minerals, protein, "
              "fibre— the measured value must come to at least four fifths of what is "
              "declared.",
        "fr": "Les règles d'étiquetage admettent un écart entre ce qui est déclaré et ce qui "
              "est mesuré, et les chiffres sont publics. Pour ce qu'il vaut mieux limiter "
              "—calories, sucres, graisses, sodium— la valeur mesurée ne doit pas dépasser la "
              "valeur déclarée de plus d'un cinquième. Pour ce qu'il vaut mieux atteindre "
              "—vitamines, minéraux, protéines, fibres— la valeur mesurée doit atteindre au "
              "moins quatre cinquièmes de celle qui est déclarée."},

    "Para calorías, azúcares, grasa total, grasa saturada, colesterol y sodio, el valor medido "
    "no debe superar en más de una quinta parte al declarado. Para vitaminas, minerales, "
    "proteína y fibra, el medido debe alcanzar al menos cuatro quintos del declarado. Es "
    "decir: la etiqueta es una franja, no un número.": {
        "en": "For calories, sugars, total fat, saturated fat, cholesterol and sodium, the "
              "measured value must not exceed the declared one by more than a fifth. For "
              "vitamins, minerals, protein and fibre, the measured value must come to at least "
              "four fifths of the declared one. In other words: the label is a band, not a "
              "number.",
        "fr": "Pour les calories, les sucres, les lipides totaux, les acides gras saturés, le "
              "cholestérol et le sodium, la valeur mesurée ne doit pas dépasser la valeur "
              "déclarée de plus d'un cinquième. Pour les vitamines, les minéraux, les "
              "protéines et les fibres, la valeur mesurée doit atteindre au moins quatre "
              "cinquièmes de celle qui est déclarée. Autrement dit : l'étiquette est une "
              "plage, pas un nombre."},

    "De aquí se sigue algo práctico: contar calorías con dos decimales es aritmética de "
    "fantasía. Un día entero de comida envasada puede llevar una desviación apreciable "
    "respecto a lo apuntado sin que nadie haya incumplido nada. Eso no invalida el registro; "
    "invalida la precisión falsa, y aconseja usar tendencias de varias semanas en vez de "
    "cuadrar días sueltos.": {
        "en": "Something practical follows: counting calories to two decimal places is fantasy "
              "arithmetic. A whole day of packaged food can carry an appreciable deviation "
              "from what was written down without anyone having broken any rule. That does not "
              "invalidate keeping a record; it invalidates false precision, and it argues for "
              "using trends over several weeks instead of balancing individual days.",
        "fr": "Il en découle quelque chose de pratique : compter les calories à deux décimales "
              "est de l'arithmétique de fantaisie. Une journée entière d'aliments emballés peut "
              "présenter un écart appréciable par rapport à ce qui a été noté sans que "
              "personne n'ait enfreint quoi que ce soit. Cela n'invalide pas le carnet ; cela "
              "invalide la fausse précision, et cela conseille de raisonner en tendances sur "
              "plusieurs semaines plutôt que d'équilibrer des journées isolées."},

    "La lectura de treinta segundos": {
        "en": "The thirty-second read", "fr": "La lecture de trente secondes"},

    "En la práctica, tres miradas bastan para casi todo: la columna por cien gramos, los tres "
    "primeros ingredientes y la cifra de sal. Con eso se distingue un alimento de un producto "
    "sin haber aprendido nada de bioquímica.": {
        "en": "In practice three glances are enough for almost everything: the per hundred "
              "grams column, the first three ingredients and the salt figure. That is enough "
              "to tell a food from a product without having learnt any biochemistry.",
        "fr": "En pratique, trois coups d'œil suffisent pour presque tout : la colonne pour "
              "cent grammes, les trois premiers ingrédients et le chiffre du sel. Avec cela on "
              "distingue un aliment d'un produit sans avoir appris la moindre biochimie."},

    # ── Capítulo del momento ───────────────────────────────────────────────
    "Es la pregunta que más se hace y la que menos importa, y merece un capítulo precisamente "
    "para ponerla en su sitio. El orden de importancia va de arriba abajo, y la mayoría de la "
    "gente empieza por el último escalón.": {
        "en": "It is the question asked most often and the one that matters least, and it "
              "deserves a chapter precisely in order to put it in its place. The order of "
              "importance runs from top to bottom, and most people start at the last rung.",
        "fr": "C'est la question la plus posée et celle qui compte le moins, et elle mérite un "
              "chapitre précisément pour la remettre à sa place. L'ordre d'importance va du "
              "haut vers le bas, et la plupart des gens commencent par le dernier échelon."},

    "Orden de importancia real": {
        "en": "The real order of importance", "fr": "L'ordre d'importance réel"},

    "1 · El total del día": {"en": "1 · The day's total", "fr": "1 · Le total de la journée"},
    "Energía y proteína totales. Aquí se decide casi todo, y sin esto ordenado el resto no "
    "cambia nada.": {
        "en": "Total energy and protein. Almost everything is decided here, and with this "
              "unsorted the rest changes nothing.",
        "fr": "Énergie et protéines totales. C'est ici que presque tout se décide, et tant que "
              "ce n'est pas en ordre le reste ne change rien."},

    "2 · La calidad del patrón": {
        "en": "2 · The quality of the pattern", "fr": "2 · La qualité du schéma"},
    "Que haya verdura, fruta, legumbre, cereal poco procesado y una fuente proteica decente.": {
        "en": "That there are vegetables, fruit, pulses, lightly processed cereal and a decent "
              "protein source.",
        "fr": "Qu'il y ait des légumes, des fruits, des légumineuses, une céréale peu "
              "transformée et une source de protéines correcte."},

    "3 · El reparto a lo largo del día": {
        "en": "3 · The spread across the day", "fr": "3 · La répartition sur la journée"},
    "Repartir la proteína en tres o cuatro tomas en vez de concentrarla. Efecto modesto y "
    "real.": {
        "en": "Spreading protein over three or four meals instead of concentrating it. A "
              "modest and real effect.",
        "fr": "Répartir les protéines sur trois ou quatre prises au lieu de les concentrer. "
              "Effet modeste et réel."},

    "4 · El momento exacto respecto a la sesión": {
        "en": "4 · The exact timing around the session",
        "fr": "4 · Le moment exact par rapport à la séance"},
    "La famosa ventana. Es el escalón más pequeño de los cuatro.": {
        "en": "The famous window. It is the smallest of the four rungs.",
        "fr": "La fameuse fenêtre. C'est le plus petit des quatre échelons."},

    "Qué pasó con la ventana anabólica": {
        "en": "What happened to the anabolic window",
        "fr": "Ce qu'il est advenu de la fenêtre anabolique"},

    "Durante años se enseñó que había una media hora sagrada después de entrenar en la que "
    "había que meter proteína o se perdía la sesión. Esa urgencia no ha resistido bien el "
    "examen: si se ha comido en las horas previas, el margen es de horas y no de minutos, y el "
    "total del día pesa muchísimo más.": {
        "en": "For years it was taught that there was a sacred half hour after training in "
              "which protein had to go in or the session was lost. That urgency has not stood "
              "up well to scrutiny: if you have eaten in the preceding hours, the margin is "
              "hours and not minutes, and the day's total weighs far more.",
        "fr": "Pendant des années on a enseigné qu'il existait une demi-heure sacrée après "
              "l'entraînement pendant laquelle il fallait faire entrer des protéines sous "
              "peine de perdre la séance. Cette urgence n'a pas bien résisté à l'examen : si "
              "l'on a mangé dans les heures précédentes, la marge est de quelques heures et "
              "non de quelques minutes, et le total de la journée pèse bien davantage."},

    "Donde el momento sí importa es en dos situaciones concretas y acotadas: cuando se entrena "
    "en ayunas y la comida siguiente queda muy lejos, y cuando hay dos sesiones exigentes "
    "separadas por pocas horas, que es situación de deportista y no de la mayoría.": {
        "en": "Where timing does matter is in two specific and bounded situations: when you "
              "train fasted and the next meal is a long way off, and when there are two "
              "demanding sessions a few hours apart, which is an athlete's situation and not "
              "most people's.",
        "fr": "Là où le moment compte vraiment, c'est dans deux situations précises et "
              "délimitées : quand on s'entraîne à jeun et que le repas suivant est très loin, "
              "et quand il y a deux séances exigeantes séparées de quelques heures, ce qui est "
              "une situation de sportif et non celle de la plupart des gens."},

    "Antes de entrenar": {"en": "Before training", "fr": "Avant l'entraînement"},

    "Una comida normal dos o tres horas antes funciona para casi todo el mundo y no requiere "
    "nada especial.": {
        "en": "A normal meal two or three hours beforehand works for almost everyone and "
              "requires nothing special.",
        "fr": "Un repas normal deux ou trois heures avant fonctionne pour presque tout le "
              "monde et n'exige rien de particulier."},

    "Si se entrena poco después de comer, conviene bajar la grasa y la fibra de esa comida: "
    "retrasan el vaciado del estómago y es lo que produce la sensación de piedra.": {
        "en": "If you train shortly after eating, it helps to lower the fat and fibre in that "
              "meal: they delay gastric emptying and that is what produces the feeling of a "
              "stone.",
        "fr": "Si l'on s'entraîne peu après avoir mangé, mieux vaut baisser les graisses et les "
              "fibres de ce repas : elles retardent la vidange de l'estomac et c'est ce qui "
              "produit la sensation de pierre."},

    "Entrenar en ayunas no es peligroso ni mágico. Rinde algo peor en sesiones largas o muy "
    "intensas y da igual en sesiones cortas. Es una preferencia, no una estrategia.": {
        "en": "Training fasted is neither dangerous nor magic. It performs somewhat worse in "
              "long or very intense sessions and makes no difference in short ones. It is a "
              "preference, not a strategy.",
        "fr": "S'entraîner à jeun n'est ni dangereux ni magique. Le rendement est un peu "
              "moindre sur les séances longues ou très intenses et cela ne change rien sur les "
              "séances courtes. C'est une préférence, pas une stratégie."},

    "El café antes de entrenar tiene un efecto sobre el rendimiento bien descrito. Ojo con la "
    "hora: la vida media de la cafeína ronda las cinco horas, así que una sesión de tarde "
    "puede costar sueño esa misma noche.": {
        "en": "Coffee before training has a well-described effect on performance. Mind the "
              "hour: caffeine's half-life is around five hours, so an afternoon session can "
              "cost sleep that same night.",
        "fr": "Le café avant l'entraînement a un effet bien décrit sur la performance. "
              "Attention à l'heure : la demi-vie de la caféine avoisine cinq heures, si bien "
              "qu'une séance de l'après-midi peut coûter du sommeil la nuit même."},

    "Durante": {"en": "During", "fr": "Pendant"},

    "Por debajo de una hora de esfuerzo, agua. A partir de ahí, y sobre todo con calor o en "
    "pruebas largas, tiene sentido aportar hidratos y electrolitos: es exactamente la única "
    "declaración de salud autorizada para las bebidas deportivas, y la palabra que hace todo "
    "el trabajo en esa frase es «prolongado».": {
        "en": "Below an hour of effort, water. Beyond that, and above all in the heat or in "
              "long events, it makes sense to supply carbohydrate and electrolytes: that is "
              "exactly the only authorised health claim for sports drinks, and the word doing "
              "all the work in that sentence is «prolonged».",
        "fr": "En dessous d'une heure d'effort, de l'eau. Au-delà, et surtout par temps chaud "
              "ou lors d'épreuves longues, il est justifié d'apporter des glucides et des "
              "électrolytes : c'est exactement la seule allégation de santé autorisée pour les "
              "boissons pour sportifs, et le mot qui fait tout le travail dans cette phrase "
              "est « prolongé »."},

    "Después": {"en": "After", "fr": "Après"},
}
