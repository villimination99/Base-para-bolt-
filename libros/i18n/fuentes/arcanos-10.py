# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · los cuatro palos y las dieciséis figuras
================================================================
La discusión de las Espadas gira sobre un verbo: la espada corta y distingue,
que es lo que hace el pensamiento. Ese verbo es el argumento entero y se
traduce por el verbo equivalente en cada lengua, no por un sinónimo elegante.
Si se pierde el corte, se pierde la razón por la que el palo es Aire.

Las figuras se nombran como en cada baraja —Rey, Reina, Caballo y Sota son
King, Queen, Knight y Page en inglés; Roi, Reine, Cavalier y Valet en
francés—, y sus combinaciones con el palo se deducen, así que basta con que
los nombres coincidan con los de las láminas.
"""

T = {
    "El itinerario completo, en una línea": {
        "en": "The complete journey, in one line",
        "fr": "Le parcours complet, en une ligne"},

    "Del I al VI se reúne el equipo; del VII al XII se pone a prueba; del XIII al XVIII se "
    "derrumba y se recompone; del XIX al XXI se cierra. Y El Loco entra y sale por donde "
    "quiere, que es lo que significa no tener número. Cuando una tirada trae varios "
    "mayores, ese orden dice en qué tramo del recorrido está el asunto — y suele ser un "
    "tramo antes del que el consultante creía.": {
        "en": "From I to VI the kit is gathered; from VII to XII it is tested; from XIII to "
              "XVIII it collapses and is put back together; from XIX to XXI it closes. And The "
              "Fool comes and goes wherever he likes, which is what having no number means. "
              "When a spread brings several majors, that order says which stretch of the road "
              "the matter is in — and it is usually one stretch earlier than the querent "
              "thought.",
        "fr": "Du I au VI on rassemble l'équipement ; du VII au XII on le met à l'épreuve ; du "
              "XIII au XVIII il s'effondre et se recompose ; du XIX au XXI il se ferme. Et Le "
              "Mat entre et sort où il veut, ce que signifie n'avoir pas de numéro. Quand un "
              "tirage amène plusieurs majeurs, cet ordre dit dans quel tronçon du parcours se "
              "trouve l'affaire — et c'est en général un tronçon plus tôt que ne le croyait le "
              "consultant."},

    "Los menores se organizan por palos, y cada palo es un elemento y una facultad. "
    "Sabiendo eso, la mitad del significado de cada carta ya está puesta antes de mirar el "
    "número.": {
        "en": "The minor arcana are organised by suit, and each suit is an element and a "
              "faculty. Knowing that, half the meaning of each card is already in place before "
              "you look at the number.",
        "fr": "Les mineurs s'organisent par couleurs, et chaque couleur est un élément et une "
              "faculté. Sachant cela, la moitié du sens de chaque carte est déjà posée avant "
              "de regarder le nombre."},

    '<span class="fig-n">Lám. 3</span> Los cuatro palos con su elemento y sus cuatro '
    "figuras. Cada figura lleva además su propio elemento dentro del palo, y de ahí salen "
    "las dieciséis combinaciones.": {
        "en": '<span class="fig-n">Pl. 3</span> The four suits with their element and their '
              "four court cards. Each court card also carries its own element within the suit, "
              "and from that come the sixteen combinations.",
        "fr": '<span class="fig-n">Pl. 3</span> Les quatre couleurs avec leur élément et leurs '
              "quatre figures. Chaque figure porte en outre son propre élément dans la "
              "couleur, et de là viennent les seize combinaisons."},

    "Bastos · Fuego": {"en": "Wands · Fire", "fr": "Bâtons · Feu"},
    "La voluntad y la empresa. Lo que se emprende, se impulsa y se defiende. Área de la "
    "vida: proyectos, trabajo propio, iniciativa.": {
        "en": "Will and enterprise. What is undertaken, driven and defended. Area of life: "
              "projects, one's own work, initiative.",
        "fr": "La volonté et l'entreprise. Ce qu'on entreprend, ce qu'on pousse et ce qu'on "
              "défend. Domaine de vie : projets, travail à son compte, initiative."},

    "Copas · Agua": {"en": "Cups · Water", "fr": "Coupes · Eau"},
    "El sentimiento y el vínculo. Lo que se siente, se recuerda y se comparte. Área: "
    "relaciones, familia, estados de ánimo.": {
        "en": "Feeling and the bond. What is felt, remembered and shared. Area: relationships, "
              "family, states of mind.",
        "fr": "Le sentiment et le lien. Ce qu'on ressent, ce dont on se souvient et ce qu'on "
              "partage. Domaine : relations, famille, états d'âme."},

    "Espadas · Aire": {"en": "Swords · Air", "fr": "Épées · Air"},
    "El pensamiento y la palabra. Lo que se decide, se discute y se corta. Área: "
    "decisiones, conflictos, comunicación.": {
        "en": "Thought and the word. What is decided, argued and cut. Area: decisions, "
              "conflicts, communication.",
        "fr": "La pensée et la parole. Ce qu'on décide, ce qu'on discute et ce qu'on tranche. "
              "Domaine : décisions, conflits, communication."},

    "Oros · Tierra": {"en": "Pentacles · Earth", "fr": "Deniers · Terre"},
    "El cuerpo y lo concreto. Lo que se sostiene, se produce y se cuenta. Área: dinero, "
    "salud, casa, trabajo por cuenta ajena.": {
        "en": "The body and the concrete. What is sustained, produced and counted. Area: "
              "money, health, home, employed work.",
        "fr": "Le corps et le concret. Ce qu'on soutient, ce qu'on produit et ce qu'on compte. "
              "Domaine : argent, santé, maison, travail salarié."},

    "La discusión de las Espadas": {
        "en": "The argument about the Swords", "fr": "La discussion des Épées"},

    "Hay una disputa vieja sobre si las Espadas son Aire o Fuego, y los Bastos lo "
    "contrario. El argumento de los que las hacen Fuego es que la espada se forja; el de "
    "los que las hacen Aire —que es el mayoritario desde el XIX y el que este libro usa— es "
    "que la espada corta y distingue, que es lo que hace el pensamiento. Se dice aquí "
    "porque si lees otro libro y no coincide, ahora sabes por qué.": {
        "en": "There is an old dispute about whether the Swords are Air or Fire, and the Wands "
              "the other way round. The argument of those who make them Fire is that a sword "
              "is forged; that of those who make them Air —the majority view since the "
              "nineteenth century and the one this book uses— is that a sword cuts and "
              "distinguishes, which is what thought does. It is said here because if you read "
              "another book and it does not agree, you now know why.",
        "fr": "Il existe une vieille dispute sur le point de savoir si les Épées sont Air ou "
              "Feu, et les Bâtons l'inverse. L'argument de ceux qui en font du Feu est que "
              "l'épée se forge ; celui de ceux qui en font de l'Air —majoritaire depuis le "
              "XIXe siècle et celui qu'emploie ce livre— est que l'épée coupe et distingue, ce "
              "que fait la pensée. On le dit ici parce que si vous lisez un autre livre et "
              "qu'il ne concorde pas, vous savez désormais pourquoi."},

    "Las cuatro figuras y el elemento dentro del elemento": {
        "en": "The four court cards and the element inside the element",
        "fr": "Les quatre figures et l'élément dans l'élément"},

    "Cada palo tiene cuatro figuras, y cada figura lleva su propio elemento. El Rey es el "
    "fuego del palo, la Reina su agua, el Caballo su aire y la Sota su tierra. De ahí salen "
    "dieciséis combinaciones que describen maneras de estar en un área, no personas.": {
        "en": "Each suit has four court cards, and each court card carries its own element. "
              "The King is the fire of the suit, the Queen its water, the Knight its air and "
              "the Page its earth. From that come sixteen combinations describing ways of "
              "being in an area, not people.",
        "fr": "Chaque couleur a quatre figures, et chaque figure porte son propre élément. Le "
              "Roi est le feu de la couleur, la Reine son eau, le Cavalier son air et le Valet "
              "sa terre. De là viennent seize combinaisons qui décrivent des façons d'être "
              "dans un domaine, non des personnes."},

    "Cómo se lee una figura": {
        "en": "How a court card is read", "fr": "Comment se lit une figure"},

    "Fuego del palo. Manda y decide en esa área. La versión que dirige.": {
        "en": "Fire of the suit. Commands and decides in that area. The version that leads.",
        "fr": "Le feu de la couleur. Commande et décide dans ce domaine. La version qui dirige."},
    "Agua del palo. Sostiene y nutre esa área desde dentro. La versión que cuida.": {
        "en": "Water of the suit. Sustains and nourishes that area from within. The version "
              "that cares.",
        "fr": "L'eau de la couleur. Soutient et nourrit ce domaine de l'intérieur. La version "
              "qui prend soin."},
    "Aire del palo. Se mueve, viaja, lleva y trae. La versión que actúa hacia fuera.": {
        "en": "Air of the suit. Moves, travels, fetches and carries. The version that acts "
              "outwards.",
        "fr": "L'air de la couleur. Se déplace, voyage, porte et rapporte. La version qui agit "
              "vers l'extérieur."},
    "Tierra del palo. Aprende, empieza, recibe. La versión que estudia.": {
        "en": "Earth of the suit. Learns, begins, receives. The version that studies.",
        "fr": "La terre de la couleur. Apprend, commence, reçoit. La version qui étudie."},

    "El Rey de Oros es el fuego de la tierra: quien dirige lo concreto. La Sota de Espadas "
    "es la tierra del aire: quien está aprendiendo a pensar. Con las dos coordenadas —palo "
    "y figura— las dieciséis se deducen y no hay que memorizarlas.": {
        "en": "The King of Pentacles is the fire of earth: the one who directs the concrete. "
              "The Page of Swords is the earth of air: the one who is learning to think. With "
              "the two coordinates —suit and court card— the sixteen are deduced and need no "
              "memorising.",
        "fr": "Le Roi de Deniers est le feu de la terre : celui qui dirige le concret. Le Valet "
              "d'Épées est la terre de l'air : celui qui apprend à penser. Avec les deux "
              "coordonnées —couleur et figure— les seize se déduisent et n'ont pas à être "
              "mémorisées."},

    "Las figuras no son personas": {
        "en": "The court cards are not people", "fr": "Les figures ne sont pas des personnes"},

    "El error más común con las dieciséis es leerlas como «alguien». A veces lo son, y casi "
    "siempre son un modo de estar: el consultante actuando como Sota cuando le tocaría "
    "actuar como Rey, o como Rey cuando debería estar aprendiendo. Preguntar «quién es esta "
    "carta» cierra la lectura; preguntar «desde dónde estoy actuando» la abre.": {
        "en": "The commonest mistake with the sixteen is reading them as «someone». Sometimes "
              "they are, and almost always they are a way of being: the querent acting as Page "
              "when it is time to act as King, or as King when they ought to be learning. "
              "Asking «who is this card» closes the reading; asking «where am I acting from» "
              "opens it.",
        "fr": "L'erreur la plus courante avec les seize est de les lire comme « quelqu'un ». "
              "Parfois elles le sont, et presque toujours elles sont une façon d'être : le "
              "consultant agissant en Valet quand il devrait agir en Roi, ou en Roi quand il "
              "devrait être en train d'apprendre. Demander « qui est cette carte » ferme la "
              "lecture ; demander « d'où est-ce que j'agis » l'ouvre."},

    "Los cuatro ases y la escala del uno al diez, que es lo que convierte cuarenta cartas "
    "en un sistema en vez de una lista.": {
        "en": "The four aces and the scale from one to ten, which is what turns forty cards "
              "into a system instead of a list.",
        "fr": "Les quatre as et l'échelle de un à dix, ce qui fait de quarante cartes un "
              "système au lieu d'une liste."},

    "Los cuatro ases": {"en": "The four aces", "fr": "Les quatre as"},
}
