# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · la postura y las cuatro emociones difíciles
=================================================================
El libro rechaza llamar «negativas» a las cuatro emociones y las llama
difíciles, y explica por qué en la misma frase. Las dos palabras van en los
tres idiomas: si se tradujera solo la elegida, el lector no vería contra qué
se está eligiendo.

La regla de las tres partes es una tríada que se sostiene a la vez —no
expresarlas, no reprimirlas, mirarlas— y las tres se traducen con la misma
construcción negativa y positiva que en el original, porque la tercera solo se
entiende contra las dos primeras.
"""

T = {
    "Hay una relación de doble sentido entre postura y estado: el estado modifica la "
    "postura, y la postura modifica el estado. Eso hace que la postura sirva para dos cosas "
    "distintas. Como observación, es un informe fiable de en qué estado estás. Como "
    "intervención —la única que este libro recomienda hacer en caliente— es la palanca más "
    "rápida disponible: enderezarse, bajar los hombros y soltar la mandíbula cambia algo en "
    "segundos.": {
        "en": "There is a two-way relationship between posture and state: the state modifies "
              "the posture, and the posture modifies the state. That makes posture useful for "
              "two different things. As observation, it is a reliable report on what state you "
              "are in. As intervention —the only one this book recommends making in the heat "
              "of the moment— it is the fastest lever available: straightening up, dropping "
              "the shoulders and releasing the jaw changes something within seconds.",
        "fr": "Il y a une relation à double sens entre posture et état : l'état modifie la "
              "posture, et la posture modifie l'état. Cela fait que la posture sert à deux "
              "choses différentes. Comme observation, c'est un compte rendu fiable de l'état "
              "où l'on est. Comme intervention —la seule que ce livre recommande de faire à "
              "chaud— c'est le levier le plus rapide dont on dispose : se redresser, baisser "
              "les épaules et relâcher la mâchoire change quelque chose en quelques secondes."},

    "La excepción a la regla de no intervenir": {
        "en": "The exception to the rule of not intervening",
        "fr": "L'exception à la règle de ne pas intervenir"},

    "El capítulo 8 dice observar sin intervenir, y aquí se hace una excepción explícita con "
    "la postura y la respiración. El motivo es práctico: son las dos únicas cosas que se "
    "pueden corregir sin dejar de observar, porque la corrección misma es observable. Todo "
    "lo demás —los pensamientos, las emociones, las decisiones— se mira y se deja.": {
        "en": "Chapter 8 says observe without intervening, and here an explicit exception is "
              "made for posture and breathing. The reason is practical: they are the only two "
              "things that can be corrected without ceasing to observe, because the correction "
              "itself is observable. Everything else —thoughts, emotions, decisions— is looked "
              "at and left alone.",
        "fr": "Le chapitre 8 dit d'observer sans intervenir, et l'on fait ici une exception "
              "explicite pour la posture et la respiration. La raison est pratique : ce sont "
              "les deux seules choses que l'on puisse corriger sans cesser d'observer, parce "
              "que la correction elle-même est observable. Tout le reste —les pensées, les "
              "émotions, les décisions— se regarde et se laisse."},

    "El ejercicio de los tres apoyos": {
        "en": "The exercise of the three supports",
        "fr": "L'exercice des trois appuis"},

    "Sentado o de pie, localiza tres puntos donde tu cuerpo esté apoyado. Planta de los "
    "pies, isquiones, espalda contra el respaldo, antebrazos sobre la mesa: los que sean.": {
        "en": "Sitting or standing, locate three points where your body is resting. Soles of "
              "the feet, sitting bones, back against the chair, forearms on the table: "
              "whichever they are.",
        "fr": "Assis ou debout, repérez trois points où votre corps s'appuie. Plante des pieds, "
              "ischions, dos contre le dossier, avant-bras sur la table : quels qu'ils soient."},

    "Siente los tres a la vez. No uno detrás de otro: los tres al mismo tiempo, que es lo "
    "que cuesta.": {
        "en": "Feel all three at once. Not one after another: all three at the same time, "
              "which is the hard part.",
        "fr": "Sentez les trois à la fois. Non l'un après l'autre : les trois en même temps, "
              "c'est là ce qui coûte."},

    "Añade la respiración sin dejar los tres apoyos. Ahora son cuatro cosas simultáneas.": {
        "en": "Add the breathing without letting go of the three supports. Now there are four "
              "simultaneous things.",
        "fr": "Ajoutez la respiration sans lâcher les trois appuis. Cela fait maintenant quatre "
              "choses simultanées."},

    "Sostenlo treinta segundos. Cuando se caiga —se caerá— vuelve a empezar sin "
    "comentarios.": {
        "en": "Hold it for thirty seconds. When it collapses —it will— start again without "
              "comment.",
        "fr": "Tenez trente secondes. Quand cela s'écroule —cela s'écroulera— recommencez sans "
              "commentaire."},

    "Este ejercicio es la forma más económica que conozco de entrenar atención dividida, "
    "porque no requiere ninguna condición: se puede hacer en una reunión, en una cola o en "
    "medio de una discusión, y nadie lo nota.": {
        "en": "This exercise is the most economical way I know of training divided attention, "
              "because it requires no conditions at all: it can be done in a meeting, in a "
              "queue or in the middle of an argument, and nobody notices.",
        "fr": "Cet exercice est la façon la plus économique que je connaisse d'entraîner "
              "l'attention divisée, car il n'exige aucune condition : on peut le faire en "
              "réunion, dans une file d'attente ou au milieu d'une dispute, et personne ne le "
              "remarque."},

    # ── Las cuatro difíciles ───────────────────────────────────────────────
    "Miedo, ira, tristeza y vergüenza. Son las cuatro emociones que la tradición llama "
    "negativas y que este libro prefiere llamar difíciles, porque «negativas» sugiere que "
    "no deberían estar y ese es exactamente el error que hay que evitar.": {
        "en": "Fear, anger, sadness and shame. They are the four emotions the tradition calls "
              "negative and that this book prefers to call difficult, because «negative» "
              "suggests they should not be there and that is exactly the mistake to be "
              "avoided.",
        "fr": "Peur, colère, tristesse et honte. Ce sont les quatre émotions que la tradition "
              "appelle négatives et que ce livre préfère appeler difficiles, parce que "
              "« négatives » suggère qu'elles ne devraient pas être là, et c'est exactement "
              "l'erreur à éviter."},

    '<span class="fig-n">Lám. 6</span> Las cuatro, con su firma corporal, la información que '
    "traen y el punto donde se tuercen.": {
        "en": '<span class="fig-n">Pl. 6</span> The four, with their bodily signature, the '
              "information they bring and the point at which they go wrong.",
        "fr": '<span class="fig-n">Pl. 6</span> Les quatre, avec leur signature corporelle, '
              "l'information qu'elles apportent et le point où elles déraillent."},

    "La regla de las tres partes": {
        "en": "The three-part rule", "fr": "La règle en trois parties"},

    "Con las cuatro se hace lo mismo, y son tres cosas que hay que sostener a la vez porque "
    "cada una sola falla.": {
        "en": "With all four you do the same thing, and it is three things that have to be "
              "held together because each one alone fails.",
        "fr": "Avec les quatre on fait la même chose, et ce sont trois choses qu'il faut tenir "
              "ensemble parce que chacune seule échoue."},

    "No expresarlas automáticamente. Descargar la emoción sobre alguien no la descarga: la "
    "entrena. La rabia expresada sin filtro sale más fácil la próxima vez, y de paso rompe "
    "cosas.": {
        "en": "Not expressing them automatically. Discharging an emotion onto someone does not "
              "discharge it: it trains it. Rage expressed without a filter comes out more "
              "easily next time, and breaks things along the way.",
        "fr": "Ne pas les exprimer automatiquement. Décharger l'émotion sur quelqu'un ne la "
              "décharge pas : cela l'entraîne. La rage exprimée sans filtre sort plus "
              "facilement la fois suivante, et casse des choses au passage."},

    "No reprimirlas. Empujar una emoción hacia abajo consume energía, no la elimina y suele "
    "reaparecer en otra parte —el cuerpo, el sueño, el trato con quien no tenía culpa—.": {
        "en": "Not repressing them. Pushing an emotion down consumes energy, does not "
              "eliminate it and tends to reappear elsewhere —the body, sleep, the way you "
              "treat someone who was not at fault.",
        "fr": "Ne pas les réprimer. Pousser une émotion vers le bas consomme de l'énergie, ne "
              "l'élimine pas et la fait d'ordinaire réapparaître ailleurs —le corps, le "
              "sommeil, la façon de traiter qui n'y était pour rien."},

    "Mirarlas hasta que pasen. Esta es la tercera vía y la difícil: sentir la emoción "
    "entera, en el cuerpo, con su nombre puesto, sin actuarla y sin empujarla. Y esperar. "
    "Todas pasan, y pasan bastante antes de lo que uno cree cuando no se las alimenta con "
    "relato.": {
        "en": "Watching them until they pass. This is the third way and the hard one: feeling "
              "the whole emotion, in the body, with its name on it, without acting it out and "
              "without pushing it away. And waiting. They all pass, and they pass considerably "
              "sooner than you think when they are not fed with story.",
        "fr": "Les regarder jusqu'à ce qu'elles passent. C'est la troisième voie et la "
              "difficile : sentir l'émotion entière, dans le corps, son nom posé dessus, sans "
              "la jouer et sans la repousser. Et attendre. Toutes passent, et bien plus tôt "
              "qu'on ne le croit lorsqu'on ne les nourrit pas de récit."},

    "La información que traen": {
        "en": "The information they bring", "fr": "L'information qu'elles apportent"},

    "Ninguna de las cuatro es un error del sistema. Las cuatro informan de algo y el "
    "problema nunca es que aparezcan: es lo que se hace con ellas.": {
        "en": "None of the four is a fault in the system. All four report something and the "
              "problem is never that they appear: it is what gets done with them.",
        "fr": "Aucune des quatre n'est un défaut du système. Toutes les quatre signalent "
              "quelque chose et le problème n'est jamais qu'elles apparaissent : c'est ce qu'on "
              "en fait."},

    "Qué avisa cada una y dónde se tuerce": {
        "en": "What each one warns of and where it goes wrong",
        "fr": "Ce que signale chacune et où elle déraille"},

    "Miedo": {"en": "Fear", "fr": "Peur"},
    "Avisa de un riesgo. Se tuerce cuando anticipa lo que no ha pasado y se queda a vivir "
    "ahí.": {
        "en": "It warns of a risk. It goes wrong when it anticipates what has not happened and "
              "settles down to live there.",
        "fr": "Elle signale un risque. Elle déraille quand elle anticipe ce qui n'est pas "
              "arrivé et s'installe pour y vivre."},

    "Ira": {"en": "Anger", "fr": "Colère"},
    "Avisa de un límite pisado. Se tuerce cuando se convierte en juicio sobre una persona "
    "en lugar de sobre un hecho.": {
        "en": "It warns of a limit crossed. It goes wrong when it turns into a judgement on a "
              "person instead of on a fact.",
        "fr": "Elle signale une limite franchie. Elle déraille quand elle devient un jugement "
              "sur une personne au lieu de porter sur un fait."},

    "Tristeza": {"en": "Sadness", "fr": "Tristesse"},
    "Avisa de una pérdida y pide tiempo. Se tuerce cuando se vuelve relato sobre uno mismo: "
    "de «he perdido algo» a «soy alguien que pierde».": {
        "en": "It warns of a loss and asks for time. It goes wrong when it turns into a story "
              "about oneself: from «I have lost something» to «I am someone who loses».",
        "fr": "Elle signale une perte et demande du temps. Elle déraille quand elle devient un "
              "récit sur soi-même : de « j'ai perdu quelque chose » à « je suis quelqu'un qui "
              "perd »."},

    "Vergüenza": {"en": "Shame", "fr": "Honte"},
}
