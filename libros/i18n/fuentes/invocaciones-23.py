# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · la tabla de prescripciones y el plan de doce meses
===============================================================================
La tabla de lo que la tradición prescribía tiene dos columnas: la práctica y
qué era en realidad, con el veredicto —se conserva o se descarta— pegado a la
glosa. Las glosas son de una o dos frases y así se quedan: la columna es
estrecha y el veredicto tiene que verse de un vistazo.

El plan de doce meses va por trimestres y sin nombrarlos: cada entrada empieza
por lo que se añade. Se conservan los meses numerados (el disco en el 2, la
copa en el 3) y el orden caldeo por su nombre, que ya está en el capítulo de
las horas.

Los tres indicadores del final son porcentajes y se dicen con letra —setenta
por ciento, cincuenta— en las tres lenguas, igual que el original.
"""

T = {
    "Algo de fuerza dos veces por semana, con lo que tengas. La postura de pie sostenida es "
    "una demanda de fuerza, no de flexibilidad.": {
        "en": "Some strength work twice a week, with whatever you have. A sustained standing "
              "posture is a demand for strength, not for flexibility.",
        "fr": "Un peu de force deux fois par semaine, avec ce que vous avez. La posture debout "
              "tenue est une exigence de force, non de souplesse."},

    "Respiración: los ejercicios del capítulo 10, fuera de la sesión, tres minutos al día. Es "
    "lo que hace que la vocalización no se quede corta de aire.": {
        "en": "Breathing: the exercises from chapter 10, outside the session, three minutes a "
              "day. That is what keeps the vocalisation from running short of air.",
        "fr": "Respiration : les exercices du chapitre 10, hors séance, trois minutes par jour. "
              "C'est ce qui évite que la vocalisation manque d'air."},

    "Lo que la tradición prescribía y lo que era en realidad": {
        "en": "What the tradition prescribed and what it actually was",
        "fr": "Ce que la tradition prescrivait et ce que c'était en réalité"},

    "El baño previo": {"en": "The bath beforehand", "fr": "Le bain préalable"},
    "Transición sensorial. Funciona, se conserva.": {
        "en": "A sensory transition. It works, it is kept.",
        "fr": "Une transition sensorielle. Cela fonctionne, on le garde."},

    "El ayuno": {"en": "The fast", "fr": "Le jeûne"},
    "Alerta aumentada. Se conserva en su versión breve; los ayunos largos se descartan.": {
        "en": "Heightened alertness. Kept in its short version; long fasts are discarded.",
        "fr": "Vigilance accrue. On garde la version brève ; les jeûnes longs sont écartés."},

    "La vigilia nocturna": {"en": "The night vigil", "fr": "La veille nocturne"},
    "Privación de sueño. Se descarta: perjudica exactamente lo que se busca.": {
        "en": "Sleep deprivation. Discarded: it damages exactly what is being sought.",
        "fr": "Privation de sommeil. Écartée : elle nuit exactement à ce que l'on cherche."},

    "La abstinencia": {"en": "Abstinence", "fr": "L'abstinence"},
    "Reducción de estímulo. Se conserva como reducción voluntaria y temporal de distracción, "
    "no como norma moral.": {
        "en": "A reduction of stimulus. Kept as a voluntary and temporary reduction of "
              "distraction, not as a moral rule.",
        "fr": "Réduction du stimulus. Gardée comme réduction volontaire et temporaire de la "
              "distraction, non comme règle morale."},

    "La ropa reservada": {"en": "The set-aside clothing", "fr": "Le vêtement réservé"},
    "Disparador condicionado. Funciona muy bien, se conserva.": {
        "en": "A conditioned trigger. It works very well, it is kept.",
        "fr": "Déclencheur conditionné. Cela fonctionne très bien, on le garde."},

    "El incienso": {"en": "Incense", "fr": "L'encens"},
    "Anclaje olfativo, que es el más potente de todos. Se conserva, con ventilación.": {
        "en": "An olfactory anchor, which is the most powerful of all. Kept, with ventilation.",
        "fr": "Ancrage olfactif, le plus puissant de tous. Gardé, avec de l'aération."},

    "El resumen del capítulo": {
        "en": "The chapter in summary", "fr": "Le résumé du chapitre"},

    "Duerme a la misma hora, come dos horas antes, no bebas alcohol el día anterior, camina "
    "todos los días y opera en el mismo sitio a la misma hora. Eso es el noventa por ciento "
    "del trabajo corporal del oficio, y no tiene absolutamente nada de misterioso. La parte "
    "misteriosa es que casi nadie lo hace.": {
        "en": "Sleep at the same time, eat two hours before, drink no alcohol the day before, "
              "walk every day and operate in the same place at the same hour. That is ninety "
              "per cent of the bodily work of the trade, and there is absolutely nothing "
              "mysterious about it. The mysterious part is that hardly anybody does it.",
        "fr": "Dormez à la même heure, mangez deux heures avant, ne buvez pas d'alcool la "
              "veille, marchez tous les jours et opérez au même endroit à la même heure. Voilà "
              "quatre-vingt-dix pour cent du travail corporel du métier, et cela n'a absolument "
              "rien de mystérieux. La part mystérieuse, c'est que presque personne ne le fait."},

    # ── El plan de doce meses ──────────────────────────────────────────────
    "Un plan de doce meses, para quien quiera uno. No es obligatorio y es mejor que "
    "improvisar.": {
        "en": "A twelve-month plan, for whoever wants one. It is not compulsory and it is "
              "better than improvising.",
        "fr": "Un plan de douze mois, pour qui en veut un. Il n'est pas obligatoire et il vaut "
              "mieux qu'improviser."},

    "Solo el rito diario, todos los días, y el diario. Nada más. Se dedica el disco en el mes "
    "2 y la copa en el 3.": {
        "en": "Only the daily rite, every day, and the journal. Nothing else. The disc is "
              "dedicated in month 2 and the cup in month 3.",
        "fr": "Seulement le rite quotidien, tous les jours, et le journal. Rien d'autre. On dédie "
              "le disque au mois 2 et la coupe au mois 3."},

    "Se añade una operación planetaria por semana, empezando por Saturno y bajando por el "
    "orden caldeo. Se dedican la espada y la vara.": {
        "en": "One planetary operation a week is added, beginning with Saturn and working down "
              "the Chaldean order. The sword and the wand are dedicated.",
        "fr": "On ajoute une opération planétaire par semaine, en commençant par Saturne et en "
              "descendant l'ordre chaldéen. On dédie l'épée et la baguette."},

    "Se añade una operación de examen al mes, sobre un solo asunto, tres sesiones separadas. "
    "Se sigue con las planetarias.": {
        "en": "One examination operation a month is added, on a single matter, three sessions "
              "apart. The planetary ones continue.",
        "fr": "On ajoute une opération d'examen par mois, sur une seule affaire, trois séances "
              "espacées. On poursuit les planétaires."},

    "Se sostiene todo lo anterior sin añadir nada. El último trimestre es el que de verdad "
    "prueba si hay práctica: no trae novedades.": {
        "en": "Everything above is kept up with nothing added. The last quarter is the one that "
              "really tests whether there is a practice: it brings nothing new.",
        "fr": "On maintient tout ce qui précède sans rien ajouter. Le dernier trimestre est "
              "celui qui éprouve vraiment s'il y a pratique : il n'apporte aucune nouveauté."},

    "Cómo saber si el año ha servido. Ninguno de los tres tiene que ver con lo que se sienta "
    "durante las sesiones.": {
        "en": "How to tell whether the year has been worth it. None of the three has anything "
              "to do with what you feel during the sessions.",
        "fr": "Comment savoir si l'année a servi. Aucun des trois n'a de rapport avec ce que l'on "
              "ressent pendant les séances."},

    "El número. Sesiones hechas frente a sesiones previstas, sacado del diario. Por encima del "
    "setenta por ciento hay práctica; por debajo del cincuenta, hay intención.": {
        "en": "The number. Sessions done against sessions planned, taken from the journal. "
              "Above seventy per cent there is a practice; below fifty, there is an intention.",
        "fr": "Le nombre. Séances faites face aux séances prévues, tiré du journal. Au-dessus de "
              "soixante-dix pour cent il y a une pratique ; au-dessous de cinquante, il y a une "
              "intention."},

    "La recuperación. Cuánto tardas en volver después de una interrupción de una semana. Al "
    "principio son semanas; con el año instalado son días. Ese es el indicador más fiable de "
    "todos.": {
        "en": "Recovery. How long you take to come back after a week's interruption. At the "
              "start it is weeks; with the year installed it is days. That is the most reliable "
              "indicator of all.",
        "fr": "La reprise. Combien de temps vous mettez à revenir après une interruption d'une "
              "semaine. Au début ce sont des semaines ; l'année installée, ce sont des jours. "
              "C'est l'indicateur le plus fiable de tous."},

    "El testimonio ajeno. Lo que nota la gente que convive contigo, preguntado directamente y "
    "sin sugerir la respuesta.": {
        "en": "Other people's testimony. What the people who live with you notice, asked "
              "directly and without prompting the answer.",
        "fr": "Le témoignage d'autrui. Ce que remarquent les gens qui vivent avec vous, demandé "
              "directement et sans souffler la réponse."},
}
