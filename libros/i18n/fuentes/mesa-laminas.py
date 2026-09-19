# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · rótulos de las láminas — inglés y francés
=============================================================
Los nombres de nutriente y las unidades —µg RAE, mg NE, µg DFE— son
nomenclatura de las tablas oficiales y se escriben igual en los tres idiomas.
Traducir «mg NE» sería inventar una unidad que no existe en ningún documento.

Las siglas de las dos columnas se dejan también como están: RDA y UL son como
las nombran las Dietary Reference Intakes, y el libro enseña precisamente a
buscarlas ahí.
"""

T = {
    "Códice de la Mesa | VILLUMINATIONS": {
        "en": "Codex of the Table | VILLUMINATIONS",
        "fr": "Codex de la Table | VILLUMINATIONS"},

    # ── Lámina: los rangos de macronutrientes ──────────────────────────────
    "Hidratos de carbono": {"en": "Carbohydrate", "fr": "Glucides"},
    "Mínimo absoluto de 130 g al día, que es lo que consume el…": {
        "en": "Absolute minimum of 130 g a day, which is what the…",
        "fr": "Minimum absolu de 130 g par jour, ce que consomme…"},
    "Grasas": {"en": "Fat", "fr": "Lipides"},
    "Por debajo del 20 % cuesta cubrir las grasas esenciales y…": {
        "en": "Below 20 % it is hard to cover the essential fats and…",
        "fr": "Sous 20 %, difficile de couvrir les lipides essentiels…"},
    "Proteínas": {"en": "Protein", "fr": "Protéines"},
    "El RDA es 0,8 g por kilo de peso, que para la mayoría cae…": {
        "en": "The RDA is 0.8 g per kilo of body weight, which for…",
        "fr": "L'AJR est de 0,8 g par kilo de poids, ce qui pour la…"},
    "LOS TRES RANGOS ADMITEN EL 100 % EN ALGÚN PUNTO": {
        "en": "ALL THREE RANGES ALLOW 100 % AT SOME POINT",
        "fr": "LES TROIS PLAGES ADMETTENT 100 % QUELQUE PART"},
    "RANGOS DE DISTRIBUCIÓN · DIETARY REFERENCE INTAKES": {
        "en": "DISTRIBUTION RANGES · DIETARY REFERENCE INTAKES",
        "fr": "PLAGES DE RÉPARTITION · DIETARY REFERENCE INTAKES"},

    # ── Lámina: los componentes del gasto ──────────────────────────────────
    "METABOLISMO BASAL": {"en": "BASAL METABOLISM", "fr": "MÉTABOLISME DE BASE"},
    "Lo que cuesta estar vivo en reposo. La mayor parte del día y…": {
        "en": "What it costs to be alive at rest. Most of the day and…",
        "fr": "Ce que coûte le fait d'être en vie au repos. L'essentiel…"},
    "ACTIVIDAD NO DEPORTIVA": {
        "en": "NON-EXERCISE ACTIVITY", "fr": "ACTIVITÉ NON SPORTIVE"},
    "Andar, estar de pie, gesticular, tareas. Es el componente MÁS…": {
        "en": "Walking, standing, gesturing, chores. It is the MOST…",
        "fr": "Marcher, être debout, gesticuler, tâches. Le composant…"},
    "EFECTO TÉRMICO DE LOS ALIMENTOS": {
        "en": "THERMIC EFFECT OF FOOD", "fr": "EFFET THERMIQUE DES ALIMENTS"},
    "Lo que cuesta digerir y asimilar. La proteína es la que más…": {
        "en": "What digesting and absorbing costs. Protein is the one…",
        "fr": "Ce que coûtent la digestion et l'assimilation. La…"},
    "EJERCICIO ESTRUCTURADO": {
        "en": "STRUCTURED EXERCISE", "fr": "EXERCICE STRUCTURÉ"},
    "La parte que todo el mundo cuenta y que en la mayoría de la…": {
        "en": "The part everybody counts and that in most people is…",
        "fr": "La part que tout le monde compte et qui, chez la…"},
    "LA PORCIÓN QUE TODOS CUENTAN ES LA MÁS PEQUEÑA": {
        "en": "THE PORTION EVERYONE COUNTS IS THE SMALLEST",
        "fr": "LA PART QUE TOUS COMPTENT EST LA PLUS PETITE"},
    "COMPONENTES DEL GASTO DIARIO · RANGOS TÍPICOS": {
        "en": "COMPONENTS OF DAILY EXPENDITURE · TYPICAL RANGES",
        "fr": "COMPOSANTS DE LA DÉPENSE QUOTIDIENNE · PLAGES TYPES"},

    # ── Lámina: los diecinueve micronutrientes ─────────────────────────────
    "UNIDAD": {"en": "UNIT", "fr": "UNITÉ"},
    "HOMBRE": {"en": "MEN", "fr": "HOMME"},
    "MUJER": {"en": "WOMEN", "fr": "FEMME"},
    "TECHO · UL": {"en": "CEILING · UL", "fr": "PLAFOND · UL"},
    "Vitamina A": {"en": "Vitamin A", "fr": "Vitamine A"},
    "µg RAE": {"en": "µg RAE", "fr": "µg RAE"},
    "Vitamina C": {"en": "Vitamin C", "fr": "Vitamine C"},
    "mg": {"en": "mg", "fr": "mg"},
    "Vitamina D": {"en": "Vitamin D", "fr": "Vitamine D"},
    "Vitamina E": {"en": "Vitamin E", "fr": "Vitamine E"},
    "Vitamina K": {"en": "Vitamin K", "fr": "Vitamine K"},
    "sin techo": {"en": "no ceiling", "fr": "sans plafond"},
    "Tiamina · B1": {"en": "Thiamin · B1", "fr": "Thiamine · B1"},
    "Riboflavina · B2": {"en": "Riboflavin · B2", "fr": "Riboflavine · B2"},
    "Niacina · B3": {"en": "Niacin · B3", "fr": "Niacine · B3"},
    "mg NE": {"en": "mg NE", "fr": "mg NE"},
    "Vitamina B6": {"en": "Vitamin B6", "fr": "Vitamine B6"},
    "Folato": {"en": "Folate", "fr": "Folate"},
    "µg DFE": {"en": "µg DFE", "fr": "µg DFE"},
    "Vitamina B12": {"en": "Vitamin B12", "fr": "Vitamine B12"},
    "Calcio": {"en": "Calcium", "fr": "Calcium"},
    "Magnesio": {"en": "Magnesium", "fr": "Magnésium"},
    "Zinc": {"en": "Zinc", "fr": "Zinc"},
    "Selenio": {"en": "Selenium", "fr": "Sélénium"},
    "Yodo": {"en": "Iodine", "fr": "Iode"},
    "Potasio": {"en": "Potassium", "fr": "Potassium"},
    "Sodio": {"en": "Sodium", "fr": "Sodium"},
    "RDA A LA IZQUIERDA · LÍMITE TOLERABLE A LA DERECHA · BARRA = MARGEN": {
        "en": "RDA ON THE LEFT · TOLERABLE LIMIT ON THE RIGHT · BAR = MARGIN",
        "fr": "AJR À GAUCHE · LIMITE TOLÉRABLE À DROITE · BARRE = MARGE"},
    "EN ROJO, MARGEN MENOR DE SEIS VECES": {
        "en": "IN RED, A MARGIN OF LESS THAN SIX TIMES",
        "fr": "EN ROUGE, UNE MARGE INFÉRIEURE À SIX FOIS"},
    "ESCALA LOGARÍTMICA · TECHO DIVIDIDO POR NECESIDAD": {
        "en": "LOGARITHMIC SCALE · CEILING DIVIDED BY REQUIREMENT",
        "fr": "ÉCHELLE LOGARITHMIQUE · PLAFOND DIVISÉ PAR BESOIN"},

    # ── Lámina: el plato y la mano ─────────────────────────────────────────
    "EL PLATO": {"en": "THE PLATE", "fr": "L'ASSIETTE"},
    "Verdura y fruta": {"en": "Vegetables and fruit", "fr": "Légumes et fruits"},
    "Proteína": {"en": "Protein", "fr": "Protéines"},
    "Cereal o tubérculo": {"en": "Grain or tuber", "fr": "Céréale ou tubercule"},
    "Palma sin dedos": {"en": "Palm, without fingers", "fr": "Paume, sans les doigts"},
    "Proteína · una ración": {
        "en": "Protein · one portion", "fr": "Protéines · une portion"},
    "Puño cerrado": {"en": "Closed fist", "fr": "Poing fermé"},
    "Verdura · una o dos": {
        "en": "Vegetables · one or two", "fr": "Légumes · une ou deux"},
    "Mano en cuenco": {"en": "Cupped hand", "fr": "Main en coupe"},
    "Cereal · una ración": {"en": "Grain · one portion", "fr": "Céréale · une portion"},
    "Pulgar entero": {"en": "Whole thumb", "fr": "Pouce entier"},
    "Grasa · una ración": {"en": "Fat · one portion", "fr": "Lipides · une portion"},
    "LA MANO ESCALA CON EL CUERPO": {
        "en": "THE HAND SCALES WITH THE BODY",
        "fr": "LA MAIN S'ADAPTE AU CORPS"},
    "SIN BÁSCULA · SIN CONTAR · SIN APLICACIÓN": {
        "en": "NO SCALES · NO COUNTING · NO APP",
        "fr": "SANS BALANCE · SANS COMPTER · SANS APPLI"},

    # ── Lámina: la etiqueta ────────────────────────────────────────────────
    "INFORMACIÓN NUTRICIONAL": {
        "en": "NUTRITION INFORMATION", "fr": "INFORMATION NUTRITIONNELLE"},
    "Por 100 g": {"en": "Per 100 g", "fr": "Pour 100 g"},
    "SIEMPRE COMPARABLE": {"en": "ALWAYS COMPARABLE", "fr": "TOUJOURS COMPARABLE"},
    "Por porción": {"en": "Per serving", "fr": "Par portion"},
    "LA PORCIÓN LA ELIGE LA MARCA": {
        "en": "THE BRAND CHOOSES THE SERVING",
        "fr": "LA MARQUE CHOISIT LA PORTION"},
    "Energía": {"en": "Energy", "fr": "Énergie"},
    "Grasas · de las cuales saturadas": {
        "en": "Fat · of which saturates", "fr": "Lipides · dont saturés"},
    "Hidratos · de los cuales azúcares": {
        "en": "Carbohydrate · of which sugars", "fr": "Glucides · dont sucres"},
    "Fibra": {"en": "Fibre", "fr": "Fibres"},
    "Sal": {"en": "Salt", "fr": "Sel"},
    "LO QUE DICE LA NORMA": {
        "en": "WHAT THE REGULATION SAYS", "fr": "CE QUE DIT LA NORME"},
    "A LIMITAR": {"en": "TO LIMIT", "fr": "À LIMITER"},
    "Calorías, azúcares, grasas, sodio: como": {
        "en": "Calories, sugars, fat, sodium: at", "fr": "Calories, sucres, lipides,"},
    "mucho una quinta parte POR ENCIMA de lo": {
        "en": "most one fifth ABOVE the declared", "fr": "sodium : au plus un cinquième"},
    "declarado": {"en": "figure", "fr": "AU-DESSUS du déclaré"},
    "A ALCANZAR": {"en": "TO REACH", "fr": "À ATTEINDRE"},
    "Vitaminas, minerales, proteína y fibra: al": {
        "en": "Vitamins, minerals, protein and fibre:",
        "fr": "Vitamines, minéraux, protéines et"},
    "menos cuatro quintos de lo declarado": {
        "en": "at least four fifths of the declared figure",
        "fr": "fibres : au moins quatre cinquièmes"},
    "EL VALOR DECLARADO ES UNA FRANJA": {
        "en": "THE DECLARED VALUE IS A BAND",
        "fr": "LA VALEUR DÉCLARÉE EST UNE FOURCHETTE"},
    "TOLERANCIAS PÚBLICAS DEL ETIQUETADO": {
        "en": "PUBLISHED LABELLING TOLERANCES",
        "fr": "TOLÉRANCES PUBLIQUES DE L'ÉTIQUETAGE"},

    # ── Lámina: la inocuidad ───────────────────────────────────────────────
    "ZONA DE": {"en": "DANGER", "fr": "ZONE"},
    "PELIGRO": {"en": "ZONE", "fr": "DE DANGER"},
    "Congelador · -18 °C": {"en": "Freezer · -18 °C", "fr": "Congélateur · -18 °C"},
    "Nevera · 4 °C o menos": {
        "en": "Fridge · 4 °C or below", "fr": "Frigo · 4 °C ou moins"},
    "Aves, entera o en piezas": {
        "en": "Poultry, whole or in pieces", "fr": "Volaille, entière ou découpée"},
    "Sin excepción y sin reposo": {
        "en": "No exceptions and no resting time",
        "fr": "Sans exception et sans repos"},
    "Sobras y guisos recalentados": {
        "en": "Leftovers and reheated stews", "fr": "Restes et plats réchauffés"},
    "Hasta que humee, no solo templado": {
        "en": "Until steaming, not merely warm",
        "fr": "Jusqu'à fumer, pas seulement tiède"},
    "Carne picada de res, cerdo…": {
        "en": "Minced beef, pork…", "fr": "Viande hachée de bœuf, porc…"},
    "Más alta que la del corte entero: al…": {
        "en": "Higher than for a whole cut: the…",
        "fr": "Plus haute que pour une pièce…"},
    "Platos con huevo": {"en": "Egg dishes", "fr": "Plats à base d'œuf"},
    "Tortillas cuajadas, quiches, flanes": {
        "en": "Set omelettes, quiches, custards",
        "fr": "Omelettes prises, quiches, flans"},
    "Cortes enteros de res, cerdo…": {
        "en": "Whole cuts of beef, pork…", "fr": "Pièces entières de bœuf, porc…"},
}
