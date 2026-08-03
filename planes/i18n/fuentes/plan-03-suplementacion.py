# -*- coding: utf-8 -*-
"""
PLAN 03 · PRO — Guía de suplementación
======================================
Las dosis, los precios y los nombres de marca no se traducen: son datos. Sí se
adapta el nombre del organismo antidopaje, que en francés y en inglés se
conoce por siglas distintas de las españolas.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Ciencia aplicada</small><span class="glow">GUÍA DE<br>SUPLEMENTACIÓN</span>': {
        "en": '<small>Applied science</small><span class="glow">SUPPLEMENT<br>GUIDE</span>',
        "fr": '<small>Science appliquée</small><span class="glow">GUIDE DE<br>COMPLÉMENTATION</span>'},
    "Qué tomar, cuánto, cuándo y por qué — y sobre todo, <em>qué no comprar nunca</em>.": {
        "en": "What to take, how much, when and why — and above all, <em>what never to buy</em>.",
        "fr": "Quoi prendre, combien, quand et pourquoi — et surtout, <em>ce qu'il ne faut jamais acheter</em>."},
    '<span class="chip on">5 esenciales</span> <span class="chip on">4 opcionales</span> <span class="chip">10 que no funcionan</span> <span class="chip">Presupuesto real</span>': {
        "en": '<span class="chip on">5 essentials</span> <span class="chip on">4 optional</span> <span class="chip">10 that do not work</span> <span class="chip">Real budget</span>',
        "fr": '<span class="chip on">5 essentiels</span> <span class="chip on">4 optionnels</span> <span class="chip">10 qui ne marchent pas</span> <span class="chip">Budget réel</span>'},
    "Con evidencia": {"en": "Evidence-backed", "fr": "Fondés sur des preuves"},
    "Dinero tirado": {"en": "Money wasted", "fr": "Argent gaspillé"},
    "Coste mensual": {"en": "Monthly cost", "fr": "Coût mensuel"},
    '<strong>Edición 2026</strong><br><span class="muted">Guía de suplementación basada en evidencia · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">Evidence-based supplement guide · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Guide de complémentation fondé sur les preuves · 8 pages</span>'},

    # ── 01 · Jerarquía ────────────────────────────────────────────────
    "01 · Jerarquía": {"en": "01 · Hierarchy", "fr": "01 · Hiérarchie"},
    'ANTES DE GASTAR <span class="a">UN SOLO EURO</span>': {
        "en": 'BEFORE YOU SPEND <span class="a">A SINGLE EURO</span>',
        "fr": 'AVANT DE DÉPENSER <span class="a">UN SEUL EURO</span>'},
    "Los suplementos aportan, como mucho, el <strong>5 % del resultado</strong>. Si el 95 % restante no está en su sitio, ningún bote lo va a arreglar. Esta es la jerarquía real, en orden de impacto.": {
        "en": "Supplements contribute, at most, <strong>5 % of the result</strong>. If the other 95 % is not in place, no tub is going to fix it. This is the real hierarchy, in order of impact.",
        "fr": "Les compléments apportent, au mieux, <strong>5 % du résultat</strong>. Si les 95 % restants ne sont pas en place, aucun pot n'y changera rien. Voici la vraie hiérarchie, par ordre d'impact."},
    "<b>Balance calórico y proteína</b>Determina si ganas o pierdes, y cuánto de ello es músculo.": {
        "en": "<b>Calorie balance and protein</b>They determine whether you gain or lose, and how much of it is muscle.",
        "fr": "<b>Balance calorique et protéines</b>Elles déterminent si vous gagnez ou perdez, et quelle part est du muscle."},
    "<b>Entrenamiento con sobrecarga progresiva</b>El estímulo sin el cual no hay adaptación.": {
        "en": "<b>Training with progressive overload</b>The stimulus without which there is no adaptation.",
        "fr": "<b>Entraînement en surcharge progressive</b>Le stimulus sans lequel il n'y a pas d'adaptation."},
    "<b>Sueño de 7–9 horas</b>Donde ocurre de verdad la recuperación y la síntesis proteica.": {
        "en": "<b>7–9 hours of sleep</b>Where recovery and protein synthesis actually happen.",
        "fr": "<b>7 à 9 heures de sommeil</b>Là où se produisent réellement la récupération et la synthèse protéique."},
    "<b>Consistencia durante meses</b>El factor que más separa a quien progresa de quien no.": {
        "en": "<b>Consistency over months</b>The factor that most separates those who progress from those who do not.",
        "fr": "<b>Régularité sur plusieurs mois</b>Le facteur qui sépare le plus ceux qui progressent de ceux qui stagnent."},
    "<b>Suplementación</b>El ajuste fino. Solo tiene sentido cuando lo anterior ya funciona.": {
        "en": "<b>Supplementation</b>The fine tuning. It only makes sense once the above already works.",
        "fr": "<b>Complémentation</b>Le réglage fin. Cela n'a de sens que lorsque le reste fonctionne déjà."},
    "Contenido de esta guía": {"en": "What is in this guide", "fr": "Contenu de ce guide"},
    "Los 2 imprescindibles": {"en": "The 2 essentials", "fr": "Les 2 indispensables"},
    "Proteína y creatina: dosis, momento y marcas": {
        "en": "Protein and creatine: dose, timing and brands",
        "fr": "Protéines et créatine : dose, moment et marques"},
    "Los 3 de salud y recuperación": {
        "en": "The 3 for health and recovery", "fr": "Les 3 pour la santé et la récupération"},
    "Omega-3, vitamina D3 + K2 y magnesio": {
        "en": "Omega-3, vitamin D3 + K2 and magnesium",
        "fr": "Oméga-3, vitamine D3 + K2 et magnésium"},
    "Segunda línea: rendimiento": {"en": "Second tier: performance", "fr": "Deuxième ligne : performance"},
    "Cafeína, beta-alanina, citrulina y ashwagandha": {
        "en": "Caffeine, beta-alanine, citrulline and ashwagandha",
        "fr": "Caféine, bêta-alanine, citrulline et ashwagandha"},
    "Los 10 que no funcionan": {"en": "The 10 that do not work", "fr": "Les 10 qui ne marchent pas"},
    "Dónde se va el dinero de la mayoría": {
        "en": "Where most people's money goes", "fr": "Où part l'argent de la plupart des gens"},
    "Tu protocolo diario y el coste real": {
        "en": "Your daily protocol and the real cost",
        "fr": "Votre protocole quotidien et le coût réel"},
    "Tabla de horarios y presupuesto mensual": {
        "en": "Timing table and monthly budget",
        "fr": "Tableau des horaires et budget mensuel"},
    "Seguridad, calidad y antidopaje": {
        "en": "Safety, quality and anti-doping", "fr": "Sécurité, qualité et antidopage"},
    "Cómo elegir sin jugártela": {
        "en": "How to choose without taking risks", "fr": "Comment choisir sans prendre de risque"},
    "Pág. 8": {"en": "P. 8", "fr": "P. 8"},
    "La pregunta que debes hacerte ante cualquier bote": {
        "en": "The question to ask yourself in front of any tub",
        "fr": "La question à se poser devant n'importe quel pot"},
    "¿Existe al menos un metaanálisis que respalde su efecto en humanos sanos y a la dosis que trae el producto? Si la respuesta es no, estás pagando marketing.": {
        "en": "Is there at least one meta-analysis backing its effect in healthy humans, at the dose the product actually contains? If the answer is no, you are paying for marketing.",
        "fr": "Existe-t-il au moins une méta-analyse appuyant son effet chez l'humain sain, à la dose que contient réellement le produit ? Si la réponse est non, vous payez du marketing."},

    # ── 02 · Imprescindibles ──────────────────────────────────────────
    "02 · Imprescindibles": {"en": "02 · Essentials", "fr": "02 · Indispensables"},
    'LOS DOS <span class="a">IMPRESCINDIBLES</span>': {
        "en": 'THE TWO <span class="a">ESSENTIALS</span>',
        "fr": 'LES DEUX <span class="a">INDISPENSABLES</span>'},
    "1 · Proteína en polvo (whey o vegetal)": {
        "en": "1 · Protein powder (whey or plant-based)",
        "fr": "1 · Protéine en poudre (whey ou végétale)"},
    "No es magia: 1 g de proteína de whey construye exactamente lo mismo que 1 g de proteína de pollo. Su valor es <strong>logístico</strong> — te permite llegar a tu cuota diaria cuando la comida real no encaja en tu horario.": {
        "en": "It is not magic: 1 g of whey protein builds exactly the same as 1 g of protein from chicken. Its value is <strong>logistical</strong> — it lets you hit your daily quota when real food does not fit your schedule.",
        "fr": "Ce n'est pas magique : 1 g de protéine de whey construit exactement autant qu'1 g de protéine de poulet. Sa valeur est <strong>logistique</strong> — elle permet d'atteindre votre quota quotidien quand les vrais repas ne rentrent pas dans votre emploi du temps."},
    "Parámetro": {"en": "Parameter", "fr": "Paramètre"},
    "20–40 g por toma (1–2 cazos)": {
        "en": "20–40 g per serving (1–2 scoops)", "fr": "20–40 g par prise (1 à 2 doses)"},
    "Post-entreno o entre comidas, como complemento para cerrar el total diario": {
        "en": "Post-workout or between meals, as a top-up to close the daily total",
        "fr": "Après la séance ou entre les repas, en appoint pour boucler le total quotidien"},
    "Tipo": {"en": "Type", "fr": "Type"},
    "Concentrado (más económico) o aislado (menos lactosa y grasa)": {
        "en": "Concentrate (cheaper) or isolate (less lactose and fat)",
        "fr": "Concentré (plus économique) ou isolat (moins de lactose et de gras)"},
    "Opción vegana": {"en": "Vegan option", "fr": "Option végane"},
    "Guisante + arroz en proporción 70/30, para completar el perfil de aminoácidos": {
        "en": "Pea + rice in a 70/30 ratio, to complete the amino acid profile",
        "fr": "Pois + riz dans un rapport 70/30, pour compléter le profil d'acides aminés"},
    "Marcas verificadas": {"en": "Verified brands", "fr": "Marques vérifiées"},
    "Optimum Nutrition, MyProtein, Garden of Life (vegana)": {
        "en": "Optimum Nutrition, MyProtein, Garden of Life (vegan)",
        "fr": "Optimum Nutrition, MyProtein, Garden of Life (végane)"},
    "Precio orientativo": {"en": "Indicative price", "fr": "Prix indicatif"},
    "30–60 $ por 2 kg (entre 1 y 2 meses de uso)": {
        "en": "$30–60 for 2 kg (1 to 2 months of use)",
        "fr": "30–60 $ les 2 kg (1 à 2 mois d'utilisation)"},
    "2 · Creatina monohidrato": {
        "en": "2 · Creatine monohydrate", "fr": "2 · Créatine monohydrate"},
    "El suplemento más estudiado de la historia del deporte, con cientos de ensayos y un perfil de seguridad excelente en personas sanas. Aumenta la fuerza entre un 5 y un 15 %, acelera la recuperación entre series y tiene beneficios cognitivos documentados.": {
        "en": "The most studied supplement in the history of sport, with hundreds of trials and an excellent safety profile in healthy people. It raises strength by 5 to 15 %, speeds recovery between sets and has documented cognitive benefits.",
        "fr": "Le complément le plus étudié de l'histoire du sport, avec des centaines d'essais et un excellent profil de sécurité chez les personnes en bonne santé. Elle augmente la force de 5 à 15 %, accélère la récupération entre les séries et présente des bénéfices cognitifs documentés."},
    "3–5 g diarios. La fase de carga es opcional y no mejora el resultado final": {
        "en": "3–5 g a day. The loading phase is optional and does not improve the final result",
        "fr": "3 à 5 g par jour. La phase de charge est facultative et n'améliore pas le résultat final"},
    "Cualquier momento del día. Con una comida mejora ligeramente la absorción": {
        "en": "Any time of day. Taking it with a meal slightly improves absorption",
        "fr": "À n'importe quel moment. Avec un repas, l'absorption est légèrement meilleure"},
    "<strong>Monohidrato únicamente.</strong> El resto de formas son marketing más caro": {
        "en": "<strong>Monohydrate only.</strong> The other forms are more expensive marketing",
        "fr": "<strong>Monohydrate uniquement.</strong> Les autres formes sont du marketing plus cher"},
    "Ciclos": {"en": "Cycling", "fr": "Cycles"},
    "No hacen falta. El uso continuo es seguro y más efectivo": {
        "en": "Not needed. Continuous use is safe and more effective",
        "fr": "Inutiles. L'usage continu est sûr et plus efficace"},
    "Marcas": {"en": "Brands", "fr": "Marques"},
    "Creapure (Alemania) o cualquier monohidrato sin sabor de marca conocida": {
        "en": "Creapure (Germany) or any unflavoured monohydrate from a known brand",
        "fr": "Creapure (Allemagne) ou tout monohydrate sans arôme d'une marque connue"},
    "15–25 $ por 500 g (3–4 meses de uso)": {
        "en": "$15–25 for 500 g (3–4 months of use)",
        "fr": "15–25 $ les 500 g (3 à 4 mois d'utilisation)"},
    "Dos aclaraciones sobre la creatina": {
        "en": "Two clarifications about creatine", "fr": "Deux précisions sur la créatine"},
    "El aumento de 1–2 kg de las primeras semanas es <strong>agua intramuscular</strong>, no grasa: es el efecto buscado. Y no, no daña el riñón en personas sanas — puede elevar levemente la creatinina en un análisis, lo cual es un artefacto de la medición, no un daño. Avisa a tu médico de que la tomas antes de una analítica.": {
        "en": "The 1–2 kg gain of the first weeks is <strong>intramuscular water</strong>, not fat: it is the intended effect. And no, it does not damage the kidneys in healthy people — it can slightly raise creatinine in a blood test, which is an artefact of the measurement, not harm. Tell your doctor you take it before any blood work.",
        "fr": "La prise de 1 à 2 kg des premières semaines est de l'<strong>eau intramusculaire</strong>, pas de la graisse : c'est l'effet recherché. Et non, elle n'abîme pas les reins chez les personnes en bonne santé — elle peut légèrement élever la créatinine à l'analyse, ce qui est un artefact de mesure, pas une lésion. Prévenez votre médecin que vous en prenez avant une prise de sang."},

    # ── 03 · Salud y recuperación ─────────────────────────────────────
    "03 · Salud y recuperación": {
        "en": "03 · Health and recovery", "fr": "03 · Santé et récupération"},
    'LOS TRES DE <span class="a">SALUD Y RECUPERACIÓN</span>': {
        "en": 'THE THREE FOR <span class="a">HEALTH AND RECOVERY</span>',
        "fr": 'LES TROIS POUR <span class="a">LA SANTÉ ET LA RÉCUPÉRATION</span>'},
    "3 · Omega-3 (EPA + DHA)": {"en": "3 · Omega-3 (EPA + DHA)", "fr": "3 · Oméga-3 (EPA + DHA)"},
    "2–3 g de EPA + DHA combinados al día (mira el reverso: no es lo mismo que gramos de aceite)": {
        "en": "2–3 g of EPA + DHA combined per day (check the back: that is not the same as grams of oil)",
        "fr": "2 à 3 g d'EPA + DHA combinés par jour (regardez au dos : ce n'est pas la même chose que des grammes d'huile)"},
    "Beneficios": {"en": "Benefits", "fr": "Bénéfices"},
    "Reduce la inflamación, mejora la recuperación y protege la salud cardiovascular": {
        "en": "It lowers inflammation, improves recovery and protects cardiovascular health",
        "fr": "Ils réduisent l'inflammation, améliorent la récupération et protègent la santé cardiovasculaire"},
    "Con las comidas que contengan grasa, para maximizar la absorción": {
        "en": "With meals containing fat, to maximise absorption",
        "fr": "Avec des repas contenant des lipides, pour maximiser l'absorption"},
    "Aceite de pescado (salmón, sardina, anchoa) o de algas para la opción vegana": {
        "en": "Fish oil (salmon, sardine, anchovy) or algae oil for the vegan option",
        "fr": "Huile de poisson (saumon, sardine, anchois) ou d'algues pour l'option végane"},
    "Nordic Naturals, Solgar, OmegaVia": {
        "en": "Nordic Naturals, Solgar, OmegaVia", "fr": "Nordic Naturals, Solgar, OmegaVia"},
    "20–35 $ por 90 cápsulas": {"en": "$20–35 for 90 capsules", "fr": "20–35 $ les 90 gélules"},
    "4 · Vitamina D3 + K2": {"en": "4 · Vitamin D3 + K2", "fr": "4 · Vitamine D3 + K2"},
    "Buena parte de la población tiene niveles insuficientes, sobre todo con trabajo en interiores o en climas nublados. Interviene en la función inmune, la salud ósea, la recuperación y la producción hormonal.": {
        "en": "A large share of the population has insufficient levels, especially with indoor work or in cloudy climates. It is involved in immune function, bone health, recovery and hormone production.",
        "fr": "Une grande partie de la population a des niveaux insuffisants, surtout avec un travail en intérieur ou sous un climat nuageux. Elle intervient dans la fonction immunitaire, la santé osseuse, la récupération et la production hormonale."},
    "Dosis D3": {"en": "D3 dose", "fr": "Dose D3"},
    "2.000–4.000 UI diarias": {"en": "2,000–4,000 IU daily", "fr": "2 000–4 000 UI par jour"},
    "Dosis K2": {"en": "K2 dose", "fr": "Dose K2"},
    "100–200 mcg (dirige el calcio hacia el hueso y no hacia la arteria)": {
        "en": "100–200 mcg (it directs calcium to bone rather than to the artery)",
        "fr": "100–200 mcg (elle dirige le calcium vers l'os plutôt que vers l'artère)"},
    "Por la mañana, con el desayuno: es liposoluble y necesita grasa": {
        "en": "In the morning, with breakfast: it is fat-soluble and needs fat",
        "fr": "Le matin, avec le petit-déjeuner : elle est liposoluble et a besoin de lipides"},
    "Forma": {"en": "Form", "fr": "Forme"},
    "D3 (colecalciferol), nunca D2 — se absorbe mucho peor": {
        "en": "D3 (cholecalciferol), never D2 — it is absorbed far worse",
        "fr": "D3 (cholécalciférol), jamais D2 — bien moins bien absorbée"},
    "Control": {"en": "Monitoring", "fr": "Contrôle"},
    "Pide 25-OH-vitamina D en tu analítica anual y ajusta con tu médico": {
        "en": "Ask for 25-OH-vitamin D in your annual blood test and adjust with your doctor",
        "fr": "Demandez la 25-OH-vitamine D lors de votre bilan annuel et ajustez avec votre médecin"},
    "10–20 $ por 3 meses": {"en": "$10–20 for 3 months", "fr": "10–20 $ pour 3 mois"},
    "5 · Magnesio": {"en": "5 · Magnesium", "fr": "5 · Magnésium"},
    "300–400 mg de magnesio elemental al día": {
        "en": "300–400 mg of elemental magnesium a day",
        "fr": "300 à 400 mg de magnésium élémentaire par jour"},
    "Mejora la calidad del sueño, la función neuromuscular y ayuda a modular el cortisol": {
        "en": "It improves sleep quality and neuromuscular function, and helps modulate cortisol",
        "fr": "Il améliore la qualité du sommeil, la fonction neuromusculaire et aide à moduler le cortisol"},
    "30–60 minutos antes de dormir": {
        "en": "30–60 minutes before sleep", "fr": "30 à 60 minutes avant le coucher"},
    "Bisglicinato (mejor tolerado) o citrato. Evita el óxido: apenas se absorbe": {
        "en": "Bisglycinate (better tolerated) or citrate. Avoid the oxide: it is barely absorbed",
        "fr": "Bisglycinate (mieux toléré) ou citrate. Évitez l'oxyde : il est à peine absorbé"},
    "15–25 $ por 3 meses": {"en": "$15–25 for 3 months", "fr": "15–25 $ pour 3 mois"},
    "Orden de compra si tu presupuesto es limitado": {
        "en": "Buying order if your budget is limited",
        "fr": "Ordre d'achat si votre budget est limité"},
    "Creatina → proteína → vitamina D3 → magnesio → omega-3. Los dos primeros son los que más impacto tienen por euro invertido en un atleta que ya entrena y come bien.": {
        "en": "Creatine → protein → vitamin D3 → magnesium → omega-3. The first two have the greatest impact per euro spent in an athlete who already trains and eats well.",
        "fr": "Créatine → protéines → vitamine D3 → magnésium → oméga-3. Les deux premiers ont le plus d'impact par euro investi chez un athlète qui s'entraîne et mange déjà bien."},

    # ── 04 · Rendimiento ──────────────────────────────────────────────
    "04 · Rendimiento": {"en": "04 · Performance", "fr": "04 · Performance"},
    'SEGUNDA LÍNEA: <span class="a">RENDIMIENTO</span>': {
        "en": 'SECOND TIER: <span class="a">PERFORMANCE</span>',
        "fr": 'DEUXIÈME LIGNE : <span class="a">PERFORMANCE</span>'},
    "Tienen evidencia sólida, pero su efecto es menor y más específico. Añádelos solo cuando los cinco anteriores ya formen parte de tu rutina.": {
        "en": "They have solid evidence, but their effect is smaller and more specific. Add them only once the previous five are already part of your routine.",
        "fr": "Ils reposent sur des preuves solides, mais leur effet est plus faible et plus spécifique. Ne les ajoutez que lorsque les cinq précédents font déjà partie de votre routine."},
    "Qué esperar realmente": {"en": "What to realistically expect", "fr": "Ce qu'il faut réellement en attendre"},
    "3–6 mg/kg": {"en": "3–6 mg/kg", "fr": "3–6 mg/kg"},
    "45–60 min antes": {"en": "45–60 min before", "fr": "45–60 min avant"},
    "Más fuerza, más repeticiones y menor percepción del esfuerzo": {
        "en": "More strength, more reps and a lower perception of effort",
        "fr": "Plus de force, plus de répétitions et une perception de l'effort réduite"},
    "Beta-alanina": {"en": "Beta-alanine", "fr": "Bêta-alanine"},
    "3–5 g/día": {"en": "3–5 g/day", "fr": "3–5 g/jour"},
    "Cualquier hora, a diario": {"en": "Any time, daily", "fr": "À n'importe quelle heure, chaque jour"},
    "Mejora esfuerzos de 1 a 4 minutos. Necesita 4 semanas para saturar": {
        "en": "It improves efforts of 1 to 4 minutes. It needs 4 weeks to saturate",
        "fr": "Elle améliore les efforts de 1 à 4 minutes. Il lui faut 4 semaines pour saturer"},
    "Citrulina malato": {"en": "Citrulline malate", "fr": "Citrulline malate"},
    "60 min antes": {"en": "60 min before", "fr": "60 min avant"},
    "Alguna repetición más y mejor congestión muscular": {
        "en": "A few more reps and a better muscle pump",
        "fr": "Quelques répétitions de plus et une meilleure congestion"},
    "Ayuda con el estrés percibido. Evidencia moderada, no espectacular": {
        "en": "It helps with perceived stress. Moderate evidence, not spectacular",
        "fr": "Il aide sur le stress perçu. Preuves modérées, rien de spectaculaire"},
    "Electrolitos": {"en": "Electrolytes", "fr": "Électrolytes"},
    "Según sudoración": {"en": "According to sweat rate", "fr": "Selon la sudation"},
    "Entrenos largos o calor": {"en": "Long sessions or heat", "fr": "Séances longues ou chaleur"},
    "Evita calambres y bajones cuando sudas mucho": {
        "en": "It prevents cramps and slumps when you sweat a lot",
        "fr": "Ils évitent crampes et coups de mou quand vous transpirez beaucoup"},
    "Cafeína: cómo usarla bien": {"en": "Caffeine: how to use it well", "fr": "Caféine : comment bien l'utiliser"},
    "Lo que debes hacer": {"en": "What to do", "fr": "Ce qu'il faut faire"},
    "Empieza por 3 mg/kg y sube solo si lo necesitas": {
        "en": "Start at 3 mg/kg and go up only if you need to",
        "fr": "Commencez à 3 mg/kg et n'augmentez que si nécessaire"},
    "Combínala con L-teanina en proporción 1:2 si te pone nervioso": {
        "en": "Combine it with L-theanine in a 1:2 ratio if it makes you jittery",
        "fr": "Associez-la à la L-théanine dans un rapport 1:2 si elle vous rend nerveux"},
    "Resérvala para tus 2–3 sesiones más duras de la semana": {
        "en": "Save it for your 2–3 hardest sessions of the week",
        "fr": "Réservez-la à vos 2 ou 3 séances les plus dures de la semaine"},
    "Descansa una semana cada 6–8 para recuperar sensibilidad": {
        "en": "Take a week off every 6–8 to restore sensitivity",
        "fr": "Faites une pause d'une semaine toutes les 6 à 8 pour retrouver la sensibilité"},
    "Lo que arruina el resultado": {"en": "What ruins the result", "fr": "Ce qui gâche le résultat"},
    "Tomarla después de las 14:00: su vida media es de 5–6 horas": {
        "en": "Taking it after 14:00: its half-life is 5–6 hours",
        "fr": "La prendre après 14 h : sa demi-vie est de 5 à 6 heures"},
    "Usarla a diario en dosis altas: la tolerancia anula el efecto": {
        "en": "Using it daily at high doses: tolerance cancels the effect",
        "fr": "En prendre chaque jour à forte dose : la tolérance annule l'effet"},
    "Compensar con cafeína un sueño insuficiente": {
        "en": "Using caffeine to paper over insufficient sleep",
        "fr": "Compenser un manque de sommeil avec de la caféine"},
    "Sumar pre-entreno, café y refresco energético sin contar el total": {
        "en": "Stacking pre-workout, coffee and an energy drink without counting the total",
        "fr": "Cumuler pre-workout, café et boisson énergisante sans compter le total"},
    "Límite de seguridad": {"en": "Safety limit", "fr": "Limite de sécurité"},
    "No superes los 400 mg de cafeína al día (unos 4 cafés) ni los 200 mg en una sola toma si no tienes tolerancia. Si tienes hipertensión, arritmias, ansiedad o problemas de sueño, consúltalo con tu médico antes de usarla como ayuda ergogénica.": {
        "en": "Do not exceed 400 mg of caffeine a day (about 4 coffees), nor 200 mg in a single dose if you have no tolerance. If you have hypertension, arrhythmias, anxiety or sleep problems, check with your doctor before using it as an ergogenic aid.",
        "fr": "Ne dépassez pas 400 mg de caféine par jour (environ 4 cafés), ni 200 mg en une seule prise si vous n'avez pas de tolérance. En cas d'hypertension, d'arythmie, d'anxiété ou de troubles du sommeil, consultez votre médecin avant de l'utiliser comme aide ergogénique."},
    "Nota sobre la beta-alanina: el hormigueo en cara y manos (parestesia) es inofensivo y desaparece repartiendo la dosis en dos tomas o usando la versión de liberación sostenida.": {
        "en": "A note on beta-alanine: the tingling in face and hands (paraesthesia) is harmless and goes away by splitting the dose in two or using the sustained-release version.",
        "fr": "Note sur la bêta-alanine : les fourmillements au visage et aux mains (paresthésie) sont inoffensifs et disparaissent en fractionnant la dose en deux prises ou en utilisant la version à libération prolongée."},

    # ── 05 · Dinero tirado ────────────────────────────────────────────
    "05 · Dinero tirado": {"en": "05 · Money wasted", "fr": "05 · Argent gaspillé"},
    'LOS 10 QUE <span class="a">NO FUNCIONAN</span>': {
        "en": 'THE 10 THAT <span class="a">DO NOT WORK</span>',
        "fr": 'LES 10 QUI <span class="a">NE MARCHENT PAS</span>'},
    "Ninguno de estos productos es peligroso por sí mismo; simplemente no hacen lo que promete su etiqueta. Este es el dinero que la mayoría de la gente tira cada mes.": {
        "en": "None of these products is dangerous in itself; they simply do not do what the label promises. This is the money most people throw away every month.",
        "fr": "Aucun de ces produits n'est dangereux en soi ; ils ne font simplement pas ce que promet leur étiquette. C'est l'argent que la plupart des gens jettent chaque mois."},
    "Lo que promete": {"en": "What it promises", "fr": "Ce qu'il promet"},
    "Lo que dice la evidencia": {"en": "What the evidence says", "fr": "Ce que disent les preuves"},
    "BCAA / aminoácidos ramificados": {
        "en": "BCAAs / branched-chain amino acids", "fr": "BCAA / acides aminés ramifiés"},
    "Más músculo y menos catabolismo": {
        "en": "More muscle and less catabolism", "fr": "Plus de muscle et moins de catabolisme"},
    "Inútiles si ya tomas suficiente proteína: te faltan los otros aminoácidos esenciales": {
        "en": "Useless if you already get enough protein: the other essential amino acids are missing",
        "fr": "Inutiles si vous consommez déjà assez de protéines : les autres acides aminés essentiels manquent"},
    "Quemagrasas termogénicos": {"en": "Thermogenic fat burners", "fr": "Brûleurs de graisse thermogéniques"},
    "Acelerar el metabolismo": {"en": "Speeding up metabolism", "fr": "Accélérer le métabolisme"},
    "El efecto sobre el gasto es mínimo y no cambia la composición corporal": {
        "en": "The effect on expenditure is minimal and does not change body composition",
        "fr": "L'effet sur la dépense est minime et ne change pas la composition corporelle"},
    "Glutamina": {"en": "Glutamine", "fr": "Glutamine"},
    "Recuperación e hipertrofia": {"en": "Recovery and hypertrophy", "fr": "Récupération et hypertrophie"},
    "Sin efecto en deportistas sanos bien alimentados": {
        "en": "No effect in healthy, well-fed athletes",
        "fr": "Sans effet chez les sportifs sains et bien nourris"},
    "Boosters de testosterona": {"en": "Testosterone boosters", "fr": "Boosters de testostérone"},
    "Subir la testosterona": {"en": "Raising testosterone", "fr": "Augmenter la testostérone"},
    "Tribulus y similares no la elevan en hombres con niveles normales": {
        "en": "Tribulus and the like do not raise it in men with normal levels",
        "fr": "Le tribulus et consorts ne l'augmentent pas chez les hommes aux niveaux normaux"},
    "Creatinas «avanzadas»": {"en": "«Advanced» creatines", "fr": "Créatines « avancées »"},
    "Mejor absorción que el monohidrato": {
        "en": "Better absorption than monohydrate", "fr": "Meilleure absorption que le monohydrate"},
    "HCL, etil éster y kre-alkalyn: más caras, sin ventaja demostrada": {
        "en": "HCL, ethyl ester and kre-alkalyn: more expensive, with no proven advantage",
        "fr": "HCL, ester éthylique et kre-alkalyn : plus chères, sans avantage démontré"},
    "Detox y limpiezas": {"en": "Detoxes and cleanses", "fr": "Détox et cures purifiantes"},
    "Eliminar toxinas": {"en": "Removing toxins", "fr": "Éliminer les toxines"},
    "De eso ya se ocupan tu hígado y tus riñones, gratis": {
        "en": "Your liver and kidneys already handle that, free of charge",
        "fr": "Votre foie et vos reins s'en chargent déjà, gratuitement"},
    "Óxido nítrico en cápsulas": {"en": "Nitric oxide capsules", "fr": "Oxyde nitrique en gélules"},
    "Congestión y vasodilatación": {"en": "Pump and vasodilation", "fr": "Congestion et vasodilatation"},
    "Suelen llevar dosis muy por debajo de la efectiva de citrulina": {
        "en": "They usually contain doses far below the effective amount of citrulline",
        "fr": "Ils contiennent généralement des doses bien inférieures à la dose efficace de citrulline"},
    "Multivitamínicos en megadosis": {"en": "Megadose multivitamins", "fr": "Multivitamines à mégadoses"},
    "Cubrir todas las carencias": {"en": "Covering every deficiency", "fr": "Combler toutes les carences"},
    "Con una dieta variada solo generas orina cara; algunas vitaminas se acumulan": {
        "en": "On a varied diet you only produce expensive urine; some vitamins accumulate",
        "fr": "Avec une alimentation variée, vous ne produisez que de l'urine coûteuse ; certaines vitamines s'accumulent"},
    "Colágeno para el músculo": {"en": "Collagen for muscle", "fr": "Collagène pour le muscle"},
    "Ganar masa muscular": {"en": "Gaining muscle mass", "fr": "Gagner de la masse musculaire"},
    "Proteína de bajo valor biológico. Útil para tendón, no para hipertrofia": {
        "en": "A low biological value protein. Useful for tendon, not for hypertrophy",
        "fr": "Protéine de faible valeur biologique. Utile pour le tendon, pas pour l'hypertrophie"},
    "Cetonas exógenas": {"en": "Exogenous ketones", "fr": "Cétones exogènes"},
    "Quemar grasa y dar energía": {
        "en": "Burning fat and giving energy", "fr": "Brûler la graisse et donner de l'énergie"},
    "Caras, de sabor desagradable y sin beneficio en el atleta que come carbohidratos": {
        "en": "Expensive, unpleasant tasting and of no benefit to an athlete who eats carbohydrates",
        "fr": "Chères, au goût désagréable et sans bénéfice pour un athlète qui mange des glucides"},
    "Regla de los 30 días": {"en": "The 30-day rule", "fr": "La règle des 30 jours"},
    "Antes de comprar un suplemento nuevo, calcula lo que cuesta al año y pregúntate qué harías con ese dinero: ¿unos meses más de creatina y proteína? ¿comida real de mejor calidad? Casi siempre la respuesta correcta es la segunda.": {
        "en": "Before buying a new supplement, work out what it costs per year and ask yourself what else you would do with that money: a few more months of creatine and protein? Better-quality real food? Almost always the right answer is the second.",
        "fr": "Avant d'acheter un nouveau complément, calculez ce qu'il coûte à l'année et demandez-vous ce que vous feriez de cet argent : quelques mois de plus de créatine et de protéines ? De la vraie nourriture de meilleure qualité ? La bonne réponse est presque toujours la seconde."},

    # ── 06 · Protocolo ────────────────────────────────────────────────
    "06 · Protocolo diario": {"en": "06 · Daily protocol", "fr": "06 · Protocole quotidien"},
    'TU <span class="a">PROTOCOLO DIARIO</span>': {
        "en": 'YOUR <span class="a">DAILY PROTOCOL</span>',
        "fr": 'VOTRE <span class="a">PROTOCOLE QUOTIDIEN</span>'},
    "Mañana": {"en": "Morning", "fr": "Matin"},
    "Proteína en polvo": {"en": "Protein powder", "fr": "Protéine en poudre"},
    '<span class="tag ok">Principal</span>': {
        "en": '<span class="tag ok">Core</span>', "fr": '<span class="tag ok">Principal</span>'},
    "Si falta cuota": {"en": "If the quota is short", "fr": "S'il manque du quota"},
    "Creatina 3–5 g": {"en": "Creatine 3–5 g", "fr": "Créatine 3–5 g"},
    '<span class="tag ok">Opción</span>': {
        "en": '<span class="tag ok">Option</span>', "fr": '<span class="tag ok">Option</span>'},
    "Opción": {"en": "Option", "fr": "Option"},
    '<span class="tag ok">Con la proteína</span>': {
        "en": '<span class="tag ok">With the protein</span>',
        "fr": '<span class="tag ok">Avec les protéines</span>'},
    "Omega-3": {"en": "Omega-3", "fr": "Oméga-3"},
    '<span class="tag ok">Con desayuno</span>': {
        "en": '<span class="tag ok">With breakfast</span>',
        "fr": '<span class="tag ok">Au petit-déjeuner</span>'},
    "Vitamina D3 + K2": {"en": "Vitamin D3 + K2", "fr": "Vitamine D3 + K2"},
    '<span class="tag ok">Obligatorio</span>': {
        "en": '<span class="tag ok">Required</span>', "fr": '<span class="tag ok">Obligatoire</span>'},
    "Magnesio": {"en": "Magnesium", "fr": "Magnésium"},
    '<span class="tag ok">30 min antes de dormir</span>': {
        "en": '<span class="tag ok">30 min before sleep</span>',
        "fr": '<span class="tag ok">30 min avant le coucher</span>'},
    "Cafeína (opcional)": {"en": "Caffeine (optional)", "fr": "Caféine (facultatif)"},
    '<span class="tag hi">45–60 min antes</span>': {
        "en": '<span class="tag hi">45–60 min before</span>',
        "fr": '<span class="tag hi">45–60 min avant</span>'},
    "Nunca": {"en": "Never", "fr": "Jamais"},
    "Beta-alanina (opcional)": {"en": "Beta-alanine (optional)", "fr": "Bêta-alanine (facultatif)"},
    "Presupuesto mensual realista": {
        "en": "A realistic monthly budget", "fr": "Un budget mensuel réaliste"},
    "Incluye": {"en": "Includes", "fr": "Comprend"},
    "Mínimo viable": {"en": "Bare minimum", "fr": "Minimum viable"},
    "Creatina + vitamina D3": {"en": "Creatine + vitamin D3", "fr": "Créatine + vitamine D3"},
    "Recomendado": {"en": "Recommended", "fr": "Recommandé"},
    "Creatina + proteína + D3 + magnesio": {
        "en": "Creatine + protein + D3 + magnesium",
        "fr": "Créatine + protéines + D3 + magnésium"},
    "Los 5 esenciales + cafeína": {
        "en": "The 5 essentials + caffeine", "fr": "Les 5 essentiels + caféine"},
    "Rendimiento": {"en": "Performance", "fr": "Performance"},
    "Completo + beta-alanina + citrulina": {
        "en": "Complete + beta-alanine + citrulline",
        "fr": "Complet + bêta-alanine + citrulline"},
    "Tu inventario": {"en": "Your inventory", "fr": "Votre inventaire"},
    "Dosis diaria": {"en": "Daily dose", "fr": "Dose quotidienne"},
    "Fecha de reposición": {"en": "Restock date", "fr": "Date de réapprovisionnement"},
    "Creatina": {"en": "Creatine", "fr": "Créatine"},

    # ── 07 · Seguridad ────────────────────────────────────────────────
    "07 · Seguridad": {"en": "07 · Safety", "fr": "07 · Sécurité"},
    'CALIDAD, SEGURIDAD Y <span class="a">ANTIDOPAJE</span>': {
        "en": 'QUALITY, SAFETY AND <span class="a">ANTI-DOPING</span>',
        "fr": 'QUALITÉ, SÉCURITÉ ET <span class="a">ANTIDOPAGE</span>'},
    "Cómo elegir un producto fiable": {
        "en": "How to choose a reliable product", "fr": "Comment choisir un produit fiable"},
    "Sellos de análisis por terceros: <strong>Informed Sport</strong> o <strong>NSF Certified for Sport</strong>": {
        "en": "Third-party testing marks: <strong>Informed Sport</strong> or <strong>NSF Certified for Sport</strong>",
        "fr": "Labels d'analyse par un tiers : <strong>Informed Sport</strong> ou <strong>NSF Certified for Sport</strong>"},
    "Etiqueta con dosis por ración, no «mezcla propia» sin cantidades": {
        "en": "A label with the dose per serving, not a «proprietary blend» with no amounts",
        "fr": "Une étiquette avec la dose par portion, pas un « mélange exclusif » sans quantités"},
    "Un solo ingrediente activo por bote siempre que sea posible": {
        "en": "A single active ingredient per tub whenever possible",
        "fr": "Un seul ingrédient actif par pot dans la mesure du possible"},
    "Fabricante con lote, caducidad y país de origen visibles": {
        "en": "A manufacturer with batch, expiry date and country of origin visible",
        "fr": "Un fabricant avec lot, date de péremption et pays d'origine visibles"},
    "Señales de alarma": {"en": "Warning signs", "fr": "Signaux d'alarme"},
    "Promesas de resultados «en 7 días» o comparaciones con fármacos": {
        "en": "Promises of results «in 7 days» or comparisons with drugs",
        "fr": "Promesses de résultats « en 7 jours » ou comparaisons avec des médicaments"},
    "Fórmulas propietarias que ocultan las dosis reales": {
        "en": "Proprietary formulas that hide the real doses",
        "fr": "Formules exclusives qui masquent les doses réelles"},
    "Productos para bajar de peso comprados fuera de canales regulados": {
        "en": "Weight-loss products bought outside regulated channels",
        "fr": "Produits amaigrissants achetés hors des circuits réglementés"},
    "Ingredientes que no sabes pronunciar ni encontrar en la literatura": {
        "en": "Ingredients you can neither pronounce nor find in the literature",
        "fr": "Des ingrédients que vous ne savez ni prononcer ni trouver dans la littérature"},
    "Situaciones que exigen consultar antes con un profesional sanitario": {
        "en": "Situations that require checking with a health professional first",
        "fr": "Situations qui exigent de consulter d'abord un professionnel de santé"},
    "Tomas medicación crónica: anticoagulantes, antihipertensivos, antidiabéticos, tiroideos o psicofármacos": {
        "en": "You take long-term medication: anticoagulants, antihypertensives, antidiabetics, thyroid drugs or psychotropics",
        "fr": "Vous prenez un traitement chronique : anticoagulants, antihypertenseurs, antidiabétiques, traitements thyroïdiens ou psychotropes"},
    "Tienes patología renal, hepática, cardiaca o un trastorno de la conducta alimentaria": {
        "en": "You have renal, hepatic or cardiac disease, or an eating disorder",
        "fr": "Vous avez une pathologie rénale, hépatique, cardiaque ou un trouble du comportement alimentaire"},
    "Estás embarazada, en periodo de lactancia o eres menor de edad": {
        "en": "You are pregnant, breastfeeding or a minor",
        "fr": "Vous êtes enceinte, allaitante ou mineure"},
    "Compites bajo control antidopaje: verifica cada producto en la lista de la AMA": {
        "en": "You compete under anti-doping control: check every product against the WADA list",
        "fr": "Vous concourez sous contrôle antidopage : vérifiez chaque produit sur la liste de l'AMA"},
    "Vas a hacerte una analítica: avisa de que tomas creatina": {
        "en": "You are about to have blood work: mention that you take creatine",
        "fr": "Vous allez faire une prise de sang : signalez que vous prenez de la créatine"},
    'PRIMERO LA COMIDA, <span class="a">DESPUÉS EL BOTE</span>': {
        "en": 'FOOD FIRST, <span class="a">THE TUB SECOND</span>',
        "fr": 'D\'ABORD L\'ASSIETTE, <span class="a">ENSUITE LE POT</span>'},
    "Ningún suplemento de esta guía compensa dormir mal o comer poco: <strong>son el 5 % final</strong>, no el atajo. Empieza por los dos esenciales, dales ocho semanas y no añadas nada más hasta poder medir qué ha cambiado.": {
        "en": "No supplement in this guide makes up for sleeping badly or eating too little: <strong>they are the final 5 %</strong>, not the shortcut. Start with the two essentials, give them eight weeks, and add nothing else until you can measure what changed.",
        "fr": "Aucun complément de ce guide ne compense un mauvais sommeil ou une alimentation insuffisante : <strong>ils représentent les 5 % finaux</strong>, pas le raccourci. Commencez par les deux essentiels, laissez-leur huit semaines et n'ajoutez rien d'autre avant de pouvoir mesurer ce qui a changé."},
    # Cabecera de la tabla de la compra: aquí «marca» es el fabricante.
    "Marca": {"en": "Brand", "fr": "Marque"},

    "<b>Aviso importante</b><br>\n      Esta guía tiene finalidad exclusivamente informativa y educativa. No constituye consejo\n      médico, diagnóstico, tratamiento ni prescripción, y no sustituye la valoración de un\n      profesional sanitario colegiado. Los suplementos alimenticios no están destinados a\n      prevenir, tratar ni curar ninguna enfermedad, y no deben sustituir una dieta variada y\n      equilibrada. Las dosis indicadas corresponden a personas adultas sanas; consulta con tu\n      médico o farmacéutico antes de iniciar cualquier suplementación, especialmente si tomas\n      medicación, padeces alguna patología, estás embarazada o en periodo de lactancia, o eres\n      menor de edad. Las marcas citadas se mencionan a título orientativo y no implican\n      patrocinio ni relación comercial. Los precios son orientativos y pueden variar según país\n      y distribuidor. Contenido protegido por derechos de autor: prohibida su reproducción,\n      distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      This guide is for informational and educational purposes only. It does not constitute medical advice, diagnosis, treatment or prescription, and it does not replace assessment by a registered health professional. Food supplements are not intended to prevent, treat or cure any disease, and must not replace a varied, balanced diet. The doses given are for healthy adults; consult your doctor or pharmacist before starting any supplementation, especially if you take medication, have a medical condition, are pregnant or breastfeeding, or are a minor. The brands named are mentioned for guidance only and imply no sponsorship or commercial relationship. Prices are indicative and may vary by country and retailer. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Ce guide a une finalité exclusivement informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement, ni une prescription, et ne remplace pas l'évaluation d'un professionnel de santé. Les compléments alimentaires ne sont pas destinés à prévenir, traiter ou guérir une maladie, et ne doivent pas se substituer à une alimentation variée et équilibrée. Les doses indiquées concernent des adultes en bonne santé ; consultez votre médecin ou votre pharmacien avant toute complémentation, en particulier si vous prenez un traitement, souffrez d'une pathologie, êtes enceinte ou allaitante, ou mineure. Les marques citées le sont à titre indicatif et n'impliquent ni parrainage ni relation commerciale. Les prix sont indicatifs et peuvent varier selon le pays et le distributeur. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
