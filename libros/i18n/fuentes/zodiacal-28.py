# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · cierre de Piscis y el recorrido de doce meses
===============================================================
«"No puedo" es una frase completa» es la línea central de la práctica de
Piscis. Va entrecomillada porque es lo que se dice en voz alta, y la
afirmación de que ya es una frase completa se conserva: es lo que autoriza a
no añadir nada.

La cuarta semana pide decir no a algo que sí se podría hacer pero no se
quiere, y el original lo marca como «el ejercicio de verdad». Esa jerarquía
entre las cuatro semanas se mantiene.

El calendario del recorrido empareja cada mes con una práctica de tres o
cuatro palabras. Se traducen igual de breves porque van en la columna
estrecha de la tabla, enfrentadas al nombre del mes y del signo.
"""

T = {
    "Lo que le funciona es movimiento en el agua —donde está en casa—, cuidado activo del pie "
    "y del calzado, y una estructura horaria que no le nace pero le sostiene. Piscis florece "
    "con rutina, aunque la rutina no le apetezca.": {
        "en": "What works for it is movement in water —where it is at home—, active care of the "
              "foot and of footwear, and a structure of set times that does not come naturally "
              "but holds it up. Pisces flourishes on routine, however little routine appeals to "
              "it.",
        "fr": "Ce qui leur réussit, c'est le mouvement dans l'eau —où ils sont chez eux—, un soin "
              "actif du pied et de la chaussure, et une structure horaire qui ne leur vient pas "
              "naturellement mais qui les soutient. Les Poissons s'épanouissent avec de la "
              "routine, même si la routine ne leur dit rien."},

    "Reducir alcohol y azúcar de forma seria: es el signo que peor los tolera.": {
        "en": "Cutting back on alcohol and sugar in earnest: it is the sign that tolerates them "
              "worst.",
        "fr": "Réduire sérieusement l'alcool et le sucre : c'est le signe qui les tolère le plus "
              "mal."},

    "Comer a horas fijas. Piscis come cuando se acuerda, y su energía depende de eso más de lo "
    "que cree.": {
        "en": "Eating at fixed times. Pisces eats when it remembers, and its energy depends on "
              "that more than it believes.",
        "fr": "Manger à heures fixes. Les Poissons mangent quand ils y pensent, et leur énergie "
              "en dépend plus qu'ils ne le croient."},

    "Cuidar la retención: menos sal, más agua, movimiento diario.": {
        "en": "Watching fluid retention: less salt, more water, daily movement.",
        "fr": "Surveiller la rétention : moins de sel, plus d'eau, du mouvement quotidien."},

    "Vigilar la cafeína y los estimulantes, que le afectan al doble que a la media.": {
        "en": "Watching caffeine and stimulants, which affect it twice as much as the average.",
        "fr": "Surveiller la caféine et les excitants, qui les touchent deux fois plus que la "
              "moyenne."},

    "Piscis no necesita sentir más. Necesita practicar el límite, y el límite se entrena "
    "diciendo no.": {
        "en": "Pisces does not need to feel more. It needs to practise the boundary, and the "
              "boundary is trained by saying no.",
        "fr": "Les Poissons n'ont pas besoin de ressentir davantage. Ils ont besoin de s'exercer "
              "à la limite, et la limite s'entraîne en disant non."},

    "Cada semana durante un mes, di no a una cosa. Una petición, una invitación, un favor.": {
        "en": "Each week for a month, say no to one thing. A request, an invitation, a favour.",
        "fr": "Chaque semaine pendant un mois, dites non à une chose. Une demande, une "
              "invitation, un service."},

    "Sin explicación larga y sin disculpa. «No puedo» es una frase completa.": {
        "en": "With no long explanation and no apology. «I can't» is a complete sentence.",
        "fr": "Sans longue explication et sans excuse. « Je ne peux pas » est une phrase "
              "complète."},

    "Anota qué sentiste al decirlo y qué pasó después. Piscis descubre casi siempre que la "
    "catástrofe que temía no ocurre.": {
        "en": "Write down what you felt on saying it and what happened afterwards. Pisces "
              "almost always discovers that the catastrophe it feared does not happen.",
        "fr": "Notez ce que vous avez ressenti en le disant et ce qui s'est passé ensuite. Les "
              "Poissons découvrent presque toujours que la catastrophe qu'ils craignaient "
              "n'arrive pas."},

    "En la cuarta semana, di no a algo que sí podrías hacer pero no quieres. Ese es el "
    "ejercicio de verdad.": {
        "en": "In the fourth week, say no to something you could indeed do but do not want to. "
              "That is the real exercise.",
        "fr": "La quatrième semaine, dites non à quelque chose que vous pourriez faire mais que "
              "vous ne voulez pas faire. C'est là le véritable exercice."},

    "Con Cáncer y Escorpio, sus compañeros de Agua: se entienden en un nivel que no requiere "
    "lenguaje.": {
        "en": "With Cancer and Scorpio, its companions in Water: they understand one another on "
              "a level that requires no language.",
        "fr": "Avec le Cancer et le Scorpion, leurs compagnons d'Eau : ils se comprennent à un "
              "niveau qui n'exige pas de langage."},

    "Con Virgo, su signo opuesto: el eje disolución–forma. Virgo le da estructura y él le da a "
    "Virgo permiso para no controlarlo todo.": {
        "en": "With Virgo, its opposite sign: the dissolution–form axis. Virgo gives it "
              "structure and it gives Virgo permission not to control everything.",
        "fr": "Avec la Vierge, leur signe opposé : l'axe dissolution–forme. La Vierge leur donne "
              "de la structure et ils donnent à la Vierge la permission de ne pas tout "
              "contrôler."},

    "Con Tauro y Capricornio, de Tierra: le dan el suelo que su naturaleza no tiene.": {
        "en": "With Taurus and Capricorn, of Earth: they give it the ground its nature does not "
              "have.",
        "fr": "Avec le Taureau et le Capricorne, de Terre : ils leur donnent le sol que leur "
              "nature n'a pas."},

    "Con Géminis y Sagitario hay fricción mutable: mucho movimiento y poca dirección común.": {
        "en": "With Gemini and Sagittarius there is mutable friction: a great deal of movement "
              "and little common direction.",
        "fr": "Avec les Gémeaux et le Sagittaire, il y a friction mutable : beaucoup de mouvement "
              "et peu de direction commune."},

    "Con Acuario y Libra la diferencia es de registro: ellos piensan la emoción y Piscis la "
    "habita.": {
        "en": "With Aquarius and Libra the difference is one of register: they think the "
              "emotion and Pisces inhabits it.",
        "fr": "Avec le Verseau et la Balance, la différence est de registre : eux pensent "
              "l'émotion et les Poissons l'habitent."},

    "¿Qué emoción de este mes no era mía?": {
        "en": "Which emotion this month was not mine?",
        "fr": "Quelle émotion de ce mois n'était pas la mienne ?"},

    "¿De qué me evadí, y a dónde fui?": {
        "en": "What did I escape from, and where did I go?",
        "fr": "De quoi me suis-je évadé, et où suis-je allé ?"},

    "¿A qué dije no, y qué pasó realmente después?": {
        "en": "What did I say no to, and what actually happened afterwards?",
        "fr": "À quoi ai-je dit non, et que s'est-il réellement passé ensuite ?"},

    # ── El año como espiral ────────────────────────────────────────────────
    "Capítulo 26": {"en": "Chapter 26", "fr": "Chapitre 26"},

    "Aquí está el uso que convierte este libro en herramienta. La propuesta es sencilla de "
    "enunciar y exigente de cumplir: recorrer los doce signos a lo largo de un año, un mes "
    "cada uno, trabajando la práctica que le corresponde.": {
        "en": "Here is the use that turns this book into a tool. The proposal is simple to "
              "state and demanding to carry out: go through the twelve signs over the course of "
              "a year, a month for each, working the practice that belongs to it.",
        "fr": "Voici l'usage qui fait de ce livre un outil. La proposition est simple à énoncer "
              "et exigeante à tenir : parcourir les douze signes au long d'une année, un mois "
              "chacun, en travaillant la pratique qui lui revient."},

    "No importa cuál sea tu signo solar. Los doce describen cualidades humanas completas, y "
    "todos las tenemos: unas desarrolladas por temperamento y otras atrofiadas por falta de "
    "uso. El objetivo de este recorrido no es reforzar lo que ya haces bien, sino visitar "
    "durante cuatro semanas la cualidad que peor llevas.": {
        "en": "It does not matter what your sun sign is. The twelve describe complete human "
              "qualities, and we all have them: some developed by temperament and others "
              "atrophied through disuse. The aim of this journey is not to reinforce what you "
              "already do well, but to visit for four weeks the quality you handle worst.",
        "fr": "Peu importe quel est votre signe solaire. Les douze décrivent des qualités "
              "humaines complètes, et nous les avons tous : certaines développées par "
              "tempérament et d'autres atrophiées faute d'usage. Le but de ce parcours n'est pas "
              "de renforcer ce que vous faites déjà bien, mais de visiter pendant quatre "
              "semaines la qualité que vous portez le plus mal."},

    "Cómo se organiza": {"en": "How it is organised", "fr": "Comment cela s'organise"},

    "El calendario del recorrido": {
        "en": "The calendar of the journey", "fr": "Le calendrier du parcours"},

    "Mes 1 · Aries": {"en": "Month 1 · Aries", "fr": "Mois 1 · Bélier"},
    "Terminar lo empezado": {
        "en": "Finishing what was started", "fr": "Terminer ce qui est commencé"},

    "Mes 2 · Tauro": {"en": "Month 2 · Taurus", "fr": "Mois 2 · Taureau"},
    "Soltar lo que ya no sirve": {
        "en": "Letting go of what no longer serves",
        "fr": "Lâcher ce qui ne sert plus"},

    "Mes 3 · Géminis": {"en": "Month 3 · Gemini", "fr": "Mois 3 · Gémeaux"},
    "Profundizar en un solo tema": {
        "en": "Going deep into one single subject",
        "fr": "Approfondir un seul sujet"},

    "Mes 4 · Cáncer": {"en": "Month 4 · Cancer", "fr": "Mois 4 · Cancer"},
}
