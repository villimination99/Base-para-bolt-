# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · las cuatro fórmulas y la tabla de las horas
========================================================================
Las cuatro fórmulas se vuelven a silabear para cada lengua, que es justamente
lo que el capítulo anterior anuncia: se dan en la grafía del lector para que
pueda pronunciarlas sin saber hebreo. IE-VE-HÚ es YEH-VEH-HOO en inglés y
IÉ-VÉ-HOU en francés; A-DO-NÁI es AH-DOH-NYE y A-DO-NAÏ. Las glosas —«el que
es», «mi señor»— sí se traducen, porque son significados y no sonidos.

La demostración del orden de la semana se traduce con sus números: la hora 24,
la 25, el domingo que empieza en el Sol y el lunes que empieza en la Luna. Es
una comprobación que el generador hace antes de dibujar la lámina y que el
lector puede rehacer con el dedo sobre la tabla.
"""

T = {
    "IE-VE-HÚ · «el que es». Cuatro sílabas abiertas, muy cómoda de sostener.": {
        "en": "YEH-VEH-HOO · «the one who is». Four open syllables, very comfortable to "
              "sustain.",
        "fr": "IÉ-VÉ-HOU · « celui qui est ». Quatre syllabes ouvertes, très confortable à "
              "tenir."},

    "EL-O-HÍM · plural que se traduce en singular; la tradición lo asocia al poder.": {
        "en": "EL-O-HEEM · a plural translated in the singular; the tradition associates it "
              "with power.",
        "fr": "EL-O-HIM · un pluriel qui se traduit au singulier ; la tradition l'associe à la "
              "puissance."},

    "EL · la más breve de las cuatro; se sostiene en una sola nota larga.": {
        "en": "EL · the shortest of the four; it is sustained on a single long note.",
        "fr": "EL · la plus brève des quatre ; elle se tient sur une seule note longue."},

    "A-DO-NÁI · «mi señor»; la que mejor resuena en el pecho de las cuatro.": {
        "en": "AH-DOH-NYE · «my lord»; the one of the four that resonates best in the chest.",
        "fr": "A-DO-NAÏ · « mon seigneur » ; celle des quatre qui résonne le mieux dans la "
              "poitrine."},

    "La técnica, paso a paso": {
        "en": "The technique, step by step", "fr": "La technique, pas à pas"},

    "De pie, hombros bajos, mandíbula suelta. La postura importa más que el volumen.": {
        "en": "Standing, shoulders down, jaw loose. Posture matters more than volume.",
        "fr": "Debout, épaules basses, mâchoire relâchée. La posture compte plus que le volume."},

    "Inhala por la nariz contando hasta cuatro, llenando el abdomen antes que el pecho.": {
        "en": "Breathe in through the nose to a count of four, filling the abdomen before the "
              "chest.",
        "fr": "Inspirez par le nez en comptant jusqu'à quatre, en remplissant l'abdomen avant "
              "la poitrine."},

    "Vocaliza la fórmula en voz baja y grave, repartiendo las sílabas por toda la "
    "exhalación. No se grita: se sostiene. Si al terminar te falta el aire bruscamente, has "
    "ido demasiado rápido.": {
        "en": "Vocalise the formula low and deep, spreading the syllables across the whole "
              "exhalation. You do not shout: you sustain. If you run abruptly out of air at "
              "the end, you went too fast.",
        "fr": "Vocalisez la formule à voix basse et grave, en répartissant les syllabes sur "
              "toute l'expiration. On ne crie pas : on tient. Si l'air vous manque brusquement "
              "à la fin, vous êtes allé trop vite."},

    "Deja un segundo de silencio con los pulmones vacíos antes de volver a inhalar. Ese "
    "silencio es parte de la fórmula.": {
        "en": "Leave a second of silence with the lungs empty before breathing in again. That "
              "silence is part of the formula.",
        "fr": "Laissez une seconde de silence les poumons vides avant de réinspirer. Ce silence "
              "fait partie de la formule."},

    "Repite tres veces por cuarto en las operaciones diarias; siete en las operaciones "
    "largas. Nunca más de siete seguidas: la hiperventilación no es un estado alterado, es "
    "un mareo.": {
        "en": "Repeat three times per quarter in daily operations; seven in long operations. "
              "Never more than seven in a row: hyperventilation is not an altered state, it is "
              "dizziness.",
        "fr": "Répétez trois fois par quartier dans les opérations quotidiennes ; sept dans les "
              "opérations longues. Jamais plus de sept d'affilée : l'hyperventilation n'est pas "
              "un état modifié, c'est un vertige."},

    "Aviso concreto": {"en": "A specific warning", "fr": "Avertissement concret"},

    "Si notas hormigueo en las manos o alrededor de la boca, sensación de irrealidad o "
    "mareo, para inmediatamente y respira normal. Son signos de hiperventilación, no de "
    "progreso. Si estás embarazada, tienes epilepsia, hipertensión no controlada o un "
    "trastorno de pánico, consulta antes con tu médico: los ejercicios respiratorios "
    "intensos no son inocuos en esas condiciones.": {
        "en": "If you notice tingling in the hands or around the mouth, a sense of unreality "
              "or dizziness, stop immediately and breathe normally. They are signs of "
              "hyperventilation, not of progress. If you are pregnant, have epilepsy, "
              "uncontrolled high blood pressure or a panic disorder, consult your doctor "
              "first: intense breathing exercises are not harmless in those conditions.",
        "fr": "Si vous remarquez des fourmillements dans les mains ou autour de la bouche, une "
              "sensation d'irréalité ou un vertige, arrêtez immédiatement et respirez "
              "normalement. Ce sont des signes d'hyperventilation, non de progrès. Si vous êtes "
              "enceinte, épileptique, hypertendue non contrôlée ou sujette au trouble panique, "
              "consultez d'abord votre médecin : les exercices respiratoires intenses ne sont "
              "pas anodins dans ces conditions."},

    # ── La tabla de las horas ──────────────────────────────────────────────
    "El capítulo 11 explicó el sistema de horas y dio el reparto de los siete días. Aquí va "
    "la tabla entera: ciento sesenta y ocho casillas, las veinticuatro horas de cada uno de "
    "los siete días con su regente. No la he encontrado impresa completa en ningún manual "
    "moderno, y es la pieza que convierte el sistema de una curiosidad en una herramienta "
    "utilizable.": {
        "en": "Chapter 11 explained the system of hours and gave the distribution of the seven "
              "days. Here is the whole table: one hundred and sixty-eight cells, the "
              "twenty-four hours of each of the seven days with their ruler. I have not found "
              "it printed in full in any modern manual, and it is the piece that turns the "
              "system from a curiosity into a usable tool.",
        "fr": "Le chapitre 11 a expliqué le système des heures et donné la répartition des sept "
              "jours. Voici la table entière : cent soixante-huit cases, les vingt-quatre "
              "heures de chacun des sept jours avec leur régent. Je ne l'ai trouvée imprimée en "
              "entier dans aucun manuel moderne, et c'est la pièce qui fait passer le système "
              "de la curiosité à l'outil utilisable."},

    '<span class="fig-n">Lám. 7</span> Las 168 horas planetarias. Cada fila es un día; cada '
    "casilla, una hora desde el amanecer. La línea vertical separa las doce horas de día de "
    "las doce de noche. En destacado, las cuatro horas de cada día que pertenecen al planeta "
    "que le da nombre.": {
        "en": '<span class="fig-n">Pl. 7</span> The 168 planetary hours. Each row is a day; '
              "each cell, one hour from dawn. The vertical line separates the twelve daytime "
              "hours from the twelve of night. Highlighted, the four hours of each day that "
              "belong to the planet the day is named after.",
        "fr": '<span class="fig-n">Pl. 7</span> Les 168 heures planétaires. Chaque ligne est un '
              "jour ; chaque case, une heure depuis l'aube. La ligne verticale sépare les douze "
              "heures de jour des douze de nuit. En surbrillance, les quatre heures de chaque "
              "jour qui appartiennent à la planète qui lui donne son nom."},

    "Cómo leerla": {"en": "How to read it", "fr": "Comment la lire"},

    "Localiza tu día en la columna de la izquierda.": {
        "en": "Find your day in the left-hand column.",
        "fr": "Repérez votre jour dans la colonne de gauche."},

    "Cuenta las horas desde el amanecer, no desde medianoche. La hora 1 empieza cuando sale "
    "el Sol; la hora 13, cuando se pone.": {
        "en": "Count the hours from dawn, not from midnight. Hour 1 begins when the Sun rises; "
              "hour 13, when it sets.",
        "fr": "Comptez les heures depuis l'aube, non depuis minuit. L'heure 1 commence au lever "
              "du Soleil ; l'heure 13, à son coucher."},

    "Recuerda que no son horas de sesenta minutos. Divide la duración real del día entre "
    "doce y la de la noche entre doce: en verano las diurnas son largas y las nocturnas "
    "cortas, y al contrario en invierno. Solo coinciden en los equinoccios.": {
        "en": "Remember they are not sixty-minute hours. Divide the real length of the day by "
              "twelve and that of the night by twelve: in summer the daytime ones are long and "
              "the night ones short, and the other way round in winter. They coincide only at "
              "the equinoxes.",
        "fr": "Rappelez-vous que ce ne sont pas des heures de soixante minutes. Divisez la "
              "durée réelle du jour par douze et celle de la nuit par douze : en été les "
              "diurnes sont longues et les nocturnes courtes, et l'inverse en hiver. Elles ne "
              "coïncident qu'aux équinoxes."},

    "Las casillas destacadas son las horas del regente del día. Son cuatro por día —la 1, la "
    "8, la 15 y la 22— y son el momento clásico para la operación de ese planeta.": {
        "en": "The highlighted cells are the hours of the day's ruler. There are four per day "
              "—the 1st, the 8th, the 15th and the 22nd— and they are the classical moment for "
              "that planet's operation.",
        "fr": "Les cases en surbrillance sont les heures du régent du jour. Il y en a quatre "
              "par jour —la 1, la 8, la 15 et la 22— et c'est le moment classique de "
              "l'opération de cette planète."},

    "El dato que la tabla demuestra sola": {
        "en": "The fact the table proves on its own",
        "fr": "Le fait que la table démontre toute seule"},

    "Mira la primera casilla de cada fila y luego cuenta veinticuatro. La casilla "
    "veinticinco —que es la primera del día siguiente— cae siempre en el regente del día "
    "siguiente. Domingo empieza en el Sol, su hora 24 es Mercurio, y la 25 es la Luna: "
    "lunes. Esa es toda la explicación del orden de la semana, y la tabla la contiene sin "
    "necesidad de argumentarla. El generador de esta lámina comprueba precisamente eso antes "
    "de dibujarla: si la hora 25 no cayera donde tiene que caer, se negaría a escribir el "
    "fichero.": {
        "en": "Look at the first cell of each row and then count twenty-four. The "
              "twenty-fifth cell —which is the first of the following day— always falls on the "
              "following day's ruler. Sunday begins with the Sun, its hour 24 is Mercury, and "
              "the 25th is the Moon: Monday. That is the whole explanation of the order of the "
              "week, and the table contains it without needing to argue it. The generator of "
              "this plate checks precisely that before drawing it: if hour 25 did not fall "
              "where it must, it would refuse to write the file.",
        "fr": "Regardez la première case de chaque ligne puis comptez vingt-quatre. La "
              "vingt-cinquième case —qui est la première du jour suivant— tombe toujours sur le "
              "régent du jour suivant. Le dimanche commence au Soleil, son heure 24 est "
              "Mercure, et la 25 est la Lune : lundi. Voilà toute l'explication de l'ordre de "
              "la semaine, et la table la contient sans avoir à l'argumenter. Le générateur de "
              "cette planche vérifie précisément cela avant de la dessiner : si l'heure 25 ne "
              "tombait pas où elle doit, il refuserait d'écrire le fichier."},

    "Por qué las cuatro horas propias están donde están": {
        "en": "Why the four proper hours are where they are",
        "fr": "Pourquoi les quatre heures propres sont là où elles sont"},

    "Porque siete no divide a veinticuatro. Si el ciclo caldeo tiene siete puestos y el día "
    "tiene veinticuatro horas, el regente del día vuelve a tocar en la hora 1, la 8, la 15 y "
    "la 22 —de siete en siete—, y la 24 cae siempre dos puestos antes de cerrar la vuelta. "
    "Toda la irregularidad aparente del sistema viene de ese resto de tres, y una vez visto "
    "ya no se olvida.": {
        "en": "Because seven does not divide twenty-four. If the Chaldean cycle has seven "
              "places and the day has twenty-four hours, the day's ruler comes round again at "
              "hour 1, hour 8, hour 15 and hour 22 —every seven— and hour 24 always falls two "
              "places short of closing the round. All the system's apparent irregularity comes "
              "from that remainder of three, and once seen it is not forgotten.",
        "fr": "Parce que sept ne divise pas vingt-quatre. Si le cycle chaldéen a sept places et "
              "que le jour a vingt-quatre heures, le régent du jour revient à l'heure 1, à la "
              "8, à la 15 et à la 22 —de sept en sept— et la 24 tombe toujours deux places "
              "avant de boucler le tour. Toute l'irrégularité apparente du système vient de ce "
              "reste de trois, et une fois vu cela ne s'oublie plus."},

    "Las cuatro horas propias de cada día": {
        "en": "The four proper hours of each day",
        "fr": "Les quatre heures propres de chaque jour"},

    "Hora 1": {"en": "Hour 1", "fr": "Heure 1"},
    "Al amanecer. La más usada de las cuatro y la más fácil de situar sin cálculo.": {
        "en": "At dawn. The most used of the four and the easiest to locate without "
              "calculation.",
        "fr": "À l'aube. La plus employée des quatre et la plus facile à situer sans calcul."},
}
