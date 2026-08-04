# -*- coding: utf-8 -*-
"""
CÓDICE DEL DESCANSO · rótulos de las seis láminas — inglés y francés
====================================================================
Las glosas del reloj circadiano van partidas por cláusulas en el módulo de
datos y aquí se traducen renglón a renglón, respetando esa partición: cada
renglón es una frase completa en los tres idiomas y ninguno pasa del ancho de
la ficha, que es de 46 caracteres. Es la misma restricción que comprueba el
generador de datos antes de dibujar.

«REM» no se traduce en ninguno de los tres idiomas: es la sigla internacional.
«Sueño profundo» sí, porque es descripción y no nomenclatura.
"""

T = {
    "Códice del Descanso | VILLUMINATIONS": {
        "en": "Codex of Rest | VILLUMINATIONS",
        "fr": "Codex du Repos | VILLUMINATIONS"},

    # ── Lámina: el reloj circadiano ────────────────────────────────────────
    "MÍNIMO DE TEMPERATURA": {
        "en": "CORE TEMPERATURE", "fr": "MINIMUM DE TEMPÉRATURE"},
    "CENTRAL": {"en": "MINIMUM", "fr": "CENTRALE"},
    "El punto más bajo del día.": {
        "en": "The lowest point of the day.", "fr": "Le point le plus bas du jour."},
    "Despertar aquí es lo que peor sienta": {
        "en": "Waking here is what feels worst",
        "fr": "S'éveiller ici est ce qui pèse le plus"},

    "DESPERTAR": {"en": "WAKING", "fr": "RÉVEIL"},
    "Sube el cortisol de forma brusca:": {
        "en": "Cortisol rises sharply:", "fr": "Le cortisol monte brusquement :"},
    "es normal y es útil": {
        "en": "normal, and useful", "fr": "normal et utile"},

    "PICO DE CORTISOL MATINAL": {
        "en": "MORNING CORTISOL PEAK", "fr": "PIC DE CORTISOL MATINAL"},
    "Treinta a cuarenta y cinco minutos": {
        "en": "Thirty to forty-five minutes", "fr": "Trente à quarante-cinq minutes"},
    "después de abrir los ojos": {
        "en": "after opening your eyes", "fr": "après avoir ouvert les yeux"},

    "BAJÓN DE ALERTA DE LA": {
        "en": "AFTERNOON DIP IN", "fr": "CREUX DE VIGILANCE DE"},
    "TARDE": {"en": "ALERTNESS", "fr": "L'APRÈS-MIDI"},
    "No lo causa la comida: ocurre igual en ayunas.": {
        "en": "Food does not cause it: it happens fasted too.",
        "fr": "Le repas n'en est pas la cause : à jeun aussi."},
    "Es el hueco de la siesta corta": {
        "en": "It is the slot for the short nap",
        "fr": "C'est le créneau de la sieste courte"},

    "MÁXIMO DE FUERZA Y": {"en": "PEAK STRENGTH AND", "fr": "MAXIMUM DE FORCE ET"},
    "TEMPERATURA": {"en": "TEMPERATURE", "fr": "DE TEMPÉRATURE"},
    "La franja en que mejor se rinde": {
        "en": "The window of best performance",
        "fr": "La plage où l'on rend le mieux"},
    "en casi todas las pruebas físicas": {
        "en": "on almost every physical test",
        "fr": "sur presque tous les tests physiques"},

    "ZONA DE MANTENIMIENTO DE": {
        "en": "WAKE MAINTENANCE", "fr": "ZONE DE MAINTIEN DE"},
    "LA VIGILIA": {"en": "ZONE", "fr": "L'ÉVEIL"},
    "Las dos o tres horas antes de dormir": {
        "en": "The two or three hours before sleep",
        "fr": "Les deux ou trois heures avant le coucher"},
    "en que cuesta más dormirse, aunque haya sueño": {
        "en": "when falling asleep is hardest, even when tired",
        "fr": "où s'endormir est le plus dur, même fatigué"},

    "INICIO DE LA MELATONINA": {
        "en": "MELATONIN ONSET", "fr": "DÉBUT DE LA MÉLATONINE"},
    "Con luz tenue.": {"en": "Under dim light.", "fr": "Sous lumière tamisée."},
    "La luz intensa a esta hora lo retrasa": {
        "en": "Bright light at this hour delays it",
        "fr": "Une lumière vive à cette heure le retarde"},

    "SUEÑO": {"en": "SLEEP", "fr": "SOMMEIL"},
    "Si el horario es estable": {
        "en": "If the schedule is stable", "fr": "Si l'horaire est stable"},
    "HORAS CONTADAS DESDE EL DESPERTAR HABITUAL · CRONOTIPO INTERMEDIO": {
        "en": "HOURS COUNTED FROM YOUR USUAL WAKING TIME · INTERMEDIATE CHRONOTYPE",
        "fr": "HEURES COMPTÉES DEPUIS LE RÉVEIL HABITUEL · CHRONOTYPE INTERMÉDIAIRE"},

    # ── Lámina: el hipnograma ──────────────────────────────────────────────
    "Despierto": {"en": "Awake", "fr": "Éveil"},
    "REM": {"en": "REM", "fr": "REM"},
    "PRIMERA MITAD · MANDA EL PROFUNDO": {
        "en": "FIRST HALF · DEEP SLEEP RULES",
        "fr": "PREMIÈRE MOITIÉ · LE PROFOND COMMANDE"},
    "SEGUNDA MITAD · MANDA EL REM": {
        "en": "SECOND HALF · REM RULES",
        "fr": "SECONDE MOITIÉ · LE REM COMMANDE"},
    "4 A 6 CICLOS DE UNOS 90 MINUTOS": {
        "en": "4 TO 6 CYCLES OF ABOUT 90 MINUTES",
        "fr": "4 À 6 CYCLES D'ENVIRON 90 MINUTES"},
    "RECORTAR POR EL FINAL SE COME EL REM, NO EL PROFUNDO": {
        "en": "CUTTING FROM THE END EATS REM, NOT DEEP SLEEP",
        "fr": "COUPER PAR LA FIN MANGE LE REM, PAS LE PROFOND"},

    # ── Lámina: las cuatro fases ───────────────────────────────────────────
    "TRANSICIÓN": {"en": "TRANSITION", "fr": "TRANSITION"},
    "Muy ligero. Se puede negar haber dormido": {
        "en": "Very light. You may deny having slept at all",
        "fr": "Très léger. On peut nier avoir dormi"},
    "1 a 5 min": {"en": "1 to 5 min", "fr": "1 à 5 min"},
    "SUEÑO LIGERO": {"en": "LIGHT SLEEP", "fr": "SOMMEIL LÉGER"},
    "Aquí se consolida buena parte de la memoria de procedimiento": {
        "en": "Much of procedural memory is consolidated here",
        "fr": "Une bonne part de la mémoire procédurale s'y consolide"},
    "La mayor parte de la noche": {
        "en": "Most of the night", "fr": "La plus grande partie de la nuit"},
    "SUEÑO PROFUNDO": {"en": "DEEP SLEEP", "fr": "SOMMEIL PROFOND"},
    "El de la recuperación física. Si se recorta el sueño por el final, este se conserva": {
        "en": "The one for physical recovery. If sleep is cut from the end, this one "
              "survives",
        "fr": "Celui de la récupération physique. Si l'on coupe le sommeil par la fin, "
              "celui-ci est préservé"},
    "Concentrado en la primera mitad": {
        "en": "Concentrated in the first half",
        "fr": "Concentré sur la première moitié"},
    "MOVIMIENTOS OCULARES RÁPIDOS": {
        "en": "RAPID EYE MOVEMENT", "fr": "MOUVEMENTS OCULAIRES RAPIDES"},
    "Concentrado en la segunda mitad. Si se recorta el sueño por el final, este es el que se pierde": {
        "en": "Concentrated in the second half. If sleep is cut from the end, this is the "
              "one you lose",
        "fr": "Concentré sur la seconde moitié. Si l'on coupe le sommeil par la fin, c'est "
              "celui-ci que l'on perd"},
    "Crece en cada ciclo": {
        "en": "It grows with every cycle", "fr": "Il croît à chaque cycle"},
    "ARQUITECTURA DEL SUEÑO · CUATRO ESTADOS, NO UNO": {
        "en": "SLEEP ARCHITECTURE · FOUR STATES, NOT ONE",
        "fr": "ARCHITECTURE DU SOMMEIL · QUATRE ÉTATS, PAS UN"},

    # ── Lámina: la deuda de sueño ──────────────────────────────────────────
    "OBJETIVO · 7 h": {"en": "TARGET · 7 h", "fr": "OBJECTIF · 7 h"},
    "DEUDA ACUMULADA EN LA SEMANA: 4,5 HORAS": {
        "en": "DEBT ACCUMULATED OVER THE WEEK: 4.5 HOURS",
        "fr": "DETTE ACCUMULÉE SUR LA SEMAINE : 4,5 HEURES"},
    "DORMIR DE MÁS EL FIN DE SEMANA RECUPERA PARTE · NO TODA": {
        "en": "SLEEPING IN AT THE WEEKEND RECOVERS SOME OF IT · NOT ALL",
        "fr": "DORMIR PLUS LE WEEK-END EN RÉCUPÈRE UNE PART · PAS TOUTE"},

    # ── Lámina: la cafeína ─────────────────────────────────────────────────
    "VIDA MEDIA DE UNAS 5 HORAS · ENTRE 3 Y 7 SEGÚN LA PERSONA": {
        "en": "HALF-LIFE OF ABOUT 5 HOURS · BETWEEN 3 AND 7 DEPENDING ON THE PERSON",
        "fr": "DEMI-VIE D'ENVIRON 5 HEURES · ENTRE 3 ET 7 SELON LA PERSONNE"},
    "horas desde la taza": {"en": "hours since the cup", "fr": "heures depuis la tasse"},
    "NO IMPIDE DORMIRSE · RECORTA EL SUEÑO PROFUNDO DE ESA NOCHE": {
        "en": "IT DOES NOT STOP YOU FALLING ASLEEP · IT CUTS THAT NIGHT'S DEEP SLEEP",
        "fr": "ELLE N'EMPÊCHE PAS DE DORMIR · ELLE ROGNE LE PROFOND DE LA NUIT"},

    # ── Lámina: la cuenta atrás ────────────────────────────────────────────
    "ÚLTIMA CAFEÍNA": {"en": "LAST CAFFEINE", "fr": "DERNIÈRE CAFÉINE"},
    "Su vida media ronda las 5 horas: a las 10 queda un octavo": {
        "en": "Its half-life is around 5 hours: by 10 an eighth is left",
        "fr": "Sa demi-vie avoisine 5 heures : à 10 h il en reste un huitième"},
    "ÚLTIMA COMIDA GRANDE": {"en": "LAST LARGE MEAL", "fr": "DERNIER GROS REPAS"},
    "La digestión sube la temperatura central": {
        "en": "Digestion raises core temperature",
        "fr": "La digestion élève la température centrale"},
    "ÚLTIMO ALCOHOL": {"en": "LAST ALCOHOL", "fr": "DERNIER ALCOOL"},
    "Adormece y luego fragmenta la segunda mitad": {
        "en": "It makes you drowsy, then fragments the second half",
        "fr": "Il endort, puis fragmente la seconde moitié"},
    "ÚLTIMO ENTRENAMIENTO FUERTE": {
        "en": "LAST HARD TRAINING SESSION", "fr": "DERNIER ENTRAÎNEMENT INTENSE"},
    "Salvo que lo lleves bien probado": {
        "en": "Unless you have tested it thoroughly",
        "fr": "Sauf si vous l'avez bien éprouvé"},
    "FUERA PANTALLAS Y TRABAJO": {
        "en": "SCREENS AND WORK OFF", "fr": "PLUS D'ÉCRANS NI DE TRAVAIL"},
    "La única regla no negociable de la lista": {
        "en": "The only non-negotiable rule on the list",
        "fr": "La seule règle non négociable de la liste"},
    "MISMA HORA, TODOS LOS DÍAS": {
        "en": "SAME TIME, EVERY DAY", "fr": "MÊME HEURE, TOUS LES JOURS"},
    "Incluido el fin de semana": {
        "en": "Weekends included", "fr": "Week-end compris"},
    "CUENTA ATRÁS DESDE LA HORA DE ACOSTARSE": {
        "en": "COUNTDOWN FROM BEDTIME",
        "fr": "COMPTE À REBOURS DEPUIS L'HEURE DU COUCHER"},
}
