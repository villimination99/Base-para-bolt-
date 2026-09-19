# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · rótulos de las láminas
===========================================
Todo lo de aquí vive dentro de un SVG, donde no hay nada que reajuste el texto
si se sale del recuadro. El cargador comprueba el ancho de cada rótulo contra
el del original y rechaza los que no caben, así que estos se han escrito
midiendo y no traduciendo a ojo.

Tres decisiones que se repiten:

  · «MET» no se traduce. Es la sigla internacional del equivalente metabólico,
    igual que «REM» en el libro del sueño.
  · Los nombres de los ocho patrones son los que se usan en cada gimnasio:
    «squat» y no «flexión de piernas» en francés, «hip hinge» y no «bisagra»
    en inglés. Traducir por el diccionario dejaría rótulos que nadie reconoce.
  · Las tres líneas de la glosa de INTENSIDAD son tres <text> distintos de un
    mismo párrafo partido a mano. Se traducen las tres a la vez y luego se
    reparten, porque traducir cada renglón por separado produce una frase que
    no concuerda consigo misma.
"""

T = {
    "Códice de la Carga | VILLUMINATIONS": {
        "en": "Codex of the Load | VILLUMINATIONS",
        "fr": "Codex de la Charge | VILLUMINATIONS"},

    # ── Lámina: la curva de la dosis semanal ───────────────────────────────
    "TRAMO MÁS RENTABLE": {
        "en": "BEST VALUE RANGE", "fr": "TRANCHE LA PLUS RENTABLE"},
    "BENEFICIO ADICIONAL": {
        "en": "EXTRA BENEFIT", "fr": "BÉNÉFICE SUPPLÉMENTAIRE"},
    "150 min": {"en": "150 min", "fr": "150 min"},
    "300 min": {"en": "300 min", "fr": "300 min"},
    "BENEFICIO": {"en": "BENEFIT", "fr": "BÉNÉFICE"},
    "min/semana": {"en": "min/week", "fr": "min/semaine"},
    "150–300 MIN MODERADOS · O 75–150 VIGOROSOS": {
        "en": "150–300 MODERATE MIN · OR 75–150 VIGOROUS",
        "fr": "150–300 MIN MODÉRÉES · OU 75–150 VIGOUREUSES"},
    "FORMA DE LA CURVA SEGÚN LAS GUÍAS · NO ES UN AJUSTE DE DATOS": {
        "en": "SHAPE OF THE CURVE PER THE GUIDELINES · NOT A FIT TO DATA",
        "fr": "FORME DE LA COURBE SELON LES GUIDES · PAS UN AJUSTEMENT"},

    # ── Lámina: la escala metabólica ───────────────────────────────────────
    "MODERADA · 3 MET": {"en": "MODERATE · 3 MET", "fr": "MODÉRÉE · 3 MET"},
    "VIGOROSA · 6 MET": {"en": "VIGOROUS · 6 MET", "fr": "VIGOUREUSE · 6 MET"},
    "Sentado, en reposo": {"en": "Sitting, at rest", "fr": "Assis, au repos"},
    "De pie, quieto": {"en": "Standing still", "fr": "Debout, immobile"},
    "Caminar despacio · 3 km/h": {
        "en": "Walking slowly · 3 km/h", "fr": "Marche lente · 3 km/h"},
    "Caminar a paso vivo · 5 km/h": {
        "en": "Brisk walking · 5 km/h", "fr": "Marche rapide · 5 km/h"},
    "Bicicleta tranquila · 14 km/h": {
        "en": "Easy cycling · 14 km/h", "fr": "Vélo tranquille · 14 km/h"},
    "Pesas, sesión general": {
        "en": "Weights, general session", "fr": "Musculation, séance type"},
    "Pesas, esfuerzo alto": {
        "en": "Weights, hard effort", "fr": "Musculation, effort élevé"},
    "Bicicleta · 20 km/h": {"en": "Cycling · 20 km/h", "fr": "Vélo · 20 km/h"},
    "Trotar · 8 km/h": {"en": "Jogging · 8 km/h", "fr": "Footing · 8 km/h"},
    "Correr · 11 km/h": {"en": "Running · 11 km/h", "fr": "Course · 11 km/h"},
    "Cuerda, ritmo rápido": {
        "en": "Skipping, fast pace", "fr": "Corde, rythme rapide"},
    "UN MINUTO VIGOROSO CUENTA COMO DOS MODERADOS": {
        "en": "ONE VIGOROUS MINUTE COUNTS AS TWO MODERATE ONES",
        "fr": "UNE MINUTE VIGOUREUSE COMPTE POUR DEUX MODÉRÉES"},
    "EQUIVALENTE METABÓLICO · VECES EL GASTO EN REPOSO": {
        "en": "METABOLIC EQUIVALENT · TIMES THE RESTING COST",
        "fr": "ÉQUIVALENT MÉTABOLIQUE · FOIS LA DÉPENSE DE REPOS"},

    # ── Lámina: los ocho patrones ──────────────────────────────────────────
    "SENTADILLA": {"en": "SQUAT", "fr": "SQUAT"},
    "Rodilla y cadera flexionan juntas": {
        "en": "Knee and hip bend together",
        "fr": "Genou et hanche fléchissent ensemble"},
    "Sentadilla, prensa, zancada, subir…": {
        "en": "Squat, leg press, lunge, step-up…",
        "fr": "Squat, presse, fente, montée…"},

    "BISAGRA DE CADERA": {"en": "HIP HINGE", "fr": "CHARNIÈRE DE HANCHE"},
    "La cadera manda y la rodilla apenas se dobla": {
        "en": "The hip leads and the knee barely bends",
        "fr": "La hanche commande, le genou fléchit à peine"},
    "Peso muerto, buenos días, empuje de…": {
        "en": "Deadlift, good morning, hip thrust…",
        "fr": "Soulevé de terre, good morning, hip…"},

    "EMPUJE HORIZONTAL": {"en": "HORIZONTAL PUSH", "fr": "POUSSÉE HORIZONTALE"},
    "Alejar peso del pecho": {
        "en": "Push weight from the chest", "fr": "Éloigner le poids du buste"},
    "Press de banca, flexiones, fondos": {
        "en": "Bench press, push-ups, dips",
        "fr": "Développé couché, pompes, dips"},

    "EMPUJE VERTICAL": {"en": "VERTICAL PUSH", "fr": "POUSSÉE VERTICALE"},
    "Llevar peso por encima de la cabeza": {
        "en": "Take weight above the head",
        "fr": "Porter le poids au-dessus de la tête"},
    "Press militar, press con mancuernas": {
        "en": "Overhead press, dumbbell press",
        "fr": "Développé militaire, développé haltères"},

    "TIRÓN HORIZONTAL": {"en": "HORIZONTAL PULL", "fr": "TIRAGE HORIZONTAL"},
    "Traer peso hacia el tronco": {
        "en": "Draw weight to the torso", "fr": "Amener le poids vers le tronc"},
    "Remo con barra, remo con mancuerna…": {
        "en": "Barbell row, dumbbell row…", "fr": "Rowing barre, rowing haltère…"},

    "TIRÓN VERTICAL": {"en": "VERTICAL PULL", "fr": "TIRAGE VERTICAL"},
    "Traer el cuerpo o el peso desde arriba": {
        "en": "Draw body or weight from above",
        "fr": "Amener le corps ou le poids d'en haut"},
    "Dominadas, jalón al pecho": {
        "en": "Pull-ups, lat pulldown", "fr": "Tractions, tirage vertical"},

    "TRANSPORTE": {"en": "CARRY", "fr": "PORTÉ"},
    "Sostener y andar con carga": {
        "en": "Hold a load and walk", "fr": "Tenir une charge et marcher"},
    "Paseo del granjero, transporte…": {
        "en": "Farmer's walk, suitcase carry…",
        "fr": "Marche du fermier, porté valise…"},

    "ANTIRROTACIÓN": {"en": "ANTI-ROTATION", "fr": "ANTIROTATION"},
    "Resistir un giro sin girar": {
        "en": "Resist a twist without twisting",
        "fr": "Résister sans laisser tourner"},
    "Plancha, press Pallof, transporte a…": {
        "en": "Plank, Pallof press, suitcase…",
        "fr": "Gainage, press Pallof, porté…"},

    "OCHO PATRONES · UNA SEMANA QUE LOS TOCA TODOS NO DEJA HUECOS": {
        "en": "EIGHT PATTERNS · A WEEK THAT TOUCHES THEM ALL LEAVES NO GAPS",
        "fr": "HUIT SCHÉMAS · UNE SEMAINE QUI LES TOUCHE TOUS NE LAISSE RIEN"},

    # ── Lámina: las seis variables ─────────────────────────────────────────
    "SEIS VARIABLES · SE SUBE UNA CADA VEZ": {
        "en": "SIX VARIABLES · YOU RAISE ONE AT A TIME",
        "fr": "SIX VARIABLES · ON EN MONTE UNE À LA FOIS"},

    "INTENSIDAD": {"en": "INTENSITY", "fr": "INTENSITÉ"},
    "Cuánto pesa respecto a tu máximo,": {
        "en": "How much it weighs against your max,",
        "fr": "Le poids par rapport à votre maximum,"},
    "o cuántas repeticiones te quedaban": {
        "en": "or how many reps you had left",
        "fr": "ou le nombre de répétitions restées"},
    "en reserva al terminar la serie": {
        "en": "in reserve when the set ended",
        "fr": "en réserve à la fin de la série"},

    "VOLUMEN": {"en": "VOLUME", "fr": "VOLUME"},
}
