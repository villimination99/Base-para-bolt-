# -*- coding: utf-8 -*-
"""
PLAN 04 · PRO — Definición + volumen, 8 semanas
===============================================
Protocolo de recomposición en dos fases. Los coeficientes por kilo son el
producto: no se redondean ni se convierten a otras unidades al traducir.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Recomposición corporal</small><span class="glow">DEFINICIÓN<br>+ VOLUMEN</span>': {
        "en": '<small>Body recomposition</small><span class="glow">CUT<br>+ BULK</span>',
        "fr": '<small>Recomposition corporelle</small><span class="glow">SÈCHE<br>+ MASSE</span>'},
    "Ocho semanas en dos fases encadenadas para construir músculo primero y revelarlo después, <em>sin</em> perder lo ganado.": {
        "en": "Eight weeks in two linked phases: build muscle first and reveal it afterwards, <em>without</em> losing what you gained.",
        "fr": "Huit semaines en deux phases enchaînées : construire du muscle d'abord et le révéler ensuite, <em>sans</em> perdre ce qui a été gagné."},
    '<span class="chip on">8 semanas</span> <span class="chip on">2 fases</span> <span class="chip">Macros por kg</span> <span class="chip">Cardio periodizado</span>': {
        "en": '<span class="chip on">8 weeks</span> <span class="chip on">2 phases</span> <span class="chip">Macros per kg</span> <span class="chip">Periodised cardio</span>',
        "fr": '<span class="chip on">8 semaines</span> <span class="chip on">2 phases</span> <span class="chip">Macros par kg</span> <span class="chip">Cardio périodisé</span>'},
    "Semanas por fase": {"en": "Weeks per phase", "fr": "Semaines par phase"},
    "5 días": {"en": "5 days", "fr": "5 jours"},
    "De transición": {"en": "Of transition", "fr": "De transition"},
    '<strong>Edición 2026</strong><br><span class="muted">Protocolo de recomposición corporal · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">Body recomposition protocol · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Protocole de recomposition corporelle · 8 pages</span>'},

    # ── 01 · La lógica ────────────────────────────────────────────────
    'LA LÓGICA DE LA <span class="a">RECOMPOSICIÓN</span>': {
        "en": 'THE LOGIC OF <span class="a">RECOMPOSITION</span>',
        "fr": 'LA LOGIQUE DE LA <span class="a">RECOMPOSITION</span>'},
    "Construir y definir a la vez es posible, pero lento e ineficiente en un atleta ya entrenado. Alternar <strong>fases cortas y bien definidas</strong> da mejores resultados: cuatro semanas empujando el músculo, cuatro revelando lo construido.": {
        "en": "Building and cutting at the same time is possible, but slow and inefficient in an already trained athlete. Alternating <strong>short, clearly defined phases</strong> works better: four weeks pushing the muscle, four revealing what was built.",
        "fr": "Construire et sécher en même temps est possible, mais lent et inefficace chez un athlète déjà entraîné. Alterner des <strong>phases courtes et bien définies</strong> donne de meilleurs résultats : quatre semaines à pousser le muscle, quatre à révéler ce qui a été construit."},
    '<span class="tag ok">Volumen</span>': {
        "en": '<span class="tag ok">Bulk</span>', "fr": '<span class="tag ok">Masse</span>'},
    "+300 a +400 kcal": {"en": "+300 to +400 kcal", "fr": "+300 à +400 kcal"},
    "2,0 g/kg": {"en": "2.0 g/kg", "fr": "2,0 g/kg"},
    "4,8–5,3 g/kg": {"en": "4.8–5.3 g/kg", "fr": "4,8–5,3 g/kg"},
    "0,9 g/kg": {"en": "0.9 g/kg", "fr": "0,9 g/kg"},
    '<span class="tag hi">Definición</span>': {
        "en": '<span class="tag hi">Cut</span>', "fr": '<span class="tag hi">Sèche</span>'},
    "−350 a −450 kcal": {"en": "−350 to −450 kcal", "fr": "−350 à −450 kcal"},
    "2,5–2,7 g/kg": {"en": "2.5–2.7 g/kg", "fr": "2,5–2,7 g/kg"},
    "2,5–3,0 g/kg": {"en": "2.5–3.0 g/kg", "fr": "2,5–3,0 g/kg"},
    "0,7 g/kg": {"en": "0.7 g/kg", "fr": "0,7 g/kg"},
    "Todas las tablas de este plan usan un atleta de referencia de 80 kg": {
        "en": "Every table in this plan uses a reference athlete of 80 kg",
        "fr": "Tous les tableaux de ce plan utilisent un athlète de référence de 80 kg"},
    "En la página 3 tienes la conversión a tu peso. No copies los gramos si pesas 65 o 95 kg: copia las <strong>proporciones</strong> por kilo.": {
        "en": "Page 3 has the conversion to your weight. Do not copy the grams if you weigh 65 or 95 kg: copy the <strong>ratios</strong> per kilo.",
        "fr": "La page 3 donne la conversion à votre poids. Ne recopiez pas les grammes si vous pesez 65 ou 95 kg : recopiez les <strong>proportions</strong> par kilo."},
    "Las tres reglas que sostienen el plan": {
        "en": "The three rules that hold the plan up",
        "fr": "Les trois règles qui soutiennent le plan"},
    "<b>La proteína sube cuando bajan las calorías</b>En déficit es lo único que separa perder grasa de perder músculo. Por eso pasa de 2,0 a 2,7 g/kg en la fase 2.": {
        "en": "<b>Protein rises when calories fall</b>In a deficit it is the only thing separating losing fat from losing muscle. That is why it goes from 2.0 to 2.7 g/kg in phase 2.",
        "fr": "<b>Les protéines montent quand les calories baissent</b>En déficit, c'est la seule chose qui sépare perdre du gras de perdre du muscle. D'où le passage de 2,0 à 2,7 g/kg en phase 2."},
    "<b>Las cargas del gimnasio no bajan en definición</b>Mismo peso, mismas series. Si reduces la carga, le dices al cuerpo que ya no necesita ese músculo.": {
        "en": "<b>Gym loads do not drop during the cut</b>Same weight, same sets. If you reduce the load, you tell the body it no longer needs that muscle.",
        "fr": "<b>Les charges ne baissent pas pendant la sèche</b>Même poids, mêmes séries. Si vous réduisez la charge, vous dites au corps qu'il n'a plus besoin de ce muscle."},
    "<b>El cardio entra progresivamente, no de golpe</b>Empieza en 2 sesiones y sube a 4. Guardarte margen es lo que te permitirá seguir avanzando en la semana 8.": {
        "en": "<b>Cardio comes in gradually, not all at once</b>Start at 2 sessions and build to 4. Keeping headroom is what lets you keep progressing in week 8.",
        "fr": "<b>Le cardio arrive progressivement, pas d'un coup</b>Commencez à 2 séances et montez à 4. Garder de la marge est ce qui vous permettra de progresser encore en semaine 8."},
    "Escala el plan a tu peso": {"en": "Scale the plan to your weight", "fr": "Adaptez le plan à votre poids"},
    "De gramos por kilo a tus gramos reales": {
        "en": "From grams per kilo to your actual grams",
        "fr": "Des grammes par kilo à vos grammes réels"},
    "Semanas 1–4 · Fase volumen": {"en": "Weeks 1–4 · Bulk phase", "fr": "Semaines 1–4 · Phase masse"},
    "Macros día a día y progresión de cargas": {
        "en": "Day-by-day macros and load progression",
        "fr": "Macros jour par jour et progression des charges"},
    "Semanas 5–8 · Fase definición": {
        "en": "Weeks 5–8 · Cutting phase", "fr": "Semaines 5–8 · Phase sèche"},
    "Déficit, cardio y protección muscular": {
        "en": "Deficit, cardio and muscle protection",
        "fr": "Déficit, cardio et protection musculaire"},
    "La transición y la comparativa": {
        "en": "The transition and the comparison", "fr": "La transition et la comparaison"},
    "Los 5 días que evitan el bajón energético": {
        "en": "The 5 days that prevent the energy crash",
        "fr": "Les 5 jours qui évitent le coup de mou"},
    "Entrenamiento y cardio por fase": {
        "en": "Training and cardio by phase", "fr": "Entraînement et cardio par phase"},
    "Qué cambia y qué no debe cambiar nunca": {
        "en": "What changes and what must never change",
        "fr": "Ce qui change et ce qui ne doit jamais changer"},

    # ── 02 · Escala ───────────────────────────────────────────────────
    'ESCALA EL PLAN A <span class="a">TU PESO</span>': {
        "en": 'SCALE THE PLAN TO <span class="a">YOUR WEIGHT</span>',
        "fr": 'ADAPTEZ LE PLAN À <span class="a">VOTRE POIDS</span>'},
    "Multiplica cada coeficiente por tu peso corporal en kilos. Si tienes más de un 25 % de grasa corporal, usa tu <strong>peso objetivo</strong> en lugar del actual para calcular la proteína.": {
        "en": "Multiply each coefficient by your body weight in kilos. If you are above 25 % body fat, use your <strong>target weight</strong> rather than your current one to work out protein.",
        "fr": "Multipliez chaque coefficient par votre poids corporel en kilos. Au-delà de 25 % de masse grasse, utilisez votre <strong>poids cible</strong> plutôt que le poids actuel pour calculer les protéines."},
    "Fase volumen": {"en": "Bulk phase", "fr": "Phase masse"},
    "Fase definición": {"en": "Cutting phase", "fr": "Phase sèche"},
    "Kcal/g": {"en": "Kcal/g", "fr": "Kcal/g"},
    "2,0 g × kg": {"en": "2.0 g × kg", "fr": "2,0 g × kg"},
    "2,5–2,7 g × kg": {"en": "2.5–2.7 g × kg", "fr": "2,5–2,7 g × kg"},
    "4,8–5,3 g × kg": {"en": "4.8–5.3 g × kg", "fr": "4,8–5,3 g × kg"},
    "2,5–3,0 g × kg": {"en": "2.5–3.0 g × kg", "fr": "2,5–3,0 g × kg"},
    "0,9 g × kg": {"en": "0.9 g × kg", "fr": "0,9 g × kg"},
    "0,7 g × kg": {"en": "0.7 g × kg", "fr": "0,7 g × kg"},
    "Equivalencias rápidas por peso corporal": {
        "en": "Quick equivalents by body weight", "fr": "Équivalences rapides par poids corporel"},
    "Tu peso": {"en": "Your weight", "fr": "Votre poids"},
    "Fase volumen (P / C / G)": {
        "en": "Bulk phase (P / C / F)", "fr": "Phase masse (P / G / L)"},
    "Fase definición (P / C / G)": {
        "en": "Cutting phase (P / C / F)", "fr": "Phase sèche (P / G / L)"},
    "60 kg": {"en": "60 kg", "fr": "60 kg"},
    "70 kg": {"en": "70 kg", "fr": "70 kg"},
    "80 kg": {"en": "80 kg", "fr": "80 kg"},
    "90 kg": {"en": "90 kg", "fr": "90 kg"},
    "100 kg": {"en": "100 kg", "fr": "100 kg"},
    "Volumen calculado a 5,0 g/kg de carbohidrato · Definición a 2,8 g/kg de carbohidrato y 2,63 g/kg de proteína (valores medios del plan).": {
        "en": "Bulk calculated at 5.0 g/kg of carbohydrate · Cut at 2.8 g/kg of carbohydrate and 2.63 g/kg of protein (the plan's mid-range values).",
        "fr": "Masse calculée à 5,0 g/kg de glucides · Sèche à 2,8 g/kg de glucides et 2,63 g/kg de protéines (valeurs moyennes du plan)."},
    "Tu ficha — complétala antes de empezar la semana 1": {
        "en": "Your record — fill it in before starting week 1",
        "fr": "Votre fiche — complétez-la avant de commencer la semaine 1"},
    "Valor inicial": {"en": "Starting value", "fr": "Valeur de départ"},
    "Cintura (ombligo)": {"en": "Waist (navel)", "fr": "Tour de taille (nombril)"},
    "Proteína volumen": {"en": "Protein, bulk", "fr": "Protéines, masse"},
    "Proteína definición": {"en": "Protein, cut", "fr": "Protéines, sèche"},
    "Carbos volumen": {"en": "Carbs, bulk", "fr": "Glucides, masse"},
    "Carbos definición": {"en": "Carbs, cut", "fr": "Glucides, sèche"},
    "Grasas volumen": {"en": "Fats, bulk", "fr": "Lipides, masse"},
    "Grasas definición": {"en": "Fats, cut", "fr": "Lipides, sèche"},
    "No empieces el plan en una semana cualquiera": {
        "en": "Do not start the plan on just any week",
        "fr": "Ne commencez pas le plan n'importe quelle semaine"},
    "Elige un bloque de ocho semanas sin viajes largos, mudanzas ni eventos que rompan tu rutina alimentaria. Un plan de ocho semanas ejecutado al 90 % vale infinitamente más que uno perfecto abandonado en la semana tres.": {
        "en": "Pick an eight-week block with no long trips, house moves or events that break your eating routine. An eight-week plan executed at 90 % is worth infinitely more than a perfect one abandoned in week three.",
        "fr": "Choisissez un bloc de huit semaines sans longs déplacements, déménagement ni événements qui cassent votre routine alimentaire. Un plan de huit semaines exécuté à 90 % vaut infiniment mieux qu'un plan parfait abandonné en semaine trois."},

    # ── 03 · Fase 1 ───────────────────────────────────────────────────
    "03 · Semanas 1–4": {"en": "03 · Weeks 1–4", "fr": "03 · Semaines 1–4"},
    'FASE 1 · <span class="a">VOLUMEN CONTROLADO</span>': {
        "en": 'PHASE 1 · <span class="a">CONTROLLED BULK</span>',
        "fr": 'PHASE 1 · <span class="a">PRISE DE MASSE CONTRÔLÉE</span>'},
    "Objetivo: crear un entorno anabólico sostenido con un superávit moderado de 300–400 kcal. Prioridad absoluta a los ejercicios compuestos con cargas máximas. El cardio se limita a dos sesiones LISS de 20–30 minutos para no comerse el superávit.": {
        "en": "Goal: create a sustained anabolic environment with a moderate surplus of 300–400 kcal. Absolute priority to compound lifts at maximal loads. Cardio is limited to two LISS sessions of 20–30 minutes so it does not eat the surplus.",
        "fr": "Objectif : créer un environnement anabolique soutenu avec un surplus modéré de 300–400 kcal. Priorité absolue aux exercices polyarticulaires à charges maximales. Le cardio se limite à deux séances LISS de 20–30 minutes pour ne pas manger le surplus."},
    "Kcal entreno": {"en": "Kcal, training", "fr": "Kcal, séance"},
    "Kcal descanso": {"en": "Kcal, rest", "fr": "Kcal, repos"},
    "Adaptación al superávit": {"en": "Adapting to the surplus", "fr": "Adaptation au surplus"},
    "Subir carga en los básicos": {
        "en": "Add load on the main lifts", "fr": "Monter la charge sur les exercices de base"},
    "Máxima intensidad": {"en": "Maximum intensity", "fr": "Intensité maximale"},
    "Evaluación y medición": {"en": "Assessment and measurement", "fr": "Évaluation et mesures"},
    "Valores para el atleta de referencia de 80 kg. Los días de descanso restan unos 60 g de carbohidrato respecto al día de entrenamiento.": {
        "en": "Values for the 80 kg reference athlete. Rest days subtract around 60 g of carbohydrate compared with a training day.",
        "fr": "Valeurs pour l'athlète de référence de 80 kg. Les jours de repos retirent environ 60 g de glucides par rapport au jour d'entraînement."},
    "Progresión de cargas semana a semana": {
        "en": "Week-by-week load progression", "fr": "Progression des charges semaine par semaine"},
    "Series por grupo": {"en": "Sets per muscle group", "fr": "Séries par groupe"},
    "Repeticiones": {"en": "Repetitions", "fr": "Répétitions"},
    "RIR objetivo": {"en": "Target RIR", "fr": "RIR cible"},
    "Establecer las cargas de partida": {
        "en": "Set the starting loads", "fr": "Établir les charges de départ"},
    "+2,5 % de peso o +1 repetición": {
        "en": "+2.5 % weight or +1 repetition", "fr": "+2,5 % de charge ou +1 répétition"},
    "+2,5 % de peso en los básicos": {
        "en": "+2.5 % weight on the main lifts", "fr": "+2,5 % de charge sur les exercices de base"},
    "Descarga: baja volumen, mantén carga": {
        "en": "Deload: drop volume, keep load", "fr": "Décharge : baissez le volume, gardez la charge"},
    "Control semanal de la fase": {"en": "Weekly phase check", "fr": "Contrôle hebdomadaire de la phase"},
    "¿Subió alguna carga?": {"en": "Did any load go up?", "fr": "Une charge a-t-elle augmenté ?"},
    "Criterio de éxito de la fase 1": {
        "en": "Success criterion for phase 1", "fr": "Critère de réussite de la phase 1"},
    "Entre <strong>0,8 y 1,6 kg</strong> de ganancia total en cuatro semanas, con la cintura creciendo como mucho 1 cm. Si el peso sube pero la cintura crece 3 cm, el superávit es demasiado grande: recorta 200 kcal de carbohidratos.": {
        "en": "Between <strong>0.8 and 1.6 kg</strong> of total gain in four weeks, with the waist growing 1 cm at most. If the weight goes up but the waist grows 3 cm, the surplus is too large: cut 200 kcal of carbohydrate.",
        "fr": "Entre <strong>0,8 et 1,6 kg</strong> de gain total en quatre semaines, avec un tour de taille qui augmente d'1 cm au maximum. Si le poids monte mais que la taille prend 3 cm, le surplus est trop grand : retirez 200 kcal de glucides."},

    # ── 04 · Fase 2 ───────────────────────────────────────────────────
    "04 · Semanas 5–8": {"en": "04 · Weeks 5–8", "fr": "04 · Semaines 5–8"},
    'FASE 2 · <span class="a">DEFINICIÓN</span>': {
        "en": 'PHASE 2 · <span class="a">CUTTING</span>',
        "fr": 'PHASE 2 · <span class="a">SÈCHE</span>'},
    "Objetivo: eliminar grasa con el mínimo catabolismo muscular. Déficit moderado de 350–450 kcal, proteína en su punto más alto y las mismas cargas en el gimnasio. El cardio crece de forma gradual para que siempre te quede margen de maniobra.": {
        "en": "Goal: strip fat with minimal muscle catabolism. A moderate deficit of 350–450 kcal, protein at its highest point and the same loads in the gym. Cardio grows gradually so that you always keep room to manoeuvre.",
        "fr": "Objectif : éliminer la graisse avec un catabolisme musculaire minimal. Déficit modéré de 350–450 kcal, protéines au plus haut et mêmes charges en salle. Le cardio augmente progressivement pour vous laisser toujours une marge de manœuvre."},
    "2 × LISS 25 min": {"en": "2 × LISS 25 min", "fr": "2 × LISS 25 min"},
    "3 × LISS 30 min": {"en": "3 × LISS 30 min", "fr": "3 × LISS 30 min"},
    "3 × HIIT + 1 × LISS": {"en": "3 × HIIT + 1 × LISS", "fr": "3 × HIIT + 1 × LISS"},
    "4 × HIIT 20 min": {"en": "4 × HIIT 20 min", "fr": "4 × HIIT 20 min"},
    "Cómo proteger el músculo en déficit": {
        "en": "How to protect muscle in a deficit", "fr": "Comment protéger le muscle en déficit"},
    "<strong>No toques las cargas.</strong> Mismo peso, mismas series. Perder un 5 % de fuerza es aceptable; perder un 20 % significa que estás perdiendo músculo.": {
        "en": "<strong>Do not touch the loads.</strong> Same weight, same sets. Losing 5 % of your strength is acceptable; losing 20 % means you are losing muscle.",
        "fr": "<strong>Ne touchez pas aux charges.</strong> Même poids, mêmes séries. Perdre 5 % de force est acceptable ; en perdre 20 % signifie que vous perdez du muscle."},
    "<strong>Proteína en cada comida:</strong> 4–5 tomas de al menos 0,4 g/kg.": {
        "en": "<strong>Protein at every meal:</strong> 4–5 servings of at least 0.4 g/kg.",
        "fr": "<strong>Des protéines à chaque repas :</strong> 4 à 5 prises d'au moins 0,4 g/kg."},
    "<strong>No añadas más cardio del planificado</strong> aunque el peso se estanque una semana: primero revisa el registro de comida.": {
        "en": "<strong>Do not add more cardio than planned</strong> even if the weight stalls for a week: check the food log first.",
        "fr": "<strong>N'ajoutez pas plus de cardio que prévu</strong> même si le poids stagne une semaine : vérifiez d'abord le relevé alimentaire."},
    "<strong>Duerme 7–9 horas.</strong> En déficit, dormir mal multiplica la pérdida de masa magra y el hambre del día siguiente.": {
        "en": "<strong>Sleep 7–9 hours.</strong> In a deficit, sleeping badly multiplies lean mass loss and next-day hunger.",
        "fr": "<strong>Dormez 7 à 9 heures.</strong> En déficit, mal dormir multiplie la perte de masse maigre et la faim du lendemain."},
    "<strong>Sal y agua:</strong> al bajar los carbohidratos se pierde sodio y agua. No restrinjas la sal salvo indicación médica.": {
        "en": "<strong>Salt and water:</strong> lowering carbohydrates flushes sodium and water. Do not restrict salt unless a doctor tells you to.",
        "fr": "<strong>Sel et eau :</strong> en baissant les glucides, on perd du sodium et de l'eau. Ne réduisez pas le sel sauf avis médical."},
    "Cardio realizado": {"en": "Cardio done", "fr": "Cardio réalisé"},
    "Fuerza (1-10)": {"en": "Strength (1-10)", "fr": "Force (1-10)"},
    "Criterio de éxito de la fase 2": {
        "en": "Success criterion for phase 2", "fr": "Critère de réussite de la phase 2"},
    "Perder entre el <strong>0,5 y el 0,8 % del peso corporal por semana</strong> — unos 0,4–0,6 kg en un atleta de 80 kg — manteniendo las cargas principales. Bajar más rápido casi siempre significa estar quemando músculo.": {
        "en": "Losing between <strong>0.5 and 0.8 % of body weight per week</strong> — about 0.4–0.6 kg in an 80 kg athlete — while holding the main loads. Dropping faster almost always means burning muscle.",
        "fr": "Perdre entre <strong>0,5 et 0,8 % du poids corporel par semaine</strong> — environ 0,4 à 0,6 kg chez un athlète de 80 kg — en conservant les charges principales. Descendre plus vite signifie presque toujours brûler du muscle."},

    # ── 05 · Transición ───────────────────────────────────────────────
    "05 · Transición": {"en": "05 · Transition", "fr": "05 · Transition"},
    'LOS 5 DÍAS DE <span class="a">TRANSICIÓN</span>': {
        "en": 'THE 5 <span class="a">TRANSITION</span> DAYS',
        "fr": 'LES 5 JOURS DE <span class="a">TRANSITION</span>'},
    "Pasar de 425 g de carbohidrato a 240 g de un día para otro provoca un desplome de energía, mal humor y sesiones desastrosas. Estos cinco días entre la semana 4 y la 5 hacen el cambio digerible.": {
        "en": "Going from 425 g of carbohydrate to 240 g overnight causes an energy crash, a foul mood and disastrous sessions. These five days between week 4 and week 5 make the change digestible.",
        "fr": "Passer de 425 g de glucides à 240 g du jour au lendemain provoque un effondrement d'énergie, de la mauvaise humeur et des séances désastreuses. Ces cinq jours entre la semaine 4 et la 5 rendent le changement digeste."},
    "Qué notarás": {"en": "What you will notice", "fr": "Ce que vous remarquerez"},
    "Día 1": {"en": "Day 1", "fr": "Jour 1"},
    "Prácticamente nada": {"en": "Practically nothing", "fr": "Pratiquement rien"},
    "Día 2": {"en": "Day 2", "fr": "Jour 2"},
    "Algo menos de congestión muscular": {
        "en": "Slightly less muscle fullness", "fr": "Un peu moins de congestion musculaire"},
    "Día 3": {"en": "Day 3", "fr": "Jour 3"},
    "Bajada de peso en báscula (agua)": {
        "en": "Weight drop on the scale (water)", "fr": "Baisse de poids sur la balance (eau)"},
    "Día 4": {"en": "Day 4", "fr": "Jour 4"},
    "Algo más de hambre por la tarde": {
        "en": "A little more hunger in the afternoon", "fr": "Un peu plus de faim l'après-midi"},
    "Día 5": {"en": "Day 5", "fr": "Jour 5"},
    "Ya estás en los valores de la semana 5": {
        "en": "You are already at week 5's numbers", "fr": "Vous êtes déjà aux valeurs de la semaine 5"},
    "Reducción aproximada de 40 g de carbohidrato al día, con la proteína subiendo en paralelo. Escala las cifras a tu peso corporal.": {
        "en": "A reduction of roughly 40 g of carbohydrate per day, with protein rising in parallel. Scale the figures to your body weight.",
        "fr": "Réduction d'environ 40 g de glucides par jour, avec les protéines qui montent en parallèle. Adaptez les chiffres à votre poids corporel."},
    "Comparativa entre fases": {"en": "Phase comparison", "fr": "Comparaison entre phases"},
    "Macronutriente": {"en": "Macronutrient", "fr": "Macronutriment"},
    "Función en cada fase": {"en": "Role in each phase", "fr": "Rôle dans chaque phase"},
    "160–180 g/día": {"en": "160–180 g/day", "fr": "160–180 g/jour"},
    "200–215 g/día": {"en": "200–215 g/day", "fr": "200–215 g/jour"},
    "Sube en definición para preservar masa muscular": {
        "en": "Rises during the cut to preserve muscle mass",
        "fr": "Monte en sèche pour préserver la masse musculaire"},
    "380–425 g/día": {"en": "380–425 g/day", "fr": "380–425 g/jour"},
    "200–240 g/día": {"en": "200–240 g/day", "fr": "200–240 g/jour"},
    "Combustible en volumen, se recortan en definición": {
        "en": "Fuel during the bulk, trimmed during the cut",
        "fr": "Carburant en masse, réduits en sèche"},
    "72 g/día": {"en": "72 g/day", "fr": "72 g/jour"},
    "56 g/día": {"en": "56 g/day", "fr": "56 g/jour"},
    "Sostienen la función hormonal, nunca por debajo de 0,6 g/kg": {
        "en": "They sustain hormone function; never below 0.6 g/kg",
        "fr": "Ils soutiennent la fonction hormonale, jamais en dessous de 0,6 g/kg"},
    "Calorías totales": {"en": "Total calories", "fr": "Calories totales"},
    "Superávit frente a déficit": {"en": "Surplus versus deficit", "fr": "Surplus contre déficit"},
    "2 sesiones LISS": {"en": "2 LISS sessions", "fr": "2 séances LISS"},
    "Hasta 4 sesiones": {"en": "Up to 4 sessions", "fr": "Jusqu'à 4 séances"},
    "Herramienta de ajuste, no protagonista": {
        "en": "An adjustment tool, not the main act",
        "fr": "Un outil d'ajustement, pas le rôle principal"},
    "El error clásico de la transición": {
        "en": "The classic transition mistake", "fr": "L'erreur classique de la transition"},
    "Bajar los carbohidratos y <strong>también</strong> las grasas el mismo día. Al hacerlo el déficit se dispara por encima de 800 kcal, la testosterona cae y la adherencia se rompe en pocos días. Baja los carbohidratos primero; las grasas, solo al final.": {
        "en": "Dropping carbohydrates and <strong>fats too</strong> on the same day. Do that and the deficit shoots past 800 kcal, testosterone falls and adherence breaks within days. Lower carbohydrates first; fats only at the end.",
        "fr": "Baisser les glucides <strong>et aussi</strong> les lipides le même jour. Le déficit dépasse alors 800 kcal, la testostérone chute et l'observance casse en quelques jours. Baissez d'abord les glucides ; les lipides, seulement à la fin."},

    # ── 06 · Entrenamiento ────────────────────────────────────────────
    "06 · Entrenamiento": {"en": "06 · Training", "fr": "06 · Entraînement"},
    'ENTRENAMIENTO Y <span class="a">CARDIO POR FASE</span>': {
        "en": 'TRAINING AND <span class="a">CARDIO BY PHASE</span>',
        "fr": 'ENTRAÎNEMENT ET <span class="a">CARDIO PAR PHASE</span>'},
    "Sesiones de pesas": {"en": "Weights sessions", "fr": "Séances de musculation"},
    "4 por semana": {"en": "4 per week", "fr": "4 par semaine"},
    "4 por semana (sin cambios)": {"en": "4 per week (unchanged)", "fr": "4 par semaine (inchangé)"},
    "Estructura": {"en": "Structure", "fr": "Structure"},
    "Push / Pull / Legs / Full body": {
        "en": "Push / Pull / Legs / Full body", "fr": "Poussée / Tirage / Jambes / Corps entier"},
    "Rango de repeticiones": {"en": "Repetition range", "fr": "Plage de répétitions"},
    "8–12 (algo más de repetición, misma carga)": {
        "en": "8–12 (a few more reps, same load)",
        "fr": "8–12 (un peu plus de répétitions, même charge)"},
    "Descanso entre series": {"en": "Rest between sets", "fr": "Repos entre les séries"},
    "90–150 s en compuestos": {"en": "90–150 s on compounds", "fr": "90–150 s sur les polyarticulaires"},
    "90–150 s (no lo acortes por «quemar más»)": {
        "en": "90–150 s (do not shorten it to «burn more»)",
        "fr": "90–150 s (ne le raccourcissez pas pour « brûler plus »)"},
    "2 × LISS 20–30 min": {"en": "2 × LISS 20–30 min", "fr": "2 × LISS 20–30 min"},
    "De 2 a 4 sesiones, progresivo": {
        "en": "From 2 to 4 sessions, progressive", "fr": "De 2 à 4 séances, progressif"},
    "Pasos diarios": {"en": "Daily steps", "fr": "Pas quotidiens"},
    "LISS y HIIT: cuándo usar cada uno": {
        "en": "LISS and HIIT: when to use each", "fr": "LISS et HIIT : quand utiliser l'un ou l'autre"},
    "LISS · baja intensidad": {"en": "LISS · low intensity", "fr": "LISS · basse intensité"},
    "Caminar en cinta inclinada, bici suave o elíptica": {
        "en": "Walking on an inclined treadmill, easy bike or elliptical",
        "fr": "Marche sur tapis incliné, vélo doux ou elliptique"},
    "Frecuencia cardiaca entre el 60 y el 70 % de la máxima": {
        "en": "Heart rate between 60 and 70 % of maximum",
        "fr": "Fréquence cardiaque entre 60 et 70 % du maximum"},
    "Apenas interfiere con la recuperación de las pesas": {
        "en": "Barely interferes with recovery from lifting",
        "fr": "Interfère à peine avec la récupération de la musculation"},
    "Ideal el día después de piernas": {
        "en": "Ideal the day after legs", "fr": "Idéal le lendemain des jambes"},
    "HIIT · alta intensidad": {"en": "HIIT · high intensity", "fr": "HIIT · haute intensité"},
    "Intervalos de 20–40 s al máximo con descanso incompleto": {
        "en": "Intervals of 20–40 s all-out with incomplete rest",
        "fr": "Intervalles de 20–40 s à fond avec repos incomplet"},
    "Máximo 3–4 sesiones semanales de 15–20 minutos": {
        "en": "No more than 3–4 sessions a week of 15–20 minutes",
        "fr": "Au maximum 3 à 4 séances par semaine de 15–20 minutes"},
    "Nunca el mismo día que piernas ni el día previo": {
        "en": "Never on leg day or the day before",
        "fr": "Jamais le jour des jambes ni la veille"},
    "Empieza por 20 s de trabajo y 40 s de descanso, y ajusta desde ahí": {
        "en": "Start with 20 s of work and 40 s of rest, and adjust from there",
        "fr": "Commencez par 20 s de travail et 40 s de repos, puis ajustez"},
    "Semana de descarga (semana 4 y semana 8)": {
        "en": "Deload week (week 4 and week 8)", "fr": "Semaine de décharge (semaines 4 et 8)"},
    "Reduce el volumen un 40 %: de 18 series por grupo a 10–11.": {
        "en": "Cut volume by 40 %: from 18 sets per group to 10–11.",
        "fr": "Réduisez le volume de 40 % : de 18 séries par groupe à 10–11."},
    "<strong>Mantén la carga.</strong> Menos series con el mismo peso, no series suaves.": {
        "en": "<strong>Keep the load.</strong> Fewer sets at the same weight, not easy sets.",
        "fr": "<strong>Gardez la charge.</strong> Moins de séries au même poids, pas des séries molles."},
    "Elimina el fallo muscular: RIR 3–4 en todas las series.": {
        "en": "Remove muscular failure: RIR 3–4 on every set.",
        "fr": "Supprimez l'échec musculaire : RIR 3–4 sur toutes les séries."},
    "Aprovecha para hacer fotos, mediciones y planificar el bloque siguiente.": {
        "en": "Use it to take photos, measurements and plan the next block.",
        "fr": "Profitez-en pour faire des photos, des mesures et planifier le bloc suivant."},
    "Registro de cargas: el dato que decide todo": {
        "en": "The load log: the data that decides everything",
        "fr": "Le carnet de charges : la donnée qui décide de tout"},
    "Si no anotas peso, series y repeticiones de cada sesión, no tienes forma de saber si el plan funciona. La báscula miente a corto plazo; el registro de cargas, no.": {
        "en": "If you do not write down weight, sets and reps for every session, you have no way of knowing whether the plan works. The scale lies in the short term; the load log does not.",
        "fr": "Si vous ne notez pas charge, séries et répétitions de chaque séance, vous n'avez aucun moyen de savoir si le plan fonctionne. La balance ment à court terme ; le carnet de charges, non."},

    # ── 07 · Evaluación ───────────────────────────────────────────────
    "07 · Evaluación final": {"en": "07 · Final assessment", "fr": "07 · Évaluation finale"},
    'EVALUACIÓN Y <span class="a">SIGUIENTE BLOQUE</span>': {
        "en": 'ASSESSMENT AND <span class="a">NEXT BLOCK</span>',
        "fr": 'ÉVALUATION ET <span class="a">BLOC SUIVANT</span>'},
    "Inicio (sem. 1)": {"en": "Start (wk 1)", "fr": "Début (sem. 1)"},
    "Fin fase 1 (sem. 4)": {"en": "End of phase 1 (wk 4)", "fr": "Fin phase 1 (sem. 4)"},
    "Fin fase 2 (sem. 8)": {"en": "End of phase 2 (wk 8)", "fr": "Fin phase 2 (sem. 8)"},
    "Diferencia total": {"en": "Total difference", "fr": "Différence totale"},
    "Brazo": {"en": "Arm", "fr": "Bras"},
    "Sentadilla 1RM estimado": {"en": "Estimated squat 1RM", "fr": "1RM estimé au squat"},
    "Press banca 1RM estimado": {
        "en": "Estimated bench press 1RM", "fr": "1RM estimé au développé couché"},
    "Qué hacer al terminar las 8 semanas": {
        "en": "What to do when the 8 weeks are over",
        "fr": "Que faire à la fin des 8 semaines"},
    "Tu resultado": {"en": "Your result", "fr": "Votre résultat"},
    "Siguiente paso": {"en": "Next step", "fr": "Étape suivante"},
    "Ganaste músculo y bajaste cintura": {
        "en": "You gained muscle and lost waist", "fr": "Vous avez gagné du muscle et perdu du tour de taille"},
    "Repite el ciclo completo subiendo un 5 % los carbohidratos de la fase 1": {
        "en": "Repeat the full cycle with phase 1 carbohydrates raised by 5 %",
        "fr": "Refaites le cycle complet en augmentant de 5 % les glucides de la phase 1"},
    "Ganaste peso pero también mucha cintura": {
        "en": "You gained weight but also a lot of waist",
        "fr": "Vous avez gagné du poids mais aussi beaucoup de tour de taille"},
    "Encadena 4 semanas más de definición antes de volver a volumen": {
        "en": "Add 4 more weeks of cutting before going back to a bulk",
        "fr": "Enchaînez 4 semaines de sèche de plus avant de repasser en masse"},
    "Perdiste grasa pero también fuerza": {
        "en": "You lost fat but also strength", "fr": "Vous avez perdu du gras mais aussi de la force"},
    "Dos semanas de mantenimiento y revisa proteína y horas de sueño": {
        "en": "Two weeks at maintenance, and review protein and hours of sleep",
        "fr": "Deux semaines de maintenance, et revoyez les protéines et les heures de sommeil"},
    "Apenas hubo cambios": {"en": "There was barely any change", "fr": "Il n'y a presque pas eu de changement"},
    "Revisa el registro real de comida: casi siempre falla la medición, no el plan": {
        "en": "Check the actual food log: it is almost always the measurement that fails, not the plan",
        "fr": "Vérifiez le relevé alimentaire réel : c'est presque toujours la mesure qui échoue, pas le plan"},
    'EL ENTRENAMIENTO QUE <span class="a">ACOMPAÑA A ESTE PLAN</span>': {
        "en": 'THE TRAINING THAT <span class="a">GOES WITH THIS PLAN</span>',
        "fr": "L'ENTRAÎNEMENT QUI <span class=\"a\">ACCOMPAGNE CE PLAN</span>"},
    "El nivel <strong>ELITE</strong> añade el trabajo de sala\n        periodizado, el acondicionamiento metabólico y una sesión semanal donde el bloque se\n        ajusta a tus datos reales en lugar de a una plantilla.": {
        "en": "The <strong>ELITE</strong> tier adds periodised gym work, metabolic conditioning and a weekly session where the block is tuned to your real data instead of to a template.",
        "fr": "Le niveau <strong>ÉLITE</strong> ajoute le travail en salle périodisé, le conditionnement métabolique et une séance hebdomadaire où le bloc s'ajuste à vos données réelles plutôt qu'à un modèle."},
    "<b>Aviso importante</b><br>\n      Documento con finalidad informativa y educativa. No constituye consejo médico, diagnóstico\n      ni tratamiento, y no sustituye la valoración de un profesional sanitario colegiado.\n      Consulta con tu médico antes de iniciar este plan, especialmente si estás embarazada o en\n      periodo de lactancia, eres menor de edad, tomas medicación o padeces alguna patología\n      cardiovascular, metabólica, renal, hepática o un trastorno de la conducta alimentaria. Los\n      déficits calóricos prolongados requieren supervisión profesional. Los resultados varían\n      entre personas y no están garantizados. Contenido protegido por derechos de autor:\n      prohibida su reproducción, distribución o reventa sin autorización escrita de\n      VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      A document for informational and educational purposes. It does not constitute medical advice, diagnosis or treatment, and it does not replace assessment by a registered health professional. Consult your doctor before starting this plan, especially if you are pregnant or breastfeeding, are a minor, take medication or have any cardiovascular, metabolic, renal or hepatic condition or an eating disorder. Prolonged calorie deficits require professional supervision. Results vary between individuals and are not guaranteed. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Document à finalité informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation d'un professionnel de santé. Consultez votre médecin avant de commencer ce plan, en particulier en cas de grossesse ou d'allaitement, si vous êtes mineur, sous traitement, ou atteint d'une pathologie cardiovasculaire, métabolique, rénale, hépatique ou d'un trouble du comportement alimentaire. Les déficits caloriques prolongés nécessitent un suivi professionnel. Les résultats varient et ne sont pas garantis. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
