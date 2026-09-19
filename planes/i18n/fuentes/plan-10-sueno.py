# -*- coding: utf-8 -*-
"""
PLAN 10 · ELITE — Protocolo de sueño
====================================
Las horas, los grados y los miligramos no cambian. Sí cambia el formato de la
hora en inglés, donde «14:00» se escribe habitualmente «2 p.m.»; se mantiene
el reloj de 24 horas por coherencia con las tablas del resto del documento.
"""

T = {
    # ── Portada ───────────────────────────────────────────────────────
    '<small>Recuperación de élite</small><span class="glow">PROTOCOLO<br>DE SUEÑO</span>': {
        "en": '<small>Elite recovery</small><span class="glow">SLEEP<br>PROTOCOL</span>',
        "fr": '<small>Récupération d\'élite</small><span class="glow">PROTOCOLE<br>DE SOMMEIL</span>'},
    "La variable que el 90 % de los atletas ignora y que decide cuánto músculo construyes de todo lo que <em>entrenas</em>.": {
        "en": "The variable 90 % of athletes ignore, and the one that decides how much muscle you actually build from everything you <em>train</em>.",
        "fr": "La variable que 90 % des athlètes ignorent, et celle qui décide de la quantité de muscle que vous construisez réellement de tout ce que vous <em>entraînez</em>."},
    '<span class="chip on">Rutina de 10 min</span> <span class="chip on">10 reglas de higiene</span> <span class="chip">Solución de problemas</span> <span class="chip">Registro 14 días</span>': {
        "en": '<span class="chip on">10-min routine</span> <span class="chip on">10 hygiene rules</span> <span class="chip">Troubleshooting</span> <span class="chip">14-day log</span>',
        "fr": '<span class="chip on">Routine de 10 min</span> <span class="chip on">10 règles d\'hygiène</span> <span class="chip">Résolution de problèmes</span> <span class="chip">Carnet 14 jours</span>'},
    "De la GH se libera durmiendo": {
        "en": "Of GH is released while asleep", "fr": "De la GH est libérée en dormant"},
    "Objetivo diario": {"en": "Daily target", "fr": "Objectif quotidien"},
    '<strong>Edición 2026</strong><br><span class="muted">Protocolo de recuperación nocturna · 8 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">Night-time recovery protocol · 8 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Protocole de récupération nocturne · 8 pages</span>'},

    # ── 01 · Fundamentos ──────────────────────────────────────────────
    'EL SUEÑO ES TU MEJOR <span class="a">SUPLEMENTO</span>': {
        "en": 'SLEEP IS YOUR BEST <span class="a">SUPPLEMENT</span>',
        "fr": 'LE SOMMEIL EST VOTRE MEILLEUR <span class="a">COMPLÉMENT</span>'},
    "Durante el sueño se libera la mayor parte de la hormona de crecimiento, se acelera la síntesis proteica muscular, cae el cortisol y el sistema nervioso se regenera. Dormir mal tres noches seguidas puede reducir la testosterona de forma significativa y disparar el apetito al día siguiente.": {
        "en": "Most growth hormone is released during sleep, muscle protein synthesis speeds up, cortisol falls and the nervous system regenerates. Sleeping badly three nights in a row can lower testosterone significantly and send next-day appetite through the roof.",
        "fr": "C'est pendant le sommeil que se libère l'essentiel de l'hormone de croissance, que la synthèse protéique musculaire s'accélère, que le cortisol baisse et que le système nerveux se régénère. Mal dormir trois nuits d'affilée peut réduire la testostérone de façon significative et faire exploser l'appétit du lendemain."},
    "de la hormona de crecimiento": {
        "en": "of growth hormone", "fr": "de l'hormone de croissance"},
    "testosterona tras 3 malas noches": {
        "en": "testosterone after 3 bad nights", "fr": "testostérone après 3 mauvaises nuits"},
    "temperatura ideal": {"en": "ideal temperature", "fr": "température idéale"},
    "Qué pierdes exactamente cuando duermes mal": {
        "en": "Exactly what you lose when you sleep badly",
        "fr": "Ce que vous perdez exactement quand vous dormez mal"},
    "Consecuencia": {"en": "Consequence", "fr": "Conséquence"},
    "Mecanismo": {"en": "Mechanism", "fr": "Mécanisme"},
    "Cómo lo notas": {"en": "How you notice it", "fr": "Comment vous le remarquez"},
    "Menos ganancia muscular": {"en": "Less muscle gain", "fr": "Moins de gain musculaire"},
    "Cae la hormona de crecimiento del sueño profundo": {
        "en": "Growth hormone from deep sleep falls",
        "fr": "L'hormone de croissance du sommeil profond chute"},
    "El entreno no se traduce en progreso": {
        "en": "Training does not translate into progress",
        "fr": "L'entraînement ne se traduit pas en progrès"},
    "Más grasa acumulada": {"en": "More fat stored", "fr": "Plus de graisse accumulée"},
    "Sube el cortisol y baja la sensibilidad a la insulina": {
        "en": "Cortisol rises and insulin sensitivity falls",
        "fr": "Le cortisol monte et la sensibilité à l'insuline baisse"},
    "La cintura crece aunque la dieta no haya cambiado": {
        "en": "The waist grows even though the diet has not changed",
        "fr": "Le tour de taille augmente alors que l'alimentation n'a pas changé"},
    "Más hambre": {"en": "More hunger", "fr": "Plus de faim"},
    "Sube la grelina y baja la leptina": {
        "en": "Ghrelin rises and leptin falls", "fr": "La ghréline monte et la leptine baisse"},
    "Antojos de ultraprocesados por la tarde": {
        "en": "Cravings for ultra-processed food in the afternoon",
        "fr": "Envies d'aliments ultra-transformés l'après-midi"},
    "Menos fuerza": {"en": "Less strength", "fr": "Moins de force"},
    "Peor recuperación neural": {"en": "Poorer neural recovery", "fr": "Moins bonne récupération nerveuse"},
    "Las cargas de siempre se sienten pesadas": {
        "en": "Your usual loads feel heavy", "fr": "Les charges habituelles paraissent lourdes"},
    "Más riesgo de lesión": {"en": "Higher injury risk", "fr": "Plus de risque de blessure"},
    "Peor coordinación y tiempo de reacción": {
        "en": "Worse coordination and reaction time",
        "fr": "Moins bonne coordination et temps de réaction"},
    "Fallos técnicos que no cometías": {
        "en": "Technical errors you did not use to make",
        "fr": "Des erreurs techniques que vous ne faisiez pas"},
    "La arquitectura de tu noche": {
        "en": "The architecture of your night", "fr": "L'architecture de votre nuit"},
    "Qué ocurre en cada fase y qué pierdes si la recortas": {
        "en": "What happens in each phase and what you lose by cutting it short",
        "fr": "Ce qui se passe dans chaque phase et ce que vous perdez en l'écourtant"},
    "La rutina de 10 minutos": {"en": "The 10-minute routine", "fr": "La routine de 10 minutes"},
    "Minuto a minuto antes de apagar la luz": {
        "en": "Minute by minute before lights out",
        "fr": "Minute par minute avant d'éteindre"},
    "10 reglas de higiene del sueño": {
        "en": "10 rules of sleep hygiene", "fr": "10 règles d'hygiène du sommeil"},
    "Lo que sí cambia la calidad de tu descanso": {
        "en": "What actually changes the quality of your rest",
        "fr": "Ce qui change réellement la qualité de votre repos"},
    "Solución de problemas": {"en": "Troubleshooting", "fr": "Résolution de problèmes"},
    "No me duermo, me despierto, turnos, viajes": {
        "en": "Cannot fall asleep, waking up, shift work, travel",
        "fr": "Je ne m'endors pas, je me réveille, horaires décalés, voyages"},
    "Script de relajación y registro": {
        "en": "Relaxation script and log", "fr": "Script de relaxation et carnet"},
    "14 noches para encontrar tu patrón": {
        "en": "14 nights to find your pattern", "fr": "14 nuits pour trouver votre schéma"},

    # ── 02 · Arquitectura ─────────────────────────────────────────────
    "02 · Arquitectura": {"en": "02 · Architecture", "fr": "02 · Architecture"},
    'LA <span class="a">ARQUITECTURA</span> DE TU NOCHE': {
        "en": 'THE <span class="a">ARCHITECTURE</span> OF YOUR NIGHT',
        "fr": "L'<span class=\"a\">ARCHITECTURE</span> DE VOTRE NUIT"},
    "Qué ocurre en el cuerpo": {"en": "What happens in the body", "fr": "Ce qui se passe dans le corps"},
    "Consecuencia de perderla": {"en": "Cost of losing it", "fr": "Conséquence de la perdre"},
    "Sueño ligero (N1–N2)": {"en": "Light sleep (N1–N2)", "fr": "Sommeil léger (N1–N2)"},
    "20–30 min": {"en": "20–30 min", "fr": "20–30 min"},
    "Transición vigilia-sueño, baja la temperatura corporal": {
        "en": "Wake-to-sleep transition; body temperature drops",
        "fr": "Transition veille-sommeil, la température corporelle baisse"},
    "Dificultad para entrar en sueño profundo": {
        "en": "Trouble getting into deep sleep",
        "fr": "Difficulté à entrer en sommeil profond"},
    "Sueño profundo (N3)": {"en": "Deep sleep (N3)", "fr": "Sommeil profond (N3)"},
    "Menos ganancia muscular y más lesiones": {
        "en": "Less muscle gain and more injuries",
        "fr": "Moins de gain musculaire et plus de blessures"},
    "Sueño REM": {"en": "REM sleep", "fr": "Sommeil REM"},
    "90–110 min": {"en": "90–110 min", "fr": "90–110 min"},
    "Consolidación de memoria y regulación emocional": {
        "en": "Memory consolidation and emotional regulation",
        "fr": "Consolidation de la mémoire et régulation émotionnelle"},
    "Más estrés y peores decisiones": {
        "en": "More stress and worse decisions", "fr": "Plus de stress et de moins bonnes décisions"},
    "Los ciclos duran unos 90 minutos": {
        "en": "Cycles last about 90 minutes", "fr": "Les cycles durent environ 90 minutes"},
    "Una noche completa son 4–6 ciclos. Por eso despertarte a las 6 h o a las 7,5 h sienta mucho mejor que a las 6,5 h: estás cortando el ciclo por la mitad, en pleno sueño profundo. Ajusta tu hora de acostarte en bloques de 90 minutos hacia atrás desde la hora del despertador.": {
        "en": "A full night is 4–6 cycles. That is why waking at 6 h or at 7.5 h feels far better than at 6.5 h: you are cutting the cycle in half, in the middle of deep sleep. Set your bedtime in 90-minute blocks counted back from the alarm.",
        "fr": "Une nuit complète compte 4 à 6 cycles. C'est pourquoi se réveiller à 6 h ou à 7,5 h est bien plus agréable qu'à 6,5 h : vous coupez le cycle en deux, en plein sommeil profond. Réglez votre heure de coucher par blocs de 90 minutes en remontant depuis le réveil."},
    "El sueño profundo se concentra al principio de la noche": {
        "en": "Deep sleep is concentrated at the start of the night",
        "fr": "Le sommeil profond se concentre en début de nuit"},
    "La mayor parte del <strong>sueño profundo</strong> ocurre en los dos primeros ciclos. Acostarte tarde y compensar durmiendo hasta más tarde <strong>no</strong> recupera esa parte: se pierde.": {
        "en": "Most <strong>deep sleep</strong> happens in the first two cycles. Going to bed late and compensating by sleeping in does <strong>not</strong> recover that part: it is lost.",
        "fr": "L'essentiel du <strong>sommeil profond</strong> a lieu lors des deux premiers cycles. Se coucher tard et compenser en dormant plus tard ne récupère <strong>pas</strong> cette part : elle est perdue."},
    "El <strong>REM</strong> se concentra en la segunda mitad de la noche. Recortar la última hora de sueño castiga sobre todo tu regulación emocional y tu memoria.": {
        "en": "<strong>REM</strong> is concentrated in the second half of the night. Cutting the last hour of sleep mainly punishes your emotional regulation and your memory.",
        "fr": "Le <strong>REM</strong> se concentre dans la seconde moitié de la nuit. Couper la dernière heure de sommeil pénalise surtout votre régulation émotionnelle et votre mémoire."},
    "El alcohol adelanta el sueño profundo pero <strong>fragmenta el REM</strong>: te duermes antes y descansas mucho peor.": {
        "en": "Alcohol brings deep sleep forward but <strong>fragments REM</strong>: you fall asleep sooner and rest far worse.",
        "fr": "L'alcool avance le sommeil profond mais <strong>fragmente le REM</strong> : vous vous endormez plus vite et vous récupérez bien moins."},
    "<b>Fig. 1</b>Arquitectura de una noche completa": {
        "en": "<b>Fig. 1</b>Architecture of a full night",
        "fr": "<b>Fig. 1</b>Architecture d'une nuit complète"},
    "Cinco ciclos de unos 90 minutos. El <b>sueño profundo</b> se concentra al principio y el <b>REM</b> al final: por eso acostarse tarde y levantarse tarde no recupera lo mismo.": {
        "en": "Five cycles of about 90 minutes. <b>Deep sleep</b> is concentrated at the start and <b>REM</b> at the end: that is why going to bed late and getting up late does not recover the same thing.",
        "fr": "Cinq cycles d'environ 90 minutes. Le <b>sommeil profond</b> se concentre au début et le <b>REM</b> à la fin : c'est pourquoi se coucher tard et se lever tard ne récupère pas la même chose."},

    # ── 03 · Rutina ───────────────────────────────────────────────────
    "03 · Rutina pre-sueño": {"en": "03 · Pre-sleep routine", "fr": "03 · Routine avant le coucher"},
    'LA RUTINA DE LOS <span class="a">10 MINUTOS</span>': {
        "en": 'THE <span class="a">10-MINUTE</span> ROUTINE',
        "fr": 'LA ROUTINE DES <span class="a">10 MINUTES</span>'},
    "Apaga todas las pantallas: móvil, tablet y televisión": {
        "en": "Turn off every screen: phone, tablet and television",
        "fr": "Éteignez tous les écrans : téléphone, tablette et télévision"},
    "Eliminar la luz azul que inhibe la melatonina": {
        "en": "Remove the blue light that suppresses melatonin",
        "fr": "Supprimer la lumière bleue qui inhibe la mélatonine"},
    "Oscurece la habitación al máximo": {
        "en": "Darken the room as much as possible", "fr": "Obscurcissez la chambre au maximum"},
    "La oscuridad total maximiza la producción de melatonina": {
        "en": "Total darkness maximises melatonin production",
        "fr": "L'obscurité totale maximise la production de mélatonine"},
    "Ajusta la temperatura entre 18 y 20 °C": {
        "en": "Set the temperature between 18 and 20 °C",
        "fr": "Réglez la température entre 18 et 20 °C"},
    "El sueño profundo requiere que baje la temperatura corporal": {
        "en": "Deep sleep requires body temperature to fall",
        "fr": "Le sommeil profond exige que la température corporelle baisse"},
    "Respiración 4-7-8: cuatro ciclos completos": {
        "en": "4-7-8 breathing: four full cycles",
        "fr": "Respiration 4-7-8 : quatre cycles complets"},
    "Activar el sistema nervioso parasimpático": {
        "en": "Engage the parasympathetic nervous system",
        "fr": "Activer le système nerveux parasympathique"},
    "Escaneo corporal rápido de un minuto": {
        "en": "A quick one-minute body scan", "fr": "Un scan corporel rapide d'une minute"},
    "Liberar la tensión muscular acumulada del día": {
        "en": "Release the muscular tension built up during the day",
        "fr": "Relâcher la tension musculaire accumulée dans la journée"},
    "Frase de intención: «mañana seré mejor»": {
        "en": "An intention: «tomorrow I will be better»",
        "fr": "Une phrase d'intention : « demain je serai meilleur »"},
    "Cerrar el día y evitar la rumiación": {
        "en": "Close the day and head off rumination",
        "fr": "Clore la journée et éviter la rumination"},
    "Tu entorno óptimo": {"en": "Your ideal environment", "fr": "Votre environnement idéal"},
    "Cómo conseguirlo con poco presupuesto": {
        "en": "How to get there on a small budget",
        "fr": "Comment y parvenir avec un petit budget"},
    "Luz": {"en": "Light", "fr": "Lumière"},
    "Oscuridad total": {"en": "Total darkness", "fr": "Obscurité totale"},
    "Antifaz de tela y cinta negra sobre los LED de aparatos": {
        "en": "A cloth eye mask and black tape over device LEDs",
        "fr": "Un masque en tissu et du ruban noir sur les LED des appareils"},
    "Temperatura": {"en": "Temperature", "fr": "Température"},
    "Baja la calefacción y usa ropa de cama transpirable": {
        "en": "Turn the heating down and use breathable bedding",
        "fr": "Baissez le chauffage et utilisez une literie respirante"},
    "Ruido": {"en": "Noise", "fr": "Bruit"},
    "Constante o ausente": {"en": "Constant or absent", "fr": "Constant ou absent"},
    "Tapones de silicona o ruido blanco (lluvia, ventilador)": {
        "en": "Silicone earplugs or white noise (rain, a fan)",
        "fr": "Bouchons en silicone ou bruit blanc (pluie, ventilateur)"},
    "Aire": {"en": "Air", "fr": "Air"},
    "Renovado": {"en": "Fresh", "fr": "Renouvelé"},
    "Ventila 10 minutos antes de acostarte": {
        "en": "Air the room for 10 minutes before bed",
        "fr": "Aérez 10 minutes avant de vous coucher"},
    "Colchón y almohada": {"en": "Mattress and pillow", "fr": "Matelas et oreiller"},
    "Alineación cervical neutra": {"en": "Neutral neck alignment", "fr": "Alignement cervical neutre"},
    "Almohada baja si duermes boca abajo, alta si de lado": {
        "en": "A low pillow if you sleep on your front, a high one if on your side",
        "fr": "Oreiller bas si vous dormez sur le ventre, haut si sur le côté"},
    "Uso de la cama": {"en": "Use of the bed", "fr": "Usage du lit"},
    "Solo dormir": {"en": "Sleep only", "fr": "Dormir uniquement"},
    "Nada de trabajo, series ni móvil dentro de la cama": {
        "en": "No work, no series, no phone in the bed",
        "fr": "Ni travail, ni séries, ni téléphone dans le lit"},
    "Las últimas horas del día": {"en": "The last hours of the day", "fr": "Les dernières heures de la journée"},
    "Cuánto antes de dormir": {"en": "How long before sleep", "fr": "Combien de temps avant le coucher"},
    "Qué eliminar": {"en": "What to cut", "fr": "Ce qu'il faut supprimer"},
    "8–10 horas": {"en": "8–10 hours", "fr": "8–10 heures"},
    "Su vida media ronda las 5–6 horas: a las 22:00 aún tienes media dosis activa": {
        "en": "Its half-life is around 5–6 hours: at 22:00 half a dose is still active",
        "fr": "Sa demi-vie tourne autour de 5–6 heures : à 22 h, une demi-dose est encore active"},
    "3–4 horas": {"en": "3–4 hours", "fr": "3–4 heures"},
    "Entrenamiento intenso": {"en": "Intense training", "fr": "Entraînement intense"},
    "Eleva el cortisol y la temperatura corporal": {
        "en": "It raises cortisol and body temperature",
        "fr": "Il élève le cortisol et la température corporelle"},
    "3 horas": {"en": "3 hours", "fr": "3 heures"},
    "Comidas copiosas y alcohol": {"en": "Large meals and alcohol", "fr": "Repas copieux et alcool"},
    "La digestión y el alcohol fragmentan el sueño REM": {
        "en": "Digestion and alcohol fragment REM sleep",
        "fr": "La digestion et l'alcool fragmentent le sommeil REM"},
    "2 horas": {"en": "2 hours", "fr": "2 heures"},
    "Trabajo y discusiones": {"en": "Work and arguments", "fr": "Travail et discussions"},
    "La activación mental prolonga la latencia de sueño": {
        "en": "Mental activation lengthens sleep latency",
        "fr": "L'activation mentale allonge la latence d'endormissement"},
    "1 hora": {"en": "1 hour", "fr": "1 heure"},
    "Pantallas y luz intensa": {"en": "Screens and bright light", "fr": "Écrans et lumière vive"},
    "Retrasa la secreción de melatonina": {
        "en": "It delays melatonin secretion", "fr": "Cela retarde la sécrétion de mélatonine"},

    # ── 04 · Higiene ──────────────────────────────────────────────────
    "04 · Higiene del sueño": {"en": "04 · Sleep hygiene", "fr": "04 · Hygiène du sommeil"},
    '10 REGLAS DE HIGIENE <span class="a">PARA ATLETAS</span>': {
        "en": '10 HYGIENE RULES <span class="a">FOR ATHLETES</span>',
        "fr": "10 RÈGLES D'HYGIÈNE <span class=\"a\">POUR ATHLÈTES</span>"},
    "<b>Horario fijo</b>Acuéstate y levántate a la misma hora los siete días de la semana. Tu reloj biológico premia la consistencia por encima de cualquier otra cosa.": {
        "en": "<b>Fixed schedule</b>Go to bed and get up at the same time all seven days of the week. Your body clock rewards consistency above everything else.",
        "fr": "<b>Horaire fixe</b>Couchez-vous et levez-vous à la même heure les sept jours de la semaine. Votre horloge biologique récompense la régularité avant tout."},
    "<b>Cafeína con hora límite</b>Ni café, ni té verde, ni pre-entreno después de las 14:00. Su vida media hace que a medianoche todavía tengas cafeína circulando.": {
        "en": "<b>A cut-off time for caffeine</b>No coffee, no green tea and no pre-workout after 14:00. Its half-life means you still have caffeine circulating at midnight.",
        "fr": "<b>Une heure limite pour la caféine</b>Ni café, ni thé vert, ni pre-workout après 14 h. Sa demi-vie fait qu'à minuit, il en circule encore."},
    "<b>Cena favorable</b>Rica en triptófano —pavo, huevo, avena, lácteos— y con carbohidrato, que facilita su entrada al cerebro. Cena 2–3 horas antes.": {
        "en": "<b>A helpful dinner</b>Rich in tryptophan — turkey, egg, oats, dairy — with carbohydrate, which helps it reach the brain. Eat 2–3 hours before bed.",
        "fr": "<b>Un dîner favorable</b>Riche en tryptophane — dinde, œuf, avoine, produits laitiers — avec des glucides, qui facilitent son passage au cerveau. Dînez 2 à 3 heures avant."},
    "<b>Alcohol fuera</b>Fragmenta el sueño REM. Una sola copa puede reducir de forma apreciable la calidad de tu noche aunque te duermas antes.": {
        "en": "<b>No alcohol</b>It fragments REM sleep. A single drink can noticeably reduce the quality of your night even if you fall asleep sooner.",
        "fr": "<b>Pas d'alcool</b>Il fragmente le sommeil REM. Un seul verre peut réduire sensiblement la qualité de votre nuit même si vous vous endormez plus vite."},
    "<b>Entrenamiento temprano</b>Termina al menos 3 horas antes de acostarte. El entreno nocturno eleva cortisol y temperatura corporal justo cuando deberían bajar.": {
        "en": "<b>Train early</b>Finish at least 3 hours before bed. Evening training raises cortisol and body temperature exactly when they should be falling.",
        "fr": "<b>Entraînez-vous tôt</b>Terminez au moins 3 heures avant le coucher. L'entraînement du soir élève le cortisol et la température corporelle juste quand ils devraient baisser."},
    "<b>La cama solo para dormir</b>Nada de trabajar, ver series ni mirar el móvil en ella. El cerebro aprende asociaciones muy rápido, para bien y para mal.": {
        "en": "<b>The bed is for sleeping only</b>No working, no series, no phone in it. The brain learns associations very fast, for better and for worse.",
        "fr": "<b>Le lit sert seulement à dormir</b>Ni travail, ni séries, ni téléphone dedans. Le cerveau apprend très vite les associations, en bien comme en mal."},
    "<b>Ritual constante</b>Ducha caliente, 10 minutos de lectura en papel y respiración. La misma secuencia cada noche funciona como señal inequívoca para el cerebro.": {
        "en": "<b>A constant ritual</b>A hot shower, 10 minutes of reading on paper and some breathing. The same sequence every night works as an unmistakable signal for the brain.",
        "fr": "<b>Un rituel constant</b>Douche chaude, 10 minutes de lecture sur papier et respiration. La même séquence chaque soir agit comme un signal sans équivoque pour le cerveau."},
    "<b>Oscuridad total</b>Usa antifaz si hace falta. Incluso el LED del router puede interferir en la producción de melatonina.": {
        "en": "<b>Total darkness</b>Use an eye mask if you need to. Even the router's LED can interfere with melatonin production.",
        "fr": "<b>Obscurité totale</b>Utilisez un masque si nécessaire. Même la LED du routeur peut perturber la production de mélatonine."},
    "<b>Silencio o ruido constante</b>Lluvia, ventilador o máquina de ruido blanco. Lo que despierta no es el ruido en sí, sino el cambio brusco de nivel sonoro.": {
        "en": "<b>Silence or constant noise</b>Rain, a fan or a white noise machine. What wakes you is not the noise itself but the abrupt change in sound level.",
        "fr": "<b>Silence ou bruit constant</b>Pluie, ventilateur ou machine à bruit blanc. Ce qui réveille n'est pas le bruit en soi, mais le changement brusque de niveau sonore."},
    "<b>Luz por la mañana</b>10–15 minutos de luz natural al levantarte. Es la señal que ancla tu ritmo circadiano y la que hará que a la noche tengas sueño a tu hora.": {
        "en": "<b>Morning light</b>10–15 minutes of natural light when you get up. It is the signal that anchors your circadian rhythm and the reason you will feel sleepy on time at night.",
        "fr": "<b>Lumière du matin</b>10 à 15 minutes de lumière naturelle au lever. C'est le signal qui ancre votre rythme circadien et qui vous rendra somnolent à la bonne heure le soir."},
    "Si solo puedes cambiar una cosa": {
        "en": "If you can only change one thing", "fr": "Si vous ne pouvez changer qu'une chose"},
    "Elige el <strong>horario fijo</strong>. Es la intervención con mayor impacto y la única que hace que todas las demás funcionen mejor. Levantarte siempre a la misma hora —incluso el domingo— vale más que cualquier suplemento para dormir.": {
        "en": "Choose the <strong>fixed schedule</strong>. It is the highest-impact intervention and the only one that makes all the others work better. Always getting up at the same time — Sunday included — is worth more than any sleep supplement.",
        "fr": "Choisissez l'<strong>horaire fixe</strong>. C'est l'intervention au plus fort impact et la seule qui fasse mieux fonctionner toutes les autres. Se lever toujours à la même heure — dimanche compris — vaut mieux que n'importe quel complément pour dormir."},

    # ── 05 · Problemas ────────────────────────────────────────────────
    "05 · Solución de problemas": {
        "en": "05 · Troubleshooting", "fr": "05 · Résolution de problèmes"},
    'CUANDO ALGO <span class="a">NO FUNCIONA</span>': {
        "en": 'WHEN SOMETHING <span class="a">IS NOT WORKING</span>',
        "fr": 'QUAND QUELQUE CHOSE <span class="a">NE MARCHE PAS</span>'},
    "Tu problema": {"en": "Your problem", "fr": "Votre problème"},
    "Causa habitual": {"en": "Usual cause", "fr": "Cause habituelle"},
    "Qué hacer esta misma noche": {"en": "What to do tonight", "fr": "Que faire dès ce soir"},
    "Tardo más de 30 min en dormirme": {
        "en": "It takes me over 30 min to fall asleep",
        "fr": "Je mets plus de 30 min à m'endormir"},
    "Activación mental y rumiación": {
        "en": "Mental activation and rumination", "fr": "Activation mentale et rumination"},
    "Levántate, ve a otra habitación con luz tenue y vuelve cuando tengas sueño": {
        "en": "Get up, go to another room with dim light and come back when you feel sleepy",
        "fr": "Levez-vous, allez dans une autre pièce en lumière tamisée et revenez quand le sommeil arrive"},
    "Me despierto a las 3 de la madrugada": {
        "en": "I wake up at 3 in the morning", "fr": "Je me réveille à 3 h du matin"},
    "Alcohol, cena tardía o estrés": {
        "en": "Alcohol, a late dinner or stress", "fr": "Alcool, dîner tardif ou stress"},
    "Sin pantallas ni reloj: respiración 4-7-8 tumbado sin intentar dormirte": {
        "en": "No screens and no clock: 4-7-8 breathing lying down, without trying to fall asleep",
        "fr": "Ni écran ni horloge : respiration 4-7-8 allongé, sans chercher à vous endormir"},
    "Duermo pero amanezco cansado": {
        "en": "I sleep but wake up tired", "fr": "Je dors mais je me réveille fatigué"},
    "Sueño fragmentado o apnea": {"en": "Fragmented sleep or apnoea", "fr": "Sommeil fragmenté ou apnée"},
    "Revisa ronquidos y pausas respiratorias: consulta médica si las hay": {
        "en": "Check for snoring and breathing pauses: see a doctor if there are any",
        "fr": "Vérifiez ronflements et pauses respiratoires : consultez un médecin s'il y en a"},
    "Me duermo viendo la tele": {"en": "I fall asleep watching TV", "fr": "Je m'endors devant la télé"},
    "Sueño de mala calidad por luz y ruido": {
        "en": "Poor-quality sleep from light and noise",
        "fr": "Sommeil de mauvaise qualité à cause de la lumière et du bruit"},
    "Adelanta la hora de acostarte 30 min y apaga la pantalla": {
        "en": "Move your bedtime 30 min earlier and turn the screen off",
        "fr": "Avancez votre coucher de 30 min et éteignez l'écran"},
    "Trabajo a turnos": {"en": "I work shifts", "fr": "Je travaille en horaires décalés"},
    "Desajuste circadiano": {"en": "Circadian misalignment", "fr": "Décalage circadien"},
    "Gafas de sol al volver de noche, oscuridad total y horario fijo dentro de cada turno": {
        "en": "Sunglasses on the way home at night, total darkness and a fixed schedule within each shift",
        "fr": "Lunettes de soleil au retour de nuit, obscurité totale et horaire fixe dans chaque rotation"},
    "Viajo y cambio de huso horario": {
        "en": "I travel and change time zone", "fr": "Je voyage et change de fuseau horaire"},
    "Jet lag": {"en": "Jet lag", "fr": "Décalage horaire"},
    "Ajusta comidas y luz al horario de destino desde el primer día": {
        "en": "Set meals and light to the destination's schedule from day one",
        "fr": "Calez repas et lumière sur l'horaire de destination dès le premier jour"},
    "Entreno de noche por trabajo": {
        "en": "I train at night because of work", "fr": "Je m'entraîne le soir à cause du travail"},
    "Activación tardía": {"en": "Late activation", "fr": "Activation tardive"},
    "Ducha templada al llegar, cena ligera y 10 min de respiración": {
        "en": "A warm shower on arrival, a light dinner and 10 min of breathing",
        "fr": "Douche tiède en rentrant, dîner léger et 10 min de respiration"},
    "Me despierta el móvil": {"en": "My phone wakes me", "fr": "Mon téléphone me réveille"},
    "Notificaciones": {"en": "Notifications", "fr": "Notifications"},
    "Modo avión y cargador fuera del dormitorio, sin excepciones": {
        "en": "Aeroplane mode and charger outside the bedroom, no exceptions",
        "fr": "Mode avion et chargeur hors de la chambre, sans exception"},
    "La siesta, bien usada": {"en": "The nap, used well", "fr": "La sieste, bien utilisée"},
    "Efecto": {"en": "Effect", "fr": "Effet"},
    "Recomendación": {"en": "Recommendation", "fr": "Recommandation"},
    "10–20 min": {"en": "10–20 min", "fr": "10–20 min"},
    "Recupera alerta sin inercia de sueño": {
        "en": "Restores alertness with no sleep inertia",
        "fr": "Restaure la vigilance sans inertie du sommeil"},
    '<span class="tag ok">Ideal</span> antes de las 15:00': {
        "en": '<span class="tag ok">Ideal</span> before 15:00',
        "fr": '<span class="tag ok">Idéale</span> avant 15 h'},
    "30–60 min": {"en": "30–60 min", "fr": "30–60 min"},
    "Te despiertas aturdido": {"en": "You wake up groggy", "fr": "Vous vous réveillez groggy"},
    '<span class="tag mid">Evítala</span> salvo privación severa': {
        "en": '<span class="tag mid">Avoid it</span> except in severe deprivation',
        "fr": '<span class="tag mid">Évitez-la</span> sauf privation sévère'},
    "90 min": {"en": "90 min", "fr": "90 min"},
    "Ciclo completo, sin aturdimiento": {
        "en": "A full cycle, no grogginess", "fr": "Cycle complet, sans étourdissement"},
    '<span class="tag lo">Válida</span> solo si dormiste muy poco': {
        "en": '<span class="tag lo">Valid</span> only if you slept very little',
        "fr": '<span class="tag lo">Valable</span> seulement si vous avez très peu dormi'},
    "Cuándo dejar de improvisar y consultar al médico": {
        "en": "When to stop improvising and see a doctor",
        "fr": "Quand cesser d'improviser et consulter un médecin"},
    "Ronquido intenso con pausas respiratorias, somnolencia diurna incapacitante, insomnio de más de tres semanas, piernas inquietas al acostarte o despertares con ahogo. Son signos de trastornos del sueño que requieren <strong>diagnóstico profesional</strong>: ningún protocolo de higiene los resuelve.": {
        "en": "Loud snoring with breathing pauses, disabling daytime sleepiness, insomnia lasting more than three weeks, restless legs at bedtime or waking up choking. These are signs of sleep disorders that require <strong>professional diagnosis</strong>: no hygiene protocol resolves them.",
        "fr": "Ronflement intense avec pauses respiratoires, somnolence diurne invalidante, insomnie de plus de trois semaines, jambes sans repos au coucher ou réveils avec sensation d'étouffement. Ce sont des signes de troubles du sommeil qui exigent un <strong>diagnostic professionnel</strong> : aucun protocole d'hygiène ne les résout."},

    # ── 06 · Script y registro ────────────────────────────────────────
    "06 · Script y registro": {"en": "06 · Script and log", "fr": "06 · Script et carnet"},
    'RELAJACIÓN PRE-SUEÑO <span class="a">Y REGISTRO</span>': {
        "en": 'PRE-SLEEP RELAXATION <span class="a">AND LOG</span>',
        "fr": 'RELAXATION AVANT LE COUCHER <span class="a">ET CARNET</span>'},
    "Script · Relajación muscular progresiva (5 min)": {
        "en": "Script · Progressive muscle relaxation (5 min)",
        "fr": "Script · Relaxation musculaire progressive (5 min)"},
    "«Túmbate boca arriba. Siente el peso de tu cuerpo sobre el colchón. Empieza por los pies: tensa los músculos del pie durante 3 segundos y suéltalos por completo. Siente la diferencia entre tensión y relajación. Sube por las pantorrillas, los muslos, los glúteos, el abdomen, el pecho, los hombros, los brazos y el cuello. Al llegar a la cara, suelta la mandíbula y suaviza los ojos. Todo tu cuerpo está ahora completamente relajado y pesado. Deja que el sueño llegue por sí solo — no lo persigas.»": {
        "en": "«Lie on your back. Feel the weight of your body on the mattress. Start with the feet: tense the muscles of the foot for 3 seconds and release them completely. Feel the difference between tension and release. Move up through the calves, the thighs, the glutes, the abdomen, the chest, the shoulders, the arms and the neck. When you reach the face, unclench the jaw and soften the eyes. Your whole body is now completely relaxed and heavy. Let sleep come on its own — do not chase it.»",
        "fr": "« Allongez-vous sur le dos. Sentez le poids de votre corps sur le matelas. Commencez par les pieds : contractez les muscles du pied pendant 3 secondes puis relâchez complètement. Sentez la différence entre tension et relâchement. Remontez par les mollets, les cuisses, les fessiers, l'abdomen, la poitrine, les épaules, les bras et le cou. Arrivé au visage, desserrez la mâchoire et adoucissez les yeux. Tout votre corps est maintenant complètement détendu et lourd. Laissez le sommeil venir de lui-même — ne le poursuivez pas. »"},
    "Registro de 14 noches": {"en": "14-night log", "fr": "Carnet de 14 nuits"},
    "Hora de acostarme": {"en": "Bedtime", "fr": "Heure du coucher"},
    "Minutos en dormirme": {"en": "Minutes to fall asleep", "fr": "Minutes pour m'endormir"},
    "Despertares": {"en": "Awakenings", "fr": "Réveils"},
    "Hora de despertar": {"en": "Wake time", "fr": "Heure du réveil"},
    "Calidad 1-10": {"en": "Quality 1-10", "fr": "Qualité 1-10"},
    "Rutina 10 min": {"en": "10-min routine", "fr": "Routine 10 min"},
    "Al terminar las dos semanas busca el patrón: ¿las noches de mayor calidad coinciden con la rutina completada, con la hora fija o con haber entrenado por la mañana? Ahí está tu palanca.": {
        "en": "When the two weeks are up, look for the pattern: do your best nights line up with the routine completed, with the fixed schedule, or with having trained in the morning? That is your lever.",
        "fr": "Au terme des deux semaines, cherchez le schéma : vos meilleures nuits coïncident-elles avec la routine effectuée, avec l'horaire fixe ou avec un entraînement du matin ? C'est là qu'est votre levier."},

    # ── 07 · Suplementación ───────────────────────────────────────────
    "07 · Suplementación": {"en": "07 · Supplementation", "fr": "07 · Compléments"},
    'SUPLEMENTOS PARA <span class="a">DORMIR MEJOR</span>': {
        "en": 'SUPPLEMENTS FOR <span class="a">BETTER SLEEP</span>',
        "fr": 'COMPLÉMENTS POUR <span class="a">MIEUX DORMIR</span>'},
    "Ninguno sustituye a la higiene del sueño. Úsalos solo cuando las páginas anteriores ya formen parte de tu rutina y sigan quedándose cortas.": {
        "en": "None of them replaces sleep hygiene. Use them only once the previous pages are already part of your routine and still fall short.",
        "fr": "Aucun ne remplace l'hygiène du sommeil. Ne les utilisez que lorsque les pages précédentes font déjà partie de votre routine et restent insuffisantes."},
    "Evidencia y matices": {"en": "Evidence and caveats", "fr": "Preuves et nuances"},
    "Magnesio bisglicinato": {"en": "Magnesium bisglycinate", "fr": "Magnésium bisglycinate"},
    "300–400 mg": {"en": "300–400 mg", "fr": "300–400 mg"},
    "30–60 min antes": {"en": "30–60 min before", "fr": "30–60 min avant"},
    "El más útil del grupo: mejora la profundidad y ayuda a modular el cortisol": {
        "en": "The most useful of the group: it improves depth and helps modulate cortisol",
        "fr": "Le plus utile du lot : il améliore la profondeur et aide à moduler le cortisol"},
    "Melatonina": {"en": "Melatonin", "fr": "Mélatonine"},
    "0,5–1 mg": {"en": "0.5–1 mg", "fr": "0,5–1 mg"},
    "Es un regulador de horario, no un somnífero. Dosis altas no funcionan mejor": {
        "en": "It is a timing regulator, not a sleeping pill. Higher doses do not work better",
        "fr": "C'est un régulateur d'horaire, pas un somnifère. Les fortes doses ne marchent pas mieux"},
    "L-teanina": {"en": "L-theanine", "fr": "L-théanine"},
    "100–200 mg": {"en": "100–200 mg", "fr": "100–200 mg"},
    "30 min antes": {"en": "30 min before", "fr": "30 min avant"},
    "Reduce la activación mental sin sedar. Buena si tu problema es la rumiación": {
        "en": "It reduces mental activation without sedating. Good if rumination is your problem",
        "fr": "Elle réduit l'activation mentale sans sédation. Utile si votre problème est la rumination"},
    "Glicina": {"en": "Glycine", "fr": "Glycine"},
    "Ayuda a bajar la temperatura corporal central": {
        "en": "It helps lower core body temperature",
        "fr": "Elle aide à faire baisser la température corporelle centrale"},
    "Evidencia moderada sobre estrés percibido y calidad de sueño": {
        "en": "Moderate evidence on perceived stress and sleep quality",
        "fr": "Preuves modérées sur le stress perçu et la qualité du sommeil"},
    "Sobre la melatonina": {"en": "About melatonin", "fr": "À propos de la mélatonine"},
    "No es inocua por ser «natural» ni debe usarse a diario de forma indefinida sin supervisión. Está desaconsejada en menores, embarazo, lactancia y en personas con enfermedades autoinmunes o que tomen anticoagulantes o antihipertensivos. Consulta con tu médico o farmacéutico antes de empezar.": {
        "en": "It is not harmless just because it is «natural», and it should not be used daily and indefinitely without supervision. It is not advised for minors, in pregnancy or breastfeeding, or for people with autoimmune diseases or taking anticoagulants or antihypertensives. Check with your doctor or pharmacist before starting.",
        "fr": "Elle n'est pas inoffensive parce qu'elle est « naturelle » et ne doit pas être prise quotidiennement et indéfiniment sans suivi. Elle est déconseillée chez les mineurs, pendant la grossesse et l'allaitement, et chez les personnes atteintes de maladies auto-immunes ou sous anticoagulants ou antihypertenseurs. Consultez votre médecin ou votre pharmacien avant de commencer."},
    'DUERME BIEN, <span class="a">ENTRENA MEJOR</span>': {
        "en": 'SLEEP WELL, <span class="a">TRAIN BETTER</span>',
        "fr": 'DORMEZ BIEN, <span class="a">ENTRAÎNEZ-VOUS MIEUX</span>'},
    "El sueño es el frente que <strong>decide si los otros rinden</strong>: se\n        entrena a la misma hora todos los días, se mide durante catorce noches y se corrige con\n        una sola variable cada vez, exactamente igual que la fuerza.": {
        "en": "Sleep is the front that <strong>decides whether the others pay off</strong>: you train it at the same time every day, measure it over fourteen nights and correct it one variable at a time, exactly like strength.",
        "fr": "Le sommeil est le front qui <strong>décide si les autres rapportent</strong> : il s'entraîne à la même heure chaque jour, se mesure sur quatorze nuits et se corrige une variable à la fois, exactement comme la force."},
    "<b>Aviso importante</b><br>\n      Documento con finalidad informativa y educativa. No constituye consejo médico, diagnóstico\n      ni tratamiento, y no sustituye la valoración de un profesional sanitario colegiado. Los\n      trastornos del sueño —insomnio crónico, apnea obstructiva, síndrome de piernas inquietas,\n      narcolepsia— requieren diagnóstico y tratamiento médico. Consulta con tu médico antes de\n      tomar cualquier suplemento para dormir, especialmente si tomas medicación, padeces alguna\n      patología, estás embarazada o en periodo de lactancia, o eres menor de edad. Las cifras\n      citadas son estimaciones divulgativas procedentes de la literatura general sobre sueño y\n      rendimiento, y varían entre personas. Contenido protegido por derechos de autor: prohibida\n      su reproducción, distribución o reventa sin autorización escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br>\n      A document for informational and educational purposes. It does not constitute medical advice, diagnosis or treatment, and it does not replace assessment by a registered health professional. Sleep disorders — chronic insomnia, obstructive apnoea, restless legs syndrome, narcolepsy — require medical diagnosis and treatment. Consult your doctor before taking any sleep supplement, especially if you take medication, have a medical condition, are pregnant or breastfeeding, or are a minor. The figures quoted are general estimates drawn from the wider literature on sleep and performance, and they vary between individuals. Copyrighted content: reproduction, distribution or resale without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br>\n      Document à finalité informative et éducative. Il ne constitue ni un avis médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation d'un professionnel de santé. Les troubles du sommeil — insomnie chronique, apnée obstructive, syndrome des jambes sans repos, narcolepsie — exigent un diagnostic et un traitement médicaux. Consultez votre médecin avant de prendre tout complément pour dormir, en particulier si vous êtes sous traitement, atteint d'une pathologie, enceinte ou allaitante, ou mineur. Les chiffres cités sont des estimations de vulgarisation issues de la littérature générale sur le sommeil et la performance, et varient d'une personne à l'autre. Contenu protégé par le droit d'auteur : toute reproduction, distribution ou revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
