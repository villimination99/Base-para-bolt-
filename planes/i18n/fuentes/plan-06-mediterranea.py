# -*- coding: utf-8 -*-
"""
06 · DIETA MEDITERRÁNEA — inglés y francés
==========================================
Criterio para los nombres de plato: se traduce lo que es una instrucción
(«pollo a la plancha», «arroz integral») y se conserva lo que es un nombre
propio culinario reconocido fuera de su país (gazpacho, salmorejo, paella,
pisto, shakshuka, caponata, tabulé, fideuá). Traducir «salmorejo» por «cold
tomato soup» borraría el plato; traducir «pollo a la plancha» por «pollo a la
plancha» dejaría al comprador sin saber qué cocinar.

AOVE se resuelve como «EVOO» en inglés, que es la abreviatura de uso real, y
se escribe entero en francés («huile d'olive vierge extra»), donde no existe
una sigla equivalente y una inventada no se entendería en la cocina.
"""

T = {

    # ── Portada ────────────────────────────────────────────────────────────
    '<small>4 semanas completas</small><span class="glow">DIETA<br>MEDITERRÁNEA</span>': {
        "en": '<small>4 complete weeks</small><span class="glow">MEDITERRANEAN<br>DIET</span>',
        "fr": '<small>4 semaines complètes</small><span class="glow">RÉGIME<br>MÉDITERRANÉEN</span>'},

    "El patrón alimentario más estudiado del mundo, rediseñado con "
    "macros de <em>atleta</em> y 28 días planificados comida a comida.": {
        "en": "The most studied eating pattern in the world, rebuilt around "
              "<em>athlete</em> macros and 28 days planned meal by meal.",
        "fr": "Le modèle alimentaire le plus étudié au monde, repensé avec des macros "
              "d'<em>athlète</em> et 28 jours planifiés repas par repas."},

    '<span class="chip on">28 días</span> '
    '<span class="chip on">20 recetas</span> '
    '<span class="chip">Lista de compras</span> '
    '<span class="chip">Batch cooking</span>': {
        "en": '<span class="chip on">28 days</span> '
              '<span class="chip on">20 recipes</span> '
              '<span class="chip">Shopping list</span> '
              '<span class="chip">Batch cooking</span>',
        "fr": '<span class="chip on">28 jours</span> '
              '<span class="chip on">20 recettes</span> '
              '<span class="chip">Liste de courses</span> '
              '<span class="chip">Batch cooking</span>'},

    "Comidas planificadas": {"en": "Meals planned", "fr": "Repas planifiés"},
    "Recetas premium": {"en": "Premium recipes", "fr": "Recettes premium"},
    "Productos de compra": {"en": "Items to buy", "fr": "Produits à acheter"},

    '<strong>Edición 2026</strong><br><span class="muted">Plan nutricional de 4 semanas · 10 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">4-week nutrition plan · 10 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Plan nutritionnel de 4 semaines · 10 pages</span>'},

    # ── 01 · Introducción ──────────────────────────────────────────────────
    "01 · Introducción": {"en": "01 · Introduction", "fr": "01 · Introduction"},

    'LA DIETA MEDITERRÁNEA <span class="a">PARA ATLETAS</span>': {
        "en": 'THE MEDITERRANEAN DIET <span class="a">FOR ATHLETES</span>',
        "fr": 'LE RÉGIME MÉDITERRANÉEN <span class="a">POUR ATHLÈTES</span>'},

    "No es solo salud cardiovascular. Es el patrón que mejor combina "
    "antioxidantes, grasas saludables, carbohidratos de calidad y densidad de micronutrientes "
    "— exactamente lo que necesita un cuerpo sometido a entrenamiento intenso.": {
        "en": "It is not just cardiovascular health. It is the pattern that best combines "
              "antioxidants, healthy fats, quality carbohydrates and micronutrient density "
              "— exactly what a body under hard training needs.",
        "fr": "Il ne s'agit pas seulement de santé cardiovasculaire. C'est le modèle qui "
              "combine le mieux antioxydants, bonnes graisses, glucides de qualité et "
              "densité en micronutriments — exactement ce dont a besoin un corps soumis à "
              "un entraînement intense."},

    "Objetivo de la semana": {"en": "Goal of the week", "fr": "Objectif de la semaine"},
    "1 · Adaptación": {"en": "1 · Adaptation", "fr": "1 · Adaptation"},
    "Eliminar ultraprocesados sin sufrir": {
        "en": "Remove ultra-processed food without suffering",
        "fr": "Éliminer les ultra-transformés sans souffrir"},
    "2 · Consolidación": {"en": "2 · Consolidation", "fr": "2 · Consolidation"},
    "Dominar el patrón y la compra": {
        "en": "Master the pattern and the shopping",
        "fr": "Maîtriser le modèle et les courses"},
    "3 · Variedad": {"en": "3 · Variety", "fr": "3 · Variété"},
    "Ampliar el recetario": {
        "en": "Widen the recipe book", "fr": "Élargir le répertoire de recettes"},
    "4 · Mantenimiento": {"en": "4 · Maintenance", "fr": "4 · Maintien"},
    "Convertirlo en modo de vida": {
        "en": "Turn it into a way of living", "fr": "En faire un mode de vie"},

    "Valores calculados para un atleta de 75 kg con entrenamiento de "
    "4–5 sesiones semanales. Ajusta proporcionalmente a tu peso corporal.": {
        "en": "Values calculated for a 75 kg athlete training 4–5 sessions a week. Scale "
              "them proportionally to your own body weight.",
        "fr": "Valeurs calculées pour un athlète de 75 kg s'entraînant 4 à 5 fois par "
              "semaine. Ajustez-les proportionnellement à votre poids de corps."},

    "Los 6 pilares del patrón mediterráneo": {
        "en": "The 6 pillars of the Mediterranean pattern",
        "fr": "Les 6 piliers du modèle méditerranéen"},
    "Base diaria": {"en": "Daily base", "fr": "Base quotidienne"},
    "Aceite de oliva virgen extra como grasa principal": {
        "en": "Extra-virgin olive oil as the main fat",
        "fr": "Huile d'olive vierge extra comme matière grasse principale"},
    "Verdura y hortaliza en comida y cena, sin excepción": {
        "en": "Vegetables at lunch and at dinner, without exception",
        "fr": "Des légumes au déjeuner et au dîner, sans exception"},
    "Cereales integrales y legumbres como carbohidrato base": {
        "en": "Wholegrain cereals and pulses as the base carbohydrate",
        "fr": "Céréales complètes et légumineuses comme glucide de base"},
    "Frecuencia semanal": {"en": "Weekly frequency", "fr": "Fréquence hebdomadaire"},
    "Pescado 3–4 veces, con 2 de pescado azul": {
        "en": "Fish 3–4 times, of which 2 oily fish",
        "fr": "Poisson 3 à 4 fois, dont 2 fois du poisson gras"},
    "Legumbre 3–4 veces, huevo 4–6 unidades": {
        "en": "Pulses 3–4 times, eggs 4–6 units",
        "fr": "Légumineuses 3 à 4 fois, 4 à 6 œufs"},
    "Carne roja como mucho 1–2 veces": {
        "en": "Red meat 1–2 times at most", "fr": "Viande rouge 1 à 2 fois au maximum"},

    "Semanas 1 a 4, día a día": {
        "en": "Weeks 1 to 4, day by day", "fr": "Semaines 1 à 4, jour par jour"},
    "Desayuno, colación, almuerzo y cena de los 28 días": {
        "en": "Breakfast, snack, lunch and dinner for all 28 days",
        "fr": "Petit-déjeuner, collation, déjeuner et dîner des 28 jours"},
    "Pág. 3–6": {"en": "P. 3–6", "fr": "P. 3–6"},
    "20 recetas premium": {"en": "20 premium recipes", "fr": "20 recettes premium"},
    "Tiempo, calorías e ingredientes de cada una": {
        "en": "Time, calories and ingredients for each one",
        "fr": "Temps, calories et ingrédients de chacune"},
    "Pág. 7–8": {"en": "P. 7–8", "fr": "P. 7–8"},
    "Lista de compras semanal": {
        "en": "Weekly shopping list", "fr": "Liste de courses hebdomadaire"},
    "Qué comprar, cuánto y en qué fijarte": {
        "en": "What to buy, how much, and what to look for",
        "fr": "Quoi acheter, en quelle quantité et à quoi faire attention"},
    "Pág. 9": {"en": "P. 9", "fr": "P. 9"},
    "Batch cooking del domingo": {
        "en": "Sunday batch cooking", "fr": "Batch cooking du dimanche"},
    "Dos horas que te resuelven la semana entera": {
        "en": "Two hours that settle your whole week",
        "fr": "Deux heures qui règlent toute votre semaine"},
    "Pág. 10": {"en": "P. 10", "fr": "P. 10"},

    # ── Semana 1 ───────────────────────────────────────────────────────────
    "Semana 1 · Adaptación": {"en": "Week 1 · Adaptation", "fr": "Semaine 1 · Adaptation"},

    'SEMANA <span class="a">1</span> · ADAPTACIÓN': {
        "en": 'WEEK <span class="a">1</span> · ADAPTATION',
        "fr": 'SEMAINE <span class="a">1</span> · ADAPTATION'},

    "2.400 kcal · 150 g de proteína · 280 g de carbohidratos · 80 g de grasas. "
    "Esta semana el objetivo no es la perfección, es <strong>sacar los ultraprocesados</strong> de casa.": {
        "en": "2,400 kcal · 150 g protein · 280 g carbohydrate · 80 g fat. This week the "
              "goal is not perfection, it is <strong>getting ultra-processed food</strong> "
              "out of the house.",
        "fr": "2 400 kcal · 150 g de protéines · 280 g de glucides · 80 g de lipides. Cette "
              "semaine, l'objectif n'est pas la perfection, c'est de <strong>sortir les "
              "ultra-transformés</strong> de chez vous."},

    "Colación": {"en": "Snack", "fr": "Collation"},

    "Yogur griego + nueces + miel + arándanos": {
        "en": "Greek yoghurt + walnuts + honey + blueberries",
        "fr": "Yaourt grec + noix + miel + myrtilles"},
    "Almendras + manzana": {"en": "Almonds + apple", "fr": "Amandes + pomme"},
    "Salmón 180 g + arroz integral + ensalada griega": {
        "en": "Salmon 180 g + brown rice + Greek salad",
        "fr": "Saumon 180 g + riz complet + salade grecque"},
    "Garbanzos con espinacas y ajo": {
        "en": "Chickpeas with spinach and garlic",
        "fr": "Pois chiches aux épinards et à l'ail"},
    "Tostada integral + AOVE + tomate + orégano": {
        "en": "Wholegrain toast + EVOO + tomato + oregano",
        "fr": "Pain complet grillé + huile d'olive + tomate + origan"},
    "Hummus + zanahoria": {"en": "Hummus + carrot", "fr": "Houmous + carotte"},
    "Lentejas con verduras y pimiento rojo": {
        "en": "Lentils with vegetables and red pepper",
        "fr": "Lentilles aux légumes et poivron rouge"},
    "Tortilla de calabacín + ensalada": {
        "en": "Courgette omelette + salad", "fr": "Omelette de courgette + salade"},
    "Avena + leche vegetal + plátano + canela": {
        "en": "Oats + plant milk + banana + cinnamon",
        "fr": "Flocons d'avoine + lait végétal + banane + cannelle"},
    "Nueces + pera": {"en": "Walnuts + pear", "fr": "Noix + poire"},
    "Pollo a la plancha 200 g + quinoa + brócoli": {
        "en": "Grilled chicken 200 g + quinoa + broccoli",
        "fr": "Poulet grillé 200 g + quinoa + brocoli"},
    "Sopa minestrone + pan integral": {
        "en": "Minestrone + wholegrain bread", "fr": "Minestrone + pain complet"},
    "Huevos revueltos + tomate cherry + albahaca": {
        "en": "Scrambled eggs + cherry tomatoes + basil",
        "fr": "Œufs brouillés + tomates cerises + basilic"},
    "Yogur + kiwi": {"en": "Yoghurt + kiwi", "fr": "Yaourt + kiwi"},
    "Pasta integral + pesto + tomates secos + queso": {
        "en": "Wholegrain pasta + pesto + sun-dried tomatoes + cheese",
        "fr": "Pâtes complètes + pesto + tomates séchées + fromage"},
    "Dorada al horno + patata + limón": {
        "en": "Baked sea bream + potato + lemon",
        "fr": "Dorade au four + pomme de terre + citron"},
    "Batido: espinaca + mango + proteína + leche": {
        "en": "Smoothie: spinach + mango + protein + milk",
        "fr": "Smoothie : épinard + mangue + protéine + lait"},
    "Dátiles + almendras": {"en": "Dates + almonds", "fr": "Dattes + amandes"},
    "Ensalada niçoise (atún, huevo, oliva, judías)": {
        "en": "Niçoise salad (tuna, egg, olives, green beans)",
        "fr": "Salade niçoise (thon, œuf, olives, haricots verts)"},
    "Merluza al vapor + verduras asadas": {
        "en": "Steamed hake + roasted vegetables", "fr": "Merlu vapeur + légumes rôtis"},
    "Tortitas de avena + sirope de arce + frutos rojos": {
        "en": "Oat pancakes + maple syrup + berries",
        "fr": "Pancakes à l'avoine + sirop d'érable + fruits rouges"},
    "Fruta de temporada": {"en": "Seasonal fruit", "fr": "Fruit de saison"},
    "Paella de verduras + alioli ligero": {
        "en": "Vegetable paella + light aioli", "fr": "Paella de légumes + aïoli léger"},
    "Cordero al romero + cuscús + menta": {
        "en": "Rosemary lamb + couscous + mint",
        "fr": "Agneau au romarin + couscous + menthe"},
    "Granola casera + leche de almendra + fresas": {
        "en": "Homemade granola + almond milk + strawberries",
        "fr": "Granola maison + lait d'amande + fraises"},
    "Nueces + naranja": {"en": "Walnuts + orange", "fr": "Noix + orange"},
    "Cocido mediterráneo (garbanzo, pollo, verdura)": {
        "en": "Mediterranean stew (chickpea, chicken, vegetables)",
        "fr": "Pot-au-feu méditerranéen (pois chiche, poulet, légumes)"},
    "Ensalada grande + queso feta + AOVE": {
        "en": "Large salad + feta + EVOO", "fr": "Grande salade + feta + huile d'olive"},

    "Claves de esta semana": {
        "en": "Keys to this week", "fr": "Les clés de cette semaine"},
    "Vacía la despensa de bollería, refrescos y snacks salados <strong>antes</strong> del lunes.": {
        "en": "Clear the cupboard of pastries, soft drinks and salty snacks "
              "<strong>before</strong> Monday.",
        "fr": "Videz le placard des viennoiseries, sodas et snacks salés "
              "<strong>avant</strong> lundi."},
    "Compra el aceite de oliva virgen extra en formato grande: será tu grasa principal.": {
        "en": "Buy the extra-virgin olive oil in a large format: it will be your main fat.",
        "fr": "Achetez l'huile d'olive vierge extra en grand format : ce sera votre matière "
              "grasse principale."},
    "Si un día te saltas el plan, la comida siguiente vuelve al plan. Sin compensaciones.": {
        "en": "If you go off plan one day, the next meal goes back on plan. No compensating.",
        "fr": "Si vous sortez du plan un jour, le repas suivant y revient. Sans compensation."},
    "Bebe 2,5–3 litros de agua: al subir la fibra, el cuerpo la necesita.": {
        "en": "Drink 2.5–3 litres of water: as the fibre goes up, your body needs it.",
        "fr": "Buvez 2,5 à 3 litres d'eau : quand les fibres augmentent, le corps en a besoin."},

    "Es normal que la primera semana notes más saciedad": {
        "en": "Feeling fuller in the first week is normal",
        "fr": "Il est normal de se sentir plus rassasié la première semaine"},
    "Vas a comer bastante más volumen de comida por la misma energía. Si te cuesta terminar "
    "los platos, reparte la verdura entre más tomas y añade una cucharada extra de aceite "
    "para no quedarte corto de calorías.": {
        "en": "You are going to eat a considerably greater volume of food for the same "
              "energy. If you struggle to finish your plates, spread the vegetables across "
              "more meals and add an extra spoonful of oil so you do not fall short on "
              "calories.",
        "fr": "Vous allez manger un volume de nourriture bien plus important pour la même "
              "énergie. Si vous avez du mal à finir vos assiettes, répartissez les légumes "
              "sur davantage de repas et ajoutez une cuillère d'huile supplémentaire pour "
              "ne pas manquer de calories."},

    # ── Semana 2 ───────────────────────────────────────────────────────────
    "Semana 2 · Consolidación": {
        "en": "Week 2 · Consolidation", "fr": "Semaine 2 · Consolidation"},

    'SEMANA <span class="a">2</span> · CONSOLIDACIÓN': {
        "en": 'WEEK <span class="a">2</span> · CONSOLIDATION',
        "fr": 'SEMAINE <span class="a">2</span> · CONSOLIDATION'},

    "2.500 kcal · 160 g de proteína · 295 g de carbohidratos · 82 g de grasas. "
    "El objetivo es que la <strong>compra y la cocina</strong> dejen de costarte esfuerzo mental.": {
        "en": "2,500 kcal · 160 g protein · 295 g carbohydrate · 82 g fat. The goal is for "
              "<strong>shopping and cooking</strong> to stop costing you mental effort.",
        "fr": "2 500 kcal · 160 g de protéines · 295 g de glucides · 82 g de lipides. "
              "L'objectif est que <strong>les courses et la cuisine</strong> ne vous "
              "demandent plus d'effort mental."},

    "Tostada integral + aguacate + huevo poché": {
        "en": "Wholegrain toast + avocado + poached egg",
        "fr": "Pain complet grillé + avocat + œuf poché"},
    "Yogur griego + nueces": {"en": "Greek yoghurt + walnuts", "fr": "Yaourt grec + noix"},
    "Arroz integral + pollo al limón + pisto": {
        "en": "Brown rice + lemon chicken + pisto",
        "fr": "Riz complet + poulet au citron + pisto"},
    "Crema de calabaza + tortilla francesa": {
        "en": "Pumpkin soup + plain omelette", "fr": "Velouté de potiron + omelette nature"},
    "Porridge de avena + higos + almendra": {
        "en": "Oat porridge + figs + almond", "fr": "Porridge d'avoine + figues + amande"},
    "Manzana + queso fresco": {"en": "Apple + fresh cheese", "fr": "Pomme + fromage frais"},
    "Bacalao + patata + judías verdes": {
        "en": "Cod + potato + green beans",
        "fr": "Cabillaud + pomme de terre + haricots verts"},
    "Ensalada de garbanzos, atún y pimiento": {
        "en": "Chickpea, tuna and pepper salad",
        "fr": "Salade de pois chiches, thon et poivron"},
    "Yogur griego + granola + frambuesas": {
        "en": "Greek yoghurt + granola + raspberries",
        "fr": "Yaourt grec + granola + framboises"},
    "Tostada + tomate + jamón": {
        "en": "Toast + tomato + ham", "fr": "Pain grillé + tomate + jambon"},
    "Espaguetis integrales + boloñesa de ternera magra": {
        "en": "Wholegrain spaghetti + lean beef bolognese",
        "fr": "Spaghettis complets + bolognaise de bœuf maigre"},
    "Sopa de pescado + pan integral": {
        "en": "Fish soup + wholegrain bread", "fr": "Soupe de poisson + pain complet"},
    "Revuelto de setas + 3 huevos + tostada": {
        "en": "Mushroom scramble with 3 eggs + toast",
        "fr": "Œufs brouillés aux champignons (3 œufs) + pain grillé"},
    "Puñado de pistachos": {
        "en": "A handful of pistachios", "fr": "Une poignée de pistaches"},
    "Cuscús integral + pollo especiado + verduras": {
        "en": "Wholegrain couscous + spiced chicken + vegetables",
        "fr": "Couscous complet + poulet épicé + légumes"},
    "Ensalada caprese + tortilla de patata ligera": {
        "en": "Caprese salad + light potato omelette",
        "fr": "Salade caprese + tortilla de pommes de terre allégée"},
    "Batido de plátano, avena y proteína": {
        "en": "Banana, oat and protein smoothie",
        "fr": "Smoothie banane, avoine et protéine"},
    "Zanahoria + hummus": {"en": "Carrot + hummus", "fr": "Carotte + houmous"},
    "Salmón al horno + boniato + espárragos": {
        "en": "Baked salmon + sweet potato + asparagus",
        "fr": "Saumon au four + patate douce + asperges"},
    "Berenjena rellena de quinoa y pavo": {
        "en": "Aubergine stuffed with quinoa and turkey",
        "fr": "Aubergine farcie au quinoa et à la dinde"},
    "Torrijas integrales al horno + frutos rojos": {
        "en": "Baked wholegrain torrijas + berries",
        "fr": "Pain perdu complet au four + fruits rouges"},
    "Naranja + almendras": {"en": "Orange + almonds", "fr": "Orange + amandes"},
    "Paella de marisco": {"en": "Seafood paella", "fr": "Paella de fruits de mer"},
    "Ensalada de lentejas + huevo cocido": {
        "en": "Lentil salad + boiled egg", "fr": "Salade de lentilles + œuf dur"},
    "Tortilla de espinacas + pan + AOVE": {
        "en": "Spinach omelette + bread + EVOO",
        "fr": "Omelette aux épinards + pain + huile d'olive"},
    "Uvas + nueces": {"en": "Grapes + walnuts", "fr": "Raisin + noix"},
    "Pollo asado + patatas al romero + ensalada": {
        "en": "Roast chicken + rosemary potatoes + salad",
        "fr": "Poulet rôti + pommes de terre au romarin + salade"},
    "Crema de puerro + feta + tostada": {
        "en": "Leek soup + feta + toast", "fr": "Velouté de poireau + feta + pain grillé"},

    "Haz la compra <strong>una sola vez</strong>, con la lista de la página 9 en la mano.": {
        "en": "Do the shopping <strong>once only</strong>, with the list on page 9 in hand.",
        "fr": "Faites les courses <strong>en une seule fois</strong>, la liste de la page 9 "
              "à la main."},
    "Cocina el arroz, la quinoa y las legumbres del domingo para tres días.": {
        "en": "On Sunday, cook the rice, the quinoa and the pulses for three days ahead.",
        "fr": "Le dimanche, cuisinez le riz, le quinoa et les légumineuses pour trois jours."},
    "Introduce el pescado azul dos veces: salmón el viernes, marisco el sábado.": {
        "en": "Bring in oily fish twice: salmon on Friday, seafood on Saturday.",
        "fr": "Introduisez le poisson gras deux fois : saumon le vendredi, fruits de mer le "
              "samedi."},
    "Anota qué dos platos te han gustado más: serán tus comodines cuando no tengas tiempo.": {
        "en": "Note the two dishes you liked most: they will be your fallbacks when time is "
              "short.",
        "fr": "Notez les deux plats que vous avez préférés : ce seront vos valeurs sûres "
              "quand vous manquerez de temps."},

    "Truco de las cenas": {"en": "The dinner trick", "fr": "L'astuce des dîners"},
    "Todas las cenas de esta semana se preparan en menos de 20 minutos y admiten la "
    "verdura que te haya sobrado del almuerzo. La cena mediterránea es ligera por diseño: "
    "el grueso de los carbohidratos va al mediodía, alrededor del entrenamiento.": {
        "en": "Every dinner this week takes under 20 minutes and will happily absorb "
              "whatever vegetables were left over from lunch. The Mediterranean dinner is "
              "light by design: the bulk of the carbohydrate goes at midday, around training.",
        "fr": "Tous les dîners de cette semaine se préparent en moins de 20 minutes et "
              "acceptent les légumes restés du déjeuner. Le dîner méditerranéen est léger "
              "par construction : l'essentiel des glucides se place à midi, autour de "
              "l'entraînement."},

    # ── Semana 3 ───────────────────────────────────────────────────────────
    "Semana 3 · Variedad": {"en": "Week 3 · Variety", "fr": "Semaine 3 · Variété"},

    'SEMANA <span class="a">3</span> · VARIEDAD': {
        "en": 'WEEK <span class="a">3</span> · VARIETY',
        "fr": 'SEMAINE <span class="a">3</span> · VARIÉTÉ'},

    "2.500 kcal · 165 g de proteína · 300 g de carbohidratos · 83 g de grasas. "
    "Se amplía el recetario para que el patrón <strong>no aburra nunca</strong>.": {
        "en": "2,500 kcal · 165 g protein · 300 g carbohydrate · 83 g fat. The recipe book "
              "widens so the pattern <strong>never gets boring</strong>.",
        "fr": "2 500 kcal · 165 g de protéines · 300 g de glucides · 83 g de lipides. Le "
              "répertoire s'élargit pour que le modèle <strong>ne lasse jamais</strong>."},

    "Avena con cacao puro y plátano": {
        "en": "Oats with pure cocoa and banana", "fr": "Avoine au cacao pur et banane"},
    "Atún fresco a la plancha + arroz + wok de verduras": {
        "en": "Seared fresh tuna + rice + vegetable stir-fry",
        "fr": "Thon frais poêlé + riz + wok de légumes"},
    "Sopa de tomate + tostada con sardinas": {
        "en": "Tomato soup + toast with sardines",
        "fr": "Soupe de tomate + pain grillé aux sardines"},
    "Tostada de centeno + queso fresco + miel": {
        "en": "Rye toast + fresh cheese + honey",
        "fr": "Pain de seigle grillé + fromage frais + miel"},
    "Almendras + pera": {"en": "Almonds + pear", "fr": "Amandes + poire"},
    "Pollo al curry mediterráneo + cuscús": {
        "en": "Mediterranean curried chicken + couscous",
        "fr": "Poulet au curry méditerranéen + couscous"},
    "Tortilla de calabacín + ensalada de rúcula": {
        "en": "Courgette omelette + rocket salad",
        "fr": "Omelette de courgette + salade de roquette"},
    "Bol de yogur + granola + arándanos": {
        "en": "Yoghurt bowl + granola + blueberries",
        "fr": "Bol de yaourt + granola + myrtilles"},
    "Hummus + crudités": {"en": "Hummus + crudités", "fr": "Houmous + crudités"},
    "Merluza en salsa verde + patata + guisantes": {
        "en": "Hake in salsa verde + potato + peas",
        "fr": "Merlu en sauce verte + pomme de terre + petits pois"},
    "Ensalada de pasta integral + atún + olivas": {
        "en": "Wholegrain pasta salad + tuna + olives",
        "fr": "Salade de pâtes complètes + thon + olives"},
    "Huevos revueltos + espinacas + tostada": {
        "en": "Scrambled eggs + spinach + toast",
        "fr": "Œufs brouillés + épinards + pain grillé"},
    "Plátano + nueces": {"en": "Banana + walnuts", "fr": "Banane + noix"},
    "Ternera magra + boniato asado + brócoli": {
        "en": "Lean beef + roast sweet potato + broccoli",
        "fr": "Bœuf maigre + patate douce rôtie + brocoli"},
    "Gazpacho + brochetas de pollo": {
        "en": "Gazpacho + chicken skewers", "fr": "Gaspacho + brochettes de poulet"},
    "Batido verde + proteína + avena": {
        "en": "Green smoothie + protein + oats", "fr": "Smoothie vert + protéine + avoine"},
    "Queso fresco + tomate": {"en": "Fresh cheese + tomato", "fr": "Fromage frais + tomate"},
    "Risotto integral de setas + pollo": {
        "en": "Wholegrain mushroom risotto + chicken",
        "fr": "Risotto complet aux champignons + poulet"},
    "Dorada al horno + verduras asadas": {
        "en": "Baked sea bream + roasted vegetables",
        "fr": "Dorade au four + légumes rôtis"},
    "Tortitas de avena + frutos rojos": {
        "en": "Oat pancakes + berries", "fr": "Pancakes à l'avoine + fruits rouges"},
    "Fideuá de marisco": {"en": "Seafood fideuá", "fr": "Fideuá de fruits de mer"},
    "Ensalada griega + huevo duro": {
        "en": "Greek salad + hard-boiled egg", "fr": "Salade grecque + œuf dur"},
    "Tostada + aguacate + salmón ahumado": {
        "en": "Toast + avocado + smoked salmon",
        "fr": "Pain grillé + avocat + saumon fumé"},
    "Naranja + pistachos": {"en": "Orange + pistachios", "fr": "Orange + pistaches"},
    "Cordero al horno + cuscús + menta": {
        "en": "Roast lamb + couscous + mint", "fr": "Agneau au four + couscous + menthe"},
    "Crema de calabacín + tortilla": {
        "en": "Courgette soup + omelette", "fr": "Velouté de courgette + omelette"},

    "Prueba al menos <strong>tres recetas nuevas</strong> del recetario de las páginas 7 y 8.": {
        "en": "Try at least <strong>three new recipes</strong> from the recipe book on "
              "pages 7 and 8.",
        "fr": "Essayez au moins <strong>trois nouvelles recettes</strong> du répertoire des "
              "pages 7 et 8."},
    "Cambia el pescado según lo que esté de temporada y mejor de precio en tu pescadería.": {
        "en": "Swap the fish for whatever is in season and best priced at your fishmonger.",
        "fr": "Changez de poisson selon ce qui est de saison et au meilleur prix chez votre "
              "poissonnier."},
    "Usa hierbas frescas: albahaca, menta, perejil y orégano cambian por completo un plato.": {
        "en": "Use fresh herbs: basil, mint, parsley and oregano completely change a dish.",
        "fr": "Utilisez des herbes fraîches : basilic, menthe, persil et origan transforment "
              "complètement un plat."},
    "Si comes fuera un día, pide pescado o carne a la plancha con verdura y guarnición de patata.": {
        "en": "If you eat out one day, order grilled fish or meat with vegetables and a "
              "potato side.",
        "fr": "Si vous mangez dehors un jour, commandez du poisson ou de la viande grillée "
              "avec des légumes et une garniture de pommes de terre."},

    "Come de temporada": {"en": "Eat in season", "fr": "Mangez de saison"},
    "El producto de temporada tiene más sabor, más densidad de nutrientes y cuesta menos. "
    "Sustituye sin miedo cualquier verdura o fruta del plan por su equivalente de temporada: "
    "el patrón es lo que importa, no el ingrediente exacto.": {
        "en": "Seasonal produce has more flavour, more nutrient density and costs less. Swap "
              "any vegetable or fruit in the plan for its seasonal equivalent without "
              "hesitation: the pattern is what matters, not the exact ingredient.",
        "fr": "Le produit de saison a plus de goût, plus de densité nutritionnelle et coûte "
              "moins cher. Remplacez sans crainte n'importe quel légume ou fruit du plan par "
              "son équivalent de saison : c'est le modèle qui compte, pas l'ingrédient exact."},

    # ── Semana 4 ───────────────────────────────────────────────────────────
    "Semana 4 · Mantenimiento": {
        "en": "Week 4 · Maintenance", "fr": "Semaine 4 · Maintien"},

    'SEMANA <span class="a">4</span> · MANTENIMIENTO': {
        "en": 'WEEK <span class="a">4</span> · MAINTENANCE',
        "fr": 'SEMAINE <span class="a">4</span> · MAINTIEN'},

    "2.600 kcal · 170 g de proteína · 310 g de carbohidratos · 85 g de grasas. "
    "Esta semana ya no estás «haciendo una dieta»: estás <strong>comiendo así</strong>.": {
        "en": "2,600 kcal · 170 g protein · 310 g carbohydrate · 85 g fat. This week you are "
              "no longer “on a diet”: this is simply <strong>how you eat</strong>.",
        "fr": "2 600 kcal · 170 g de protéines · 310 g de glucides · 85 g de lipides. Cette "
              "semaine, vous ne « suivez » plus un régime : c'est <strong>votre façon de "
              "manger</strong>."},

    "Porridge de avena + manzana y canela": {
        "en": "Oat porridge + apple and cinnamon",
        "fr": "Porridge d'avoine + pomme et cannelle"},
    "Yogur griego + miel": {"en": "Greek yoghurt + honey", "fr": "Yaourt grec + miel"},
    "Pollo al limón + arroz integral + ensalada": {
        "en": "Lemon chicken + brown rice + salad",
        "fr": "Poulet au citron + riz complet + salade"},
    "Sopa minestrone + queso feta": {
        "en": "Minestrone + feta", "fr": "Minestrone + feta"},
    "Tostada integral + tomate + jamón serrano": {
        "en": "Wholegrain toast + tomato + serrano ham",
        "fr": "Pain complet grillé + tomate + jambon serrano"},
    "Nueces + mandarina": {"en": "Walnuts + mandarin", "fr": "Noix + mandarine"},
    "Lentejas estofadas con verduras": {
        "en": "Braised lentils with vegetables", "fr": "Lentilles mijotées aux légumes"},
    "Salmón a la plancha + espárragos": {
        "en": "Grilled salmon + asparagus", "fr": "Saumon poêlé + asperges"},
    "Batido de proteína + plátano + avena": {
        "en": "Protein + banana + oat smoothie",
        "fr": "Smoothie protéine + banane + avoine"},
    "Hummus + pan de pita integral": {
        "en": "Hummus + wholegrain pitta", "fr": "Houmous + pain pita complet"},
    "Pasta integral + pesto + pollo": {
        "en": "Wholegrain pasta + pesto + chicken", "fr": "Pâtes complètes + pesto + poulet"},
    "Revuelto de setas + ensalada": {
        "en": "Mushroom scramble + salad",
        "fr": "Œufs brouillés aux champignons + salade"},
    "Yogur griego + granola + frutos rojos": {
        "en": "Greek yoghurt + granola + berries",
        "fr": "Yaourt grec + granola + fruits rouges"},
    "Bacalao con garbanzos y espinacas": {
        "en": "Cod with chickpeas and spinach",
        "fr": "Cabillaud aux pois chiches et épinards"},
    "Tortilla de patata ligera + ensalada": {
        "en": "Light potato omelette + salad",
        "fr": "Tortilla de pommes de terre allégée + salade"},
    "Tostada francesa integral + fresas": {
        "en": "Wholegrain French toast + strawberries",
        "fr": "Pain perdu complet + fraises"},
    "Queso fresco + nueces": {"en": "Fresh cheese + walnuts", "fr": "Fromage frais + noix"},
    "Ternera + patata al horno + pimientos": {
        "en": "Beef + baked potato + peppers",
        "fr": "Bœuf + pomme de terre au four + poivrons"},
    "Crema de verduras + brochetas de gambas": {
        "en": "Vegetable soup + prawn skewers",
        "fr": "Velouté de légumes + brochettes de crevettes"},
    "Huevos escalfados + espinacas + tostada": {
        "en": "Poached eggs + spinach + toast",
        "fr": "Œufs pochés + épinards + pain grillé"},
    "Fruta + pistachos": {"en": "Fruit + pistachios", "fr": "Fruit + pistaches"},
    "Paella valenciana": {"en": "Valencian paella", "fr": "Paella valencienne"},
    "Ensalada de quinoa, aguacate y atún": {
        "en": "Quinoa, avocado and tuna salad",
        "fr": "Salade de quinoa, avocat et thon"},
    "Bol mediterráneo: yogur, higos y nueces": {
        "en": "Mediterranean bowl: yoghurt, figs and walnuts",
        "fr": "Bol méditerranéen : yaourt, figues et noix"},
    "Uvas + almendras": {"en": "Grapes + almonds", "fr": "Raisin + amandes"},
    "Cocido ligero (garbanzo, pollo, verdura)": {
        "en": "Light stew (chickpea, chicken, vegetables)",
        "fr": "Pot-au-feu léger (pois chiche, poulet, légumes)"},
    "Pescado al horno + ensalada grande": {
        "en": "Baked fish + large salad", "fr": "Poisson au four + grande salade"},

    "Cómo continuar a partir de aquí": {
        "en": "How to carry on from here", "fr": "Comment continuer à partir d'ici"},
    "Tu objetivo": {"en": "Your goal", "fr": "Votre objectif"},
    "Ajuste sobre la semana 4": {
        "en": "Adjustment to week 4", "fr": "Ajustement par rapport à la semaine 4"},
    "Mantener peso": {"en": "Maintain weight", "fr": "Maintenir le poids"},
    "Repite la semana 4 indefinidamente, rotando las cuatro semanas": {
        "en": "Repeat week 4 indefinitely, rotating through all four weeks",
        "fr": "Répétez la semaine 4 indéfiniment, en faisant tourner les quatre semaines"},
    "Suma 300–400 kcal: más arroz, pasta o pan integral en el almuerzo": {
        "en": "Add 300–400 kcal: more rice, pasta or wholegrain bread at lunch",
        "fr": "Ajoutez 300 à 400 kcal : plus de riz, de pâtes ou de pain complet au déjeuner"},
    "Resta 350–450 kcal: reduce los carbohidratos de la cena y una cucharada de aceite": {
        "en": "Take off 350–450 kcal: cut the dinner carbohydrate and one spoonful of oil",
        "fr": "Retirez 350 à 450 kcal : réduisez les glucides du dîner et une cuillère d'huile"},
    "Rendimiento en resistencia": {
        "en": "Endurance performance", "fr": "Performance en endurance"},
    "Sube los carbohidratos el día previo a las sesiones largas": {
        "en": "Raise the carbohydrate the day before long sessions",
        "fr": "Augmentez les glucides la veille des séances longues"},

    "Has completado 28 días": {
        "en": "You have completed 28 days", "fr": "Vous avez terminé 28 jours"},
    "Rota estas cuatro semanas de forma indefinida. Es la gran ventaja del patrón "
    "mediterráneo frente a cualquier dieta de moda: <strong>no tiene fecha de caducidad</strong>, "
    "porque no depende de restringir grupos enteros de alimentos.": {
        "en": "Rotate these four weeks indefinitely. That is the great advantage of the "
              "Mediterranean pattern over any fad diet: <strong>it has no expiry "
              "date</strong>, because it does not depend on restricting whole food groups.",
        "fr": "Faites tourner ces quatre semaines indéfiniment. C'est le grand avantage du "
              "modèle méditerranéen sur n'importe quel régime à la mode : <strong>il n'a pas "
              "de date de péremption</strong>, parce qu'il ne repose pas sur l'exclusion de "
              "groupes d'aliments entiers."},

    # ── Recetas 1–10 ───────────────────────────────────────────────────────
    "Recetas 1–10": {"en": "Recipes 1–10", "fr": "Recettes 1–10"},
    '20 RECETAS PREMIUM · <span class="a">PARTE 1</span>': {
        "en": '20 PREMIUM RECIPES · <span class="a">PART 1</span>',
        "fr": '20 RECETTES PREMIUM · <span class="a">PARTIE 1</span>'},
    "Receta": {"en": "Recipe", "fr": "Recette"},
    "Tiempo · Kcal": {"en": "Time · Kcal", "fr": "Temps · Kcal"},
    "Ingredientes y elaboración": {
        "en": "Ingredients and method", "fr": "Ingrédients et préparation"},

    "Tzatziki de aguacate": {"en": "Avocado tzatziki", "fr": "Tzatziki à l'avocat"},
    '5 min · 180 kcal<br><span class="muted small">Vegano</span>': {
        "en": '5 min · 180 kcal<br><span class="muted small">Vegan</span>',
        "fr": '5 min · 180 kcal<br><span class="muted small">Végétalien</span>'},
    "Aguacate maduro, yogur de coco, pepino, ajo, limón y eneldo. Machaca el aguacate, mezcla todo y refrigera 30 min.": {
        "en": "Ripe avocado, coconut yoghurt, cucumber, garlic, lemon and dill. Mash the "
              "avocado, mix everything and chill for 30 min.",
        "fr": "Avocat mûr, yaourt de coco, concombre, ail, citron et aneth. Écrasez "
              "l'avocat, mélangez le tout et réfrigérez 30 min."},

    "Salmón con salsa verde": {
        "en": "Salmon with salsa verde", "fr": "Saumon à la sauce verte"},
    "20 min · 480 kcal": {"en": "20 min · 480 kcal", "fr": "20 min · 480 kcal"},
    "Salmón 200 g, perejil, alcaparras, anchoas, limón y AOVE. Cocina el salmón 4 min por lado, tritura la salsa y sirve junto.": {
        "en": "Salmon 200 g, parsley, capers, anchovies, lemon and EVOO. Cook the salmon "
              "4 min per side, blend the sauce and serve together.",
        "fr": "Saumon 200 g, persil, câpres, anchois, citron et huile d'olive vierge extra. "
              "Cuisez le saumon 4 min par face, mixez la sauce et servez ensemble."},

    "Gazpacho andaluz": {"en": "Andalusian gazpacho", "fr": "Gaspacho andalou"},
    "10 min · 140 kcal": {"en": "10 min · 140 kcal", "fr": "10 min · 140 kcal"},
    "Tomate 600 g, pepino, pimiento, pan remojado, vinagre de Jerez y AOVE. Tritura muy fino, cuela y enfría 2 h.": {
        "en": "Tomato 600 g, cucumber, pepper, soaked bread, sherry vinegar and EVOO. Blend "
              "very fine, strain and chill for 2 h.",
        "fr": "Tomate 600 g, concombre, poivron, pain trempé, vinaigre de Xérès et huile "
              "d'olive. Mixez très finement, passez au chinois et réfrigérez 2 h."},

    "Hummus casero": {"en": "Homemade hummus", "fr": "Houmous maison"},
    "10 min · 220 kcal": {"en": "10 min · 220 kcal", "fr": "10 min · 220 kcal"},
    "Garbanzos 400 g, tahini 3 cdas, limón, ajo, AOVE y comino. Tritura hasta que quede cremoso y decora con pimentón.": {
        "en": "Chickpeas 400 g, tahini 3 tbsp, lemon, garlic, EVOO and cumin. Blend until "
              "creamy and dust with paprika.",
        "fr": "Pois chiches 400 g, tahini 3 c. à s., citron, ail, huile d'olive et cumin. "
              "Mixez jusqu'à obtenir une texture crémeuse et saupoudrez de paprika."},

    "Tortilla mediterránea": {
        "en": "Mediterranean omelette", "fr": "Omelette méditerranéenne"},
    "15 min · 320 kcal": {"en": "15 min · 320 kcal", "fr": "15 min · 320 kcal"},
    "3 huevos, berenjena, pimiento, tomate cherry y feta. Sofríe la verdura, añade el huevo y cuaja a fuego bajo.": {
        "en": "3 eggs, aubergine, pepper, cherry tomatoes and feta. Fry the vegetables, add "
              "the egg and set over a low heat.",
        "fr": "3 œufs, aubergine, poivron, tomates cerises et feta. Faites revenir les "
              "légumes, ajoutez l'œuf et laissez prendre à feu doux."},

    "Pasta con pesto de rúcula": {
        "en": "Pasta with rocket pesto", "fr": "Pâtes au pesto de roquette"},
    "15 min · 520 kcal": {"en": "15 min · 520 kcal", "fr": "15 min · 520 kcal"},
    "Pasta integral 120 g, rúcula 60 g, parmesano, piñones, ajo y AOVE. Pesto en crudo, mezclado con la pasta al dente.": {
        "en": "Wholegrain pasta 120 g, rocket 60 g, parmesan, pine nuts, garlic and EVOO. "
              "Raw pesto, tossed through the pasta al dente.",
        "fr": "Pâtes complètes 120 g, roquette 60 g, parmesan, pignons, ail et huile "
              "d'olive. Pesto cru, mélangé aux pâtes al dente."},

    "Lentejas a la provenzal": {"en": "Provençal lentils", "fr": "Lentilles à la provençale"},
    "30 min · 420 kcal": {"en": "30 min · 420 kcal", "fr": "30 min · 420 kcal"},
    "Lentejas 150 g, tomate, zanahoria, apio, tomillo, laurel y AOVE. Sofríe la verdura, añade la lenteja y cuece 25 min.": {
        "en": "Lentils 150 g, tomato, carrot, celery, thyme, bay and EVOO. Fry the "
              "vegetables, add the lentils and simmer for 25 min.",
        "fr": "Lentilles 150 g, tomate, carotte, céleri, thym, laurier et huile d'olive. "
              "Faites revenir les légumes, ajoutez les lentilles et cuisez 25 min."},

    "Dorada al horno con patatas": {
        "en": "Baked sea bream with potatoes", "fr": "Dorade au four aux pommes de terre"},
    "35 min · 510 kcal": {"en": "35 min · 510 kcal", "fr": "35 min · 510 kcal"},
    "Dorada 300 g, patata 200 g, tomate, olivas, alcaparras y vino blanco. Hornea a 200 °C durante 25 minutos.": {
        "en": "Sea bream 300 g, potato 200 g, tomato, olives, capers and white wine. Bake at "
              "200 °C for 25 minutes.",
        "fr": "Dorade 300 g, pomme de terre 200 g, tomate, olives, câpres et vin blanc. "
              "Enfournez à 200 °C pendant 25 minutes."},

    "Tabulé libanés": {"en": "Lebanese tabbouleh", "fr": "Taboulé libanais"},
    "15 min · 280 kcal": {"en": "15 min · 280 kcal", "fr": "15 min · 280 kcal"},
    "Bulgur 80 g, perejil, menta, tomate, pepino, limón y AOVE. Remoja el bulgur, mezcla en frío y deja reposar 30 min.": {
        "en": "Bulgur 80 g, parsley, mint, tomato, cucumber, lemon and EVOO. Soak the "
              "bulgur, mix cold and leave to rest for 30 min.",
        "fr": "Boulgour 80 g, persil, menthe, tomate, concombre, citron et huile d'olive. "
              "Faites tremper le boulgour, mélangez à froid et laissez reposer 30 min."},

    "Shakshuka": {"en": "Shakshuka", "fr": "Shakshuka"},
    "20 min · 380 kcal": {"en": "20 min · 380 kcal", "fr": "20 min · 380 kcal"},
    "Tomate triturado 400 g, pimiento, cebolla, comino, pimentón ahumado y 3 huevos. Sofríe, casca los huevos y tapa hasta cuajar.": {
        "en": "Crushed tomato 400 g, pepper, onion, cumin, smoked paprika and 3 eggs. Fry "
              "the base, crack in the eggs and cover until they set.",
        "fr": "Tomate concassée 400 g, poivron, oignon, cumin, paprika fumé et 3 œufs. "
              "Faites revenir, cassez les œufs et couvrez jusqu'à ce qu'ils prennent."},

    "Sobre el aceite de oliva": {
        "en": "About olive oil", "fr": "À propos de l'huile d'olive"},
    "Usa virgen extra en crudo para aliñar y virgen para cocinar. Contra lo que se suele "
    "decir, el AOVE resiste bien la temperatura de una sartén doméstica gracias a sus "
    "antioxidantes y su alto contenido en ácido oleico.": {
        "en": "Use extra virgin raw for dressing and virgin for cooking. Contrary to what is "
              "often said, extra-virgin olive oil stands up well to the temperature of a "
              "domestic frying pan, thanks to its antioxidants and its high oleic acid "
              "content.",
        "fr": "Utilisez la vierge extra à cru pour assaisonner et la vierge pour cuisiner. "
              "Contrairement à ce que l'on dit souvent, l'huile d'olive vierge extra "
              "supporte bien la température d'une poêle domestique, grâce à ses "
              "antioxydants et à sa forte teneur en acide oléique."},

    # ── Recetas 11–20 ──────────────────────────────────────────────────────
    "Recetas 11–20": {"en": "Recipes 11–20", "fr": "Recettes 11–20"},
    '20 RECETAS PREMIUM · <span class="a">PARTE 2</span>': {
        "en": '20 PREMIUM RECIPES · <span class="a">PART 2</span>',
        "fr": '20 RECETTES PREMIUM · <span class="a">PARTIE 2</span>'},

    "Salmorejo cordobés": {"en": "Salmorejo from Córdoba", "fr": "Salmorejo de Cordoue"},
    "10 min · 260 kcal": {"en": "10 min · 260 kcal", "fr": "10 min · 260 kcal"},
    "Tomate 1 kg, pan 150 g, ajo, AOVE 60 ml y sal. Tritura muy fino hasta emulsionar y sirve con huevo duro y jamón.": {
        "en": "Tomato 1 kg, bread 150 g, garlic, EVOO 60 ml and salt. Blend very fine until "
              "it emulsifies and serve with hard-boiled egg and ham.",
        "fr": "Tomate 1 kg, pain 150 g, ail, huile d'olive 60 ml et sel. Mixez très finement "
              "jusqu'à émulsion et servez avec œuf dur et jambon."},

    "Berenjenas a la parmesana ligeras": {
        "en": "Light aubergine parmigiana", "fr": "Aubergines à la parmesane allégées"},
    "40 min · 390 kcal": {"en": "40 min · 390 kcal", "fr": "40 min · 390 kcal"},
    "Berenjena al horno (no frita), tomate triturado, albahaca, mozzarella light y parmesano. Capas y gratinado 15 min.": {
        "en": "Baked (not fried) aubergine, crushed tomato, basil, light mozzarella and "
              "parmesan. Layer it up and grill for 15 min.",
        "fr": "Aubergine au four (non frite), tomate concassée, basilic, mozzarella allégée "
              "et parmesan. Montez en couches et gratinez 15 min."},

    "25 min · 470 kcal": {"en": "25 min · 470 kcal", "fr": "25 min · 470 kcal"},
    "Bacalao desalado 200 g, garbanzos 200 g, espinacas, ajo, pimentón y AOVE. Saltea, añade el bacalao y cuece 8 min.": {
        "en": "Desalted cod 200 g, chickpeas 200 g, spinach, garlic, paprika and EVOO. Sauté, "
              "add the cod and cook for 8 min.",
        "fr": "Cabillaud dessalé 200 g, pois chiches 200 g, épinards, ail, paprika et huile "
              "d'olive. Faites sauter, ajoutez le cabillaud et cuisez 8 min."},

    "Pollo al limón y orégano": {
        "en": "Lemon and oregano chicken", "fr": "Poulet au citron et à l'origan"},
    "25 min · 420 kcal": {"en": "25 min · 420 kcal", "fr": "25 min · 420 kcal"},
    "Pechuga 200 g, limón, orégano, ajo, AOVE y caldo. Marca el pollo, desglasa con limón y caldo, reduce 5 min.": {
        "en": "Chicken breast 200 g, lemon, oregano, garlic, EVOO and stock. Sear the "
              "chicken, deglaze with lemon and stock, reduce for 5 min.",
        "fr": "Blanc de poulet 200 g, citron, origan, ail, huile d'olive et bouillon. "
              "Saisissez le poulet, déglacez au citron et au bouillon, réduisez 5 min."},

    "Risotto integral de setas": {
        "en": "Wholegrain mushroom risotto", "fr": "Risotto complet aux champignons"},
    "35 min · 520 kcal": {"en": "35 min · 520 kcal", "fr": "35 min · 520 kcal"},
    "Arroz integral 100 g, setas variadas, cebolla, caldo de verdura, vino blanco y parmesano. Añade el caldo poco a poco.": {
        "en": "Brown rice 100 g, mixed mushrooms, onion, vegetable stock, white wine and "
              "parmesan. Add the stock a ladle at a time.",
        "fr": "Riz complet 100 g, champignons variés, oignon, bouillon de légumes, vin blanc "
              "et parmesan. Ajoutez le bouillon petit à petit."},

    "Caponata siciliana": {"en": "Sicilian caponata", "fr": "Caponata sicilienne"},
    '30 min · 240 kcal<br><span class="muted small">Vegano</span>': {
        "en": '30 min · 240 kcal<br><span class="muted small">Vegan</span>',
        "fr": '30 min · 240 kcal<br><span class="muted small">Végétalien</span>'},
    "Berenjena, apio, cebolla, tomate, alcaparras, olivas, vinagre y una pizca de miel. Guisa 20 min y sirve templada.": {
        "en": "Aubergine, celery, onion, tomato, capers, olives, vinegar and a pinch of "
              "honey. Stew for 20 min and serve warm.",
        "fr": "Aubergine, céleri, oignon, tomate, câpres, olives, vinaigre et une pointe de "
              "miel. Mijotez 20 min et servez tiède."},

    "Boquerones en vinagre": {
        "en": "Fresh anchovies in vinegar", "fr": "Anchois frais au vinaigre"},
    "15 min + 24 h · 180 kcal": {
        "en": "15 min + 24 h · 180 kcal", "fr": "15 min + 24 h · 180 kcal"},
    "Boquerones limpios, vinagre de vino, ajo, perejil y AOVE. Congela 48 h antes por seguridad, después macera en vinagre.": {
        "en": "Cleaned fresh anchovies, wine vinegar, garlic, parsley and EVOO. Freeze for "
              "48 h beforehand for safety, then marinate in vinegar.",
        "fr": "Anchois frais nettoyés, vinaigre de vin, ail, persil et huile d'olive. "
              "Congelez 48 h au préalable par sécurité, puis faites mariner dans le vinaigre."},

    "Ensalada griega auténtica": {
        "en": "Authentic Greek salad", "fr": "Salade grecque authentique"},
    "10 min · 310 kcal": {"en": "10 min · 310 kcal", "fr": "10 min · 310 kcal"},
    "Tomate, pepino, cebolla roja, pimiento verde, olivas kalamata, bloque de feta y orégano. Sin lechuga, con AOVE generoso.": {
        "en": "Tomato, cucumber, red onion, green pepper, kalamata olives, a block of feta "
              "and oregano. No lettuce, and be generous with the EVOO.",
        "fr": "Tomate, concombre, oignon rouge, poivron vert, olives kalamata, un bloc de "
              "feta et origan. Sans laitue, et généreux en huile d'olive."},

    "Pisto manchego con huevo": {
        "en": "Pisto manchego with egg", "fr": "Pisto manchego à l'œuf"},
    "35 min · 350 kcal": {"en": "35 min · 350 kcal", "fr": "35 min · 350 kcal"},
    "Calabacín, berenjena, pimiento, cebolla y tomate. Sofríe por separado, une y termina con un huevo escalfado encima.": {
        "en": "Courgette, aubergine, pepper, onion and tomato. Fry each one separately, "
              "bring them together and finish with a poached egg on top.",
        "fr": "Courgette, aubergine, poivron, oignon et tomate. Faites revenir séparément, "
              "réunissez et terminez avec un œuf poché dessus."},

    "Yogur griego con higos y nueces": {
        "en": "Greek yoghurt with figs and walnuts", "fr": "Yaourt grec aux figues et noix"},
    "3 min · 290 kcal": {"en": "3 min · 290 kcal", "fr": "3 min · 290 kcal"},
    "Yogur griego 200 g, higos frescos, nueces 20 g, miel y canela. El postre mediterráneo por excelencia.": {
        "en": "Greek yoghurt 200 g, fresh figs, walnuts 20 g, honey and cinnamon. The "
              "Mediterranean dessert par excellence.",
        "fr": "Yaourt grec 200 g, figues fraîches, noix 20 g, miel et cannelle. Le dessert "
              "méditerranéen par excellence."},

    "Cómo adaptar cualquier receta a tus macros": {
        "en": "How to fit any recipe to your macros",
        "fr": "Comment adapter n'importe quelle recette à vos macros"},
    "La proteína y la verdura son fijas; el carbohidrato y el aceite son tus mandos de "
    "ajuste. Para subir calorías, añade 10 g de aceite (90 kcal) o 30 g de arroz en crudo "
    "(105 kcal). Para bajarlas, haz lo contrario. Nunca toques la proteína.": {
        "en": "Protein and vegetables are fixed; carbohydrate and oil are your adjustment "
              "dials. To raise calories, add 10 g of oil (90 kcal) or 30 g of uncooked rice "
              "(105 kcal). To lower them, do the opposite. Never touch the protein.",
        "fr": "Les protéines et les légumes sont fixes ; les glucides et l'huile sont vos "
              "molettes de réglage. Pour augmenter les calories, ajoutez 10 g d'huile "
              "(90 kcal) ou 30 g de riz cru (105 kcal). Pour les baisser, faites l'inverse. "
              "Ne touchez jamais aux protéines."},

    # ── Lista de compras ───────────────────────────────────────────────────
    "Lista de compras": {"en": "Shopping list", "fr": "Liste de courses"},
    'LISTA DE COMPRAS <span class="a">SEMANAL</span>': {
        "en": '<span class="a">WEEKLY</span> SHOPPING LIST',
        "fr": 'LISTE DE COURSES <span class="a">HEBDOMADAIRE</span>'},
    "Sección": {"en": "Section", "fr": "Rayon"},
    "Cantidad semanal": {"en": "Weekly quantity", "fr": "Quantité hebdomadaire"},
    "En qué fijarte": {"en": "What to look for", "fr": "À quoi faire attention"},

    "Frutas y verduras": {"en": "Fruit and vegetables", "fr": "Fruits et légumes"},
    "Tomates": {"en": "Tomatoes", "fr": "Tomates"},
    "1,5 kg": {"en": "1.5 kg", "fr": "1,5 kg"},
    "Maduros, para salsas y salmorejo": {
        "en": "Ripe, for sauces and salmorejo",
        "fr": "Bien mûres, pour les sauces et le salmorejo"},
    "Espinacas baby": {"en": "Baby spinach", "fr": "Jeunes pousses d'épinard"},
    "Para ensaladas y sofritos": {
        "en": "For salads and sautés", "fr": "Pour salades et poêlées"},
    "Pimientos variados": {"en": "Assorted peppers", "fr": "Poivrons variés"},
    "4–6 unidades": {"en": "4–6 units", "fr": "4 à 6 unités"},
    "De todos los colores": {"en": "Of every colour", "fr": "De toutes les couleurs"},
    "Berenjena y calabacín": {
        "en": "Aubergine and courgette", "fr": "Aubergine et courgette"},
    "2 de cada": {"en": "2 of each", "fr": "2 de chaque"},
    "Pisto, caponata y tortilla": {
        "en": "Pisto, caponata and omelette", "fr": "Pisto, caponata et omelette"},
    "Pepino y tomate cherry": {
        "en": "Cucumber and cherry tomatoes", "fr": "Concombre et tomates cerises"},
    "Ensaladas frescas": {"en": "Fresh salads", "fr": "Salades fraîches"},
    "2 kg": {"en": "2 kg", "fr": "2 kg"},
    "Variada, para colaciones": {"en": "Mixed, for snacks", "fr": "Variés, pour les collations"},

    "Proteínas": {"en": "Protein", "fr": "Protéines"},
    "Salmón fresco": {"en": "Fresh salmon", "fr": "Saumon frais"},
    "Refrigerado, consumir en 2 días": {
        "en": "Refrigerated, use within 2 days", "fr": "Au frais, à consommer sous 2 jours"},
    "Atún en lata al AOVE": {
        "en": "Tinned tuna in EVOO", "fr": "Thon en conserve à l'huile d'olive"},
    "6 latas": {"en": "6 tins", "fr": "6 boîtes"},
    "Para ensaladas y pastas": {
        "en": "For salads and pasta", "fr": "Pour salades et pâtes"},
    "Pechuga de pollo": {"en": "Chicken breast", "fr": "Blanc de poulet"},
    "1 kg": {"en": "1 kg", "fr": "1 kg"},
    "Sin piel, a la plancha o al horno": {
        "en": "Skinless, grilled or baked", "fr": "Sans peau, à la poêle ou au four"},
    "Huevos camperos": {
        "en": "Free-range eggs", "fr": "Œufs de poules élevées en plein air"},
    "18 unidades": {"en": "18 units", "fr": "18 unités"},
    "Código 0 o 1 en la cáscara": {
        "en": "Code 0 or 1 stamped on the shell", "fr": "Code 0 ou 1 sur la coquille"},
    "Garbanzos y lentejas": {
        "en": "Chickpeas and lentils", "fr": "Pois chiches et lentilles"},
    "500 g de cada": {"en": "500 g of each", "fr": "500 g de chaque"},
    "Cocidos en bote o secos": {
        "en": "Cooked in a jar, or dried", "fr": "Cuits en bocal, ou secs"},
    "Pescado blanco": {"en": "White fish", "fr": "Poisson blanc"},
    "Merluza, bacalao o dorada": {
        "en": "Hake, cod or sea bream", "fr": "Merlu, cabillaud ou dorade"},

    "Lácteos": {"en": "Dairy", "fr": "Produits laitiers"},
    "Yogur griego natural": {"en": "Plain Greek yoghurt", "fr": "Yaourt grec nature"},
    "8 unidades": {"en": "8 units", "fr": "8 unités"},
    "Sin azúcares añadidos": {"en": "No added sugars", "fr": "Sans sucres ajoutés"},
    "Queso feta": {"en": "Feta cheese", "fr": "Feta"},
    "Para ensaladas y gratinados": {
        "en": "For salads and gratins", "fr": "Pour salades et gratins"},

    "Despensa": {"en": "Store cupboard", "fr": "Épicerie"},
    "Aceite de oliva virgen extra": {
        "en": "Extra-virgin olive oil", "fr": "Huile d'olive vierge extra"},
    "1 L al mes": {"en": "1 L a month", "fr": "1 L par mois"},
    "Primera prensada en frío": {
        "en": "First cold pressing", "fr": "Première pression à froid"},
    "Pasta y arroz integrales": {
        "en": "Wholegrain pasta and rice", "fr": "Pâtes et riz complets"},
    "Base de los almuerzos": {
        "en": "The base of your lunches", "fr": "Base des déjeuners"},
    "Avena, quinoa y cuscús": {
        "en": "Oats, quinoa and couscous", "fr": "Avoine, quinoa et couscous"},
    "500 g en total": {"en": "500 g in total", "fr": "500 g au total"},
    "Rotación de cereales": {"en": "Cereal rotation", "fr": "Rotation des céréales"},
    "Frutos secos": {"en": "Nuts", "fr": "Fruits à coque"},
    "Almendras y nueces": {"en": "Almonds and walnuts", "fr": "Amandes et noix"},
    "200 g de cada": {"en": "200 g of each", "fr": "200 g de chaque"},
    "Crudos, sin sal ni tostar": {
        "en": "Raw, unsalted and untoasted", "fr": "Crus, ni salés ni grillés"},
    "Hierbas": {"en": "Herbs", "fr": "Herbes"},
    "Orégano, albahaca, tomillo, romero": {
        "en": "Oregano, basil, thyme, rosemary", "fr": "Origan, basilic, thym, romarin"},
    "Variado": {"en": "Assorted", "fr": "Assortiment"},
    "Frescas mejor que secas": {
        "en": "Fresh beats dried", "fr": "Fraîches plutôt que séchées"},

    "Regla mediterránea de la etiqueta": {
        "en": "The Mediterranean label rule",
        "fr": "La règle méditerranéenne de l'étiquette"},
    "Si un producto tiene más de cinco ingredientes en la etiqueta, o tu abuela no lo "
    "reconocería como comida, no forma parte de este patrón. Compra local, de temporada y "
    "sin procesar.": {
        "en": "If a product has more than five ingredients on the label, or your grandmother "
              "would not recognise it as food, it is not part of this pattern. Buy local, "
              "seasonal and unprocessed.",
        "fr": "Si un produit compte plus de cinq ingrédients sur l'étiquette, ou si votre "
              "grand-mère ne le reconnaîtrait pas comme de la nourriture, il ne fait pas "
              "partie de ce modèle. Achetez local, de saison et non transformé."},

    # ── Batch cooking ──────────────────────────────────────────────────────
    "Batch cooking": {"en": "Batch cooking", "fr": "Batch cooking"},
    'DOS HORAS QUE TE RESUELVEN <span class="a">LA SEMANA</span>': {
        "en": 'TWO HOURS THAT SETTLE <span class="a">YOUR WHOLE WEEK</span>',
        "fr": 'DEUX HEURES QUI RÈGLENT <span class="a">TOUTE LA SEMAINE</span>'},
    "Tarea": {"en": "Task", "fr": "Tâche"},
    "Resultado": {"en": "Result", "fr": "Résultat"},

    "Enciende el horno a 200 °C y pon a hervir arroz y quinoa": {
        "en": "Heat the oven to 200 °C and put rice and quinoa on to boil",
        "fr": "Allumez le four à 200 °C et mettez le riz et le quinoa à cuire"},
    "Base de carbohidratos para 4 días": {
        "en": "Carbohydrate base for 4 days", "fr": "Base de glucides pour 4 jours"},
    "Bandeja de verduras al horno: pimiento, calabacín, berenjena, cebolla": {
        "en": "A tray of roast vegetables: pepper, courgette, aubergine, onion",
        "fr": "Une plaque de légumes au four : poivron, courgette, aubergine, oignon"},
    "Guarnición lista para 5 comidas": {
        "en": "A side dish ready for 5 meals", "fr": "Une garniture prête pour 5 repas"},
    "Segunda bandeja: pechugas de pollo especiadas y boniato": {
        "en": "Second tray: spiced chicken breasts and sweet potato",
        "fr": "Deuxième plaque : blancs de poulet épicés et patate douce"},
    "Proteína y carbohidrato para 3 almuerzos": {
        "en": "Protein and carbohydrate for 3 lunches",
        "fr": "Protéines et glucides pour 3 déjeuners"},
    "Guiso de lentejas o garbanzos en una olla": {
        "en": "A pot of lentil or chickpea stew",
        "fr": "Une cocotte de lentilles ou de pois chiches"},
    "Dos comidas completas de legumbre": {
        "en": "Two complete pulse-based meals",
        "fr": "Deux repas complets à base de légumineuses"},
    "Sofrito base de tomate y salsa de pesto": {
        "en": "A base tomato sofrito and a pesto sauce",
        "fr": "Un sofrito de tomate de base et une sauce pesto"},
    "Sirve para pasta, pisto y shakshuka": {
        "en": "Works for pasta, pisto and shakshuka",
        "fr": "Sert pour les pâtes, le pisto et la shakshuka"},
    "Lava y seca la hoja verde, corta crudités": {
        "en": "Wash and dry the leaves, cut the crudités",
        "fr": "Lavez et séchez les feuilles, taillez les crudités"},
    "Ensaladas en 30 segundos toda la semana": {
        "en": "Salads in 30 seconds all week",
        "fr": "Des salades en 30 secondes toute la semaine"},
    "Cuece 6 huevos y prepara hummus": {
        "en": "Boil 6 eggs and make hummus",
        "fr": "Faites cuire 6 œufs et préparez du houmous"},
    "Colaciones y proteína de emergencia": {
        "en": "Snacks and emergency protein",
        "fr": "Collations et protéines de secours"},
    "Reparte en táperes y etiqueta con el día": {
        "en": "Divide into containers and label each with the day",
        "fr": "Répartissez en boîtes et étiquetez chacune avec le jour"},
    "Cero decisiones durante la semana": {
        "en": "Zero decisions during the week", "fr": "Zéro décision pendant la semaine"},

    "Conservación segura": {"en": "Safe storage", "fr": "Conservation sûre"},
    "Enfría los platos antes de cerrar el táper y refrigéralos en menos de 2 horas.": {
        "en": "Cool the dishes before sealing the container and refrigerate them within "
              "2 hours.",
        "fr": "Laissez refroidir les plats avant de fermer la boîte et réfrigérez-les en "
              "moins de 2 heures."},
    "Cereales cocidos y legumbres: 3–4 días en frigorífico. Pescado cocinado: 2 días.": {
        "en": "Cooked grains and pulses: 3–4 days in the fridge. Cooked fish: 2 days.",
        "fr": "Céréales cuites et légumineuses : 3 à 4 jours au réfrigérateur. Poisson "
              "cuit : 2 jours."},
    "Congela en raciones individuales lo que no vayas a comer en 3 días.": {
        "en": "Freeze in single portions anything you will not eat within 3 days.",
        "fr": "Congelez en portions individuelles ce que vous ne mangerez pas sous 3 jours."},
    "Las ensaladas se montan en el momento: la hoja verde aliñada se estropea en horas.": {
        "en": "Salads are assembled at the last moment: dressed leaves spoil within hours.",
        "fr": "Les salades se montent au dernier moment : les feuilles assaisonnées se "
              "dégradent en quelques heures."},

    # ── Cierre ─────────────────────────────────────────────────────────────
    'VEINTIOCHO DÍAS, <span class="a">Y LUEGO TODA LA VIDA</span>': {
        "en": 'TWENTY-EIGHT DAYS, <span class="a">AND THEN A LIFETIME</span>',
        "fr": 'VINGT-HUIT JOURS, <span class="a">ET ENSUITE TOUTE LA VIE</span>'},

    "Estos menús están calculados para 75 kg: <strong>escala cada ración a "
    "tu peso</strong> y vuelve a empezar por la semana 1. El patrón mediterráneo no caduca "
    "porque no prohíbe ningún grupo de alimentos, y por eso se puede repetir sin fin.": {
        "en": "These menus are calculated for 75 kg: <strong>scale every portion to your own "
              "weight</strong> and start again from week 1. The Mediterranean pattern does "
              "not expire, because it bans no food group — which is exactly why it can be "
              "repeated without end.",
        "fr": "Ces menus sont calculés pour 75 kg : <strong>adaptez chaque portion à votre "
              "poids</strong> et recommencez à la semaine 1. Le modèle méditerranéen ne "
              "périme pas, parce qu'il n'interdit aucun groupe d'aliments — et c'est "
              "précisément pour cela qu'on peut le répéter sans fin."},

    # ── Aviso legal ────────────────────────────────────────────────────────
    "<b>Aviso importante</b><br> "
    "Este plan tiene finalidad informativa y educativa. No constituye consejo médico, "
    "diagnóstico ni tratamiento, y no sustituye la valoración de un profesional sanitario "
    "colegiado ni de un dietista-nutricionista. Los menús están diseñados para personas adultas "
    "sanas y no contemplan alergias ni intolerancias: revisa cada ingrediente si eres alérgico "
    "al pescado, marisco, frutos secos, huevo, lácteos o gluten. Consulta con tu médico antes "
    "de iniciar este plan si estás embarazada o en periodo de lactancia, eres menor de edad, "
    "tomas medicación o padeces alguna patología. Los valores nutricionales son estimaciones "
    "y pueden variar según marca, corte y método de cocinado. Contenido protegido por derechos "
    "de autor: prohibida su reproducción, distribución o reventa sin autorización escrita de "
    "VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br> "
              "This plan is for informational and educational purposes. It does not "
              "constitute medical advice, diagnosis or treatment, and it does not replace "
              "assessment by a registered health professional or a dietitian. The menus are "
              "designed for healthy adults and do not account for allergies or intolerances: "
              "check every ingredient if you are allergic to fish, shellfish, nuts, egg, "
              "dairy or gluten. Consult your doctor before starting this plan if you are "
              "pregnant or breastfeeding, are a minor, take medication or have a medical "
              "condition. The nutritional values are estimates and may vary with brand, cut "
              "and cooking method. Copyrighted content: reproduction, distribution or resale "
              "without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br> "
              "Ce plan a une finalité informative et éducative. Il ne constitue ni un avis "
              "médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation "
              "d'un professionnel de santé ni d'un diététicien-nutritionniste. Les menus "
              "sont conçus pour des adultes en bonne santé et ne tiennent pas compte des "
              "allergies ni des intolérances : vérifiez chaque ingrédient si vous êtes "
              "allergique au poisson, aux fruits de mer, aux fruits à coque, à l'œuf, aux "
              "produits laitiers ou au gluten. Consultez votre médecin avant de commencer ce "
              "plan si vous êtes enceinte ou allaitante, mineure, si vous prenez un "
              "traitement ou souffrez d'une pathologie. Les valeurs nutritionnelles sont des "
              "estimations et peuvent varier selon la marque, la découpe et le mode de "
              "cuisson. Contenu protégé par le droit d'auteur : toute reproduction, "
              "distribution ou revente sans autorisation écrite de VILLUMINATIONS est "
              "interdite."},
}
