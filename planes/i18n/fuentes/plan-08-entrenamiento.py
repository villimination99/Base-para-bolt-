# -*- coding: utf-8 -*-
"""
08 · PLAN DE ENTRENAMIENTO 8 SEMANAS — inglés y francés
=======================================================
El vocabulario de sala tiene un original inglés en casi todos los casos (hip
thrust, face pull, rest-pause, push/pull/legs). Cuando el término inglés es el
que se usa de verdad en un gimnasio francés, se conserva: traducirlo por un
calco correcto pero inexistente dejaría al comprador sin poder pedir la máquina.

Las abreviaturas técnicas (RIR, 1RM, 4×10) son iguales en los tres idiomas y no
se tocan: son notación, no prosa.
"""

T = {

    # ── Portada ────────────────────────────────────────────────────────────
    '<small>De principiante a avanzado</small><span class="glow">PLAN DE<br>ENTRENAMIENTO</span>': {
        "en": '<small>From beginner to advanced</small><span class="glow">TRAINING<br>PLAN</span>',
        "fr": '<small>Du débutant au confirmé</small><span class="glow">PLAN<br>D\'ENTRAÎNEMENT</span>'},

    "Ocho semanas en cuatro fases progresivas, con los 30 ejercicios "
    "fundamentales explicados <em>error por error</em>.": {
        "en": "Eight weeks in four progressive phases, with the 30 fundamental exercises "
              "explained <em>mistake by mistake</em>.",
        "fr": "Huit semaines en quatre phases progressives, avec les 30 exercices "
              "fondamentaux expliqués <em>erreur par erreur</em>."},

    '<span class="chip on">4 fases</span> '
    '<span class="chip on">30 ejercicios</span> '
    '<span class="chip">Registro de cargas</span> '
    '<span class="chip">Descargas incluidas</span>': {
        "en": '<span class="chip on">4 phases</span> '
              '<span class="chip on">30 exercises</span> '
              '<span class="chip">Load log</span> '
              '<span class="chip">Deloads included</span>',
        "fr": '<span class="chip on">4 phases</span> '
              '<span class="chip on">30 exercices</span> '
              '<span class="chip">Suivi des charges</span> '
              '<span class="chip">Décharges incluses</span>'},

    "Ejercicios": {"en": "Exercises", "fr": "Exercices"},
    "Fases progresivas": {"en": "Progressive phases", "fr": "Phases progressives"},

    '<strong>Edición 2026</strong><br><span class="muted">Programa de fuerza e hipertrofia · 11 páginas</span>': {
        "en": '<strong>2026 edition</strong><br><span class="muted">Strength and hypertrophy programme · 11 pages</span>',
        "fr": '<strong>Édition 2026</strong><br><span class="muted">Programme de force et d\'hypertrophie · 11 pages</span>'},

    # ── 01 · Estructura ────────────────────────────────────────────────────
    "01 · Estructura": {"en": "01 · Structure", "fr": "01 · Structure"},

    'CUATRO FASES <span class="a">PROGRESIVAS</span>': {
        "en": 'FOUR PROGRESSIVE <span class="a">PHASES</span>',
        "fr": 'QUATRE PHASES <span class="a">PROGRESSIVES</span>'},

    "Cada fase construye sobre la anterior: técnica, base de fuerza, intensidad "
    "máxima y definición. Saltarte una es la forma más eficiente de estancarte o lesionarte.": {
        "en": "Each phase builds on the one before it: technique, strength base, peak "
              "intensity and getting lean. Skipping one is the most efficient way to stall "
              "or get injured.",
        "fr": "Chaque phase s'appuie sur la précédente : technique, base de force, intensité "
              "maximale et sèche. En sauter une est la façon la plus efficace de stagner ou "
              "de se blesser."},

    "Volumen": {"en": "Volume", "fr": "Volume"},
    "Intensidad": {"en": "Intensity", "fr": "Intensité"},

    '<span class="tag lo">1 · Activación</span>': {
        "en": '<span class="tag lo">1 · Activation</span>',
        "fr": '<span class="tag lo">1 · Activation</span>'},
    "12–16 series/sem": {"en": "12–16 sets/wk", "fr": "12–16 séries/sem"},
    "60–70 % 1RM": {"en": "60–70 % 1RM", "fr": "60–70 % 1RM"},
    "Aprender técnica y activar patrones": {
        "en": "Learn the technique and switch the patterns on",
        "fr": "Apprendre la technique et activer les schémas moteurs"},

    '<span class="tag ok">2 · Desarrollo</span>': {
        "en": '<span class="tag ok">2 · Development</span>',
        "fr": '<span class="tag ok">2 · Développement</span>'},
    "Básico": {"en": "Basic", "fr": "Basique"},
    "16–20 series/sem": {"en": "16–20 sets/wk", "fr": "16–20 séries/sem"},
    "65–75 % 1RM": {"en": "65–75 % 1RM", "fr": "65–75 % 1RM"},
    "Construir base de fuerza e hipertrofia": {
        "en": "Build a base of strength and hypertrophy",
        "fr": "Construire une base de force et d'hypertrophie"},

    '<span class="tag mid">3 · Intensificación</span>': {
        "en": '<span class="tag mid">3 · Intensification</span>',
        "fr": '<span class="tag mid">3 · Intensification</span>'},
    "20–24 series/sem": {"en": "20–24 sets/wk", "fr": "20–24 séries/sem"},
    "75–85 % 1RM": {"en": "75–85 % 1RM", "fr": "75–85 % 1RM"},
    "Máxima hipertrofia y primeros récords": {
        "en": "Peak hypertrophy and your first personal records",
        "fr": "Hypertrophie maximale et premiers records"},

    '<span class="tag hi">4 · Quema</span>': {
        "en": '<span class="tag hi">4 · Burn</span>',
        "fr": '<span class="tag hi">4 · Sèche</span>'},
    "18–22 series/sem": {"en": "18–22 sets/wk", "fr": "18–22 séries/sem"},
    "70–80 % + HIIT": {"en": "70–80 % + HIIT", "fr": "70–80 % + HIIT"},
    "Definir manteniendo la masa muscular": {
        "en": "Get lean while keeping the muscle",
        "fr": "S'affûter en conservant la masse musculaire"},

    "Los tres conceptos que necesitas dominar": {
        "en": "The three concepts you need to master",
        "fr": "Les trois notions que vous devez maîtriser"},

    "Repeticiones en reserva: las que <em>podrías</em> hacer al terminar "
    "la serie. RIR 2 significa que te quedaban dos. Es la forma más fiable de regular la "
    "intensidad sin calcular tu 1RM.": {
        "en": "Reps in reserve: the ones you <em>could</em> still have done when the set "
              "ended. RIR 2 means two were left. It is the most reliable way to regulate "
              "intensity without calculating your 1RM.",
        "fr": "Répétitions en réserve : celles que vous <em>auriez pu</em> faire en plus à "
              "la fin de la série. RIR 2 signifie qu'il vous en restait deux. C'est la façon "
              "la plus fiable de régler l'intensité sans calculer votre 1RM."},

    "Sobrecarga progresiva": {"en": "Progressive overload", "fr": "Surcharge progressive"},
    "Cada semana: más peso, más repeticiones o mejor ejecución con el "
    "mismo peso. Si ninguna de las tres sube, no estás progresando.": {
        "en": "Every week: more weight, more reps, or better execution at the same weight. "
              "If none of the three goes up, you are not progressing.",
        "fr": "Chaque semaine : plus de poids, plus de répétitions, ou une meilleure "
              "exécution au même poids. Si aucune des trois ne monte, vous ne progressez pas."},

    "Volumen efectivo": {"en": "Effective volume", "fr": "Volume efficace"},
    "Series por grupo muscular y semana llevadas cerca del fallo. "
    "Entre 10 y 20 es el rango donde ocurre casi todo el crecimiento.": {
        "en": "Sets per muscle group per week taken close to failure. Between 10 and 20 is "
              "the range where almost all the growth happens.",
        "fr": "Séries par groupe musculaire et par semaine menées près de l'échec. Entre 10 "
              "et 20, c'est la zone où se produit presque toute la croissance."},

    "Fase 1 · Activación": {"en": "Phase 1 · Activation", "fr": "Phase 1 · Activation"},
    "Full body 3 días con los 8 patrones básicos": {
        "en": "Full body 3 days a week with the 8 basic patterns",
        "fr": "Full body 3 jours avec les 8 schémas de base"},
    "Fase 2 · Desarrollo": {"en": "Phase 2 · Development", "fr": "Phase 2 · Développement"},
    "Push / Pull / Legs, 4 días por semana": {
        "en": "Push / Pull / Legs, 4 days a week",
        "fr": "Push / Pull / Legs, 4 jours par semaine"},
    "Fase 3 · Intensificación": {
        "en": "Phase 3 · Intensification", "fr": "Phase 3 · Intensification"},
    "Torso / Pierna, 5 días y técnicas de intensidad": {
        "en": "Upper / Lower, 5 days plus intensity techniques",
        "fr": "Haut / Bas, 5 jours et techniques d'intensité"},
    "Fase 4 · Quema": {"en": "Phase 4 · Burn", "fr": "Phase 4 · Sèche"},
    "Superseries, circuitos y HIIT integrado": {
        "en": "Supersets, circuits and integrated HIIT",
        "fr": "Supersets, circuits et HIIT intégré"},
    "Mapa muscular de referencia": {
        "en": "Reference muscle map", "fr": "Carte musculaire de référence"},
    "Los 30 ejercicios, uno a uno": {
        "en": "The 30 exercises, one by one", "fr": "Les 30 exercices, un par un"},
    "Técnica, error común y consejo clave": {
        "en": "Technique, common mistake and key tip",
        "fr": "Technique, erreur courante et conseil clé"},
    "Pág. 8–9": {"en": "P. 8–9", "fr": "P. 8–9"},

    # ── Fase 1 ─────────────────────────────────────────────────────────────
    "Fase 1 · Semanas 1–2": {"en": "Phase 1 · Weeks 1–2", "fr": "Phase 1 · Semaines 1–2"},

    'FASE 1 · <span class="a">ACTIVACIÓN</span>': {
        "en": 'PHASE 1 · <span class="a">ACTIVATION</span>',
        "fr": 'PHASE 1 · <span class="a">ACTIVATION</span>'},

    "Full body tres días por semana (lunes, miércoles y viernes) con al menos un "
    "día de descanso entre sesiones. <strong>La técnica manda sobre el peso</strong>: la forma "
    "perfecta previene lesiones y maximiza el estímulo real sobre el músculo.": {
        "en": "Full body three days a week (Monday, Wednesday and Friday) with at least one "
              "rest day between sessions. <strong>Technique outranks weight</strong>: perfect "
              "form prevents injury and maximises the real stimulus on the muscle.",
        "fr": "Full body trois jours par semaine (lundi, mercredi et vendredi) avec au moins "
              "un jour de repos entre les séances. <strong>La technique prime sur la "
              "charge</strong> : une exécution parfaite prévient les blessures et maximise "
              "le stimulus réel sur le muscle."},

    "Músculo": {"en": "Muscle", "fr": "Muscle"},
    "Series": {"en": "Sets", "fr": "Séries"},
    "Reps": {"en": "Reps", "fr": "Reps"},
    "Técnica clave": {"en": "Key technique", "fr": "Technique clé"},

    "Sentadilla con barra": {"en": "Barbell squat", "fr": "Squat à la barre"},
    "Cuádriceps, glúteo, core": {
        "en": "Quads, glutes, core", "fr": "Quadriceps, fessiers, gainage"},
    "Rodillas alineadas con los pies, espalda recta": {
        "en": "Knees tracking over the feet, back straight",
        "fr": "Genoux alignés sur les pieds, dos droit"},
    "Press banca plano": {"en": "Flat bench press", "fr": "Développé couché à plat"},
    "Pecho, tríceps": {"en": "Chest, triceps", "fr": "Pectoraux, triceps"},
    "Retracción escapular, codos a 45°": {
        "en": "Scapulae retracted, elbows at 45°",
        "fr": "Omoplates rétractées, coudes à 45°"},
    "Remo con barra": {"en": "Barbell row", "fr": "Rowing à la barre"},
    "Dorsal, bíceps": {"en": "Lats, biceps", "fr": "Grand dorsal, biceps"},
    "Torso a 45°, tira del codo hacia atrás": {
        "en": "Torso at 45°, pull the elbow back",
        "fr": "Buste à 45°, tirez le coude vers l'arrière"},
    "Press militar": {"en": "Overhead press", "fr": "Développé militaire"},
    "Hombro, tríceps": {"en": "Shoulders, triceps", "fr": "Épaules, triceps"},
    "Core activado, sin arquear la zona lumbar": {
        "en": "Core braced, no arching in the lower back",
        "fr": "Gainage actif, sans cambrer le bas du dos"},
    "Peso muerto rumano": {"en": "Romanian deadlift", "fr": "Soulevé de terre roumain"},
    "Isquiotibiales, glúteo": {
        "en": "Hamstrings, glutes", "fr": "Ischio-jambiers, fessiers"},
    "Bisagra de cadera, barra pegada a las piernas": {
        "en": "Hip hinge, bar grazing the legs",
        "fr": "Charnière de hanche, barre au contact des jambes"},
    "Dominadas asistidas": {"en": "Assisted pull-ups", "fr": "Tractions assistées"},
    "Amplitud completa, sin balanceo": {
        "en": "Full range, no swinging", "fr": "Amplitude complète, sans balancier"},
    "Zancadas caminando": {"en": "Walking lunges", "fr": "Fentes marchées"},
    "Cuádriceps, glúteo": {"en": "Quads, glutes", "fr": "Quadriceps, fessiers"},
    "10/lado": {"en": "10/side", "fr": "10/côté"},
    "La rodilla delantera no rebasa la punta del pie": {
        "en": "The front knee does not travel past the toes",
        "fr": "Le genou avant ne dépasse pas la pointe du pied"},
    "Plancha abdominal": {"en": "Abdominal plank", "fr": "Gainage ventral"},
    "Cadera neutra, ombligo activado": {
        "en": "Hip neutral, navel drawn in", "fr": "Bassin neutre, nombril rentré"},

    "Cómo elegir el peso de partida": {
        "en": "How to choose your starting weight",
        "fr": "Comment choisir votre charge de départ"},
    "<b>Serie de tanteo</b>Empieza con un peso que puedas mover 15 veces con facilidad "
    "evidente. Es tu punto de partida, no tu límite.": {
        "en": "<b>Feeler set</b>Start with a weight you can move 15 times with obvious ease. "
              "That is your starting point, not your ceiling.",
        "fr": "<b>Série de repérage</b>Commencez avec une charge que vous déplacez 15 fois "
              "avec une facilité évidente. C'est votre point de départ, pas votre limite."},
    "<b>Ajusta en la segunda serie</b>Si al llegar a 15 repeticiones te sobraban más de "
    "cuatro, sube entre un 5 y un 10 %.": {
        "en": "<b>Adjust on the second set</b>If you still had more than four reps left at "
              "15, add between 5 and 10 %.",
        "fr": "<b>Ajustez à la deuxième série</b>S'il vous restait plus de quatre "
              "répétitions à 15, montez de 5 à 10 %."},
    "<b>Termina con RIR 3</b>En esta fase debes acabar cada serie sabiendo que te quedaban "
    "tres repeticiones. Nada de fallo muscular.": {
        "en": "<b>Finish at RIR 3</b>In this phase you should end every set knowing three "
              "reps were left. No muscular failure.",
        "fr": "<b>Terminez à RIR 3</b>Dans cette phase, vous devez finir chaque série en "
              "sachant qu'il vous restait trois répétitions. Pas d'échec musculaire."},
    "<b>Anota todo desde el primer día</b>Sin registro no hay progresión, y la fase 2 "
    "empieza justo donde termina esta.": {
        "en": "<b>Log everything from day one</b>Without a record there is no progression, "
              "and phase 2 starts exactly where this one ends.",
        "fr": "<b>Notez tout dès le premier jour</b>Sans relevé il n'y a pas de progression, "
              "et la phase 2 commence exactement là où celle-ci s'arrête."},

    "Objetivo real de estas dos semanas": {
        "en": "The real goal of these two weeks",
        "fr": "Le véritable objectif de ces deux semaines"},
    "Que los ocho patrones te salgan de forma automática y sin dolor. No busques agujetas ni "
    "récords: busca que la sentadilla número 15 se vea igual de bien que la número 1.": {
        "en": "That the eight patterns come out automatically and pain-free. Do not chase "
              "soreness or records: aim for squat number 15 to look exactly as good as "
              "number 1.",
        "fr": "Que les huit schémas sortent automatiquement et sans douleur. Ne cherchez ni "
              "courbatures ni records : cherchez à ce que le quinzième squat soit aussi "
              "propre que le premier."},

    # ── Fase 2 ─────────────────────────────────────────────────────────────
    "Fase 2 · Semanas 3–4": {"en": "Phase 2 · Weeks 3–4", "fr": "Phase 2 · Semaines 3–4"},

    'FASE 2 · <span class="a">DESARROLLO</span>': {
        "en": 'PHASE 2 · <span class="a">DEVELOPMENT</span>',
        "fr": 'PHASE 2 · <span class="a">DÉVELOPPEMENT</span>'},

    "Cambias a rutina Push / Pull / Legs de cuatro días. Sube los pesos entre un "
    "5 y un 10 % respecto a la fase 1. El RIR objetivo es 2–3: <strong>debe costar, pero no "
    "llegas al fallo</strong>.": {
        "en": "You switch to a four-day Push / Pull / Legs split. Raise the weights by "
              "5 to 10 % over phase 1. The target RIR is 2–3: <strong>it should be hard, but "
              "you do not reach failure</strong>.",
        "fr": "Vous passez à une routine Push / Pull / Legs sur quatre jours. Montez les "
              "charges de 5 à 10 % par rapport à la phase 1. Le RIR visé est 2–3 : "
              "<strong>cela doit être dur, mais sans aller à l'échec</strong>."},

    "Grupos": {"en": "Groups", "fr": "Groupes"},
    "Lunes · PUSH": {"en": "Monday · PUSH", "fr": "Lundi · PUSH"},
    "Pecho, hombro, tríceps": {
        "en": "Chest, shoulders, triceps", "fr": "Pectoraux, épaules, triceps"},
    "Press banca · Press inclinado · Aperturas · Press militar · Extensión de tríceps · Fondos": {
        "en": "Bench press · Incline press · Flyes · Overhead press · Triceps extension · Dips",
        "fr": "Développé couché · Développé incliné · Écartés · Développé militaire · "
              "Extension triceps · Dips"},
    "Martes · PULL": {"en": "Tuesday · PULL", "fr": "Mardi · PULL"},
    "Espalda, bíceps": {"en": "Back, biceps", "fr": "Dos, biceps"},
    "Dominadas · Remo con barra · Jalón al pecho · Face pull · Curl con barra · Curl martillo": {
        "en": "Pull-ups · Barbell row · Lat pulldown · Face pull · Barbell curl · Hammer curl",
        "fr": "Tractions · Rowing à la barre · Tirage vertical · Face pull · Curl à la "
              "barre · Curl marteau"},
    "Jueves · LEGS": {"en": "Thursday · LEGS", "fr": "Jeudi · LEGS"},
    "Piernas, glúteo": {"en": "Legs, glutes", "fr": "Jambes, fessiers"},
    "Sentadilla · Prensa · Peso muerto rumano · Hip thrust · Extensiones · Curl femoral": {
        "en": "Squat · Leg press · Romanian deadlift · Hip thrust · Leg extensions · Leg curl",
        "fr": "Squat · Presse · Soulevé de terre roumain · Hip thrust · Leg extension · "
              "Leg curl"},
    "Viernes · FULL": {"en": "Friday · FULL", "fr": "Vendredi · FULL"},
    "Cuerpo completo (pesado)": {"en": "Full body (heavy)", "fr": "Corps entier (lourd)"},
    "Sentadilla pesada · Press banca pesado · Peso muerto · Press militar": {
        "en": "Heavy squat · Heavy bench press · Deadlift · Overhead press",
        "fr": "Squat lourd · Développé couché lourd · Soulevé de terre · Développé militaire"},

    "Esquema de series y repeticiones": {
        "en": "Set and rep scheme", "fr": "Schéma de séries et de répétitions"},
    "Tipo de ejercicio": {"en": "Type of exercise", "fr": "Type d'exercice"},
    "Compuesto principal": {"en": "Main compound", "fr": "Polyarticulaire principal"},
    "Compuesto secundario": {"en": "Secondary compound", "fr": "Polyarticulaire secondaire"},
    "Aislamiento": {"en": "Isolation", "fr": "Isolation"},

    "Progresión semana a semana": {
        "en": "Week-by-week progression", "fr": "Progression semaine après semaine"},
    "Situación al terminar la serie": {
        "en": "Where you are at the end of the set",
        "fr": "Votre situation à la fin de la série"},
    "Qué haces la próxima sesión": {
        "en": "What you do next session", "fr": "Ce que vous faites à la séance suivante"},
    "Has alcanzado el tope de repeticiones con RIR 2 o más": {
        "en": "You hit the top of the rep range at RIR 2 or more",
        "fr": "Vous atteignez le haut de la fourchette à RIR 2 ou plus"},
    "Sube un 2,5–5 % el peso y vuelve al extremo bajo del rango": {
        "en": "Add 2.5–5 % to the weight and go back to the bottom of the range",
        "fr": "Montez la charge de 2,5 à 5 % et revenez au bas de la fourchette"},
    "Estás dentro del rango con RIR 1–2": {
        "en": "You are inside the range at RIR 1–2",
        "fr": "Vous êtes dans la fourchette à RIR 1–2"},
    "Repite el mismo peso y busca una repetición más": {
        "en": "Repeat the same weight and chase one more rep",
        "fr": "Répétez la même charge et cherchez une répétition de plus"},
    "No llegas al mínimo del rango": {
        "en": "You cannot reach the bottom of the range",
        "fr": "Vous n'atteignez pas le bas de la fourchette"},
    "Baja un 5 % el peso: te has pasado en la subida anterior": {
        "en": "Drop the weight by 5 %: you overshot on the last increase",
        "fr": "Baissez la charge de 5 % : vous avez trop augmenté la fois précédente"},
    "Dos sesiones seguidas sin progresar": {
        "en": "Two sessions in a row without progress",
        "fr": "Deux séances de suite sans progression"},
    "Revisa sueño, calorías y proteína antes de tocar el programa": {
        "en": "Check sleep, calories and protein before you touch the programme",
        "fr": "Vérifiez sommeil, calories et protéines avant de toucher au programme"},

    "El viernes es el día que más se descuida": {
        "en": "Friday is the most neglected day",
        "fr": "Le vendredi est le jour le plus négligé"},
    "La sesión full body pesada del viernes es la que consolida la fuerza de los patrones "
    "principales. Llega descansado a ella: si el jueves de piernas te deja destrozado, "
    "significa que estás yendo al fallo cuando no debes.": {
        "en": "Friday's heavy full-body session is the one that consolidates strength in the "
              "main patterns. Arrive at it fresh: if Thursday's leg day wrecks you, it means "
              "you are going to failure when you should not be.",
        "fr": "La séance full body lourde du vendredi est celle qui consolide la force sur "
              "les schémas principaux. Arrivez-y reposé : si le jeudi jambes vous détruit, "
              "c'est que vous allez à l'échec alors que vous ne devriez pas."},

    # ── Fase 3 ─────────────────────────────────────────────────────────────
    "Fase 3 · Semanas 5–6": {"en": "Phase 3 · Weeks 5–6", "fr": "Phase 3 · Semaines 5–6"},

    'FASE 3 · <span class="a">INTENSIFICACIÓN</span>': {
        "en": 'PHASE 3 · <span class="a">INTENSIFICATION</span>',
        "fr": 'PHASE 3 · <span class="a">INTENSIFICATION</span>'},

    "Cinco días con estructura Torso / Pierna y trabajo diferenciado de fuerza e "
    "hipertrofia. Es la fase donde aparecen los primeros récords personales. "
    "<strong>RIR 1–2</strong>, y solo la última serie de los aislamientos llega al fallo.": {
        "en": "Five days on an Upper / Lower structure, with strength and hypertrophy work "
              "kept separate. This is the phase where the first personal records appear. "
              "<strong>RIR 1–2</strong>, and only the last set of the isolation work goes to "
              "failure.",
        "fr": "Cinq jours en structure Haut / Bas, avec un travail de force et un travail "
              "d'hypertrophie distincts. C'est la phase où apparaissent les premiers records "
              "personnels. <strong>RIR 1–2</strong>, et seule la dernière série des exercices "
              "d'isolation va à l'échec."},

    "Bloque principal": {"en": "Main block", "fr": "Bloc principal"},
    "Bloque accesorio": {"en": "Accessory block", "fr": "Bloc accessoire"},

    'Lunes<br><span class="muted small">Torso fuerza</span>': {
        "en": 'Monday<br><span class="muted small">Upper, strength</span>',
        "fr": 'Lundi<br><span class="muted small">Haut, force</span>'},
    "Press banca 5×5 · Remo con barra 5×5": {
        "en": "Bench press 5×5 · Barbell row 5×5",
        "fr": "Développé couché 5×5 · Rowing à la barre 5×5"},
    "Press militar 3×8 · Dominadas lastradas 3×6 · Face pull 3×15": {
        "en": "Overhead press 3×8 · Weighted pull-ups 3×6 · Face pull 3×15",
        "fr": "Développé militaire 3×8 · Tractions lestées 3×6 · Face pull 3×15"},

    'Martes<br><span class="muted small">Pierna fuerza</span>': {
        "en": 'Tuesday<br><span class="muted small">Lower, strength</span>',
        "fr": 'Mardi<br><span class="muted small">Bas, force</span>'},
    "Sentadilla 5×5 · Peso muerto 4×4": {
        "en": "Squat 5×5 · Deadlift 4×4", "fr": "Squat 5×5 · Soulevé de terre 4×4"},
    "Prensa 3×10 · Curl femoral 3×12 · Gemelo 4×15": {
        "en": "Leg press 3×10 · Leg curl 3×12 · Calf raise 4×15",
        "fr": "Presse 3×10 · Leg curl 3×12 · Mollets 4×15"},

    "Descanso activo: 30 min de caminata y movilidad": {
        "en": "Active rest: 30 min of walking and mobility",
        "fr": "Repos actif : 30 min de marche et de mobilité"},

    'Jueves<br><span class="muted small">Torso hipertrofia</span>': {
        "en": 'Thursday<br><span class="muted small">Upper, hypertrophy</span>',
        "fr": 'Jeudi<br><span class="muted small">Haut, hypertrophie</span>'},
    "Press inclinado 4×10 · Jalón al pecho 4×10": {
        "en": "Incline press 4×10 · Lat pulldown 4×10",
        "fr": "Développé incliné 4×10 · Tirage vertical 4×10"},
    "Aperturas 3×12 · Elevaciones laterales 4×15 · Curl 3×12 · Tríceps polea 3×12": {
        "en": "Flyes 3×12 · Lateral raises 4×15 · Curl 3×12 · Cable triceps 3×12",
        "fr": "Écartés 3×12 · Élévations latérales 4×15 · Curl 3×12 · Triceps poulie 3×12"},

    'Viernes<br><span class="muted small">Pierna hipertrofia</span>': {
        "en": 'Friday<br><span class="muted small">Lower, hypertrophy</span>',
        "fr": 'Vendredi<br><span class="muted small">Bas, hypertrophie</span>'},
    "Sentadilla búlgara 4×10 · Hip thrust 4×10": {
        "en": "Bulgarian split squat 4×10 · Hip thrust 4×10",
        "fr": "Squat bulgare 4×10 · Hip thrust 4×10"},
    "Extensiones 3×15 · Peso muerto rumano 3×12 · Gemelo 4×20": {
        "en": "Leg extensions 3×15 · Romanian deadlift 3×12 · Calf raise 4×20",
        "fr": "Leg extension 3×15 · Soulevé de terre roumain 3×12 · Mollets 4×20"},

    'Sábado<br><span class="muted small">Puntos débiles</span>': {
        "en": 'Saturday<br><span class="muted small">Weak points</span>',
        "fr": 'Samedi<br><span class="muted small">Points faibles</span>'},
    "Elige los dos grupos que peor responden y añade 6–8 series de aislamiento": {
        "en": "Pick the two groups that respond worst and add 6–8 isolation sets",
        "fr": "Choisissez les deux groupes qui répondent le moins bien et ajoutez 6 à "
              "8 séries d'isolation"},

    "Técnicas de intensidad · una por sesión, nunca más": {
        "en": "Intensity techniques · one per session, never more",
        "fr": "Techniques d'intensité · une par séance, jamais plus"},
    "Cómo se ejecuta": {"en": "How it is done", "fr": "Comment l'exécuter"},
    "Dónde aplicarla": {"en": "Where to use it", "fr": "Où l'appliquer"},
    "Serie descendente": {"en": "Drop set", "fr": "Série dégressive"},
    "Al fallo, baja el peso un 20 % y continúa sin descanso": {
        "en": "At failure, cut the weight by 20 % and carry on with no rest",
        "fr": "À l'échec, baissez la charge de 20 % et continuez sans repos"},
    "Última serie de un aislamiento": {
        "en": "The last set of an isolation exercise",
        "fr": "La dernière série d'un exercice d'isolation"},
    "Rest-pause": {"en": "Rest-pause", "fr": "Rest-pause"},
    "Al fallo, descansa 15 s y saca 3–5 repeticiones más": {
        "en": "At failure, rest 15 s and squeeze out 3–5 more reps",
        "fr": "À l'échec, reposez 15 s et sortez 3 à 5 répétitions de plus"},
    "Máquinas o poleas, nunca con barra libre": {
        "en": "Machines or cables, never with a free barbell",
        "fr": "Machines ou poulies, jamais à la barre libre"},
    "Repeticiones parciales": {"en": "Partial reps", "fr": "Répétitions partielles"},
    "Al fallo, sigue en el rango donde eres más fuerte": {
        "en": "At failure, keep going in the range where you are strongest",
        "fr": "À l'échec, continuez dans l'amplitude où vous êtes le plus fort"},
    "Elevaciones laterales y curl": {
        "en": "Lateral raises and curls", "fr": "Élévations latérales et curl"},
    "Series mecánicas": {"en": "Mechanical drop sets", "fr": "Séries mécaniques"},
    "Al fallo, cambia a una variante más fácil del mismo patrón": {
        "en": "At failure, switch to an easier variant of the same pattern",
        "fr": "À l'échec, passez à une variante plus facile du même schéma"},
    "Flexiones, dominadas, press": {
        "en": "Push-ups, pull-ups, presses", "fr": "Pompes, tractions, développés"},

    "Esta fase es la que más gente rompe": {
        "en": "This is the phase that breaks the most people",
        "fr": "C'est la phase qui casse le plus de monde"},
    "Veintidós series por grupo con un 85 % del 1RM solo funciona si comes en superávit o "
    "mantenimiento y duermes 8 horas. Si estás en déficit calórico agresivo, quédate en el "
    "volumen de la fase 2: no ganarás nada añadiendo series que no puedes recuperar.": {
        "en": "Twenty-two sets per group at 85 % of 1RM only works if you eat at surplus or "
              "maintenance and sleep 8 hours. If you are in an aggressive calorie deficit, "
              "stay on phase 2 volume: you gain nothing by adding sets you cannot recover "
              "from.",
        "fr": "Vingt-deux séries par groupe à 85 % du 1RM ne fonctionnent que si vous mangez "
              "en surplus ou à l'entretien et dormez 8 heures. Si vous êtes en déficit "
              "calorique agressif, restez au volume de la phase 2 : vous ne gagnerez rien à "
              "ajouter des séries que vous ne pouvez pas récupérer."},

    # ── Fase 4 ─────────────────────────────────────────────────────────────
    "Fase 4 · Semanas 7–8": {"en": "Phase 4 · Weeks 7–8", "fr": "Phase 4 · Semaines 7–8"},

    'FASE 4 · <span class="a">QUEMA</span>': {
        "en": 'PHASE 4 · <span class="a">BURN</span>',
        "fr": 'PHASE 4 · <span class="a">SÈCHE</span>'},

    "Cuatro sesiones de pesas más tres de HIIT. El volumen baja ligeramente y "
    "aparecen superseries y circuitos para aumentar la densidad del entrenamiento. "
    "<strong>Las cargas principales no bajan</strong>: es lo que preserva el músculo en déficit.": {
        "en": "Four weights sessions plus three of HIIT. Volume comes down slightly and "
              "supersets and circuits appear, to raise the density of the training. "
              "<strong>The main loads do not drop</strong>: that is what preserves muscle in "
              "a deficit.",
        "fr": "Quatre séances de musculation plus trois de HIIT. Le volume baisse légèrement "
              "et des supersets et des circuits apparaissent pour augmenter la densité de "
              "l'entraînement. <strong>Les charges principales ne baissent pas</strong> : "
              "c'est ce qui préserve le muscle en déficit."},

    "Formato": {"en": "Format", "fr": "Format"},
    "Lunes · Torso": {"en": "Monday · Upper", "fr": "Lundi · Haut du corps"},
    "Press banca 4×6 · Remo 4×6 · Superserie: press militar + jalón 3×10 · Superserie: curl + tríceps 3×12": {
        "en": "Bench press 4×6 · Row 4×6 · Superset: overhead press + pulldown 3×10 · "
              "Superset: curl + triceps 3×12",
        "fr": "Développé couché 4×6 · Rowing 4×6 · Superset : développé militaire + tirage "
              "3×10 · Superset : curl + triceps 3×12"},
    "Fuerza + superseries": {"en": "Strength + supersets", "fr": "Force + supersets"},
    "Martes · HIIT": {"en": "Tuesday · HIIT", "fr": "Mardi · HIIT"},
    "Intervalos 40 s al máximo / 20 s caminando, 24 min en total": {
        "en": "Intervals of 40 s all-out / 20 s walking, 24 min in total",
        "fr": "Intervalles de 40 s au maximum / 20 s de marche, 24 min au total"},
    "Intervalos": {"en": "Intervals", "fr": "Intervalles"},
    "Miércoles · Pierna": {"en": "Wednesday · Lower", "fr": "Mercredi · Bas du corps"},
    "Sentadilla 4×6 · Peso muerto rumano 4×8 · Superserie: prensa + curl femoral 3×12 · Gemelo 4×20": {
        "en": "Squat 4×6 · Romanian deadlift 4×8 · Superset: leg press + leg curl 3×12 · "
              "Calf raise 4×20",
        "fr": "Squat 4×6 · Soulevé de terre roumain 4×8 · Superset : presse + leg curl "
              "3×12 · Mollets 4×20"},
    "Jueves · HIIT": {"en": "Thursday · HIIT", "fr": "Jeudi · HIIT"},
    "Circuito de core, 30 s de trabajo / 10 s de descanso, 6 vueltas (18 min)": {
        "en": "Core circuit, 30 s of work / 10 s of rest, 6 circuits (18 min)",
        "fr": "Circuit de gainage, 30 s de travail / 10 s de repos, 6 tours (18 min)"},
    "Viernes · Torso": {"en": "Friday · Upper", "fr": "Vendredi · Haut du corps"},
    "Press inclinado 4×10 · Dominadas 4×máx · Circuito de hombro y brazo 3 vueltas": {
        "en": "Incline press 4×10 · Pull-ups 4×max · Shoulder and arm circuit, 3 rounds",
        "fr": "Développé incliné 4×10 · Tractions 4×max · Circuit épaules et bras, 3 tours"},
    "Hipertrofia + circuito": {"en": "Hypertrophy + circuit", "fr": "Hypertrophie + circuit"},
    "Sábado · Pierna": {"en": "Saturday · Lower", "fr": "Samedi · Bas du corps"},
    "Hip thrust 4×10 · Zancadas 3×12 · Extensiones 3×15 · Circuito de core 3 vueltas": {
        "en": "Hip thrust 4×10 · Lunges 3×12 · Leg extensions 3×15 · Core circuit, 3 rounds",
        "fr": "Hip thrust 4×10 · Fentes 3×12 · Leg extension 3×15 · Circuit de gainage, "
              "3 tours"},
    "Domingo · HIIT": {"en": "Sunday · HIIT", "fr": "Dimanche · HIIT"},
    "Circuito de cuerpo completo, 30 s / 15 s, 5 vueltas (25 min), o descanso completo": {
        "en": "Full-body circuit, 30 s / 15 s, 5 rounds (25 min), or complete rest",
        "fr": "Circuit corps entier, 30 s / 15 s, 5 tours (25 min), ou repos complet"},
    "Opcional": {"en": "Optional", "fr": "Optionnel"},

    "Cómo se ejecutan superseries y circuitos": {
        "en": "How supersets and circuits are run",
        "fr": "Comment exécuter supersets et circuits"},
    "Ejecución": {"en": "Execution", "fr": "Exécution"},
    "Ventaja": {"en": "Advantage", "fr": "Avantage"},
    "Superserie antagonista": {"en": "Antagonist superset", "fr": "Superset antagoniste"},
    "Dos ejercicios de grupos opuestos, sin descanso entre ellos": {
        "en": "Two exercises for opposing groups, with no rest between them",
        "fr": "Deux exercices de groupes opposés, sans repos entre eux"},
    "90 s tras el par": {"en": "90 s after the pair", "fr": "90 s après la paire"},
    "Ahorra tiempo sin perder rendimiento": {
        "en": "Saves time without losing performance",
        "fr": "Fait gagner du temps sans perte de performance"},
    "Circuito": {"en": "Circuit", "fr": "Circuit"},
    "3–4 ejercicios seguidos, 12–15 repeticiones cada uno": {
        "en": "3–4 exercises back to back, 12–15 reps each",
        "fr": "3 à 4 exercices à la suite, 12 à 15 répétitions chacun"},
    "2 min entre vueltas": {"en": "2 min between rounds", "fr": "2 min entre les tours"},
    "Alta densidad y gasto calórico": {
        "en": "High density and calorie burn", "fr": "Haute densité et dépense calorique"},
    "Serie compuesta": {"en": "Compound set", "fr": "Série composée"},
    "Dos ejercicios del mismo grupo, seguidos": {
        "en": "Two exercises for the same group, back to back",
        "fr": "Deux exercices du même groupe, à la suite"},
    "Máxima fatiga local, úsala solo en aislamientos": {
        "en": "Maximum local fatigue — use it on isolation work only",
        "fr": "Fatigue locale maximale — à réserver aux exercices d'isolation"},

    "Reglas de la fase de definición": {
        "en": "Rules for the cutting phase", "fr": "Règles de la phase de sèche"},
    "<strong>Nunca bajes el peso para hacer más repeticiones.</strong> El músculo se "
    "conserva con la carga, no con la sensación de quemazón.": {
        "en": "<strong>Never drop the weight in order to do more reps.</strong> Muscle is "
              "preserved by load, not by the burning sensation.",
        "fr": "<strong>Ne baissez jamais la charge pour faire plus de répétitions.</strong> "
              "Le muscle se conserve par la charge, pas par la sensation de brûlure."},
    "No hagas HIIT el día antes de pierna ni el día después.": {
        "en": "Do not do HIIT the day before leg day, nor the day after.",
        "fr": "Ne faites pas de HIIT la veille du jour des jambes, ni le lendemain."},
    "Si pierdes más de un 10 % en tu press banca, tienes un problema de recuperación: "
    "sube calorías o quita una sesión de HIIT.": {
        "en": "If you lose more than 10 % on your bench press, you have a recovery problem: "
              "raise calories or drop one HIIT session.",
        "fr": "Si vous perdez plus de 10 % au développé couché, vous avez un problème de "
              "récupération : augmentez les calories ou retirez une séance de HIIT."},
    "La semana 8 termina con una descarga: reduce el volumen un 40 % y mantén la carga.": {
        "en": "Week 8 ends with a deload: cut the volume by 40 % and keep the load.",
        "fr": "La semaine 8 se termine par une décharge : réduisez le volume de 40 % et "
              "gardez la charge."},

    "Al terminar las 8 semanas": {
        "en": "When the 8 weeks are over", "fr": "À la fin des 8 semaines"},
    "Tómate una semana de descarga completa y vuelve a empezar desde la fase 2 con las "
    "cargas nuevas. El ciclo funciona indefinidamente: cada vuelta parte de un nivel superior.": {
        "en": "Take a full week of deload and start again from phase 2 with your new loads. "
              "The cycle works indefinitely: each pass starts from a higher level.",
        "fr": "Prenez une semaine de décharge complète et recommencez à la phase 2 avec vos "
              "nouvelles charges. Le cycle fonctionne indéfiniment : chaque tour repart d'un "
              "niveau supérieur."},

    # ── Mapa muscular ──────────────────────────────────────────────────────
    "Mapa muscular": {"en": "Muscle map", "fr": "Carte musculaire"},
    'MAPA MUSCULAR DE <span class="a">REFERENCIA</span>': {
        "en": 'REFERENCE <span class="a">MUSCLE MAP</span>',
        "fr": 'CARTE MUSCULAIRE DE <span class="a">RÉFÉRENCE</span>'},

    "Estos son los dieciséis grupos que cubre el plan. Antes de cerrar tu semana, "
    "comprueba que <strong>ninguno se queda sin estímulo</strong>: es el error de programación "
    "más frecuente y el que produce los desequilibrios que después cuesta años corregir.": {
        "en": "These are the sixteen groups the plan covers. Before you close your week, "
              "check that <strong>none of them is left without a stimulus</strong>: it is the "
              "most common programming mistake, and the one that produces the imbalances that "
              "later take years to correct.",
        "fr": "Voici les seize groupes couverts par le plan. Avant de boucler votre semaine, "
              "vérifiez qu'<strong>aucun ne reste sans stimulus</strong> : c'est l'erreur de "
              "programmation la plus fréquente, et celle qui crée les déséquilibres qu'il "
              "faut ensuite des années à corriger."},

    "<b>Fig. 1</b>Los dieciséis grupos del plan": {
        "en": "<b>Fig. 1</b>The sixteen groups in the plan",
        "fr": "<b>Fig. 1</b>Les seize groupes du plan"},
    "Vista anterior y posterior con la numeración que se usa en las "
    "tablas de las páginas siguientes.": {
        "en": "Front and back views, with the numbering used in the tables on the following "
              "pages.",
        "fr": "Vues antérieure et postérieure, avec la numérotation utilisée dans les "
              "tableaux des pages suivantes."},

    "Cobertura semanal mínima": {
        "en": "Minimum weekly coverage", "fr": "Couverture hebdomadaire minimale"},
    "Grupo": {"en": "Group", "fr": "Groupe"},
    "Series/semana": {"en": "Sets/week", "fr": "Séries/semaine"},
    "Ejercicios del plan que lo cubren": {
        "en": "Exercises in the plan that cover it",
        "fr": "Exercices du plan qui le couvrent"},
    "Pecho (03)": {"en": "Chest (03)", "fr": "Pectoraux (03)"},
    "Press banca, press inclinado, aperturas, fondos": {
        "en": "Bench press, incline press, flyes, dips",
        "fr": "Développé couché, développé incliné, écartés, dips"},
    "Espalda (10, 11)": {"en": "Back (10, 11)", "fr": "Dos (10, 11)"},
    "Dominadas, remo con barra, jalón, remo en polea": {
        "en": "Pull-ups, barbell row, pulldown, cable row",
        "fr": "Tractions, rowing à la barre, tirage vertical, rowing à la poulie"},
    "Piernas (08, 15, 16)": {"en": "Legs (08, 15, 16)", "fr": "Jambes (08, 15, 16)"},
    "Sentadilla, peso muerto rumano, prensa, curl femoral": {
        "en": "Squat, Romanian deadlift, leg press, leg curl",
        "fr": "Squat, soulevé de terre roumain, presse, leg curl"},
    "Glúteo (14)": {"en": "Glutes (14)", "fr": "Fessiers (14)"},
    "Hip thrust, sentadilla búlgara, zancadas": {
        "en": "Hip thrust, Bulgarian split squat, lunges",
        "fr": "Hip thrust, squat bulgare, fentes"},
    "Hombro (02)": {"en": "Shoulders (02)", "fr": "Épaules (02)"},
    "Press militar, elevaciones laterales, face pull": {
        "en": "Overhead press, lateral raises, face pull",
        "fr": "Développé militaire, élévations latérales, face pull"},
    "Brazo (04, 13)": {"en": "Arms (04, 13)", "fr": "Bras (04, 13)"},
    "Curl, curl martillo, extensión de tríceps, fondos": {
        "en": "Curl, hammer curl, triceps extension, dips",
        "fr": "Curl, curl marteau, extension triceps, dips"},
    "Core (06, 07, 12)": {"en": "Core (06, 07, 12)", "fr": "Gainage (06, 07, 12)"},
    "Plancha, crunch en polea, peso muerto (indirecto)": {
        "en": "Plank, cable crunch, deadlift (indirect)",
        "fr": "Gainage, crunch à la poulie, soulevé de terre (indirect)"},

    "Los grupos que casi todo el mundo descuida": {
        "en": "The groups almost everyone neglects",
        "fr": "Les groupes que presque tout le monde néglige"},
    "El <strong>deltoides posterior (02)</strong>, los <strong>isquiotibiales (15)</strong> y "
    "el <strong>gemelo (16)</strong>. Los tres se entrenan en el plan, pero son los primeros "
    "que la gente se salta cuando va con prisa — y los tres son los que más equilibran una "
    "figura y protegen la articulación.": {
        "en": "The <strong>rear deltoid (02)</strong>, the <strong>hamstrings (15)</strong> "
              "and the <strong>calves (16)</strong>. All three are trained in the plan, but "
              "they are the first thing people skip when they are in a hurry — and all three "
              "do the most to balance a physique and protect the joint.",
        "fr": "Le <strong>deltoïde postérieur (02)</strong>, les <strong>ischio-jambiers "
              "(15)</strong> et les <strong>mollets (16)</strong>. Les trois sont travaillés "
              "dans le plan, mais ce sont les premiers que l'on saute quand on est pressé — "
              "et ce sont les trois qui équilibrent le plus une silhouette et protègent "
              "l'articulation."},

    # ── Ejercicios 1–15 ────────────────────────────────────────────────────
    "Ejercicios 1–15": {"en": "Exercises 1–15", "fr": "Exercices 1–15"},
    'LOS 30 EJERCICIOS · <span class="a">PARTE 1</span>': {
        "en": 'THE 30 EXERCISES · <span class="a">PART 1</span>',
        "fr": 'LES 30 EXERCICES · <span class="a">PARTIE 1</span>'},
    "Grupo muscular": {"en": "Muscle group", "fr": "Groupe musculaire"},
    "Error común": {"en": "Common mistake", "fr": "Erreur courante"},
    "Consejo clave": {"en": "Key tip", "fr": "Conseil clé"},

    "Rodillas hacia dentro": {"en": "Knees caving inwards", "fr": "Genoux rentrés"},
    "Empuja el suelo con el pie completo": {
        "en": "Push the floor away with the whole foot",
        "fr": "Poussez le sol avec tout le pied"},
    "Press banca": {"en": "Bench press", "fr": "Développé couché"},
    "Codos muy abiertos a 90°": {
        "en": "Elbows flared right out to 90°", "fr": "Coudes trop ouverts à 90°"},
    "Escápulas fijas contra el banco": {
        "en": "Scapulae locked against the bench",
        "fr": "Omoplates fixées contre le banc"},
    "Peso muerto convencional": {
        "en": "Conventional deadlift", "fr": "Soulevé de terre conventionnel"},
    "Espalda, piernas": {"en": "Back, legs", "fr": "Dos, jambes"},
    "Redondear la zona lumbar": {
        "en": "Rounding the lower back", "fr": "Arrondir le bas du dos"},
    "Barra pegada a la pierna todo el recorrido": {
        "en": "Bar against the leg through the whole lift",
        "fr": "Barre au contact de la jambe sur tout le trajet"},
    "Dominadas": {"en": "Pull-ups", "fr": "Tractions"},
    "Balanceo con el cuerpo": {"en": "Swinging the body", "fr": "Balancier du corps"},
    "Piensa en llevar los codos al bolsillo": {
        "en": "Think about driving the elbows to your back pocket",
        "fr": "Pensez à amener les coudes vers la poche arrière"},
    "Dorsal medio": {"en": "Mid-back", "fr": "Dos moyen"},
    "Torso demasiado vertical": {"en": "Torso too upright", "fr": "Buste trop vertical"},
    "Mantén 45° y no uses impulso lumbar": {
        "en": "Hold 45° and do not drive with the lower back",
        "fr": "Tenez 45° et n'utilisez pas d'élan lombaire"},
    "Arquear en exceso la lumbar": {
        "en": "Over-arching the lower back", "fr": "Cambrer excessivement le bas du dos"},
    "Aprieta glúteo y abdomen antes de empujar": {
        "en": "Squeeze glutes and abs before you press",
        "fr": "Serrez fessiers et abdominaux avant de pousser"},
    "Hip thrust": {"en": "Hip thrust", "fr": "Hip thrust"},
    "Glúteo": {"en": "Glutes", "fr": "Fessiers"},
    "No llegar a extensión completa": {
        "en": "Not reaching full extension", "fr": "Ne pas atteindre l'extension complète"},
    "Pausa de 1 s arriba con la pelvis retrovertida": {
        "en": "1 s pause at the top with the pelvis tucked",
        "fr": "Pause d'1 s en haut, bassin en rétroversion"},
    "Prensa de piernas": {"en": "Leg press", "fr": "Presse à cuisses"},
    "Rodillas cayendo hacia dentro": {
        "en": "Knees collapsing inwards", "fr": "Genoux qui rentrent vers l'intérieur"},
    "No despegues la zona lumbar del respaldo": {
        "en": "Do not let your lower back come off the pad",
        "fr": "Ne décollez pas le bas du dos du dossier"},
    "Fondos en paralelas": {"en": "Parallel-bar dips", "fr": "Dips aux barres parallèles"},
    "Tríceps, pecho": {"en": "Triceps, chest", "fr": "Triceps, pectoraux"},
    "Inclinar demasiado el torso": {
        "en": "Leaning the torso too far forward", "fr": "Trop incliner le buste"},
    "Vertical para tríceps, inclinado para pecho": {
        "en": "Upright for triceps, leaning for chest",
        "fr": "Vertical pour les triceps, incliné pour les pectoraux"},
    "Curl con barra": {"en": "Barbell curl", "fr": "Curl à la barre"},
    "Mover el codo hacia delante": {
        "en": "Letting the elbow drift forward", "fr": "Avancer le coude"},
    "Codos pegados al costado, sin balanceo": {
        "en": "Elbows pinned to your sides, no swinging",
        "fr": "Coudes collés au corps, sans balancier"},
    "Press inclinado": {"en": "Incline press", "fr": "Développé incliné"},
    "Pectoral superior": {"en": "Upper chest", "fr": "Haut des pectoraux"},
    "Bajar demasiado la barra": {
        "en": "Bringing the bar down too low", "fr": "Descendre la barre trop bas"},
    "Inclinación de 30°, más no aporta": {
        "en": "30° of incline; more adds nothing",
        "fr": "30° d'inclinaison ; au-delà, cela n'apporte rien"},
    "Remo en polea": {"en": "Cable row", "fr": "Rowing à la poulie"},
    "Dorsal": {"en": "Lats", "fr": "Grand dorsal"},
    "Tirar con la espalda baja": {
        "en": "Pulling with the lower back", "fr": "Tirer avec le bas du dos"},
    "Pecho alto y torso quieto": {
        "en": "Chest up and torso still", "fr": "Poitrine haute et buste immobile"},
    "Elevaciones laterales": {"en": "Lateral raises", "fr": "Élévations latérales"},
    "Deltoides lateral": {"en": "Lateral deltoid", "fr": "Deltoïde latéral"},
    "Encoger los hombros al subir": {
        "en": "Shrugging the shoulders on the way up",
        "fr": "Hausser les épaules en montant"},
    "Sube solo hasta la altura del hombro": {
        "en": "Raise only to shoulder height", "fr": "Ne montez qu'à hauteur d'épaule"},
    "Extensión de tríceps en polea": {
        "en": "Cable triceps extension", "fr": "Extension triceps à la poulie"},
    "Separar los codos del costado": {
        "en": "Letting the elbows drift away from your sides",
        "fr": "Écarter les coudes du corps"},
    "Solo se mueve el antebrazo": {
        "en": "Only the forearm moves", "fr": "Seul l'avant-bras bouge"},
    "Curl en polea": {"en": "Cable curl", "fr": "Curl à la poulie"},
    "Balanceo del torso": {"en": "Swinging the torso", "fr": "Balancier du buste"},
    "Apóyate en la pared si no puedes evitarlo": {
        "en": "Lean against a wall if you cannot avoid it",
        "fr": "Appuyez-vous au mur si vous n'y arrivez pas autrement"},

    '<span class="tag lo">B</span> Básico · <span class="tag mid">I</span> Intermedio · '
    '<span class="tag hi">A</span> Avanzado': {
        "en": '<span class="tag lo">B</span> Basic · <span class="tag mid">I</span> '
              'Intermediate · <span class="tag hi">A</span> Advanced',
        "fr": '<span class="tag lo">B</span> Basique · <span class="tag mid">I</span> '
              'Intermédiaire · <span class="tag hi">A</span> Avancé'},

    # ── Ejercicios 16–30 ───────────────────────────────────────────────────
    "Ejercicios 16–30": {"en": "Exercises 16–30", "fr": "Exercices 16–30"},
    'LOS 30 EJERCICIOS · <span class="a">PARTE 2</span>': {
        "en": 'THE 30 EXERCISES · <span class="a">PART 2</span>',
        "fr": 'LES 30 EXERCICES · <span class="a">PARTIE 2</span>'},

    "Zancadas con mancuerna": {"en": "Dumbbell lunges", "fr": "Fentes avec haltères"},
    "La rodilla delantera cae hacia dentro": {
        "en": "The front knee caves inwards", "fr": "Le genou avant rentre vers l'intérieur"},
    "Paso largo para glúteo, corto para cuádriceps": {
        "en": "Long step for glutes, short step for quads",
        "fr": "Grand pas pour les fessiers, petit pas pour les quadriceps"},
    "Doblar demasiado las rodillas": {
        "en": "Bending the knees too much", "fr": "Trop plier les genoux"},
    "Lleva la cadera atrás, no bajes el torso": {
        "en": "Send the hip back; do not simply lower the torso",
        "fr": "Envoyez les hanches en arrière ; ne descendez pas simplement le buste"},
    "Aperturas en pec deck": {"en": "Pec deck flyes", "fr": "Écartés au pec deck"},
    "Pectoral medial": {"en": "Inner chest", "fr": "Pectoraux internes"},
    "Aplanar el pecho al final": {
        "en": "Letting the chest flatten at the end",
        "fr": "Laisser la poitrine s'affaisser en fin de mouvement"},
    "Mantén el pecho alto y aprieta 1 s": {
        "en": "Keep the chest up and squeeze for 1 s",
        "fr": "Gardez la poitrine haute et contractez 1 s"},
    "Curl femoral tumbado": {"en": "Lying leg curl", "fr": "Leg curl allongé"},
    "Levantar las caderas del banco": {
        "en": "Lifting the hips off the bench", "fr": "Décoller les hanches du banc"},
    "Baja el peso si tienes que despegar la cadera": {
        "en": "Lower the weight if you have to lift the hip",
        "fr": "Baissez la charge si vous devez décoller les hanches"},
    "Press de hombro con mancuerna": {
        "en": "Dumbbell shoulder press", "fr": "Développé épaules aux haltères"},
    "No llegar a la extensión superior": {
        "en": "Not locking out at the top", "fr": "Ne pas aller au bout de l'extension"},
    "Muñecas sobre los codos en todo el recorrido": {
        "en": "Wrists stacked over the elbows throughout",
        "fr": "Poignets à l'aplomb des coudes sur tout le trajet"},
    "Cruce de poleas": {"en": "Cable crossover", "fr": "Écarté à la poulie vis-à-vis"},
    "Extender demasiado los codos": {
        "en": "Straightening the elbows too much", "fr": "Trop tendre les coudes"},
    "Codos ligeramente flexionados y fijos": {
        "en": "Elbows slightly bent and fixed", "fr": "Coudes légèrement fléchis et fixes"},
    "Jalón al pecho": {"en": "Lat pulldown", "fr": "Tirage vertical poitrine"},
    "Echar el torso muy hacia atrás": {
        "en": "Leaning the torso too far back", "fr": "Trop rejeter le buste en arrière"},
    "Inclinación máxima de 20°": {
        "en": "20° of lean at most", "fr": "20° d'inclinaison au maximum"},
    "Extensión de cuádriceps": {"en": "Leg extension", "fr": "Leg extension"},
    "Subir demasiado rápido": {"en": "Lifting too fast", "fr": "Monter trop vite"},
    "2 s de bajada controlada en cada repetición": {
        "en": "2 s of controlled lowering on every rep",
        "fr": "2 s de descente contrôlée à chaque répétition"},
    "Reverse fly": {"en": "Reverse fly", "fr": "Reverse fly (oiseau)"},
    "Deltoides posterior": {"en": "Rear deltoid", "fr": "Deltoïde postérieur"},
    "Mover los codos durante el recorrido": {
        "en": "Moving the elbows during the rep",
        "fr": "Bouger les coudes pendant le mouvement"},
    "Peso ligero: aquí el ego no sirve de nada": {
        "en": "Light weight: ego is worth nothing here",
        "fr": "Charge légère : ici l'ego ne sert à rien"},
    "Curl martillo": {"en": "Hammer curl", "fr": "Curl marteau"},
    "Braquial, bíceps": {"en": "Brachialis, biceps", "fr": "Brachial, biceps"},
    "Supinar la muñeca al subir": {
        "en": "Supinating the wrist on the way up", "fr": "Supiner le poignet en montant"},
    "Agarre neutro estricto de principio a fin": {
        "en": "Strict neutral grip from start to finish",
        "fr": "Prise neutre stricte du début à la fin"},
    "Face pull": {"en": "Face pull", "fr": "Face pull"},
    "Trapecio, hombro posterior": {
        "en": "Traps, rear shoulder", "fr": "Trapèzes, épaule postérieure"},
    "Tirar desde una altura demasiado baja": {
        "en": "Pulling from too low a height", "fr": "Tirer depuis une hauteur trop basse"},
    "Polea a la altura de la cara, codos altos": {
        "en": "Cable at face height, elbows high",
        "fr": "Poulie à hauteur du visage, coudes hauts"},
    "Cadera elevada o hundida": {
        "en": "Hip too high or sagging", "fr": "Hanches trop hautes ou affaissées"},
    "Mejor 30 s perfectos que 2 min mal hechos": {
        "en": "30 perfect seconds beat 2 badly held minutes",
        "fr": "30 s parfaites valent mieux que 2 min mal tenues"},
    "Crunch en polea": {"en": "Cable crunch", "fr": "Crunch à la poulie"},
    "Abdominales": {"en": "Abs", "fr": "Abdominaux"},
    "Tirar del cuello con las manos": {
        "en": "Pulling on your neck with your hands",
        "fr": "Tirer sur la nuque avec les mains"},
    "Flexiona la columna, no la cadera": {
        "en": "Flex the spine, not the hip", "fr": "Fléchissez la colonne, pas la hanche"},
    "Sentadilla búlgara": {"en": "Bulgarian split squat", "fr": "Squat bulgare"},
    "Rodilla delantera muy adelantada": {
        "en": "Front knee too far forward", "fr": "Genou avant trop avancé"},
    "Separa bien el pie del banco y estabiliza primero": {
        "en": "Set the foot well away from the bench and find your balance first",
        "fr": "Éloignez bien le pied du banc et stabilisez-vous d'abord"},
    "Dominadas lastradas": {"en": "Weighted pull-ups", "fr": "Tractions lestées"},
    "Rango de movimiento parcial": {
        "en": "Partial range of motion", "fr": "Amplitude partielle"},
    "Solo añade lastre si haces 10 limpias sin peso": {
        "en": "Only add weight once you can do 10 clean reps unloaded",
        "fr": "N'ajoutez du lest que si vous faites 10 tractions propres sans charge"},

    "Si un ejercicio te duele, sustitúyelo": {
        "en": "If an exercise hurts, replace it",
        "fr": "Si un exercice vous fait mal, remplacez-le"},
    "Cada patrón tiene alternativas: sentadilla → prensa o goblet; press banca → press con "
    "mancuernas; peso muerto → peso muerto rumano con mancuernas. <strong>El dolor articular "
    "no se entrena, se rodea.</strong>": {
        "en": "Every pattern has alternatives: squat → leg press or goblet squat; bench press "
              "→ dumbbell press; deadlift → dumbbell Romanian deadlift. <strong>You do not "
              "train through joint pain, you work around it.</strong>",
        "fr": "Chaque schéma a des alternatives : squat → presse ou goblet squat ; développé "
              "couché → développé aux haltères ; soulevé de terre → soulevé de terre roumain "
              "aux haltères. <strong>La douleur articulaire ne se travaille pas, elle se "
              "contourne.</strong>"},

    # ── Calentamiento y descarga ───────────────────────────────────────────
    "Calentamiento y descarga": {
        "en": "Warm-up and deload", "fr": "Échauffement et décharge"},
    'LO QUE RODEA <span class="a">A LAS SERIES</span>': {
        "en": 'WHAT SURROUNDS <span class="a">THE SETS</span>',
        "fr": 'CE QUI ENTOURE <span class="a">LES SÉRIES</span>'},

    "Calentamiento estándar · 8 minutos": {
        "en": "Standard warm-up · 8 minutes", "fr": "Échauffement standard · 8 minutes"},
    "Cardio suave: bici, remo o cinta": {
        "en": "Easy cardio: bike, rower or treadmill",
        "fr": "Cardio léger : vélo, rameur ou tapis"},
    "Sube temperatura y frecuencia cardiaca": {
        "en": "Raises temperature and heart rate",
        "fr": "Augmente la température et la fréquence cardiaque"},
    "Movilidad de la articulación del día": {
        "en": "Mobility for the joint of the day",
        "fr": "Mobilité de l'articulation du jour"},
    "Cadera y tobillo, u hombro y torácica": {
        "en": "Hip and ankle, or shoulder and thoracic spine",
        "fr": "Hanche et cheville, ou épaule et rachis thoracique"},
    "Aproximación al 40 %, 60 % y 80 %": {
        "en": "Ramp-up sets at 40 %, 60 % and 80 %",
        "fr": "Séries d'approche à 40 %, 60 % et 80 %"},
    "Prepara el sistema nervioso": {
        "en": "Primes the nervous system", "fr": "Prépare le système nerveux"},

    "Escala de RIR": {"en": "The RIR scale", "fr": "Échelle de RIR"},
    "Sensación": {"en": "How it feels", "fr": "Sensation"},
    "Cuándo usarlo": {"en": "When to use it", "fr": "Quand l'utiliser"},
    "Cómodo, técnica impecable": {
        "en": "Comfortable, flawless technique", "fr": "Confortable, technique impeccable"},
    "Aproximación y descargas": {
        "en": "Ramp-up sets and deloads", "fr": "Séries d'approche et décharges"},
    "Exigente pero controlado": {
        "en": "Demanding but controlled", "fr": "Exigeant mais maîtrisé"},
    "Fase 1": {"en": "Phase 1", "fr": "Phase 1"},
    "La barra pierde velocidad": {
        "en": "The bar starts slowing down", "fr": "La barre perd de la vitesse"},
    "Fases 2 y 3": {"en": "Phases 2 and 3", "fr": "Phases 2 et 3"},
    "La última cuesta mucho": {
        "en": "The last rep is a real grind", "fr": "La dernière est très dure"},
    "Compuestos en fase 3": {
        "en": "Compound lifts in phase 3", "fr": "Polyarticulaires en phase 3"},
    "Fallo muscular": {"en": "Muscular failure", "fr": "Échec musculaire"},
    "Solo aislamientos": {"en": "Isolation work only", "fr": "Isolation uniquement"},

    "Cuándo hace falta una descarga": {
        "en": "When a deload is needed", "fr": "Quand une décharge s'impose"},
    "Dos semanas sin progresar en ningún ejercicio principal": {
        "en": "Two weeks without progress on any main lift",
        "fr": "Deux semaines sans progresser sur aucun exercice principal"},
    "Dolor articular persistente al calentar": {
        "en": "Persistent joint pain during the warm-up",
        "fr": "Douleur articulaire persistante à l'échauffement"},
    "Han pasado 6–8 semanas desde la última": {
        "en": "It has been 6–8 weeks since the last one",
        "fr": "Cela fait 6 à 8 semaines depuis la dernière"},

    "<b>Fig. 2</b>Sentadilla: recorrido correcto y los dos errores caros": {
        "en": "<b>Fig. 2</b>The squat: the correct path and the two expensive mistakes",
        "fr": "<b>Fig. 2</b>Le squat : la trajectoire correcte et les deux erreurs coûteuses"},
    "La línea de puntos es la <b>plomada</b>: la barra debe caer siempre "
    "sobre la mitad del pie. Los dos errores de la derecha son los que provocan la mayoría de "
    "las lesiones de rodilla y de zona lumbar.": {
        "en": "The dotted line is the <b>plumb line</b>: the bar must always fall over the "
              "middle of the foot. The two mistakes on the right are what cause most knee and "
              "lower-back injuries.",
        "fr": "La ligne pointillée est le <b>fil à plomb</b> : la barre doit toujours tomber "
              "au milieu du pied. Les deux erreurs de droite provoquent la majorité des "
              "blessures au genou et au bas du dos."},

    "Estiramientos: cuándo sí y cuándo no": {
        "en": "Stretching: when yes and when no",
        "fr": "Étirements : quand oui et quand non"},
    "Estiramiento estático <strong>después</strong> de entrenar, no antes: reduce la "
    "producción de fuerza. Antes, movilidad dinámica.": {
        "en": "Static stretching <strong>after</strong> training, not before: it reduces "
              "force production. Before, do dynamic mobility.",
        "fr": "Étirements statiques <strong>après</strong> la séance, pas avant : ils "
              "réduisent la production de force. Avant, mobilité dynamique."},

    # ── Registro ───────────────────────────────────────────────────────────
    "Registro de cargas": {"en": "Load log", "fr": "Suivi des charges"},
    'TU REGISTRO DE <span class="a">PROGRESIÓN</span>': {
        "en": 'YOUR <span class="a">PROGRESSION</span> LOG',
        "fr": 'VOTRE SUIVI DE <span class="a">PROGRESSION</span>'},
    "Sem. 5": {"en": "Wk 5", "fr": "Sem. 5"},
    "Sem. 6": {"en": "Wk 6", "fr": "Sem. 6"},
    "Sem. 7": {"en": "Wk 7", "fr": "Sem. 7"},
    "Sem. 8": {"en": "Wk 8", "fr": "Sem. 8"},
    "Sentadilla": {"en": "Squat", "fr": "Squat"},
    "Peso muerto": {"en": "Deadlift", "fr": "Soulevé de terre"},
    "Récords personales del ciclo": {
        "en": "Personal records for the cycle", "fr": "Records personnels du cycle"},
    "Marca inicial": {"en": "Starting mark", "fr": "Marque de départ"},
    "Marca final": {"en": "Final mark", "fr": "Marque finale"},

    # ── Cierre ─────────────────────────────────────────────────────────────
    'OCHO SEMANAS, <span class="a">UNA SOLA REGLA</span>': {
        "en": 'EIGHT WEEKS, <span class="a">ONE SINGLE RULE</span>',
        "fr": 'HUIT SEMAINES, <span class="a">UNE SEULE RÈGLE</span>'},

    "La progresión solo funciona si <strong>anotas cada serie</strong>: sin "
    "registro no hay sobrecarga, hay repetición. Ocho semanas bien apuntadas valen más que un "
    "año entrenando de memoria.": {
        "en": "Progression only works if you <strong>write down every set</strong>: without a "
              "log there is no overload, there is repetition. Eight weeks properly recorded "
              "are worth more than a year of training from memory.",
        "fr": "La progression ne fonctionne que si vous <strong>notez chaque série</strong> : "
              "sans relevé il n'y a pas de surcharge, il y a de la répétition. Huit semaines "
              "bien notées valent mieux qu'une année d'entraînement de mémoire."},

    # ── Aviso legal ────────────────────────────────────────────────────────
    "<b>Aviso importante</b><br> "
    "Documento con finalidad informativa y educativa. No constituye consejo médico, "
    "diagnóstico ni tratamiento, y no sustituye la valoración de un profesional sanitario "
    "colegiado ni la supervisión presencial de un entrenador cualificado. El entrenamiento con "
    "cargas conlleva riesgo de lesión: solicita una valoración médica antes de comenzar, "
    "especialmente si tienes más de 40 años, llevas tiempo inactivo, has sufrido lesiones "
    "previas, padeces hipertensión, cardiopatía o patología articular, estás embarazada o en "
    "periodo de lactancia, o eres menor de edad. Ejecuta siempre los movimientos con técnica "
    "correcta y utiliza ayudante o barras de seguridad en los ejercicios con carga elevada. "
    "Los resultados varían entre personas y no están garantizados. Contenido protegido por "
    "derechos de autor: prohibida su reproducción, distribución o reventa sin autorización "
    "escrita de VILLUMINATIONS.": {
        "en": "<b>Important notice</b><br> "
              "This document is for informational and educational purposes. It does not "
              "constitute medical advice, diagnosis or treatment, and it does not replace "
              "assessment by a registered health professional or in-person supervision by a "
              "qualified coach. Resistance training carries a risk of injury: seek a medical "
              "assessment before starting, especially if you are over 40, have been inactive "
              "for some time, have had previous injuries, have high blood pressure, heart "
              "disease or a joint condition, are pregnant or breastfeeding, or are a minor. "
              "Always perform the movements with correct technique, and use a spotter or "
              "safety bars on heavily loaded exercises. Results vary between individuals and "
              "are not guaranteed. Copyrighted content: reproduction, distribution or resale "
              "without written permission from VILLUMINATIONS is prohibited.",
        "fr": "<b>Avertissement important</b><br> "
              "Document à finalité informative et éducative. Il ne constitue ni un avis "
              "médical, ni un diagnostic, ni un traitement, et ne remplace pas l'évaluation "
              "d'un professionnel de santé ni la supervision sur place d'un entraîneur "
              "qualifié. L'entraînement avec charges comporte un risque de blessure : "
              "demandez un avis médical avant de commencer, en particulier si vous avez plus "
              "de 40 ans, si vous êtes inactif depuis longtemps, si vous avez déjà été "
              "blessé, si vous souffrez d'hypertension, d'une cardiopathie ou d'une "
              "pathologie articulaire, si vous êtes enceinte ou allaitante, ou si vous êtes "
              "mineur. Exécutez toujours les mouvements avec une technique correcte et "
              "utilisez un partenaire ou des barres de sécurité sur les exercices lourds. "
              "Les résultats varient d'une personne à l'autre et ne sont pas garantis. "
              "Contenu protégé par le droit d'auteur : toute reproduction, distribution ou "
              "revente sans autorisation écrite de VILLUMINATIONS est interdite."},
}
