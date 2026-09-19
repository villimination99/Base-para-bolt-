# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · el trazo del pentagrama
====================================================
La secuencia del trazo se da por partes del cuerpo —cadera izquierda, frente,
cadera derecha, hombro izquierdo, hombro derecho— y las flechas del original
se conservan tal cual. El lector lo ejecuta de pie con el libro en la otra
mano, y cualquier reordenación le dibujaría otra figura.

La nota sobre la visualización dice explícitamente que no visualizar es una
variación normal y no un defecto. Esa aclaración se traduce entera: es lo que
impide que media docena de lectores abandonen creyendo que lo hacen mal.
"""

T = {
    "Atribución de las puntas": {
        "en": "Attribution of the points", "fr": "Attribution des branches"},

    "Superior": {"en": "Upper", "fr": "Supérieure"},
    "Espíritu · la atención que observa": {
        "en": "Spirit · the attention that observes",
        "fr": "Esprit · l'attention qui observe"},
    "Superior izquierda": {"en": "Upper left", "fr": "Supérieure gauche"},
    "Aire · el aliento y el pensamiento": {
        "en": "Air · breath and thought", "fr": "Air · le souffle et la pensée"},
    "Superior derecha": {"en": "Upper right", "fr": "Supérieure droite"},
    "Agua · la memoria y el sentimiento": {
        "en": "Water · memory and feeling", "fr": "Eau · la mémoire et le sentiment"},
    "Inferior izquierda": {"en": "Lower left", "fr": "Inférieure gauche"},
    "Tierra · el cuerpo": {"en": "Earth · the body", "fr": "Terre · le corps"},
    "Inferior derecha": {"en": "Lower right", "fr": "Inférieure droite"},
    "Fuego · la voluntad": {"en": "Fire · will", "fr": "Feu · la volonté"},

    "Invocar: de Tierra a Espíritu": {
        "en": "To invoke: from Earth to Spirit",
        "fr": "Invoquer : de la Terre à l'Esprit"},

    "El trazo de apertura empieza en la punta inferior izquierda —Tierra, el cuerpo— y sube "
    "hacia el vértice superior. El gesto dice algo muy concreto: se parte de donde uno está, "
    "que es un cuerpo en una habitación, y se sube desde ahí. Cualquier práctica que empiece "
    "por arriba se está saltando el único punto de partida disponible.": {
        "en": "The opening stroke begins at the lower left point —Earth, the body— and rises "
              "towards the upper vertex. The gesture says something very concrete: you start "
              "from where you are, which is a body in a room, and you go up from there. Any "
              "practice that begins at the top is skipping the only starting point available.",
        "fr": "Le tracé d'ouverture commence à la branche inférieure gauche —la Terre, le "
              "corps— et monte vers le sommet. Le geste dit quelque chose de très concret : on "
              "part d'où l'on est, c'est-à-dire d'un corps dans une pièce, et on monte de là. "
              "Toute pratique qui commence par le haut saute le seul point de départ "
              "disponible."},

    "Despedir: de Espíritu a Tierra": {
        "en": "To dismiss: from Spirit to Earth",
        "fr": "Congédier : de l'Esprit à la Terre"},

    "El trazo de cierre invierte el primer movimiento: baja del vértice superior a Tierra. "
    "Se vuelve al cuerpo y a la habitación. Es el gesto de terminar, y es el que más se "
    "omite y el que más falta hace: sin cierre, la operación no acaba, se disuelve — y lo "
    "que se disuelve deja residuo.": {
        "en": "The closing stroke reverses the first movement: it descends from the upper "
              "vertex to Earth. You return to the body and to the room. It is the gesture of "
              "finishing, and it is the one most often left out and the one most needed: "
              "without a closing the operation does not end, it dissolves — and what dissolves "
              "leaves residue.",
        "fr": "Le tracé de clôture inverse le premier mouvement : il descend du sommet à la "
              "Terre. On revient au corps et à la pièce. C'est le geste de terminer, et c'est "
              "celui qu'on omet le plus et dont on a le plus besoin : sans clôture, l'opération "
              "ne s'achève pas, elle se dissout — et ce qui se dissout laisse un résidu."},

    "Por qué el cierre no es opcional": {
        "en": "Why the closing is not optional",
        "fr": "Pourquoi la clôture n'est pas facultative"},

    "Una sesión de concentración intensa que termina sin transición deja al operante en un "
    "estado intermedio: absorto, algo irritable, con la sensación de no estar del todo en lo "
    "que hace. Cualquiera que haya salido de golpe de cuatro horas de trabajo profundo lo "
    "reconoce. El rito de cierre es un procedimiento de aterrizaje, y funciona por la misma "
    "razón por la que un corredor no se para en seco.": {
        "en": "A session of intense concentration that ends without a transition leaves the "
              "operator in an intermediate state: absorbed, somewhat irritable, with the "
              "feeling of not being entirely in what they are doing. Anyone who has come "
              "abruptly out of four hours of deep work recognises it. The closing rite is a "
              "landing procedure, and it works for the same reason a runner does not stop "
              "dead.",
        "fr": "Une séance de concentration intense qui se termine sans transition laisse "
              "l'opérant dans un état intermédiaire : absorbé, un peu irritable, avec le "
              "sentiment de n'être pas tout à fait à ce qu'il fait. Quiconque est sorti d'un "
              "coup de quatre heures de travail profond le reconnaît. Le rite de clôture est "
              "une procédure d'atterrissage, et il fonctionne pour la même raison qu'un coureur "
              "ne s'arrête pas net."},

    "El trazo, paso a paso": {
        "en": "The stroke, step by step", "fr": "Le tracé, pas à pas"},

    "De pie, mirando al cuarto que toque. Brazo derecho extendido, dedos índice y medio "
    "juntos, el resto recogido. O el arma que corresponda.": {
        "en": "Standing, facing the quarter in question. Right arm extended, index and middle "
              "fingers together, the rest folded in. Or the corresponding weapon.",
        "fr": "Debout, face au quartier concerné. Bras droit tendu, index et majeur joints, le "
              "reste replié. Ou l'arme correspondante."},

    "Sitúa mentalmente los cinco vértices en un cuadro imaginario del tamaño de tu propio "
    "cuerpo: la punta superior a la altura de la frente, las inferiores a la de las "
    "caderas.": {
        "en": "Place the five vertices mentally in an imaginary frame the size of your own "
              "body: the upper point at the height of your forehead, the lower ones at the "
              "height of your hips.",
        "fr": "Placez mentalement les cinq sommets dans un cadre imaginaire à la taille de "
              "votre propre corps : la branche supérieure à hauteur du front, les inférieures "
              "à hauteur des hanches."},

    "Empieza en la cadera izquierda y sube a la frente. Ese es el primer trazo y el que "
    "marca la dirección de todo lo demás.": {
        "en": "Begin at the left hip and rise to the forehead. That is the first stroke and "
              "the one that sets the direction of everything else.",
        "fr": "Commencez à la hanche gauche et montez au front. C'est le premier tracé et "
              "celui qui donne la direction de tout le reste."},

    "Continúa: frente → cadera derecha → hombro izquierdo → hombro derecho → cadera "
    "izquierda. Cinco trazos, sin levantar la mano.": {
        "en": "Continue: forehead → right hip → left shoulder → right shoulder → left hip. "
              "Five strokes, without lifting the hand.",
        "fr": "Continuez : front → hanche droite → épaule gauche → épaule droite → hanche "
              "gauche. Cinq tracés, sans lever la main."},

    "Cierra el circuito volviendo al punto de partida y detén ahí la mano un instante antes "
    "de bajarla. La figura queda cerrada; un pentagrama a medio trazar no vale.": {
        "en": "Close the circuit by returning to the starting point and hold the hand there "
              "for an instant before lowering it. The figure is closed; a half-traced pentagram "
              "is no good.",
        "fr": "Fermez le circuit en revenant au point de départ et arrêtez-y la main un instant "
              "avant de la baisser. La figure est close ; un pentagramme à moitié tracé ne vaut "
              "rien."},

    "Sobre la visualización": {"en": "On visualisation", "fr": "Sur la visualisation"},

    "Se recomienda ver la figura trazada en luz. Si no la ves —y mucha gente no visualiza, "
    "es una variación normal y no un defecto—, basta con sostener la intención y ejecutar el "
    "gesto con precisión. La eficacia está en la secuencia motora y en la atención "
    "sostenida, no en la calidad de la imagen mental.": {
        "en": "It is recommended that you see the figure traced in light. If you do not see it "
              "—and many people do not visualise, which is a normal variation and not a defect— "
              "it is enough to hold the intention and carry out the gesture precisely. The "
              "effectiveness lies in the motor sequence and in sustained attention, not in the "
              "quality of the mental image.",
        "fr": "Il est recommandé de voir la figure tracée en lumière. Si vous ne la voyez pas "
              "—et beaucoup de gens ne visualisent pas, c'est une variation normale et non un "
              "défaut— il suffit de tenir l'intention et d'exécuter le geste avec précision. "
              "L'efficacité tient à la séquence motrice et à l'attention soutenue, non à la "
              "qualité de l'image mentale."},

    # ── El hexagrama ───────────────────────────────────────────────────────
    "Donde el pentagrama ordena los cuatro elementos, el hexagrama ordena los siete "
    "planetas. Es la figura del trabajo con las funciones más generales: el límite, la "
    "expansión, el empuje, la identidad, el vínculo, la palabra y el ritmo.": {
        "en": "Where the pentagram orders the four elements, the hexagram orders the seven "
              "planets. It is the figure for work with the most general functions: the limit, "
              "expansion, drive, identity, the bond, the word and rhythm.",
        "fr": "Là où le pentagramme ordonne les quatre éléments, l'hexagramme ordonne les sept "
              "planètes. C'est la figure du travail avec les fonctions les plus générales : la "
              "limite, l'expansion, l'élan, l'identité, le lien, la parole et le rythme."},
}
