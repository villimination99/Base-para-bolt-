# -*- coding: utf-8 -*-
"""
07 · 10 RUTINAS HIIT — inglés y francés
=======================================
Los nombres propios de las rutinas (Tabata, EMOM, Full Body Fury…) no se
traducen: son la etiqueta con la que el comprador las busca en su registro y
cambiarlas por idioma rompería la correspondencia entre la tabla de progresión
y las fichas de cada sesión.

Los nombres de los ejercicios sí se traducen, porque son instrucciones. En
francés se conserva el anglicismo cuando es el término real de la sala
(burpee, mountain climber, jumping jack, AMRAP); inventar un equivalente
haría el documento menos utilizable, no más francés.
"""

T = {

    # ── Portada ────────────────────────────────────────────────────────────
    '<small>Sin equipo · 15 a 30 min</small><span class="glow">10 RUTINAS<br>HIIT</span>': {
        "en": '<small>No equipment · 15 to 30 min</small><span class="glow">10 HIIT<br>ROUTINES</span>',
        "fr": '<small>Sans matériel · 15 à 30 min</small><span class="glow">10 SÉANCES<br>HIIT</span>'},

    "Máximo estímulo metabólico en el mínimo tiempo, con la estructura "
    "exacta para <em>no</em> sacrificar el músculo que has construido.": {
        "en": "Maximum metabolic stimulus in the minimum time, with the exact "
              "structure needed <em>not</em> to sacrifice the muscle you have built.",
        "fr": "Un stimulus métabolique maximal en un minimum de temps, avec la "
              "structure exacte pour <em>ne pas</em> sacrifier le muscle que vous avez construit."},

    '<span class="chip on">10 rutinas completas</span> '
    '<span class="chip on">Sin equipo</span> '
    '<span class="chip">Progresión 8 semanas</span> '
    '<span class="chip">3 niveles</span>': {
        "en": '<span class="chip on">10 complete routines</span> '
              '<span class="chip on">No equipment</span> '
              '<span class="chip">8-week progression</span> '
              '<span class="chip">3 levels</span>',
        "fr": '<span class="chip on">10 séances complètes</span> '
              '<span class="chip on">Sans matériel</span> '
              '<span class="chip">Progression sur 8 semaines</span> '
              '<span class="chip">3 niveaux</span>'},

    "Rutinas": {"en": "Routines", "fr": "Séances"},
    "Minutos por sesión": {"en": "Minutes per session", "fr": "Minutes par séance"},
    "Niveles de escalado": {"en": "Scaling levels", "fr": "Niveaux d'adaptation"},

    '<strong>Edición 2026</strong><br><span class="muted">Protocolos de alta intensidad · 9 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">High-intensity protocols · 9 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Protocoles de haute intensité · 9 pages</span>'},

    # ── 01 · Cómo usar el HIIT ─────────────────────────────────────────────
    "01 · Cómo usar el HIIT": {
        "en": "01 · How to use HIIT", "fr": "01 · Comment utiliser le HIIT"},

    'ANTES DE LA <span class="a">PRIMERA RONDA</span>': {
        "en": 'BEFORE THE <span class="a">FIRST ROUND</span>',
        "fr": 'AVANT LE <span class="a">PREMIER ROUND</span>'},

    "El HIIT es potente y por eso fácil de sobredosificar: hecho bien quema grasa "
    "y mejora tu capacidad de trabajo; hecho mal te roba la recuperación de las pesas.": {
        "en": "HIIT is powerful, and that is exactly why it is easy to overdose: done "
              "well it burns fat and raises your work capacity; done badly it steals "
              "the recovery your lifting depends on.",
        "fr": "Le HIIT est puissant, et c'est précisément pour cela qu'il est facile "
              "d'en abuser : bien mené, il brûle de la graisse et augmente votre "
              "capacité de travail ; mal mené, il vole la récupération dont vos "
              "séances de force dépendent."},

    "<b>Fig. 1</b>Intervalos y frecuencia cardiaca": {
        "en": "<b>Fig. 1</b>Intervals and heart rate",
        "fr": "<b>Fig. 1</b>Intervalles et fréquence cardiaque"},

    "Los bloques naranjas son trabajo máximo y los azules descanso activo. "
    "Fíjate en que la curva de pulso <b>no baja del todo</b> entre intervalos.": {
        "en": "The orange blocks are all-out work and the blue ones active rest. "
              "Notice that the heart-rate curve <b>never comes all the way down</b> "
              "between intervals.",
        "fr": "Les blocs orange correspondent au travail maximal et les bleus à la "
              "récupération active. Remarquez que la courbe de pouls <b>ne redescend "
              "jamais complètement</b> entre les intervalles."},

    "Las cinco reglas del HIIT inteligente": {
        "en": "The five rules of intelligent HIIT",
        "fr": "Les cinq règles du HIIT intelligent"},

    "<b>Nunca el día antes de piernas</b>Ni el mismo día después. El HIIT compite "
    "directamente con tu sesión de tren inferior por los mismos recursos.": {
        "en": "<b>Never the day before leg day</b>Nor the day right after. HIIT "
              "competes directly with your lower-body session for the same resources.",
        "fr": "<b>Jamais la veille du jour des jambes</b>Ni le lendemain. Le HIIT "
              "entre en concurrence directe avec votre séance de bas du corps pour "
              "les mêmes ressources."},

    "<b>Calienta 5 minutos siempre</b>Movilidad de cadera y tobillo, 20 jumping jacks, "
    "10 sentadillas sin peso y 10 rotaciones de hombro. No es opcional.": {
        "en": "<b>Always warm up for 5 minutes</b>Hip and ankle mobility, 20 jumping "
              "jacks, 10 bodyweight squats and 10 shoulder rotations. It is not optional.",
        "fr": "<b>Échauffez-vous toujours 5 minutes</b>Mobilité de hanche et de "
              "cheville, 20 jumping jacks, 10 squats au poids du corps et 10 rotations "
              "d'épaules. Ce n'est pas facultatif."},

    "<b>El intervalo es al máximo o no es HIIT</b>Si puedes mantener una conversación "
    "durante el trabajo, estás haciendo cardio moderado con nombre elegante.": {
        "en": "<b>The interval is all-out or it is not HIIT</b>If you can hold a "
              "conversation during the work phase, you are doing moderate cardio under "
              "a fancier name.",
        "fr": "<b>L'intervalle est maximal, sinon ce n'est pas du HIIT</b>Si vous "
              "pouvez tenir une conversation pendant la phase de travail, vous faites "
              "du cardio modéré sous un nom plus élégant."},

    "<b>El descanso también es parte del entrenamiento</b>Respira por la nariz y camina. "
    "Recortarlo no lo hace más efectivo, solo peor ejecutado.": {
        "en": "<b>Rest is part of the training too</b>Breathe through your nose and keep "
              "walking. Cutting it short does not make the session more effective, only "
              "worse executed.",
        "fr": "<b>Le repos fait aussi partie de l'entraînement</b>Respirez par le nez et "
              "marchez. Le raccourcir ne rend pas la séance plus efficace, seulement "
              "moins bien exécutée."},

    "<b>Registra rondas y repeticiones</b>Progresar en HIIT es hacer más trabajo en el "
    "mismo tiempo, no simplemente terminar reventado.": {
        "en": "<b>Log your rounds and reps</b>Progressing in HIIT means doing more work "
              "in the same time, not simply finishing wrecked.",
        "fr": "<b>Notez vos rounds et vos répétitions</b>Progresser en HIIT, c'est faire "
              "plus de travail dans le même temps, pas seulement finir à bout de souffle."},

    "Cuándo NO hacer HIIT": {
        "en": "When NOT to do HIIT", "fr": "Quand NE PAS faire de HIIT"},

    "Has dormido menos de 6 horas o vienes de tres noches malas seguidas.": {
        "en": "You have slept less than 6 hours, or you are coming off three bad nights "
              "in a row.",
        "fr": "Vous avez dormi moins de 6 heures ou vous enchaînez trois mauvaises nuits."},

    "Tienes agujetas intensas que alteran tu técnica.": {
        "en": "You have severe muscle soreness that alters your technique.",
        "fr": "Vous avez des courbatures intenses qui altèrent votre technique."},

    "Estás en la última semana de un déficit calórico agresivo y la fuerza está cayendo.": {
        "en": "You are in the final week of an aggressive calorie deficit and your "
              "strength is dropping.",
        "fr": "Vous êtes dans la dernière semaine d'un déficit calorique agressif et "
              "votre force baisse."},

    "Notas molestia articular en rodilla, tobillo, hombro o zona lumbar.": {
        "en": "You feel joint discomfort in a knee, an ankle, a shoulder or your lower back.",
        "fr": "Vous ressentez une gêne articulaire au genou, à la cheville, à l'épaule "
              "ou dans le bas du dos."},

    "Señal de alarma: para inmediatamente": {
        "en": "Warning sign: stop immediately",
        "fr": "Signal d'alarme : arrêtez immédiatement"},

    "Dolor en el pecho, mareo, visión borrosa, náuseas intensas o falta de aire "
    "desproporcionada. Detén la sesión, siéntate y busca atención médica si no remite en "
    "pocos minutos.": {
        "en": "Chest pain, dizziness, blurred vision, severe nausea or breathlessness out "
              "of all proportion to the effort. Stop the session, sit down and seek "
              "medical attention if it does not pass within a few minutes.",
        "fr": "Douleur thoracique, vertige, vision trouble, nausées intenses ou "
              "essoufflement disproportionné. Arrêtez la séance, asseyez-vous et "
              "consultez un médecin si cela ne passe pas en quelques minutes."},

    # ── Cabeceras de las fichas ────────────────────────────────────────────
    "Trabajo": {"en": "Work", "fr": "Travail"},
    "Rondas": {"en": "Rounds", "fr": "Rounds"},
    "Músculo principal": {"en": "Main muscle", "fr": "Muscle principal"},
    "Bloque": {"en": "Block", "fr": "Bloc"},
    "Trabajo por minuto": {"en": "Work per minute", "fr": "Travail par minute"},
    "Minutos": {"en": "Minutes", "fr": "Minutes"},
    "Vueltas": {"en": "Circuits", "fr": "Tours"},
    "Orden": {"en": "Order", "fr": "Ordre"},

    # ── Rutinas 1 y 2 ──────────────────────────────────────────────────────
    "Rutinas 1 y 2": {"en": "Routines 1 and 2", "fr": "Séances 1 et 2"},

    '01 · TABATA <span class="a">CLÁSICO</span> — 20 MIN': {
        "en": '01 · CLASSIC <span class="a">TABATA</span> — 20 MIN',
        "fr": '01 · TABATA <span class="a">CLASSIQUE</span> — 20 MIN'},

    "El protocolo HIIT más estudiado. Cuatro bloques de 8 rondas, con "
    '1 minuto de descanso entre bloques. <span class="tag mid">Nivel medio</span>': {
        "en": "The most studied HIIT protocol there is. Four blocks of 8 rounds, with "
              '1 minute of rest between blocks. <span class="tag mid">Medium level</span>',
        "fr": "Le protocole HIIT le plus étudié. Quatre blocs de 8 rounds, avec "
              '1 minute de repos entre les blocs. <span class="tag mid">Niveau moyen</span>'},

    "Burpees": {"en": "Burpees", "fr": "Burpees"},
    "Todo el cuerpo": {"en": "Full body", "fr": "Corps entier"},
    "Saltos de estrella": {"en": "Star jumps", "fr": "Sauts en étoile"},
    "Cardio y piernas": {"en": "Cardio and legs", "fr": "Cardio et jambes"},
    "Escaladores": {"en": "Mountain climbers", "fr": "Mountain climbers"},
    "Core y cardio": {"en": "Core and cardio", "fr": "Gainage et cardio"},
    "Sentadillas con salto": {"en": "Jump squats", "fr": "Squats sautés"},
    "Piernas y glúteos": {"en": "Legs and glutes", "fr": "Jambes et fessiers"},

    '02 · HIIT <span class="a">40/20</span> — 24 MIN': {
        "en": '02 · HIIT <span class="a">40/20</span> — 24 MIN',
        "fr": '02 · HIIT <span class="a">40/20</span> — 24 MIN'},

    "Más tiempo bajo trabajo para acumular volumen. La mejor opción cuando el "
    'objetivo principal es el gasto calórico. <span class="tag hi">Nivel alto</span>': {
        "en": "More time under work to accumulate volume. The best option when the main "
              'goal is calorie expenditure. <span class="tag hi">High level</span>',
        "fr": "Plus de temps sous travail pour accumuler du volume. La meilleure option "
              'quand l\'objectif principal est la dépense calorique. <span class="tag hi">Niveau élevé</span>'},

    "Sprints en el sitio": {"en": "Sprints in place", "fr": "Sprints sur place"},
    "Cardio total": {"en": "Whole-body cardio", "fr": "Cardio complet"},
    "Zancadas con salto": {"en": "Jump lunges", "fr": "Fentes sautées"},
    "Flexiones explosivas": {"en": "Explosive push-ups", "fr": "Pompes explosives"},
    "Pecho y tríceps": {"en": "Chest and triceps", "fr": "Pectoraux et triceps"},
    "Rodillas al pecho": {"en": "High knees", "fr": "Montées de genoux"},
    "Cardio y core": {"en": "Cardio and core", "fr": "Cardio et gainage"},

    "Cómo se recorre la rutina": {
        "en": "How to run the routine", "fr": "Comment dérouler la séance"},

    "En estas dos rutinas completas <strong>todas las rondas de un ejercicio</strong> antes "
    "de pasar al siguiente. Es lo que genera la acumulación de lactato característica del "
    "Tabata original.": {
        "en": "In these two routines you complete <strong>every round of one exercise</strong> "
              "before moving on to the next. That is what produces the lactate build-up "
              "characteristic of the original Tabata.",
        "fr": "Dans ces deux séances, vous enchaînez <strong>tous les rounds d'un "
              "exercice</strong> avant de passer au suivant. C'est ce qui produit "
              "l'accumulation de lactate caractéristique du Tabata original."},

    # ── Rutinas 3 y 4 ──────────────────────────────────────────────────────
    "Rutinas 3 y 4": {"en": "Routines 3 and 4", "fr": "Séances 3 et 4"},

    '03 · <span class="a">EMOM</span> — 20 MIN': {
        "en": '03 · <span class="a">EMOM</span> — 20 MIN',
        "fr": '03 · <span class="a">EMOM</span> — 20 MIN'},

    "<em>Every Minute On the Minute:</em> ejecuta las repeticiones marcadas y "
    "descansa lo que sobre del minuto. Cuanto más rápido, más descansas. "
    '<span class="tag mid">Nivel medio</span>': {
        "en": "<em>Every Minute On the Minute:</em> perform the prescribed reps and rest "
              "for whatever is left of the minute. The faster you work, the longer you rest. "
              '<span class="tag mid">Medium level</span>',
        "fr": "<em>Every Minute On the Minute :</em> effectuez les répétitions prescrites "
              "et récupérez le temps restant de la minute. Plus vous allez vite, plus vous "
              'récupérez. <span class="tag mid">Niveau moyen</span>'},

    "Minutos 1–5": {"en": "Minutes 1–5", "fr": "Minutes 1–5"},
    "15 burpees": {"en": "15 burpees", "fr": "15 burpees"},
    "Minutos 6–10": {"en": "Minutes 6–10", "fr": "Minutes 6–10"},
    "20 sentadillas con salto": {"en": "20 jump squats", "fr": "20 squats sautés"},
    "Minutos 11–15": {"en": "Minutes 11–15", "fr": "Minutes 11–15"},
    "12 flexiones": {"en": "12 push-ups", "fr": "12 pompes"},
    "Tren superior": {"en": "Upper body", "fr": "Haut du corps"},
    "Minutos 16–20": {"en": "Minutes 16–20", "fr": "Minutes 16–20"},
    "20 escaladores": {"en": "20 mountain climbers", "fr": "20 mountain climbers"},

    '04 · FULL BODY <span class="a">FURY</span> — 25 MIN': {
        "en": '04 · FULL BODY <span class="a">FURY</span> — 25 MIN',
        "fr": '04 · FULL BODY <span class="a">FURY</span> — 25 MIN'},

    "Circuito de cuerpo completo: 30 s de trabajo y 15 s de transición, "
    '5 vueltas con 1 minuto de descanso entre vueltas. <span class="tag hi">Nivel alto</span>': {
        "en": "Full-body circuit: 30 s of work and 15 s of transition, 5 circuits with "
              '1 minute of rest between circuits. <span class="tag hi">High level</span>',
        "fr": "Circuit corps entier : 30 s de travail et 15 s de transition, 5 tours avec "
              '1 minute de repos entre les tours. <span class="tag hi">Niveau élevé</span>'},

    "Burpee completo": {"en": "Full burpee", "fr": "Burpee complet"},
    "Sentadilla con salto": {"en": "Jump squat", "fr": "Squat sauté"},
    "Cuádriceps y glúteo": {"en": "Quads and glutes", "fr": "Quadriceps et fessiers"},
    "Flexiones": {"en": "Push-ups", "fr": "Pompes"},
    "Zancadas alternas": {"en": "Alternating lunges", "fr": "Fentes alternées"},
    "Piernas y glúteo": {"en": "Legs and glutes", "fr": "Jambes et fessiers"},
    "Plancha con toque de hombro": {
        "en": "Plank with shoulder tap", "fr": "Planche avec touche d'épaule"},
    "Core y estabilidad": {"en": "Core and stability", "fr": "Gainage et stabilité"},

    "Cuenta tus repeticiones en la vuelta 1": {
        "en": "Count your reps on circuit 1",
        "fr": "Comptez vos répétitions au premier tour"},

    "Anótalas y trata de igualarlas en la vuelta 5. Perder más de un 30 % de repeticiones "
    "entre la primera y la última vuelta significa que has salido demasiado fuerte: "
    "dosifica mejor la próxima vez.": {
        "en": "Write them down and try to match them on circuit 5. Losing more than 30 % of "
              "your reps between the first circuit and the last means you went out too hard: "
              "pace yourself better next time.",
        "fr": "Notez-les et essayez de les égaler au cinquième tour. Perdre plus de 30 % de "
              "répétitions entre le premier et le dernier tour signifie que vous êtes parti "
              "trop fort : dosez mieux la prochaine fois."},

    # ── Rutinas 5 y 6 ──────────────────────────────────────────────────────
    "Rutinas 5 y 6": {"en": "Routines 5 and 6", "fr": "Séances 5 et 6"},

    '05 · LOWER BODY <span class="a">INFERNO</span> — 22 MIN': {
        "en": '05 · LOWER BODY <span class="a">INFERNO</span> — 22 MIN',
        "fr": '05 · LOWER BODY <span class="a">INFERNO</span> — 22 MIN'},

    "40 s de trabajo y 20 s de descanso, 4 vueltas. Trabajo específico de tren "
    'inferior: colócalo lejos de tu día de piernas. <span class="tag hi">Nivel alto</span>': {
        "en": "40 s of work and 20 s of rest, 4 circuits. Specific lower-body work: place "
              'it well away from your leg day. <span class="tag hi">High level</span>',
        "fr": "40 s de travail et 20 s de repos, 4 tours. Travail spécifique du bas du "
              'corps : placez-le loin de votre jour de jambes. <span class="tag hi">Niveau élevé</span>'},

    "Salto al cajón o al escalón": {
        "en": "Box or step jump", "fr": "Saut sur box ou sur marche"},
    "Potencia de cuádriceps": {"en": "Quad power", "fr": "Puissance des quadriceps"},
    "Sentadilla sumo": {"en": "Sumo squat", "fr": "Squat sumo"},
    "Aductores y glúteo": {"en": "Adductors and glutes", "fr": "Adducteurs et fessiers"},
    "Sentadilla isométrica en pared": {"en": "Wall sit", "fr": "Chaise contre le mur"},
    "Cuádriceps (isométrico)": {
        "en": "Quads (isometric)", "fr": "Quadriceps (isométrique)"},
    "Zancada búlgara alterna": {
        "en": "Alternating Bulgarian split squat", "fr": "Fente bulgare alternée"},
    "Glúteo unilateral": {"en": "Single-leg glute", "fr": "Fessier unilatéral"},
    "Elevación de gemelos con salto": {
        "en": "Calf raises with a hop", "fr": "Extensions de mollets sautées"},

    '06 · UPPER BODY <span class="a">BLAST</span> — 20 MIN': {
        "en": '06 · UPPER BODY <span class="a">BLAST</span> — 20 MIN',
        "fr": '06 · UPPER BODY <span class="a">BLAST</span> — 20 MIN'},

    "35 s de trabajo y 15 s de descanso, 5 vueltas. Ideal como finalizador tras "
    'una sesión de tren superior ligera. <span class="tag mid">Nivel medio</span>': {
        "en": "35 s of work and 15 s of rest, 5 circuits. Ideal as a finisher after a "
              'light upper-body session. <span class="tag mid">Medium level</span>',
        "fr": "35 s de travail et 15 s de repos, 5 tours. Idéal comme finisher après une "
              'séance légère du haut du corps. <span class="tag mid">Niveau moyen</span>'},

    "Flexiones estándar": {"en": "Standard push-ups", "fr": "Pompes standard"},
    "Fondos en banco o silla": {
        "en": "Dips on a bench or chair", "fr": "Dips sur banc ou sur chaise"},
    "Flexiones diamante": {"en": "Diamond push-ups", "fr": "Pompes diamant"},
    "Tríceps y pecho interno": {
        "en": "Triceps and inner chest", "fr": "Triceps et pectoraux internes"},
    "Flexiones pike": {"en": "Pike push-ups", "fr": "Pompes pike"},

    "Escalado de las flexiones": {
        "en": "Scaling the push-ups", "fr": "Adapter les pompes"},

    "Si no completas 8 repeticiones limpias, apoya las rodillas o eleva las manos sobre un "
    "banco. Bajar la exigencia manteniendo el rango completo siempre es mejor que hacer "
    "medias repeticiones con la cadera caída.": {
        "en": "If you cannot complete 8 clean reps, drop to your knees or raise your hands "
              "onto a bench. Lowering the demand while keeping the full range is always "
              "better than half-reps with a sagging hip.",
        "fr": "Si vous n'enchaînez pas 8 répétitions propres, posez les genoux ou "
              "surélevez les mains sur un banc. Réduire l'exigence en conservant "
              "l'amplitude complète vaut toujours mieux que des demi-répétitions avec "
              "les hanches affaissées."},

    # ── Rutinas 7 y 8 ──────────────────────────────────────────────────────
    "Rutinas 7 y 8": {"en": "Routines 7 and 8", "fr": "Séances 7 et 8"},

    '07 · CORE <span class="a">DESTROYER</span> — 18 MIN': {
        "en": '07 · CORE <span class="a">DESTROYER</span> — 18 MIN',
        "fr": '07 · CORE <span class="a">DESTROYER</span> — 18 MIN'},

    "30 s de trabajo y 10 s de descanso, 6 vueltas. La rutina más corta y la "
    'que mejor combina con cualquier otra. <span class="tag mid">Nivel medio</span>': {
        "en": "30 s of work and 10 s of rest, 6 circuits. The shortest routine, and the "
              'one that pairs best with any other. <span class="tag mid">Medium level</span>',
        "fr": "30 s de travail et 10 s de repos, 6 tours. La séance la plus courte et "
              'celle qui se combine le mieux avec toutes les autres. <span class="tag mid">Niveau moyen</span>'},

    "Plancha frontal": {"en": "Front plank", "fr": "Planche frontale"},
    "Core anterior": {"en": "Anterior core", "fr": "Gainage antérieur"},
    "Giros rusos": {"en": "Russian twists", "fr": "Russian twists"},
    "Bicicleta": {"en": "Bicycle crunches", "fr": "Crunch bicyclette"},
    "Recto y oblicuos": {
        "en": "Rectus abdominis and obliques", "fr": "Grand droit et obliques"},
    "V-sit": {"en": "V-sit", "fr": "V-sit"},

    '08 · CARDIO <span class="a">KING</span> — 30 MIN': {
        "en": '08 · CARDIO <span class="a">KING</span> — 30 MIN',
        "fr": '08 · CARDIO <span class="a">KING</span> — 30 MIN'},

    "45 s de trabajo y 15 s de descanso, 4 vueltas con 1 minuto entre vueltas. "
    'La sesión de mayor gasto calórico del documento. <span class="tag hi">Nivel alto</span>': {
        "en": "45 s of work and 15 s of rest, 4 circuits with 1 minute between circuits. "
              'The highest calorie-burn session in this document. <span class="tag hi">High level</span>',
        "fr": "45 s de travail et 15 s de repos, 4 tours avec 1 minute entre les tours. "
              'La séance à la plus forte dépense calorique de ce document. <span class="tag hi">Niveau élevé</span>'},

    "Sprint en el sitio": {"en": "Sprint in place", "fr": "Sprint sur place"},
    "Comba o salto simulado": {
        "en": "Jump rope, or the same movement without a rope",
        "fr": "Corde à sauter, ou le même mouvement sans corde"},
    "Gemelo y coordinación": {
        "en": "Calves and coordination", "fr": "Mollets et coordination"},
    "Flexores de cadera": {"en": "Hip flexors", "fr": "Fléchisseurs de hanche"},
    "Skaters laterales": {"en": "Lateral skaters", "fr": "Skaters latéraux"},
    "Glúteo medio": {"en": "Gluteus medius", "fr": "Moyen fessier"},
    "Burpee sin flexión": {"en": "Burpee without the push-up", "fr": "Burpee sans pompe"},
    "Jumping jacks": {"en": "Jumping jacks", "fr": "Jumping jacks"},

    "Cardio King no es una rutina semanal": {
        "en": "Cardio King is not a weekly routine",
        "fr": "Cardio King n'est pas une séance hebdomadaire"},

    "Úsala como mucho <strong>una vez cada dos semanas</strong>. Treinta minutos a esta "
    "intensidad generan una fatiga central que se nota en el gimnasio durante dos días.": {
        "en": "Use it <strong>once every two weeks</strong> at most. Thirty minutes at this "
              "intensity create a central fatigue you will feel in the gym for two days.",
        "fr": "Utilisez-la <strong>une fois toutes les deux semaines</strong> au maximum. "
              "Trente minutes à cette intensité génèrent une fatigue centrale qui se "
              "ressent en salle pendant deux jours."},

    # ── Rutinas 9 y 10 ─────────────────────────────────────────────────────
    "Rutinas 9 y 10": {"en": "Routines 9 and 10", "fr": "Séances 9 et 10"},

    '09 · METABOLIC <span class="a">CIRCUIT</span> — 28 MIN': {
        "en": '09 · METABOLIC <span class="a">CIRCUIT</span> — 28 MIN',
        "fr": '09 · METABOLIC <span class="a">CIRCUIT</span> — 28 MIN'},

    "Cinco bloques AMRAP (tantas rondas como puedas) de 4 minutos, con "
    '2 minutos de descanso entre bloques. <span class="tag hi">Nivel avanzado</span>': {
        "en": "Five 4-minute AMRAP blocks (as many rounds as possible), with 2 minutes of "
              'rest between blocks. <span class="tag hi">Advanced level</span>',
        "fr": "Cinq blocs AMRAP (autant de rounds que possible) de 4 minutes, avec "
              '2 minutes de repos entre les blocs. <span class="tag hi">Niveau avancé</span>'},

    "Secuencia (repetir durante 4 min)": {
        "en": "Sequence (repeat for 4 min)", "fr": "Séquence (à répéter pendant 4 min)"},
    "Rondas logradas": {"en": "Rounds completed", "fr": "Rounds réalisés"},
    "Bloque 1": {"en": "Block 1", "fr": "Bloc 1"},
    "8 burpees + 12 sentadillas con salto": {
        "en": "8 burpees + 12 jump squats", "fr": "8 burpees + 12 squats sautés"},
    "Bloque 2": {"en": "Block 2", "fr": "Bloc 2"},
    "10 flexiones + 15 escaladores por lado": {
        "en": "10 push-ups + 15 mountain climbers per side",
        "fr": "10 pompes + 15 mountain climbers par côté"},
    "Bloque 3": {"en": "Block 3", "fr": "Bloc 3"},
    "12 zancadas alternas + 10 saltos al cajón": {
        "en": "12 alternating lunges + 10 box jumps",
        "fr": "12 fentes alternées + 10 sauts sur box"},
    "Bloque 4": {"en": "Block 4", "fr": "Bloc 4"},
    "15 jumping jacks + 10 V-sit + 20 s de plancha": {
        "en": "15 jumping jacks + 10 V-sits + 20 s of plank",
        "fr": "15 jumping jacks + 10 V-sit + 20 s de planche"},
    "Bloque 5": {"en": "Block 5", "fr": "Bloc 5"},
    "8 burpees + 8 flexiones diamante + 20 rodillas al pecho": {
        "en": "8 burpees + 8 diamond push-ups + 20 high knees",
        "fr": "8 burpees + 8 pompes diamant + 20 montées de genoux"},

    '10 · FINISHER <span class="a">EXPRESS</span> — 15 MIN': {
        "en": '10 · FINISHER <span class="a">EXPRESS</span> — 15 MIN',
        "fr": '10 · FINISHER <span class="a">EXPRESS</span> — 15 MIN'},

    "Ocho ejercicios en formato Tabata (20 s / 10 s), tres vueltas completas con "
    "1 minuto entre vueltas. El entrenamiento que nunca te apetece hacer. "
    '<span class="tag hi">Nivel máximo</span>': {
        "en": "Eight exercises in Tabata format (20 s / 10 s), three full circuits with "
              "1 minute between circuits. The workout you never feel like doing. "
              '<span class="tag hi">Maximum level</span>',
        "fr": "Huit exercices en format Tabata (20 s / 10 s), trois tours complets avec "
              "1 minute entre les tours. La séance dont on n'a jamais envie. "
              '<span class="tag hi">Niveau maximal</span>'},

    "Plancha activa": {"en": "Active plank", "fr": "Planche active"},

    "Cómo puntuar tu sesión": {
        "en": "How to score your session", "fr": "Comment noter votre séance"},

    "En las rutinas AMRAP tu marca es el <strong>número total de rondas</strong>. Anótalo y "
    "compáralo cada cuatro semanas con la misma rutina: es la forma más limpia de comprobar "
    "que tu condición física está mejorando de verdad.": {
        "en": "In AMRAP routines your score is the <strong>total number of rounds</strong>. "
              "Write it down and compare it every four weeks on the same routine: it is the "
              "cleanest way to confirm that your conditioning really is improving.",
        "fr": "Dans les séances AMRAP, votre score est le <strong>nombre total de "
              "rounds</strong>. Notez-le et comparez-le toutes les quatre semaines sur la "
              "même séance : c'est la façon la plus propre de vérifier que votre condition "
              "physique progresse réellement."},

    # ── Progresión de 8 semanas ────────────────────────────────────────────
    'PROGRESIÓN DE <span class="a">8 SEMANAS</span>': {
        "en": '<span class="a">8-WEEK</span> PROGRESSION',
        "fr": 'PROGRESSION SUR <span class="a">8 SEMAINES</span>'},

    "Sesiones": {"en": "Sessions", "fr": "Séances"},
    "Rutinas recomendadas": {"en": "Recommended routines", "fr": "Séances recommandées"},

    "07 Core Destroyer · 03 EMOM": {
        "en": "07 Core Destroyer · 03 EMOM", "fr": "07 Core Destroyer · 03 EMOM"},
    "Aprender los formatos sin destrozarte": {
        "en": "Learn the formats without wrecking yourself",
        "fr": "Apprendre les formats sans se détruire"},
    "01 Tabata · 06 Upper Body Blast": {
        "en": "01 Tabata · 06 Upper Body Blast", "fr": "01 Tabata · 06 Upper Body Blast"},
    "Introducir el trabajo interválico puro": {
        "en": "Introduce pure interval work",
        "fr": "Introduire le travail par intervalles pur"},
    "01 Tabata · 04 Full Body Fury · 07 Core": {
        "en": "01 Tabata · 04 Full Body Fury · 07 Core",
        "fr": "01 Tabata · 04 Full Body Fury · 07 Core"},
    "Subir la frecuencia": {"en": "Raise the frequency", "fr": "Augmenter la fréquence"},
    "03 EMOM · 07 Core Destroyer": {
        "en": "03 EMOM · 07 Core Destroyer", "fr": "03 EMOM · 07 Core Destroyer"},
    "Descarga: menos volumen, misma intensidad": {
        "en": "Deload: less volume, same intensity",
        "fr": "Décharge : moins de volume, même intensité"},
    "02 HIIT 40/20 · 05 Lower Inferno · 06 Upper": {
        "en": "02 HIIT 40/20 · 05 Lower Inferno · 06 Upper",
        "fr": "02 HIIT 40/20 · 05 Lower Inferno · 06 Upper"},
    "Trabajo por grupos específicos": {
        "en": "Work by specific muscle groups", "fr": "Travail par groupes spécifiques"},
    "02 HIIT 40/20 · 04 Full Body Fury · 08 Cardio King": {
        "en": "02 HIIT 40/20 · 04 Full Body Fury · 08 Cardio King",
        "fr": "02 HIIT 40/20 · 04 Full Body Fury · 08 Cardio King"},
    "Máximo gasto calórico del bloque": {
        "en": "Highest calorie burn of the block",
        "fr": "Dépense calorique maximale du bloc"},
    "09 Metabolic · 05 Lower · 06 Upper · 07 Core": {
        "en": "09 Metabolic · 05 Lower · 06 Upper · 07 Core",
        "fr": "09 Metabolic · 05 Lower · 06 Upper · 07 Core"},
    "Pico de volumen": {"en": "Volume peak", "fr": "Pic de volume"},
    "10 Finisher Express · 01 Tabata · 07 Core": {
        "en": "10 Finisher Express · 01 Tabata · 07 Core",
        "fr": "10 Finisher Express · 01 Tabata · 07 Core"},
    "Test final y descarga": {"en": "Final test and deload", "fr": "Test final et décharge"},

    # ── Escalado ───────────────────────────────────────────────────────────
    "Escalado según tu nivel": {
        "en": "Scaling to your level", "fr": "Adaptation selon votre niveau"},
    "Ratio trabajo/descanso": {"en": "Work/rest ratio", "fr": "Ratio travail/repos"},
    "La mitad de las indicadas": {
        "en": "Half of those prescribed", "fr": "La moitié de celles indiquées"},
    "Las indicadas": {"en": "As prescribed", "fr": "Celles indiquées"},
    "Las indicadas + 1": {"en": "As prescribed + 1", "fr": "Celles indiquées + 1"},
    "Sin salto ni flexión": {"en": "No jump, no push-up", "fr": "Sans saut ni pompe"},
    "Con salto al pecho": {
        "en": "With a knees-to-chest jump", "fr": "Avec saut genoux à la poitrine"},
    "Con rodillas apoyadas": {"en": "On your knees", "fr": "Genoux au sol"},
    "Estándar": {"en": "Standard", "fr": "Standard"},
    "Explosivas o con palmada": {
        "en": "Explosive, or with a clap", "fr": "Explosives, ou avec claquement de mains"},
    "Sentadilla al aire": {"en": "Bodyweight squat", "fr": "Squat au poids du corps"},
    "Con salto": {"en": "With a jump", "fr": "Avec saut"},
    "Con salto y giro de 180°": {
        "en": "With a jump and a 180° turn", "fr": "Avec saut et rotation à 180°"},
    "Impacto articular": {"en": "Joint impact", "fr": "Impact articulaire"},
    "Sustituye saltos por pasos": {
        "en": "Replace the jumps with steps", "fr": "Remplacez les sauts par des pas"},
    "Salto controlado": {"en": "Controlled jump", "fr": "Saut contrôlé"},
    "Salto pliométrico completo": {
        "en": "Full plyometric jump", "fr": "Saut pliométrique complet"},

    # ── Registro ───────────────────────────────────────────────────────────
    "Tu registro de sesiones": {
        "en": "Your session log", "fr": "Votre journal de séances"},
    "Rutina": {"en": "Routine", "fr": "Séance"},
    "Rondas o repeticiones": {
        "en": "Rounds or reps", "fr": "Rounds ou répétitions"},
    "RPE (1-10)": {"en": "RPE (1-10)", "fr": "RPE (1-10)"},
    "Sensaciones": {"en": "How it felt", "fr": "Sensations"},

    # ── Técnica y cierre ───────────────────────────────────────────────────
    "Técnica y cierre": {"en": "Technique and closing", "fr": "Technique et conclusion"},

    'TÉCNICA DE LOS <span class="a">MOVIMIENTOS CLAVE</span>': {
        "en": 'TECHNIQUE FOR THE <span class="a">KEY MOVEMENTS</span>',
        "fr": 'TECHNIQUE DES <span class="a">MOUVEMENTS CLÉS</span>'},

    "Ejecución correcta": {"en": "Correct execution", "fr": "Exécution correcte"},
    "Error que causa lesión": {
        "en": "The mistake that causes injury", "fr": "L'erreur qui provoque la blessure"},

    "Burpee": {"en": "Burpee", "fr": "Burpee"},
    "Manos al suelo, salto atrás controlado, pecho abajo, salto adelante y salto vertical": {
        "en": "Hands to the floor, controlled jump back, chest down, jump forward and "
              "vertical jump",
        "fr": "Mains au sol, saut arrière contrôlé, poitrine au sol, saut avant et saut "
              "vertical"},
    "Dejar caer la cadera al bajar (hiperextensión lumbar)": {
        "en": "Letting the hip drop on the way down (lumbar hyperextension)",
        "fr": "Laisser tomber les hanches en descendant (hyperextension lombaire)"},
    "Aterriza con la punta del pie primero y absorbe flexionando rodilla y cadera": {
        "en": "Land on the ball of the foot first and absorb by bending knee and hip",
        "fr": "Atterrissez d'abord sur l'avant du pied et amortissez en fléchissant genou "
              "et hanche"},
    "Caer con la pierna rígida y la rodilla hacia dentro": {
        "en": "Landing with a stiff leg and the knee caving inwards",
        "fr": "Atterrir jambe raide et genou rentré vers l'intérieur"},
    "Cadera baja y estable, hombros sobre las muñecas": {
        "en": "Hip low and stable, shoulders over the wrists",
        "fr": "Hanches basses et stables, épaules au-dessus des poignets"},
    "Subir la cadera y rebotar con los pies": {
        "en": "Raising the hip and bouncing off the feet",
        "fr": "Relever les hanches et rebondir sur les pieds"},
    "Zancada con salto": {"en": "Jump lunge", "fr": "Fente sautée"},
    "Torso vertical, rodilla trasera hacia el suelo sin tocarlo": {
        "en": "Torso vertical, rear knee towards the floor without touching it",
        "fr": "Buste vertical, genou arrière vers le sol sans le toucher"},
    "Rodilla delantera muy por delante de la punta del pie": {
        "en": "Front knee travelling far beyond the toes",
        "fr": "Genou avant très en avant de la pointe du pied"},
    "Flexión": {"en": "Push-up", "fr": "Pompe"},
    "Cuerpo en línea recta, codos a 45°, pecho al suelo": {
        "en": "Body in a straight line, elbows at 45°, chest to the floor",
        "fr": "Corps aligné, coudes à 45°, poitrine au sol"},
    "Codos abiertos a 90° y cadera hundida": {
        "en": "Elbows flared to 90° and hip sagging",
        "fr": "Coudes ouverts à 90° et hanches affaissées"},
    "Glúteo y abdomen activos, cadera neutra, mirada al suelo": {
        "en": "Glutes and abs engaged, hip neutral, eyes on the floor",
        "fr": "Fessiers et abdominaux engagés, bassin neutre, regard au sol"},
    "Cadera elevada o caída, cuello en extensión": {
        "en": "Hip too high or sagging, neck in extension",
        "fr": "Hanches trop hautes ou affaissées, nuque en extension"},
    "Salto al cajón": {"en": "Box jump", "fr": "Saut sur box"},
    "Sube saltando, baja caminando": {
        "en": "Jump up, step down", "fr": "Montez en sautant, descendez en marchant"},
    "Bajar de un salto: multiplica la carga sobre el tendón rotuliano": {
        "en": "Jumping back down: it multiplies the load on the patellar tendon",
        "fr": "Redescendre en sautant : cela multiplie la charge sur le tendon rotulien"},

    "La técnica se rompe antes que el músculo": {
        "en": "Technique breaks before the muscle does",
        "fr": "La technique lâche avant le muscle"},

    "En los últimos 10 segundos de cada intervalo, la fatiga degrada la ejecución. Si notas "
    "que pierdes la posición, <strong>para y termina el intervalo</strong>. Un burpee mal "
    "hecho no suma trabajo, suma riesgo.": {
        "en": "In the last 10 seconds of every interval, fatigue degrades execution. If you "
              "feel your position going, <strong>stop and end the interval</strong>. A badly "
              "done burpee does not add work, it adds risk.",
        "fr": "Dans les 10 dernières secondes de chaque intervalle, la fatigue dégrade "
              "l'exécution. Si vous sentez que la position se perd, <strong>arrêtez et "
              "terminez l'intervalle</strong>. Un burpee mal fait n'ajoute pas de travail, "
              "il ajoute du risque."},

    # ── Cierre ─────────────────────────────────────────────────────────────
    'EL HIIT ES SOLO <span class="a">UNA PIEZA</span>': {
        "en": 'HIIT IS ONLY <span class="a">ONE PIECE</span>',
        "fr": 'LE HIIT N\'EST QU\'<span class="a">UNE PIÈCE</span>'},

    "El HIIT rinde cuando <strong>no es lo único que haces</strong>: dos "
    "sesiones por semana como máximo, nunca en días seguidos, y siempre sobre una base de "
    "fuerza, comida suficiente y sueño. Solo, se convierte en desgaste.": {
        "en": "HIIT pays off when it is <strong>not the only thing you do</strong>: two "
              "sessions a week at most, never on consecutive days, and always on a base of "
              "strength work, enough food and sleep. On its own it turns into wear and tear.",
        "fr": "Le HIIT paie quand il <strong>n'est pas la seule chose que vous "
              "faites</strong> : deux séances par semaine au maximum, jamais deux jours de "
              "suite, et toujours sur une base de force, d'alimentation suffisante et de "
              "sommeil. Seul, il devient de l'usure."},

    # ── Aviso legal ────────────────────────────────────────────────────────
    "<b>Aviso importante</b><br> "
    "Documento con finalidad informativa y educativa. No constituye consejo médico, "
    "diagnóstico ni tratamiento, y no sustituye la valoración de un profesional sanitario "
    "colegiado. El entrenamiento de alta intensidad conlleva riesgo de lesión y supone una "
    "exigencia cardiovascular elevada: solicita una valoración médica antes de comenzar, "
    "especialmente si tienes más de 40 años, llevas tiempo inactivo, padeces hipertensión, "
    "cardiopatía, patología articular o respiratoria, estás embarazada o en periodo de "
    "lactancia, o eres menor de edad. Detén el ejercicio de inmediato ante dolor torácico, "
    "mareo o falta de aire desproporcionada. Los resultados varían entre personas y no están "
    "garantizados. Contenido protegido por derechos de autor: prohibida su reproducción, "
    "distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br> "
              "This document is for informational and educational purposes. It does not "
              "constitute medical advice, diagnosis or treatment, and it does not replace "
              "assessment by a registered health professional. High-intensity training "
              "carries a risk of injury and places a high demand on the cardiovascular "
              "system: seek a medical assessment before starting, especially if you are over "
              "40, have been inactive for some time, have high blood pressure, heart disease, "
              "a joint or respiratory condition, are pregnant or breastfeeding, or are a "
              "minor. Stop exercising immediately if you experience chest pain, dizziness or "
              "breathlessness out of proportion to the effort. Results vary between "
              "individuals and are not guaranteed. Copyrighted content: reproduction, "
              "distribution or resale without written permission from VILLUMINATIONS is "
              "prohibited.",
        "fr": "<b>Avertissement important</b><br> "
              "Document à finalité informative et éducative. Il ne constitue ni un avis "
              "médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation "
              "d'un professionnel de santé. L'entraînement de haute intensité comporte un "
              "risque de blessure et impose une exigence cardiovasculaire élevée : demandez "
              "un avis médical avant de commencer, en particulier si vous avez plus de "
              "40 ans, si vous êtes inactif depuis longtemps, si vous souffrez "
              "d'hypertension, d'une cardiopathie, d'une pathologie articulaire ou "
              "respiratoire, si vous êtes enceinte ou allaitante, ou si vous êtes mineur. "
              "Arrêtez immédiatement l'exercice en cas de douleur thoracique, de vertige ou "
              "d'essoufflement disproportionné. Les résultats varient d'une personne à "
              "l'autre et ne sont pas garantis. Contenu protégé par le droit d'auteur : "
              "toute reproduction, distribution ou revente sans autorisation écrite de "
              "VILLUMINATIONS est interdite."},
}
