# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · la vista desde arriba y el cuerpo del observador
======================================================================
El ejercicio de la vista desde arriba se traduce en los mismos seis pasos y
con los mismos verbos de movimiento: sube, sigue subiendo, vuelve. Es una
secuencia que el lector recorre con los ojos cerrados y cada paso tiene que
sentirse como un peldaño más alto que el anterior.

El aviso sanitario del capítulo del cuerpo se traduce entero, con sus cuatro
supuestos nombrados uno a uno. Es la clase de frase que solo sirve si el
lector se reconoce en ella, y para eso hay que nombrarlos.
"""

T = {
    "Un último ejercicio, documentado en Marco Aurelio y practicado por los estoicos como "
    "técnica formal. Es el más rápido de todos los de este libro y el que produce el cambio "
    "de perspectiva más brusco.": {
        "en": "One last exercise, documented in Marcus Aurelius and practised by the Stoics as "
              "a formal technique. It is the fastest of all those in this book and the one "
              "that produces the most abrupt change of perspective.",
        "fr": "Un dernier exercice, documenté chez Marc Aurèle et pratiqué par les stoïciens "
              "comme une technique formelle. C'est le plus rapide de tous ceux de ce livre et "
              "celui qui produit le changement de perspective le plus brusque."},

    "El ejercicio": {"en": "The exercise", "fr": "L'exercice"},

    "Cierra los ojos y sitúate en la habitación donde estás. Sin adornos: la habitación tal "
    "cual.": {
        "en": "Close your eyes and place yourself in the room you are in. With no ornament: "
              "the room just as it is.",
        "fr": "Fermez les yeux et placez-vous dans la pièce où vous êtes. Sans ornement : la "
              "pièce telle quelle."},

    "Sube. Mira el edificio desde encima, con tu habitación dentro y las demás alrededor, "
    "cada una con alguien haciendo algo.": {
        "en": "Rise. Look at the building from above, with your room inside it and the others "
              "around, each with someone doing something.",
        "fr": "Montez. Regardez le bâtiment d'en haut, avec votre pièce dedans et les autres "
              "autour, chacune avec quelqu'un en train de faire quelque chose."},

    "Sigue subiendo. El barrio, la ciudad entera, con toda la gente que en este momento está "
    "discutiendo, durmiendo, naciendo y muriendo a la vez.": {
        "en": "Keep rising. The neighbourhood, the whole city, with all the people who at this "
              "moment are arguing, sleeping, being born and dying all at once.",
        "fr": "Continuez de monter. Le quartier, la ville entière, avec tous les gens qui en ce "
              "moment discutent, dorment, naissent et meurent à la fois."},

    "Sigue. El país, el continente, el planeta entero visto desde fuera, con su noche y su "
    "día simultáneos.": {
        "en": "Keep going. The country, the continent, the whole planet seen from outside, "
              "with its night and its day at the same time.",
        "fr": "Continuez. Le pays, le continent, la planète entière vue du dehors, avec sa nuit "
              "et son jour simultanés."},

    "Ahora añade el tiempo: la misma vista hace mil años, y dentro de mil. Las mismas "
    "ciudades con otros nombres y otra gente haciendo exactamente lo mismo.": {
        "en": "Now add time: the same view a thousand years ago, and a thousand years hence. "
              "The same cities under other names and other people doing exactly the same "
              "things.",
        "fr": "Ajoutez maintenant le temps : la même vue il y a mille ans, et dans mille ans. "
              "Les mêmes villes sous d'autres noms et d'autres gens faisant exactement la même "
              "chose."},

    "Vuelve. Baja hasta tu habitación y abre los ojos. Dos minutos en total.": {
        "en": "Come back. Descend to your room and open your eyes. Two minutes in all.",
        "fr": "Revenez. Redescendez jusqu'à votre pièce et ouvrez les yeux. Deux minutes en "
              "tout."},

    "Qué hace": {"en": "What it does", "fr": "Ce que cela fait"},

    "Reduce la escala del propio asunto, y lo hace por una vía que el razonamiento no "
    "consigue. Decirse «esto no es tan importante» no funciona porque es una afirmación y se "
    "puede discutir. Ver la escala sí funciona, porque no argumenta nada: solo cambia el "
    "punto desde el que se mira.": {
        "en": "It reduces the scale of your own affair, and it does so by a route reasoning "
              "cannot take. Telling yourself «this is not that important» does not work "
              "because it is an assertion and it can be argued with. Seeing the scale does "
              "work, because it argues nothing: it only changes the point you look from.",
        "fr": "Cela réduit l'échelle de sa propre affaire, et par une voie que le raisonnement "
              "n'atteint pas. Se dire « ce n'est pas si important » ne fonctionne pas parce que "
              "c'est une affirmation et qu'on peut la discuter. Voir l'échelle fonctionne, "
              "parce que cela n'argumente rien : cela change seulement le point d'où l'on "
              "regarde."},

    "Marco Aurelio vuelve a esta operación una y otra vez en sus notas, y siempre en el "
    "mismo contexto: cuando está molesto con alguien de su corte o abrumado por un asunto de "
    "gobierno. Que el hombre más poderoso del Mediterráneo necesitara recordarse el tamaño "
    "real de sus problemas es, probablemente, el mejor argumento a favor del ejercicio.": {
        "en": "Marcus Aurelius returns to this operation again and again in his notes, and "
              "always in the same context: when he is annoyed with someone at his court or "
              "overwhelmed by an affair of government. That the most powerful man in the "
              "Mediterranean needed to remind himself of the real size of his problems is, "
              "probably, the best argument in the exercise's favour.",
        "fr": "Marc Aurèle revient à cette opération encore et encore dans ses notes, et "
              "toujours dans le même contexte : quand il est agacé par quelqu'un de sa cour ou "
              "accablé par une affaire de gouvernement. Que l'homme le plus puissant de la "
              "Méditerranée ait eu besoin de se rappeler la taille réelle de ses problèmes est "
              "probablement le meilleur argument en faveur de l'exercice."},

    "Cuándo usarlo": {"en": "When to use it", "fr": "Quand s'en servir"},

    "Sirve muy bien": {"en": "It works very well", "fr": "Il sert très bien"},
    "Para la ofensa reciente, la discusión que no se te va de la cabeza y la preocupación "
    "por lo que otros piensen de ti.": {
        "en": "For the recent offence, the argument that will not leave your head and worry "
              "about what others think of you.",
        "fr": "Pour l'offense récente, la dispute qui ne quitte pas la tête et le souci de ce "
              "que les autres pensent de vous."},

    "Sirve regular": {"en": "It works so-so", "fr": "Il sert moyennement"},
    "Para una decisión práctica que hay que tomar: reducir la escala no ayuda a elegir.": {
        "en": "For a practical decision that has to be made: reducing the scale does not help "
              "you choose.",
        "fr": "Pour une décision pratique à prendre : réduire l'échelle n'aide pas à choisir."},

    "No sirve": {"en": "It does not work", "fr": "Il ne sert pas"},
    "Para una pérdida real. Ahí empequeñecer el asunto es faltar al respeto a lo perdido, y "
    "el capítulo 18 ya explicó por qué no todo dolor es un error de perspectiva.": {
        "en": "For a real loss. There, making the matter small is a disrespect to what was "
              "lost, and chapter 18 already explained why not all pain is an error of "
              "perspective.",
        "fr": "Pour une perte réelle. Là, rapetisser l'affaire est un manque de respect envers "
              "ce qui a été perdu, et le chapitre 18 a déjà expliqué pourquoi toute douleur "
              "n'est pas une erreur de perspective."},

    "La vista desde arriba no dice que nada importe. Dice que casi nada importa TANTO como "
    "parece desde dentro, que es una afirmación distinta y mucho más defendible. Si el "
    "ejercicio te deja indiferente ante lo que deberías atender, lo has hecho de más: el "
    "objetivo es recuperar la proporción, no perder el interés.": {
        "en": "The view from above does not say that nothing matters. It says that almost "
              "nothing matters AS MUCH as it seems from inside, which is a different assertion "
              "and a far more defensible one. If the exercise leaves you indifferent to what "
              "you ought to attend to, you have overdone it: the aim is to recover proportion, "
              "not to lose interest.",
        "fr": "La vue d'en haut ne dit pas que rien n'importe. Elle dit que presque rien "
              "n'importe AUTANT qu'il n'y paraît de l'intérieur, ce qui est une affirmation "
              "différente et bien plus défendable. Si l'exercice vous laisse indifférent à ce "
              "dont vous devriez vous occuper, vous en avez fait trop : l'objectif est de "
              "retrouver la proportion, non de perdre l'intérêt."},

    "Y con esto se cierra el repertorio. Seis instrumentos, siete láminas, un cuaderno y un "
    "año. No hay nada más, y quien practique la mitad de lo que aquí se propone durante doce "
    "meses habrá hecho más trabajo sobre sí mismo que la mayoría de la gente en una vida "
    "entera.": {
        "en": "And with that the repertoire closes. Six instruments, seven plates, a notebook "
              "and a year. There is nothing more, and anyone who practises half of what is "
              "proposed here for twelve months will have done more work on themselves than "
              "most people do in a whole lifetime.",
        "fr": "Et sur cela le répertoire se referme. Six instruments, sept planches, un carnet "
              "et une année. Il n'y a rien de plus, et qui pratiquera la moitié de ce qui est "
              "proposé ici pendant douze mois aura fait sur lui-même plus de travail que la "
              "plupart des gens en une vie entière."},

    # ── El cuerpo del observador ───────────────────────────────────────────
    "Este capítulo existe porque casi ningún libro de esta materia lo escribe, y porque sin "
    "él el resto no se sostiene. La atención no es una facultad abstracta: es una función "
    "biológica con condiciones materiales bastante concretas.": {
        "en": "This chapter exists because almost no book on this subject writes it, and "
              "because without it the rest does not hold up. Attention is not an abstract "
              "faculty: it is a biological function with quite concrete material conditions.",
        "fr": "Ce chapitre existe parce que presque aucun livre sur cette matière ne l'écrit, "
              "et parce que sans lui le reste ne tient pas. L'attention n'est pas une faculté "
              "abstraite : c'est une fonction biologique avec des conditions matérielles assez "
              "concrètes."},

    "Lo que sigue son hábitos de sentido común orientados a tener atención disponible. No es "
    "una pauta dietética individualizada ni un programa de entrenamiento, y no considera "
    "patologías. Si tienes una condición médica, tomas medicación, estás embarazada o tienes "
    "antecedentes de trastorno alimentario, revísalo con tu profesional sanitario antes de "
    "aplicar nada de aquí.": {
        "en": "What follows are common-sense habits aimed at having attention available. It is "
              "not an individualised dietary plan or a training programme, and it does not "
              "take account of pathologies. If you have a medical condition, take medication, "
              "are pregnant or have a history of an eating disorder, check with your health "
              "professional before applying anything from here.",
        "fr": "Ce qui suit sont des habitudes de bon sens visant à disposer d'attention. Ce "
              "n'est ni un plan alimentaire individualisé ni un programme d'entraînement, et "
              "cela ne tient pas compte des pathologies. Si vous avez une affection médicale, "
              "prenez un traitement, êtes enceinte ou avez des antécédents de trouble du "
              "comportement alimentaire, voyez-le avec votre professionnel de santé avant "
              "d'appliquer quoi que ce soit d'ici."},

    "El sueño, que va primero y con diferencia": {
        "en": "Sleep, which comes first and by a distance",
        "fr": "Le sommeil, qui vient en premier et de loin"},

    "No hay técnica de atención que compense dormir mal. Es el factor con más peso de todo "
    "el libro y el que menos atractivo tiene, y por eso se ignora. Un observador con cinco "
    "horas de sueño no tiene atención que dividir: tiene un déficit, y lo que va a observar "
    "es sobre todo su propia irritabilidad.": {
        "en": "There is no attention technique that makes up for sleeping badly. It is the "
              "weightiest factor in the whole book and the least attractive, and that is why "
              "it gets ignored. An observer on five hours of sleep has no attention to divide: "
              "they have a deficit, and what they are going to observe is mostly their own "
              "irritability.",
        "fr": "Aucune technique d'attention ne compense un mauvais sommeil. C'est le facteur "
              "qui pèse le plus de tout le livre et le moins séduisant, et c'est pourquoi on "
              "l'ignore. Un observateur à cinq heures de sommeil n'a pas d'attention à "
              "diviser : il a un déficit, et ce qu'il va observer est surtout sa propre "
              "irritabilité."},

    "Hora fija de acostarse, incluido el fin de semana. La regularidad pesa más que el "
    "total.": {
        "en": "A fixed bedtime, weekends included. Regularity weighs more than the total.",
        "fr": "Une heure de coucher fixe, week-end compris. La régularité pèse plus que le "
              "total."},
    "La última hora sin pantalla y sin trabajo. Si solo cambias una cosa de este capítulo, "
    "cambia esta.": {
        "en": "The last hour with no screen and no work. If you change only one thing from "
              "this chapter, change this one.",
        "fr": "La dernière heure sans écran et sans travail. Si vous ne changez qu'une chose de "
              "ce chapitre, changez celle-là."},
    "El inventario nocturno del capítulo 14 sustituye con ventaja al repaso involuntario que "
    "se hace con los ojos abiertos a las tres de la mañana.": {
        "en": "The nightly inventory of chapter 14 is a better substitute for the involuntary "
              "review carried out with the eyes open at three in the morning.",
        "fr": "L'inventaire du soir du chapitre 14 remplace avantageusement le repassage "
              "involontaire qu'on fait les yeux ouverts à trois heures du matin."},
    "Habitación fresca y a oscuras. Barato y eficaz.": {
        "en": "A cool, dark room. Cheap and effective.",
        "fr": "Une chambre fraîche et dans le noir. Bon marché et efficace."},

    "La mesa, en clave de atención": {
        "en": "The table, in terms of attention", "fr": "La table, du côté de l'attention"},

    "El criterio aquí no es la composición corporal: es la estabilidad. Interesa evitar los "
    "dos estados que hacen imposible observar nada, que son la somnolencia después de comer "
    "y la irritabilidad del hambre — y conviene saber que la segunda se confunde con enfado "
    "moral con una facilidad asombrosa.": {
        "en": "The criterion here is not body composition: it is stability. What matters is "
              "avoiding the two states that make observing anything impossible, which are "
              "drowsiness after eating and the irritability of hunger — and it is worth "
              "knowing that the second is confused with moral indignation with astonishing "
              "ease.",
        "fr": "Le critère ici n'est pas la composition corporelle : c'est la stabilité. Il "
              "s'agit d'éviter les deux états qui rendent toute observation impossible, à "
              "savoir la somnolence après le repas et l'irritabilité de la faim — et il vaut "
              "mieux savoir que la seconde se confond avec l'indignation morale avec une "
              "facilité stupéfiante."},

    "Comer despacio y sin pantalla. Es, además, el mejor ejercicio de atención dividida "
    "disponible tres veces al día.": {
        "en": "Eat slowly and without a screen. It is also the best exercise in divided "
              "attention available three times a day.",
        "fr": "Manger lentement et sans écran. C'est en outre le meilleur exercice d'attention "
              "divisée disponible trois fois par jour."},
    "Proteína y verdura en la comida principal; azúcar rápido, poco. El bajón posterior cae "
    "justo en el recuerdo de media tarde y lo estropea.": {
        "en": "Protein and vegetables at the main meal; fast sugar, little of it. The slump "
              "afterwards falls right on the mid-afternoon recollection and spoils it.",
        "fr": "Des protéines et des légumes au repas principal ; du sucre rapide, peu. Le creux "
              "qui suit tombe pile sur le rappel du milieu d'après-midi et le gâche."},
    "Cafeína temprano y en cantidad fija. Es la sustancia que más distorsiona la percepción "
    "del propio estado, y esta práctica consiste en percibir el propio estado.": {
        "en": "Caffeine early and in a fixed amount. It is the substance that most distorts "
              "the perception of your own state, and this practice consists in perceiving your "
              "own state.",
        "fr": "De la caféine tôt et en quantité fixe. C'est la substance qui déforme le plus la "
              "perception de son propre état, et cette pratique consiste à percevoir son propre "
              "état."},
    "Alcohol, poco y nunca la noche anterior a un día que importe. Arrasa el sueño profundo "
    "y el efecto se cobra al día siguiente.": {
        "en": "Alcohol, little of it and never the night before a day that matters. It "
              "flattens deep sleep and the effect is charged the next day.",
        "fr": "De l'alcool, peu et jamais la veille d'un jour qui compte. Il rase le sommeil "
              "profond et l'effet se paie le lendemain."},
    "Antes de comer fuera de horario, una pregunta escrita: ¿de qué tengo hambre? El hambre "
    "emocional se reconoce en cuanto se le pregunta.": {
        "en": "Before eating outside mealtimes, one written question: what am I hungry for? "
              "Emotional hunger is recognised the moment it is asked.",
        "fr": "Avant de manger hors des heures, une question écrite : de quoi ai-je faim ? La "
              "faim émotionnelle se reconnaît dès qu'on la lui pose."},

    "La tradición contemplativa suele ignorar el cuerpo o desconfiar de él, y en eso se "
    "equivoca. El movimiento diario hace tres cosas que sirven directamente a esta práctica: "
    "descarga la activación que si no se convierte en rumiación, mejora el sueño, y da "
    "acceso a sensaciones corporales claras, que son el material de la observación.": {
        "en": "The contemplative tradition tends to ignore the body or to distrust it, and in "
              "that it is wrong. Daily movement does three things that serve this practice "
              "directly: it discharges the activation that otherwise turns into rumination, it "
              "improves sleep, and it gives access to clear bodily sensations, which are the "
              "material of observation.",
        "fr": "La tradition contemplative a tendance à ignorer le corps ou à s'en méfier, et "
              "sur ce point elle a tort. Le mouvement quotidien fait trois choses qui servent "
              "directement cette pratique : il décharge l'activation qui autrement se change en "
              "rumination, il améliore le sommeil, et il donne accès à des sensations "
              "corporelles nettes, qui sont le matériau de l'observation."},

    "Caminar cuarenta minutos al día, y una parte de ellos sin auriculares. El paseo en "
    "silencio es una de las mejores condiciones para observar que existen.": {
        "en": "Walk forty minutes a day, and part of that without headphones. Walking in "
              "silence is one of the best conditions for observing that exist.",
        "fr": "Marcher quarante minutes par jour, dont une partie sans écouteurs. La promenade "
              "en silence est l'une des meilleures conditions d'observation qui soient."},
    "Algo de fuerza dos veces por semana. Sostener una postura erguida durante horas es una "
    "demanda de fuerza, no de buena intención.": {
        "en": "Some strength work twice a week. Holding an upright posture for hours is a "
              "demand on strength, not on good intentions.",
        "fr": "Un peu de force deux fois par semaine. Tenir une posture droite pendant des "
              "heures est une exigence de force, non de bonne intention."},
    "Movilidad de cuello y hombros a diario: son los dos puntos donde casi todo el mundo "
    "acumula la tensión que luego no sabe de dónde viene.": {
        "en": "Neck and shoulder mobility daily: they are the two points where almost everyone "
              "accumulates the tension they later cannot account for.",
        "fr": "De la mobilité du cou et des épaules chaque jour : ce sont les deux points où "
              "presque tout le monde accumule la tension dont il ne sait ensuite d'où elle "
              "vient."},
    "Nada de esto tiene que ser intenso. La constancia es la variable, como en todo lo demás "
    "de este libro.": {
        "en": "None of this has to be intense. Consistency is the variable, as in everything "
              "else in this book.",
        "fr": "Rien de tout cela n'a besoin d'être intense. La constance est la variable, comme "
              "dans tout le reste de ce livre."},

    "Las cuatro condiciones materiales de la atención": {
        "en": "The four material conditions of attention",
        "fr": "Les quatre conditions matérielles de l'attention"},

    "Suficiente y regular. Es la primera y no hay sustituto.": {
        "en": "Enough of it and regular. It is the first and there is no substitute.",
        "fr": "Suffisant et régulier. C'est la première et il n'y a pas de substitut."},

    "Glucosa estable": {"en": "Stable glucose", "fr": "Glucose stable"},
    "Comidas ordenadas. La atención es caro de mantener metabólicamente.": {
        "en": "Orderly meals. Attention is metabolically expensive to maintain.",
        "fr": "Des repas réguliers. L'attention coûte cher à entretenir sur le plan "
              "métabolique."},

    "Movimiento": {"en": "Movement", "fr": "Mouvement"},
}
