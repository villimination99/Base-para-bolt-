# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · el registro y la respiración pautada
==========================================================
El ejemplo de entrada del cuaderno —«12/04, 4 de 6, prisa y sueño, se me
apretó el estómago al leer el mensaje de M.»— es deliberadamente feo, y así se
traduce. El párrafo acaba de decir que las entradas útiles son cortas, feas y
precisas; una versión pulida en inglés o en francés desmentiría la frase que
la introduce. La fecha se escribe con el orden de cada lengua y la inicial del
nombre se queda en M., que es lo que uno escribe cuando escribe rápido.
"""

T = {
    "Al principio no te acordarás, y no es un problema de voluntad: es que estar ausente es "
    "precisamente el estado que impide recordar que hay que mirar. Usa anclas externas sin "
    "ningún pudor: una alarma, una pegatina en el marco de la puerta, el gesto de lavarse "
    "las manos. Con las semanas el ancla se vuelve innecesaria; al principio es "
    "indispensable.": {
        "en": "At first you will not remember, and it is not a problem of will: being absent "
              "is precisely the state that prevents you from remembering to look. Use external "
              "anchors without any embarrassment: an alarm, a sticker on the door frame, the "
              "act of washing your hands. Over the weeks the anchor becomes unnecessary; at "
              "the start it is indispensable.",
        "fr": "Au début vous ne vous en souviendrez pas, et ce n'est pas un problème de "
              "volonté : être absent est précisément l'état qui empêche de se rappeler qu'il "
              "faut regarder. Servez-vous d'ancres extérieures sans aucune gêne : une alarme, "
              "un autocollant sur le chambranle, le geste de se laver les mains. Au fil des "
              "semaines l'ancre devient inutile ; au début elle est indispensable."},

    # ── El registro ────────────────────────────────────────────────────────
    "Marco Aurelio escribió las «Meditaciones» sin intención de publicarlas: son las notas "
    "de un hombre observándose por escrito durante años. Es el mejor ejemplo conservado de "
    "lo que este capítulo pide, y no es casualidad que sea también el texto que mejor ha "
    "resistido dieciocho siglos.": {
        "en": "Marcus Aurelius wrote the «Meditations» with no intention of publishing them: "
              "they are the notes of a man observing himself in writing over years. It is the "
              "best surviving example of what this chapter asks for, and it is no coincidence "
              "that it is also the text that has best withstood eighteen centuries.",
        "fr": "Marc Aurèle a écrit les « Pensées » sans intention de les publier : ce sont les "
              "notes d'un homme qui s'observe par écrit pendant des années. C'est le meilleur "
              "exemple conservé de ce que demande ce chapitre, et ce n'est pas un hasard si "
              "c'est aussi le texte qui a le mieux résisté à dix-huit siècles."},

    "Por qué por escrito y no mentalmente": {
        "en": "Why in writing and not in your head",
        "fr": "Pourquoi par écrit et non mentalement"},

    "Porque la memoria de los estados internos reescribe. Sin registro, a los diez días "
    "recuerdas la versión que te conviene.": {
        "en": "Because memory for inner states rewrites. Without a record, after ten days you "
              "remember the version that suits you.",
        "fr": "Parce que la mémoire des états intérieurs réécrit. Sans relevé, au bout de dix "
              "jours vous vous rappelez la version qui vous arrange."},

    "Porque escribir obliga a concretar. Un estado difuso no se puede poner en una línea, y "
    "el esfuerzo de ponerlo en una línea es la mitad del trabajo.": {
        "en": "Because writing forces you to be specific. A diffuse state cannot be put into "
              "one line, and the effort of putting it into one line is half the work.",
        "fr": "Parce qu'écrire oblige à préciser. Un état flou ne peut pas se mettre en une "
              "ligne, et l'effort de le mettre en une ligne est la moitié du travail."},

    "Porque solo lo escrito se puede comparar. El valor del cuaderno no está en la entrada "
    "de hoy: está en releer tres meses juntos y ver el patrón que ninguna entrada "
    "individual mostraba.": {
        "en": "Because only what is written can be compared. The notebook's value is not in "
              "today's entry: it is in rereading three months together and seeing the pattern "
              "no individual entry showed.",
        "fr": "Parce que seul ce qui est écrit peut se comparer. La valeur du carnet n'est pas "
              "dans l'entrée d'aujourd'hui : elle est dans la relecture de trois mois d'un "
              "coup et dans le schéma qu'aucune entrée isolée ne montrait."},

    "Porque el papel no discute. Es el único sitio donde se puede ser completamente sincero "
    "sin consecuencias, y esa es una posibilidad rara.": {
        "en": "Because paper does not argue. It is the only place where you can be completely "
              "sincere with no consequences, and that is a rare possibility.",
        "fr": "Parce que le papier ne discute pas. C'est le seul endroit où l'on peut être "
              "complètement sincère sans conséquences, et c'est une possibilité rare."},

    "Entrada diaria mínima": {
        "en": "Minimum daily entry", "fr": "Entrée quotidienne minimale"},

    "Fecha": {"en": "Date", "fr": "Date"},
    "Y la hora en que escribes": {
        "en": "And the time at which you write", "fr": "Et l'heure à laquelle vous écrivez"},

    "Los seis recuerdos": {"en": "The six recollections", "fr": "Les six rappels"},
    "Cuántos de los seis hiciste. El número, sin excusas al lado": {
        "en": "How many of the six you did. The number, with no excuses beside it",
        "fr": "Combien des six vous avez faits. Le nombre, sans excuses à côté"},

    "Estados del día": {"en": "States of the day", "fr": "États de la journée"},
    "Dos o tres palabras. Solo las etiquetas": {
        "en": "Two or three words. Only the labels",
        "fr": "Deux ou trois mots. Seulement les étiquettes"},

    "Una reacción observada": {
        "en": "One observed reaction", "fr": "Une réaction observée"},
    "Qué la disparó y dónde la notaste en el cuerpo. Una línea": {
        "en": "What set it off and where in the body you noticed it. One line",
        "fr": "Ce qui l'a déclenchée et où vous l'avez sentie dans le corps. Une ligne"},

    "Lo que no quiero escribir": {
        "en": "What I do not want to write", "fr": "Ce que je ne veux pas écrire"},
    "El campo más útil de los cinco. Se deja en blanco muchos días y los días que se rellena "
    "valen la semana entera": {
        "en": "The most useful field of the five. It is left blank many days, and the days it "
              "gets filled in are worth the whole week",
        "fr": "Le champ le plus utile des cinq. On le laisse vide bien des jours, et les jours "
              "où il se remplit valent la semaine entière"},

    "La tentación de escribir bien arruina el registro. Las entradas útiles son cortas, feas "
    "y precisas. «12/04, 4 de 6, prisa y sueño, se me apretó el estómago al leer el mensaje "
    "de M.» Eso, cien veces, revela más que cualquier página elegante — y además se "
    "sostiene, que es la otra ventaja de escribir poco.": {
        "en": "The temptation to write well ruins the record. Useful entries are short, ugly "
              "and precise. «12/04, 4 of 6, hurry and sleepiness, stomach tightened on reading "
              "M.'s message.» That, a hundred times over, reveals more than any elegant page — "
              "and it also lasts, which is the other advantage of writing little.",
        "fr": "La tentation de bien écrire ruine le relevé. Les entrées utiles sont courtes, "
              "laides et précises. « 12/04, 4 sur 6, hâte et sommeil, l'estomac s'est serré en "
              "lisant le message de M. » Cela, cent fois, révèle plus que n'importe quelle page "
              "élégante — et en plus cela tient, ce qui est l'autre avantage d'écrire peu."},

    "La revisión, donde está el valor": {
        "en": "The review, where the value lies",
        "fr": "La révision, où se trouve la valeur"},

    "Cada domingo: relee la semana. Diez minutos. Cuenta los recuerdos hechos y busca qué "
    "día falló y por qué.": {
        "en": "Every Sunday: reread the week. Ten minutes. Count the recollections done and "
              "look for which day failed and why.",
        "fr": "Chaque dimanche : relisez la semaine. Dix minutes. Comptez les rappels faits et "
              "cherchez quel jour a manqué et pourquoi."},
    "Cada mes: relee el mes y escribe cinco líneas. Qué estado se repite, qué disparador se "
    "repite, qué has dejado de anotar.": {
        "en": "Every month: reread the month and write five lines. Which state repeats, which "
              "trigger repeats, what you have stopped writing down.",
        "fr": "Chaque mois : relisez le mois et écrivez cinq lignes. Quel état se répète, quel "
              "déclencheur se répète, ce que vous avez cessé de noter."},
    "Cada tres meses: relee el trimestre y escribe media página. Aquí es donde aparece lo "
    "que ninguna semana muestra.": {
        "en": "Every three months: reread the quarter and write half a page. This is where "
              "what no single week shows appears.",
        "fr": "Tous les trois mois : relisez le trimestre et écrivez une demi-page. C'est ici "
              "qu'apparaît ce qu'aucune semaine ne montre."},
    "Cada año: relee el año. Es la práctica más incómoda del libro y la que más enseña. "
    "Reserva una tarde.": {
        "en": "Every year: reread the year. It is the most uncomfortable practice in the book "
              "and the one that teaches most. Set an afternoon aside.",
        "fr": "Chaque année : relisez l'année. C'est la pratique la plus inconfortable du livre "
              "et celle qui enseigne le plus. Réservez-y un après-midi."},

    # ── La respiración pautada ─────────────────────────────────────────────
    "La respiración es el único proceso que funciona solo y que además se puede gobernar a "
    "voluntad, y eso la convierte en la puerta más práctica al estado del cuerpo. Dos "
    "pautas bastan para todo lo que este libro propone.": {
        "en": "Breathing is the only process that runs by itself and can also be governed at "
              "will, and that makes it the most practical door into the state of the body. Two "
              "patterns are enough for everything this book proposes.",
        "fr": "La respiration est le seul processus qui fonctionne tout seul et que l'on peut "
              "en outre gouverner à volonté, ce qui en fait la porte la plus pratique vers "
              "l'état du corps. Deux cadences suffisent pour tout ce que propose ce livre."},

    '<span class="fig-n">Lám. 5</span> Las dos pautas, con la duración relativa de cada '
    "tramo. Se cuenta a un tiempo por segundo, sin forzar.": {
        "en": '<span class="fig-n">Pl. 5</span> The two patterns, with the relative duration '
              "of each stretch. You count at one beat per second, without forcing.",
        "fr": '<span class="fig-n">Pl. 5</span> Les deux cadences, avec la durée relative de '
              "chaque temps. On compte un temps par seconde, sans forcer."},
}
