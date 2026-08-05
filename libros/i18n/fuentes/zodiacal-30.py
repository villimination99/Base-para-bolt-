# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · los ocho tramos lunares y los días planetarios
================================================================
Los nombres de las ocho fases van aquí en texto corrido y no en la lámina, así
que pueden ir completos: waxing gibbous, gibbeuse croissante, sin la
abreviatura de nueve caracteres que impone el dibujo.

Los nombres de los días de la semana NO se traducen. El capítulo los cita como
prueba —la semana es un artefacto astrológico y sus nombres lo delatan— y la
prueba está justamente en la forma que tienen en cada lengua. El original
enumera el castellano y el francés, y añade el inglés solo donde el inglés
conserva el planeta: Monday, Saturday, Sunday. Esa selección es el argumento y
se copia igual en las tres ediciones; lo único que se traduce es la glosa que
va detrás del punto.

«Lo que la Luna no hace» enumera cuatro efectos que se le atribuyen y no
tiene, y dice que la atribución es cultural y no física. Va literal: es lo que
autoriza el resto del capítulo.
"""

T = {
    "Sembrar. Se decide y se escribe qué se va a hacer. No se empieza todavía: se define.": {
        "en": "Sow. You decide and write down what you are going to do. You do not begin yet: "
              "you define.",
        "fr": "Semer. On décide et on écrit ce que l'on va faire. On ne commence pas encore : on "
              "définit."},

    "Creciente": {"en": "Waxing crescent", "fr": "Premier croissant"},
    "Empezar. El primer movimiento concreto, aunque sea mínimo.": {
        "en": "Begin. The first concrete movement, however small.",
        "fr": "Commencer. Le premier mouvement concret, si minime soit-il."},

    "Cuarto creciente": {"en": "First quarter", "fr": "Premier quartier"},
    "Decidir. Aparece el primer obstáculo real y hay que elegir cómo seguir.": {
        "en": "Decide. The first real obstacle appears and you have to choose how to go on.",
        "fr": "Décider. Le premier obstacle réel apparaît et il faut choisir comment continuer."},

    "Gibosa creciente": {"en": "Waxing gibbous", "fr": "Gibbeuse croissante"},
    "Sostener. El tramo aburrido, y el que separa los proyectos que salen de los que no.": {
        "en": "Sustain. The boring stretch, and the one that separates the projects that come "
              "off from the ones that do not.",
        "fr": "Tenir. Le tronçon ennuyeux, et celui qui sépare les projets qui aboutissent de "
              "ceux qui n'aboutissent pas."},

    "Luna llena": {"en": "Full moon", "fr": "Pleine lune"},
    "Culminar. Se mira lo hecho y se enseña. También el tramo en que todo se ve más intenso de "
    "lo que es.": {
        "en": "Culminate. You look at what has been done and you show it. Also the stretch in "
              "which everything looks more intense than it is.",
        "fr": "Culminer. On regarde ce qui a été fait et on le montre. C'est aussi le tronçon où "
              "tout paraît plus intense qu'il ne l'est."},

    "Gibosa menguante": {"en": "Waning gibbous", "fr": "Gibbeuse décroissante"},
    "Revisar. Se corrige con la información que ya se tiene y antes no se tenía.": {
        "en": "Review. You correct with the information you now have and did not have before.",
        "fr": "Revoir. On corrige avec l'information que l'on a désormais et que l'on n'avait pas "
              "avant."},

    "Cuarto menguante": {"en": "Last quarter", "fr": "Dernier quartier"},
    "Soltar. Se quita lo que no va a llegar. Es el tramo que casi nadie hace.": {
        "en": "Release. You take away what is not going to arrive. It is the stretch hardly "
              "anybody does.",
        "fr": "Lâcher. On retire ce qui n'arrivera pas. C'est le tronçon que presque personne ne "
              "fait."},

    "Menguante": {"en": "Waning crescent", "fr": "Dernier croissant"},
    "Cerrar. Se anota qué ha funcionado y se deja el terreno limpio para el ciclo siguiente.": {
        "en": "Close. You write down what worked and leave the ground clear for the next cycle.",
        "fr": "Clore. On note ce qui a fonctionné et on laisse le terrain net pour le cycle "
              "suivant."},

    "Cómo usarlo con este libro": {
        "en": "How to use it with this book", "fr": "Comment s'en servir avec ce livre"},

    "Cada mes del recorrido de doce meses coincide aproximadamente con un ciclo lunar. Empieza "
    "la práctica del signo en luna nueva y no antes.": {
        "en": "Each month of the twelve-month journey coincides roughly with a lunar cycle. "
              "Begin the sign's practice at the new moon and not before.",
        "fr": "Chaque mois du parcours de douze mois coïncide à peu près avec un cycle lunaire. "
              "Commencez la pratique du signe à la nouvelle lune et pas avant."},

    "Las cuatro semanas de la práctica encajan con las cuatro fases: definir, empezar, "
    "sostener, cerrar. La práctica del signo ya está escrita en cuatro pasos precisamente por "
    "esto.": {
        "en": "The four weeks of the practice fit the four phases: define, begin, sustain, "
              "close. The sign's practice is already written in four steps precisely for this "
              "reason.",
        "fr": "Les quatre semaines de la pratique s'accordent aux quatre phases : définir, "
              "commencer, tenir, clore. La pratique du signe est déjà écrite en quatre pas "
              "précisément pour cela."},

    "Escribe el registro del mes en luna menguante, no en llena. En llena todo parece más "
    "importante de lo que es y el registro sale exagerado.": {
        "en": "Write the month's record at the waning moon, not at the full. At the full "
              "everything looks more important than it is and the record comes out exaggerated.",
        "fr": "Écrivez le registre du mois à la lune décroissante, non à la pleine. À la pleine "
              "tout paraît plus important qu'il ne l'est et le registre sort exagéré."},

    "Si un mes se te descuadra, no lo arregles: anótalo. El ciclo que se rompe informa más que "
    "el que sale perfecto.": {
        "en": "If a month goes out of true on you, do not fix it: write it down. The cycle that "
              "breaks tells you more than the one that comes out perfect.",
        "fr": "Si un mois se dérègle, ne le réparez pas : notez-le. Le cycle qui se casse "
              "renseigne plus que celui qui sort parfait."},

    "Lo que la Luna no hace": {
        "en": "What the Moon does not do", "fr": "Ce que la Lune ne fait pas"},

    "No provoca partos, no altera el sueño de forma demostrada, no determina el resultado de "
    "una decisión y no explica el mal humor de nadie. La atribución de esos efectos es "
    "cultural, no física, y este libro no la sostiene. Lo que aquí se propone es usar un ciclo "
    "visible y regular como armazón temporal: la misma función que cumple una agenda, con la "
    "ventaja de que a esta no hay que darle cuerda.": {
        "en": "It does not bring on births, it does not alter sleep in any demonstrated way, it "
              "does not determine the outcome of a decision and it does not explain anybody's "
              "bad temper. The attribution of those effects is cultural, not physical, and this "
              "book does not maintain it. What is proposed here is to use a visible and regular "
              "cycle as a temporal frame: the same function a diary performs, with the "
              "advantage that this one does not have to be wound up.",
        "fr": "Elle ne provoque pas les accouchements, elle n'altère pas le sommeil de façon "
              "démontrée, elle ne détermine pas l'issue d'une décision et elle n'explique la "
              "mauvaise humeur de personne. L'attribution de ces effets est culturelle, non "
              "physique, et ce livre ne la soutient pas. Ce que l'on propose ici, c'est "
              "d'employer un cycle visible et régulier comme ossature temporelle : la même "
              "fonction que remplit un agenda, avec l'avantage que celui-ci n'a pas besoin "
              "d'être remonté."},

    # ── Los días y las horas planetarias ───────────────────────────────────
    "Capítulo 28": {"en": "Chapter 28", "fr": "Chapitre 28"},

    "Este capítulo recoge la parte más técnica y menos divulgada del sistema clásico, y "
    "también la que produce el pequeño asombro de ver que una costumbre cotidiana esconde una "
    "estructura matemática antigua. La semana que usas todos los días es un artefacto "
    "astrológico, y sus nombres lo delatan.": {
        "en": "This chapter gathers the most technical and least publicised part of the "
              "classical system, and also the part that produces the small astonishment of "
              "seeing that an everyday custom hides an ancient mathematical structure. The week "
              "you use every day is an astrological artefact, and its names give it away.",
        "fr": "Ce chapitre rassemble la partie la plus technique et la moins vulgarisée du "
              "système classique, et aussi celle qui produit le petit étonnement de voir qu'une "
              "coutume quotidienne cache une structure mathématique ancienne. La semaine dont "
              "vous vous servez tous les jours est un artefact astrologique, et ses noms la "
              "trahissent."},

    "Los siete días": {"en": "The seven days", "fr": "Les sept jours"},
    "Cada día y su regente": {
        "en": "Each day and its ruler", "fr": "Chaque jour et son régent"},

    "Luna · lunes, lundi, Monday. Rutina, casa, cuidado, memoria": {
        "en": "Moon · lunes, lundi, Monday. Routine, home, care, memory",
        "fr": "Lune · lunes, lundi, Monday. Routine, maison, soin, mémoire"},

    "Marte · martes, mardi. Empuje, conflicto, ejercicio, decisión": {
        "en": "Mars · martes, mardi. Drive, conflict, exercise, decision",
        "fr": "Mars · martes, mardi. Élan, conflit, exercice, décision"},

    "Mercurio · miércoles, mercredi. Palabra, trámite, estudio": {
        "en": "Mercury · miércoles, mercredi. Word, paperwork, study",
        "fr": "Mercure · miércoles, mercredi. Parole, démarche, étude"},

    "Júpiter · jueves, jeudi. Expansión, acuerdo, viaje, generosidad": {
        "en": "Jupiter · jueves, jeudi. Expansion, agreement, travel, generosity",
        "fr": "Jupiter · jueves, jeudi. Expansion, accord, voyage, générosité"},
}
