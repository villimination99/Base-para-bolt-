# -*- coding: utf-8 -*-
"""
CÓDICE DE LA VOLUNTAD · resto del capítulo 2 y capítulo 3
=========================================================
Nota de vocabulario: «cumplimiento» se traduce por «adherence» en inglés y por
«observance» en francés, que es el término que usan de verdad los documentos
de salud pública en cada idioma. «Compliance» y «compliance» suenan a
obediencia y el libro sostiene exactamente lo contrario.
"""

T = {
    # ── Los cinco dominios, uno a uno ──────────────────────────────────────
    "Nutricional": {"en": "Nutritional", "fr": "Nutritionnel"},
    "Lo que entra y cuándo. Si está bajo: no se recupera de lo que se entrena": {
        "en": "What goes in and when. If it is low: you do not recover from what you train",
        "fr": "Ce qui entre et quand. S'il est bas : on ne récupère pas de ce que l'on "
              "s'entraîne"},
    "Mental": {"en": "Mental", "fr": "Mental"},
    "Objetivos, atención, diálogo interno y activación. Si está bajo: nada se sostiene "
    "más de unas semanas": {
        "en": "Goals, attention, self-talk and arousal. If it is low: nothing holds for "
              "more than a few weeks",
        "fr": "Objectifs, attention, discours intérieur et activation. S'il est bas : rien "
              "ne tient plus de quelques semaines"},
    "Del sueño": {"en": "Sleep", "fr": "Sommeil"},
    "Duración, horario y calidad. Si está bajo: se hunden los otros cuatro a la vez": {
        "en": "Duration, timing and quality. If it is low: the other four sink at once",
        "fr": "Durée, horaire et qualité. S'il est bas : les quatre autres s'effondrent "
              "d'un coup"},
    "Espiritual": {"en": "Spiritual", "fr": "Spirituel"},
    "Sentido, valores y propósito propio. Si está bajo: solo tú puedes juzgarlo, y por "
    "eso aquí no se juzga": {
        "en": "Meaning, values and your own purpose. If it is low: only you can judge it, "
              "and that is why it is not judged here",
        "fr": "Sens, valeurs et projet personnel. S'il est bas : vous seul pouvez en juger, "
              "et c'est pourquoi on n'en juge pas ici"},

    "La regla que hace útil el modelo": {
        "en": "The rule that makes the model useful",
        "fr": "La règle qui rend le modèle utile"},

    "Un dominio en mal estado limita a los demás, y lo hace de forma silenciosa. Quien "
    "duerme cinco horas no rinde en el gimnasio por mucho que su programa sea excelente. "
    "Quien come mal no recupera. Quien tiene la cabeza en otra parte no sostiene ningún "
    "hábito por bueno que sea el diseño. El eslabón que falla no se compensa apretando los "
    "otros: los arrastra.": {
        "en": "A domain in poor shape limits the others, and it does so silently. Someone "
              "sleeping five hours will not perform in the gym however excellent the "
              "programme. Someone eating badly does not recover. Someone whose head is "
              "elsewhere sustains no habit, however good the design. The failing link is "
              "not compensated by squeezing the others: it drags them down.",
        "fr": "Un domaine en mauvais état limite les autres, et il le fait en silence. Qui "
              "dort cinq heures ne rend rien en salle, aussi excellent que soit son "
              "programme. Qui mange mal ne récupère pas. Qui a la tête ailleurs ne tient "
              "aucune habitude, aussi bonne que soit la conception. Le maillon qui lâche ne "
              "se compense pas en serrant les autres : il les entraîne avec lui."},

    "De ahí sale el consejo de diagnóstico más útil de este libro: cuando algo no "
    "funciona, la pregunta correcta no es «¿cómo me esfuerzo más?» sino «¿cuál de los "
    "cinco está roto?». Nueve de cada diez veces es el sueño, y casi nadie lo mira primero.": {
        "en": "From that comes the most useful diagnostic advice in this book: when "
              "something is not working, the right question is not “how do I try harder?” "
              "but “which of the five is broken?”. Nine times out of ten it is sleep, and "
              "almost nobody looks there first.",
        "fr": "De là vient le conseil de diagnostic le plus utile de ce livre : quand "
              "quelque chose ne marche pas, la bonne question n'est pas « comment forcer "
              "davantage ? » mais « lequel des cinq est cassé ? ». Neuf fois sur dix c'est "
              "le sommeil, et presque personne ne regarde là en premier."},

    "El quinto dominio, y por qué no lo trato": {
        "en": "The fifth domain, and why I do not deal with it",
        "fr": "Le cinquième domaine, et pourquoi je ne le traite pas"},

    "La doctrina original incluye un dominio de sentido, valores y propósito. Lo menciono "
    "porque omitirlo sin avisar sería contar mal la fuente, y no lo desarrollo porque no "
    "me corresponde. Un libro que te vende entrenamiento no tiene ninguna autoridad para "
    "decirte para qué vives, y la industria del fitness lleva años cruzando esa línea con "
    "resultados que van del ridículo al daño.": {
        "en": "The original doctrine includes a domain of meaning, values and purpose. I "
              "mention it because leaving it out without saying so would misreport the "
              "source, and I do not develop it because it is not my place. A book that "
              "sells you training has no authority whatsoever to tell you what you live "
              "for, and the fitness industry has spent years crossing that line with "
              "results ranging from the ridiculous to the harmful.",
        "fr": "La doctrine d'origine comprend un domaine du sens, des valeurs et du projet. "
              "Je le mentionne parce que l'omettre sans le dire reviendrait à mal rapporter "
              "la source, et je ne le développe pas parce que ce n'est pas mon rôle. Un "
              "livre qui vous vend de l'entraînement n'a aucune autorité pour vous dire "
              "pourquoi vous vivez, et l'industrie du fitness passe cette ligne depuis des "
              "années, avec des résultats qui vont du ridicule au nuisible."},

    "Lo único que diré es que la conexión existe y está en la doctrina: la gente sostiene "
    "mejor los hábitos que encajan con algo que le importa de verdad, y peor los que solo "
    "encajan con una imagen que quiere dar. Qué te importa de verdad es tuyo y no de este "
    "libro.": {
        "en": "The only thing I will say is that the connection exists and is in the "
              "doctrine: people sustain better the habits that fit something they genuinely "
              "care about, and worse the ones that only fit an image they want to project. "
              "What you genuinely care about is yours, not this book's.",
        "fr": "La seule chose que je dirai, c'est que le lien existe et figure dans la "
              "doctrine : on tient mieux les habitudes qui correspondent à quelque chose "
              "qui compte vraiment pour soi, et moins bien celles qui ne correspondent qu'à "
              "une image que l'on veut donner. Ce qui compte vraiment pour vous vous "
              "appartient, pas à ce livre."},

    "Cómo usar esto de forma práctica": {
        "en": "How to use this in practice", "fr": "Comment s'en servir concrètement"},

    "Puntúate del uno al cinco en los cuatro primeros dominios, hoy, sin pensarlo mucho. "
    "El más bajo es donde está tu siguiente mes de trabajo, y casi nunca es el que estabas "
    "a punto de elegir.": {
        "en": "Score yourself from one to five on the first four domains, today, without "
              "overthinking it. The lowest is where your next month of work lies, and it is "
              "almost never the one you were about to pick.",
        "fr": "Notez-vous de un à cinq sur les quatre premiers domaines, aujourd'hui, sans "
              "trop y réfléchir. Le plus bas est celui où se trouve votre prochain mois de "
              "travail, et ce n'est presque jamais celui que vous alliez choisir."},

    # ── Capítulo 3 ─────────────────────────────────────────────────────────
    "La única variable que domina": {
        "en": "The one variable that rules", "fr": "La seule variable qui commande"},

    "Hay una discusión que ocupa la mitad de internet y que está mal planteada desde la "
    "primera línea: cuál es la mejor dieta, cuál es el mejor método de entrenamiento. La "
    "respuesta, en cuanto se mira lo que ocurre a lo largo de meses y no de semanas, es "
    "siempre la misma y es incómoda para todos los que venden algo.": {
        "en": "There is an argument that takes up half the internet and that is badly put "
              "from its very first line: which is the best diet, which is the best training "
              "method. The answer, as soon as you look at what happens over months rather "
              "than weeks, is always the same one — and it is inconvenient for everybody "
              "who is selling something.",
        "fr": "Il y a un débat qui occupe la moitié d'internet et qui est mal posé dès la "
              "première ligne : quel est le meilleur régime, quelle est la meilleure "
              "méthode d'entraînement. La réponse, dès que l'on regarde ce qui se passe sur "
              "des mois et non sur des semaines, est toujours la même — et elle dérange "
              "tous ceux qui ont quelque chose à vendre."},

    '<span class="fig-n">La misma dieta, tres grados de cumplimiento</span> Las tres '
    "líneas representan el mismo método aplicado con distinto cumplimiento. La distancia "
    "entre ellas es mayor que la que suele haber entre dos métodos razonables distintos. "
    "Es un esquema conceptual y no los datos de un estudio concreto: dice qué variable "
    "manda, no cuánto exactamente.": {
        "en": '<span class="fig-n">The same diet, three degrees of adherence</span> The '
              "three lines represent the same method applied with different levels of "
              "adherence. The gap between them is wider than the gap you usually find "
              "between two different reasonable methods. This is a conceptual diagram and "
              "not data from a specific study: it says which variable rules, not exactly by "
              "how much.",
        "fr": '<span class="fig-n">Le même régime, trois degrés d\'observance</span> Les '
              "trois courbes représentent la même méthode appliquée avec des niveaux "
              "d'observance différents. L'écart entre elles est plus grand que celui qui "
              "sépare habituellement deux méthodes raisonnables différentes. C'est un "
              "schéma conceptuel et non les données d'une étude précise : il dit quelle "
              "variable commande, pas de combien exactement."},

    "Lo que esta lámina significa": {
        "en": "What this plate means", "fr": "Ce que cette planche signifie"},

    "Dos planes distintos, ambos razonables, cumplidos igual de bien, tienden a dar "
    "resultados parecidos. El mismo plan cumplido al noventa por ciento y al treinta da "
    "resultados que no se parecen en nada. Por lo tanto, la pregunta «¿cuál es mejor?» es "
    "menos útil que la pregunta «¿cuál voy a cumplir?», y esa segunda pregunta solo la "
    "puedes contestar tú porque depende de tu horario, tu cocina, tu trabajo y lo que te "
    "gusta comer.": {
        "en": "Two different plans, both reasonable, followed equally well, tend to give "
              "similar results. The same plan followed ninety per cent of the time and "
              "thirty per cent of the time gives results that look nothing alike. So the "
              "question “which is better?” is less useful than the question “which will I "
              "actually follow?”, and only you can answer the second one, because it "
              "depends on your schedule, your kitchen, your job and what you like to eat.",
        "fr": "Deux plans différents, tous deux raisonnables, suivis aussi bien l'un que "
              "l'autre, tendent à donner des résultats semblables. Le même plan suivi à "
              "quatre-vingt-dix pour cent et à trente pour cent donne des résultats qui "
              "n'ont rien à voir. Donc la question « lequel est le meilleur ? » est moins "
              "utile que la question « lequel vais-je réellement suivre ? », et seule vous "
              "pouvez répondre à la seconde, parce qu'elle dépend de votre emploi du temps, "
              "de votre cuisine, de votre travail et de ce que vous aimez manger."},

    "De aquí sale un criterio de elección que va contra todo el marketing del sector: "
    "entre dos planes, elige el peor de los dos si es el que vas a sostener. Un plan "
    "mediocre ejecutado durante dos años gana por goleada a uno óptimo ejecutado durante "
    "cinco semanas, y ese es el escenario real de la mayoría de la gente, no una hipótesis.": {
        "en": "From this comes a rule for choosing that runs against all the marketing in "
              "the sector: between two plans, pick the worse of the two if it is the one "
              "you will keep up. A mediocre plan run for two years beats an optimal one run "
              "for five weeks hands down, and that is most people's real situation, not a "
              "hypothesis.",
        "fr": "D'où un critère de choix qui va à l'encontre de tout le marketing du "
              "secteur : entre deux plans, choisissez le pire des deux si c'est celui que "
              "vous tiendrez. Un plan médiocre suivi pendant deux ans bat à plate couture "
              "un plan optimal suivi pendant cinq semaines, et c'est la situation réelle de "
              "la plupart des gens, pas une hypothèse."},

    "Las tres causas por las que un plan bueno se cae": {
        "en": "The three reasons a good plan collapses",
        "fr": "Les trois causes de l'effondrement d'un bon plan"},

    "Demasiado grande": {"en": "Too big", "fr": "Trop grand"},
    "El compromiso inicial se dimensiona con el entusiasmo del primer día, que es un "
    "estado temporal. Cuando el entusiasmo baja al nivel normal, el plan sigue teniendo el "
    "tamaño del día uno y ya no cabe.": {
        "en": "The initial commitment is sized against day-one enthusiasm, which is a "
              "temporary state. When the enthusiasm drops back to normal, the plan is still "
              "day-one sized and no longer fits.",
        "fr": "L'engagement initial est calibré sur l'enthousiasme du premier jour, qui est "
              "un état temporaire. Quand l'enthousiasme redescend à la normale, le plan a "
              "toujours la taille du jour un et il n'entre plus."},

    "Demasiada fricción": {"en": "Too much friction", "fr": "Trop de friction"},
    "Cada paso previo a la conducta es una oportunidad de que no ocurra. Un gimnasio a "
    "cuarenta minutos, una comida que exige comprar cuatro cosas raras, una app que hay "
    "que abrir y actualizar. La fricción no se nota el primer día y decide el mes tres.": {
        "en": "Every step that comes before the behaviour is a chance for it not to happen. "
              "A gym forty minutes away, a meal that requires buying four unusual things, "
              "an app you have to open and update. Friction is not noticeable on day one "
              "and it decides month three.",
        "fr": "Chaque étape qui précède le comportement est une occasion qu'il n'ait pas "
              "lieu. Une salle à quarante minutes, un repas qui exige d'acheter quatre "
              "choses inhabituelles, une appli qu'il faut ouvrir et mettre à jour. La "
              "friction ne se remarque pas le premier jour et décide du troisième mois."},

    "Todo o nada": {"en": "All or nothing", "fr": "Tout ou rien"},
    "El plan no contempla el fallo, así que el primer fallo lo invalida entero. Es la "
    "causa más común y la más fácil de arreglar, y tiene su propio capítulo.": {
        "en": "The plan makes no allowance for a lapse, so the first lapse invalidates the "
              "whole thing. It is the most common cause and the easiest to fix, and it has "
              "a chapter of its own.",
        "fr": "Le plan ne prévoit pas l'écart, si bien que le premier écart l'invalide en "
              "entier. C'est la cause la plus fréquente et la plus facile à corriger, et "
              "elle a son propre chapitre."},

    "Lo que sí dicen las guías oficiales sobre esto": {
        "en": "What the official guidelines do say about this",
        "fr": "Ce que les recommandations officielles disent bel et bien à ce sujet"},

    "Las guías de actividad física dedican espacio a las estrategias de cambio de conducta "
    "y mencionan, entre otras, el establecimiento de objetivos, el autorregistro, el apoyo "
    "social y la modificación del entorno. No es un descubrimiento de este libro: es un "
    "apartado poco leído de un documento muy citado.": {
        "en": "The physical activity guidelines give space to behaviour-change strategies "
              "and mention, among others, goal setting, self-monitoring, social support and "
              "modifying the environment. This is not a discovery of this book: it is a "
              "little-read section of a much-cited document.",
        "fr": "Les recommandations d'activité physique consacrent une place aux stratégies "
              "de changement de comportement et mentionnent, entre autres, la fixation "
              "d'objectifs, l'auto-observation, le soutien social et la modification de "
              "l'environnement. Ce n'est pas une découverte de ce livre : c'est une section "
              "peu lue d'un document très cité."},

    "El bucle y sus tres palancas": {
        "en": "The loop and its three levers", "fr": "La boucle et ses trois leviers"},
}
