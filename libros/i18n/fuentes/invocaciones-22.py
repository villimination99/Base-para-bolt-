# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · los errores que quedan y el estado del cuerpo
==========================================================================
«Todo lo que hay en este libro está publicado desde el siglo XIX» se traduce
con la forma de siglo que ya usa la casa: nineteenth-century en inglés, XIXe
siècle en francés, sin voladita. La remisión al capítulo 17 conserva el número.

El aviso sanitario del capítulo del cuerpo es la segunda pieza legal del libro
y va literal: enumera las cuatro situaciones, dice que hay que consultar antes
y añade que el ayuno no es negociable. No se abrevia ni se reordena en ninguna
de las dos lenguas.

La prueba de la vida ordinaria —preguntar a quien vive contigo— es el criterio
que el libro pone por encima de cualquier fenómeno, y su segundo párrafo, el
que manda parar si la práctica está haciendo daño, se traduce con la misma
rotundidad.
"""

T = {
    "Buscar fenómenos. Esperar visiones, voces, sensaciones. La práctica bien hecha produce "
    "sobre todo una cosa muy poco vistosa: más atención disponible en la vida ordinaria. Quien "
    "busca espectáculo se acaba convenciendo de que lo ha visto, y ahí empieza el "
    "autoengaño.": {
        "en": "Hunting for phenomena. Expecting visions, voices, sensations. Practice done "
              "properly produces above all one very unshowy thing: more attention available in "
              "ordinary life. Whoever goes looking for a spectacle ends up convincing themselves "
              "they have seen one, and that is where self-deception begins.",
        "fr": "Chercher des phénomènes. Attendre des visions, des voix, des sensations. La "
              "pratique bien menée produit surtout une chose fort peu spectaculaire : plus "
              "d'attention disponible dans la vie ordinaire. Qui cherche le spectacle finit par "
              "se convaincre qu'il l'a vu, et c'est là que commence l'auto-illusion."},

    "No cerrar. Ya dicho en el capítulo 17, y se repite porque es el error que más desgasta a "
    "largo plazo.": {
        "en": "Not closing. Already said in chapter 17, and repeated because it is the error "
              "that wears you down most in the long run.",
        "fr": "Ne pas clore. Déjà dit au chapitre 17, et répété parce que c'est l'erreur qui use "
              "le plus à la longue."},

    "Practicar en crisis. La práctica intensiva no es el sitio donde resolver una crisis "
    "aguda; en el mejor de los casos no ayuda y en el peor la amplifica. En crisis se reduce a "
    "lo mínimo, se sostiene el rito diario corto y se busca ayuda.": {
        "en": "Practising in a crisis. Intensive practice is not the place to resolve an acute "
              "crisis; at best it does not help and at worst it amplifies it. In a crisis you "
              "cut back to the minimum, keep up the short daily rite and look for help.",
        "fr": "Pratiquer en pleine crise. La pratique intensive n'est pas le lieu où résoudre "
              "une crise aiguë ; au mieux elle n'aide pas et au pire elle l'amplifie. En crise "
              "on réduit au minimum, on maintient le rite quotidien court et on cherche de "
              "l'aide."},

    "El secreto y la superioridad. La sensación de pertenecer a una minoría que sabe algo es "
    "la trampa más antigua del oficio. Es agradable, es falsa y aísla. Todo lo que hay en este "
    "libro está publicado desde el siglo XIX.": {
        "en": "Secrecy and superiority. The feeling of belonging to a minority that knows "
              "something is the oldest trap in the trade. It is pleasant, it is false and it "
              "isolates. Everything in this book has been in print since the nineteenth "
              "century.",
        "fr": "Le secret et la supériorité. Le sentiment d'appartenir à une minorité qui sait "
              "quelque chose est le plus vieux piège du métier. Il est agréable, il est faux et "
              "il isole. Tout ce qui se trouve dans ce livre est publié depuis le XIXe siècle."},

    "Hay una manera muy simple de saber si una práctica ritual está haciendo su trabajo, y no "
    "tiene nada que ver con lo que se sienta durante la sesión. Pregunta a quien vive contigo "
    "si te nota distinto, y en qué. Si llevas seis meses de práctica diaria y nadie a tu "
    "alrededor ha notado nada en ninguna dirección, algo no está pasando donde tendría que "
    "pasar.": {
        "en": "There is a very simple way of telling whether a ritual practice is doing its "
              "job, and it has nothing to do with what you feel during the session. Ask whoever "
              "lives with you whether they notice you are different, and how. If you have six "
              "months of daily practice behind you and nobody around you has noticed anything "
              "in any direction, something is not happening where it ought to be happening.",
        "fr": "Il y a une façon très simple de savoir si une pratique rituelle fait son travail, "
              "et elle n'a rien à voir avec ce que l'on ressent pendant la séance. Demandez à "
              "qui vit avec vous s'il vous trouve différent, et en quoi. Si vous avez six mois "
              "de pratique quotidienne derrière vous et que personne autour de vous n'a rien "
              "remarqué dans aucun sens, quelque chose ne se produit pas là où cela devrait se "
              "produire."},

    "Si lo que notan es que estás más raro, más aislado o más irritable, la práctica está "
    "haciendo daño y hay que parar y revisar. Una disciplina de atención bien llevada hace a "
    "la gente más presente y más fácil de tratar, no menos. Cualquier camino que te aleje de "
    "los tuyos y te convenza de que eso es progreso está mal construido.": {
        "en": "If what they notice is that you are odder, more isolated or more irritable, the "
              "practice is doing harm and it has to be stopped and reviewed. A discipline of "
              "attention carried out well makes people more present and easier to deal with, "
              "not less. Any path that takes you away from your own people and convinces you "
              "that this is progress is badly built.",
        "fr": "Si ce qu'ils remarquent, c'est que vous êtes plus bizarre, plus isolé ou plus "
              "irritable, la pratique fait du mal et il faut s'arrêter et réviser. Une "
              "discipline de l'attention bien menée rend les gens plus présents et plus faciles "
              "à vivre, pas moins. Tout chemin qui vous éloigne des vôtres et vous convainc que "
              "c'est là un progrès est mal bâti."},

    # ── El estado del cuerpo ───────────────────────────────────────────────
    "Los grimorios prescriben ayunos, vigilias, abstinencias y baños, y esa parte del material "
    "se suele leer como folclore devoto. Es un error: son prescripciones sobre el estado "
    "fisiológico del operante, y lo que buscaban —a tientas y sin fisiología— sigue siendo "
    "exactamente lo que hace falta.": {
        "en": "The grimoires prescribe fasts, vigils, abstinences and baths, and that part of "
              "the material tends to be read as devout folklore. That is a mistake: they are "
              "prescriptions about the operator's physiological state, and what they were after "
              "—by feel and with no physiology— is still exactly what is needed.",
        "fr": "Les grimoires prescrivent des jeûnes, des veilles, des abstinences et des bains, "
              "et cette partie du matériau se lit d'ordinaire comme du folklore dévot. C'est une "
              "erreur : ce sont des prescriptions sur l'état physiologique de l'opérant, et ce "
              "qu'elles cherchaient —à tâtons et sans physiologie— reste exactement ce qu'il "
              "faut."},

    "Lo que sigue son hábitos de sentido común orientados a tener atención disponible. No es "
    "una pauta dietética ni un programa de entrenamiento individualizado, y no considera "
    "patologías. Si tienes una condición médica, tomas medicación, estás embarazada o tienes "
    "antecedentes de trastorno alimentario, nada de este capítulo se aplica sin que lo revise "
    "antes tu profesional sanitario. El ayuno, en particular, está contraindicado en varios "
    "casos y no es negociable.": {
        "en": "What follows are common-sense habits aimed at having attention available. It is "
              "not a dietary plan or an individualised training programme, and it does not take "
              "pathologies into account. If you have a medical condition, take medication, are "
              "pregnant or have a history of eating disorder, nothing in this chapter applies "
              "without your healthcare professional reviewing it first. Fasting in particular is "
              "contraindicated in several cases and that is not negotiable.",
        "fr": "Ce qui suit, ce sont des habitudes de bon sens visant à disposer d'attention. Ce "
              "n'est ni un régime alimentaire ni un programme d'entraînement individualisé, et "
              "cela ne tient pas compte des pathologies. Si vous avez une affection médicale, si "
              "vous prenez un traitement, si vous êtes enceinte ou si vous avez des antécédents "
              "de trouble du comportement alimentaire, rien de ce chapitre ne s'applique sans "
              "que votre professionnel de santé l'ait examiné au préalable. Le jeûne, en "
              "particulier, est contre-indiqué dans plusieurs cas et cela n'est pas négociable."},

    "El sueño, que es lo primero": {
        "en": "Sleep, which comes first", "fr": "Le sommeil, qui vient en premier"},

    "No hay técnica de atención que compense dormir mal. Es el factor con más peso de todo "
    "este capítulo y el más ignorado, porque no tiene ningún atractivo esotérico. Un operante "
    "con cinco horas de sueño no tiene atención que dirigir: tiene un déficit.": {
        "en": "There is no technique of attention that makes up for sleeping badly. It is the "
              "heaviest factor in this whole chapter and the most ignored, because it has no "
              "esoteric appeal whatever. An operator on five hours of sleep has no attention to "
              "direct: they have a deficit.",
        "fr": "Aucune technique d'attention ne compense un mauvais sommeil. C'est le facteur qui "
              "pèse le plus dans tout ce chapitre et le plus ignoré, parce qu'il n'a aucun "
              "attrait ésotérique. Un opérant avec cinq heures de sommeil n'a pas d'attention à "
              "diriger : il a un déficit."},

    "Hora fija de acostarse, incluido el fin de semana. La regularidad pesa más que la "
    "cantidad total.": {
        "en": "A fixed bedtime, weekends included. Regularity weighs more than the total "
              "amount.",
        "fr": "Une heure de coucher fixe, week-end compris. La régularité pèse plus que la "
              "quantité totale."},

    "La última hora sin pantalla y sin trabajo. Si solo puedes cambiar una cosa de este "
    "capítulo, cambia esta.": {
        "en": "The last hour with no screen and no work. If you can change only one thing in "
              "this chapter, change this one.",
        "fr": "La dernière heure sans écran et sans travail. Si vous ne pouvez changer qu'une "
              "seule chose de ce chapitre, changez celle-là."},

    "Habitación fresca y a oscuras. Es barato y funciona.": {
        "en": "A cool, dark room. It is cheap and it works.",
        "fr": "Une chambre fraîche et dans le noir. C'est bon marché et cela fonctionne."},

    "Si la sesión es por la mañana —lo recomendable—, se levanta media hora antes, no se "
    "recorta el sueño por el otro extremo.": {
        "en": "If the session is in the morning —which is what is recommended— you get up half "
              "an hour earlier; you do not trim sleep off the other end.",
        "fr": "Si la séance a lieu le matin —ce qui est recommandé—, on se lève une demi-heure "
              "plus tôt ; on ne rogne pas le sommeil par l'autre bout."},

    "La comida, en clave de atención": {
        "en": "Food, in terms of attention", "fr": "La nourriture, du point de vue de l'attention"},

    "El criterio aquí no es la composición corporal: es la estabilidad. Lo que interesa es "
    "evitar los dos estados que arruinan una sesión, que son la somnolencia posprandial y la "
    "irritabilidad del hambre.": {
        "en": "The criterion here is not body composition: it is stability. What matters is "
              "avoiding the two states that ruin a session, which are post-meal drowsiness and "
              "the irritability of hunger.",
        "fr": "Le critère ici n'est pas la composition corporelle : c'est la stabilité. Ce qui "
              "importe, c'est d'éviter les deux états qui ruinent une séance, à savoir la "
              "somnolence postprandiale et l'irritabilité de la faim."},

    "Operar dos horas después de comer o antes de desayunar. En los dos casos el estómago está "
    "tranquilo.": {
        "en": "Operate two hours after a meal or before breakfast. In both cases the stomach is "
              "quiet.",
        "fr": "Opérer deux heures après le repas ou avant le petit-déjeuner. Dans les deux cas "
              "l'estomac est tranquille."},

    "Proteína y verdura en la comida previa; azúcar rápido, no. El bajón posterior cae justo "
    "en la sesión.": {
        "en": "Protein and vegetables in the preceding meal; fast sugar, no. The slump "
              "afterwards falls right in the middle of the session.",
        "fr": "Protéines et légumes au repas précédent ; sucre rapide, non. Le coup de barre qui "
              "suit tombe en plein dans la séance."},

    "Cafeína, si se usa, temprano y en cantidad fija. Es el hábito que más distorsiona la "
    "percepción del propio estado, y una práctica que consiste en observar el propio estado no "
    "se lleva bien con eso.": {
        "en": "Caffeine, if used, early and in a fixed amount. It is the habit that most "
              "distorts the perception of your own state, and a practice that consists in "
              "observing your own state does not sit well with that.",
        "fr": "La caféine, si l'on en prend, tôt et en quantité fixe. C'est l'habitude qui "
              "déforme le plus la perception de son propre état, et une pratique qui consiste à "
              "observer son propre état s'en accommode mal."},

    "Agua a mano y bebida antes, no durante. Levantarse a beber a mitad de una operación es la "
    "interrupción más tonta y la más frecuente.": {
        "en": "Water within reach and drunk beforehand, not during. Getting up for a drink "
              "halfway through an operation is the silliest interruption and the commonest.",
        "fr": "De l'eau à portée et bue avant, non pendant. Se lever pour boire au milieu d'une "
              "opération est l'interruption la plus bête et la plus fréquente."},

    "Alcohol, no. El día de la sesión y el anterior. No por pureza: porque arrasa el sueño "
    "profundo y el efecto se nota al día siguiente.": {
        "en": "Alcohol, no. On the day of the session and the day before. Not for the sake of "
              "purity: because it wrecks deep sleep and the effect shows the next day.",
        "fr": "L'alcool, non. Le jour de la séance et la veille. Non par pureté : parce qu'il "
              "ravage le sommeil profond et que l'effet se remarque le lendemain."},

    "El ayuno tradicional, revisado": {
        "en": "The traditional fast, revisited", "fr": "Le jeûne traditionnel, revu"},

    "Los manuales antiguos prescriben ayunar antes de las operaciones importantes. Lo que "
    "produce el ayuno breve es un estado de alerta ligeramente aumentada que, en efecto, "
    "favorece la concentración. Lo que también produce, pasado cierto punto, es irritabilidad, "
    "mala regulación emocional y decisiones peores. La versión utilizable es la más modesta: "
    "operar en ayunas por la mañana, antes del desayuno. Eso es todo. Los ayunos de tres días "
    "de los grimorios no producen lucidez, producen hipoglucemia — y en varias condiciones "
    "médicas son peligrosos.": {
        "en": "The old manuals prescribe fasting before important operations. What a short fast "
              "produces is a slightly heightened state of alertness that does indeed favour "
              "concentration. What it also produces, past a certain point, is irritability, poor "
              "emotional regulation and worse decisions. The usable version is the most modest "
              "one: operate fasting in the morning, before breakfast. That is all. The "
              "three-day fasts of the grimoires do not produce lucidity, they produce "
              "hypoglycaemia — and in several medical conditions they are dangerous.",
        "fr": "Les vieux manuels prescrivent de jeûner avant les opérations importantes. Ce que "
              "produit le jeûne bref, c'est un état de vigilance légèrement accru qui favorise "
              "en effet la concentration. Ce qu'il produit aussi, passé un certain point, c'est "
              "de l'irritabilité, une mauvaise régulation émotionnelle et de moins bonnes "
              "décisions. La version utilisable est la plus modeste : opérer à jeun le matin, "
              "avant le petit-déjeuner. C'est tout. Les jeûnes de trois jours des grimoires ne "
              "produisent pas de la lucidité, ils produisent une hypoglycémie — et dans "
              "plusieurs affections médicales ils sont dangereux."},

    "La tradición no dice nada de esto y debería. Una sesión de veinte minutos de pie, "
    "girando, con los brazos extendidos y sosteniendo la voz exige una condición física mínima, "
    "y el operante que se cansa deja de tener atención libre. No hace falta nada heroico.": {
        "en": "The tradition says nothing about this and it ought to. A twenty-minute session "
              "standing, turning, with the arms extended and the voice sustained demands a "
              "minimum of physical condition, and an operator who tires stops having any "
              "attention to spare. Nothing heroic is required.",
        "fr": "La tradition ne dit rien de cela et elle le devrait. Une séance de vingt minutes "
              "debout, en tournant, les bras tendus et la voix soutenue exige une condition "
              "physique minimale, et l'opérant qui se fatigue n'a plus d'attention libre. Rien "
              "d'héroïque n'est nécessaire."},

    "Caminar cuarenta minutos al día. Es la base, y es suficiente para lo que aquí se pide.": {
        "en": "Walk forty minutes a day. That is the base, and it is enough for what is asked "
              "here.",
        "fr": "Marcher quarante minutes par jour. C'est la base, et c'est suffisant pour ce qui "
              "est demandé ici."},

    "Movilidad de hombro y de cadera antes de operar: tres minutos. Los brazos extendidos "
    "durante el recorrido de los cuartos se notan en el trapecio a la segunda semana.": {
        "en": "Shoulder and hip mobility before operating: three minutes. Arms held out during "
              "the round of the quarters make themselves felt in the trapezius by the second "
              "week.",
        "fr": "Mobilité d'épaule et de hanche avant d'opérer : trois minutes. Les bras tendus "
              "pendant le parcours des quartiers se font sentir dans le trapèze dès la deuxième "
              "semaine."},
}
