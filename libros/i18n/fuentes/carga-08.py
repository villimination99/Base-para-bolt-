# -*- coding: utf-8 -*-
"""
CÓDICE DE LA CARGA · el aerobio por dentro y el experimento de quitar el peso
=============================================================================
Los tres tipos de aerobio se llaman aquí base, umbral e intervalos. Son los
nombres corrientes en las tres lenguas y no hace falta inventar nada: quien
corra en inglés reconoce «threshold» y quien corra en francés reconoce
« seuil ».

Los porcentajes de pérdida llevan coma decimal en español y en francés y punto
en inglés: 1,5 % al mes y 1.5 % a month son la misma cifra. Y se dicen como
rangos —de 1 a 2 %— porque así están en la literatura: el capítulo insiste en
que lo fiable es el signo y no el número exacto, y redondear a una cifra sola
contradiría el propio párrafo que lo explica.
"""

T = {
    "Bajar el ritmo cinco minutos al final no acelera la recuperación de forma apreciable, "
    "pero evita el mareo de parar en seco tras un esfuerzo intenso y es un buen momento "
    "para el trabajo de movilidad, porque el tejido está caliente. Es un hábito barato con "
    "dos ventajas pequeñas; no le pidas más.": {
        "en": "Easing off for five minutes at the end does not appreciably speed up recovery, "
              "but it avoids the dizziness of stopping dead after intense effort and it is a "
              "good moment for mobility work, because the tissue is warm. It is a cheap habit "
              "with two small advantages; do not ask more of it.",
        "fr": "Réduire le rythme cinq minutes à la fin n'accélère pas la récupération de "
              "façon appréciable, mais cela évite le vertige de s'arrêter net après un effort "
              "intense et c'est un bon moment pour le travail de mobilité, parce que le tissu "
              "est chaud. C'est une habitude bon marché avec deux petits avantages ; ne lui "
              "en demandez pas plus."},

    "«Hacer cardio» describe tan poco como «comer comida». Bajo esa etiqueta caben tres "
    "cosas distintas que producen adaptaciones distintas y cuestan recuperaciones "
    "distintas, y saber cuál es cuál cambia el resultado de una temporada.": {
        "en": "«Doing cardio» describes as little as «eating food». Under that label fit "
              "three different things that produce different adaptations and cost different "
              "recoveries, and knowing which is which changes the outcome of a season.",
        "fr": "« Faire du cardio » décrit aussi peu que « manger de la nourriture ». Sous "
              "cette étiquette tiennent trois choses différentes qui produisent des "
              "adaptations différentes et coûtent des récupérations différentes, et savoir "
              "laquelle est laquelle change le résultat d'une saison."},

    "Los tres tipos": {"en": "The three kinds", "fr": "Les trois types"},

    "Base": {"en": "Base", "fr": "Base"},
    "Conversación posible durante toda la sesión. Volumen cómodo, de treinta minutos a dos "
    "horas. Construye la capacidad de fondo y apenas cuesta recuperación.": {
        "en": "Conversation possible throughout the session. Comfortable volume, from thirty "
              "minutes to two hours. It builds background capacity and costs almost no "
              "recovery.",
        "fr": "Conversation possible pendant toute la séance. Volume confortable, de trente "
              "minutes à deux heures. Elle construit la capacité de fond et ne coûte presque "
              "aucune récupération."},

    "Umbral": {"en": "Threshold", "fr": "Seuil"},
    "Ritmo sostenido en el que las frases se acortan. Bloques de diez a veinte minutos. "
    "Mejora el ritmo que puedes sostener mucho tiempo.": {
        "en": "A sustained pace at which sentences get shorter. Blocks of ten to twenty "
              "minutes. It improves the pace you can hold for a long time.",
        "fr": "Un rythme soutenu où les phrases raccourcissent. Des blocs de dix à vingt "
              "minutes. Il améliore l'allure que vous pouvez tenir longtemps."},

    "Intervalos": {"en": "Intervals", "fr": "Intervalles"},
    "Esfuerzos cortos muy intensos con descanso. Mejoran el techo, cuestan bastante "
    "recuperación y son los que más se abusan.": {
        "en": "Short, very intense efforts with rest. They raise the ceiling, cost a good "
              "deal of recovery and are the most overused of the three.",
        "fr": "Des efforts courts et très intenses avec du repos. Ils élèvent le plafond, "
              "coûtent pas mal de récupération et sont ceux dont on abuse le plus."},

    "El error de vivir en el medio": {
        "en": "The mistake of living in the middle",
        "fr": "L'erreur de vivre au milieu"},

    "La trampa más común del aerobio amateur es hacerlo todo a una intensidad intermedia: "
    "demasiado fuerte para acumular volumen sin fatiga y demasiado suave para producir la "
    "adaptación de la intensidad alta. Es cómodo, se siente productivo y rinde poco por lo "
    "que cuesta.": {
        "en": "The commonest trap of amateur aerobic work is doing it all at an intermediate "
              "intensity: too hard to accumulate volume without fatigue and too easy to "
              "produce the adaptation of high intensity. It is comfortable, it feels "
              "productive and it returns little for what it costs.",
        "fr": "Le piège le plus courant de l'aérobie amateur est de tout faire à une "
              "intensité intermédiaire : trop fort pour accumuler du volume sans fatigue et "
              "trop doux pour produire l'adaptation de la haute intensité. C'est confortable, "
              "cela donne le sentiment d'être productif et cela rapporte peu au regard de ce "
              "que cela coûte."},

    "La corrección es sencilla y funciona: que la mayor parte del volumen sea claramente "
    "fácil —de verdad fácil, hablando cómodamente— y que la parte dura sea claramente dura "
    "y ocupe poco. Los extremos hacen el trabajo; el medio acumula fatiga.": {
        "en": "The correction is simple and it works: let most of the volume be clearly easy "
              "—genuinely easy, talking comfortably— and let the hard part be clearly hard and "
              "take up little. The extremes do the work; the middle accumulates fatigue.",
        "fr": "La correction est simple et elle fonctionne : que l'essentiel du volume soit "
              "nettement facile —vraiment facile, en parlant confortablement— et que la partie "
              "dure soit nettement dure et occupe peu de place. Les extrêmes font le travail ; "
              "le milieu accumule de la fatigue."},

    "¿Interfiere el aerobio con la fuerza?": {
        "en": "Does aerobic work interfere with strength?",
        "fr": "L'aérobie interfère-t-elle avec la force ?"},

    "La pregunta lleva décadas en el aire y la respuesta razonable es: mucho menos de lo "
    "que teme el gimnasio, y algo más que cero. Lo que se sabe con cierta solidez es que "
    "la interferencia aparece sobre todo con volúmenes muy altos de aerobio, con las dos "
    "cosas en la misma sesión y con poca recuperación entre ellas.": {
        "en": "The question has been in the air for decades and the reasonable answer is: far "
              "less than the gym fears, and rather more than zero. What is known with some "
              "solidity is that the interference appears above all with very high aerobic "
              "volumes, with both things in the same session and with little recovery between "
              "them.",
        "fr": "La question traîne depuis des décennies et la réponse raisonnable est : bien "
              "moins que ne le craint la salle, et un peu plus que zéro. Ce que l'on sait avec "
              "une certaine solidité, c'est que l'interférence apparaît surtout avec de très "
              "hauts volumes d'aérobie, avec les deux choses dans la même séance et avec peu "
              "de récupération entre elles."},

    "Si puedes, separa las dos sesiones por varias horas o ponlas en días distintos.": {
        "en": "If you can, separate the two sessions by several hours or put them on "
              "different days.",
        "fr": "Si vous le pouvez, séparez les deux séances de plusieurs heures ou mettez-les "
              "des jours différents."},

    "Si tienen que ir juntas, haz primero lo que sea prioritario para ti.": {
        "en": "If they have to go together, do first whatever is the priority for you.",
        "fr": "Si elles doivent aller ensemble, faites d'abord ce qui est prioritaire pour "
              "vous."},

    "Correr interfiere más que pedalear, probablemente por el componente excéntrico de la "
    "zancada.": {
        "en": "Running interferes more than cycling, probably because of the eccentric "
              "component of the stride.",
        "fr": "Courir interfère plus que pédaler, probablement à cause de la composante "
              "excentrique de la foulée."},

    "Para la inmensa mayoría de la gente, que hace tres o cuatro horas semanales en total, "
    "esta discusión es puramente teórica.": {
        "en": "For the vast majority of people, who do three or four hours a week in total, "
              "this discussion is purely theoretical.",
        "fr": "Pour l'immense majorité des gens, qui font trois ou quatre heures par semaine "
              "au total, cette discussion est purement théorique."},

    "Lo que el aerobio hace y la fuerza no": {
        "en": "What aerobic work does and strength does not",
        "fr": "Ce que fait l'aérobie et que la force ne fait pas"},

    "Cambia el corazón y el sistema vascular de una manera que el entrenamiento de fuerza "
    "no reproduce, y esos cambios son los que mejor se asocian con vivir más años y con "
    "vivirlos mejor. Por eso las guías piden las dos cosas y no dejan elegir: no son "
    "sustitutos.": {
        "en": "It changes the heart and the vascular system in a way strength training does "
              "not reproduce, and those changes are the ones most strongly associated with "
              "living more years and living them better. That is why the guidelines ask for "
              "both and do not let you choose: they are not substitutes.",
        "fr": "Elle modifie le cœur et le système vasculaire d'une façon que l'entraînement de "
              "force ne reproduit pas, et ce sont ces changements qui s'associent le mieux au "
              "fait de vivre plus longtemps et de mieux vivre ces années. C'est pourquoi les "
              "recommandations demandent les deux et ne laissent pas choisir : ce ne sont pas "
              "des substituts."},

    # ── El experimento de quitar el peso ───────────────────────────────────
    "Para saber para qué sirve la carga, lo más limpio es quitarla del todo y mirar qué "
    "pasa. Eso es exactamente lo que llevan décadas haciendo los programas de "
    "investigación en vuelo espacial y en reposo en cama prolongado, y sus resultados son "
    "de acceso público.": {
        "en": "To find out what load is for, the cleanest thing is to remove it entirely and "
              "watch what happens. That is exactly what spaceflight and prolonged bed rest "
              "research programmes have been doing for decades, and their results are "
              "publicly accessible.",
        "fr": "Pour savoir à quoi sert la charge, le plus propre est de la retirer entièrement "
              "et de regarder ce qui se passe. C'est exactement ce que font depuis des "
              "décennies les programmes de recherche sur le vol spatial et l'alitement "
              "prolongé, et leurs résultats sont d'accès public."},

    '<span class="fig-n">Lo que le ocurre a un cuerpo sin carga</span> Las zonas señaladas '
    "son las que más pierden: lo que sostiene el cuerpo contra la gravedad. La columna da "
    "el ritmo de cada pérdida.": {
        "en": '<span class="fig-n">What happens to a body with no load on it</span> The areas '
              "marked are the ones that lose most: what holds the body up against gravity. "
              "The column gives the rate of each loss.",
        "fr": '<span class="fig-n">Ce qui arrive à un corps sans charge</span> Les zones '
              "signalées sont celles qui perdent le plus : ce qui soutient le corps contre la "
              "gravité. La colonne donne le rythme de chaque perte."},

    "Son órdenes de magnitud de la literatura de reposo en cama y de vuelo espacial. Los "
    "estudios difieren en la cifra según la duración, la población y el método de medida; "
    "en lo que no difieren es en el signo, y esa coincidencia es lo que hace fiable el "
    "conjunto.": {
        "en": "These are orders of magnitude from the bed rest and spaceflight literature. "
              "The studies differ on the figure according to duration, population and method "
              "of measurement; what they do not differ on is the sign, and that agreement is "
              "what makes the whole reliable.",
        "fr": "Ce sont des ordres de grandeur issus de la littérature sur l'alitement et le "
              "vol spatial. Les études diffèrent sur le chiffre selon la durée, la population "
              "et la méthode de mesure ; ce sur quoi elles ne diffèrent pas, c'est le signe, "
              "et cette concordance est ce qui rend l'ensemble fiable."},

    "Los cinco efectos": {"en": "The five effects", "fr": "Les cinq effets"},

    "1 a 2 % por semana · En reposo en cama estricto. Los extensores de la pierna y la "
    "espalda son los primeros y los que más pierden": {
        "en": "1 to 2 % a week · In strict bed rest. The leg and back extensors are the first "
              "to go and the ones that lose most",
        "fr": "1 à 2 % par semaine · En alitement strict. Les extenseurs de la jambe et du dos "
              "sont les premiers et ceux qui perdent le plus"},

    "Cae más rápido que la masa · La pérdida de fuerza precede a la de tamaño: parte es "
    "nerviosa": {
        "en": "It falls faster than mass · Loss of strength precedes loss of size: part of it "
              "is neural",
        "fr": "Elle chute plus vite que la masse · La perte de force précède celle de taille : "
              "une partie est nerveuse"},

    "En torno a 1 a 1,5 % al mes · En huesos de carga —cadera, columna lumbar, calcáneo—. "
    "Los brazos apenas cambian": {
        "en": "Around 1 to 1.5 % a month · In load-bearing bones —hip, lumbar spine, "
              "calcaneus—. The arms barely change",
        "fr": "Environ 1 à 1,5 % par mois · Dans les os porteurs —hanche, rachis lombaire, "
              "calcanéum—. Les bras changent à peine"},

    "Baja en los primeros días · De ahí el mareo al incorporarse tras días en cama": {
        "en": "It drops in the first days · Hence the dizziness on standing up after days in "
              "bed",
        "fr": "Il baisse dès les premiers jours · D'où le vertige en se levant après des jours "
              "au lit"},

    "Medible en una o dos semanas · Se recupera antes que el hueso, que es lo más lento de "
    "todo": {
        "en": "Measurable in one or two weeks · It recovers sooner than bone, which is the "
              "slowest of all",
        "fr": "Mesurable en une ou deux semaines · Elle récupère avant l'os, qui est le plus "
              "lent de tout"},

    "El orden importa más que las cifras": {
        "en": "The order matters more than the figures",
        "fr": "L'ordre compte plus que les chiffres"},
}
