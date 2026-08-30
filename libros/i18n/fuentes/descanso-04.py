# -*- coding: utf-8 -*-
"""
CÓDICE DEL DESCANSO · capítulo 3, la arquitectura de una noche
==============================================================
Las etiquetas de fase —N1, N2, N3, REM— son nomenclatura internacional y no se
traducen. Lo que sí se traduce es su descripción, que es lo que el comprador
necesita para entender la lámina.
"""

T = {
    "Dormir no es un estado: son cuatro, que se alternan en un orden que no es aleatorio y "
    "que se repite en ciclos. Ese orden es la información más útil de este libro, porque "
    "explica qué se pierde exactamente cuando se duerme poco.": {
        "en": "Sleeping is not one state: it is four, alternating in an order that is not "
              "random and that repeats in cycles. That order is the most useful piece of "
              "information in this book, because it explains exactly what is lost when you "
              "sleep too little.",
        "fr": "Dormir n'est pas un état : ce sont quatre états, qui alternent dans un ordre "
              "qui n'a rien d'aléatoire et qui se répète en cycles. Cet ordre est "
              "l'information la plus utile de ce livre, parce qu'il explique exactement ce "
              "que l'on perd quand on dort peu."},

    '<span class="fig-n">El recorrido de una noche completa</span> De 4 a 6 ciclos de unos '
    "90 minutos. El sueño profundo se concentra en la primera mitad de la noche y los "
    "tramos de sueño con movimientos oculares rápidos se alargan en cada ciclo, dominando "
    "la segunda mitad. La noche no es simétrica, y esa asimetría es la clave de todo el "
    "capítulo.": {
        "en": '<span class="fig-n">The course of a full night</span> From 4 to 6 cycles of '
              "about 90 minutes. Deep sleep is concentrated in the first half of the night, "
              "and the stretches of rapid eye movement sleep lengthen with every cycle, "
              "dominating the second half. The night is not symmetrical, and that asymmetry "
              "is the key to the whole chapter.",
        "fr": '<span class="fig-n">Le parcours d\'une nuit complète</span> De 4 à 6 cycles '
              "d'environ 90 minutes. Le sommeil profond se concentre dans la première "
              "moitié de la nuit et les plages de sommeil à mouvements oculaires rapides "
              "s'allongent à chaque cycle, dominant la seconde moitié. La nuit n'est pas "
              "symétrique, et cette asymétrie est la clé de tout le chapitre."},

    "Las cuatro fases": {"en": "The four stages", "fr": "Les quatre phases"},

    '<span class="fig-n">Qué hace cada fase</span> Los dos primeros estados son sueño '
    "ligero; el tercero es el profundo, asociado a la recuperación física; el cuarto es el "
    "de los movimientos oculares rápidos. Un despertar breve entre ciclos es normal y no "
    "indica que algo vaya mal.": {
        "en": '<span class="fig-n">What each stage does</span> The first two states are '
              "light sleep; the third is deep sleep, associated with physical recovery; the "
              "fourth is rapid eye movement sleep. A brief awakening between cycles is "
              "normal and does not mean anything is wrong.",
        "fr": '<span class="fig-n">Ce que fait chaque phase</span> Les deux premiers états '
              "sont du sommeil léger ; le troisième est le sommeil profond, associé à la "
              "récupération physique ; le quatrième est celui des mouvements oculaires "
              "rapides. Un bref réveil entre deux cycles est normal et n'indique pas que "
              "quelque chose ne va pas."},

    "En una tabla": {"en": "In a table", "fr": "En tableau"},

    "N1 · Transición": {"en": "N1 · Transition", "fr": "N1 · Transition"},
    "1 a 5 min · Muy ligero. Se puede negar haber dormido": {
        "en": "1 to 5 min · Very light. You may deny having slept at all",
        "fr": "1 à 5 min · Très léger. On peut nier avoir dormi"},

    "N2 · Sueño ligero": {"en": "N2 · Light sleep", "fr": "N2 · Sommeil léger"},
    "La mayor parte de la noche · Aquí se consolida buena parte de la memoria de "
    "procedimiento": {
        "en": "Most of the night · Much of procedural memory is consolidated here",
        "fr": "La plus grande partie de la nuit · Une bonne part de la mémoire procédurale "
              "s'y consolide"},

    "N3 · Sueño profundo": {"en": "N3 · Deep sleep", "fr": "N3 · Sommeil profond"},
    "Concentrado en la primera mitad · El de la recuperación física. Si se recorta el "
    "sueño por el final, este se conserva": {
        "en": "Concentrated in the first half · The one for physical recovery. If sleep is "
              "cut from the end, this one survives",
        "fr": "Concentré sur la première moitié · Celui de la récupération physique. Si "
              "l'on coupe le sommeil par la fin, celui-ci est préservé"},

    "REM · Movimientos oculares rápidos": {
        "en": "REM · Rapid eye movement", "fr": "REM · Mouvements oculaires rapides"},
    "Crece en cada ciclo · Concentrado en la segunda mitad. Si se recorta el sueño por el "
    "final, este es el que se pierde": {
        "en": "It grows with every cycle · Concentrated in the second half. If sleep is cut "
              "from the end, this is the one you lose",
        "fr": "Il s'allonge à chaque cycle · Concentré sur la seconde moitié. Si l'on coupe "
              "le sommeil par la fin, c'est celui-ci que l'on perd"},

    "La consecuencia que casi nadie ha oído": {
        "en": "The consequence almost nobody has heard",
        "fr": "La conséquence dont presque personne n'a entendu parler"},

    "Si la noche fuera homogénea, recortar una hora costaría lo mismo por cualquiera de "
    "los dos extremos. No lo es. Como el sueño profundo va delante y el de movimientos "
    "oculares rápidos va detrás, quitar la última hora no quita un poco de cada cosa: "
    "quita casi exclusivamente el segundo, que es el que más crece precisamente en los "
    "últimos ciclos.": {
        "en": "If the night were homogeneous, cutting an hour would cost the same from "
              "either end. It is not. Because deep sleep comes first and rapid eye movement "
              "sleep comes later, removing the last hour does not remove a little of each: "
              "it removes almost exclusively the second, which is precisely the one that "
              "grows most in the final cycles.",
        "fr": "Si la nuit était homogène, retrancher une heure coûterait la même chose par "
              "l'un ou l'autre bout. Elle ne l'est pas. Comme le sommeil profond vient "
              "d'abord et celui à mouvements oculaires rapides ensuite, retirer la dernière "
              "heure n'enlève pas un peu de chaque : cela enlève presque exclusivement le "
              "second, celui-là même qui s'allonge le plus dans les derniers cycles."},

    "Eso significa que quien duerme cinco horas conserva la mayor parte de su sueño "
    "profundo y pierde una fracción enorme del otro. Y explica algo que mucha gente ha "
    "notado sin saber por qué: después de una noche corta uno puede sentirse físicamente "
    "aceptable y estar claramente peor de humor, de concentración y de memoria.": {
        "en": "That means someone sleeping five hours keeps most of their deep sleep and "
              "loses an enormous fraction of the other. And it explains something many "
              "people have noticed without knowing why: after a short night you can feel "
              "physically acceptable and be clearly worse in mood, concentration and memory.",
        "fr": "Cela signifie que celui qui dort cinq heures conserve l'essentiel de son "
              "sommeil profond et perd une fraction énorme de l'autre. Et cela explique une "
              "chose que beaucoup ont remarquée sans savoir pourquoi : après une nuit "
              "courte, on peut se sentir physiquement acceptable et être nettement moins "
              "bien sur l'humeur, la concentration et la mémoire."},

    "Al revés también funciona, y es más importante para quien entrena: acostarse tarde y "
    "levantarse a la misma hora se come el sueño de la segunda mitad; acostarse a la hora "
    "y levantarse antes hace lo mismo. Las dos formas habituales de recortar atacan al "
    "mismo lado de la noche.": {
        "en": "It works the other way round too, and this matters more for anyone who "
              "trains: going to bed late and getting up at the same time eats into the "
              "second half's sleep; going to bed on time and getting up earlier does the "
              "same. Both of the usual ways of cutting attack the same side of the night.",
        "fr": "L'inverse vaut aussi, et c'est plus important pour qui s'entraîne : se "
              "coucher tard et se lever à la même heure mange le sommeil de la seconde "
              "moitié ; se coucher à l'heure et se lever plus tôt fait la même chose. Les "
              "deux façons habituelles de rogner attaquent le même côté de la nuit."},

    "Por qué el mito de despertarse entre ciclos funciona a medias": {
        "en": "Why the myth of waking between cycles only half works",
        "fr": "Pourquoi le mythe du réveil entre deux cycles ne marche qu'à moitié"},

    "Es cierto que despertarse en mitad de un tramo profundo produce esa sensación pastosa "
    "de aturdimiento, y que despertarse en sueño ligero es más agradable. Lo que no es "
    "cierto es que las aplicaciones que dicen calcular tu ciclo desde el móvil en la "
    "mesilla puedan hacerlo con precisión: los ciclos no duran exactamente noventa minutos "
    "ni son iguales entre sí ni entre personas. La forma fiable de despertarse en sueño "
    "ligero es dormir lo suficiente, porque los últimos ciclos son casi todo sueño ligero "
    "y REM.": {
        "en": "It is true that waking in the middle of a deep stretch produces that thick, "
              "groggy feeling, and that waking in light sleep is more pleasant. What is not "
              "true is that the apps claiming to work out your cycle from a phone on the "
              "bedside table can do so accurately: cycles do not last exactly ninety "
              "minutes, nor are they equal to one another or between people. The reliable "
              "way to wake in light sleep is to sleep enough, because the last cycles are "
              "almost entirely light sleep and REM.",
        "fr": "Il est vrai que se réveiller au milieu d'une plage profonde produit cette "
              "sensation pâteuse d'hébétude, et que se réveiller en sommeil léger est plus "
              "agréable. Ce qui est faux, c'est que les applications qui prétendent "
              "calculer votre cycle depuis le téléphone posé sur la table de nuit puissent "
              "le faire avec précision : les cycles ne durent pas exactement quatre-vingt-"
              "dix minutes et ne sont égaux ni entre eux ni d'une personne à l'autre. La "
              "façon fiable de se réveiller en sommeil léger, c'est de dormir assez, parce "
              "que les derniers cycles sont presque entièrement du sommeil léger et du REM."},

    # ── Capítulo 4 · la deuda ──────────────────────────────────────────────
    "La expresión «deuda de sueño» suena a metáfora y describe bastante bien lo que "
    "ocurre: el déficit se acumula, produce efectos medibles antes de que uno se dé "
    "cuenta, y no se salda de una vez.": {
        "en": "The phrase “sleep debt” sounds like a metaphor and describes what happens "
              "rather well: the deficit accumulates, produces measurable effects before you "
              "notice them, and is not settled in one go.",
        "fr": "L'expression « dette de sommeil » sonne comme une métaphore et décrit assez "
              "bien ce qui se passe : le déficit s'accumule, produit des effets mesurables "
              "avant qu'on s'en aperçoive, et ne se solde pas d'un coup."},

    '<span class="fig-n">Una semana normal y lo que deja detrás</span> Cinco noches por '
    "debajo del objetivo de 7 horas y dos de recuperación el fin de semana. La deuda de la "
    "semana no se cancela: dormir de más el sábado recupera parte del déficit —sobre todo "
    "del profundo, que tiene prioridad— pero no todo, y a cambio desplaza el horario y "
    "hace más difícil el lunes.": {
        "en": '<span class="fig-n">An ordinary week and what it leaves behind</span> Five '
              "nights below the 7-hour target and two of recovery at the weekend. The "
              "week's debt is not cancelled: sleeping in on Saturday recovers part of the "
              "deficit —above all the deep sleep, which has priority— but not all of it, "
              "and in exchange it shifts the schedule and makes Monday harder.",
        "fr": '<span class="fig-n">Une semaine ordinaire et ce qu\'elle laisse</span> Cinq '
              "nuits sous l'objectif de 7 heures et deux de récupération le week-end. La "
              "dette de la semaine ne s'annule pas : dormir davantage le samedi récupère "
              "une partie du déficit —surtout le sommeil profond, qui est prioritaire— mais "
              "pas la totalité, et en échange cela décale l'horaire et rend le lundi plus "
              "difficile."},

    "Los tres hechos que hacen peligrosa a la deuda": {
        "en": "The three facts that make the debt dangerous",
        "fr": "Les trois faits qui rendent la dette dangereuse"},

    "Se acumula": {"en": "It accumulates", "fr": "Elle s'accumule"},
    "Varias noches de seis horas producen un deterioro comparable al de noches enteras sin "
    "dormir, alcanzado poco a poco.": {
        "en": "Several nights of six hours produce a deterioration comparable to whole "
              "nights without sleep, reached little by little.",
        "fr": "Plusieurs nuits de six heures produisent une dégradation comparable à celle "
              "de nuits entières sans sommeil, atteinte petit à petit."},
}
