# -*- coding: utf-8 -*-
"""
PLAN 01 · BÁSICO — Guía rápida de volumen limpio
================================================
Traducción al inglés y al francés. Las cifras, las unidades y las fórmulas se
mantienen idénticas: son datos, no prosa, y cambiarlas al traducir sería
introducir un error. Sí se adapta la puntuación decimal, que en inglés lleva
punto y en español y francés lleva coma.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Guía rápida</small>\n        <span class="glow">VOLUMEN<br>LIMPIO</span>': {
        "en": '<small>Quick guide</small>\n        <span class="glow">CLEAN<br>BULKING</span>',
        "fr": '<small>Guide rapide</small>\n        <span class="glow">PRISE DE<br>MASSE PROPRE</span>'},
    "Los 10 principios que debes dominar para ganar masa muscular\n        de calidad — con la calculadora para convertirlos en <em>tus</em> números.": {
        "en": "The 10 principles you need to master to gain quality muscle — with the calculator that turns them into <em>your</em> numbers.",
        "fr": "Les 10 principes à maîtriser pour gagner du muscle de qualité — avec le calculateur qui les transforme en <em>vos</em> chiffres."},
    '<span class="chip on">10 principios</span>\n        <span class="chip on">Macros a medida</span>\n        <span class="chip">Menús de ejemplo</span>\n        <span class="chip">Checklist semanal</span>': {
        "en": '<span class="chip on">10 principles</span>\n        <span class="chip on">Custom macros</span>\n        <span class="chip">Sample menus</span>\n        <span class="chip">Weekly checklist</span>',
        "fr": '<span class="chip on">10 principes</span>\n        <span class="chip on">Macros sur mesure</span>\n        <span class="chip">Menus types</span>\n        <span class="chip">Check-list hebdo</span>'},
    "Principios": {"en": "Principles", "fr": "Principes"},
    "3 pasos": {"en": "3 steps", "fr": "3 étapes"},
    "Para tus macros": {"en": "To your macros", "fr": "Vers vos macros"},
    "Intercambios": {"en": "Swaps", "fr": "Équivalences"},
    "4 sem.": {"en": "4 wks", "fr": "4 sem."},
    "De registro": {"en": "Of tracking", "fr": "De suivi"},
    '<strong>Edición 2026</strong><br>\n        <span class="muted">Guía de referencia rápida · 7 páginas</span>': {
        "en": '<strong>2026 edition</strong><br>\n        <span class="muted">Quick reference guide · 7 pages</span>',
        "fr": '<strong>Édition 2026</strong><br>\n        <span class="muted">Guide de référence rapide · 7 pages</span>'},

    # ── Índice ────────────────────────────────────────────────────────
    "Cómo usar esta guía": {"en": "How to use this guide", "fr": "Comment utiliser ce guide"},
    'ANTES DE <span class="a">EMPEZAR</span>': {
        "en": 'BEFORE YOU <span class="a">START</span>',
        "fr": 'AVANT DE <span class="a">COMMENCER</span>'},
    "El volumen limpio no consiste en «comer mucho». Consiste en comer <strong>lo justo por encima</strong> de lo que gastas, con la proteína cubierta y el entrenamiento progresando. Todo lo demás es ruido.": {
        "en": "Clean bulking is not about «eating a lot». It is about eating <strong>just above</strong> what you burn, with protein covered and training progressing. Everything else is noise.",
        "fr": "La prise de masse propre ne consiste pas à « manger beaucoup ». Elle consiste à manger <strong>juste au-dessus</strong> de ce que vous dépensez, avec les protéines couvertes et l'entraînement qui progresse. Tout le reste est du bruit."},
    "sobre tu gasto": {"en": "above your expenditure", "fr": "au-dessus de votre dépense"},
    "2 g/kg": {"en": "2 g/kg", "fr": "2 g/kg"},
    "proteína diaria": {"en": "protein per day", "fr": "protéines par jour"},
    "peso ganado/semana": {"en": "weight gained/week", "fr": "poids gagné/semaine"},
    "Contenido": {"en": "Contents", "fr": "Sommaire"},
    "Los 10 principios del volumen limpio": {
        "en": "The 10 principles of clean bulking",
        "fr": "Les 10 principes de la prise de masse propre"},
    "Las reglas que gobiernan todo lo demás": {
        "en": "The rules that govern everything else",
        "fr": "Les règles qui gouvernent tout le reste"},
    "Pág. 3": {"en": "P. 3", "fr": "P. 3"},
    "Calcula TUS macros en 3 pasos": {
        "en": "Work out YOUR macros in 3 steps",
        "fr": "Calculez VOS macros en 3 étapes"},
    "Fórmula, ejemplo resuelto y tabla para rellenar": {
        "en": "Formula, worked example and a table to fill in",
        "fr": "Formule, exemple résolu et tableau à remplir"},
    "Pág. 4": {"en": "P. 4", "fr": "P. 4"},
    "Menús y reparto del día": {
        "en": "Menus and how the day is split",
        "fr": "Menus et répartition de la journée"},
    "Opciones por momento + tabla de intercambios": {
        "en": "Options for each meal + swap table",
        "fr": "Options par moment + tableau d'équivalences"},
    "Pág. 5": {"en": "P. 5", "fr": "P. 5"},
    "Errores que frenan tu progreso": {
        "en": "Mistakes that stall your progress",
        "fr": "Erreurs qui freinent vos progrès"},
    "Los 8 fallos más caros y cómo corregirlos": {
        "en": "The 8 costliest mistakes and how to fix them",
        "fr": "Les 8 erreurs les plus coûteuses et comment les corriger"},
    "Pág. 6": {"en": "P. 6", "fr": "P. 6"},
    "Checklist semanal y siguiente paso": {
        "en": "Weekly checklist and next step",
        "fr": "Check-list hebdomadaire et étape suivante"},
    "Tu rutina de control cada lunes": {
        "en": "Your Monday review routine",
        "fr": "Votre routine de contrôle du lundi"},
    "Pág. 7": {"en": "P. 7", "fr": "P. 7"},
    "Cómo sacarle el máximo partido": {
        "en": "How to get the most out of it",
        "fr": "Comment en tirer le meilleur parti"},
    "Lee la guía entera una vez. Después vuelve a la página 4, calcula tus números y quédate con ellos <strong>cuatro semanas completas</strong> antes de cambiar nada. Ajustar cada dos días es la forma más rápida de no progresar nunca.": {
        "en": "Read the guide through once. Then go back to page 4, work out your numbers and stick with them for <strong>four full weeks</strong> before changing anything. Adjusting every two days is the fastest way never to progress.",
        "fr": "Lisez le guide en entier une fois. Revenez ensuite à la page 4, calculez vos chiffres et gardez-les <strong>quatre semaines complètes</strong> avant de changer quoi que ce soit. Ajuster tous les deux jours est le moyen le plus rapide de ne jamais progresser."},

    # ── 01 · Principios ───────────────────────────────────────────────
    "01 · Principios": {"en": "01 · Principles", "fr": "01 · Principes"},
    'LOS 10 PRINCIPIOS DEL <span class="a">VOLUMEN LIMPIO</span>': {
        "en": 'THE 10 PRINCIPLES OF <span class="a">CLEAN BULKING</span>',
        "fr": 'LES 10 PRINCIPES DE LA <span class="a">PRISE DE MASSE PROPRE</span>'},
    "<b>Superávit controlado</b>Un 10–15 % por encima de tu mantenimiento: unas 300–500 kcal. Más superávit no acelera el músculo, solo la grasa.": {
        "en": "<b>Controlled surplus</b>10–15 % above your maintenance: roughly 300–500 kcal. A bigger surplus does not speed up muscle, only fat.",
        "fr": "<b>Surplus contrôlé</b>10–15 % au-dessus de votre maintenance : environ 300–500 kcal. Un surplus plus grand n'accélère pas le muscle, seulement la graisse."},
    "<b>La proteína va primero</b>1,8–2,2 g por kg de peso corporal, repartida en 4–5 tomas de al menos 0,4 g/kg cada una. Es el único macro que no se negocia.": {
        "en": "<b>Protein comes first</b>1.8–2.2 g per kg of body weight, split across 4–5 servings of at least 0.4 g/kg each. It is the one macro that is not negotiable.",
        "fr": "<b>Les protéines d'abord</b>1,8–2,2 g par kg de poids corporel, réparties en 4–5 prises d'au moins 0,4 g/kg chacune. C'est le seul macro qui ne se négocie pas."},
    "<b>Carbohidratos estratégicos</b>4–6 g/kg al día, concentrando la mayor parte en las 2 horas previas y las 2 posteriores al entrenamiento.": {
        "en": "<b>Strategic carbohydrates</b>4–6 g/kg per day, with most of it in the 2 hours before and the 2 hours after training.",
        "fr": "<b>Glucides stratégiques</b>4–6 g/kg par jour, en concentrant l'essentiel dans les 2 heures avant et les 2 heures après l'entraînement."},
    "<b>Grasas saludables</b>0,8–1 g/kg. Nunca bajes de 0,6 g/kg: por debajo de ahí la producción hormonal se resiente. Prioriza omega-3, aguacate y aceite de oliva virgen extra.": {
        "en": "<b>Healthy fats</b>0.8–1 g/kg. Never drop below 0.6 g/kg: below that, hormone production suffers. Prioritise omega-3, avocado and extra virgin olive oil.",
        "fr": "<b>Bonnes graisses</b>0,8–1 g/kg. Ne descendez jamais sous 0,6 g/kg : en dessous, la production hormonale en pâtit. Privilégiez les oméga-3, l'avocat et l'huile d'olive vierge extra."},
    "<b>Hidratación real</b>35–40 ml por kg al día, más 500–750 ml extra por cada hora de entrenamiento. Una deshidratación del 2 % ya reduce tu fuerza.": {
        "en": "<b>Real hydration</b>35–40 ml per kg per day, plus an extra 500–750 ml for every hour of training. Just 2 % dehydration already cuts your strength.",
        "fr": "<b>Hydratation réelle</b>35–40 ml par kg et par jour, plus 500–750 ml supplémentaires par heure d'entraînement. Une déshydratation de 2 % réduit déjà votre force."},
    "<b>Calidad sobre cantidad</b>80 % alimentos mínimamente procesados, 20 % flexibilidad. Esa flexibilidad no es un premio: es lo que hace que sigas aquí dentro de un año.": {
        "en": "<b>Quality over quantity</b>80 % minimally processed food, 20 % flexibility. That flexibility is not a reward: it is what keeps you here a year from now.",
        "fr": "<b>La qualité avant la quantité</b>80 % d'aliments peu transformés, 20 % de souplesse. Cette souplesse n'est pas une récompense : c'est ce qui fera que vous serez encore là dans un an."},
    "<b>Paciencia calibrada</b>0,25–0,5 % de tu peso corporal por semana. En un atleta de 80 kg son 200–400 g semanales. Ganar más rápido es ganar grasa.": {
        "en": "<b>Calibrated patience</b>0.25–0.5 % of your body weight per week. For an 80 kg athlete that is 200–400 g a week. Gaining faster means gaining fat.",
        "fr": "<b>Patience calibrée</b>0,25–0,5 % de votre poids corporel par semaine. Pour un athlète de 80 kg, cela fait 200–400 g par semaine. Gagner plus vite, c'est gagner de la graisse."},
    "<b>Sueño como suplemento</b>7–9 horas. El 70 % de la hormona de crecimiento se libera durmiendo, y tres noches malas bajan la testosterona hasta un 15 %.": {
        "en": "<b>Sleep as a supplement</b>7–9 hours. 70 % of growth hormone is released while asleep, and three bad nights lower testosterone by up to 15 %.",
        "fr": "<b>Le sommeil comme complément</b>7–9 heures. 70 % de l'hormone de croissance est libérée pendant le sommeil, et trois mauvaises nuits font baisser la testostérone jusqu'à 15 %."},
    "<b>Sobrecarga progresiva</b>Cada 1–2 semanas: +2,5–5 % de peso, o una repetición más con el mismo peso. Si el registro no sube, el músculo tampoco.": {
        "en": "<b>Progressive overload</b>Every 1–2 weeks: +2.5–5 % weight, or one more rep at the same weight. If the logbook does not go up, neither does the muscle.",
        "fr": "<b>Surcharge progressive</b>Toutes les 1–2 semaines : +2,5–5 % de charge, ou une répétition de plus au même poids. Si le carnet ne monte pas, le muscle non plus."},
    "<b>Registro honesto</b>Pesa la comida las primeras 4–6 semanas hasta calibrar el ojo. Pésate a diario y trabaja con el <strong>promedio semanal</strong>, nunca con el dato suelto.": {
        "en": "<b>Honest tracking</b>Weigh your food for the first 4–6 weeks until your eye is calibrated. Weigh yourself daily and work with the <strong>weekly average</strong>, never with a single reading.",
        "fr": "<b>Suivi honnête</b>Pesez vos aliments les 4–6 premières semaines, le temps de calibrer l'œil. Pesez-vous chaque jour et travaillez avec la <strong>moyenne hebdomadaire</strong>, jamais avec une valeur isolée."},
    "El error nº 1 del principiante": {
        "en": "The beginner's number one mistake",
        "fr": "L'erreur n° 1 du débutant"},
    "Confundir «volumen» con permiso para comer sin control. Un superávit de 1.000 kcal no construye el doble de músculo que uno de 400: construye lo mismo, con el doble de grasa y una definición mucho más larga por delante.": {
        "en": "Mistaking «bulking» for permission to eat without control. A 1,000 kcal surplus does not build twice the muscle of a 400 kcal one: it builds the same, with twice the fat and a much longer cut ahead of you.",
        "fr": "Confondre « prise de masse » et permission de manger sans contrôle. Un surplus de 1 000 kcal ne construit pas deux fois plus de muscle qu'un surplus de 400 : il en construit autant, avec deux fois plus de graisse et une sèche bien plus longue devant vous."},

    # ── 02 · Tus números ──────────────────────────────────────────────
    "02 · Tus números": {"en": "02 · Your numbers", "fr": "02 · Vos chiffres"},
    'CALCULA <span class="a">TUS MACROS</span> EN 3 PASOS': {
        "en": 'WORK OUT <span class="a">YOUR MACROS</span> IN 3 STEPS',
        "fr": 'CALCULEZ <span class="a">VOS MACROS</span> EN 3 ÉTAPES'},
    "Paso 1 · Tu metabolismo basal (fórmula Mifflin-St Jeor)": {
        "en": "Step 1 · Your basal metabolic rate (Mifflin-St Jeor formula)",
        "fr": "Étape 1 · Votre métabolisme de base (formule Mifflin-St Jeor)"},
    "Sexo": {"en": "Sex", "fr": "Sexe"},
    "Fórmula (peso en kg · altura en cm · edad en años)": {
        "en": "Formula (weight in kg · height in cm · age in years)",
        "fr": "Formule (poids en kg · taille en cm · âge en années)"},
    "Hombre": {"en": "Male", "fr": "Homme"},
    "TMB = (10 × peso) + (6,25 × altura) − (5 × edad) + 5": {
        "en": "BMR = (10 × weight) + (6.25 × height) − (5 × age) + 5",
        "fr": "MB = (10 × poids) + (6,25 × taille) − (5 × âge) + 5"},
    "Mujer": {"en": "Female", "fr": "Femme"},
    "TMB = (10 × peso) + (6,25 × altura) − (5 × edad) − 161": {
        "en": "BMR = (10 × weight) + (6.25 × height) − (5 × age) − 161",
        "fr": "MB = (10 × poids) + (6,25 × taille) − (5 × âge) − 161"},
    "Paso 2 · Multiplica por tu nivel de actividad": {
        "en": "Step 2 · Multiply by your activity level",
        "fr": "Étape 2 · Multipliez par votre niveau d'activité"},
    "Nivel": {"en": "Level", "fr": "Niveau"},
    "Factor": {"en": "Factor", "fr": "Facteur"},
    "Descripción": {"en": "Description", "fr": "Description"},
    "Sedentario": {"en": "Sedentary", "fr": "Sédentaire"},
    "Trabajo de oficina, sin entrenamiento": {
        "en": "Desk job, no training", "fr": "Travail de bureau, sans entraînement"},
    "Ligero": {"en": "Light", "fr": "Léger"},
    "1–3 sesiones por semana": {"en": "1–3 sessions per week", "fr": "1–3 séances par semaine"},
    "Moderado": {"en": "Moderate", "fr": "Modéré"},
    "3–5 sesiones por semana": {"en": "3–5 sessions per week", "fr": "3–5 séances par semaine"},
    "Alto": {"en": "High", "fr": "Élevé"},
    "6–7 sesiones por semana": {"en": "6–7 sessions per week", "fr": "6–7 séances par semaine"},
    "Muy alto": {"en": "Very high", "fr": "Très élevé"},
    "Doble sesión o trabajo físico intenso": {
        "en": "Two sessions a day or heavy physical work",
        "fr": "Double séance ou travail physique intense"},
    "Paso 3 · Reparte los macros": {
        "en": "Step 3 · Split the macros", "fr": "Étape 3 · Répartissez les macros"},
    "Macro": {"en": "Macro", "fr": "Macro"},
    "Cantidad": {"en": "Amount", "fr": "Quantité"},
    "Kcal por gramo": {"en": "Kcal per gram", "fr": "Kcal par gramme"},
    "Calorías objetivo": {"en": "Target calories", "fr": "Calories cibles"},
    "Mantenimiento + 300 a 500 kcal": {
        "en": "Maintenance + 300 to 500 kcal", "fr": "Maintenance + 300 à 500 kcal"},
    "Proteína": {"en": "Protein", "fr": "Protéines"},
    "2,0 g × tu peso en kg": {"en": "2.0 g × your weight in kg", "fr": "2,0 g × votre poids en kg"},
    "Grasas": {"en": "Fats", "fr": "Lipides"},
    "0,9 g × tu peso en kg": {"en": "0.9 g × your weight in kg", "fr": "0,9 g × votre poids en kg"},
    "Carbohidratos": {"en": "Carbohydrates", "fr": "Glucides"},
    "(Calorías − proteína − grasas) ÷ 4": {
        "en": "(Calories − protein − fats) ÷ 4", "fr": "(Calories − protéines − lipides) ÷ 4"},
    "Ejemplo resuelto · Hombre, 75 kg, 178 cm, 28 años, actividad moderada": {
        "en": "Worked example · Male, 75 kg, 178 cm, 28 years, moderate activity",
        "fr": "Exemple résolu · Homme, 75 kg, 178 cm, 28 ans, activité modérée"},
    "TMB = 750 + 1.112 − 140 + 5 = <strong>1.727 kcal</strong> · Mantenimiento = 1.727 × 1,55 = <strong>2.680 kcal</strong><br>\n        Objetivo = 2.680 + 350 = <strong>3.030 kcal</strong> · Proteína 150 g (600 kcal) · Grasas 68 g (612 kcal) · Carbohidratos (3.030 − 1.212) ÷ 4 = <strong>455 g</strong>": {
        "en": "BMR = 750 + 1,112 − 140 + 5 = <strong>1,727 kcal</strong> · Maintenance = 1,727 × 1.55 = <strong>2,680 kcal</strong><br>\n        Target = 2,680 + 350 = <strong>3,030 kcal</strong> · Protein 150 g (600 kcal) · Fats 68 g (612 kcal) · Carbohydrates (3,030 − 1,212) ÷ 4 = <strong>455 g</strong>",
        "fr": "MB = 750 + 1 112 − 140 + 5 = <strong>1 727 kcal</strong> · Maintenance = 1 727 × 1,55 = <strong>2 680 kcal</strong><br>\n        Objectif = 2 680 + 350 = <strong>3 030 kcal</strong> · Protéines 150 g (600 kcal) · Lipides 68 g (612 kcal) · Glucides (3 030 − 1 212) ÷ 4 = <strong>455 g</strong>"},
    "Tu tabla — rellénala y no la cambies en 4 semanas": {
        "en": "Your table — fill it in and leave it alone for 4 weeks",
        "fr": "Votre tableau — remplissez-le et n'y touchez plus pendant 4 semaines"},
    "Dato": {"en": "Figure", "fr": "Donnée"},
    "Valor": {"en": "Value", "fr": "Valeur"},
    "Peso (kg)": {"en": "Weight (kg)", "fr": "Poids (kg)"},
    "TMB": {"en": "BMR", "fr": "MB"},
    "Altura (cm)": {"en": "Height (cm)", "fr": "Taille (cm)"},
    "Mantenimiento": {"en": "Maintenance", "fr": "Maintenance"},
    "Edad": {"en": "Age", "fr": "Âge"},
    "Kcal objetivo": {"en": "Target kcal", "fr": "Kcal cibles"},
    "Factor actividad": {"en": "Activity factor", "fr": "Facteur d'activité"},
    "Proteína / Grasas / Carbos": {
        "en": "Protein / Fats / Carbs", "fr": "Protéines / Lipides / Glucides"},

    # ── 03 · Menús ────────────────────────────────────────────────────
    "03 · Menús": {"en": "03 · Menus", "fr": "03 · Menus"},
    'EL DÍA, <span class="a">MOMENTO A MOMENTO</span>': {
        "en": 'THE DAY, <span class="a">MEAL BY MEAL</span>',
        "fr": 'LA JOURNÉE, <span class="a">MOMENT PAR MOMENT</span>'},
    "Tres opciones intercambiables por momento del día: las tres aportan un aporte proteico equivalente.": {
        "en": "Three interchangeable options for each point in the day: all three deliver an equivalent protein load.",
        "fr": "Trois options interchangeables par moment de la journée : toutes apportent autant de protéines."},
    "Momento": {"en": "Moment", "fr": "Moment"},
    "Opción A": {"en": "Option A", "fr": "Option A"},
    "Opción B": {"en": "Option B", "fr": "Option B"},
    "Opción C": {"en": "Option C", "fr": "Option C"},
    'Desayuno<br><span class="muted small">07:00</span>': {
        "en": 'Breakfast<br><span class="muted small">07:00</span>',
        "fr": 'Petit-déjeuner<br><span class="muted small">07:00</span>'},
    "Avena 80 g + 3 huevos": {"en": "Oats 80 g + 3 eggs", "fr": "Flocons d'avoine 80 g + 3 œufs"},
    "Tortilla + tostada integral": {
        "en": "Omelette + wholegrain toast", "fr": "Omelette + tartine complète"},
    "Batido de proteína + fruta + frutos secos": {
        "en": "Protein shake + fruit + nuts", "fr": "Shake protéiné + fruit + fruits secs"},
    'Pre-entreno<br><span class="muted small">12:00</span>': {
        "en": 'Pre-workout<br><span class="muted small">12:00</span>',
        "fr": 'Avant séance<br><span class="muted small">12:00</span>'},
    "Arroz 150 g + pollo 180 g": {"en": "Rice 150 g + chicken 180 g", "fr": "Riz 150 g + poulet 180 g"},
    "Pasta 130 g + atún": {"en": "Pasta 130 g + tuna", "fr": "Pâtes 130 g + thon"},
    "Boniato 250 g + pechuga": {
        "en": "Sweet potato 250 g + chicken breast", "fr": "Patate douce 250 g + blanc de poulet"},
    'Post-entreno<br><span class="muted small">15:00</span>': {
        "en": 'Post-workout<br><span class="muted small">15:00</span>',
        "fr": 'Après séance<br><span class="muted small">15:00</span>'},
    "Batido de proteína + plátano": {
        "en": "Protein shake + banana", "fr": "Shake protéiné + banane"},
    "Arroz + pollo + fruta": {"en": "Rice + chicken + fruit", "fr": "Riz + poulet + fruit"},
    "Avena + proteína + miel": {"en": "Oats + protein + honey", "fr": "Avoine + protéines + miel"},
    'Cena<br><span class="muted small">19:30</span>': {
        "en": 'Dinner<br><span class="muted small">19:30</span>',
        "fr": 'Dîner<br><span class="muted small">19:30</span>'},
    "Salmón + verduras + quinoa": {
        "en": "Salmon + vegetables + quinoa", "fr": "Saumon + légumes + quinoa"},
    "Ternera + ensalada": {"en": "Beef + salad", "fr": "Bœuf + salade"},
    "Pollo + brócoli + arroz": {"en": "Chicken + broccoli + rice", "fr": "Poulet + brocoli + riz"},
    'Pre-cama<br><span class="muted small">22:00</span>': {
        "en": 'Before bed<br><span class="muted small">22:00</span>',
        "fr": 'Avant le coucher<br><span class="muted small">22:00</span>'},
    "Requesón + almendras": {"en": "Cottage cheese + almonds", "fr": "Fromage blanc + amandes"},
    "Yogur griego + frutos secos": {
        "en": "Greek yoghurt + nuts", "fr": "Yaourt grec + fruits secs"},
    "Caseína + leche": {"en": "Casein + milk", "fr": "Caséine + lait"},
    "Reparto de la proteína a lo largo del día": {
        "en": "How protein is spread across the day",
        "fr": "Répartition des protéines sur la journée"},
    "Con un objetivo de 150 g diarios, la distribución que maximiza la síntesis proteica es esta. Concentrar 100 g en la cena no sirve de nada.": {
        "en": "With a 150 g daily target, this is the distribution that maximises protein synthesis. Cramming 100 g into dinner achieves nothing.",
        "fr": "Avec 150 g par jour, voici la répartition qui maximise la synthèse protéique. Concentrer 100 g au dîner ne sert à rien."},
    "desayuno": {"en": "breakfast", "fr": "petit-déjeuner"},
    "pre-entreno": {"en": "pre-workout", "fr": "avant séance"},
    "post-entreno": {"en": "post-workout", "fr": "après séance"},
    "cena / pre-cama": {"en": "dinner / before bed", "fr": "dîner / avant le coucher"},
    "Tabla de intercambios rápidos": {
        "en": "Quick swap table", "fr": "Tableau d'équivalences rapides"},
    "Si no tienes…": {"en": "If you have no…", "fr": "Si vous n'avez pas…"},
    "Cámbialo por…": {"en": "Swap it for…", "fr": "Remplacez par…"},
    "Equivalencia": {"en": "Equivalence", "fr": "Équivalence"},
    "Arroz 100 g (crudo)": {"en": "Rice 100 g (dry)", "fr": "Riz 100 g (cru)"},
    "Pasta 100 g · Boniato 340 g · Patata 400 g": {
        "en": "Pasta 100 g · Sweet potato 340 g · Potato 400 g",
        "fr": "Pâtes 100 g · Patate douce 340 g · Pomme de terre 400 g"},
    "≈ 75 g de carbohidrato": {"en": "≈ 75 g of carbohydrate", "fr": "≈ 75 g de glucides"},
    "Pechuga de pollo 150 g": {"en": "Chicken breast 150 g", "fr": "Blanc de poulet 150 g"},
    "Pavo 150 g · Atún 160 g · Merluza 190 g": {
        "en": "Turkey 150 g · Tuna 160 g · Hake 190 g",
        "fr": "Dinde 150 g · Thon 160 g · Merlu 190 g"},
    "≈ 33 g de proteína": {"en": "≈ 33 g of protein", "fr": "≈ 33 g de protéines"},
    "1 scoop de proteína": {"en": "1 scoop of protein", "fr": "1 dose de protéines"},
    "3 claras + 1 huevo · 200 g de yogur griego": {
        "en": "3 egg whites + 1 egg · 200 g Greek yoghurt",
        "fr": "3 blancs + 1 œuf · 200 g de yaourt grec"},
    "≈ 24 g de proteína": {"en": "≈ 24 g of protein", "fr": "≈ 24 g de protéines"},
    "Aceite de oliva 10 g": {"en": "Olive oil 10 g", "fr": "Huile d'olive 10 g"},
    "Aguacate 55 g · Almendras 15 g": {
        "en": "Avocado 55 g · Almonds 15 g", "fr": "Avocat 55 g · Amandes 15 g"},
    "≈ 9 g de grasa": {"en": "≈ 9 g of fat", "fr": "≈ 9 g de lipides"},
    "Avena 80 g": {"en": "Oats 80 g", "fr": "Flocons d'avoine 80 g"},
    "Pan integral 100 g · Copos de maíz sin azúcar 70 g": {
        "en": "Wholegrain bread 100 g · Unsweetened cornflakes 70 g",
        "fr": "Pain complet 100 g · Pétales de maïs sans sucre 70 g"},
    "≈ 48 g de carbohidrato": {"en": "≈ 48 g of carbohydrate", "fr": "≈ 48 g de glucides"},
    "<b>Fig. 1</b>Porciones sin báscula": {
        "en": "<b>Fig. 1</b>Portions without scales",
        "fr": "<b>Fig. 1</b>Des portions sans balance"},
    "Cada medida usa <b>tu</b> mano, así que se escala sola a tu tamaño corporal. Es el método para los días que comes fuera.": {
        "en": "Every measure uses <b>your</b> hand, so it scales itself to your body size. This is the method for days when you eat out.",
        "fr": "Chaque mesure utilise <b>votre</b> main : elle s'ajuste donc à votre corpulence. La méthode des jours où vous mangez dehors."},

    # ── 04 · Errores ──────────────────────────────────────────────────
    "04 · Errores": {"en": "04 · Mistakes", "fr": "04 · Erreurs"},
    'LOS 8 ERRORES QUE <span class="a">FRENAN TU PROGRESO</span>': {
        "en": 'THE 8 MISTAKES THAT <span class="a">STALL YOUR PROGRESS</span>',
        "fr": 'LES 8 ERREURS QUI <span class="a">FREINENT VOS PROGRÈS</span>'},
    "Error": {"en": "Mistake", "fr": "Erreur"},
    "Qué provoca": {"en": "What it causes", "fr": "Ce qu'elle provoque"},
    "Corrección": {"en": "Fix", "fr": "Correction"},
    "Cambiar las calorías cada semana": {
        "en": "Changing calories every week", "fr": "Changer les calories chaque semaine"},
    "Nunca sabes qué funcionaba porque nunca das tiempo a verlo": {
        "en": "You never know what was working because you never give it time to show",
        "fr": "Vous ne savez jamais ce qui marchait, faute de lui laisser le temps de se voir"},
    "Mantén los números 2–3 semanas antes de tocar nada": {
        "en": "Hold the numbers for 2–3 weeks before touching anything",
        "fr": "Gardez les chiffres 2–3 semaines avant d'y toucher"},
    "Pesarte un solo día": {"en": "Weighing yourself on one day", "fr": "Se peser un seul jour"},
    "El agua y el glucógeno mueven ±1,5 kg sin que cambie tu grasa": {
        "en": "Water and glycogen swing ±1.5 kg without your fat changing at all",
        "fr": "L'eau et le glycogène font varier ±1,5 kg sans que votre masse grasse bouge"},
    "Pésate a diario en ayunas y compara promedios semanales": {
        "en": "Weigh in daily, fasted, and compare weekly averages",
        "fr": "Pesez-vous chaque jour à jeun et comparez les moyennes hebdomadaires"},
    "No registrar el aceite y las salsas": {
        "en": "Not logging oil and sauces", "fr": "Ne pas comptabiliser l'huile et les sauces"},
    "300–500 kcal invisibles al día: el superávit se duplica": {
        "en": "300–500 invisible kcal a day: the surplus doubles",
        "fr": "300–500 kcal invisibles par jour : le surplus double"},
    "Pesa la grasa de cocinado durante las primeras 4 semanas": {
        "en": "Weigh your cooking fat for the first 4 weeks",
        "fr": "Pesez la matière grasse de cuisson les 4 premières semaines"},
    "Entrenar sin registro de cargas": {
        "en": "Training with no load logbook", "fr": "S'entraîner sans carnet de charges"},
    "Sin sobrecarga progresiva, el superávit solo produce grasa": {
        "en": "Without progressive overload, the surplus only produces fat",
        "fr": "Sans surcharge progressive, le surplus ne produit que de la graisse"},
    "Anota series, repeticiones y peso de cada sesión": {
        "en": "Write down sets, reps and weight for every session",
        "fr": "Notez séries, répétitions et charge de chaque séance"},
    "Copiar la dieta de otra persona": {
        "en": "Copying someone else's diet", "fr": "Copier le régime de quelqu'un d'autre"},
    "Sus calorías corresponden a su peso, su altura y su gasto": {
        "en": "Their calories match their weight, their height and their expenditure",
        "fr": "Ses calories correspondent à son poids, sa taille et sa dépense"},
    "Usa la calculadora de la página 4 con tus propios datos": {
        "en": "Use the calculator on page 4 with your own figures",
        "fr": "Utilisez le calculateur de la page 4 avec vos propres données"},
    "Cardio excesivo «por si acaso»": {
        "en": "Excessive cardio «just in case»", "fr": "Trop de cardio « au cas où »"},
    "Se come el superávit que tanto te cuesta generar": {
        "en": "It eats the surplus you work so hard to create",
        "fr": "Il mange le surplus que vous avez tant de mal à créer"},
    "Máximo 2 sesiones LISS de 20–30 min por semana": {
        "en": "No more than 2 LISS sessions of 20–30 min per week",
        "fr": "Au maximum 2 séances LISS de 20–30 min par semaine"},
    "Dormir 5–6 horas": {"en": "Sleeping 5–6 hours", "fr": "Dormir 5–6 heures"},
    "Menos testosterona, menos recuperación, más apetito": {
        "en": "Less testosterone, less recovery, more appetite",
        "fr": "Moins de testostérone, moins de récupération, plus d'appétit"},
    "Trata las 7–9 h como parte del plan, no como un lujo": {
        "en": "Treat 7–9 h as part of the plan, not as a luxury",
        "fr": "Traitez les 7–9 h comme une partie du plan, pas comme un luxe"},
    "Abandonar en la semana 3": {"en": "Quitting in week 3", "fr": "Abandonner en semaine 3"},
    "Los cambios visibles empiezan entre la semana 6 y la 8": {
        "en": "Visible change starts between week 6 and week 8",
        "fr": "Les changements visibles commencent entre la semaine 6 et la 8"},
    "Comprométete a 12 semanas antes de juzgar resultados": {
        "en": "Commit to 12 weeks before judging results",
        "fr": "Engagez-vous sur 12 semaines avant de juger des résultats"},
    "La regla de oro del ajuste": {
        "en": "The golden rule of adjustment", "fr": "La règle d'or de l'ajustement"},
    "Lo que marca la báscula en 2 semanas": {
        "en": "What the scale shows over 2 weeks",
        "fr": "Ce qu'indique la balance en 2 semaines"},
    "Qué significa": {"en": "What it means", "fr": "Ce que cela signifie"},
    "Qué haces": {"en": "What you do", "fr": "Ce que vous faites"},
    "Menos de +0,3 kg": {"en": "Less than +0.3 kg", "fr": "Moins de +0,3 kg"},
    "El superávit es insuficiente": {
        "en": "The surplus is too small", "fr": "Le surplus est insuffisant"},
    '<span class="tag ok">Suma 200 kcal</span> de carbohidratos': {
        "en": '<span class="tag ok">Add 200 kcal</span> of carbohydrate',
        "fr": '<span class="tag ok">Ajoutez 200 kcal</span> de glucides'},
    "Entre +0,3 y +1,0 kg": {"en": "Between +0.3 and +1.0 kg", "fr": "Entre +0,3 et +1,0 kg"},
    "Estás en el rango óptimo": {
        "en": "You are in the optimal range", "fr": "Vous êtes dans la fourchette optimale"},
    '<span class="tag lo">No cambies nada</span>': {
        "en": '<span class="tag lo">Change nothing</span>',
        "fr": '<span class="tag lo">Ne changez rien</span>'},
    "Más de +1,0 kg": {"en": "More than +1.0 kg", "fr": "Plus de +1,0 kg"},
    "Estás ganando grasa de más": {
        "en": "You are gaining excess fat", "fr": "Vous prenez trop de graisse"},
    '<span class="tag hi">Resta 200 kcal</span> de carbohidratos': {
        "en": '<span class="tag hi">Cut 200 kcal</span> of carbohydrate',
        "fr": '<span class="tag hi">Retirez 200 kcal</span> de glucides'},
    "Condiciones de medición constantes": {
        "en": "Keep measurement conditions constant",
        "fr": "Conditions de mesure constantes"},
    "Siempre el mismo día (lunes), a la misma hora (nada más levantarte), después de ir al baño, en ayunas y sin ropa. Cambiar las condiciones invalida la comparación.": {
        "en": "Always the same day (Monday), at the same time (as soon as you get up), after using the bathroom, fasted and without clothes. Changing the conditions invalidates the comparison.",
        "fr": "Toujours le même jour (lundi), à la même heure (dès le lever), après être passé aux toilettes, à jeun et sans vêtements. Changer les conditions invalide la comparaison."},

    # ── 05 · Siguiente paso ───────────────────────────────────────────
    "05 · Tu siguiente paso": {"en": "05 · Your next step", "fr": "05 · Votre étape suivante"},
    'CHECKLIST <span class="a">DE CADA LUNES</span>': {
        "en": 'YOUR <span class="a">MONDAY CHECKLIST</span>',
        "fr": 'CHECK-LIST <span class="a">DE CHAQUE LUNDI</span>'},
    "Peso en ayunas anotado y promedio semanal calculado": {
        "en": "Fasted weight logged and weekly average worked out",
        "fr": "Poids à jeun noté et moyenne hebdomadaire calculée"},
    "Perímetro de cintura medido a la altura del ombligo": {
        "en": "Waist measured at navel height",
        "fr": "Tour de taille mesuré à hauteur du nombril"},
    "Cargas de la semana revisadas: ¿ha subido algo?": {
        "en": "This week's loads reviewed: has anything gone up?",
        "fr": "Charges de la semaine revues : quelque chose a-t-il augmenté ?"},
    'Días con la proteína completa: <span class="fill" style="min-width:14mm"></span> de 7': {
        "en": 'Days with protein fully covered: <span class="fill" style="min-width:14mm"></span> of 7',
        "fr": 'Jours avec les protéines couvertes : <span class="fill" style="min-width:14mm"></span> sur 7'},
    'Media de horas de sueño: <span class="fill" style="min-width:14mm"></span>': {
        "en": 'Average hours of sleep: <span class="fill" style="min-width:14mm"></span>',
        "fr": 'Moyenne d\'heures de sommeil : <span class="fill" style="min-width:14mm"></span>'},
    "Litros de agua diarios cumplidos": {
        "en": "Daily litres of water met", "fr": "Litres d'eau quotidiens atteints"},
    "Foto de progreso con la misma luz y postura": {
        "en": "Progress photo in the same light and pose",
        "fr": "Photo de progression avec la même lumière et la même posture"},
    "Decisión tomada: mantener, sumar o restar 200 kcal": {
        "en": "Decision made: hold, add or cut 200 kcal",
        "fr": "Décision prise : maintenir, ajouter ou retirer 200 kcal"},
    "Registro rápido de las 4 primeras semanas": {
        "en": "Quick log for the first 4 weeks",
        "fr": "Registre rapide des 4 premières semaines"},
    "Semana": {"en": "Week", "fr": "Semaine"},
    "Peso medio": {"en": "Average weight", "fr": "Poids moyen"},
    "Cintura": {"en": "Waist", "fr": "Taille"},
    "Kcal aplicadas": {"en": "Kcal applied", "fr": "Kcal appliquées"},
    "Decisión": {"en": "Decision", "fr": "Décision"},
    "Semana 1": {"en": "Week 1", "fr": "Semaine 1"},
    "Semana 2": {"en": "Week 2", "fr": "Semaine 2"},
    "Semana 3": {"en": "Week 3", "fr": "Semaine 3"},
    "Semana 4": {"en": "Week 4", "fr": "Semaine 4"},
    "Has dominado los principios. El plan <strong>PRO</strong> convierte estos\n        principios en un protocolo de 8 semanas con ciclado de carbohidratos, suplementación y\n        seguimiento medido.": {
        "en": "You have mastered the principles. The <strong>PRO</strong> plan turns them into an 8-week protocol with carb cycling, supplementation and measured tracking.",
        "fr": "Vous maîtrisez les principes. La formule <strong>PRO</strong> les transforme en un protocole de 8 semaines avec cyclage des glucides, compléments et suivi mesuré."},
}
