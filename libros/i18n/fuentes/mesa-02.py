# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · capítulos 1 (cierre) y 2
============================================
Las cuatro siglas —EAR, RDA, AI, UL— no se traducen en ninguno de los tres
idiomas: son como las nombran las Dietary Reference Intakes y el capítulo
entero enseña a reconocerlas en el documento original. Traducirlas por siglas
locales las volvería imposibles de buscar, que es justo lo contrario de lo que
el libro quiere.

La advertencia sobre interacciones con medicación se traduce literal. El
propio texto dice que es el consejo más útil del libro, y lo es en los tres
idiomas.
"""

T = {
    # ── Lámina de inocuidad, cierre ────────────────────────────────────────
    "Más tres minutos de reposo": {
        "en": "Plus three minutes' resting time", "fr": "Plus trois minutes de repos"},
    "Pescado y marisco": {"en": "Fish and shellfish", "fr": "Poissons et fruits de mer"},
    "O hasta que la carne se separe en…": {
        "en": "Or until the flesh flakes apart…", "fr": "Ou jusqu'à ce que la chair se…"},
    "FUERA DE LA NEVERA: 2 HORAS · CON MÁS DE 32 °C, 1": {
        "en": "OUT OF THE FRIDGE: 2 HOURS · ABOVE 32 °C, 1",
        "fr": "HORS DU FRIGO : 2 HEURES · AU-DESSUS DE 32 °C, 1"},
    "TEMPERATURAS INTERNAS · SE MIDEN CON TERMÓMETRO, NO POR COLOR": {
        "en": "INTERNAL TEMPERATURES · MEASURED WITH A THERMOMETER, NOT BY COLOUR",
        "fr": "TEMPÉRATURES À CŒUR · SE MESURENT AU THERMOMÈTRE, PAS À LA COULEUR"},

    # ── Capítulo 1 · lo que el libro no afirma ─────────────────────────────
    "No es una prescripción individual. Los valores de referencia son poblacionales: "
    "describen lo que cubre las necesidades de casi todos los adultos sanos, no las tuyas.": {
        "en": "It is not an individual prescription. Reference values are population "
              "values: they describe what covers the needs of almost all healthy adults, "
              "not yours.",
        "fr": "Ce n'est pas une prescription individuelle. Les valeurs de référence sont "
              "des valeurs de population : elles décrivent ce qui couvre les besoins de "
              "presque tous les adultes en bonne santé, pas les vôtres."},

    "No considera patologías, embarazo, lactancia, infancia, vejez avanzada ni medicación. "
    "Cualquiera de esas cuatro palabras cambia las cifras, y en algunos casos las "
    "invierte.": {
        "en": "It does not account for medical conditions, pregnancy, breastfeeding, "
              "childhood, advanced age or medication. Any of those words changes the "
              "figures, and in some cases reverses them.",
        "fr": "Il ne tient compte ni des pathologies, ni de la grossesse, ni de "
              "l'allaitement, ni de l'enfance, ni du grand âge, ni des traitements. "
              "N'importe lequel de ces mots change les chiffres, et dans certains cas les "
              "inverse."},

    "No sustituye a un profesional sanitario. Un análisis de sangre y una consulta valen "
    "más que este libro entero, y este libro está escrito para que llegues a esa consulta "
    "sabiendo qué preguntar.": {
        "en": "It does not replace a health professional. A blood test and an appointment "
              "are worth more than this entire book, and this book is written so that you "
              "arrive at that appointment knowing what to ask.",
        "fr": "Il ne remplace pas un professionnel de santé. Une prise de sang et une "
              "consultation valent plus que ce livre entier, et ce livre est écrit pour que "
              "vous arriviez à cette consultation en sachant quoi demander."},

    "No promete resultados de composición corporal. Ninguna cifra de aquí adelgaza a "
    "nadie; lo que hacen es evitar que te falte algo mientras haces lo que sí funciona.": {
        "en": "It promises no body composition results. No figure in here makes anyone "
              "leaner; what they do is stop you going short of something while you do what "
              "actually works.",
        "fr": "Il ne promet aucun résultat de composition corporelle. Aucun chiffre d'ici "
              "ne fait maigrir personne ; ce qu'ils font, c'est éviter que quelque chose "
              "vous manque pendant que vous faites ce qui, lui, fonctionne."},

    "Advertencia que viaja con los datos": {
        "en": "A warning that travels with the data",
        "fr": "Un avertissement qui voyage avec les données"},

    "Si tomas medicación —anticoagulantes, tiroideos, antihipertensivos, metformina, "
    "litio, entre otros— hay nutrientes de esta tabla que interaccionan con ella de forma "
    "clínicamente relevante. La vitamina K y los anticoagulantes son el caso de manual, "
    "pero no el único. No cambies una ingesta ni empieces un suplemento sin decírselo a "
    "quien te receta. Esto no es una fórmula de cortesía: es el consejo más útil del "
    "libro.": {
        "en": "If you take medication —anticoagulants, thyroid drugs, antihypertensives, "
              "metformin, lithium, among others— there are nutrients in this table that "
              "interact with it in clinically relevant ways. Vitamin K and anticoagulants "
              "are the textbook case, but not the only one. Do not change an intake or "
              "start a supplement without telling whoever prescribes for you. This is not a "
              "polite formula: it is the most useful piece of advice in the book.",
        "fr": "Si vous prenez un traitement —anticoagulants, hormones thyroïdiennes, "
              "antihypertenseurs, metformine, lithium, entre autres— certains nutriments de "
              "ce tableau interagissent avec lui de façon cliniquement significative. La "
              "vitamine K et les anticoagulants sont le cas d'école, mais pas le seul. Ne "
              "modifiez pas un apport et ne commencez pas un complément sans le dire à qui "
              "vous prescrit. Ce n'est pas une formule de politesse : c'est le conseil le "
              "plus utile du livre."},

    "De dónde sale cada cifra": {
        "en": "Where every figure comes from", "fr": "D'où sort chaque chiffre"},

    "De ocho fuentes públicas, todas citadas por su nombre en el último capítulo con "
    "indicación de dónde se consultan. Ninguna cifra de este libro está inventada, "
    "redondeada por comodidad ni copiada de otro libro de divulgación.": {
        "en": "From eight public sources, all named in the final chapter with an indication "
              "of where to consult them. No figure in this book is invented, rounded for "
              "convenience, or copied from another popular-science book.",
        "fr": "De huit sources publiques, toutes nommées dans le dernier chapitre avec "
              "l'indication de l'endroit où les consulter. Aucun chiffre de ce livre n'est "
              "inventé, arrondi par commodité ou recopié d'un autre ouvrage de "
              "vulgarisation."},

    "Y hay algo más, que es lo que convierte a este libro en un sistema y no en un folleto "
    "bien maquetado: las tablas se comprueban solas. El programa que compone estas páginas "
    "ejecuta primero una batería de verificaciones —que los rangos de macronutrientes "
    "admitan el cien por cien, que la fibra cuadre con su regla de catorce gramos por cada "
    "mil kilocalorías, que ningún valor de referencia supere su propio techo sin una nota "
    "que explique por qué— y si alguna falla, se niega a escribir el libro. Una de esas "
    "comprobaciones cazó un error mío mientras escribía esto. Por eso están.": {
        "en": "And there is something else, which is what makes this book a system rather "
              "than a well-laid-out leaflet: the tables check themselves. The programme that "
              "typesets these pages first runs a battery of verifications —that the "
              "macronutrient ranges allow a hundred per cent, that the fibre squares with "
              "its rule of fourteen grams per thousand kilocalories, that no reference value "
              "exceeds its own ceiling without a note explaining why— and if any of them "
              "fails, it refuses to write the book. One of those checks caught a mistake of "
              "mine while I was writing this. That is why they are there.",
        "fr": "Et il y a autre chose, qui fait de ce livre un système et non une brochure "
              "bien maquettée : les tableaux se vérifient tout seuls. Le programme qui "
              "compose ces pages exécute d'abord une batterie de vérifications —que les "
              "plages de macronutriments admettent cent pour cent, que les fibres cadrent "
              "avec leur règle de quatorze grammes pour mille kilocalories, qu'aucune valeur "
              "de référence ne dépasse son propre plafond sans une note expliquant "
              "pourquoi— et si l'une échoue, il refuse d'écrire le livre. L'une de ces "
              "vérifications a attrapé une erreur de ma part pendant que j'écrivais ceci. "
              "C'est pour cela qu'elles existent."},

    "Cómo se lee este libro": {
        "en": "How this book is read", "fr": "Comment lire ce livre"},

    "Se puede leer de principio a fin, y está escrito para eso. Pero también funciona como "
    "manual de consulta: las cuatro siglas del capítulo «Las cuatro letras que nadie "
    "explica» son la llave de todo lo demás; la tabla de los diecinueve es la referencia "
    "que se vuelve a mirar cada vez que aparece un bote nuevo; y el cuaderno del final es "
    "lo único que hay que ejecutar. Si solo vas a leer tres capítulos, que sean esos tres.": {
        "en": "It can be read from beginning to end, and it is written for that. But it "
              "also works as a reference manual: the four acronyms in the chapter “The four "
              "acronyms nobody explains” are the key to everything else; the table of the "
              "nineteen is the reference you come back to every time a new tub appears; and "
              "the notebook at the end is the only thing to actually carry out. If you are "
              "only going to read three chapters, make it those three.",
        "fr": "On peut le lire du début à la fin, et il est écrit pour cela. Mais il "
              "fonctionne aussi comme manuel de consultation : les quatre sigles du "
              "chapitre « Les quatre sigles que personne n'explique » sont la clé de tout "
              "le reste ; le tableau des dix-neuf est la référence que l'on reconsulte "
              "chaque fois qu'un nouveau pot apparaît ; et le carnet de la fin est la seule "
              "chose à exécuter. Si vous ne lisez que trois chapitres, que ce soient "
              "ces trois-là."},

    # ── Capítulo 2 · las cuatro siglas ─────────────────────────────────────
    "Antes de la primera cifra hay que entender cuatro siglas, porque son la diferencia "
    "entre leer una tabla de nutrición y creer que la lees. Las cuatro salen del mismo "
    "marco oficial, y el marco es más interesante que las cifras.": {
        "en": "Before the first figure you have to understand four acronyms, because they "
              "are the difference between reading a nutrition table and believing you are "
              "reading it. All four come from the same official framework, and the "
              "framework is more interesting than the figures.",
        "fr": "Avant le premier chiffre, il faut comprendre quatre sigles, car ils font la "
              "différence entre lire un tableau de nutrition et croire qu'on le lit. Les "
              "quatre viennent du même cadre officiel, et le cadre est plus intéressant que "
              "les chiffres."},

    "El marco de referencia, en cuatro piezas": {
        "en": "The reference framework, in four pieces",
        "fr": "Le cadre de référence, en quatre pièces"},

    "EAR": {"en": "EAR", "fr": "EAR"},
    "Requerimiento medio estimado. La cantidad que cubre la necesidad de la MITAD de la "
    "población. Es la cifra estadística de partida, y no es un objetivo para nadie.": {
        "en": "Estimated Average Requirement. The amount that covers the need of HALF the "
              "population. It is the statistical starting figure, and it is nobody's target.",
        "fr": "Besoin moyen estimé. La quantité qui couvre le besoin de la MOITIÉ de la "
              "population. C'est le chiffre statistique de départ, et ce n'est un objectif "
              "pour personne."},

    "RDA": {"en": "RDA", "fr": "RDA"},
    "Ingesta diaria recomendada. Se calcula sumando al EAR dos desviaciones típicas, de "
    "modo que cubra a cerca del 97 % de la gente. Casi seguro es más de lo que tú "
    "necesitas.": {
        "en": "Recommended Dietary Allowance. It is worked out by adding two standard "
              "deviations to the EAR, so that it covers around 97 % of people. It is almost "
              "certainly more than you need.",
        "fr": "Apport journalier recommandé. Il se calcule en ajoutant deux écarts-types à "
              "l'EAR, de sorte qu'il couvre environ 97 % des gens. C'est presque à coup sûr "
              "plus que ce dont vous avez besoin."},

    "AI": {"en": "AI", "fr": "AI"},
    "Ingesta adecuada. Se usa cuando no hay datos suficientes para calcular un EAR. Es un "
    "valor observado en poblaciones sanas, no un valor derivado: tiene menos fuerza y muy "
    "pocas tablas lo distinguen del RDA.": {
        "en": "Adequate Intake. It is used when there is not enough data to calculate an "
              "EAR. It is a value observed in healthy populations, not a derived value: it "
              "carries less weight, and very few tables distinguish it from the RDA.",
        "fr": "Apport suffisant. On l'emploie quand les données ne suffisent pas à calculer "
              "un EAR. C'est une valeur observée dans des populations en bonne santé, pas "
              "une valeur dérivée : elle a moins de force, et très peu de tableaux la "
              "distinguent du RDA."},

    "UL": {"en": "UL", "fr": "UL"},
    "Límite superior tolerable. El techo por encima del cual el riesgo de efectos adversos "
    "empieza a subir. No es una dosis tóxica: es donde deja de haber margen conocido.": {
        "en": "Tolerable Upper Intake Level. The ceiling above which the risk of adverse "
              "effects starts to rise. It is not a toxic dose: it is where the known margin "
              "runs out.",
        "fr": "Limite supérieure tolérable. Le plafond au-delà duquel le risque d'effets "
              "indésirables commence à monter. Ce n'est pas une dose toxique : c'est là où "
              "s'arrête la marge connue."},

    "La consecuencia que casi nadie saca": {
        "en": "The conclusion almost nobody draws",
        "fr": "La conséquence que presque personne n'en tire"},

    "Si el valor recomendado está puesto para cubrir al noventa y siete por ciento de la "
    "población, entonces la mayoría de la gente está por encima de su necesidad real cuando "
    "lo alcanza. Quedarse un poco por debajo del RDA no significa tener un déficit: "
    "significa que no se puede saber, porque el déficit se define contra la necesidad "
    "individual y esa cifra no aparece en ninguna tabla.": {
        "en": "If the recommended value is set to cover ninety-seven per cent of the "
              "population, then most people are above their real need when they reach it. "
              "Falling a little below the RDA does not mean having a deficiency: it means "
              "you cannot tell, because a deficiency is defined against individual need and "
              "that figure appears in no table.",
        "fr": "Si la valeur recommandée est fixée pour couvrir quatre-vingt-dix-sept pour "
              "cent de la population, alors la plupart des gens sont au-dessus de leur "
              "besoin réel quand ils l'atteignent. Rester un peu sous le RDA ne signifie pas "
              "avoir une carence : cela signifie qu'on ne peut pas le savoir, parce que la "
              "carence se définit par rapport au besoin individuel et que ce chiffre "
              "n'apparaît dans aucun tableau."},
}
