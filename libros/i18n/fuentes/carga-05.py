# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · progresión y los ocho patrones en prosa
============================================================
Los nombres de los patrones aparecen aquí en minúscula y dentro de una frase,
mientras que en la lámina van en versales y solos. Son segmentos distintos y
llevan traducción distinta a propósito: en la lámina manda el ancho del
recuadro y aquí manda la frase. Lo que sí coincide es el término elegido, para
que quien mire la ilustración y luego lea el capítulo reconozca el mismo
movimiento.
"""

T = {
    "Hombros": {"en": "Shoulders", "fr": "Épaules"},
    "Press por encima de la cabeza, elevaciones": {
        "en": "Overhead press, raises", "fr": "Développé au-dessus de la tête, élévations"},

    "Brazos": {"en": "Arms", "fr": "Bras"},
    "Curl, extensión de tríceps. Reciben mucho trabajo indirecto: son los que menos "
    "atención específica necesitan": {
        "en": "Curl, triceps extension. They get a lot of indirect work: they are the ones "
              "that need the least specific attention",
        "fr": "Curl, extension des triceps. Ils reçoivent beaucoup de travail indirect : ce "
              "sont eux qui ont le moins besoin d'attention spécifique"},

    "Abdomen y tronco": {"en": "Abdomen and trunk", "fr": "Abdomen et tronc"},
    "Plancha, antirrotaciones, cargadas y transportes": {
        "en": "Plank, anti-rotation work, loaded carries",
        "fr": "Gainage, antirotations, chargements et portés"},

    "El material es indiferente. Las guías no distinguen entre barra, mancuerna, máquina, "
    "banda elástica o peso corporal: lo que cuenta es que el músculo trabaje contra una "
    "resistencia que suponga un esfuerzo real. Quien no pisa un gimnasio puede cumplir la "
    "recomendación entera en el suelo de su casa, y esa es una información que la "
    "industria del fitness no tiene ningún incentivo en difundir.": {
        "en": "The equipment is beside the point. The guidelines draw no distinction between "
              "barbell, dumbbell, machine, resistance band or body weight: what counts is "
              "that the muscle works against a resistance that represents a real effort. "
              "Someone who never sets foot in a gym can meet the whole recommendation on the "
              "floor at home, and that is a piece of information the fitness industry has no "
              "incentive to spread.",
        "fr": "Le matériel est indifférent. Les recommandations ne distinguent pas entre "
              "barre, haltère, machine, élastique ou poids de corps : ce qui compte, c'est "
              "que le muscle travaille contre une résistance qui représente un effort réel. "
              "Qui ne met jamais les pieds dans une salle peut satisfaire toute la "
              "recommandation par terre chez lui, et c'est une information que l'industrie "
              "du fitness n'a aucun intérêt à diffuser."},

    "La única variable que hay que respetar: la progresión": {
        "en": "The one variable you have to respect: progression",
        "fr": "La seule variable qu'il faut respecter : la progression"},

    "Un músculo se adapta a lo que se le exige, y deja de adaptarse cuando la exigencia "
    "deja de subir. La progresión no tiene que ser rápida ni constante, pero tiene que "
    "existir, y hay más de una manera de conseguirla:": {
        "en": "A muscle adapts to what is demanded of it, and stops adapting when the demand "
              "stops rising. Progression does not have to be fast or steady, but it has to "
              "exist, and there is more than one way of getting it:",
        "fr": "Un muscle s'adapte à ce qu'on lui demande, et cesse de s'adapter quand la "
              "demande cesse de monter. La progression n'a pas besoin d'être rapide ni "
              "régulière, mais elle doit exister, et il y a plus d'une façon de l'obtenir :"},

    "Más peso con las mismas repeticiones.": {
        "en": "More weight for the same repetitions.",
        "fr": "Plus de poids pour les mêmes répétitions."},
    "Más repeticiones con el mismo peso.": {
        "en": "More repetitions with the same weight.",
        "fr": "Plus de répétitions avec le même poids."},
    "Más series del mismo ejercicio.": {
        "en": "More sets of the same exercise.",
        "fr": "Plus de séries du même exercice."},
    "Mismo trabajo con menos descanso entre series.": {
        "en": "The same work with less rest between sets.",
        "fr": "Le même travail avec moins de repos entre les séries."},
    "Mismo trabajo con mejor técnica y más recorrido, que es la progresión que más se "
    "subestima y la que más rinde en los primeros meses.": {
        "en": "The same work with better technique and more range, which is the most "
              "underrated progression and the one that pays best in the first months.",
        "fr": "Le même travail avec une meilleure technique et plus d'amplitude, la "
              "progression la plus sous-estimée et celle qui rapporte le plus dans les "
              "premiers mois."},

    "Y una regla de sensatez que no está en ningún documento oficial pero que evita la "
    "mayoría de las lesiones de quien empieza: sube una variable cada vez, y sube poco. La "
    "prisa en las primeras semanas es la causa más común de parar en las siguientes, y "
    "parar cuesta mucho más que ir despacio.": {
        "en": "And a rule of common sense that is in no official document but that prevents "
              "most of the injuries of people starting out: raise one variable at a time, "
              "and raise it a little. Haste in the first weeks is the commonest cause of "
              "stopping in the following ones, and stopping costs far more than going slowly.",
        "fr": "Et une règle de bon sens qui ne figure dans aucun document officiel mais qui "
              "évite la plupart des blessures de qui débute : montez une variable à la fois, "
              "et montez peu. La précipitation des premières semaines est la cause la plus "
              "fréquente d'arrêt dans les suivantes, et s'arrêter coûte bien plus cher que "
              "d'aller lentement."},

    "Lo que dice la doctrina militar sobre esto": {
        "en": "What military doctrine says about this",
        "fr": "Ce qu'en dit la doctrine militaire"},

    "El manual de salud y preparación física del Ejército de Estados Unidos —publicado "
    "íntegro y descargable— organiza el entrenamiento en fases y dedica una cantidad "
    "notable de páginas a la progresión gradual y a la prevención de lesiones por "
    "sobreuso. Una institución que entrena a cientos de miles de personas a la vez no "
    "puede permitirse lesionarlas, y por eso su doctrina es bastante más conservadora que "
    "el discurso habitual del gimnasio. Merece leerse por eso.": {
        "en": "The United States Army's health and physical readiness manual —published in "
              "full and downloadable— organises training in phases and devotes a notable "
              "number of pages to gradual progression and to the prevention of overuse "
              "injuries. An institution that trains hundreds of thousands of people at once "
              "cannot afford to injure them, and that is why its doctrine is considerably "
              "more conservative than the usual gym talk. It is worth reading for that.",
        "fr": "Le manuel de santé et de préparation physique de l'armée des États-Unis "
              "—publié intégralement et téléchargeable— organise l'entraînement en phases et "
              "consacre un nombre notable de pages à la progression graduelle et à la "
              "prévention des blessures de surmenage. Une institution qui entraîne des "
              "centaines de milliers de personnes à la fois ne peut pas se permettre de les "
              "blesser, et c'est pourquoi sa doctrine est nettement plus prudente que le "
              "discours habituel des salles. Elle mérite d'être lue pour cela."},

    # ── Los ocho patrones ──────────────────────────────────────────────────
    "Un programa de fuerza no se organiza por músculos: se organiza por patrones de "
    "movimiento. Son ocho, cubren todo lo que un cuerpo humano hace contra una "
    "resistencia, y una semana que los toca todos no deja huecos por definición. Es la "
    "manera más rápida de auditar cualquier plan, incluido uno que te vendan.": {
        "en": "A strength programme is not organised by muscles: it is organised by movement "
              "patterns. There are eight, they cover everything a human body does against a "
              "resistance, and a week that touches them all leaves no gaps by definition. It "
              "is the quickest way to audit any plan, including one being sold to you.",
        "fr": "Un programme de force ne s'organise pas par muscles : il s'organise par "
              "schémas de mouvement. Ils sont huit, ils couvrent tout ce qu'un corps humain "
              "fait contre une résistance, et une semaine qui les touche tous ne laisse "
              "aucun trou par définition. C'est la façon la plus rapide d'auditer n'importe "
              "quel plan, y compris celui qu'on vous vend."},

    '<span class="fig-n">Los ocho patrones y una opción para cada uno</span> Organizados '
    "por lo que hace la articulación y no por el músculo que se quiere «trabajar». "
    "Cualquier ejercicio conocido cae en uno de los ocho, y si tu semana deja alguno "
    "vacío, ahí está tu hueco.": {
        "en": '<span class="fig-n">The eight patterns and one option for each</span> '
              "Organised by what the joint does and not by the muscle you want to «work». "
              "Any exercise you know of falls into one of the eight, and if your week leaves "
              "one of them empty, there is your gap.",
        "fr": '<span class="fig-n">Les huit schémas et une option pour chacun</span> '
              "Organisés selon ce que fait l'articulation et non selon le muscle que l'on "
              "veut « travailler ». N'importe quel exercice connu tombe dans l'un des huit, "
              "et si votre semaine en laisse un vide, votre trou est là."},

    "Los ocho, con ejemplos": {
        "en": "The eight, with examples", "fr": "Les huit, avec des exemples"},

    "Sentadilla": {"en": "Squat", "fr": "Squat"},
    "Rodilla y cadera flexionan juntas · Sentadilla, prensa, zancada, subir escalón": {
        "en": "Knee and hip bend together · Squat, leg press, lunge, step-up",
        "fr": "Genou et hanche fléchissent ensemble · Squat, presse, fente, montée sur banc"},

    "Bisagra de cadera": {"en": "Hip hinge", "fr": "Charnière de hanche"},
    "La cadera manda y la rodilla apenas se dobla · Peso muerto, buenos días, empuje de "
    "cadera, balanceo": {
        "en": "The hip leads and the knee barely bends · Deadlift, good morning, hip thrust, "
              "swing",
        "fr": "La hanche commande et le genou fléchit à peine · Soulevé de terre, good "
              "morning, hip thrust, swing"},

    "Empuje horizontal": {"en": "Horizontal push", "fr": "Poussée horizontale"},
    "Alejar peso del pecho · Press de banca, flexiones, fondos": {
        "en": "Pushing weight away from the chest · Bench press, push-ups, dips",
        "fr": "Éloigner le poids de la poitrine · Développé couché, pompes, dips"},

    "Empuje vertical": {"en": "Vertical push", "fr": "Poussée verticale"},
    "Llevar peso por encima de la cabeza · Press militar, press con mancuernas": {
        "en": "Taking weight above the head · Overhead press, dumbbell press",
        "fr": "Porter le poids au-dessus de la tête · Développé militaire, développé "
              "haltères"},

    "Tirón horizontal": {"en": "Horizontal pull", "fr": "Tirage horizontal"},
    "Traer peso hacia el tronco · Remo con barra, remo con mancuerna, remo invertido": {
        "en": "Drawing weight towards the torso · Barbell row, dumbbell row, inverted row",
        "fr": "Amener le poids vers le tronc · Rowing barre, rowing haltère, rowing inversé"},
}
