# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · los tres centros en prosa y el bucle de la identificación
===============================================================================
El ejemplo de la observación precisa —«estoy nervioso» frente a «respiración
alta y hombros subidos, sin ningún pensamiento concreto»— es el que enseña la
diferencia entre una idea y una observación. La segunda frase se traduce sin
verbo y sin sujeto en las tres lenguas, como en el original: su forma
telegráfica es parte de la lección.

«Identificarse» es el término tradicional del fenómeno y tiene forma propia en
cada lengua. La oposición que lo define —tener algo frente a serlo— se
conserva con los mismos dos verbos.
"""

T = {
    "Los tres, en la práctica": {
        "en": "The three, in practice", "fr": "Les trois, en pratique"},

    "Intelectual": {"en": "Intellectual", "fr": "Intellectuel"},
    "Sede: cabeza. El más lento. Piensa, compara, planifica, decide. Llega siempre después "
    "de que algo haya pasado, y casi siempre para explicarlo.": {
        "en": "Seat: the head. The slowest. It thinks, compares, plans, decides. It always "
              "arrives after something has happened, and almost always in order to explain it.",
        "fr": "Siège : la tête. Le plus lent. Il pense, compare, planifie, décide. Il arrive "
              "toujours après que quelque chose s'est passé, et presque toujours pour "
              "l'expliquer."},

    "Emocional": {"en": "Emotional", "fr": "Émotionnel"},
    "Sede: pecho. El más rápido. Valora antes de entender. Cuando el intelectual empieza a "
    "analizar, este ya ha reaccionado y ha teñido todo lo demás.": {
        "en": "Seat: the chest. The fastest. It appraises before understanding. By the time "
              "the intellectual begins to analyse, this one has already reacted and coloured "
              "everything else.",
        "fr": "Siège : la poitrine. Le plus rapide. Il évalue avant de comprendre. Quand "
              "l'intellectuel commence à analyser, celui-ci a déjà réagi et teinté tout le "
              "reste."},

    "Motor e instintivo": {"en": "Moving and instinctive", "fr": "Moteur et instinctif"},
    "Sede: vientre y miembros. El más constante. Postura, respiración, movimiento, hábito. "
    "No se detiene nunca, ni durmiendo.": {
        "en": "Seat: the belly and the limbs. The steadiest. Posture, breathing, movement, "
              "habit. It never stops, not even in sleep.",
        "fr": "Siège : le ventre et les membres. Le plus constant. Posture, respiration, "
              "mouvement, habitude. Il ne s'arrête jamais, pas même en dormant."},

    "Para qué sirve el esquema": {
        "en": "What the scheme is for", "fr": "À quoi sert le schéma"},

    "Para localizar. Cuando una observación no se puede colocar en ninguno de los tres, es "
    "que no era una observación sino una idea. Y cuando se puede colocar, la información se "
    "vuelve mucho más precisa: «estoy nervioso» no dice nada; «respiración alta y hombros "
    "subidos, sin ningún pensamiento concreto» dice mucho, y además sugiere qué hacer.": {
        "en": "For locating. When an observation cannot be placed in any of the three, it was "
              "not an observation but an idea. And when it can be placed, the information "
              "becomes far more precise: «I am nervous» says nothing; «high breathing and "
              "raised shoulders, with no particular thought» says a great deal, and it also "
              "suggests what to do.",
        "fr": "À localiser. Quand une observation ne peut se placer dans aucun des trois, c'est "
              "que ce n'était pas une observation mais une idée. Et quand elle peut se placer, "
              "l'information devient bien plus précise : « je suis nerveux » ne dit rien ; "
              "« respiration haute et épaules montées, sans aucune pensée précise » dit "
              "beaucoup, et suggère en plus quoi faire."},

    "La regla del más rápido": {
        "en": "The rule of the fastest", "fr": "La règle du plus rapide"},

    "De las tres, la emocional es la que manda en la práctica, y no porque sea más "
    "importante: porque llega primero. Cuando aparece una reacción fuerte, el centro "
    "emocional ha decidido ya y el intelectual solo está redactando el informe. Toda la "
    "técnica de la pausa del capítulo siguiente consiste en meter unos segundos entre esos "
    "dos momentos.": {
        "en": "Of the three, the emotional one is what rules in practice, and not because it "
              "is more important: because it arrives first. When a strong reaction appears, "
              "the emotional centre has already decided and the intellectual one is merely "
              "drafting the report. The whole technique of the pause in the next chapter "
              "consists of inserting a few seconds between those two moments.",
        "fr": "Des trois, c'est l'émotionnel qui commande en pratique, et non parce qu'il "
              "serait plus important : parce qu'il arrive le premier. Quand une réaction forte "
              "apparaît, le centre émotionnel a déjà décidé et l'intellectuel ne fait que "
              "rédiger le rapport. Toute la technique de la pause du chapitre suivant consiste "
              "à glisser quelques secondes entre ces deux moments."},

    "La honestidad sobre este esquema": {
        "en": "Being honest about this scheme", "fr": "L'honnêteté sur ce schéma"},

    "El modelo de tres centros procede de la tradición y no de la neurociencia. No se "
    "corresponde con estructuras cerebrales concretas y no se ofrece como si lo hiciera. Se "
    "conserva porque como herramienta de clasificación de las propias observaciones "
    "funciona extraordinariamente bien: tres cajones bastan para ordenar casi todo y son "
    "pocos como para usarlos en caliente.": {
        "en": "The three-centre model comes from the tradition and not from neuroscience. It "
              "does not correspond to particular brain structures and it is not offered as if "
              "it did. It is kept because as a tool for classifying your own observations it "
              "works extraordinarily well: three drawers are enough to sort almost everything "
              "and few enough to be used in the heat of the moment.",
        "fr": "Le modèle des trois centres vient de la tradition et non des neurosciences. Il "
              "ne correspond pas à des structures cérébrales précises et il n'est pas proposé "
              "comme s'il le faisait. On le garde parce que, comme outil de classement de ses "
              "propres observations, il fonctionne remarquablement bien : trois tiroirs "
              "suffisent à ranger presque tout et sont assez peu nombreux pour servir à chaud."},

    # ── El bucle de la identificación ──────────────────────────────────────
    "Identificarse es la palabra tradicional para el fenómeno más frecuente y más costoso "
    "de la vida interior: dejar de tener algo y convertirse en ello. No tener enfado, sino "
    "ser el enfado. Es la diferencia entre «hay miedo aquí» y «soy un cobarde», y esa "
    "diferencia decide bastante.": {
        "en": "Identifying is the traditional word for the most frequent and most costly "
              "phenomenon of the inner life: ceasing to have something and becoming it. Not "
              "having anger, but being the anger. It is the difference between «there is fear "
              "here» and «I am a coward», and that difference decides a great deal.",
        "fr": "S'identifier est le mot traditionnel pour le phénomène le plus fréquent et le "
              "plus coûteux de la vie intérieure : cesser d'avoir quelque chose et le devenir. "
              "Non pas avoir de la colère, mais être la colère. C'est la différence entre « il "
              "y a de la peur ici » et « je suis un lâche », et cette différence décide de pas "
              "mal de choses."},

    '<span class="fig-n">Lám. 3</span> El bucle en sus cuatro pasos. Se cierra solo y se '
    "refuerza en cada vuelta. Hay un único punto con salida, y está entre el primero y el "
    "segundo.": {
        "en": '<span class="fig-n">Pl. 3</span> The loop in its four steps. It closes itself '
              "and reinforces itself on each turn. There is a single point with a way out, and "
              "it lies between the first and the second.",
        "fr": '<span class="fig-n">Pl. 3</span> La boucle en ses quatre pas. Elle se ferme '
              "seule et se renforce à chaque tour. Il y a un seul point avec une issue, et il "
              "se trouve entre le premier et le deuxième."},

    "El estímulo. Algo pasa: un comentario, un correo, una cara, un recuerdo. Dura una "
    "fracción de segundo y casi nunca se registra.": {
        "en": "The stimulus. Something happens: a remark, an email, a face, a memory. It lasts "
              "a fraction of a second and is almost never registered.",
        "fr": "Le stimulus. Il se passe quelque chose : une remarque, un courriel, un visage, "
              "un souvenir. Cela dure une fraction de seconde et n'est presque jamais "
              "enregistré."},

    "La reacción. El cuerpo responde: se aprieta algo, cambia la respiración, sube el tono. "
    "Ocurre antes de cualquier pensamiento y es lo primero que se puede aprender a notar.": {
        "en": "The reaction. The body responds: something tightens, the breathing changes, the "
              "voice rises. It happens before any thought and it is the first thing you can "
              "learn to notice.",
        "fr": "La réaction. Le corps répond : quelque chose se serre, la respiration change, le "
              "ton monte. Cela se produit avant toute pensée et c'est la première chose qu'on "
              "peut apprendre à remarquer."},

    "La justificación. Aparece un relato que explica la reacción y le da la razón. Es "
    "rapidísimo, es convincente y es la parte que más cuesta reconocer como parte del bucle "
    "y no como pensamiento propio.": {
        "en": "The justification. A story appears that explains the reaction and finds it "
              "right. It is extremely fast, it is convincing, and it is the part hardest to "
              "recognise as part of the loop rather than as a thought of your own.",
        "fr": "La justification. Apparaît un récit qui explique la réaction et lui donne "
              "raison. Il est très rapide, il est convaincant, et c'est la partie la plus "
              "difficile à reconnaître comme faisant partie de la boucle plutôt que comme une "
              "pensée à soi."},

    "La confirmación. La conclusión: «soy así». La reacción queda incorporada a la "
    "identidad, y a la vez siguiente arrancará con más fuerza porque ahora tiene un "
    "precedente.": {
        "en": "The confirmation. The conclusion: «I am like this». The reaction gets built "
              "into the identity, and next time it will start with more force because now it "
              "has a precedent.",
        "fr": "La confirmation. La conclusion : « je suis comme ça ». La réaction s'incorpore à "
              "l'identité, et la fois suivante elle démarrera avec plus de force parce qu'elle "
              "a désormais un précédent."},

    "Por qué se refuerza": {
        "en": "Why it reinforces itself", "fr": "Pourquoi elle se renforce"},

    "Porque cada vuelta añade una prueba. Un patrón que se ha justificado cuarenta veces "
    "tiene cuarenta razones a su favor, y a la cuarenta y una sale antes y más fuerte. Nada "
    "de esto requiere mala voluntad: es aprendizaje ordinario funcionando sobre material "
    "que preferiríamos no aprender.": {
        "en": "Because each turn adds a piece of evidence. A pattern that has been justified "
              "forty times has forty reasons in its favour, and on the forty-first it comes "
              "out sooner and stronger. None of this requires ill will: it is ordinary "
              "learning working on material we would rather not learn.",
        "fr": "Parce que chaque tour ajoute une preuve. Un schéma qui s'est justifié quarante "
              "fois a quarante raisons en sa faveur, et à la quarante et unième il sort plus "
              "tôt et plus fort. Rien de tout cela n'exige de mauvaise volonté : c'est de "
              "l'apprentissage ordinaire qui travaille sur un matériau que nous préférerions "
              "ne pas apprendre."},

    "La pausa": {"en": "The pause", "fr": "La pause"},

    "Entre el estímulo y la reacción hay un intervalo, y es el único lugar del bucle donde "
    "hay algo que elegir. Una vez que la reacción ha ocurrido, la justificación viene sola "
    "y la confirmación detrás; discutir con la justificación cuando ya se ha reaccionado es "
    "llegar tarde a todo. La práctica entera consiste en ampliar ese intervalo, y se amplía "
    "por un único procedimiento: notar la reacción corporal antes de que llegue el relato.": {
        "en": "Between the stimulus and the reaction there is an interval, and it is the only "
              "place in the loop where there is anything to choose. Once the reaction has "
              "happened, the justification comes on its own and the confirmation behind it; "
              "arguing with the justification when you have already reacted is arriving late "
              "for everything. The whole practice consists of widening that interval, and it "
              "is widened by a single procedure: noticing the bodily reaction before the story "
              "arrives.",
        "fr": "Entre le stimulus et la réaction il y a un intervalle, et c'est le seul endroit "
              "de la boucle où il y ait quelque chose à choisir. Une fois la réaction "
              "survenue, la justification vient toute seule et la confirmation derrière ; "
              "discuter avec la justification quand on a déjà réagi, c'est arriver en retard "
              "sur tout. Toute la pratique consiste à élargir cet intervalle, et il s'élargit "
              "par un seul procédé : remarquer la réaction corporelle avant que le récit "
              "n'arrive."},

    "Aprende primero a reconocer TU reacción física característica. Cada persona tiene una "
    "o dos: mandíbula, estómago, hombros, respiración alta, calor en la cara. Búscala "
    "durante una semana sin intentar cambiar nada.": {
        "en": "Learn first to recognise YOUR characteristic physical reaction. Each person has "
              "one or two: jaw, stomach, shoulders, high breathing, heat in the face. Look for "
              "it for a week without trying to change anything.",
        "fr": "Apprenez d'abord à reconnaître VOTRE réaction physique caractéristique. Chacun "
              "en a une ou deux : mâchoire, estomac, épaules, respiration haute, chaleur au "
              "visage. Cherchez-la pendant une semaine sans essayer de rien changer."},

    "Cuando la reconozcas en caliente, no hagas nada con ella. Solo nómbrala por dentro, sin "
    "palabras bonitas: «mandíbula».": {
        "en": "When you recognise it in the heat of the moment, do nothing with it. Just name "
              "it inwardly, with no pretty words: «jaw».",
        "fr": "Quand vous la reconnaissez à chaud, n'en faites rien. Nommez-la seulement "
              "au-dedans, sans jolis mots : « mâchoire »."},

    "Respira una vez, completa, antes de hablar. Una. No es una técnica de relajación: es un "
    "retardo deliberado.": {
        "en": "Take one breath, a full one, before speaking. One. It is not a relaxation "
              "technique: it is a deliberate delay.",
        "fr": "Respirez une fois, complètement, avant de parler. Une. Ce n'est pas une "
              "technique de relaxation : c'est un retard délibéré."},
}
