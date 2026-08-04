# -*- coding: utf-8 -*-
"""
CÓDICE DEL DESCANSO · capítulo 2, el reloj interno
==================================================
La ficha de hitos del libro repite las glosas del reloj, pero unidas en una
sola frase: la lámina las imprime partidas en dos renglones y el texto las lee
seguidas. Son segmentos distintos porque son cadenas distintas, y las dos
traducciones tienen que decir lo mismo — se han escrito emparejadas para que
así sea.

Las horas llevan coma decimal en español y en francés («+0,6 h») y punto en
inglés («+0.6 h»), que es la convención de cada idioma.
"""

T = {
    '<span class="fig-n">El día biológico, hito por hito</span> Las horas van contadas '
    "desde el despertar habitual y corresponden a un cronotipo intermedio. Ninguno de "
    "estos hitos se decide a voluntad: se arrastran cambiando la hora de levantarse y la "
    "exposición a la luz.": {
        "en": '<span class="fig-n">The biological day, milestone by milestone</span> The '
              "hours are counted from your usual waking time and correspond to an "
              "intermediate chronotype. None of these milestones is decided at will: they "
              "are dragged along by changing your get-up time and your light exposure.",
        "fr": '<span class="fig-n">La journée biologique, jalon par jalon</span> Les heures '
              "sont comptées depuis le réveil habituel et correspondent à un chronotype "
              "intermédiaire. Aucun de ces jalons ne se décide à volonté : on les déplace "
              "en changeant l'heure du lever et l'exposition à la lumière."},

    "Los hitos del día": {
        "en": "The milestones of the day", "fr": "Les jalons de la journée"},

    "-2 h · Mínimo de temperatura central": {
        "en": "-2 h · Core temperature minimum",
        "fr": "-2 h · Minimum de température centrale"},
    "El punto más bajo del día. Despertar aquí es lo que peor sienta": {
        "en": "The lowest point of the day. Waking here is what feels worst",
        "fr": "Le point le plus bas du jour. S'éveiller ici est ce qui pèse le plus"},

    "+0 h · Despertar": {"en": "+0 h · Waking", "fr": "+0 h · Réveil"},
    "Sube el cortisol de forma brusca: es normal y es útil": {
        "en": "Cortisol rises sharply: this is normal and it is useful",
        "fr": "Le cortisol monte brusquement : c'est normal et c'est utile"},

    "+0,6 h · Pico de cortisol matinal": {
        "en": "+0.6 h · Morning cortisol peak",
        "fr": "+0,6 h · Pic de cortisol matinal"},
    "Treinta a cuarenta y cinco minutos después de abrir los ojos": {
        "en": "Thirty to forty-five minutes after opening your eyes",
        "fr": "Trente à quarante-cinq minutes après avoir ouvert les yeux"},

    "+7 h · Bajón de alerta de la tarde": {
        "en": "+7 h · Afternoon dip in alertness",
        "fr": "+7 h · Creux de vigilance de l'après-midi"},
    "No lo causa la comida: ocurre igual en ayunas. Es el hueco de la siesta corta": {
        "en": "Food does not cause it: it happens fasted too. It is the slot for the short "
              "nap",
        "fr": "Le repas n'en est pas la cause : à jeun aussi. C'est le créneau de la sieste "
              "courte"},

    "+10 h · Máximo de fuerza y temperatura": {
        "en": "+10 h · Peak strength and temperature",
        "fr": "+10 h · Maximum de force et de température"},
    "La franja en que mejor se rinde en casi todas las pruebas físicas": {
        "en": "The window of best performance on almost every physical test",
        "fr": "La plage où l'on rend le mieux sur presque tous les tests physiques"},

    "+14 h · Zona de mantenimiento de la vigilia": {
        "en": "+14 h · Wake maintenance zone",
        "fr": "+14 h · Zone de maintien de l'éveil"},
    "Las dos o tres horas antes de dormir en que cuesta más dormirse, aunque haya sueño": {
        "en": "The two or three hours before sleep when falling asleep is hardest, even "
              "when tired",
        "fr": "Les deux ou trois heures avant le coucher où s'endormir est le plus dur, "
              "même fatigué"},

    "+15 h · Inicio de la melatonina": {
        "en": "+15 h · Melatonin onset", "fr": "+15 h · Début de la mélatonine"},
    "Con luz tenue. La luz intensa a esta hora lo retrasa": {
        "en": "Under dim light. Bright light at this hour delays it",
        "fr": "Sous lumière tamisée. Une lumière vive à cette heure le retarde"},

    "+16 h · Sueño": {"en": "+16 h · Sleep", "fr": "+16 h · Sommeil"},

    "Los tres que más se pueden usar": {
        "en": "The three you can do most with",
        "fr": "Les trois dont on peut le plus se servir"},

    "El mínimo de temperatura central cae unas dos horas antes de la hora habitual de "
    "despertar, y es el peor momento posible para levantarse. Quien adelanta el "
    "despertador dos horas un día suelto no está robando dos horas de sueño cualquiera: "
    "está despertando en el fondo del pozo, y de ahí la sensación desproporcionada.": {
        "en": "The core temperature minimum falls about two hours before your usual waking "
              "time, and it is the worst possible moment to get up. Someone who moves the "
              "alarm two hours earlier on a one-off day is not stealing two ordinary hours "
              "of sleep: they are waking at the bottom of the well, and hence the "
              "disproportionate feeling.",
        "fr": "Le minimum de température centrale tombe environ deux heures avant l'heure "
              "habituelle du réveil, et c'est le pire moment possible pour se lever. Celui "
              "qui avance son réveil de deux heures un jour isolé ne vole pas deux heures "
              "de sommeil ordinaires : il se réveille au fond du puits, d'où cette "
              "sensation disproportionnée."},

    "La zona de mantenimiento de la vigilia es el hito que más consuela conocer. Las dos o "
    "tres horas anteriores a la hora habitual de dormirse son, paradójicamente, de las más "
    "difíciles del día para dormirse: el reloj empuja hacia arriba justo antes de soltar. "
    "Por eso irse a la cama dos horas antes de lo normal la víspera de un madrugón casi "
    "nunca funciona, y por eso no significa que tengas insomnio.": {
        "en": "The wake maintenance zone is the most reassuring milestone to know about. "
              "The two or three hours before your usual sleep onset are, paradoxically, "
              "among the hardest of the day for falling asleep: the clock pushes upwards "
              "just before it lets go. That is why going to bed two hours earlier than "
              "usual the night before an early start almost never works, and why it does "
              "not mean you have insomnia.",
        "fr": "La zone de maintien de l'éveil est le jalon dont la connaissance console le "
              "plus. Les deux ou trois heures qui précèdent l'endormissement habituel sont, "
              "paradoxalement, parmi les plus difficiles de la journée pour s'endormir : "
              "l'horloge pousse vers le haut juste avant de lâcher. C'est pourquoi se "
              "coucher deux heures plus tôt que d'habitude la veille d'un lever matinal ne "
              "marche presque jamais, et pourquoi cela ne signifie pas que vous souffrez "
              "d'insomnie."},

    "Y el inicio de la melatonina, que ocurre con luz tenue un par de horas antes de "
    "dormirse, es el que explica la última hora sin pantallas fuertes y sin luz de techo. "
    "No porque una pantalla envenene: porque la luz intensa a esa hora retrasa el inicio, "
    "y el retraso se paga a la mañana siguiente.": {
        "en": "And melatonin onset, which happens under dim light a couple of hours before "
              "sleep, is what explains the last hour without bright screens and without the "
              "ceiling light on. Not because a screen poisons you: because bright light at "
              "that hour delays the onset, and the delay is paid for the next morning.",
        "fr": "Et le début de la mélatonine, qui survient sous lumière tamisée deux heures "
              "environ avant l'endormissement, est ce qui explique la dernière heure sans "
              "écrans lumineux et sans plafonnier. Non pas parce qu'un écran empoisonne : "
              "parce qu'une lumière vive à cette heure retarde ce début, et le retard se "
              "paie le lendemain matin."},

    "El cronotipo, y por qué no es una excusa": {
        "en": "Chronotype, and why it is not an excuse",
        "fr": "Le chronotype, et pourquoi ce n'est pas une excuse"},

    "Existe una variación individual real en la preferencia horaria y tiene base "
    "biológica: hay personas cuyo reloj corre naturalmente adelantado y otras cuyo reloj "
    "corre atrasado. No es una cuestión de disciplina y burlarse de ello es tan sensato "
    "como burlarse de la altura.": {
        "en": "There is real individual variation in time-of-day preference and it has a "
              "biological basis: some people's clock naturally runs early and others' runs "
              "late. It is not a question of discipline, and mocking it makes about as much "
              "sense as mocking someone's height.",
        "fr": "Il existe une réelle variation individuelle de la préférence horaire, et "
              "elle a une base biologique : l'horloge de certaines personnes avance "
              "naturellement, celle d'autres retarde. Ce n'est pas une question de "
              "discipline, et s'en moquer est aussi sensé que de se moquer de la taille."},

    "Lo que sí es cierto es que el reloj se puede desplazar dentro de un margen, y que la "
    "herramienta para hacerlo es la luz: luz intensa poco después de despertar adelanta el "
    "reloj; luz intensa por la noche lo atrasa. Quien quiera madrugar mejor tiene ahí su "
    "palanca, y no en acostarse antes a mirar el techo.": {
        "en": "What is true is that the clock can be shifted within a margin, and that the "
              "tool for doing it is light: bright light shortly after waking advances the "
              "clock; bright light at night delays it. Anyone who wants to get up earlier "
              "has their lever there, and not in going to bed sooner to stare at the "
              "ceiling.",
        "fr": "Ce qui est vrai, c'est que l'horloge peut être déplacée dans une certaine "
              "marge, et que l'outil pour le faire est la lumière : une lumière vive peu "
              "après le réveil avance l'horloge ; une lumière vive le soir la retarde. Qui "
              "veut se lever plus tôt a son levier là, et non dans le fait de se coucher "
              "plus tôt pour fixer le plafond."},

    "Cuándo el desfase deja de ser un cronotipo": {
        "en": "When the offset stops being a chronotype",
        "fr": "Quand le décalage cesse d'être un chronotype"},

    "Si la preferencia horaria es tan extrema que impide dormir en horarios socialmente "
    "viables durante meses, con repercusión seria en el trabajo o en los estudios, eso "
    "tiene nombre clínico y tratamiento, que incluye pautas de luz con horarios concretos. "
    "No se arregla con fuerza de voluntad y merece una consulta.": {
        "en": "If the time-of-day preference is so extreme that it prevents sleeping on "
              "socially workable hours for months on end, with serious consequences at work "
              "or in study, that has a clinical name and a treatment, which includes light "
              "protocols at specific times. It is not fixed with willpower and it deserves "
              "an appointment.",
        "fr": "Si la préférence horaire est si extrême qu'elle empêche de dormir à des "
              "horaires socialement viables pendant des mois, avec des répercussions "
              "sérieuses sur le travail ou les études, cela porte un nom clinique et se "
              "traite, notamment par des protocoles de lumière à des heures précises. Cela "
              "ne se règle pas par la volonté et mérite une consultation."},
}
