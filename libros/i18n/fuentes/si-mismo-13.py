# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · el ejercicio de las dos columnas y los papeles
====================================================================
Los cinco papeles llevan nombre de persona —el competente, el hijo, el
agradable, el crítico, el de la pareja— y se traducen como sustantivos con
artículo, igual que en el original. En inglés se resuelven con «the competent
one» y sus hermanos, que es la forma que el idioma tiene de nombrar un papel
sin nombrar a nadie.

«Recordarse a sí mismo» es un término de la tradición y tiene forma fijada:
self-remembering en inglés, rappel de soi en francés. Va donde va, y el
párrafo que lo introduce lo presenta como término y no como descripción.
"""

T = {
    "Reparte todos los elementos del asunto. Todos, incluidos los incómodos.": {
        "en": "Distribute every element of the matter. All of them, the uncomfortable ones "
              "included.",
        "fr": "Répartissez tous les éléments de l'affaire. Tous, y compris les inconfortables."},

    "Tacha la columna derecha. Literalmente: pásale una raya.": {
        "en": "Cross out the right-hand column. Literally: draw a line through it.",
        "fr": "Barrez la colonne de droite. Littéralement : tirez un trait dessus."},

    "De la columna izquierda, elige lo primero y hazlo hoy. Suele ser mucho más pequeño de "
    "lo que parecía desde dentro del problema.": {
        "en": "From the left-hand column, choose the first item and do it today. It is usually "
              "far smaller than it looked from inside the problem.",
        "fr": "Dans la colonne de gauche, choisissez le premier point et faites-le aujourd'hui. "
              "C'est en général bien plus petit que cela ne paraissait depuis l'intérieur du "
              "problème."},

    "Por qué funciona este ejercicio": {
        "en": "Why this exercise works", "fr": "Pourquoi cet exercice fonctionne"},

    "Porque la mayor parte del peso de un problema está en la columna derecha, y la columna "
    "derecha no admite trabajo: solo admite rumiación. Separar las dos no resuelve nada por "
    "sí mismo, y sin embargo cambia bastante la sensación — porque el agotamiento no venía "
    "del problema, venía de empujar contra lo que no se mueve.": {
        "en": "Because most of a problem's weight is in the right-hand column, and the "
              "right-hand column allows no work: it allows only rumination. Separating the two "
              "resolves nothing in itself, and yet it changes the feeling a good deal — "
              "because the exhaustion was not coming from the problem, it was coming from "
              "pushing against what does not move.",
        "fr": "Parce que l'essentiel du poids d'un problème est dans la colonne de droite, et "
              "la colonne de droite n'admet aucun travail : elle n'admet que la rumination. "
              "Séparer les deux ne résout rien en soi, et pourtant cela change pas mal la "
              "sensation — car l'épuisement ne venait pas du problème, il venait de pousser "
              "contre ce qui ne bouge pas."},

    # ── Los papeles ────────────────────────────────────────────────────────
    "Con unas semanas de observación aparece un hallazgo que suele incomodar: no hay una "
    "sola persona ahí dentro. Hay varias formas de ser que se alternan según el contexto, "
    "con voz distinta, vocabulario distinto y a veces opiniones incompatibles entre sí.": {
        "en": "After a few weeks of observation a finding appears that tends to be "
              "uncomfortable: there is not one single person in there. There are several ways "
              "of being that take turns according to the context, with a different voice, a "
              "different vocabulary and sometimes opinions incompatible with one another.",
        "fr": "Après quelques semaines d'observation apparaît une découverte qui met en général "
              "mal à l'aise : il n'y a pas là-dedans une seule personne. Il y a plusieurs "
              "façons d'être qui alternent selon le contexte, avec une voix différente, un "
              "vocabulaire différent et parfois des opinions incompatibles entre elles."},

    "Cómo se detectan": {"en": "How they are detected", "fr": "Comment on les repère"},

    "Por la voz, que es el indicador más fiable. Grábate hablando con tu jefe y con tu mejor "
    "amigo el mismo día: cambia el tono, cambia la velocidad, cambia el registro de "
    "vocabulario. Por la postura, que también cambia. Y por las opiniones: casi todo el "
    "mundo sostiene, en contextos distintos, cosas que no encajan entre sí, y no lo nota "
    "porque nunca están las dos en la misma habitación.": {
        "en": "By the voice, which is the most reliable indicator. Record yourself talking to "
              "your boss and to your best friend on the same day: the tone changes, the speed "
              "changes, the register of vocabulary changes. By the posture, which also "
              "changes. And by the opinions: almost everyone holds, in different contexts, "
              "things that do not fit together, and does not notice because the two are never "
              "in the same room.",
        "fr": "Par la voix, qui est l'indicateur le plus fiable. Enregistrez-vous parlant à "
              "votre patron et à votre meilleur ami le même jour : le ton change, la vitesse "
              "change, le registre de vocabulaire change. Par la posture, qui change aussi. Et "
              "par les opinions : presque tout le monde soutient, dans des contextes "
              "différents, des choses qui ne s'accordent pas entre elles, et ne le remarque pas "
              "parce que les deux ne sont jamais dans la même pièce."},

    "Los papeles más comunes": {
        "en": "The commonest roles", "fr": "Les rôles les plus courants"},

    "El competente": {"en": "The competent one", "fr": "Le compétent"},
    "En el trabajo. No admite no saber. Suele ser el más desarrollado y el más agotador de "
    "sostener.": {
        "en": "At work. It cannot admit to not knowing. It is usually the most developed and "
              "the most exhausting to sustain.",
        "fr": "Au travail. Il n'admet pas de ne pas savoir. C'est en général le plus développé "
              "et le plus épuisant à tenir."},

    "El hijo": {"en": "The child", "fr": "L'enfant"},
    "Con la familia de origen. Recupera de golpe reacciones de hace veinte años, con una "
    "fidelidad que asusta.": {
        "en": "With the family you came from. It recovers reactions from twenty years ago all "
              "at once, with a fidelity that is frightening.",
        "fr": "Avec la famille d'origine. Il récupère d'un coup des réactions d'il y a vingt "
              "ans, avec une fidélité qui fait peur."},

    "El agradable": {"en": "The agreeable one", "fr": "L'agréable"},
    "Con desconocidos y en grupo. Cede en cosas que no quería ceder y se entera después.": {
        "en": "With strangers and in groups. It gives way on things it did not want to give "
              "way on and finds out afterwards.",
        "fr": "Avec des inconnus et en groupe. Il cède sur des choses qu'il ne voulait pas "
              "céder et s'en aperçoit après."},

    "El crítico": {"en": "The critic", "fr": "Le critique"},
    "A solas y por dentro. Es el que habla cuando no hay nadie y el que peor trata al que lo "
    "escucha.": {
        "en": "Alone and on the inside. It is the one that talks when there is nobody there "
              "and the one that treats its listener worst.",
        "fr": "Seul et au-dedans. C'est celui qui parle quand il n'y a personne et celui qui "
              "traite le plus mal celui qui l'écoute."},

    "El de la pareja": {"en": "The partner", "fr": "Celui du couple"},
    "El más ciego de todos, porque el otro suele ver de él mucho más que uno mismo.": {
        "en": "The blindest of them all, because the other person usually sees far more of it "
              "than you do.",
        "fr": "Le plus aveugle de tous, parce que l'autre en voit d'ordinaire bien plus que "
              "soi-même."},

    "Qué se hace con esto": {
        "en": "What is done with this", "fr": "Que fait-on de cela"},

    "Nada, al principio. Se observa y se anota cuál está al mando: es el dato más útil que "
    "puede tener el cuaderno, porque explica de golpe reacciones que aisladas no tenían "
    "sentido. «Estaba el competente» aclara más que cualquier análisis de por qué te "
    "pusiste a la defensiva en esa reunión.": {
        "en": "Nothing, at first. You observe and you write down which one is in charge: it is "
              "the most useful piece of data the notebook can hold, because it explains at a "
              "stroke reactions that made no sense in isolation. «The competent one was there» "
              "clarifies more than any analysis of why you went on the defensive in that "
              "meeting.",
        "fr": "Rien, au début. On observe et on note lequel commande : c'est la donnée la plus "
              "utile que puisse contenir le carnet, car elle explique d'un coup des réactions "
              "qui, isolées, n'avaient pas de sens. « C'était le compétent » éclaire davantage "
              "que n'importe quelle analyse de pourquoi vous vous êtes mis sur la défensive à "
              "cette réunion."},

    "Con el tiempo aparece la segunda parte, y es lo que la tradición llama recordarse a sí "
    "mismo: notar que hay algo que permanece mientras los papeles se alternan. No es una "
    "experiencia mística ni tiene nada de espectacular; es la sensación bastante sobria de "
    "estar presente en varios contextos siendo el mismo. Aparece sola, a los meses, y no se "
    "puede forzar.": {
        "en": "In time the second part appears, and it is what the tradition calls "
              "self-remembering: noticing that there is something that stays while the roles "
              "take turns. It is not a mystical experience and there is nothing spectacular "
              "about it; it is the fairly sober sensation of being present in several contexts "
              "as the same person. It appears on its own, after months, and it cannot be "
              "forced.",
        "fr": "Avec le temps apparaît la seconde partie, et c'est ce que la tradition appelle "
              "le rappel de soi : remarquer qu'il y a quelque chose qui demeure pendant que "
              "les rôles alternent. Ce n'est pas une expérience mystique et cela n'a rien de "
              "spectaculaire ; c'est la sensation assez sobre d'être présent dans plusieurs "
              "contextes en étant le même. Cela apparaît tout seul, au bout de quelques mois, "
              "et cela ne se force pas."},

    "El malentendido que hay que evitar": {
        "en": "The misunderstanding to avoid",
        "fr": "Le malentendu qu'il faut éviter"},

    "Descubrir que hay varios papeles no significa que haya un papel auténtico escondido "
    "debajo y los demás sean máscaras. Esa idea es atractiva y no aguanta la observación: "
    "los cinco son igual de reales y todos son tú. Lo que se busca no es encontrar al "
    "verdadero, es dejar de estar dormido dentro de cada uno.": {
        "en": "Discovering that there are several roles does not mean there is an authentic "
              "role hidden underneath and the rest are masks. That idea is attractive and does "
              "not survive observation: all five are equally real and all of them are you. "
              "What is sought is not to find the true one, it is to stop being asleep inside "
              "each of them.",
        "fr": "Découvrir qu'il y a plusieurs rôles ne signifie pas qu'il y aurait en dessous un "
              "rôle authentique et que les autres seraient des masques. Cette idée est "
              "séduisante et ne résiste pas à l'observation : les cinq sont également réels et "
              "tous sont vous. Ce qu'on cherche n'est pas de trouver le vrai, c'est de cesser "
              "de dormir à l'intérieur de chacun."},

    # ── Las cuentas pendientes ─────────────────────────────────────────────
    "Marco Aurelio vuelve una y otra vez, en sus notas, sobre el mismo asunto: la gente que "
    "le molesta y el tiempo que gasta molestándose. Que un emperador con poder absoluto "
    "dedicara tantas páginas a eso dice bastante sobre lo universal del problema.": {
        "en": "Marcus Aurelius returns again and again, in his notes, to the same matter: the "
              "people who annoy him and the time he spends being annoyed. That an emperor with "
              "absolute power devoted so many pages to it says a good deal about how universal "
              "the problem is.",
        "fr": "Marc Aurèle revient encore et encore, dans ses notes, sur le même sujet : les "
              "gens qui l'agacent et le temps qu'il passe à s'agacer. Qu'un empereur au pouvoir "
              "absolu ait consacré tant de pages à cela en dit long sur le caractère universel "
              "du problème."},

    "Qué es una cuenta pendiente": {
        "en": "What an unsettled account is",
        "fr": "Ce qu'est un compte en suspens"},
}
