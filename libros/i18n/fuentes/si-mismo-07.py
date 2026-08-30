# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · los tres errores y los seis recuerdos del día
===================================================================
Los tres errores llevan cada uno una frase entrecomillada que es lo que el
lector se dice a sí mismo: «otra vez lo mismo, qué desastre soy», «esto me
pasa porque de pequeño…», «a partir de ahora voy a…». Se traducen como habla
corriente y conservan los puntos suspensivos donde los tienen: las dos frases
que se cortan se cortan porque nadie las termina.

Los seis momentos del día no llevan hora fija en el texto —«a media tarde», «al
terminar»— y así se quedan. La lámina es la que los coloca; el capítulo solo
los nombra.
"""

T = {
    "Por dos razones. La primera es técnica: en cuanto intentas cambiar lo que observas, "
    "dejas de verlo — la intervención consume la atención que estaba mirando. La segunda es "
    "más profunda: no se puede cambiar con criterio algo que todavía no se conoce, y la "
    "prisa por corregir es lo que hace que la gente lleve años arreglando el problema "
    "equivocado.": {
        "en": "For two reasons. The first is technical: the moment you try to change what you "
              "are observing, you stop seeing it — the intervention consumes the attention "
              "that was doing the looking. The second is deeper: you cannot change with "
              "judgement something you do not yet know, and the hurry to correct is what has "
              "people spending years fixing the wrong problem.",
        "fr": "Pour deux raisons. La première est technique : dès que vous essayez de changer "
              "ce que vous observez, vous cessez de le voir — l'intervention consomme "
              "l'attention qui regardait. La seconde est plus profonde : on ne peut pas changer "
              "avec discernement une chose qu'on ne connaît pas encore, et la hâte de corriger "
              "est ce qui fait que les gens passent des années à réparer le mauvais problème."},

    "Esto no significa resignación. Significa orden: primero ver, y bastante tiempo; "
    "después, si hace falta, actuar. En la práctica ocurre además algo curioso y muy "
    "reportado: una parte de lo observado con constancia cambia sin que se haga nada, "
    "simplemente porque dejar de ser automático ya es un cambio.": {
        "en": "This does not mean resignation. It means order: first see, and for a good "
              "while; then, if necessary, act. In practice something curious and much reported "
              "also happens: part of what is observed consistently changes without anything "
              "being done, simply because ceasing to be automatic is already a change.",
        "fr": "Cela ne signifie pas la résignation. Cela signifie l'ordre : d'abord voir, et un "
              "bon moment ; ensuite, s'il le faut, agir. En pratique il se produit en outre "
              "quelque chose de curieux et de très rapporté : une partie de ce qui est observé "
              "avec constance change sans qu'on fasse rien, simplement parce que cesser d'être "
              "automatique est déjà un changement."},

    "Los tres errores": {"en": "The three mistakes", "fr": "Les trois erreurs"},

    "Juzgar. «Otra vez lo mismo, qué desastre soy.» En el momento en que aparece el juicio, "
    "la observación ha terminado y ha empezado otra cosa —normalmente el bucle del capítulo "
    "6—. Cuando notes el juicio, nómbralo también: «juicio». Y sigue.": {
        "en": "Judging. «The same thing again, what a disaster I am.» The moment judgement "
              "appears, the observation has ended and something else has begun —usually the "
              "loop of chapter 6. When you notice the judgement, name that too: «judgement». "
              "And carry on.",
        "fr": "Juger. « Encore la même chose, quel désastre je fais. » Au moment où le jugement "
              "apparaît, l'observation est finie et autre chose a commencé —d'ordinaire la "
              "boucle du chapitre 6. Quand vous remarquez le jugement, nommez-le aussi : "
              "« jugement ». Et continuez."},

    "Explicar. «Esto me pasa porque de pequeño…» Puede que sea verdad y no es el momento. La "
    "explicación sustituye el dato por una teoría, y una teoría es mucho más cómoda de "
    "mirar que un hecho.": {
        "en": "Explaining. «This happens to me because as a child…» It may well be true and it "
              "is not the moment. Explanation replaces the datum with a theory, and a theory "
              "is far more comfortable to look at than a fact.",
        "fr": "Expliquer. « Cela m'arrive parce que, enfant… » C'est peut-être vrai et ce n'est "
              "pas le moment. L'explication remplace la donnée par une théorie, et une théorie "
              "est bien plus confortable à regarder qu'un fait."},

    "Arreglar. «A partir de ahora voy a…» Los propósitos formulados en caliente son casi "
    "todos falsos, y su función real es cerrar la observación antes de que resulte "
    "incómoda. Anota lo visto; los propósitos se toman en frío y por escrito.": {
        "en": "Fixing. «From now on I am going to…» Resolutions made in the heat of the moment "
              "are almost all false, and their real function is to close the observation "
              "before it becomes uncomfortable. Write down what you saw; resolutions are made "
              "cold and in writing.",
        "fr": "Réparer. « À partir de maintenant je vais… » Les résolutions formulées à chaud "
              "sont presque toutes fausses, et leur fonction réelle est de clore l'observation "
              "avant qu'elle ne devienne inconfortable. Notez ce que vous avez vu ; les "
              "résolutions se prennent à froid et par écrit."},

    "Y el error que los engloba": {
        "en": "And the mistake that contains them all",
        "fr": "Et l'erreur qui les englobe"},

    "Querer que la observación sirva para algo hoy. Sirve, pero en la escala de los meses. "
    "El que exige rendimiento inmediato acaba fabricando hallazgos para sentir que avanza, "
    "y eso arruina el instrumento: un observador que quiere encontrar algo encuentra "
    "siempre lo que quiere.": {
        "en": "Wanting the observation to be good for something today. It is, but on the scale "
              "of months. Anyone who demands immediate returns ends up manufacturing findings "
              "in order to feel they are progressing, and that ruins the instrument: an "
              "observer who wants to find something always finds what they want.",
        "fr": "Vouloir que l'observation serve à quelque chose aujourd'hui. Elle sert, mais à "
              "l'échelle des mois. Qui exige un rendement immédiat finit par fabriquer des "
              "trouvailles pour se sentir avancer, et cela ruine l'instrument : un observateur "
              "qui veut trouver quelque chose trouve toujours ce qu'il veut."},

    # ── Los seis recuerdos del día ─────────────────────────────────────────
    "La observación de sí no se practica todo el día: eso no es posible y quien lo intenta "
    "abandona en una semana. Se practica en momentos concretos, pocos y fijos, y se "
    "extiende desde ahí.": {
        "en": "Self-observation is not practised all day: that is not possible and anyone who "
              "tries gives up within a week. It is practised at specific moments, few and "
              "fixed, and it spreads out from there.",
        "fr": "L'observation de soi ne se pratique pas toute la journée : ce n'est pas possible "
              "et qui l'essaie abandonne en une semaine. Elle se pratique à des moments précis, "
              "peu nombreux et fixes, et elle s'étend à partir de là."},

    '<span class="fig-n">Lám. 4</span> Los seis momentos repartidos por el día, siempre los '
    "mismos y siempre a la misma hora. En gris, el tramo de descanso.": {
        "en": '<span class="fig-n">Pl. 4</span> The six moments spread through the day, always '
              "the same ones and always at the same hour. In grey, the stretch of rest.",
        "fr": '<span class="fig-n">Pl. 4</span> Les six moments répartis sur la journée, '
              "toujours les mêmes et toujours à la même heure. En gris, la plage de repos."},

    "Los seis momentos": {"en": "The six moments", "fr": "Les six moments"},
    "Uno cada pocas horas": {
        "en": "One every few hours", "fr": "Un toutes les quelques heures"},

    "Antes de levantarte y antes de coger el teléfono. Treinta segundos: qué estado hay, qué "
    "tal el cuerpo, qué es lo primero que aparece en la cabeza.": {
        "en": "Before getting up and before picking up the phone. Thirty seconds: what state "
              "there is, how the body is, what is the first thing that appears in your head.",
        "fr": "Avant de vous lever et avant de prendre le téléphone. Trente secondes : quel "
              "état il y a, comment va le corps, quelle est la première chose qui apparaît dans "
              "la tête."},

    "Antes de la primera tarea real del día. La postura y la respiración, y una palabra para "
    "el estado.": {
        "en": "Before the first real task of the day. Posture and breathing, and one word for "
              "the state.",
        "fr": "Avant la première vraie tâche de la journée. La posture et la respiration, et un "
              "mot pour l'état."},

    "El mejor de los seis, porque el hambre y la prisa hacen visible mucho. Tres "
    "respiraciones antes del primer bocado.": {
        "en": "The best of the six, because hunger and hurry make a great deal visible. Three "
              "breaths before the first mouthful.",
        "fr": "Le meilleur des six, parce que la faim et la hâte rendent beaucoup de choses "
              "visibles. Trois respirations avant la première bouchée."},

    "El momento del bajón, y por tanto el más informativo. Distinguir cansancio de "
    "desánimo.": {
        "en": "The moment of the slump, and therefore the most informative. Tell tiredness "
              "from discouragement.",
        "fr": "Le moment du creux, et donc le plus informatif. Distinguer la fatigue du "
              "découragement."},

    "Al cerrar la jornada. Qué queda encendido: eso es lo que se llevará a casa si nadie lo "
    "mira.": {
        "en": "As the working day closes. What is still switched on: that is what will go home "
              "with you if nobody looks at it.",
        "fr": "À la clôture de la journée. Ce qui reste allumé : c'est ce que vous emporterez "
              "chez vous si personne ne le regarde."},

    "Enlaza con el inventario nocturno del capítulo 14.": {
        "en": "It links up with the nightly inventory of chapter 14.",
        "fr": "Il fait la jonction avec l'inventaire du soir du chapitre 14."},

    "Lo que se hace en cada uno": {
        "en": "What is done at each one", "fr": "Ce qu'on fait à chacun"},

    "Parar. Literalmente: dejar de moverse durante unos segundos.": {
        "en": "Stop. Literally: stop moving for a few seconds.",
        "fr": "S'arrêter. Littéralement : cesser de bouger pendant quelques secondes."},
    "Sentir el cuerpo entero de una vez —peso, apoyo, postura— sin recorrerlo por partes.": {
        "en": "Feel the whole body at once —weight, support, posture— without going through it "
              "part by part.",
        "fr": "Sentir le corps entier d'un coup —poids, appui, posture— sans le parcourir par "
              "morceaux."},
    "Notar la respiración tal como está. Sin corregirla. Este punto es el que casi todo el "
    "mundo se salta.": {
        "en": "Notice the breathing as it is. Without correcting it. This is the point almost "
              "everyone skips.",
        "fr": "Remarquer la respiration telle qu'elle est. Sans la corriger. C'est le point que "
              "presque tout le monde saute."},
    "Poner una palabra al estado.": {
        "en": "Put one word to the state.", "fr": "Mettre un mot sur l'état."},
    "Seguir con lo que estabas haciendo. Sin conclusiones.": {
        "en": "Carry on with what you were doing. With no conclusions.",
        "fr": "Poursuivre ce que vous faisiez. Sans conclusions."},

    "Treinta segundos cada uno. Tres minutos al día en total. Es deliberadamente poco: lo "
    "que se busca en los primeros meses no es cantidad, es que el hábito exista.": {
        "en": "Thirty seconds each. Three minutes a day in all. It is deliberately little: "
              "what is wanted in the first months is not quantity, it is that the habit should "
              "exist.",
        "fr": "Trente secondes chacun. Trois minutes par jour en tout. C'est délibérément peu : "
              "ce qu'on cherche dans les premiers mois n'est pas la quantité, c'est que "
              "l'habitude existe."},

    "Cómo acordarse": {"en": "How to remember", "fr": "Comment s'en souvenir"},
}
