# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · el cuaderno de tiradas y el plan de doce meses
======================================================================
La regla que resume las seis prohibiciones viene partida en cuatro <span>
porque la lámina la compone en cuatro renglones. Se traduce renglón a renglón,
manteniendo el corte donde está: cada trozo termina donde el original y el
conjunto vuelve a leerse como una frase seguida.

La casilla de revisión se deja EN BLANCO, con versales, en los tres idiomas.
Es una instrucción y las versales son la instrucción.
"""

T = {
    "Si quien consulta está en crisis aguda —duelo reciente, ruptura de días, ansiedad "
    "alta, pensamientos de hacerse daño— no se le lee. No porque el tarot sea peligroso, "
    "sino porque en ese estado cualquier figura ambigua se lee del peor modo posible, y "
    "porque lo que esa persona necesita es otra cosa y tú se lo estás retrasando. La "
    "respuesta correcta es acompañar y señalar hacia ayuda profesional.": {
        "en": "If the person consulting is in acute crisis —recent bereavement, a break-up of "
              "days ago, high anxiety, thoughts of self-harm— you do not read for them. Not "
              "because tarot is dangerous, but because in that state any ambiguous figure is "
              "read in the worst possible way, and because what that person needs is something "
              "else and you are delaying it. The correct response is to stay with them and "
              "point towards professional help.",
        "fr": "Si la personne qui consulte est en crise aiguë —deuil récent, rupture d'il y a "
              "quelques jours, anxiété élevée, pensées de se faire du mal— on ne lit pas pour "
              "elle. Non parce que le tarot serait dangereux, mais parce que dans cet état "
              "toute figure ambiguë se lit de la pire façon possible, et parce que ce dont "
              "cette personne a besoin est autre chose et que vous le lui retardez. La bonne "
              "réponse est d'accompagner et d'orienter vers une aide professionnelle."},

    "Cómo se dice un no": {"en": "How to say no", "fr": "Comment on dit non"},

    "Sin misterio y sin dárselas de nada: «esto no se lee con cartas». Si insisten, se "
    "repite igual. Un lector que acepta cualquier pregunta para no decepcionar acaba "
    "haciendo daño, y lo hará sin enterarse — porque las consecuencias de una mala lectura "
    "casi nunca vuelven al que la hizo.": {
        "en": "With no mystery and no airs: «this is not something you read with cards». If "
              "they insist, you repeat it the same way. A reader who accepts any question so "
              "as not to disappoint ends up doing harm, and will do it without noticing — "
              "because the consequences of a bad reading almost never come back to the person "
              "who gave it.",
        "fr": "Sans mystère et sans se donner d'importance : « cela ne se lit pas avec des "
              "cartes ». S'ils insistent, on le répète à l'identique. Un lecteur qui accepte "
              "n'importe quelle question pour ne pas décevoir finit par faire du mal, et il le "
              "fera sans s'en apercevoir — car les conséquences d'une mauvaise lecture ne "
              "reviennent presque jamais à celui qui l'a faite."},

    "<span>La regla que resume las seis:</span><span>el tarot sirve para ordenar lo que el "
    "consultante ya sabe.</span><span>Nunca para sustituir lo que no sabe</span><span>y "
    "tiene que preguntarle a otro.</span>": {
        "en": "<span>The rule that sums up the six:</span><span>tarot serves to order what the "
              "querent already knows.</span><span>Never to replace what they do not "
              "know</span><span>and have to ask someone else.</span>",
        "fr": "<span>La règle qui résume les six :</span><span>le tarot sert à ordonner ce que "
              "le consultant sait déjà.</span><span>Jamais à remplacer ce qu'il ne sait "
              "pas</span><span>et doit demander à un autre.</span>"},

    # ── El cuaderno ────────────────────────────────────────────────────────
    "Si de este libro solo conservas una práctica, conserva esta. El motivo es sencillo y no "
    "admite discusión: sin registro escrito no hay forma de saber si algo funciona.": {
        "en": "If you keep only one practice from this book, keep this one. The reason is "
              "simple and admits no argument: without a written record there is no way of "
              "knowing whether anything works.",
        "fr": "Si vous ne gardez qu'une seule pratique de ce livre, gardez celle-ci. La raison "
              "est simple et ne se discute pas : sans trace écrite, il n'y a aucun moyen de "
              "savoir si quelque chose fonctionne."},

    "Por qué en el tarot importa más que en nada": {
        "en": "Why it matters more in tarot than anywhere",
        "fr": "Pourquoi cela compte au tarot plus que partout ailleurs"},

    "Porque la lectura de cartas es el terreno más fértil que existe para el autoengaño. "
    "Una tirada ambigua interpretada a posteriori siempre parece haber acertado: la memoria "
    "selecciona lo que encajó y descarta lo demás sin avisar. El cuaderno es el único "
    "antídoto, y funciona por una razón muy simple: lo escrito antes no se puede reescribir "
    "después.": {
        "en": "Because card reading is the most fertile ground there is for self-deception. An "
              "ambiguous spread interpreted after the fact always looks as though it got it "
              "right: memory selects what fitted and discards the rest without warning. The "
              "notebook is the only antidote, and it works for a very simple reason: what was "
              "written before cannot be rewritten afterwards.",
        "fr": "Parce que la lecture des cartes est le terrain le plus fertile qui soit pour "
              "l'auto-illusion. Un tirage ambigu interprété après coup semble toujours avoir "
              "vu juste : la mémoire retient ce qui s'est ajusté et écarte le reste sans "
              "prévenir. Le carnet est le seul antidote, et il fonctionne pour une raison très "
              "simple : ce qui a été écrit avant ne peut pas être réécrit après."},

    "Entrada por tirada": {"en": "One entry per spread", "fr": "Une entrée par tirage"},

    "La pregunta": {"en": "The question", "fr": "La question"},
    "Textual, tal como se formuló. Sin arreglarla luego": {
        "en": "Verbatim, as it was asked. With no tidying up afterwards",
        "fr": "Textuelle, telle qu'elle a été formulée. Sans la retoucher ensuite"},

    "Tirada": {"en": "Spread", "fr": "Tirage"},
    "Las Tres · Cruz de Cuatro · El Espejo · otra": {
        "en": "The Three · Cross of Four · The Mirror · other",
        "fr": "Les Trois · Croix de Quatre · Le Miroir · autre"},

    "Las cartas": {"en": "The cards", "fr": "Les cartes"},
    "Por posición, con su orientación": {
        "en": "By position, with their orientation",
        "fr": "Par position, avec leur orientation"},

    "El conjunto": {"en": "The whole", "fr": "L'ensemble"},
    "Cuántos mayores · qué palo domina · números repetidos": {
        "en": "How many majors · which suit dominates · repeated numbers",
        "fr": "Combien de majeurs · quelle couleur domine · nombres répétés"},

    "La lectura": {"en": "The reading", "fr": "La lecture"},
    "Cuatro líneas como máximo. Si no cabe en cuatro, no la tenías clara": {
        "en": "Four lines at most. If it does not fit in four, you did not have it clear",
        "fr": "Quatre lignes au maximum. Si cela ne tient pas en quatre, vous ne l'aviez pas "
              "clair"},

    "La acción": {"en": "The action", "fr": "L'action"},
    "Lo que voy a hacer en los próximos siete días": {
        "en": "What I am going to do in the next seven days",
        "fr": "Ce que je vais faire dans les sept prochains jours"},

    "Revisión": {"en": "Review", "fr": "Révision"},
    "Se deja EN BLANCO. Se rellena a las cuatro semanas": {
        "en": "Left BLANK. Filled in after four weeks",
        "fr": "Laissée EN BLANC. Remplie au bout de quatre semaines"},

    "La casilla de revisión es todo el método": {
        "en": "The review box is the whole method",
        "fr": "La case de révision est toute la méthode"},

    "Cuatro semanas después se vuelve a la entrada y se anota, sin piedad, qué pasó: si la "
    "acción se hizo, si la lectura resultó pertinente o si fue un adorno. Cincuenta "
    "entradas con su revisión rellenada valen más que quinientas tiradas sin ella, y son la "
    "única forma de descubrir que hay cartas que llevas años leyendo mal.": {
        "en": "Four weeks later you go back to the entry and note down, without mercy, what "
              "happened: whether the action was carried out, whether the reading turned out to "
              "be pertinent or whether it was decoration. Fifty entries with their review "
              "filled in are worth more than five hundred spreads without it, and they are the "
              "only way of discovering that there are cards you have been reading wrongly for "
              "years.",
        "fr": "Quatre semaines plus tard, on revient à l'entrée et on note, sans pitié, ce qui "
              "s'est passé : si l'action a été faite, si la lecture s'est révélée pertinente "
              "ou si elle n'était qu'un ornement. Cinquante entrées avec leur révision remplie "
              "valent mieux que cinq cents tirages sans elle, et c'est la seule façon de "
              "découvrir qu'il y a des cartes que vous lisez de travers depuis des années."},

    "La revisión trimestral": {
        "en": "The quarterly review", "fr": "La révision trimestrielle"},

    "Cuenta las tiradas hechas y las revisiones rellenadas. El segundo número es el que "
    "importa.": {
        "en": "Count the spreads done and the reviews filled in. The second number is the one "
              "that matters.",
        "fr": "Comptez les tirages faits et les révisions remplies. C'est le second nombre qui "
              "compte."},
    "Cuenta cuántas acciones se ejecutaron de verdad. Por debajo de la mitad, no estás "
    "leyendo: estás consultando.": {
        "en": "Count how many actions were actually carried out. Below half, you are not "
              "reading: you are consulting.",
        "fr": "Comptez combien d'actions ont réellement été exécutées. En dessous de la moitié, "
              "vous ne lisez pas : vous consultez."},
    "Busca la carta que más te ha salido. Casi siempre hay una, y casi siempre señala un "
    "asunto que llevas sin resolver.": {
        "en": "Look for the card that has come up most. There is almost always one, and it "
              "almost always points to a matter you have left unresolved.",
        "fr": "Cherchez la carte qui est le plus souvent sortie. Il y en a presque toujours "
              "une, et elle signale presque toujours une affaire non réglée."},
    "Busca la lectura que resultó más equivocada y anota por qué. Este punto es el que "
    "produce el aprendizaje.": {
        "en": "Look for the reading that turned out most wrong and note down why. This point "
              "is the one that produces the learning.",
        "fr": "Cherchez la lecture qui s'est révélée la plus fausse et notez pourquoi. C'est ce "
              "point qui produit l'apprentissage."},

    # ── El plan de doce meses ──────────────────────────────────────────────
    "Un plan de doce meses. Es voluntario y es mejor que improvisar.": {
        "en": "A twelve-month plan. It is optional and it is better than improvising.",
        "fr": "Un plan de douze mois. Il est facultatif et il vaut mieux qu'improviser."},

    "Solo los veintidós mayores, apartados del resto del mazo. Una carta al día, sacada por "
    "la mañana, leída en tres líneas y revisada por la noche. Noventa entradas.": {
        "en": "Only the twenty-two majors, separated from the rest of the deck. One card a "
              "day, drawn in the morning, read in three lines and reviewed at night. Ninety "
              "entries.",
        "fr": "Seulement les vingt-deux majeurs, mis à part du reste du jeu. Une carte par "
              "jour, tirée le matin, lue en trois lignes et revue le soir. Quatre-vingt-dix "
              "entrées."},

    "Se añaden los cuatro palos con la escala del número. Una tirada de Las Tres por "
    "semana, con revisión a cuatro semanas.": {
        "en": "The four suits are added, with the scale of number. One spread of The Three a "
              "week, with a review at four weeks.",
        "fr": "On ajoute les quatre couleurs avec l'échelle du nombre. Un tirage des Trois par "
              "semaine, avec révision à quatre semaines."},

    "Se añaden los decanatos: cada carta menor se lee también por su signo y su regente. "
    "Aquí es donde conviene tener a mano la tabla de decanatos y regentes del capítulo "
    "once.": {
        "en": "The decans are added: each minor card is also read by its sign and its ruler. "
              "This is where it is worth having the table of decans and rulers from chapter "
              "eleven to hand.",
        "fr": "On ajoute les décans : chaque carte mineure se lit aussi par son signe et son "
              "régent. C'est ici qu'il vaut mieux avoir sous la main la table des décans et "
              "des régents du chapitre onze."},

    "No se añade nada. Se sostiene, se revisa el año y se releen las primeras noventa "
    "entradas. Ese último ejercicio es el que enseña.": {
        "en": "Nothing is added. You keep it up, you review the year and you reread the first "
              "ninety entries. That last exercise is the one that teaches.",
        "fr": "On n'ajoute rien. On tient, on révise l'année et on relit les quatre-vingt-dix "
              "premières entrées. C'est ce dernier exercice qui enseigne."},

    "Revisiones rellenadas frente a tiradas hechas. Por encima del setenta por ciento hay "
    "práctica.": {
        "en": "Reviews filled in against spreads done. Above seventy per cent there is a "
              "practice.",
        "fr": "Révisions remplies face aux tirages faits. Au-dessus de soixante-dix pour cent, "
              "il y a une pratique."},
    "Acciones ejecutadas frente a acciones anotadas. Es la medida de si el instrumento está "
    "sirviendo para algo.": {
        "en": "Actions carried out against actions written down. It is the measure of whether "
              "the instrument is being any use.",
        "fr": "Actions exécutées face aux actions notées. C'est la mesure de savoir si "
              "l'instrument sert à quelque chose."},
    "Coincidencia entre tu lectura de hoy y la de hace seis meses sobre la misma tirada. Es "
    "la medida de si tienes método o improvisas.": {
        "en": "Agreement between today's reading and the one from six months ago on the same "
              "spread. It is the measure of whether you have a method or are improvising.",
        "fr": "Concordance entre votre lecture d'aujourd'hui et celle d'il y a six mois sur le "
              "même tirage. C'est la mesure de savoir si vous avez une méthode ou si vous "
              "improvisez."},

    "Y la advertencia del segundo año": {
        "en": "And the warning for the second year",
        "fr": "Et l'avertissement de la deuxième année"},

    "El riesgo no es abandonar: es la fluidez. Cuando las setenta y ocho se leen sin "
    "esfuerzo, la tentación es leer rápido y bonito, y ahí la estructura empieza a estorbar "
    "y se abandona sin darse cuenta. La señal de alarma es dejar de contar los mayores "
    "antes de interpretar. Cuando llegues ahí, vuelve al capítulo 12 y a la casilla de "
    "revisión.": {
        "en": "The risk is not giving up: it is fluency. When the seventy-eight are read "
              "effortlessly, the temptation is to read fast and prettily, and there the "
              "structure starts to get in the way and gets dropped without your noticing. The "
              "warning sign is no longer counting the majors before interpreting. When you get "
              "there, go back to chapter 12 and to the review box.",
        "fr": "Le risque n'est pas d'abandonner : c'est l'aisance. Quand les soixante-dix-huit "
              "se lisent sans effort, la tentation est de lire vite et joliment, et là la "
              "structure commence à gêner et se laisse tomber sans qu'on s'en aperçoive. Le "
              "signal d'alarme, c'est de cesser de compter les majeurs avant d'interpréter. "
              "Quand vous y arrivez, revenez au chapitre 12 et à la case de révision."},

    "Los términos de este libro, para poder leer cualquier otro tratado sin perderse.": {
        "en": "This book's terms, so that any other treatise can be read without getting lost.",
        "fr": "Les termes de ce livre, pour pouvoir lire n'importe quel autre traité sans se "
              "perdre."},
}
