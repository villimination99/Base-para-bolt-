# -*- coding: utf-8 -*-
"""
PLAN 11 · ELITE — Coaching semanal 1 a 1
========================================
Formulario de preparación de sesión. El tratamiento es de «usted» en francés
solo en el aviso legal; en el cuerpo se tutea, porque es un documento de
trabajo entre coach y cliente y el tuteo es lo normal en ese contexto en las
tres lenguas.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Sesión 1 a 1</small><span class="glow">COACHING<br>SEMANAL</span>': {
        "en": '<small>One-to-one session</small><span class="glow">WEEKLY<br>COACHING</span>',
        "fr": '<small>Séance individuelle</small><span class="glow">COACHING<br>HEBDOMADAIRE</span>'},
    "Cuatro semanas con un foco distinto cada una. Llega preparado y convierte cada sesión en <em>decisiones</em>, no en conversación.": {
        "en": "Four weeks, each with a different focus. Arrive prepared and turn every session into <em>decisions</em>, not conversation.",
        "fr": "Quatre semaines avec un axe différent chacune. Arrivez préparé et transformez chaque séance en <em>décisions</em>, pas en conversation."},
    '<span class="chip on">4 sesiones</span> <span class="chip on">4 focos distintos</span> <span class="chip">Banco de preguntas</span> <span class="chip">Plan de acción</span>': {
        "en": '<span class="chip on">4 sessions</span> <span class="chip on">4 different focuses</span> <span class="chip">Question bank</span> <span class="chip">Action plan</span>',
        "fr": '<span class="chip on">4 séances</span> <span class="chip on">4 axes différents</span> <span class="chip">Banque de questions</span> <span class="chip">Plan d\'action</span>'},
    "Preguntas sugeridas": {"en": "Suggested questions", "fr": "Questions suggérées"},
    "Objetivos a fijar": {"en": "Targets to set", "fr": "Objectifs à fixer"},
    '<strong>Edición 2026</strong><br><span class="muted">Preparación de sesión 1 a 1 · 10 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">One-to-one session prep · 10 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Préparation de séance individuelle · 10 pages</span>'},

    # ── 01 · Preparación ──────────────────────────────────────────────
    "01 · Cómo preparar la sesión": {
        "en": "01 · How to prepare the session", "fr": "01 · Comment préparer la séance"},
    'APROVECHA <span class="a">CADA MINUTO</span>': {
        "en": 'MAKE <span class="a">EVERY MINUTE</span> COUNT',
        "fr": 'TIREZ PARTI DE <span class="a">CHAQUE MINUTE</span>'},
    "Una sesión de coaching bien preparada vale por tres improvisadas. Estos formularios existen para que llegues con <strong>datos</strong>, no con impresiones, y salgas con <strong>decisiones</strong>, no con buenas intenciones.": {
        "en": "A well-prepared coaching session is worth three improvised ones. These forms exist so that you arrive with <strong>data</strong>, not impressions, and leave with <strong>decisions</strong>, not good intentions.",
        "fr": "Une séance de coaching bien préparée en vaut trois improvisées. Ces formulaires existent pour que vous arriviez avec des <strong>données</strong>, pas des impressions, et repartiez avec des <strong>décisions</strong>, pas de bonnes intentions."},
    "El ritual de los 15 minutos previos": {
        "en": "The 15-minute pre-session ritual", "fr": "Le rituel des 15 minutes avant"},
    "<b>Rellena el formulario la noche antes</b>No en los cinco minutos previos. Necesitas revisar el registro real de la semana con calma.": {
        "en": "<b>Fill in the form the night before</b>Not in the five minutes beforehand. You need to go through the week's actual log calmly.",
        "fr": "<b>Remplissez le formulaire la veille au soir</b>Pas dans les cinq minutes qui précèdent. Vous devez relire au calme le relevé réel de la semaine."},
    "<b>Puntúa con honestidad</b>Un 6 sincero es infinitamente más útil que un 9 de cortesía. Nadie puede ayudarte a corregir lo que le ocultas.": {
        "en": "<b>Score honestly</b>A sincere 6 is infinitely more useful than a polite 9. Nobody can help you fix what you hide from them.",
        "fr": "<b>Notez honnêtement</b>Un 6 sincère est infiniment plus utile qu'un 9 de politesse. Personne ne peut vous aider à corriger ce que vous lui cachez."},
    "<b>Prioriza tus tres preguntas</b>Escríbelas en orden de importancia. Si solo diera tiempo a una, ¿cuál sería?": {
        "en": "<b>Prioritise your three questions</b>Write them in order of importance. If there were time for only one, which would it be?",
        "fr": "<b>Priorisez vos trois questions</b>Écrivez-les par ordre d'importance. S'il n'y avait le temps que pour une, laquelle serait-ce ?"},
    "<b>Trae los números, no la sensación</b>«Me he sentido flojo» sirve poco. «Bajé de 100 a 92,5 kg en press banca y dormí 5,5 horas de media» sirve mucho.": {
        "en": "<b>Bring numbers, not feelings</b>«I felt flat» is not much use. «I dropped from 100 to 92.5 kg on bench press and averaged 5.5 hours of sleep» is very useful.",
        "fr": "<b>Apportez les chiffres, pas les impressions</b>« Je me suis senti mou » ne sert pas à grand-chose. « Je suis passé de 100 à 92,5 kg au développé couché et j'ai dormi 5,5 heures en moyenne » sert beaucoup."},
    "<b>Anota los acuerdos durante la sesión</b>Lo que no queda escrito no se ejecuta.": {
        "en": "<b>Write down the agreements during the session</b>What is not written down does not get done.",
        "fr": "<b>Notez les décisions pendant la séance</b>Ce qui n'est pas écrit ne s'exécute pas."},
    "Estructura de las 4 semanas": {
        "en": "How the 4 weeks are structured", "fr": "Structure des 4 semaines"},
    "Pregunta que responde la sesión": {
        "en": "The question the session answers", "fr": "La question à laquelle répond la séance"},
    '<span class="tag lo">Diagnóstico</span>': {
        "en": '<span class="tag lo">Diagnosis</span>', "fr": '<span class="tag lo">Diagnostic</span>'},
    "¿Dónde estoy exactamente y qué me está frenando?": {
        "en": "Where exactly am I, and what is holding me back?",
        "fr": "Où en suis-je exactement, et qu'est-ce qui me freine ?"},
    '<span class="tag ok">Ajuste</span>': {
        "en": '<span class="tag ok">Adjustment</span>', "fr": '<span class="tag ok">Ajustement</span>'},
    "¿Qué cambio concreto aplico y cómo mido si funciona?": {
        "en": "What specific change do I make, and how do I measure whether it works?",
        "fr": "Quel changement concret j'applique, et comment je mesure s'il marche ?"},
    '<span class="tag mid">Intensificación</span>': {
        "en": '<span class="tag mid">Intensification</span>',
        "fr": '<span class="tag mid">Intensification</span>'},
    "¿Dónde puedo apretar sin romper la recuperación?": {
        "en": "Where can I push harder without breaking recovery?",
        "fr": "Où puis-je pousser sans casser la récupération ?"},
    '<span class="tag hi">Consolidación</span>': {
        "en": '<span class="tag hi">Consolidation</span>',
        "fr": '<span class="tag hi">Consolidation</span>'},
    "¿Qué me llevo del mes y cómo lo mantengo?": {
        "en": "What do I take from the month, and how do I keep it?",
        "fr": "Que je retiens du mois, et comment je le maintiens ?"},
    "Datos que debes tener a mano en cada sesión": {
        "en": "Data to have at hand for every session",
        "fr": "Données à avoir sous la main à chaque séance"},
    "Nutrición": {"en": "Nutrition", "fr": "Nutrition"},
    "Promedio de calorías y proteína reales": {
        "en": "Average actual calories and protein",
        "fr": "Moyenne réelle des calories et des protéines"},
    "Días cumplidos de 7": {"en": "Days met out of 7", "fr": "Jours respectés sur 7"},
    "Peso medio semanal y perímetro de cintura": {
        "en": "Weekly average weight and waist measurement",
        "fr": "Poids moyen hebdomadaire et tour de taille"},
    "Sesiones completadas y cargas principales": {
        "en": "Sessions completed and main loads",
        "fr": "Séances réalisées et charges principales"},
    "Horas de sueño de media": {"en": "Average hours of sleep", "fr": "Heures de sommeil en moyenne"},
    "Molestias o dolores nuevos": {"en": "New aches or pains", "fr": "Gênes ou douleurs nouvelles"},
    "Contacto": {"en": "Contact", "fr": "Contact"},
    "Coach: <strong>@villuminations</strong> · villuminations.com · Reserva y reprogramación de sesiones desde tu área de cliente.": {
        "en": "Coach: <strong>@villuminations</strong> · villuminations.com · Book and reschedule sessions from your customer area.",
        "fr": "Coach : <strong>@villuminations</strong> · villuminations.com · Réservation et report des séances depuis votre espace client."},

    # ── Sesiones ──────────────────────────────────────────────────────
    "Semana 1 · Diagnóstico": {"en": "Week 1 · Diagnosis", "fr": "Semaine 1 · Diagnostic"},
    'SESIÓN 1 · <span class="a">DIAGNÓSTICO</span>': {
        "en": 'SESSION 1 · <span class="a">DIAGNOSIS</span>',
        "fr": 'SÉANCE 1 · <span class="a">DIAGNOSTIC</span>'},
    'Fecha de la sesión: <span class="fill w"></span> &nbsp;·&nbsp; Coach: <strong>@villuminations</strong>': {
        "en": 'Session date: <span class="fill w"></span> &nbsp;·&nbsp; Coach: <strong>@villuminations</strong>',
        "fr": 'Date de la séance : <span class="fill w"></span> &nbsp;·&nbsp; Coach : <strong>@villuminations</strong>'},
    "1 · Resumen de la semana": {"en": "1 · Week in summary", "fr": "1 · Résumé de la semaine"},
    "Aspecto": {"en": "Aspect", "fr": "Aspect"},
    "Nota 1-10": {"en": "Score 1-10", "fr": "Note 1-10"},
    "Comentario": {"en": "Comment", "fr": "Commentaire"},
    "Calidad de los entrenamientos": {
        "en": "Quality of the sessions", "fr": "Qualité des entraînements"},
    "Energía y vitalidad": {"en": "Energy and vitality", "fr": "Énergie et vitalité"},
    "Calidad del sueño": {"en": "Sleep quality", "fr": "Qualité du sommeil"},
    "Estado mental y motivación": {
        "en": "Mental state and motivation", "fr": "État mental et motivation"},
    "2 · Resultados físicos": {"en": "2 · Physical results", "fr": "2 · Résultats physiques"},
    "Esta semana": {"en": "This week", "fr": "Cette semaine"},
    "Tendencia": {"en": "Trend", "fr": "Tendance"},
    '<span class="fill"></span> kg': {
        "en": '<span class="fill"></span> kg', "fr": '<span class="fill"></span> kg'},
    '<span class="box"></span>Sube <span class="box"></span>Baja <span class="box"></span>Igual': {
        "en": '<span class="box"></span>Up <span class="box"></span>Down <span class="box"></span>Same',
        "fr": '<span class="box"></span>Hausse <span class="box"></span>Baisse <span class="box"></span>Stable'},
    '<span class="fill"></span> cm': {
        "en": '<span class="fill"></span> cm', "fr": '<span class="fill"></span> cm'},
    "Récord principal": {"en": "Main personal best", "fr": "Record principal"},
    '<span class="box"></span>Nuevo récord <span class="box"></span>Igual': {
        "en": '<span class="box"></span>New best <span class="box"></span>Same',
        "fr": '<span class="box"></span>Nouveau record <span class="box"></span>Stable'},
    "3 · Foco de esta sesión: punto de partida": {
        "en": "3 · This session's focus: the starting point",
        "fr": "3 · Axe de cette séance : le point de départ"},
    "Pregunta de diagnóstico": {"en": "Diagnostic question", "fr": "Question de diagnostic"},
    "Tu respuesta": {"en": "Your answer", "fr": "Votre réponse"},
    "¿Cuál es tu objetivo principal para los próximos 3 meses?": {
        "en": "What is your main goal for the next 3 months?",
        "fr": "Quel est votre objectif principal pour les 3 prochains mois ?"},
    "¿Qué has intentado antes que no funcionó?": {
        "en": "What have you tried before that did not work?",
        "fr": "Qu'avez-vous déjà essayé qui n'a pas marché ?"},
    "¿Cuál es tu mayor obstáculo real: tiempo, comida, sueño o constancia?": {
        "en": "What is your real biggest obstacle: time, food, sleep or consistency?",
        "fr": "Quel est votre plus grand obstacle réel : temps, alimentation, sommeil ou régularité ?"},
    "¿Cuántos días a la semana puedes entrenar de forma realista?": {
        "en": "How many days a week can you realistically train?",
        "fr": "Combien de jours par semaine pouvez-vous réellement vous entraîner ?"},
    "¿Hay lesiones, molestias o limitaciones médicas a tener en cuenta?": {
        "en": "Are there injuries, aches or medical limitations to take into account?",
        "fr": "Y a-t-il des blessures, des gênes ou des limitations médicales à prendre en compte ?"},
    "4 · Tus preguntas para el coach": {
        "en": "4 · Your questions for the coach", "fr": "4 · Vos questions pour le coach"},
    "5 · Objetivos para la próxima semana": {
        "en": "5 · Targets for next week", "fr": "5 · Objectifs pour la semaine prochaine"},
    "Área": {"en": "Area", "fr": "Domaine"},
    "Objetivo concreto y medible": {
        "en": "Specific, measurable target", "fr": "Objectif concret et mesurable"},
    "Entrenamiento": {"en": "Training", "fr": "Entraînement"},
    "Recuperación": {"en": "Recovery", "fr": "Récupération"},
    "Semana 2 · Ajuste": {"en": "Week 2 · Adjustment", "fr": "Semaine 2 · Ajustement"},
    'SESIÓN 2 · <span class="a">AJUSTE</span>': {
        "en": 'SESSION 2 · <span class="a">ADJUSTMENT</span>',
        "fr": 'SÉANCE 2 · <span class="a">AJUSTEMENT</span>'},
    "3 · Foco de esta sesión: revisión de los acuerdos": {
        "en": "3 · This session's focus: reviewing the agreements",
        "fr": "3 · Axe de cette séance : revue des engagements"},
    "Objetivo fijado la semana pasada": {
        "en": "Target set last week", "fr": "Objectif fixé la semaine dernière"},
    "¿Cumplido?": {"en": "Met?", "fr": "Atteint ?"},
    "Qué lo facilitó o lo impidió": {
        "en": "What helped or got in the way", "fr": "Ce qui l'a facilité ou empêché"},
    '<span class="box"></span>Sí <span class="box"></span>No': {
        "en": '<span class="box"></span>Yes <span class="box"></span>No',
        "fr": '<span class="box"></span>Oui <span class="box"></span>Non'},
    "Pregunta de ajuste": {"en": "Adjustment question", "fr": "Question d'ajustement"},
    "¿Qué variable vas a cambiar esta semana? (una sola)": {
        "en": "Which variable will you change this week? (only one)",
        "fr": "Quelle variable allez-vous changer cette semaine ? (une seule)"},
    "¿Cómo sabrás dentro de 7 días si ha funcionado?": {
        "en": "How will you know in 7 days whether it worked?",
        "fr": "Comment saurez-vous dans 7 jours si cela a marché ?"},
    "Semana 3 · Intensificación": {
        "en": "Week 3 · Intensification", "fr": "Semaine 3 · Intensification"},
    'SESIÓN 3 · <span class="a">INTENSIFICACIÓN</span>': {
        "en": 'SESSION 3 · <span class="a">INTENSIFICATION</span>',
        "fr": 'SÉANCE 3 · <span class="a">INTENSIFICATION</span>'},
    "3 · Margen de recuperación": {
        "en": "3 · Recovery headroom", "fr": "3 · Marge de récupération"},
    "Indicador de recuperación": {"en": "Recovery indicator", "fr": "Indicateur de récupération"},
    "Estado": {"en": "Status", "fr": "État"},
    "Agujetas que alteran la técnica": {
        "en": "Soreness that alters technique", "fr": "Courbatures qui altèrent la technique"},
    "Molestia articular nueva": {"en": "New joint discomfort", "fr": "Gêne articulaire nouvelle"},
    "Ganas reales de entrenar": {
        "en": "Genuine desire to train", "fr": "Envie réelle de s'entraîner"},
    "Pregunta de intensificación": {
        "en": "Intensification question", "fr": "Question d'intensification"},
    "¿Dónde tienes margen: más volumen, más carga o más frecuencia?": {
        "en": "Where do you have headroom: more volume, more load or more frequency?",
        "fr": "Où avez-vous de la marge : plus de volume, plus de charge ou plus de fréquence ?"},
    "¿Qué tendrías que recortar para poder asumir ese aumento?": {
        "en": "What would you have to cut back to absorb that increase?",
        "fr": "Que devriez-vous réduire pour absorber cette augmentation ?"},
    "Semana 4 · Consolidación": {
        "en": "Week 4 · Consolidation", "fr": "Semaine 4 · Consolidation"},
    'SESIÓN 4 · <span class="a">CONSOLIDACIÓN</span>': {
        "en": 'SESSION 4 · <span class="a">CONSOLIDATION</span>',
        "fr": 'SÉANCE 4 · <span class="a">CONSOLIDATION</span>'},
    "3 · Foco de esta sesión: qué se queda para siempre": {
        "en": "3 · This session's focus: what stays for good",
        "fr": "3 · Axe de cette séance : ce qui reste pour de bon"},
    "Pregunta de cierre": {"en": "Closing question", "fr": "Question de clôture"},
    "¿Qué hábito de este mes ya no te cuesta esfuerzo?": {
        "en": "Which habit from this month no longer takes effort?",
        "fr": "Quelle habitude de ce mois ne vous demande plus d'effort ?"},
    "¿Cuál sigue costándote y por qué?": {
        "en": "Which one still costs you, and why?",
        "fr": "Laquelle vous coûte encore, et pourquoi ?"},
    "¿Qué cambio ha tenido mayor impacto en tus resultados?": {
        "en": "Which change had the biggest impact on your results?",
        "fr": "Quel changement a eu le plus d'impact sur vos résultats ?"},
    "¿Qué harías distinto si repitieras el mes?": {
        "en": "What would you do differently if you repeated the month?",
        "fr": "Que feriez-vous différemment si vous refaisiez le mois ?"},
    "¿Qué objetivo te pones para el mes siguiente?": {
        "en": "What target are you setting for next month?",
        "fr": "Quel objectif vous fixez-vous pour le mois suivant ?"},

    # ── Métricas del mes ──────────────────────────────────────────────
    "Métricas del mes": {"en": "Month metrics", "fr": "Indicateurs du mois"},
    'EL MES <span class="a">EN UNA PÁGINA</span>': {
        "en": 'THE MONTH <span class="a">ON ONE PAGE</span>',
        "fr": 'LE MOIS <span class="a">EN UNE PAGE</span>'},
    "Evolución de las cuatro semanas": {
        "en": "How the four weeks evolved", "fr": "Évolution des quatre semaines"},
    "Peso corporal (kg)": {"en": "Body weight (kg)", "fr": "Poids corporel (kg)"},
    "Adherencia (días/7)": {"en": "Adherence (days/7)", "fr": "Observance (jours/7)"},
    "Sueño (h de media)": {"en": "Sleep (avg h)", "fr": "Sommeil (h en moyenne)"},
    "Energía media (1-10)": {"en": "Average energy (1-10)", "fr": "Énergie moyenne (1-10)"},
    "Récords personales conseguidos": {
        "en": "Personal bests achieved", "fr": "Records personnels obtenus"},
    "Los tres momentos clave del mes": {
        "en": "The month's three key moments", "fr": "Les trois moments clés du mois"},
    "Qué pasó y qué aprendiste": {
        "en": "What happened and what you learned", "fr": "Ce qui s'est passé et ce que vous en retenez"},
    "Mi mejor sesión": {"en": "My best session", "fr": "Ma meilleure séance"},
    "Mi semana más difícil": {"en": "My hardest week", "fr": "Ma semaine la plus difficile"},
    "La decisión más acertada": {"en": "The best decision I made", "fr": "La décision la plus juste"},

    # ── Banco de preguntas ────────────────────────────────────────────
    "Banco de preguntas": {"en": "Question bank", "fr": "Banque de questions"},
    '30 PREGUNTAS QUE <span class="a">MERECE LA PENA HACER</span>': {
        "en": '30 QUESTIONS <span class="a">WORTH ASKING</span>',
        "fr": '30 QUESTIONS QUI <span class="a">VALENT LA PEINE</span>'},
    "Si no sabes qué preguntar, elige de aquí. Marca las que quieras llevar a tu próxima sesión.": {
        "en": "If you do not know what to ask, pick from here. Tick the ones you want to take to your next session.",
        "fr": "Si vous ne savez pas quoi demander, choisissez ici. Cochez celles que vous voulez emporter à votre prochaine séance."},
    "¿Mis calorías actuales encajan con mi objetivo o voy demasiado agresivo?": {
        "en": "Do my current calories fit my goal, or am I being too aggressive?",
        "fr": "Mes calories actuelles correspondent-elles à mon objectif, ou suis-je trop agressif ?"},
    "¿Cómo ajusto los macros los días que no puedo entrenar?": {
        "en": "How do I adjust macros on days I cannot train?",
        "fr": "Comment ajuster les macros les jours où je ne peux pas m'entraîner ?"},
    "¿Qué hago cuando como fuera de casa varios días seguidos?": {
        "en": "What do I do when I eat out several days in a row?",
        "fr": "Que faire quand je mange dehors plusieurs jours d'affilée ?"},
    "¿Estoy comiendo suficiente proteína para el volumen de entrenamiento que llevo?": {
        "en": "Am I eating enough protein for the training volume I am doing?",
        "fr": "Est-ce que je mange assez de protéines pour le volume d'entraînement que j'ai ?"},
    "¿Merece la pena que cicle carbohidratos en mi caso concreto?": {
        "en": "Is carb cycling worth it in my specific case?",
        "fr": "Le cyclage des glucides vaut-il la peine dans mon cas précis ?"},
    "¿Cómo gestiono un fin de semana con evento social sin tirar la semana?": {
        "en": "How do I handle a weekend with a social event without wrecking the week?",
        "fr": "Comment gérer un week-end avec un événement social sans gâcher la semaine ?"},
    "¿Cuánto tiempo debería mantener este déficit antes de una fase de mantenimiento?": {
        "en": "How long should I keep this deficit before a maintenance phase?",
        "fr": "Combien de temps garder ce déficit avant une phase de maintenance ?"},
    "¿Mi peso se ha estancado por adaptación o porque estoy midiendo mal?": {
        "en": "Has my weight stalled because of adaptation, or because I am measuring badly?",
        "fr": "Mon poids stagne-t-il par adaptation ou parce que je mesure mal ?"},
    "¿Mi volumen semanal por grupo muscular es el adecuado para mi nivel?": {
        "en": "Is my weekly volume per muscle group right for my level?",
        "fr": "Mon volume hebdomadaire par groupe musculaire convient-il à mon niveau ?"},
    "¿Estoy progresando a buen ritmo en los ejercicios principales?": {
        "en": "Am I progressing at a good rate on the main lifts?",
        "fr": "Est-ce que je progresse à bon rythme sur les exercices principaux ?"},
    "¿Qué ejercicio debería sustituir por esta molestia concreta?": {
        "en": "Which exercise should I swap out because of this particular discomfort?",
        "fr": "Quel exercice remplacer à cause de cette gêne précise ?"},
    "¿Cómo sé si estoy entrenando demasiado cerca del fallo?": {
        "en": "How do I know if I am training too close to failure?",
        "fr": "Comment savoir si je m'entraîne trop près de l'échec ?"},
    "¿Debería cambiar de rutina o seguir con esta más tiempo?": {
        "en": "Should I change programme or stay on this one longer?",
        "fr": "Dois-je changer de programme ou continuer celui-ci plus longtemps ?"},
    "¿Cuánto cardio puedo meter sin comprometer la fuerza?": {
        "en": "How much cardio can I add without compromising strength?",
        "fr": "Combien de cardio puis-je ajouter sans compromettre la force ?"},
    "¿Cómo estructuro la semana si solo puedo entrenar 3 días?": {
        "en": "How do I structure the week if I can only train 3 days?",
        "fr": "Comment structurer la semaine si je ne peux m'entraîner que 3 jours ?"},
    "¿Mi técnica en este ejercicio es correcta? (trae vídeo)": {
        "en": "Is my technique on this lift correct? (bring video)",
        "fr": "Ma technique sur cet exercice est-elle correcte ? (apportez une vidéo)"},
    "Recuperación y hábitos": {"en": "Recovery and habits", "fr": "Récupération et habitudes"},
    "¿Necesito una semana de descarga ahora mismo?": {
        "en": "Do I need a deload week right now?",
        "fr": "Ai-je besoin d'une semaine de décharge maintenant ?"},
    "¿Cómo mejoro mi sueño con mi horario de trabajo actual?": {
        "en": "How do I improve my sleep with my current work schedule?",
        "fr": "Comment améliorer mon sommeil avec mes horaires de travail actuels ?"},
    "¿Qué hago los días que llego sin energía al gimnasio?": {
        "en": "What do I do on days I arrive at the gym with no energy?",
        "fr": "Que faire les jours où j'arrive sans énergie à la salle ?"},
    "¿Es normal el nivel de agujetas que tengo?": {
        "en": "Is the level of soreness I have normal?",
        "fr": "Le niveau de courbatures que j'ai est-il normal ?"},
    "¿Cómo gestiono las semanas de mucho estrés laboral?": {
        "en": "How do I manage weeks with heavy work stress?",
        "fr": "Comment gérer les semaines de fort stress professionnel ?"},
    "¿Debería añadir movilidad o trabajo de core?": {
        "en": "Should I add mobility or core work?",
        "fr": "Devrais-je ajouter de la mobilité ou du gainage ?"},
    "Suplementación y estrategia": {
        "en": "Supplementation and strategy", "fr": "Compléments et stratégie"},
    "¿Merece la pena algún suplemento nuevo en mi situación?": {
        "en": "Is any new supplement worth it in my situation?",
        "fr": "Un nouveau complément vaut-il la peine dans ma situation ?"},
    "¿Estoy tomando la creatina de forma correcta?": {
        "en": "Am I taking creatine correctly?",
        "fr": "Est-ce que je prends la créatine correctement ?"},
    "¿Qué prioridad tiene cada cosa si mi presupuesto es limitado?": {
        "en": "What takes priority if my budget is limited?",
        "fr": "Quelle priorité donner à chaque chose si mon budget est limité ?"},
    "¿Qué expectativa realista de resultados tengo a 3 y 6 meses?": {
        "en": "What is a realistic expectation of results at 3 and 6 months?",
        "fr": "Quelle attente réaliste de résultats à 3 et 6 mois ?"},
    "¿Qué métrica debería vigilar más y cuál está distrayéndome?": {
        "en": "Which metric should I watch more, and which one is distracting me?",
        "fr": "Quel indicateur surveiller davantage, et lequel me distrait ?"},
    "¿Voy por buen camino o me estoy engañando con los datos?": {
        "en": "Am I on the right track, or am I fooling myself with the data?",
        "fr": "Suis-je sur la bonne voie, ou est-ce que je me trompe moi-même avec les données ?"},
    "¿Qué me recomendarías si solo pudiera cambiar una cosa este mes?": {
        "en": "What would you recommend if I could change only one thing this month?",
        "fr": "Que me recommanderiez-vous si je ne pouvais changer qu'une chose ce mois-ci ?"},
    "¿Cuál es el siguiente paso lógico cuando termine este bloque?": {
        "en": "What is the logical next step when this block ends?",
        "fr": "Quelle est l'étape logique suivante à la fin de ce bloc ?"},

    # ── Plan de acción ────────────────────────────────────────────────
    "Plan de acción": {"en": "Action plan", "fr": "Plan d'action"},
    'PLAN DE ACCIÓN DEL <span class="a">MES SIGUIENTE</span>': {
        "en": '<span class="a">NEXT MONTH\'S</span> ACTION PLAN',
        "fr": "PLAN D'ACTION DU <span class=\"a\">MOIS SUIVANT</span>"},
    "Objetivo principal": {"en": "Main goal", "fr": "Objectif principal"},
    "Mi objetivo para las próximas 4 semanas": {
        "en": "My goal for the next 4 weeks", "fr": "Mon objectif pour les 4 prochaines semaines"},
    "Cómo lo voy a medir": {"en": "How I will measure it", "fr": "Comment je vais le mesurer"},
    "Indicador": {"en": "Indicator", "fr": "Indicateur"},
    "Valor actual": {"en": "Current value", "fr": "Valeur actuelle"},
    "Valor objetivo": {"en": "Target value", "fr": "Valeur cible"},
    "Fecha de revisión": {"en": "Review date", "fr": "Date de revue"},
    "Los tres hábitos innegociables": {
        "en": "The three non-negotiable habits", "fr": "Les trois habitudes non négociables"},
    "Hábito": {"en": "Habit", "fr": "Habitude"},
    "Cuándo y dónde exactamente": {
        "en": "Exactly when and where", "fr": "Quand et où exactement"},
    "Obstáculos previstos y plan B": {
        "en": "Expected obstacles and plan B", "fr": "Obstacles prévus et plan B"},
    "Si ocurre esto…": {"en": "If this happens…", "fr": "Si ceci arrive…"},
    "…haré esto": {"en": "…I will do this", "fr": "…je ferai cela"},
    "Seguimiento semanal": {"en": "Weekly follow-up", "fr": "Suivi hebdomadaire"},
    "Hábito 1": {"en": "Habit 1", "fr": "Habitude 1"},
    "Hábito 2": {"en": "Habit 2", "fr": "Habitude 2"},
    "Hábito 3": {"en": "Habit 3", "fr": "Habitude 3"},
    "Nota de la semana": {"en": "Week's score", "fr": "Note de la semaine"},
    "Un objetivo, tres hábitos": {"en": "One goal, three habits", "fr": "Un objectif, trois habitudes"},
    "Más de tres hábitos nuevos a la vez tiene una tasa de fracaso altísima. Elige los tres que más mueven la aguja y protégelos por encima de todo lo demás.": {
        "en": "More than three new habits at once has an enormous failure rate. Pick the three that move the needle most and protect them above everything else.",
        "fr": "Plus de trois nouvelles habitudes à la fois : le taux d'échec est énorme. Choisissez les trois qui font le plus de différence et protégez-les avant tout le reste."},

    # ── Cierre ────────────────────────────────────────────────────────
    "Cierre": {"en": "Closing", "fr": "Clôture"},
    'LOS SEIS FRENTES DE <span class="a">UN MES BIEN LLEVADO</span>': {
        "en": 'THE SIX FRONTS OF <span class="a">A MONTH DONE WELL</span>',
        "fr": 'LES SIX FRONTS D\'<span class="a">UN MOIS BIEN MENÉ</span>'},
    "Frente": {"en": "Front", "fr": "Front"},
    "Qué decide": {"en": "What it decides", "fr": "Ce qu'il décide"},
    "Con qué frecuencia": {"en": "How often", "fr": "À quelle fréquence"},
    "Fuerza estructurada": {"en": "Structured strength", "fr": "Force structurée"},
    "Progresión medible en los movimientos principales": {
        "en": "Measurable progression on the main movements",
        "fr": "Progression mesurable sur les mouvements principaux"},
    "Todo el bloque": {"en": "The whole block", "fr": "Tout le bloc"},
    "Trabajo metabólico": {"en": "Metabolic work", "fr": "Travail métabolique"},
    "Capacidad de esfuerzo y gasto complementario": {
        "en": "Work capacity and complementary expenditure",
        "fr": "Capacité d'effort et dépense complémentaire"},
    "2–4 veces por semana": {"en": "2–4 times a week", "fr": "2 à 4 fois par semaine"},
    "Base alimentaria": {"en": "Nutritional base", "fr": "Base alimentaire"},
    "Energía, proteína y calidad del patrón": {
        "en": "Energy, protein and the quality of the pattern",
        "fr": "Énergie, protéines et qualité du schéma"},
    "A diario": {"en": "Daily", "fr": "Quotidien"},
    "Descanso nocturno": {"en": "Night-time rest", "fr": "Repos nocturne"},
    "Todo lo anterior se consolida aquí o no se consolida": {
        "en": "Everything above consolidates here, or it does not consolidate",
        "fr": "Tout ce qui précède se consolide ici, ou ne se consolide pas"},
    "Cada noche": {"en": "Every night", "fr": "Chaque nuit"},
    "Cabeza y foco": {"en": "Head and focus", "fr": "Tête et concentration"},
    "Adherencia, gestión del estrés y vuelta tras un fallo": {
        "en": "Adherence, stress management and getting back after a slip",
        "fr": "Observance, gestion du stress et retour après un écart"},
    "Revisión con datos": {"en": "Review with data", "fr": "Revue avec les données"},
    "Qué se mantiene, qué se ajusta y qué se retira": {
        "en": "What stays, what gets adjusted and what gets dropped",
        "fr": "Ce qu'on garde, ce qu'on ajuste et ce qu'on retire"},
    "Una vez por semana": {"en": "Once a week", "fr": "Une fois par semaine"},
    "La sesión semanal es la que une los seis": {
        "en": "The weekly session is what joins all six",
        "fr": "La séance hebdomadaire est ce qui relie les six"},
    "Cada frente por separado se puede llevar bien y aun así no avanzar, porque el\n        que falla arrastra a los demás. La sesión de la semana existe para mirar los seis a la vez\n        y decidir <strong>cuál es el que hay que tocar</strong>, que casi nunca es el que uno\n        creía.": {
        "en": "You can handle each front well on its own and still not move forward, because the one that fails drags the rest with it. The weekly session exists to look at all six at once and decide <strong>which one needs changing</strong> — and it is almost never the one you thought.",
        "fr": "Chaque front pris séparément peut être bien mené sans que vous avanciez pour autant, car celui qui flanche entraîne les autres. La séance hebdomadaire existe pour regarder les six d'un coup et décider <strong>lequel il faut toucher</strong> — et ce n'est presque jamais celui qu'on croyait."},
    'NOS VEMOS EN <span class="a">LA PRÓXIMA SESIÓN</span>': {
        "en": 'SEE YOU AT <span class="a">THE NEXT SESSION</span>',
        "fr": 'À <span class="a">LA PROCHAINE SÉANCE</span>'},
    "Reserva, reprograma y consulta tus documentos desde tu área de\n        cliente en la tienda.": {
        "en": "Book, reschedule and access your documents from your customer area in the store.",
        "fr": "Réservez, reprogrammez et consultez vos documents depuis votre espace client dans la boutique."},
    "<b>Aviso importante</b><br>\n      Este formulario tiene finalidad organizativa y educativa. El servicio de coaching de\n      VILLUMINATIONS consiste en orientación sobre entrenamiento y hábitos, y no constituye\n      consejo médico, diagnóstico, tratamiento ni terapia nutricional individualizada. No\n      sustituye la valoración de un profesional sanitario colegiado, un dietista-nutricionista\n      ni un fisioterapeuta. Consulta con tu médico antes de iniciar o modificar cualquier plan\n      de entrenamiento o alimentación, especialmente si padeces alguna patología, tomas\n      medicación, estás embarazada o en periodo de lactancia, o eres menor de edad. Los datos\n      personales y de salud que compartas se tratarán de forma confidencial y conforme a la\n      normativa de protección de datos aplicable. Los resultados varían entre personas y no\n      están garantizados. Contenido protegido por derechos de autor: prohibida su reproducción,\n      distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      This form is for organisational and educational purposes. The VILLUMINATIONS coaching service consists of guidance on training and habits, and does not constitute medical advice, diagnosis, treatment or individualised nutritional therapy. It does not replace assessment by a registered health professional, a dietitian or a physiotherapist. Consult your doctor before starting or modifying any training or nutrition plan, especially if you have a medical condition, take medication, are pregnant or breastfeeding, or are a minor. Personal and health data you share will be handled confidentially and in accordance with applicable data protection law. Results vary between individuals and are not guaranteed. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Ce formulaire a une finalité organisationnelle et éducative. Le service de coaching VILLUMINATIONS consiste en un accompagnement sur l'entraînement et les habitudes, et ne constitue ni un avis médical, ni un diagnostic, ni un traitement, ni une thérapie nutritionnelle individualisée. Il ne remplace pas l'évaluation d'un professionnel de santé, d'un diététicien ni d'un kinésithérapeute. Consultez votre médecin avant d'entreprendre ou de modifier tout programme d'entraînement ou d'alimentation, en particulier en cas de pathologie, de traitement, de grossesse ou d'allaitement, ou si vous êtes mineur. Les données personnelles et de santé que vous partagez seront traitées de façon confidentielle et conformément à la réglementation applicable. Les résultats varient et ne sont pas garantis. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
