# -*- coding: utf-8 -*-
"""
PLAN 02 · PRO — Ciclado de carbohidratos
========================================
Los gramos por kilo y las kilocalorías no se tocan al traducir: son el
protocolo. Sí se adapta el separador decimal y el de millares, que difieren
entre las tres lenguas.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Protocolo avanzado</small>\n        <span class="glow">CICLADO DE<br>CARBOHIDRATOS</span>': {
        "en": '<small>Advanced protocol</small>\n        <span class="glow">CARBOHYDRATE<br>CYCLING</span>',
        "fr": '<small>Protocole avancé</small>\n        <span class="glow">CYCLAGE DES<br>GLUCIDES</span>'},
    "Alterna alto, medio y bajo según tu entrenamiento para mejorar\n        composición corporal <em>sin</em> perder rendimiento.": {
        "en": "Alternate high, medium and low with your training to improve body composition <em>without</em> losing performance.",
        "fr": "Alternez haut, moyen et bas selon votre entraînement pour améliorer la composition corporelle <em>sans</em> perdre en performance."},
    '<span class="chip on">4 semanas</span>\n        <span class="chip on">Gramos por kg</span>\n        <span class="chip">3 menús completos</span>\n        <span class="chip">Recargas</span>': {
        "en": '<span class="chip on">4 weeks</span>\n        <span class="chip on">Grams per kg</span>\n        <span class="chip">3 full menus</span>\n        <span class="chip">Refeeds</span>',
        "fr": '<span class="chip on">4 semaines</span>\n        <span class="chip on">Grammes par kg</span>\n        <span class="chip">3 menus complets</span>\n        <span class="chip">Recharges</span>'},
    "Tipos de día": {"en": "Day types", "fr": "Types de jour"},
    "Comidas detalladas": {"en": "Detailed meals", "fr": "Repas détaillés"},
    '<strong>Edición 2026</strong><br>\n        <span class="muted">Protocolo nutricional avanzado · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br>\n        <span class="muted">Advanced nutrition protocol · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br>\n        <span class="muted">Protocole nutritionnel avancé · 8 pages</span>'},

    # ── 01 · Qué es ───────────────────────────────────────────────────
    'QUÉ ES EL <span class="a">CICLADO DE CARBOHIDRATOS</span>': {
        "en": 'WHAT <span class="a">CARBOHYDRATE CYCLING</span> IS',
        "fr": "CE QU'EST LE <span class=\"a\">CYCLAGE DES GLUCIDES</span>"},
    "Es una estrategia que <strong>alterna la ingesta de carbohidratos</strong> según la demanda real de cada día: mucho combustible cuando entrenas fuerte, poco cuando descansas. Ni magia ni metabolismo acelerado — simplemente poner la energía donde hace falta.": {
        "en": "It is a strategy that <strong>alternates carbohydrate intake</strong> with each day's real demand: plenty of fuel when you train hard, little when you rest. No magic and no accelerated metabolism — simply putting the energy where it is needed.",
        "fr": "C'est une stratégie qui <strong>alterne l'apport en glucides</strong> selon la demande réelle de chaque jour : beaucoup de carburant quand vous vous entraînez dur, peu quand vous vous reposez. Ni magie ni métabolisme accéléré — simplement mettre l'énergie là où elle sert."},
    "Para quién SÍ funciona": {"en": "Who it DOES work for", "fr": "Pour qui ça marche"},
    "Tienes al menos 6 meses de entrenamiento constante": {
        "en": "You have at least 6 months of consistent training",
        "fr": "Vous avez au moins 6 mois d'entraînement régulier"},
    "Ya sabes contar macros y pesar alimentos": {
        "en": "You already know how to count macros and weigh food",
        "fr": "Vous savez déjà compter les macros et peser les aliments"},
    "Buscas definir sin perder fuerza en los básicos": {
        "en": "You want to cut without losing strength on the main lifts",
        "fr": "Vous voulez sécher sans perdre en force sur les mouvements de base"},
    "Tu semana tiene días claramente distintos en intensidad": {
        "en": "Your week has clearly different days in terms of intensity",
        "fr": "Votre semaine comporte des jours d'intensité nettement différente"},
    "Para quién NO todavía": {"en": "Who it is NOT for yet", "fr": "Pour qui ce n'est pas encore"},
    "Estás empezando: primero domina el superávit o déficit simple": {
        "en": "You are starting out: master a plain surplus or deficit first",
        "fr": "Vous débutez : maîtrisez d'abord un surplus ou un déficit simple"},
    "No registras lo que comes con precisión": {
        "en": "You do not log what you eat accurately",
        "fr": "Vous ne notez pas précisément ce que vous mangez"},
    "Tienes antecedentes de trastorno de conducta alimentaria": {
        "en": "You have a history of eating disorders",
        "fr": "Vous avez des antécédents de trouble du comportement alimentaire"},
    "Tu horario cambia cada semana y no puedes planificar": {
        "en": "Your schedule changes every week and you cannot plan",
        "fr": "Votre emploi du temps change chaque semaine et vous ne pouvez pas planifier"},
    "Los tres tipos de día": {"en": "The three day types", "fr": "Les trois types de jour"},
    "Tipo de día": {"en": "Day type", "fr": "Type de jour"},
    "Calorías aprox.": {"en": "Approx. calories", "fr": "Calories approx."},
    "Cuándo aplicarlo": {"en": "When to use it", "fr": "Quand l'appliquer"},
    '<span class="tag hi">Alto · A</span>': {
        "en": '<span class="tag hi">High · H</span>',
        "fr": '<span class="tag hi">Haut · H</span>'},
    '<span class="tag mid">Medio · M</span>': {
        "en": '<span class="tag mid">Medium · M</span>',
        "fr": '<span class="tag mid">Moyen · M</span>'},
    '<span class="tag lo">Bajo · B</span>': {
        "en": '<span class="tag lo">Low · L</span>',
        "fr": '<span class="tag lo">Bas · B</span>'},
    "Entrenamiento pesado: piernas o espalda": {
        "en": "Heavy training: legs or back", "fr": "Entraînement lourd : jambes ou dos"},
    "Entrenamiento moderado: tren superior": {
        "en": "Moderate training: upper body", "fr": "Entraînement modéré : haut du corps"},
    "Descanso o cardio ligero (LISS)": {
        "en": "Rest or light cardio (LISS)", "fr": "Repos ou cardio léger (LISS)"},
    "Los valores de la tabla corresponden a un atleta de referencia de 75 kg. En la página 3 los conviertes a <strong>tu</strong> peso corporal.": {
        "en": "The table values are for a reference athlete of 75 kg. On page 3 you convert them to <strong>your</strong> body weight.",
        "fr": "Les valeurs du tableau correspondent à un athlète de référence de 75 kg. Page 3, vous les convertissez à <strong>votre</strong> poids corporel."},
    "Por qué funciona": {"en": "Why it works", "fr": "Pourquoi ça marche"},
    "<strong>Sensibilidad a la insulina:</strong> tras un entreno duro el músculo capta glucosa con mucha más eficiencia. Los carbohidratos del día alto van al glucógeno, no al tejido graso.": {
        "en": "<strong>Insulin sensitivity:</strong> after a hard session, muscle takes up glucose far more efficiently. The high day's carbohydrates go to glycogen, not to fat tissue.",
        "fr": "<strong>Sensibilité à l'insuline :</strong> après une séance dure, le muscle capte le glucose bien plus efficacement. Les glucides du jour haut vont au glycogène, pas au tissu adipeux."},
    "<strong>Rendimiento protegido:</strong> los días exigentes llegan con los depósitos llenos, así que mantienes las cargas mientras el promedio semanal queda en déficit.": {
        "en": "<strong>Performance protected:</strong> the demanding days arrive with full stores, so you keep your loads while the weekly average stays in deficit.",
        "fr": "<strong>Performance protégée :</strong> les jours exigeants arrivent avec les réserves pleines, donc vous conservez vos charges pendant que la moyenne hebdomadaire reste en déficit."},
    "<strong>Adherencia:</strong> psicológicamente es mucho más llevadero que un déficit plano y monótono durante ocho semanas.": {
        "en": "<strong>Adherence:</strong> psychologically it is far easier to live with than a flat, monotonous deficit for eight weeks.",
        "fr": "<strong>Observance :</strong> psychologiquement, c'est bien plus tenable qu'un déficit plat et monotone pendant huit semaines."},
    "Lo que el ciclado NO hace": {"en": "What cycling does NOT do", "fr": "Ce que le cyclage NE fait PAS"},
    "No quema grasa por sí mismo. La pérdida de grasa sigue dependiendo del <strong>balance calórico semanal</strong>. El ciclado solo reparte mejor esas calorías para que rindas más y conserves músculo mientras el balance hace su trabajo.": {
        "en": "It does not burn fat by itself. Fat loss still depends on the <strong>weekly calorie balance</strong>. Cycling merely distributes those calories better so that you perform more and keep muscle while the balance does its work.",
        "fr": "Il ne brûle pas de graisse par lui-même. La perte de gras dépend toujours de la <strong>balance calorique hebdomadaire</strong>. Le cyclage ne fait que mieux répartir ces calories pour que vous performiez davantage et gardiez du muscle pendant que la balance fait son travail."},

    # ── 02 · A tu peso ────────────────────────────────────────────────
    'CONVIERTE EL PROTOCOLO A <span class="a">TU PESO</span>': {
        "en": 'CONVERT THE PROTOCOL TO <span class="a">YOUR WEIGHT</span>',
        "fr": 'CONVERTISSEZ LE PROTOCOLE À <span class="a">VOTRE POIDS</span>'},
    "Las cifras genéricas solo sirven a quien pesa exactamente lo mismo que el atleta de referencia. Estas son las proporciones reales del protocolo: multiplícalas por tus kilos y tendrás tu propia versión.": {
        "en": "Generic figures only serve someone who weighs exactly the same as the reference athlete. These are the protocol's real ratios: multiply them by your kilos and you have your own version.",
        "fr": "Les chiffres génériques ne servent qu'à qui pèse exactement comme l'athlète de référence. Voici les vraies proportions du protocole : multipliez-les par vos kilos et vous obtenez votre propre version."},
    "Lógica": {"en": "Logic", "fr": "Logique"},
    '<span class="tag hi">Alto</span>': {
        "en": '<span class="tag hi">High</span>', "fr": '<span class="tag hi">Haut</span>'},
    '<span class="tag mid">Medio</span>': {
        "en": '<span class="tag mid">Medium</span>', "fr": '<span class="tag mid">Moyen</span>'},
    '<span class="tag lo">Bajo</span>': {
        "en": '<span class="tag lo">Low</span>', "fr": '<span class="tag lo">Bas</span>'},
    "4,5–5,5 g/kg": {"en": "4.5–5.5 g/kg", "fr": "4,5–5,5 g/kg"},
    "2,2 g/kg": {"en": "2.2 g/kg", "fr": "2,2 g/kg"},
    "0,8 g/kg": {"en": "0.8 g/kg", "fr": "0,8 g/kg"},
    "3,0–3,5 g/kg": {"en": "3.0–3.5 g/kg", "fr": "3,0–3,5 g/kg"},
    "2,4 g/kg": {"en": "2.4 g/kg", "fr": "2,4 g/kg"},
    "1,0 g/kg": {"en": "1.0 g/kg", "fr": "1,0 g/kg"},
    "1,0–1,5 g/kg": {"en": "1.0–1.5 g/kg", "fr": "1,0–1,5 g/kg"},
    "2,6 g/kg": {"en": "2.6 g/kg", "fr": "2,6 g/kg"},
    "1,2 g/kg": {"en": "1.2 g/kg", "fr": "1,2 g/kg"},
    "Carbos altos, grasa baja": {"en": "High carbs, low fat", "fr": "Glucides hauts, lipides bas"},
    "Punto de equilibrio": {"en": "The balance point", "fr": "Le point d'équilibre"},
    "Grasa sube, proteína protege el músculo": {
        "en": "Fat rises, protein protects the muscle",
        "fr": "Les lipides montent, les protéines protègent le muscle"},
    "Regla clave del protocolo": {"en": "The protocol's key rule", "fr": "La règle clé du protocole"},
    "La proteína <strong>sube</strong> cuando bajan los carbohidratos y las grasas hacen lo contrario que los carbos. Así las calorías no se desploman en los días bajos y proteges la masa muscular justo cuando más riesgo hay de perderla.": {
        "en": "Protein <strong>rises</strong> when carbohydrates fall, and fats do the opposite of carbs. That way calories do not collapse on low days and you protect muscle mass exactly when the risk of losing it is highest.",
        "fr": "Les protéines <strong>montent</strong> quand les glucides baissent, et les lipides font l'inverse des glucides. Ainsi les calories ne s'effondrent pas les jours bas et vous protégez la masse musculaire au moment où le risque de la perdre est le plus grand."},
    "Ejemplo resuelto · Atleta de 75 kg": {
        "en": "Worked example · 75 kg athlete", "fr": "Exemple résolu · Athlète de 75 kg"},
    "Calorías": {"en": "Calories", "fr": "Calories"},
    "Alto (5,0 g/kg)": {"en": "High (5.0 g/kg)", "fr": "Haut (5,0 g/kg)"},
    "Medio (3,2 g/kg)": {"en": "Medium (3.2 g/kg)", "fr": "Moyen (3,2 g/kg)"},
    "Bajo (1,3 g/kg)": {"en": "Low (1.3 g/kg)", "fr": "Bas (1,3 g/kg)"},
    "Media semanal (3 A · 2 M · 2 B)": {
        "en": "Weekly average (3 H · 2 M · 2 L)", "fr": "Moyenne hebdo (3 H · 2 M · 2 B)"},
    "2.386 kcal": {"en": "2,386 kcal", "fr": "2 386 kcal"},
    "Tu tabla — calcúlala una vez y trabaja con ella 4 semanas": {
        "en": "Your table — work it out once and use it for 4 weeks",
        "fr": "Votre tableau — calculez-le une fois et gardez-le 4 semaines"},
    'Carbos (g/kg × <span class="fill" style="min-width:16mm"></span> kg)': {
        "en": 'Carbs (g/kg × <span class="fill" style="min-width:16mm"></span> kg)',
        "fr": 'Glucides (g/kg × <span class="fill" style="min-width:16mm"></span> kg)'},
    "Medio": {"en": "Medium", "fr": "Moyen"},
    "Bajo": {"en": "Low", "fr": "Bas"},
    "Recuerda: 1 g de carbohidrato = 4 kcal · 1 g de proteína = 4 kcal · 1 g de grasa = 9 kcal. La fibra ya está incluida en el cómputo de carbohidratos.": {
        "en": "Remember: 1 g of carbohydrate = 4 kcal · 1 g of protein = 4 kcal · 1 g of fat = 9 kcal. Fibre is already included in the carbohydrate count.",
        "fr": "Rappel : 1 g de glucides = 4 kcal · 1 g de protéines = 4 kcal · 1 g de lipides = 9 kcal. Les fibres sont déjà comptées dans les glucides."},

    # ── 03 · Calendario ───────────────────────────────────────────────
    "03 · Calendario": {"en": "03 · Calendar", "fr": "03 · Calendrier"},
    'CALENDARIO DE <span class="a">4 SEMANAS</span>': {
        "en": '<span class="a">4-WEEK</span> CALENDAR',
        "fr": 'CALENDRIER DE <span class="a">4 SEMAINES</span>'},
    "Adapta el patrón a TU semana, no al revés": {
        "en": "Adapt the pattern to YOUR week, not the other way round",
        "fr": "Adaptez le schéma à VOTRE semaine, pas l'inverse"},
    "Este calendario asume entrenar lunes, miércoles y viernes en pesado. Si tu día de piernas es el martes, mueve el día ALTO al martes. La regla que nunca cambia es: <strong>día alto = día de mayor volumen de entrenamiento</strong>.": {
        "en": "This calendar assumes heavy training on Monday, Wednesday and Friday. If your leg day is Tuesday, move the HIGH day to Tuesday. The rule that never changes is: <strong>high day = day of greatest training volume</strong>.",
        "fr": "Ce calendrier suppose un entraînement lourd le lundi, le mercredi et le vendredi. Si votre jour de jambes est le mardi, déplacez le jour HAUT au mardi. La règle qui ne change jamais : <strong>jour haut = jour de plus grand volume d'entraînement</strong>."},
    "Cómo emparejar cada día con tu entrenamiento": {
        "en": "How to pair each day with your training",
        "fr": "Comment associer chaque jour à votre entraînement"},
    "Tu sesión": {"en": "Your session", "fr": "Votre séance"},
    "Reparto de los carbohidratos": {
        "en": "How the carbohydrates are split", "fr": "Répartition des glucides"},
    "Piernas o espalda pesado": {"en": "Heavy legs or back", "fr": "Jambes ou dos lourds"},
    "50 % antes del entreno · 30 % después · 20 % resto del día": {
        "en": "50 % before training · 30 % after · 20 % rest of the day",
        "fr": "50 % avant la séance · 30 % après · 20 % le reste de la journée"},
    "Pecho, hombro o brazos": {"en": "Chest, shoulders or arms", "fr": "Pectoraux, épaules ou bras"},
    "40 % antes · 30 % después · 30 % resto": {
        "en": "40 % before · 30 % after · 30 % rest", "fr": "40 % avant · 30 % après · 30 % reste"},
    "Full body o híbrido": {"en": "Full body or hybrid", "fr": "Corps entier ou hybride"},
    "45 % antes · 35 % después · 20 % resto": {
        "en": "45 % before · 35 % after · 20 % rest", "fr": "45 % avant · 35 % après · 20 % reste"},
    "Cardio LISS o movilidad": {"en": "LISS cardio or mobility", "fr": "Cardio LISS ou mobilité"},
    "Reparto libre, prioriza verdura y proteína": {
        "en": "Split as you like, prioritise vegetables and protein",
        "fr": "Répartition libre, privilégiez légumes et protéines"},
    "Descanso completo": {"en": "Full rest", "fr": "Repos complet"},
    "Reparto libre, cena con más grasa para saciedad": {
        "en": "Split as you like, a fattier dinner for satiety",
        "fr": "Répartition libre, dîner plus gras pour la satiété"},
    "<b>Fig. 1</b>La semana de ciclado, de un vistazo": {
        "en": "<b>Fig. 1</b>The cycling week at a glance",
        "fr": "<b>Fig. 1</b>La semaine de cyclage en un coup d'œil"},
    "Altura de cada barra = gramos de carbohidrato por kilo de peso. Compara esta figura con la tabla de la página anterior antes de fijar tu propia semana.": {
        "en": "Each bar's height = grams of carbohydrate per kilo of body weight. Compare this figure with the table on the previous page before setting your own week.",
        "fr": "La hauteur de chaque barre = grammes de glucides par kilo de poids. Comparez cette figure au tableau de la page précédente avant de fixer votre propre semaine."},

    # ── 04 · Día alto ─────────────────────────────────────────────────
    "04 · Menú día alto": {"en": "04 · High-day menu", "fr": "04 · Menu jour haut"},
    'DÍA <span class="a">ALTO</span> EN CARBOHIDRATOS': {
        "en": '<span class="a">HIGH</span>-CARBOHYDRATE DAY',
        "fr": 'JOUR <span class="a">HAUT</span> EN GLUCIDES'},
    "carbohidratos": {"en": "carbohydrates", "fr": "glucides"},
    "proteína": {"en": "protein", "fr": "protéines"},
    "grasas": {"en": "fats", "fr": "lipides"},
    "kcal": {"en": "kcal", "fr": "kcal"},
    "Comida": {"en": "Meal", "fr": "Repas"},
    "Alimentos": {"en": "Foods", "fr": "Aliments"},
    "Avena 100 g + plátano + 3 claras": {
        "en": "Oats 100 g + banana + 3 egg whites",
        "fr": "Avoine 100 g + banane + 3 blancs d'œuf"},
    "Arroz 200 g cocido + pollo 200 g + tomate": {
        "en": "Cooked rice 200 g + chicken 200 g + tomato",
        "fr": "Riz cuit 200 g + poulet 200 g + tomate"},
    "Batido de proteína + arroz con leche 100 g": {
        "en": "Protein shake + rice pudding 100 g",
        "fr": "Shake protéiné + riz au lait 100 g"},
    "Pasta 150 g + salmón 180 g + ensalada": {
        "en": "Pasta 150 g + salmon 180 g + salad",
        "fr": "Pâtes 150 g + saumon 180 g + salade"},
    "Boniato 200 g + pechuga 180 g + verduras": {
        "en": "Sweet potato 200 g + chicken breast 180 g + vegetables",
        "fr": "Patate douce 200 g + blanc de poulet 180 g + légumes"},
    "Total del día": {"en": "Day total", "fr": "Total du jour"},
    "Timing del día alto": {"en": "High-day timing", "fr": "Timing du jour haut"},
    "Franja": {"en": "Window", "fr": "Créneau"},
    "Detalle práctico": {"en": "Practical detail", "fr": "Détail pratique"},
    "Llenar depósitos": {"en": "Fill the stores", "fr": "Remplir les réserves"},
    "La comida más grande en carbohidratos del día, con poca grasa para digerir rápido": {
        "en": "The day's biggest carbohydrate meal, low in fat so it digests fast",
        "fr": "Le repas le plus riche en glucides de la journée, peu gras pour digérer vite"},
    "Intra-entreno": {"en": "Intra-workout", "fr": "Pendant la séance"},
    "Sostener intensidad": {"en": "Hold the intensity", "fr": "Tenir l'intensité"},
    "Solo si la sesión supera 75 min: 30–40 g de carbohidrato líquido": {
        "en": "Only if the session runs over 75 min: 30–40 g of liquid carbohydrate",
        "fr": "Seulement si la séance dépasse 75 min : 30–40 g de glucides liquides"},
    "0–90 min después": {"en": "0–90 min after", "fr": "0–90 min après"},
    "Reponer glucógeno": {"en": "Replenish glycogen", "fr": "Reconstituer le glycogène"},
    "Carbohidrato de digestión rápida + 40 g de proteína": {
        "en": "Fast-digesting carbohydrate + 40 g of protein",
        "fr": "Glucides à digestion rapide + 40 g de protéines"},
    "Resto del día": {"en": "Rest of the day", "fr": "Reste de la journée"},
    "Completar el total": {"en": "Make up the total", "fr": "Compléter le total"},
    "Fuentes integrales, fruta y verdura para llegar a fibra y micronutrientes": {
        "en": "Wholegrain sources, fruit and vegetables to reach fibre and micronutrients",
        "fr": "Sources complètes, fruits et légumes pour atteindre fibres et micronutriments"},
    "<b>Fig. 2</b>La ventana peri-entreno del día alto": {
        "en": "<b>Fig. 2</b>The high day's peri-workout window",
        "fr": "<b>Fig. 2</b>La fenêtre péri-entraînement du jour haut"},
    "Los gramos están en g/kg de peso corporal, así que se escalan solos. La curva inferior es la razón de todo el protocolo.": {
        "en": "The grams are in g/kg of body weight, so they scale by themselves. The lower curve is the reason for the whole protocol.",
        "fr": "Les grammes sont en g/kg de poids corporel : ils s'adaptent d'eux-mêmes. La courbe du bas est la raison d'être de tout le protocole."},
    "Baja la grasa cuando suben los carbos": {
        "en": "Drop the fat when the carbs go up",
        "fr": "Baissez les lipides quand les glucides montent"},
    "El día alto no es un día de comer más de todo. Las grasas bajan a 0,8 g/kg precisamente para dejar espacio calórico a los carbohidratos. Si mantienes la grasa alta y además subes los carbos, has creado un superávit sin querer.": {
        "en": "The high day is not a day for eating more of everything. Fats drop to 0.8 g/kg precisely to make caloric room for the carbohydrates. If you keep fat high and raise carbs as well, you have created a surplus by accident.",
        "fr": "Le jour haut n'est pas un jour où l'on mange plus de tout. Les lipides descendent à 0,8 g/kg précisément pour laisser de la place calorique aux glucides. Si vous gardez les lipides hauts et montez aussi les glucides, vous avez créé un surplus sans le vouloir."},

    # ── 05 · Día medio ────────────────────────────────────────────────
    "05 · Menú día medio": {"en": "05 · Medium-day menu", "fr": "05 · Menu jour moyen"},
    'DÍA <span class="a">MEDIO</span> EN CARBOHIDRATOS': {
        "en": '<span class="a">MEDIUM</span>-CARBOHYDRATE DAY',
        "fr": 'JOUR <span class="a">MOYEN</span> EN GLUCIDES'},
    "Avena 60 g + 2 huevos + 2 claras + arándanos": {
        "en": "Oats 60 g + 2 eggs + 2 egg whites + blueberries",
        "fr": "Avoine 60 g + 2 œufs + 2 blancs + myrtilles"},
    "Arroz 120 g crudo + pollo 180 g + verduras salteadas": {
        "en": "Rice 120 g dry + chicken 180 g + sautéed vegetables",
        "fr": "Riz 120 g cru + poulet 180 g + légumes sautés"},
    "Batido de proteína + plátano grande": {
        "en": "Protein shake + large banana", "fr": "Shake protéiné + grosse banane"},
    "Boniato 200 g + salmón 150 g + ensalada verde": {
        "en": "Sweet potato 200 g + salmon 150 g + green salad",
        "fr": "Patate douce 200 g + saumon 150 g + salade verte"},
    "Pechuga 180 g + quinoa 40 g + brócoli + 1 cda de AOVE": {
        "en": "Chicken breast 180 g + quinoa 40 g + broccoli + 1 tbsp of olive oil",
        "fr": "Blanc de poulet 180 g + quinoa 40 g + brocoli + 1 c. à s. d'huile d'olive"},
    "Pre-cama": {"en": "Before bed", "fr": "Avant le coucher"},
    "Requesón 200 g + nueces 15 g": {
        "en": "Cottage cheese 200 g + walnuts 15 g",
        "fr": "Fromage blanc 200 g + noix 15 g"},
    "Menú calculado para un atleta de 75 kg. Escala las cantidades de forma proporcional a tu peso con la tabla de la página 3.": {
        "en": "Menu calculated for a 75 kg athlete. Scale the amounts in proportion to your weight using the table on page 3.",
        "fr": "Menu calculé pour un athlète de 75 kg. Adaptez les quantités proportionnellement à votre poids avec le tableau de la page 3."},
    "El día medio es el más útil de los tres": {
        "en": "The medium day is the most useful of the three",
        "fr": "Le jour moyen est le plus utile des trois"},
    "Es tu <strong>día por defecto</strong>: cuando dudes de qué tipo de día toca, elige medio.": {
        "en": "It is your <strong>default day</strong>: when in doubt about which type of day it is, choose medium.",
        "fr": "C'est votre <strong>jour par défaut</strong> : en cas de doute sur le type de jour, choisissez moyen."},
    "Encaja con el 70 % de las sesiones reales: tren superior, técnica o volumen moderado.": {
        "en": "It fits 70 % of real sessions: upper body, technique or moderate volume.",
        "fr": "Il convient à 70 % des séances réelles : haut du corps, technique ou volume modéré."},
    "Permite entrenar bien sin acumular el cansancio del día bajo repetido.": {
        "en": "It lets you train well without piling up the fatigue of repeated low days.",
        "fr": "Il permet de bien s'entraîner sans accumuler la fatigue des jours bas répétés."},
    "Es el día que usarás para <strong>mantener</strong> cuando termines el protocolo.": {
        "en": "It is the day you will use to <strong>maintain</strong> once the protocol is over.",
        "fr": "C'est le jour que vous utiliserez pour <strong>maintenir</strong> à la fin du protocole."},
    "Sustituciones válidas del día medio": {
        "en": "Valid swaps for the medium day", "fr": "Substitutions valables du jour moyen"},
    "Boniato ↔ patata ↔ arroz integral · Salmón ↔ caballa ↔ atún fresco · Requesón ↔ yogur griego 0 % ↔ caseína · Quinoa ↔ cuscús integral ↔ bulgur. Mantén los gramos de carbohidrato, no el peso del alimento.": {
        "en": "Sweet potato ↔ potato ↔ brown rice · Salmon ↔ mackerel ↔ fresh tuna · Cottage cheese ↔ 0 % Greek yoghurt ↔ casein · Quinoa ↔ wholewheat couscous ↔ bulgur. Keep the grams of carbohydrate, not the weight of the food.",
        "fr": "Patate douce ↔ pomme de terre ↔ riz complet · Saumon ↔ maquereau ↔ thon frais · Fromage blanc ↔ yaourt grec 0 % ↔ caséine · Quinoa ↔ couscous complet ↔ boulgour. Conservez les grammes de glucides, pas le poids de l'aliment."},

    # ── 06 · Día bajo ─────────────────────────────────────────────────
    "06 · Menú día bajo": {"en": "06 · Low-day menu", "fr": "06 · Menu jour bas"},
    'DÍA <span class="a">BAJO</span> EN CARBOHIDRATOS': {
        "en": '<span class="a">LOW</span>-CARBOHYDRATE DAY',
        "fr": 'JOUR <span class="a">BAS</span> EN GLUCIDES'},
    "Tortilla de 4 claras + 2 huevos + aguacate": {
        "en": "Omelette of 4 egg whites + 2 eggs + avocado",
        "fr": "Omelette de 4 blancs + 2 œufs + avocat"},
    "Colación 1": {"en": "Snack 1", "fr": "Collation 1"},
    "Salmón 220 g + ensalada grande + AOVE": {
        "en": "Salmon 220 g + large salad + olive oil",
        "fr": "Saumon 220 g + grande salade + huile d'olive"},
    "Colación 2": {"en": "Snack 2", "fr": "Collation 2"},
    "Proteína whey + almendras 30 g": {
        "en": "Whey protein + almonds 30 g", "fr": "Protéine whey + amandes 30 g"},
    "Pechuga 200 g + brócoli + espinacas": {
        "en": "Chicken breast 200 g + broccoli + spinach",
        "fr": "Blanc de poulet 200 g + brocoli + épinards"},
    "Requesón 200 g + semillas de chía": {
        "en": "Cottage cheese 200 g + chia seeds",
        "fr": "Fromage blanc 200 g + graines de chia"},
    "Cómo sobrevivir bien a un día bajo": {
        "en": "How to get through a low day well",
        "fr": "Comment bien traverser un jour bas"},
    "Problema": {"en": "Problem", "fr": "Problème"},
    "Causa": {"en": "Cause", "fr": "Cause"},
    "Solución": {"en": "Solution", "fr": "Solution"},
    "Hambre a media tarde": {"en": "Mid-afternoon hunger", "fr": "Faim en milieu d'après-midi"},
    "Poco volumen de comida": {"en": "Too little food volume", "fr": "Trop peu de volume alimentaire"},
    "Duplica la verdura: aporta saciedad casi sin calorías": {
        "en": "Double the vegetables: they add satiety at almost no calorie cost",
        "fr": "Doublez les légumes : ils rassasient pour presque aucune calorie"},
    "Dolor de cabeza": {"en": "Headache", "fr": "Mal de tête"},
    "Falta de sodio y agua": {"en": "Lack of sodium and water", "fr": "Manque de sodium et d'eau"},
    "Añade sal a las comidas y sube 500 ml de agua": {
        "en": "Add salt to your meals and add 500 ml of water",
        "fr": "Salez vos repas et ajoutez 500 ml d'eau"},
    "Antojo intenso de dulce": {"en": "Strong sugar craving", "fr": "Forte envie de sucre"},
    "Caída de glucosa y hábito": {"en": "Glucose dip and habit", "fr": "Chute de glucose et habitude"},
    "Gelatina sin azúcar, infusión o 20 g de chocolate del 90 %": {
        "en": "Sugar-free jelly, herbal tea or 20 g of 90 % chocolate",
        "fr": "Gelée sans sucre, infusion ou 20 g de chocolat à 90 %"},
    "Sensación de flojera en el gimnasio": {
        "en": "Feeling flat in the gym", "fr": "Sensation de mollesse à la salle"},
    "Has puesto el día bajo junto a una sesión dura": {
        "en": "You have put the low day next to a hard session",
        "fr": "Vous avez placé le jour bas à côté d'une séance dure"},
    "Reordena la semana: el día bajo va con descanso o cardio suave": {
        "en": "Reorder the week: the low day belongs with rest or easy cardio",
        "fr": "Réorganisez la semaine : le jour bas va avec le repos ou un cardio doux"},
    "Estreñimiento": {"en": "Constipation", "fr": "Constipation"},
    "Menos fibra al bajar los cereales": {
        "en": "Less fibre when cereals go down", "fr": "Moins de fibres quand les céréales baissent"},
    "Verdura de hoja, chía, psyllium y 2,5 L de agua": {
        "en": "Leafy greens, chia, psyllium and 2.5 L of water",
        "fr": "Légumes-feuilles, chia, psyllium et 2,5 L d'eau"},
    "Nunca encadenes más de dos días bajos seguidos": {
        "en": "Never chain more than two low days in a row",
        "fr": "N'enchaînez jamais plus de deux jours bas de suite"},
    "Tres o más días bajos consecutivos hunden el rendimiento, la calidad del sueño y el estado de ánimo, y disparan la probabilidad de un atracón. Si el calendario te obliga, convierte el tercero en día medio.": {
        "en": "Three or more consecutive low days sink performance, sleep quality and mood, and send the odds of a binge through the roof. If the calendar forces it, turn the third into a medium day.",
        "fr": "Trois jours bas consécutifs ou plus font chuter la performance, la qualité du sommeil et l'humeur, et font grimper le risque de crise alimentaire. Si le calendrier l'impose, transformez le troisième en jour moyen."},

    # ── 07 · Ajustes y cierre ─────────────────────────────────────────
    "07 · Ajustes y cierre": {"en": "07 · Adjustments and close", "fr": "07 · Ajustements et clôture"},
    'RECARGAS, AJUSTES Y <span class="a">SEÑALES</span>': {
        "en": 'REFEEDS, ADJUSTMENTS AND <span class="a">SIGNALS</span>',
        "fr": 'RECHARGES, AJUSTEMENTS ET <span class="a">SIGNAUX</span>'},
    "Cuándo y cómo hacer una recarga": {
        "en": "When and how to run a refeed", "fr": "Quand et comment faire une recharge"},
    "Señal": {"en": "Signal", "fr": "Signal"},
    "Qué indica": {"en": "What it indicates", "fr": "Ce qu'il indique"},
    "Peso estancado 2 semanas y fuerza cayendo": {
        "en": "Weight flat for 2 weeks and strength falling",
        "fr": "Poids stable 2 semaines et force en baisse"},
    "Depósitos vacíos, no falta de déficit": {
        "en": "Empty stores, not a missing deficit",
        "fr": "Réserves vides, pas un déficit insuffisant"},
    "Un día extra alto a 6 g/kg de carbohidrato": {
        "en": "One extra high day at 6 g/kg of carbohydrate",
        "fr": "Un jour haut supplémentaire à 6 g/kg de glucides"},
    "Peso baja más de 1 % semanal": {
        "en": "Weight dropping more than 1 % a week",
        "fr": "Le poids baisse de plus de 1 % par semaine"},
    "Déficit demasiado agresivo": {"en": "Deficit too aggressive", "fr": "Déficit trop agressif"},
    "Convierte un día bajo en medio": {
        "en": "Turn a low day into a medium one", "fr": "Transformez un jour bas en jour moyen"},
    "Peso sube dos semanas seguidas": {
        "en": "Weight up two weeks in a row", "fr": "Le poids monte deux semaines de suite"},
    "Falta de déficit real": {"en": "No real deficit", "fr": "Absence de déficit réel"},
    "Convierte un día alto en medio": {
        "en": "Turn a high day into a medium one", "fr": "Transformez un jour haut en jour moyen"},
    "Sueño malo y pulso en reposo alto": {
        "en": "Poor sleep and high resting pulse",
        "fr": "Mauvais sommeil et pouls de repos élevé"},
    "Fatiga acumulada": {"en": "Accumulated fatigue", "fr": "Fatigue accumulée"},
    "Semana completa a nivel medio antes de retomar": {
        "en": "A full week at medium level before resuming",
        "fr": "Une semaine entière au niveau moyen avant de reprendre"},
    "Registro de las 4 semanas": {"en": "4-week log", "fr": "Relevé des 4 semaines"},
    "Fuerza (sensación 1-10)": {"en": "Strength (feel 1-10)", "fr": "Force (ressenti 1-10)"},
    "Ajuste aplicado": {"en": "Adjustment applied", "fr": "Ajustement appliqué"},
    'EL CICLADO SE AJUSTA <span class="a">CON DATOS, NO CON FE</span>': {
        "en": 'CYCLING IS TUNED <span class="a">WITH DATA, NOT FAITH</span>',
        "fr": 'LE CYCLAGE S\'AJUSTE <span class="a">AVEC DES DONNÉES, PAS DE LA FOI</span>'},
    "Da al protocolo <strong>tres semanas completas</strong> antes de tocar nada, y cámbialo entonces con la báscula y el registro delante. Un ciclado corregido cada pocos días no es un ciclado: es ruido.": {
        "en": "Give the protocol <strong>three full weeks</strong> before you touch anything, then change it with the scale and the log in front of you. A cycling plan corrected every few days is not a cycling plan: it is noise.",
        "fr": "Laissez au protocole <strong>trois semaines complètes</strong> avant de toucher à quoi que ce soit, puis modifiez-le avec la balance et le relevé sous les yeux. Un cyclage corrigé tous les deux jours n'est pas un cyclage : c'est du bruit."},
    "<b>Aviso importante</b><br>\n      Documento con finalidad informativa y educativa. No constituye consejo médico,\n      diagnóstico ni tratamiento, y no sustituye la valoración de un profesional sanitario\n      colegiado. Consulta con tu médico antes de iniciar este protocolo, especialmente si\n      padeces diabetes u otra alteración del metabolismo de la glucosa, tomas medicación, estás\n      embarazada o en lactancia, eres menor de edad o tienes antecedentes de trastorno de la\n      conducta alimentaria. Los resultados varían entre personas y no están garantizados.\n      Contenido protegido por derechos de autor: prohibida su reproducción, distribución o\n      reventa total o parcial sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      A document for informational and educational purposes. It does not constitute medical advice, diagnosis or treatment, and it does not replace assessment by a registered health professional. Consult your doctor before starting this protocol, especially if you have diabetes or another disorder of glucose metabolism, take medication, are pregnant or breastfeeding, are a minor, or have a history of eating disorders. Results vary between individuals and are not guaranteed. Copyrighted content: reproduction, distribution or resale in whole or in part without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Document à finalité informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation d'un professionnel de santé. Consultez votre médecin avant de commencer ce protocole, en particulier en cas de diabète ou d'autre trouble du métabolisme du glucose, de traitement en cours, de grossesse ou d'allaitement, si vous êtes mineur ou avez des antécédents de trouble du comportement alimentaire. Les résultats varient et ne sont pas garantis. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente, totale ou partielle, sans autorisation écrite de VILLUMINATIONS est interdite."},
}
