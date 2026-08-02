# -*- coding: utf-8 -*-
"""
PLAN 09 · ELITE — Meditación y mindfulness, 21 días
===================================================
Los dos guiones se traducen como se leen en voz alta: frases cortas, ritmo
pausado y segunda persona. Un guion traducido literalmente se vuelve
impronunciable, y estos están hechos para grabarse.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Programa de 21 días</small><span class="glow">MEDITACIÓN<br>Y MINDFULNESS</span>': {
        "en": '<small>21-day programme</small><span class="glow">MEDITATION<br>AND MINDFULNESS</span>',
        "fr": '<small>Programme de 21 jours</small><span class="glow">MÉDITATION<br>ET PLEINE CONSCIENCE</span>'},
    "Mente fuerte, cuerpo fuerte. Tres semanas de práctica guiada diseñadas para quien <em>entrena en serio</em>.": {
        "en": "Strong mind, strong body. Three weeks of guided practice designed for people who <em>train seriously</em>.",
        "fr": "Esprit fort, corps fort. Trois semaines de pratique guidée conçues pour qui <em>s'entraîne sérieusement</em>."},
    '<span class="chip on">21 días</span> <span class="chip on">2 scripts completos</span> <span class="chip">3 técnicas de respiración</span> <span class="chip">Registro de práctica</span>': {
        "en": '<span class="chip on">21 days</span> <span class="chip on">2 full scripts</span> <span class="chip">3 breathing techniques</span> <span class="chip">Practice log</span>',
        "fr": '<span class="chip on">21 jours</span> <span class="chip on">2 scripts complets</span> <span class="chip">3 techniques de respiration</span> <span class="chip">Carnet de pratique</span>'},
    "Prácticas guiadas": {"en": "Guided practices", "fr": "Pratiques guidées"},
    "Minutos al día": {"en": "Minutes a day", "fr": "Minutes par jour"},
    "Scripts palabra a palabra": {"en": "Word-for-word scripts", "fr": "Scripts mot à mot"},
    '<strong>Edición 2026</strong><br><span class="muted">Programa de entrenamiento mental · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">Mental training programme · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Programme d\'entraînement mental · 8 pages</span>'},

    # ── 01 · Por qué ──────────────────────────────────────────────────
    "01 · Por qué": {"en": "01 · Why", "fr": "01 · Pourquoi"},
    'POR QUÉ UN ATLETA <span class="a">MEDITA</span>': {
        "en": 'WHY AN ATHLETE <span class="a">MEDITATES</span>',
        "fr": 'POURQUOI UN ATHLÈTE <span class="a">MÉDITE</span>'},
    "No es espiritualidad ni «poner la mente en blanco». Es entrenar la capacidad de <strong>dirigir tu atención</strong> y de bajar el sistema nervioso a modo recuperación cuando toca: dos habilidades que se transfieren a la serie pesada y al sueño profundo.": {
        "en": "This is not spirituality, nor «emptying your mind». It is training the ability to <strong>direct your attention</strong> and to drop the nervous system into recovery mode when it is time: two skills that transfer to the heavy set and to deep sleep.",
        "fr": "Ce n'est ni de la spiritualité ni « faire le vide ». C'est entraîner la capacité à <strong>diriger votre attention</strong> et à faire passer le système nerveux en mode récupération au bon moment : deux compétences qui se transfèrent à la série lourde et au sommeil profond."},
    "Lo que sí puedes esperar": {"en": "What you can expect", "fr": "Ce à quoi vous attendre"},
    "Conciliar el sueño más rápido las noches de estrés": {
        "en": "Falling asleep faster on stressful nights",
        "fr": "Vous endormir plus vite les soirs de stress"},
    "Mejor concentración en la serie de máxima intensidad": {
        "en": "Better focus on the maximal set",
        "fr": "Une meilleure concentration sur la série maximale"},
    "Menor reactividad ante un mal día de entreno o de báscula": {
        "en": "Less reactivity to a bad day in the gym or on the scale",
        "fr": "Moins de réactivité face à une mauvaise séance ou une mauvaise pesée"},
    "Lo que no es": {"en": "What it is not", "fr": "Ce que ce n'est pas"},
    "No sustituye tratamiento psicológico ni psiquiátrico": {
        "en": "It does not replace psychological or psychiatric treatment",
        "fr": "Cela ne remplace ni un suivi psychologique ni un traitement psychiatrique"},
    "No consiste en dejar la mente vacía: consiste en volver": {
        "en": "It is not about emptying the mind: it is about coming back",
        "fr": "Il ne s'agit pas de vider l'esprit : il s'agit de revenir"},
    "No funciona practicando solo cuando estás mal": {
        "en": "It does not work if you only practise when you feel bad",
        "fr": "Cela ne marche pas si vous ne pratiquez que quand ça va mal"},
    "Cómo funciona el programa": {"en": "How the programme works", "fr": "Comment fonctionne le programme"},
    "<b>Una práctica al día durante 21 días</b>De 5 a 20 minutos, en orden. Cada día se apoya en la habilidad construida el anterior.": {
        "en": "<b>One practice a day for 21 days</b>From 5 to 20 minutes, in order. Each day builds on the skill built the day before.",
        "fr": "<b>Une pratique par jour pendant 21 jours</b>De 5 à 20 minutes, dans l'ordre. Chaque jour s'appuie sur la compétence de la veille."},
    "<b>Misma hora, mismo sitio</b>El contexto estable es lo que convierte la práctica en hábito. La mañana, nada más levantarte, funciona para la mayoría.": {
        "en": "<b>Same time, same place</b>A stable context is what turns practice into habit. Mornings, right after getting up, work for most people.",
        "fr": "<b>Même heure, même endroit</b>Un contexte stable est ce qui transforme la pratique en habitude. Le matin, dès le lever, convient à la plupart."},
    "<b>Perder el hilo es la práctica</b>Cada vez que notas que te has distraído y vuelves, has hecho una repetición. Ahí está el entrenamiento.": {
        "en": "<b>Losing the thread is the practice</b>Every time you notice you have drifted and come back, you have done one repetition. That is the training.",
        "fr": "<b>Perdre le fil, c'est la pratique</b>Chaque fois que vous remarquez que vous avez dérivé et que vous revenez, vous avez fait une répétition. C'est là l'entraînement."},
    "<b>Si fallas un día, sigues al siguiente</b>No repitas el día perdido ni empieces de cero. La constancia importa más que la perfección.": {
        "en": "<b>If you miss a day, carry on the next</b>Do not repeat the missed day and do not start over. Consistency matters more than perfection.",
        "fr": "<b>Si vous manquez un jour, continuez le lendemain</b>Ne refaites pas le jour manqué et ne repartez pas de zéro. La régularité compte plus que la perfection."},
    "Programa de 21 días": {"en": "21-day programme", "fr": "Programme de 21 jours"},
    "Técnica, duración y descripción de cada jornada": {
        "en": "Technique, duration and description for each day",
        "fr": "Technique, durée et description de chaque journée"},
    "Script · Escaneo corporal": {"en": "Script · Body scan", "fr": "Script · Scan corporel"},
    "Para leer o grabar, palabra a palabra": {
        "en": "To read out or record, word for word",
        "fr": "À lire ou à enregistrer, mot à mot"},
    "Script · Visualización atlética": {
        "en": "Script · Athletic visualisation", "fr": "Script · Visualisation athlétique"},
    "Ensayo mental de tu sesión perfecta": {
        "en": "Mental rehearsal of your perfect session",
        "fr": "Répétition mentale de votre séance parfaite"},
    "Tres técnicas de respiración": {
        "en": "Three breathing techniques", "fr": "Trois techniques de respiration"},
    "Mindfulness aplicado y registro": {
        "en": "Applied mindfulness and logging",
        "fr": "Pleine conscience appliquée et carnet"},

    # ── Los 21 días ───────────────────────────────────────────────────
    "Programa 21 días": {"en": "21-day programme", "fr": "Programme 21 jours"},
    'LOS <span class="a">21 DÍAS</span>, UNO A UNO': {
        "en": 'THE <span class="a">21 DAYS</span>, ONE BY ONE',
        "fr": 'LES <span class="a">21 JOURS</span>, UN PAR UN'},
    "En qué consiste": {"en": "What it involves", "fr": "En quoi cela consiste"},
    "Hecho": {"en": "Done", "fr": "Fait"},
    "Respiración consciente": {"en": "Conscious breathing", "fr": "Respiration consciente"},
    "5 min": {"en": "5 min", "fr": "5 min"},
    "Observa tu respiración sin intentar cambiarla": {
        "en": "Observe your breath without trying to change it",
        "fr": "Observez votre respiration sans chercher à la modifier"},
    "Conteo de respiraciones": {"en": "Breath counting", "fr": "Comptage des respirations"},
    "7 min": {"en": "7 min", "fr": "7 min"},
    "Cuenta hasta 10 y reinicia. Si te pierdes, vuelve al 1": {
        "en": "Count to 10 and start again. If you lose count, go back to 1",
        "fr": "Comptez jusqu'à 10 et recommencez. Si vous perdez le compte, revenez à 1"},
    "Escaneo corporal": {"en": "Body scan", "fr": "Scan corporel"},
    "10 min": {"en": "10 min", "fr": "10 min"},
    "Recorre cada parte del cuerpo con atención": {
        "en": "Move attention through every part of the body",
        "fr": "Parcourez chaque partie du corps avec attention"},
    "Respiración 4-7-8": {"en": "4-7-8 breathing", "fr": "Respiration 4-7-8"},
    "8 min": {"en": "8 min", "fr": "8 min"},
    "Inhala 4 s, retén 7 s, exhala 8 s": {
        "en": "Inhale 4 s, hold 7 s, exhale 8 s",
        "fr": "Inspirez 4 s, retenez 7 s, expirez 8 s"},
    "Mindfulness al caminar": {"en": "Walking mindfulness", "fr": "Pleine conscience en marchant"},
    "15 min": {"en": "15 min", "fr": "15 min"},
    "Cada paso con plena atención al apoyo del pie": {
        "en": "Every step with full attention on the foot landing",
        "fr": "Chaque pas avec toute votre attention sur l'appui du pied"},
    "Meditación de gratitud": {"en": "Gratitude meditation", "fr": "Méditation de gratitude"},
    "Tres cosas concretas por las que estás agradecido": {
        "en": "Three specific things you are grateful for",
        "fr": "Trois choses concrètes dont vous êtes reconnaissant"},
    "Visualización atlética": {"en": "Athletic visualisation", "fr": "Visualisation athlétique"},
    "12 min": {"en": "12 min", "fr": "12 min"},
    "Ensaya mentalmente tu entrenamiento perfecto": {
        "en": "Mentally rehearse your perfect session",
        "fr": "Répétez mentalement votre séance parfaite"},
    "Metta (amor bondadoso)": {"en": "Metta (loving-kindness)", "fr": "Metta (bienveillance)"},
    "Dirige buenos deseos hacia ti y hacia los demás": {
        "en": "Direct good wishes towards yourself and towards others",
        "fr": "Adressez de bons souhaits à vous-même et aux autres"},
    "Respiración de caja": {"en": "Box breathing", "fr": "Respiration carrée"},
    "4-4-4-4: inhala, retén, exhala, retén en vacío": {
        "en": "4-4-4-4: inhale, hold, exhale, hold empty",
        "fr": "4-4-4-4 : inspirez, retenez, expirez, retenez à vide"},
    "Escaneo corporal profundo": {"en": "Deep body scan", "fr": "Scan corporel profond"},
    "Relajación muscular progresiva completa": {
        "en": "Full progressive muscle relaxation",
        "fr": "Relaxation musculaire progressive complète"},
    "Observación de pensamientos": {"en": "Observing thoughts", "fr": "Observation des pensées"},
    "Tus pensamientos son nubes que pasan, no eres tú": {
        "en": "Your thoughts are passing clouds; they are not you",
        "fr": "Vos pensées sont des nuages qui passent, elles ne sont pas vous"},
    "Mindfulness en la ducha": {"en": "Mindfulness in the shower", "fr": "Pleine conscience sous la douche"},
    "5–10 min": {"en": "5–10 min", "fr": "5–10 min"},
    "Atención plena a temperatura, sonido y tacto": {
        "en": "Full attention to temperature, sound and touch",
        "fr": "Pleine attention à la température, au son et au toucher"},
    "Respiración alternada": {"en": "Alternate nostril breathing", "fr": "Respiration alternée"},
    "Nadi Shodhana: una fosa nasal cada vez": {
        "en": "Nadi Shodhana: one nostril at a time",
        "fr": "Nadi Shodhana : une narine à la fois"},
    "Meditación caminando": {"en": "Walking meditation", "fr": "Méditation en marchant"},
    "20 min": {"en": "20 min", "fr": "20 min"},
    "Camina al aire libre con presencia total": {
        "en": "Walk outdoors with complete presence",
        "fr": "Marchez dehors en pleine présence"},
    "Visualización de objetivos": {"en": "Goal visualisation", "fr": "Visualisation d'objectifs"},
    "Tu mejor versión dentro de seis meses, en detalle": {
        "en": "Your best self six months from now, in detail",
        "fr": "Votre meilleure version dans six mois, en détail"},
    "Escaneo corporal atlético": {"en": "Athletic body scan", "fr": "Scan corporel athlétique"},
    "Atención a las tensiones antes y después de entrenar": {
        "en": "Attention to tension before and after training",
        "fr": "Attention aux tensions avant et après l'entraînement"},
    "Respiración 4-7-8 avanzada": {"en": "Advanced 4-7-8 breathing", "fr": "Respiration 4-7-8 avancée"},
    "Tres ciclos de diez respiraciones completas": {
        "en": "Three cycles of ten full breaths",
        "fr": "Trois cycles de dix respirations complètes"},
    "Meditación de compasión": {"en": "Compassion meditation", "fr": "Méditation de compassion"},
    "Reconoce tu esfuerzo y tus logros sin exigencia": {
        "en": "Acknowledge your effort and your wins without demanding more",
        "fr": "Reconnaissez vos efforts et vos réussites sans exigence"},
    "Mindfulness al comer": {"en": "Mindful eating", "fr": "Manger en pleine conscience"},
    "Una comida entera con atención plena al sabor": {
        "en": "A whole meal with full attention to flavour",
        "fr": "Un repas entier avec pleine attention à la saveur"},
    "Conciencia abierta": {"en": "Open awareness", "fr": "Conscience ouverte"},
    "Observa todo lo que aparece, sin juzgar ni dirigir": {
        "en": "Observe whatever arises, without judging or steering",
        "fr": "Observez tout ce qui apparaît, sans juger ni diriger"},
    "Práctica libre": {"en": "Free practice", "fr": "Pratique libre"},
    "Elige la técnica que más te haya resonado": {
        "en": "Choose whichever technique resonated most",
        "fr": "Choisissez la technique qui vous a le plus parlé"},
    "Qué hacer el día 22": {"en": "What to do on day 22", "fr": "Que faire le jour 22"},
    "Quédate con las <strong>dos o tres prácticas</strong> que mejor te han funcionado y conviértelas en rutina: una por la mañana para el enfoque y otra por la noche para el descanso. El programa no termina, se simplifica.": {
        "en": "Keep the <strong>two or three practices</strong> that worked best for you and turn them into routine: one in the morning for focus and one at night for rest. The programme does not end, it simplifies.",
        "fr": "Gardez les <strong>deux ou trois pratiques</strong> qui ont le mieux fonctionné et faites-en une routine : une le matin pour la concentration et une le soir pour le repos. Le programme ne s'arrête pas, il se simplifie."},

    # ── Script · escaneo corporal ─────────────────────────────────────
    'ESCANEO CORPORAL <span class="a">COMPLETO</span> · 15 MIN': {
        "en": '<span class="a">FULL</span> BODY SCAN · 15 MIN',
        "fr": 'SCAN CORPOREL <span class="a">COMPLET</span> · 15 MIN'},
    "Instrucciones de uso": {"en": "How to use it", "fr": "Mode d'emploi"},
    "Lee el texto lentamente o grábate leyéndolo para reproducirlo después. Deja <strong>3–5 segundos de pausa</strong> entre párrafos. Posición: tumbado boca arriba, brazos a los lados, ojos cerrados.": {
        "en": "Read the text slowly, or record yourself reading it to play back later. Leave a <strong>3–5 second pause</strong> between paragraphs. Position: lying on your back, arms at your sides, eyes closed.",
        "fr": "Lisez le texte lentement, ou enregistrez-vous pour l'écouter ensuite. Laissez <strong>3 à 5 secondes de pause</strong> entre les paragraphes. Position : allongé sur le dos, bras le long du corps, yeux fermés."},
    "«Cierra los ojos. Permite que tu cuerpo descanse completamente sobre la superficie. Siente el peso de tu cuerpo. No necesitas cambiar nada, solo observar. Respira con naturalidad…»": {
        "en": "«Close your eyes. Let your body rest completely on the surface beneath you. Feel the weight of your body. You do not need to change anything, only to observe. Breathe naturally…»",
        "fr": "« Fermez les yeux. Laissez votre corps reposer complètement sur la surface. Sentez le poids de votre corps. Vous n'avez rien à changer, seulement à observer. Respirez naturellement… »"},
    "«Lleva tu atención a la planta de los pies. Sin juzgar, sin cambiar, observa cualquier sensación que esté presente: temperatura, tensión, contacto. Permanece aquí unos momentos…»": {
        "en": "«Bring your attention to the soles of your feet. Without judging, without changing, notice any sensation that is there: temperature, tension, contact. Stay here for a few moments…»",
        "fr": "« Portez votre attention sur la plante des pieds. Sans juger, sans modifier, observez toute sensation présente : température, tension, contact. Restez ici quelques instants… »"},
    "«Ahora sube lentamente por los tobillos, las pantorrillas, las rodillas. Si encuentras tensión, simplemente nómbrala: tensión, calor, hormigueo. Después deja que se disuelva con cada exhalación…»": {
        "en": "«Now move slowly up through the ankles, the calves, the knees. If you find tension, simply name it: tension, warmth, tingling. Then let it dissolve with each exhale…»",
        "fr": "« Remontez lentement par les chevilles, les mollets, les genoux. Si vous trouvez une tension, nommez-la simplement : tension, chaleur, picotement. Puis laissez-la se dissoudre à chaque expiration… »"},
    "«Continúa subiendo hacia los muslos, las caderas, el abdomen. Con cada respiración el abdomen sube y baja suavemente. Eres consciente del ritmo natural de tu cuerpo…»": {
        "en": "«Keep moving up towards the thighs, the hips, the abdomen. With each breath the abdomen rises and falls gently. You are aware of your body's natural rhythm…»",
        "fr": "« Continuez vers les cuisses, les hanches, l'abdomen. À chaque respiration, l'abdomen monte et descend doucement. Vous percevez le rythme naturel de votre corps… »"},
    "«Lleva la atención al pecho y al corazón. Siente el latido suave y constante. Este corazón lleva latiendo toda tu vida, sin descanso. Siente gratitud por él…»": {
        "en": "«Bring your attention to the chest and the heart. Feel the soft, steady beat. This heart has been beating your whole life, without a break. Feel gratitude for it…»",
        "fr": "« Portez votre attention sur la poitrine et le cœur. Sentez ce battement doux et régulier. Ce cœur bat depuis toujours, sans repos. Éprouvez de la gratitude pour lui… »"},
    "«Sube por los hombros y los brazos hasta la punta de los dedos. Libera cualquier tensión que hayas acumulado durante el día…»": {
        "en": "«Move up through the shoulders and the arms to the fingertips. Release any tension you have gathered during the day…»",
        "fr": "« Remontez par les épaules et les bras jusqu'au bout des doigts. Relâchez toute tension accumulée pendant la journée… »"},
    "«Por último, lleva la atención al cuello, la mandíbula —suelta los dientes—, los ojos y la frente. Imagina que cada exhalación se lleva consigo la tensión del día. Tu cuerpo está pesado y relajado…»": {
        "en": "«Finally, bring your attention to the neck, the jaw — unclench your teeth — the eyes and the forehead. Imagine each exhale carrying the day's tension away with it. Your body is heavy and relaxed…»",
        "fr": "« Enfin, portez votre attention sur le cou, la mâchoire — desserrez les dents —, les yeux et le front. Imaginez que chaque expiration emporte la tension de la journée. Votre corps est lourd et détendu… »"},
    "«Cuando estés listo, mueve suavemente los dedos de las manos y de los pies. Abre los ojos despacio. Tómate un momento antes de levantarte. Llévate esta calma contigo al resto del día.»": {
        "en": "«When you are ready, gently move your fingers and your toes. Open your eyes slowly. Take a moment before getting up. Carry this calm with you into the rest of the day.»",
        "fr": "« Quand vous êtes prêt, bougez doucement les doigts et les orteils. Ouvrez les yeux lentement. Prenez un instant avant de vous lever. Emportez ce calme avec vous pour le reste de la journée. »"},
    "Variante de 5 minutos para antes de dormir": {
        "en": "A 5-minute variant for bedtime",
        "fr": "Variante de 5 minutes avant le coucher"},
    "Recorre solo cuatro zonas —pies, piernas, torso y cara— tensando cada una durante 3 segundos y soltándola por completo. La diferencia entre tensión y relajación es lo que enseña al cuerpo a soltar de verdad.": {
        "en": "Go through only four areas — feet, legs, torso and face — tensing each for 3 seconds and then releasing it completely. The contrast between tension and release is what teaches the body to let go for real.",
        "fr": "Parcourez seulement quatre zones — pieds, jambes, tronc et visage — en contractant chacune 3 secondes puis en relâchant complètement. C'est le contraste entre tension et relâchement qui apprend au corps à lâcher pour de bon."},

    # ── Script · visualización ────────────────────────────────────────
    "Script · Visualización": {"en": "Script · Visualisation", "fr": "Script · Visualisation"},
    'VISUALIZACIÓN <span class="a">ATLÉTICA</span> · 12 MIN': {
        "en": '<span class="a">ATHLETIC</span> VISUALISATION · 12 MIN',
        "fr": 'VISUALISATION <span class="a">ATHLÉTIQUE</span> · 12 MIN'},
    "Cuándo usarla": {"en": "When to use it", "fr": "Quand l'utiliser"},
    "La noche anterior a una sesión importante o 30 minutos antes de entrenar. Sentado, espalda recta, ojos cerrados. El ensayo mental funciona porque activa <strong>las mismas rutas neuronales</strong> que la ejecución real del movimiento.": {
        "en": "The night before an important session, or 30 minutes before training. Seated, back straight, eyes closed. Mental rehearsal works because it activates <strong>the same neural pathways</strong> as actually performing the movement.",
        "fr": "La veille d'une séance importante ou 30 minutes avant l'entraînement. Assis, dos droit, yeux fermés. La répétition mentale fonctionne parce qu'elle active <strong>les mêmes voies neuronales</strong> que l'exécution réelle du mouvement."},
    "«Siéntate cómodo, con la espalda recta y los pies apoyados en el suelo. Toma tres respiraciones profundas: inhala por la nariz, exhala lentamente por la boca. Con cada exhalación, suelta el ruido del día…»": {
        "en": "«Sit comfortably, back straight and feet flat on the floor. Take three deep breaths: in through the nose, slowly out through the mouth. With each exhale, let go of the day's noise…»",
        "fr": "« Asseyez-vous confortablement, dos droit et pieds à plat au sol. Prenez trois respirations profondes : inspirez par le nez, expirez lentement par la bouche. À chaque expiration, laissez tomber le bruit de la journée… »"},
    "«Imagina que entras en el gimnasio. Siente la temperatura del aire, escucha el sonido de fondo, huele el ambiente. Estás aquí con un propósito claro…»": {
        "en": "«Imagine walking into the gym. Feel the temperature of the air, hear the background sound, smell the room. You are here with a clear purpose…»",
        "fr": "« Imaginez que vous entrez dans la salle. Sentez la température de l'air, écoutez le bruit de fond, sentez l'odeur du lieu. Vous êtes ici avec un but clair… »"},
    "«Te ves calentando. Los movimientos son fluidos. Notas cómo el cuerpo responde, cómo la articulación se abre, cómo el músculo se despierta. Todo está en su sitio…»": {
        "en": "«You see yourself warming up. The movements are fluid. You notice the body responding, the joint opening, the muscle waking up. Everything is in place…»",
        "fr": "« Vous vous voyez à l'échauffement. Les mouvements sont fluides. Vous sentez le corps répondre, l'articulation s'ouvrir, le muscle se réveiller. Tout est en place… »"},
    "«Ahora te colocas frente a la barra. Ves el peso. Es exigente, y estás preparado. Sientes la textura del agarre en las manos, la posición firme de los pies contra el suelo…»": {
        "en": "«Now you set up in front of the bar. You see the weight. It is demanding, and you are ready. You feel the texture of the grip in your hands, the firm placement of your feet against the floor…»",
        "fr": "« Vous vous placez maintenant devant la barre. Vous voyez la charge. Elle est exigeante, et vous êtes prêt. Vous sentez la texture de la prise dans vos mains, l'appui ferme de vos pieds au sol… »"},
    "«Ejecutas la primera repetición. Perfecta. Sientes exactamente qué músculo trabaja, la velocidad controlada en la bajada, la fuerza precisa en la subida. La técnica es impecable…»": {
        "en": "«You perform the first repetition. Perfect. You feel exactly which muscle is working, the controlled speed on the way down, the precise force on the way up. The technique is flawless…»",
        "fr": "« Vous exécutez la première répétition. Parfaite. Vous sentez exactement quel muscle travaille, la vitesse contrôlée à la descente, la force précise à la montée. La technique est impeccable… »"},
    "«Repetición tras repetición, mantienes la misma calidad. Cuando aparece la fatiga, la reconoces sin miedo: forma parte del proceso. Respiras, te reorganizas y continúas…»": {
        "en": "«Repetition after repetition, you hold the same quality. When fatigue appears, you recognise it without fear: it is part of the process. You breathe, you reset, you carry on…»",
        "fr": "« Répétition après répétition, vous gardez la même qualité. Quand la fatigue arrive, vous la reconnaissez sans crainte : elle fait partie du processus. Vous respirez, vous vous replacez et vous continuez… »"},
    "«Terminas la última serie. Sientes el esfuerzo bien hecho, la satisfacción de haber cumplido lo que te propusiste. No es suerte: es la consecuencia de tu preparación…»": {
        "en": "«You finish the last set. You feel the effort well spent, the satisfaction of having done what you set out to do. This is not luck: it is the consequence of your preparation…»",
        "fr": "« Vous terminez la dernière série. Vous ressentez l'effort bien fait, la satisfaction d'avoir accompli ce que vous vous étiez fixé. Ce n'est pas de la chance : c'est la conséquence de votre préparation… »"},
    "«Toma una respiración profunda. Guarda esta sensación de control y llévala contigo. Cuando abras los ojos, tu cuerpo ya sabe lo que tiene que hacer.»": {
        "en": "«Take one deep breath. Keep this feeling of control and carry it with you. When you open your eyes, your body already knows what it has to do.»",
        "fr": "« Prenez une respiration profonde. Gardez cette sensation de contrôle et emportez-la avec vous. Quand vous ouvrirez les yeux, votre corps saura déjà quoi faire. »"},
    "Las tres reglas de una visualización efectiva": {
        "en": "The three rules of an effective visualisation",
        "fr": "Les trois règles d'une visualisation efficace"},
    "<strong>Primera persona, no tercera.</strong> Vívelo desde dentro de tus ojos, no te veas desde fuera como en un vídeo.": {
        "en": "<strong>First person, not third.</strong> Live it from behind your own eyes; do not watch yourself from outside as if on video.",
        "fr": "<strong>À la première personne, pas à la troisième.</strong> Vivez-le depuis vos propres yeux, ne vous regardez pas de l'extérieur comme dans une vidéo."},
    "<strong>Incluye todos los sentidos.</strong> Tacto, sonido y esfuerzo muscular importan más que la imagen visual.": {
        "en": "<strong>Include every sense.</strong> Touch, sound and muscular effort matter more than the visual image.",
        "fr": "<strong>Incluez tous les sens.</strong> Le toucher, le son et l'effort musculaire comptent plus que l'image visuelle."},
    "<strong>Ensaya también la dificultad.</strong> Visualizar solo el éxito fácil no prepara para el momento en que la repetición se atasca.": {
        "en": "<strong>Rehearse the difficulty too.</strong> Visualising only easy success does not prepare you for the moment the rep stalls.",
        "fr": "<strong>Répétez aussi la difficulté.</strong> Ne visualiser que la réussite facile ne prépare pas au moment où la répétition bloque."},

    # ── Respiración ───────────────────────────────────────────────────
    "Respiración": {"en": "Breathing", "fr": "Respiration"},
    'TRES TÉCNICAS DE <span class="a">RESPIRACIÓN</span>': {
        "en": 'THREE <span class="a">BREATHING</span> TECHNIQUES',
        "fr": 'TROIS TECHNIQUES DE <span class="a">RESPIRATION</span>'},
    "Técnica 1 · Respiración 4-7-8 (anti-estrés)": {
        "en": "Technique 1 · 4-7-8 breathing (anti-stress)",
        "fr": "Technique 1 · Respiration 4-7-8 (anti-stress)"},
    "Paso": {"en": "Step", "fr": "Étape"},
    "Siéntate con la espalda recta o túmbate boca arriba": {
        "en": "Sit with your back straight or lie on your back",
        "fr": "Asseyez-vous dos droit ou allongez-vous sur le dos"},
    "Exhala por completo por la boca, con sonido audible": {
        "en": "Exhale completely through the mouth, audibly",
        "fr": "Expirez complètement par la bouche, de façon audible"},
    "Cierra la boca e <strong>inhala por la nariz</strong> contando hasta 4": {
        "en": "Close your mouth and <strong>inhale through the nose</strong> for a count of 4",
        "fr": "Fermez la bouche et <strong>inspirez par le nez</strong> en comptant jusqu'à 4"},
    "<strong>Retén</strong> la respiración contando hasta 7": {
        "en": "<strong>Hold</strong> the breath for a count of 7",
        "fr": "<strong>Retenez</strong> votre souffle en comptant jusqu'à 7"},
    "<strong>Exhala</strong> por la boca contando hasta 8": {
        "en": "<strong>Exhale</strong> through the mouth for a count of 8",
        "fr": "<strong>Expirez</strong> par la bouche en comptant jusqu'à 8"},
    "Repite el ciclo 3–4 veces. Máxima eficacia justo antes de dormir": {
        "en": "Repeat the cycle 3–4 times. Most effective right before sleep",
        "fr": "Répétez le cycle 3 à 4 fois. Efficacité maximale juste avant le coucher"},
    "Si te mareas, acorta los tiempos manteniendo la proporción 4-7-8.": {
        "en": "If you feel dizzy, shorten the counts while keeping the 4-7-8 ratio.",
        "fr": "Si vous avez la tête qui tourne, raccourcissez les temps en gardant la proportion 4-7-8."},
    "Técnica 2 · Respiración de caja (enfoque)": {
        "en": "Technique 2 · Box breathing (focus)",
        "fr": "Technique 2 · Respiration carrée (concentration)"},
    "<b>Fig. 1</b>Las dos respiraciones del programa": {
        "en": "<b>Fig. 1</b>The programme's two breathing patterns",
        "fr": "<b>Fig. 1</b>Les deux respirations du programme"},
    "La anchura de cada bloque es proporcional a los segundos reales.": {
        "en": "Each block's width is proportional to the actual seconds.",
        "fr": "La largeur de chaque bloc est proportionnelle aux secondes réelles."},
    "Técnica 3 · Respiración diafragmática (base)": {
        "en": "Technique 3 · Diaphragmatic breathing (the base)",
        "fr": "Technique 3 · Respiration diaphragmatique (la base)"},
    "<b>Coloca las manos</b>Una sobre el pecho y otra sobre el abdomen.": {
        "en": "<b>Place your hands</b>One on the chest and one on the abdomen.",
        "fr": "<b>Placez les mains</b>Une sur la poitrine et une sur l'abdomen."},
    "<b>Inhala lentamente</b>Solo debe moverse la mano del abdomen.": {
        "en": "<b>Inhale slowly</b>Only the hand on the abdomen should move.",
        "fr": "<b>Inspirez lentement</b>Seule la main de l'abdomen doit bouger."},
    "<b>Comprueba el patrón</b>Si se mueve la del pecho, estás respirando de forma superficial: el patrón del estrés.": {
        "en": "<b>Check the pattern</b>If the chest hand moves, you are breathing shallowly: the stress pattern.",
        "fr": "<b>Vérifiez le schéma</b>Si la main de la poitrine bouge, votre respiration est superficielle : le schéma du stress."},
    "<b>10 respiraciones cada mañana</b>Antes de levantarte. En 3–4 semanas será tu patrón natural.": {
        "en": "<b>10 breaths every morning</b>Before getting up. In 3–4 weeks it will be your natural pattern.",
        "fr": "<b>10 respirations chaque matin</b>Avant de vous lever. En 3 à 4 semaines, ce sera votre schéma naturel."},
    "Precaución con las retenciones": {
        "en": "Take care with breath holds", "fr": "Prudence avec les rétentions"},
    "Con hipertensión no controlada, patología cardiaca o respiratoria, embarazo o crisis de ansiedad con hiperventilación, evita las retenciones prolongadas y consúltalo con tu médico. Nunca las practiques en el agua ni conduciendo.": {
        "en": "With uncontrolled hypertension, cardiac or respiratory conditions, pregnancy, or anxiety attacks involving hyperventilation, avoid prolonged holds and check with your doctor. Never practise them in water or while driving.",
        "fr": "En cas d'hypertension non contrôlée, de pathologie cardiaque ou respiratoire, de grossesse ou de crises d'angoisse avec hyperventilation, évitez les rétentions prolongées et consultez votre médecin. Ne les pratiquez jamais dans l'eau ni au volant."},

    # ── Mindfulness aplicado ──────────────────────────────────────────
    "Mindfulness aplicado": {"en": "Applied mindfulness", "fr": "Pleine conscience appliquée"},
    'LLÉVALO AL <span class="a">GIMNASIO Y A LA MESA</span>': {
        "en": 'TAKE IT TO THE <span class="a">GYM AND THE TABLE</span>',
        "fr": 'EMPORTEZ-LA À LA <span class="a">SALLE ET À TABLE</span>'},
    "Práctica de 60 segundos": {"en": "60-second practice", "fr": "Pratique de 60 secondes"},
    "Qué mejora": {"en": "What it improves", "fr": "Ce que cela améliore"},
    "Antes de la serie pesada": {"en": "Before the heavy set", "fr": "Avant la série lourde"},
    "Tres respiraciones de caja mirando la barra": {
        "en": "Three box breaths while looking at the bar",
        "fr": "Trois respirations carrées en regardant la barre"},
    "Baja el ruido mental y mejora la activación": {
        "en": "Lowers mental noise and improves activation",
        "fr": "Réduit le bruit mental et améliore l'activation"},
    "Entre series": {"en": "Between sets", "fr": "Entre les séries"},
    "Respiración nasal lenta contando la exhalación": {
        "en": "Slow nasal breathing, counting the exhale",
        "fr": "Respiration nasale lente en comptant l'expiration"},
    "Acelera la recuperación entre esfuerzos": {
        "en": "Speeds up recovery between efforts",
        "fr": "Accélère la récupération entre les efforts"},
    "Al terminar de entrenar": {"en": "When you finish training", "fr": "En fin de séance"},
    "Escaneo rápido: ¿qué zona quedó tensa?": {
        "en": "Quick scan: which area stayed tense?",
        "fr": "Scan rapide : quelle zone est restée tendue ?"},
    "Detecta compensaciones antes de que sean lesión": {
        "en": "Catches compensations before they become injuries",
        "fr": "Détecte les compensations avant qu'elles ne deviennent des blessures"},
    "Antes de comer": {"en": "Before eating", "fr": "Avant de manger"},
    "Tres respiraciones y una pregunta: ¿tengo hambre real?": {
        "en": "Three breaths and one question: am I actually hungry?",
        "fr": "Trois respirations et une question : ai-je vraiment faim ?"},
    "Distingue hambre fisiológica de hambre emocional": {
        "en": "Tells physiological hunger from emotional hunger",
        "fr": "Distingue la faim physiologique de la faim émotionnelle"},
    "Durante la comida": {"en": "During the meal", "fr": "Pendant le repas"},
    "Suelta los cubiertos entre bocados": {
        "en": "Put the cutlery down between mouthfuls",
        "fr": "Posez les couverts entre les bouchées"},
    "Mejora la saciedad y la digestión": {
        "en": "Improves satiety and digestion", "fr": "Améliore la satiété et la digestion"},
    "Cuatro ciclos de 4-7-8": {"en": "Four cycles of 4-7-8", "fr": "Quatre cycles de 4-7-8"},
    "Reduce el tiempo que tardas en dormirte": {
        "en": "Shortens the time it takes you to fall asleep",
        "fr": "Réduit le temps que vous mettez à vous endormir"},
    "Tu registro de 21 días": {"en": "Your 21-day log", "fr": "Votre carnet de 21 jours"},
    "Cómo me he sentido": {"en": "How I felt", "fr": "Comment je me suis senti"},
    "Lo que he aprendido en estas tres semanas": {
        "en": "What I learned in these three weeks",
        "fr": "Ce que j'ai appris en trois semaines"},
    "Un indicador honesto de progreso": {
        "en": "An honest measure of progress", "fr": "Un indicateur honnête de progrès"},
    "No es «cuánto rato aguanto sin distraerme», sino <strong>cuánto tardo en darme cuenta de que me he distraído</strong>. Ese tiempo se acorta con la práctica, y es exactamente la habilidad que después usas en la vida real.": {
        "en": "It is not «how long I last without drifting» but <strong>how long it takes me to notice I have drifted</strong>. That time shortens with practice, and it is exactly the skill you then use in real life.",
        "fr": "Ce n'est pas « combien de temps je tiens sans me distraire », mais <strong>combien de temps je mets à remarquer que je me suis distrait</strong>. Ce délai se raccourcit avec la pratique, et c'est exactement la compétence que vous utilisez ensuite dans la vie réelle."},

    # ── Dificultades ──────────────────────────────────────────────────
    "Dificultades frecuentes": {"en": "Common difficulties", "fr": "Difficultés fréquentes"},
    'CUANDO LA PRÁCTICA <span class="a">SE ATASCA</span>': {
        "en": 'WHEN THE PRACTICE <span class="a">GETS STUCK</span>',
        "fr": 'QUAND LA PRATIQUE <span class="a">BLOQUE</span>'},
    "Lo que te pasa": {"en": "What is happening", "fr": "Ce qui vous arrive"},
    "Por qué ocurre": {"en": "Why it happens", "fr": "Pourquoi cela arrive"},
    "Qué hacer": {"en": "What to do", "fr": "Que faire"},
    "«No puedo dejar de pensar»": {
        "en": "«I cannot stop thinking»", "fr": "« Je n'arrive pas à arrêter de penser »"},
    "Estás intentando vaciar la mente, que no es el objetivo": {
        "en": "You are trying to empty your mind, which is not the goal",
        "fr": "Vous essayez de vider votre esprit, ce qui n'est pas le but"},
    "Cada vez que vuelves, has hecho una repetición. Ese es el ejercicio": {
        "en": "Every time you come back, you have done a repetition. That is the exercise",
        "fr": "Chaque fois que vous revenez, vous faites une répétition. C'est ça, l'exercice"},
    "Me quedo dormido": {"en": "I fall asleep", "fr": "Je m'endors"},
    "Practicas tumbado y con déficit de sueño": {
        "en": "You practise lying down and short on sleep",
        "fr": "Vous pratiquez allongé et en manque de sommeil"},
    "Practica sentado, con los ojos entreabiertos y no en la cama": {
        "en": "Practise sitting, with eyes half open, and not in bed",
        "fr": "Pratiquez assis, les yeux entrouverts, et pas au lit"},
    "Me pongo más nervioso": {"en": "I get more anxious", "fr": "Je deviens plus nerveux"},
    "Al bajar el ruido externo aparece el interno": {
        "en": "When the outside noise drops, the inside noise appears",
        "fr": "Quand le bruit extérieur baisse, le bruit intérieur apparaît"},
    "Cambia a mindfulness al caminar o a la práctica de la ducha": {
        "en": "Switch to walking mindfulness or to the shower practice",
        "fr": "Passez à la pleine conscience en marchant ou à la pratique sous la douche"},
    "No tengo tiempo": {"en": "I have no time", "fr": "Je n'ai pas le temps"},
    "Estás apuntando a sesiones demasiado largas": {
        "en": "You are aiming at sessions that are too long",
        "fr": "Vous visez des séances trop longues"},
    "Tres minutos diarios superan a veinte minutos una vez por semana": {
        "en": "Three minutes daily beats twenty minutes once a week",
        "fr": "Trois minutes par jour valent mieux que vingt minutes une fois par semaine"},
    "Me aburro": {"en": "I get bored", "fr": "Je m'ennuie"},
    "Expectativa de que «pase algo»": {
        "en": "Expecting «something to happen»", "fr": "L'attente qu'« il se passe quelque chose »"},
    "El aburrimiento también se observa. Suele ser la puerta de entrada": {
        "en": "Boredom can be observed too. It is usually the way in",
        "fr": "L'ennui aussi s'observe. C'est souvent la porte d'entrée"},
    "Aparecen emociones intensas": {
        "en": "Intense emotions come up", "fr": "Des émotions intenses surgissent"},
    "El silencio deja espacio a lo que llevabas tapando": {
        "en": "Silence makes room for what you had been covering up",
        "fr": "Le silence laisse place à ce que vous recouvriez"},
    "Abre los ojos, respira y para. Si se repite, consúltalo con un profesional": {
        "en": "Open your eyes, breathe and stop. If it recurs, speak to a professional",
        "fr": "Ouvrez les yeux, respirez et arrêtez. Si cela se répète, consultez un professionnel"},
    'MENTE FUERTE, <span class="a">CUERPO FUERTE</span>': {
        "en": 'STRONG MIND, <span class="a">STRONG BODY</span>',
        "fr": 'ESPRIT FORT, <span class="a">CORPS FORT</span>'},
    "La respiración 4-7-8 de la página 6 es la pieza que\n        <strong>une la práctica con el descanso</strong>: úsala cada noche y el\n        programa sigue trabajando mientras duermes.": {
        "en": "The 4-7-8 breathing on page 6 is the piece that <strong>joins the practice to your rest</strong>: use it every night and the programme keeps working while you sleep.",
        "fr": "La respiration 4-7-8 de la page 6 est la pièce qui <strong>relie la pratique au repos</strong> : utilisez-la chaque soir et le programme continue de travailler pendant votre sommeil."},
    "<b>Aviso importante</b><br>\n      Este programa tiene finalidad informativa y educativa sobre técnicas de relajación y\n      atención plena. No constituye consejo médico ni psicológico, no es un tratamiento y no\n      sustituye la atención de un profesional sanitario colegiado. La meditación no debe\n      utilizarse como sustituto de terapia ni de medicación prescrita. Si padeces ansiedad grave,\n      depresión, trastorno de estrés postraumático, trastorno psicótico o disociativo, consulta\n      con tu profesional de salud mental antes de comenzar: algunas prácticas intensivas pueden\n      agravar ciertos cuadros. Interrumpe la práctica y busca ayuda profesional si aparece\n      malestar psicológico intenso. Las técnicas de respiración con retención están\n      contraindicadas en hipertensión no controlada, patología cardiaca o respiratoria y\n      embarazo. Contenido protegido por derechos de autor: prohibida su reproducción,\n      distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      This programme is for informational and educational purposes about relaxation and mindfulness techniques. It does not constitute medical or psychological advice, is not a treatment and does not replace care from a registered health professional. Meditation must not be used as a substitute for therapy or prescribed medication. If you have severe anxiety, depression, post-traumatic stress disorder, or a psychotic or dissociative disorder, consult your mental health professional before starting: some intensive practices can worsen certain conditions. Stop the practice and seek professional help if intense psychological distress appears. Breathing techniques involving breath holds are contraindicated in uncontrolled hypertension, cardiac or respiratory conditions and pregnancy. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Ce programme a une finalité informative et éducative sur les techniques de relaxation et de pleine conscience. Il ne constitue ni un avis médical ni psychologique, n'est pas un traitement et ne remplace pas la prise en charge par un professionnel de santé. La méditation ne doit pas se substituer à une thérapie ni à un traitement prescrit. En cas d'anxiété sévère, de dépression, de trouble de stress post-traumatique, de trouble psychotique ou dissociatif, consultez votre professionnel de santé mentale avant de commencer : certaines pratiques intensives peuvent aggraver certains tableaux. Interrompez la pratique et cherchez de l'aide si une souffrance psychologique intense apparaît. Les techniques avec rétention du souffle sont contre-indiquées en cas d'hypertension non contrôlée, de pathologie cardiaque ou respiratoire et de grossesse. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
