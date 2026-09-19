# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · la lista de la compra y las trampas de la etiqueta
=====================================================================
Las palabras que no significan nada son un problema de traducción de los
buenos: «light» es idéntica en las tres lenguas porque el envase la escribe en
inglés en todas partes, mientras que «sin azúcares añadidos» tiene fórmula
legal propia en cada idioma y hay que usar la que aparece impresa —«no added
sugars», «sans sucres ajoutés»— o el lector no la reconocerá en el súper.
"""

T = {
    "Con dos raciones de proteína, dos o tres de verdura, dos de cereal y dos de grasa al día "
    "se cubre un patrón razonable para mucha gente. Quien entrena fuerte sube proteína y "
    "cereal; quien está en déficit baja cereal y grasa antes que proteína y verdura. No es "
    "exacto y no pretende serlo: pretende sobrevivir al mes tres, que es donde mueren los "
    "sistemas exactos.": {
        "en": "Two protein portions, two or three of vegetables, two of cereal and two of fat "
              "a day cover a reasonable pattern for a lot of people. Anyone training hard "
              "raises protein and cereal; anyone in a deficit lowers cereal and fat before "
              "protein and vegetables. It is not exact and does not claim to be: it claims to "
              "survive month three, which is where exact systems die.",
        "fr": "Deux portions de protéines, deux ou trois de légumes, deux de céréales et deux "
              "de matières grasses par jour couvrent un schéma raisonnable pour beaucoup de "
              "gens. Qui s'entraîne dur augmente protéines et céréales ; qui est en déficit "
              "baisse céréales et graisses avant protéines et légumes. Ce n'est pas exact et "
              "cela ne prétend pas l'être : cela prétend survivre au troisième mois, là où "
              "meurent les systèmes exacts."},

    "La lista de la compra que sale de este libro": {
        "en": "The shopping list this book produces",
        "fr": "La liste de courses qui sort de ce livre"},

    "No es una lista de superalimentos. Es la lista de las categorías que cubren los huecos "
    "que la tabla suele mostrar, ordenada por lo que resuelve cada una:": {
        "en": "It is not a list of superfoods. It is the list of the categories that fill the "
              "gaps the table tends to show, ordered by what each one solves:",
        "fr": "Ce n'est pas une liste de super-aliments. C'est la liste des catégories qui "
              "comblent les manques que le tableau met généralement en évidence, classées "
              "selon ce que chacune résout :"},

    "Verdura de hoja verde: folato, vitamina K, potasio, magnesio, fibra. La categoría que más "
    "casillas tacha por unidad de esfuerzo.": {
        "en": "Green leafy vegetables: folate, vitamin K, potassium, magnesium, fibre. The "
              "category that ticks the most boxes per unit of effort.",
        "fr": "Légumes à feuilles vertes : folates, vitamine K, potassium, magnésium, fibres. "
              "La catégorie qui coche le plus de cases par unité d'effort."},

    "Legumbre: proteína, fibra, hierro no hemo, potasio, folato. Con vitamina C en la misma "
    "comida —un tomate, un pimiento, un cítrico— la absorción del hierro mejora de forma "
    "apreciable.": {
        "en": "Pulses: protein, fibre, non-haem iron, potassium, folate. With vitamin C in the "
              "same meal —a tomato, a pepper, a citrus fruit— iron absorption improves "
              "appreciably.",
        "fr": "Légumineuses : protéines, fibres, fer non héminique, potassium, folates. Avec "
              "de la vitamine C au même repas —une tomate, un poivron, un agrume— "
              "l'absorption du fer s'améliore de façon appréciable."},

    "Pescado azul: los ácidos grasos de cadena larga, vitamina D y yodo. Dos veces por semana "
    "es el consejo estándar de las guías.": {
        "en": "Oily fish: the long-chain fatty acids, vitamin D and iodine. Twice a week is "
              "the standard advice in the guidelines.",
        "fr": "Poisson gras : les acides gras à longue chaîne, la vitamine D et l'iode. Deux "
              "fois par semaine est le conseil standard des guides."},

    "Huevo: proteína completa, colina, vitaminas del grupo B, y liposolubles en la yema. "
    "Rehabilitado hace años en las guías; la restricción sistemática que se recomendaba antaño "
    "ya no figura.": {
        "en": "Egg: complete protein, choline, B vitamins, and fat-soluble vitamins in the "
              "yolk. Rehabilitated in the guidelines years ago; the blanket restriction once "
              "recommended no longer appears.",
        "fr": "Œuf : protéine complète, choline, vitamines du groupe B et liposolubles dans le "
              "jaune. Réhabilité depuis des années dans les guides ; la restriction "
              "systématique que l'on recommandait autrefois n'y figure plus."},

    "Frutos secos y semillas: grasas esenciales, magnesio, vitamina E, fibra. Aquí es donde "
    "vive la nuez de Brasil, así que una o dos y no un puñado.": {
        "en": "Nuts and seeds: essential fats, magnesium, vitamin E, fibre. This is where the "
              "Brazil nut lives, so one or two and not a handful.",
        "fr": "Fruits à coque et graines : graisses essentielles, magnésium, vitamine E, "
              "fibres. C'est ici que vit la noix du Brésil, donc une ou deux et pas une "
              "poignée."},

    "Lácteo o su equivalente fortificado: calcio, proteína, vitamina B12 y a menudo vitamina "
    "D. Si se sustituye por bebida vegetal, comprobar que esté fortificada, porque la mayoría "
    "de las no fortificadas no aportan nada de esto.": {
        "en": "Dairy or its fortified equivalent: calcium, protein, vitamin B12 and often "
              "vitamin D. If you replace it with a plant drink, check that it is fortified, "
              "because most unfortified ones supply none of this.",
        "fr": "Produit laitier ou son équivalent enrichi : calcium, protéines, vitamine B12 et "
              "souvent vitamine D. Si on le remplace par une boisson végétale, vérifier "
              "qu'elle est enrichie, car la plupart de celles qui ne le sont pas n'apportent "
              "rien de tout cela."},

    "Sal yodada: es la vía por la que la población cubre el yodo. Sin ella y sin pescado ni "
    "lácteos, quedarse corto es fácil.": {
        "en": "Iodised salt: it is the route by which the population covers iodine. Without it "
              "and without fish or dairy, falling short is easy.",
        "fr": "Sel iodé : c'est la voie par laquelle la population couvre l'iode. Sans lui et "
              "sans poisson ni produits laitiers, il est facile d'être en dessous."},

    "Y una categoría más, para quien no come productos animales": {
        "en": "And one more category, for anyone who eats no animal products",
        "fr": "Et une catégorie de plus, pour qui ne mange pas de produits animaux"},

    "La vitamina B12 no está en los vegetales en forma aprovechable. No es una cuestión de "
    "planificar mejor: es un suplemento o un alimento fortificado, y no es opinable. El resto "
    "de una dieta vegetal bien llevada resiste cualquier análisis; este punto concreto no "
    "admite improvisación, y la carencia sostenida hace daño neurológico que no siempre se "
    "recupera.": {
        "en": "Vitamin B12 is not present in plants in a usable form. It is not a question of "
              "planning better: it is a supplement or a fortified food, and it is not a matter "
              "of opinion. The rest of a well-run plant-based diet withstands any scrutiny; "
              "this particular point allows no improvisation, and sustained deficiency does "
              "neurological damage that is not always recovered.",
        "fr": "La vitamine B12 n'est pas présente dans les végétaux sous une forme "
              "utilisable. Ce n'est pas une question de mieux planifier : c'est un complément "
              "ou un aliment enrichi, et cela ne se discute pas. Le reste d'un régime végétal "
              "bien mené résiste à n'importe quel examen ; ce point précis n'admet aucune "
              "improvisation, et la carence prolongée fait des dégâts neurologiques qui ne se "
              "récupèrent pas toujours."},

    # ── Capítulo de la etiqueta ────────────────────────────────────────────
    "La etiqueta de un envase es el único documento nutricional que la mayoría de la gente "
    "tiene delante todos los días, y casi nadie sabe leerlo. Tiene cuatro trampas conocidas y "
    "una franja de tolerancia legal que muy poca gente sospecha.": {
        "en": "The label on a packet is the only nutritional document most people have in "
              "front of them every day, and almost nobody knows how to read it. It has four "
              "known traps and a band of legal tolerance very few people suspect.",
        "fr": "L'étiquette d'un emballage est le seul document nutritionnel que la plupart des "
              "gens ont sous les yeux tous les jours, et presque personne ne sait le lire. "
              "Elle comporte quatre pièges connus et une plage de tolérance légale que très "
              "peu de gens soupçonnent."},

    '<span class="fig-n">Anatomía de una etiqueta y sus tolerancias legales</span> La columna '
    "por cien gramos es la única comparable entre productos. La porción la elige el "
    "fabricante. Y a la derecha, la tolerancia: el valor declarado no es un número, es una "
    "franja.": {
        "en": '<span class="fig-n">Anatomy of a label and its legal tolerances</span> The per '
              "hundred grams column is the only one comparable between products. The serving "
              "is chosen by the manufacturer. And on the right, the tolerance: the declared "
              "value is not a number, it is a band.",
        "fr": '<span class="fig-n">Anatomie d\'une étiquette et ses tolérances légales</span> '
              "La colonne pour cent grammes est la seule comparable d'un produit à l'autre. La "
              "portion, c'est le fabricant qui la choisit. Et à droite, la tolérance : la "
              "valeur déclarée n'est pas un nombre, c'est une plage."},

    "La primera trampa: la porción": {
        "en": "The first trap: the serving", "fr": "Le premier piège : la portion"},

    "La ley obliga a declarar los valores por cien gramos, y eso es lo que hace comparables dos "
    "productos. Junto a esa columna suele aparecer otra «por porción», y la porción la decide "
    "quien vende. Una porción de treinta gramos de un cereal de desayuno es aproximadamente "
    "una cuarta parte de lo que cualquiera se sirve, y todas las cifras de esa columna están "
    "divididas por cuatro respecto a lo que va a pasar de verdad.": {
        "en": "The law requires values to be declared per hundred grams, and that is what "
              "makes two products comparable. Next to that column there is usually another one "
              "«per serving», and the serving is decided by whoever is selling. A thirty-gram "
              "serving of a breakfast cereal is roughly a quarter of what anyone actually "
              "pours, and every figure in that column is divided by four relative to what is "
              "really going to happen.",
        "fr": "La loi oblige à déclarer les valeurs pour cent grammes, et c'est ce qui rend "
              "deux produits comparables. À côté de cette colonne en apparaît d'ordinaire une "
              "autre « par portion », et la portion, c'est le vendeur qui la décide. Une "
              "portion de trente grammes d'une céréale de petit-déjeuner représente environ le "
              "quart de ce que n'importe qui se sert, et tous les chiffres de cette colonne "
              "sont divisés par quatre par rapport à ce qui va réellement se passer."},

    "Regla: comparar siempre por cien gramos, y después mirar cuánto se come de verdad. Nunca "
    "al revés.": {
        "en": "Rule: always compare per hundred grams, and then look at how much is really "
              "eaten. Never the other way round.",
        "fr": "Règle : comparer toujours pour cent grammes, puis regarder combien on mange "
              "réellement. Jamais l'inverse."},

    "La segunda: el orden de los ingredientes": {
        "en": "The second: the order of the ingredients",
        "fr": "Le deuxième : l'ordre des ingrédients"},

    "Los ingredientes van por peso descendente, y eso convierte a la lista en una radiografía "
    "bastante honesta. Si el azúcar aparece en los tres primeros puestos, el producto es "
    "principalmente azúcar por mucho que la portada hable de fibra. La contramedida de la "
    "industria es dividir el azúcar en varios nombres —jarabe, dextrosa, concentrado de zumo, "
    "melaza— para que cada uno pese menos y baje puestos. Sumarlos mentalmente devuelve la "
    "imagen real.": {
        "en": "Ingredients are listed by descending weight, and that turns the list into a "
              "fairly honest X-ray. If sugar appears in the first three places, the product is "
              "mainly sugar however much the front of the pack talks about fibre. The "
              "industry's countermeasure is to split the sugar across several names —syrup, "
              "dextrose, juice concentrate, molasses— so that each weighs less and drops down "
              "the order. Adding them up in your head restores the real picture.",
        "fr": "Les ingrédients sont classés par poids décroissant, et cela fait de la liste une "
              "radiographie assez honnête. Si le sucre apparaît dans les trois premières "
              "places, le produit est principalement du sucre, quoi que la face avant raconte "
              "sur les fibres. La contre-mesure de l'industrie consiste à répartir le sucre "
              "entre plusieurs noms —sirop, dextrose, concentré de jus, mélasse— pour que "
              "chacun pèse moins et recule dans la liste. Les additionner mentalement rétablit "
              "l'image réelle."},

    "La tercera: las palabras que no significan nada": {
        "en": "The third: the words that mean nothing",
        "fr": "Le troisième : les mots qui ne veulent rien dire"},

    "«Natural» no tiene una definición reglada que sirva para juzgar nada.": {
        "en": "«Natural» has no regulated definition that serves to judge anything.",
        "fr": "« Naturel » n'a pas de définition réglementée qui permette de juger quoi que ce "
              "soit."},

    "«Artesano», «casero», «de siempre», «receta tradicional» son estilo, no composición.": {
        "en": "«Artisan», «home-made», «the way it used to be», «traditional recipe» are "
              "style, not composition.",
        "fr": "« Artisanal », « fait maison », « comme avant », « recette traditionnelle » "
              "relèvent du style, pas de la composition."},

    "«Sin azúcares añadidos» no equivale a poco azúcar: un zumo cumple y lleva tanto azúcar "
    "como un refresco.": {
        "en": "«No added sugars» does not amount to little sugar: a fruit juice qualifies and "
              "carries as much sugar as a soft drink.",
        "fr": "« Sans sucres ajoutés » n'équivaut pas à peu de sucre : un jus de fruits "
              "satisfait au critère et contient autant de sucre qu'un soda."},

    "«Light» solo obliga a una reducción respecto al producto de referencia, que puede seguir "
    "siendo altísimo en términos absolutos.": {
        "en": "«Light» only requires a reduction relative to the reference product, which may "
              "still be extremely high in absolute terms.",
        "fr": "« Light » n'impose qu'une réduction par rapport au produit de référence, lequel "
              "peut rester très élevé en valeur absolue."},

    "«Enriquecido con vitaminas» suele señalar un producto que necesitaba una razón para estar "
    "en el carro.": {
        "en": "«Enriched with vitamins» usually marks a product that needed a reason to be in "
              "the trolley.",
        "fr": "« Enrichi en vitamines » signale d'ordinaire un produit qui avait besoin d'une "
              "raison de se trouver dans le caddie."},

    "La cuarta, y la que nadie cuenta: la tolerancia": {
        "en": "The fourth, and the one nobody mentions: the tolerance",
        "fr": "Le quatrième, celui dont personne ne parle : la tolérance"},
}
