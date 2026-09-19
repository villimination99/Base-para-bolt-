# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · custodios, cierre y la operación planetaria
========================================================================
La fórmula de los custodios va partida en cinco <span>, como la del eje, y se
traduce igual: renglón a renglón, con el corte donde está. Los cuatro primeros
sitúan una función en una dirección y el quinto se queda en el centro; el
orden es el del giro y no puede alterarse.

El calendario del primer mes describe cuatro semanas con su estado
característico. Se traduce sin suavizar la segunda —el aburrimiento y el tramo
donde se abandona— porque es la que evita que el lector crea que le pasa algo
raro.
"""

T = {
    "Entre un cuarto y el siguiente el brazo se mantiene extendido, trazando con los dedos "
    "una línea a la altura del hombro mientras se camina. No se bajan los brazos hasta haber "
    "cerrado el cuarto círculo en el este. Suena a manía y no lo es: mantener el brazo "
    "extendido es lo que impide que el recorrido se convierta en cuatro gestos sueltos.": {
        "en": "Between one quarter and the next the arm stays extended, tracing a line at "
              "shoulder height with the fingers as you walk. You do not lower your arms until "
              "you have closed the fourth circle in the east. It sounds like fussiness and it "
              "is not: keeping the arm extended is what stops the round from turning into four "
              "loose gestures.",
        "fr": "Entre un quartier et le suivant, le bras reste tendu, traçant des doigts une "
              "ligne à hauteur d'épaule pendant qu'on marche. On ne baisse pas les bras avant "
              "d'avoir fermé le quatrième cercle à l'est. Cela a l'air d'une manie et n'en est "
              "pas une : garder le bras tendu est ce qui empêche le parcours de devenir quatre "
              "gestes épars."},

    "Movimiento tercero · Los cuatro custodios": {
        "en": "Third movement · The four guardians",
        "fr": "Troisième mouvement · Les quatre gardiens"},

    "Vuelto al centro y mirando al este, brazos extendidos en cruz. Se nombra cada función "
    "en su sitio, sin girar, dejando un par de segundos entre una y otra.": {
        "en": "Back at the centre and facing east, arms extended in a cross. Each function is "
              "named in its place, without turning, leaving a couple of seconds between one "
              "and the next.",
        "fr": "Revenu au centre et face à l'est, les bras étendus en croix. On nomme chaque "
              "fonction à sa place, sans tourner, en laissant deux secondes entre l'une et "
              "l'autre."},

    "<span>Delante de mí, el aliento: lo que respiro y lo que digo.</span><span>A mi "
    "derecha, la voluntad: lo que decido y sostengo.</span><span>Detrás de mí, la memoria: "
    "lo que siento y lo que recuerdo.</span><span>A mi izquierda, el cuerpo: lo que me "
    "sostiene y se cansa.</span><span>Y en el centro, quien mira las cuatro.</span>": {
        "en": "<span>Before me, the breath: what I breathe and what I say.</span><span>On my "
              "right, the will: what I decide and hold to.</span><span>Behind me, the memory: "
              "what I feel and what I remember.</span><span>On my left, the body: what holds "
              "me up and grows tired.</span><span>And at the centre, whoever looks at the "
              "four.</span>",
        "fr": "<span>Devant moi, le souffle : ce que je respire et ce que je dis.</span><span>À "
              "ma droite, la volonté : ce que je décide et ce que je tiens.</span><span>Derrière "
              "moi, la mémoire : ce que je ressens et ce dont je me souviens.</span><span>À ma "
              "gauche, le corps : ce qui me soutient et se fatigue.</span><span>Et au centre, "
              "celui qui regarde les quatre.</span>"},

    "Qué son los custodios y qué no": {
        "en": "What the guardians are and what they are not",
        "fr": "Ce que sont les gardiens et ce qu'ils ne sont pas"},

    "No se está llamando a nadie. Se está nombrando en voz alta y en un orden fijo las "
    "cuatro funciones del propio operante, situándolas en el espacio para poder mirarlas de "
    "una en una. Es un inventario, y hacerlo en voz alta y de pie funciona mucho mejor que "
    "hacerlo pensando, por la misma razón por la que una lista escrita funciona mejor que "
    "una lista recordada.": {
        "en": "Nobody is being called. What is being done is naming aloud and in a fixed order "
              "the operator's own four functions, placing them in space so that they can be "
              "looked at one at a time. It is an inventory, and doing it aloud and standing "
              "works far better than doing it by thinking, for the same reason a written list "
              "works better than a remembered one.",
        "fr": "On n'appelle personne. On nomme à voix haute et dans un ordre fixe les quatre "
              "fonctions de l'opérant lui-même, en les situant dans l'espace pour pouvoir les "
              "regarder une à une. C'est un inventaire, et le faire à voix haute et debout "
              "fonctionne bien mieux que de le faire en pensant, pour la même raison qu'une "
              "liste écrite fonctionne mieux qu'une liste mémorisée."},

    "Movimiento cuarto · El cierre": {
        "en": "Fourth movement · The closing",
        "fr": "Quatrième mouvement · La clôture"},

    "Se repite el movimiento del eje, exactamente igual que al principio, y se termina con "
    "las manos juntas al pecho y tres respiraciones completas. Después se camina el círculo "
    "en sentido contrario a las agujas del reloj, una vuelta, y se sale.": {
        "en": "The movement of the axis is repeated, exactly as at the beginning, and it ends "
              "with the hands together at the chest and three full breaths. Then you walk the "
              "circle anticlockwise, one turn, and you step out.",
        "fr": "On répète le mouvement de l'axe, exactement comme au début, et on termine les "
              "mains jointes sur la poitrine et trois respirations complètes. Ensuite on marche "
              "le cercle dans le sens inverse des aiguilles d'une montre, un tour, et on sort."},

    "Y ya está. Entre siete y diez minutos, todos los días. La tentación de añadir cosas "
    "aparecerá la segunda semana: no le hagas caso hasta el mes.": {
        "en": "And that is it. Between seven and ten minutes, every day. The temptation to add "
              "things will appear in the second week: pay it no attention until the month is "
              "up.",
        "fr": "Et c'est tout. Entre sept et dix minutes, tous les jours. La tentation d'ajouter "
              "des choses apparaîtra la deuxième semaine : n'y prêtez pas attention avant le "
              "mois écoulé."},

    "Qué esperar del primer mes": {
        "en": "What to expect from the first month",
        "fr": "À quoi s'attendre le premier mois"},

    "Primera semana: torpeza y sensación de ridículo. Es lo normal y no significa nada. Se "
    "ejecuta igual.": {
        "en": "First week: clumsiness and a feeling of absurdity. That is normal and it means "
              "nothing. You carry it out anyway.",
        "fr": "Première semaine : maladresse et sentiment de ridicule. C'est normal et cela ne "
              "signifie rien. On l'exécute quand même."},

    "Segunda semana: la secuencia empieza a salir sin pensarla y aparece el aburrimiento. Es "
    "el tramo donde se abandona, y es el tramo que hay que atravesar.": {
        "en": "Second week: the sequence starts coming out without thinking about it and "
              "boredom appears. It is the stretch where people give up, and it is the stretch "
              "that has to be crossed.",
        "fr": "Deuxième semaine : la séquence commence à sortir sans y penser et l'ennui "
              "apparaît. C'est le tronçon où l'on abandonne, et c'est le tronçon qu'il faut "
              "traverser."},

    "Tercera semana: la primera señal real. Entrar en el sitio ya produce un cambio de "
    "estado antes de haber hecho nada. Eso es el condicionamiento funcionando, y es todo el "
    "efecto que el rito promete.": {
        "en": "Third week: the first real sign. Entering the place already produces a change "
              "of state before you have done anything. That is conditioning at work, and it is "
              "the whole effect the rite promises.",
        "fr": "Troisième semaine : le premier signe réel. Entrer dans le lieu produit déjà un "
              "changement d'état avant d'avoir rien fait. C'est le conditionnement qui "
              "fonctionne, et c'est tout l'effet que promet le rite."},

    "Cuarta semana: se nota cuándo falta. Ese es el indicador de que la práctica está "
    "instalada, y el momento de pasar al capítulo siguiente.": {
        "en": "Fourth week: you notice when it is missing. That is the indicator that the "
              "practice is installed, and the moment to move on to the next chapter.",
        "fr": "Quatrième semaine : on remarque quand il manque. C'est l'indicateur que la "
              "pratique est installée, et le moment de passer au chapitre suivant."},

    # ── La operación planetaria ────────────────────────────────────────────
    "Con el rito diario instalado, se puede trabajar sobre una función concreta. La "
    "operación planetaria es una sesión más larga —de veinte a treinta minutos— dedicada a "
    "una sola de las siete funciones, en su día, y con un objetivo escrito de antemano.": {
        "en": "With the daily rite installed, you can work on a specific function. The "
              "planetary operation is a longer session —twenty to thirty minutes— devoted to a "
              "single one of the seven functions, on its day, and with an objective written "
              "down beforehand.",
        "fr": "Le rite quotidien installé, on peut travailler sur une fonction précise. "
              "L'opération planétaire est une séance plus longue —de vingt à trente minutes— "
              "consacrée à une seule des sept fonctions, le jour qui lui revient, et avec un "
              "objectif écrit d'avance."},

    "La estructura de la sesión": {
        "en": "The structure of the session", "fr": "La structure de la séance"},

    "Rito diario completo. Sin excepción: es la apertura.": {
        "en": "The complete daily rite. Without exception: it is the opening.",
        "fr": "Le rite quotidien complet. Sans exception : c'est l'ouverture."},

    "Hexagrama del planeta en el este, con su sigilo trazado en el centro de la figura.": {
        "en": "The planet's hexagram in the east, with its sigil traced at the centre of the "
              "figure.",
        "fr": "L'hexagramme de la planète à l'est, avec son sceau tracé au centre de la figure."},

    "Vocalización del nombre del planeta, siete veces.": {
        "en": "Vocalisation of the planet's name, seven times.",
        "fr": "Vocalisation du nom de la planète, sept fois."},

    "El trabajo: veinte minutos sobre el asunto elegido, con el cuadrado del planeta y el "
    "diario delante.": {
        "en": "The work: twenty minutes on the chosen matter, with the planet's square and the "
              "journal in front of you.",
        "fr": "Le travail : vingt minutes sur l'affaire choisie, avec le carré de la planète et "
              "le journal devant soi."},

    "Cierre del hexagrama y rito diario otra vez, completo. La sesión no termina hasta "
    "esto.": {
        "en": "Closing of the hexagram and the daily rite again, complete. The session does "
              "not end until this is done.",
        "fr": "Clôture de l'hexagramme et rite quotidien de nouveau, complet. La séance ne se "
              "termine pas avant cela."},

    "Las siete operaciones": {
        "en": "The seven operations", "fr": "Les sept opérations"},

    "Una por función. La columna del objetivo es lo que se pone por escrito antes de "
    "empezar: sin objetivo escrito la sesión se convierte en divagación con velas.": {
        "en": "One per function. The objective column is what gets written down before "
              "starting: without a written objective the session turns into rambling by "
              "candlelight.",
        "fr": "Une par fonction. La colonne de l'objectif est ce que l'on met par écrit avant "
              "de commencer : sans objectif écrit, la séance se change en divagation à la "
              "bougie."},

    "Saturno · sábado": {"en": "Saturn · Saturday", "fr": "Saturne · samedi"},
    "Función": {"en": "Function", "fr": "Fonction"},
    "El límite y el cierre": {
        "en": "The limit and the closing", "fr": "La limite et la clôture"},
}
