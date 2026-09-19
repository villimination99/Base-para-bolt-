# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · volumen, repeticiones en reserva y el calentamiento
========================================================================
«Agujetas» tiene nombre propio en cada idioma y ninguno es una traducción
literal del otro: en inglés son el dolor muscular de aparición tardía y en
francés son las courbatures. Se usa el término corriente en cada lengua, no el
clínico, porque el capítulo trata precisamente de lo que la gente cree sobre
ellas.

El aviso del final —dolor que dura días, hinchazón marcada y orina oscura— se
traduce sin suavizar. Describe un cuadro que se consulta el mismo día, y una
redacción más amable lo convertiría en una recomendación más.
"""

T = {
    "El recorrido. Media sentadilla con el doble de peso no es más entrenamiento que una "
    "sentadilla completa con la mitad: es otro ejercicio, y bastante peor. La amplitud "
    "completa produce más adaptación en la parte del músculo que trabaja estirada, "
    "mantiene la movilidad de la articulación y, de paso, obliga a usar un peso honesto.": {
        "en": "Range of motion. A half squat with twice the weight is not more training than "
              "a full squat with half of it: it is a different exercise, and a considerably "
              "worse one. Full range produces more adaptation in the part of the muscle that "
              "works stretched, maintains the mobility of the joint and, along the way, "
              "forces you to use an honest weight.",
        "fr": "L'amplitude. Un demi-squat avec le double du poids n'est pas plus "
              "d'entraînement qu'un squat complet avec la moitié : c'est un autre exercice, "
              "et nettement moins bon. L'amplitude complète produit plus d'adaptation dans la "
              "partie du muscle qui travaille en étirement, entretient la mobilité de "
              "l'articulation et, au passage, oblige à utiliser un poids honnête."},

    "Es también la variable que más se sacrifica por vanidad, porque bajar el peso para "
    "completar el recorrido se siente como retroceder. No lo es. Es la única forma de que "
    "el número que apuntas signifique algo.": {
        "en": "It is also the variable most often sacrificed to vanity, because dropping the "
              "weight in order to complete the range feels like going backwards. It is not. "
              "It is the only way for the number you write down to mean anything.",
        "fr": "C'est aussi la variable que l'on sacrifie le plus par vanité, car baisser le "
              "poids pour faire l'amplitude complète donne l'impression de reculer. Ce n'en "
              "est pas une. C'est la seule façon pour que le chiffre que vous notez veuille "
              "dire quelque chose."},

    "La que casi nadie cuenta bien: el volumen": {
        "en": "The one almost nobody counts properly: volume",
        "fr": "Celle que presque personne ne compte bien : le volume"},

    "La cuenta que predice la ganancia de tamaño son las series efectivas por músculo y "
    "por semana, no el tiempo en el gimnasio ni el número de ejercicios. Una serie "
    "efectiva es la que se lleva cerca del fallo técnico: con cuatro o cinco repeticiones "
    "de margen sobrando, el estímulo es escaso por muchas series que se hagan.": {
        "en": "The count that predicts the gain in size is effective sets per muscle per "
              "week, not the time spent in the gym or the number of exercises. An effective "
              "set is one taken close to technical failure: with four or five repetitions of "
              "margin left over, the stimulus is thin however many sets are done.",
        "fr": "Le compte qui prédit le gain de taille, ce sont les séries efficaces par "
              "muscle et par semaine, pas le temps passé en salle ni le nombre d'exercices. "
              "Une série efficace est celle que l'on mène près de l'échec technique : avec "
              "quatre ou cinq répétitions de marge en trop, le stimulus est maigre quel que "
              "soit le nombre de séries."},

    "De ahí que una sesión de cuarenta y cinco minutos bien apretada rinda más que dos "
    "horas de deambular entre máquinas, y de ahí también que aumentar el volumen sin "
    "límite deje de funcionar: llega un punto en que lo que se añade no se recupera, y lo "
    "que no se recupera no adapta.": {
        "en": "Hence a tightly packed forty-five-minute session returns more than two hours "
              "of drifting between machines, and hence too that raising volume without limit "
              "stops working: a point arrives at which what is added is not recovered, and "
              "what is not recovered does not adapt.",
        "fr": "D'où le fait qu'une séance de quarante-cinq minutes bien serrée rapporte plus "
              "que deux heures d'errance entre les machines, et d'où le fait aussi "
              "qu'augmenter le volume sans limite cesse de fonctionner : arrive un point où "
              "ce que l'on ajoute ne se récupère pas, et ce qui ne se récupère pas n'adapte "
              "rien."},

    "La escala de esfuerzo, que resuelve el problema de los porcentajes": {
        "en": "The effort scale, which solves the percentage problem",
        "fr": "L'échelle d'effort, qui règle le problème des pourcentages"},

    "Programar por porcentaje del máximo exige conocer el máximo, y el máximo cambia con "
    "el sueño, el estrés y la semana. La alternativa práctica es puntuar cuántas "
    "repeticiones te quedaban en reserva al terminar la serie:": {
        "en": "Programming by percentage of the maximum requires knowing the maximum, and the "
              "maximum changes with sleep, with stress and with the week. The practical "
              "alternative is to score how many repetitions you had left in reserve when the "
              "set ended:",
        "fr": "Programmer en pourcentage du maximum exige de connaître le maximum, et le "
              "maximum change avec le sommeil, le stress et la semaine. L'alternative "
              "pratique consiste à noter combien de répétitions il vous restait en réserve à "
              "la fin de la série :"},

    "Repeticiones en reserva": {
        "en": "Repetitions in reserve", "fr": "Répétitions en réserve"},
    "No podías hacer ni una más. Se usa poco y con criterio": {
        "en": "You could not have done one more. Used sparingly and with judgement",
        "fr": "Vous ne pouviez pas en faire une de plus. À utiliser peu et à bon escient"},
    "La zona de trabajo de las series de fuerza y de tamaño": {
        "en": "The working zone for strength and size sets",
        "fr": "La zone de travail des séries de force et de taille"},
    "Estímulo válido y mucho menos coste de recuperación": {
        "en": "A valid stimulus at much less recovery cost",
        "fr": "Un stimulus valable pour un coût de récupération bien moindre"},
    "5 o más": {"en": "5 or more", "fr": "5 ou plus"},
    "Calentamiento, técnica o volumen de relleno": {
        "en": "Warm-up, technique or filler volume",
        "fr": "Échauffement, technique ou volume de remplissage"},

    "Con esta escala, un mal día se ajusta solo: el peso que hoy te deja a dos "
    "repeticiones puede ser menor que el de la semana pasada, y aun así la sesión ha sido "
    "correcta. Programar por porcentaje fijo obliga a fallar o a mentir.": {
        "en": "With this scale a bad day adjusts itself: the weight that leaves you two "
              "repetitions short today may be lower than last week's, and the session was "
              "still correct. Programming by a fixed percentage forces you either to fail or "
              "to lie.",
        "fr": "Avec cette échelle, un mauvais jour se règle tout seul : le poids qui vous "
              "laisse aujourd'hui à deux répétitions peut être inférieur à celui de la "
              "semaine passée, et la séance a tout de même été correcte. Programmer en "
              "pourcentage fixe oblige soit à échouer, soit à mentir."},

    "La regla de progresión que evita casi todo": {
        "en": "The progression rule that prevents almost everything",
        "fr": "La règle de progression qui évite presque tout"},

    "Una variable, un escalón, y sostenerlo dos o tres semanas antes de tocar otra. Si el "
    "rendimiento baja tres sesiones seguidas, o si aparece dolor articular, el escalón "
    "anterior era el bueno: se vuelve y se sostiene más tiempo. Bajar no es retroceder; es "
    "lo que hace posible seguir subiendo el año que viene.": {
        "en": "One variable, one step, and hold it for two or three weeks before touching "
              "another. If performance drops for three sessions running, or if joint pain "
              "appears, the previous step was the right one: you go back and hold it longer. "
              "Going down is not going backwards; it is what makes it possible to keep going "
              "up next year.",
        "fr": "Une variable, un palier, et le tenir deux ou trois semaines avant d'en toucher "
              "une autre. Si le rendement baisse trois séances de suite, ou si une douleur "
              "articulaire apparaît, c'est le palier précédent qui était le bon : on y "
              "revient et on le tient plus longtemps. Descendre n'est pas reculer ; c'est ce "
              "qui permet de continuer à monter l'année prochaine."},

    # ── Calentar y enfriar ─────────────────────────────────────────────────
    "El calentamiento es la parte del entrenamiento con más mitología por minuto "
    "invertido. Lo que sigue separa lo que tiene respaldo razonable de lo que se repite "
    "por costumbre.": {
        "en": "The warm-up is the part of training with the most mythology per minute "
              "invested. What follows separates what has reasonable backing from what gets "
              "repeated out of habit.",
        "fr": "L'échauffement est la partie de l'entraînement qui compte le plus de "
              "mythologie par minute investie. Ce qui suit sépare ce qui a un appui "
              "raisonnable de ce qui se répète par habitude."},

    "Un calentamiento que sí hace algo, en tres actos": {
        "en": "A warm-up that actually does something, in three acts",
        "fr": "Un échauffement qui fait vraiment quelque chose, en trois actes"},

    "Cinco o diez minutos de movimiento general que suba la temperatura y la frecuencia "
    "cardíaca. Andar rápido, bici suave, cuerda ligera. Cualquier cosa que no sea "
    "estirar.": {
        "en": "Five or ten minutes of general movement that raises temperature and heart "
              "rate. Brisk walking, easy cycling, light skipping. Anything that is not "
              "stretching.",
        "fr": "Cinq ou dix minutes de mouvement général qui fait monter la température et la "
              "fréquence cardiaque. Marche rapide, vélo souple, corde légère. Tout sauf des "
              "étirements."},

    "Movilidad activa de las articulaciones que vas a usar. Círculos, balanceos, "
    "sentadillas sin peso, rotaciones. Movimiento, no posturas sostenidas.": {
        "en": "Active mobility of the joints you are going to use. Circles, swings, bodyweight "
              "squats, rotations. Movement, not held positions.",
        "fr": "Mobilité active des articulations que vous allez utiliser. Cercles, "
              "balancements, squats à vide, rotations. Du mouvement, pas des postures tenues."},

    "Series de aproximación del primer ejercicio: la barra vacía, después la mitad del "
    "peso, después algo por debajo del peso de trabajo. Es la parte del calentamiento que "
    "más rinde y la que más gente se salta.": {
        "en": "Ramp-up sets of the first exercise: the empty bar, then half the weight, then "
              "something just below the working weight. It is the part of the warm-up that "
              "returns most and the part most people skip.",
        "fr": "Des séries d'approche du premier exercice : la barre à vide, puis la moitié du "
              "poids, puis un peu en dessous du poids de travail. C'est la partie de "
              "l'échauffement qui rapporte le plus et celle que le plus de gens sautent."},

    "El objetivo no es prevenir lesiones —la evidencia sobre eso es más floja de lo que se "
    "dice— sino rendir mejor en las primeras series, que es un efecto inmediato y "
    "comprobable: la primera serie después de calentar bien se siente distinta, y eso ya "
    "justifica los diez minutos.": {
        "en": "The aim is not to prevent injuries —the evidence on that is weaker than is "
              "claimed— but to perform better in the first sets, which is an immediate and "
              "checkable effect: the first set after warming up properly feels different, and "
              "that alone justifies the ten minutes.",
        "fr": "L'objectif n'est pas de prévenir les blessures —les preuves sur ce point sont "
              "plus faibles qu'on ne le dit— mais de mieux rendre dans les premières séries, "
              "ce qui est un effet immédiat et vérifiable : la première série après un bon "
              "échauffement se ressent autrement, et cela justifie déjà les dix minutes."},

    "El estiramiento estático, en su sitio": {
        "en": "Static stretching, put in its place",
        "fr": "L'étirement statique, remis à sa place"},

    "Antes de entrenar, sostener un estiramiento largo reduce ligeramente la fuerza "
    "disponible durante los minutos siguientes. Si lo haces, que sea breve y no justo "
    "antes de la serie pesada.": {
        "en": "Before training, holding a long stretch slightly reduces the strength "
              "available over the following minutes. If you do it, keep it brief and not "
              "immediately before the heavy set.",
        "fr": "Avant l'entraînement, tenir un étirement long réduit légèrement la force "
              "disponible dans les minutes qui suivent. Si vous le faites, que ce soit bref "
              "et pas juste avant la série lourde."},

    "No previene lesiones de forma demostrada, y llevamos décadas intentando demostrarlo.": {
        "en": "It does not demonstrably prevent injuries, and we have spent decades trying to "
              "demonstrate that it does.",
        "fr": "Il ne prévient pas les blessures de façon démontrée, et cela fait des "
              "décennies qu'on essaie de le démontrer."},

    "No previene ni cura las agujetas. Esto está bastante bien establecido y sigue "
    "apareciendo en todas partes.": {
        "en": "It neither prevents nor cures muscle soreness. This is quite well established "
              "and it still turns up everywhere.",
        "fr": "Il ne prévient ni ne guérit les courbatures. C'est assez bien établi et cela "
              "continue d'apparaître partout."},

    "Sí mejora el rango de movimiento si se hace de forma regular, y eso tiene valor "
    "propio. Hazlo porque quieres más movilidad, no porque creas que te protege.": {
        "en": "It does improve range of motion if done regularly, and that has a value of its "
              "own. Do it because you want more mobility, not because you believe it protects "
              "you.",
        "fr": "Il améliore bien l'amplitude de mouvement s'il est pratiqué régulièrement, et "
              "cela a une valeur propre. Faites-le parce que vous voulez plus de mobilité, "
              "pas parce que vous croyez qu'il vous protège."},

    "Las agujetas, que no son lo que la gente cree": {
        "en": "Muscle soreness, which is not what people think",
        "fr": "Les courbatures, qui ne sont pas ce que l'on croit"},

    "Aparecen sobre todo tras trabajo excéntrico —la fase de bajada— y tras ejercicios "
    "nuevos, alcanzan su punto máximo entre veinticuatro y cuarenta y ocho horas después y "
    "se van solas. No son un indicador de que la sesión haya sido buena: un programa bien "
    "llevado produce cada vez menos agujetas mientras el rendimiento sigue subiendo, y "
    "perseguirlas es perseguir la señal equivocada.": {
        "en": "They appear above all after eccentric work —the lowering phase— and after new "
              "exercises, they peak between twenty-four and forty-eight hours later and they "
              "go away on their own. They are not an indicator that the session was good: a "
              "well-run programme produces less and less soreness while performance keeps "
              "rising, and chasing them is chasing the wrong signal.",
        "fr": "Elles apparaissent surtout après un travail excentrique —la phase de descente— "
              "et après des exercices nouveaux, culminent entre vingt-quatre et "
              "quarante-huit heures plus tard et s'en vont toutes seules. Ce n'est pas un "
              "indicateur que la séance a été bonne : un programme bien mené produit de moins "
              "en moins de courbatures pendant que le rendement continue de monter, et les "
              "poursuivre, c'est poursuivre le mauvais signal."},

    "Lo que mejor las alivia es moverse suave. Lo que no las quita es estirar. Y si duran "
    "más de cuatro o cinco días, o si vienen con hinchazón marcada y orina oscura después "
    "de una sesión inusualmente dura, eso ya no son agujetas y es motivo de consulta el "
    "mismo día.": {
        "en": "What relieves them best is gentle movement. What does not shift them is "
              "stretching. And if they last more than four or five days, or if they come with "
              "marked swelling and dark urine after an unusually hard session, that is no "
              "longer soreness and it is a reason to seek advice the same day.",
        "fr": "Ce qui les soulage le mieux, c'est de bouger doucement. Ce qui ne les enlève "
              "pas, c'est de s'étirer. Et si elles durent plus de quatre ou cinq jours, ou si "
              "elles s'accompagnent d'un gonflement marqué et d'urines foncées après une "
              "séance inhabituellement dure, ce ne sont plus des courbatures et c'est un "
              "motif de consultation le jour même."},
}
