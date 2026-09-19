# -*- coding: utf-8 -*-
"""
CÓDICE DEL SÍ MISMO · los errores, el año de observación y el cierre
====================================================================
La prueba externa del libro —preguntarle a quien vive contigo si te nota
distinto— y su contraparte —si lo que notan es que estás más raro, más aislado
o más severo, la práctica está haciendo daño— se traducen enteras y en el
mismo orden. Es la única salvaguarda que el libro se pone contra sí mismo, y
el propio texto dice que vale para él igual que para cualquier otro.

Los campos de la plantilla del cuaderno son rótulos de una casilla y se
traducen igual de escuetos: se escriben a mano al lado de una raya.
"""

T = {
    "Diario y moderado. Descarga lo que si no se rumia.": {
        "en": "Daily and moderate. It discharges what otherwise gets chewed over.",
        "fr": "Quotidien et modéré. Il décharge ce qui, sinon, se rumine."},

    "Silencio": {"en": "Silence", "fr": "Silence"},
    "Ratos sin estímulo. No es un lujo espiritual: es la condición para oír algo.": {
        "en": "Stretches with no stimulus. It is not a spiritual luxury: it is the condition "
              "for hearing anything.",
        "fr": "Des moments sans stimulation. Ce n'est pas un luxe spirituel : c'est la "
              "condition pour entendre quelque chose."},

    "El resumen": {"en": "The summary", "fr": "Le résumé"},

    "Duerme a la misma hora, come despacio y sin pantalla, camina todos los días y reserva "
    "algún rato de silencio. No tiene nada de misterioso, es el noventa por ciento del "
    "trabajo, y casi nadie lo hace — que es también, si se piensa, el resumen de este libro "
    "entero.": {
        "en": "Sleep at the same hour, eat slowly and without a screen, walk every day and set "
              "aside some silence. There is nothing mysterious about it, it is ninety per cent "
              "of the work, and almost nobody does it — which is also, come to think of it, "
              "the summary of this whole book.",
        "fr": "Dormez à la même heure, mangez lentement et sans écran, marchez tous les jours "
              "et réservez-vous des moments de silence. Cela n'a rien de mystérieux, c'est "
              "quatre-vingt-dix pour cent du travail, et presque personne ne le fait — ce qui "
              "est aussi, à y réfléchir, le résumé de tout ce livre."},

    # ── Los errores ────────────────────────────────────────────────────────
    "Predecibles, y por tanto evitables.": {
        "en": "Predictable, and therefore avoidable.",
        "fr": "Prévisibles, et donc évitables."},

    "Querer hacerlo todo el día. Es imposible, produce agotamiento en una semana y termina "
    "en abandono con la conclusión falsa de que no se puede. Seis momentos de treinta "
    "segundos. Eso es todo, durante meses.": {
        "en": "Wanting to do it all day. It is impossible, it produces exhaustion within a "
              "week and it ends in abandonment with the false conclusion that it cannot be "
              "done. Six moments of thirty seconds. That is all, for months.",
        "fr": "Vouloir le faire toute la journée. C'est impossible, cela produit de "
              "l'épuisement en une semaine et cela finit en abandon avec la fausse conclusion "
              "que ce n'est pas possible. Six moments de trente secondes. C'est tout, pendant "
              "des mois."},

    "Convertir la observación en juicio. El error central: en cuanto aparece el «qué mal lo "
    "hago», la práctica se ha transformado en el bucle del capítulo 6, con vocabulario "
    "nuevo.": {
        "en": "Turning observation into judgement. The central mistake: the moment «how badly "
              "I do this» appears, the practice has turned into the loop of chapter 6, with a "
              "new vocabulary.",
        "fr": "Faire de l'observation un jugement. L'erreur centrale : dès qu'apparaît le "
              "« comme je m'y prends mal », la pratique s'est changée en la boucle du "
              "chapitre 6, avec un vocabulaire neuf."},

    "Buscar experiencias. Esperar estados inusuales, luces, sensaciones de unidad. Esta "
    "práctica no produce nada de eso y quien lo busca acaba convenciéndose de haberlo "
    "tenido. Lo que produce es más rato despierto, que es menos vistoso y bastante más "
    "útil.": {
        "en": "Looking for experiences. Expecting unusual states, lights, sensations of unity. "
              "This practice produces none of that and whoever looks for it ends up convincing "
              "themselves they have had it. What it produces is more time awake, which is less "
              "showy and considerably more useful.",
        "fr": "Chercher des expériences. Attendre des états inhabituels, des lumières, des "
              "sensations d'unité. Cette pratique ne produit rien de tel et qui le cherche "
              "finit par se convaincre de l'avoir eu. Ce qu'elle produit, c'est plus de temps "
              "éveillé, ce qui est moins spectaculaire et nettement plus utile."},

    "Leer en lugar de practicar. Diez libros y tres semanas de cuaderno. Es el error más "
    "cómodo y el más difícil de reconocer, porque leer también se siente como progreso.": {
        "en": "Reading instead of practising. Ten books and three weeks of notebook. It is the "
              "most comfortable mistake and the hardest to recognise, because reading also "
              "feels like progress.",
        "fr": "Lire au lieu de pratiquer. Dix livres et trois semaines de carnet. C'est "
              "l'erreur la plus confortable et la plus difficile à reconnaître, car lire donne "
              "aussi le sentiment de progresser."},

    "No escribir. Sin registro no hay comparación, sin comparación no hay corrección, y sin "
    "corrección esto es repetición, no práctica.": {
        "en": "Not writing. Without a record there is no comparison, without comparison there "
              "is no correction, and without correction this is repetition, not practice.",
        "fr": "Ne pas écrire. Sans relevé pas de comparaison, sans comparaison pas de "
              "correction, et sans correction ceci est de la répétition, non de la pratique."},

    "Contarlo. Explicarle a la gente lo que estás haciendo produce una satisfacción "
    "inmediata que sustituye a la del trabajo, y de paso convierte la práctica en identidad. "
    "Hazlo y no lo cuentes.": {
        "en": "Telling people. Explaining to others what you are doing produces an immediate "
              "satisfaction that substitutes for the satisfaction of the work, and along the "
              "way turns the practice into an identity. Do it and do not talk about it.",
        "fr": "Le raconter. Expliquer aux gens ce que vous faites produit une satisfaction "
              "immédiate qui se substitue à celle du travail, et transforme au passage la "
              "pratique en identité. Faites-le et n'en parlez pas."},

    "Practicar en crisis. La observación intensiva no es donde se resuelve una crisis aguda; "
    "en el mejor caso no ayuda. En crisis se reduce a lo mínimo, se cuida el sueño y se "
    "busca ayuda.": {
        "en": "Practising in a crisis. Intensive observation is not where an acute crisis gets "
              "resolved; at best it does not help. In a crisis you reduce it to the minimum, "
              "you look after your sleep and you seek help.",
        "fr": "Pratiquer en crise. L'observation intensive n'est pas là où se résout une crise "
              "aiguë ; au mieux elle n'aide pas. En crise on réduit au minimum, on soigne le "
              "sommeil et on cherche de l'aide."},

    "Hay una manera muy simple de saber si esto está funcionando, y no tiene nada que ver "
    "con lo que se sienta durante los ejercicios: pregúntale a quien vive contigo si te nota "
    "distinto, y en qué. Si llevas seis meses y nadie ha notado nada en ninguna dirección, "
    "algo no está ocurriendo donde tendría que ocurrir.": {
        "en": "There is a very simple way of knowing whether this is working, and it has "
              "nothing to do with what is felt during the exercises: ask whoever lives with "
              "you whether they find you different, and in what. If you are six months in and "
              "nobody has noticed anything in any direction, something is not happening where "
              "it ought to be happening.",
        "fr": "Il existe une façon très simple de savoir si cela fonctionne, et elle n'a rien à "
              "voir avec ce que l'on ressent pendant les exercices : demandez à qui vit avec "
              "vous s'il vous trouve différent, et en quoi. Si vous en êtes à six mois et que "
              "personne n'a rien remarqué dans aucun sens, quelque chose ne se produit pas là "
              "où cela devrait."},

    "Si lo que notan es que estás más raro, más aislado o más severo, la práctica está "
    "haciendo daño y hay que parar y revisarla. Una disciplina de atención bien llevada hace "
    "a la gente más presente y más fácil de tratar. Cualquier camino que te aleje de los "
    "tuyos y te convenza de que eso es progreso está mal construido, y ese diagnóstico vale "
    "para este libro igual que para cualquier otro.": {
        "en": "If what they notice is that you are odder, more isolated or more severe, the "
              "practice is doing harm and it has to be stopped and reviewed. A well-run "
              "discipline of attention makes people more present and easier to deal with. Any "
              "road that takes you away from your own people and convinces you that this is "
              "progress is badly built, and that diagnosis applies to this book just as it "
              "does to any other.",
        "fr": "Si ce qu'ils remarquent est que vous êtes plus étrange, plus isolé ou plus "
              "sévère, la pratique fait du mal et il faut l'arrêter et la revoir. Une "
              "discipline d'attention bien menée rend les gens plus présents et plus faciles à "
              "vivre. Tout chemin qui vous éloigne des vôtres et vous convainc que c'est un "
              "progrès est mal construit, et ce diagnostic vaut pour ce livre comme pour "
              "n'importe quel autre."},

    # ── El año de observación ──────────────────────────────────────────────
    "Un plan de doce meses y un cuaderno. Con esto el libro termina.": {
        "en": "A twelve-month plan and a notebook. With this the book ends.",
        "fr": "Un plan de douze mois et un carnet. C'est là-dessus que le livre se termine."},

    "Solo dos cosas: los seis recuerdos del día y la entrada diaria del cuaderno. Nada más. "
    "Es deliberadamente poco.": {
        "en": "Only two things: the six recollections of the day and the daily notebook entry. "
              "Nothing else. It is deliberately little.",
        "fr": "Deux choses seulement : les six rappels de la journée et l'entrée quotidienne du "
              "carnet. Rien d'autre. C'est délibérément peu."},

    "Se añade el inventario nocturno y el ejercicio de los tres apoyos. Se empieza a trabajar "
    "la pausa.": {
        "en": "The nightly inventory and the exercise of the three supports are added. Work on "
              "the pause begins.",
        "fr": "On ajoute l'inventaire du soir et l'exercice des trois appuis. On commence à "
              "travailler la pause."},

    "Se añaden las dos columnas de Epicteto una vez por semana y el inventario de cuentas "
    "pendientes, una sola vez.": {
        "en": "Epictetus's two columns are added once a week, and the inventory of unsettled "
              "accounts, just once.",
        "fr": "On ajoute les deux colonnes d'Épictète une fois par semaine et l'inventaire des "
              "comptes en suspens, une seule fois."},

    "No se añade nada. El último trimestre sostiene lo anterior, y es el que prueba si hay "
    "práctica o hubo entusiasmo.": {
        "en": "Nothing is added. The last quarter sustains what came before, and it is the one "
              "that proves whether there is a practice or there was enthusiasm.",
        "fr": "On n'ajoute rien. Le dernier trimestre tient ce qui précède, et c'est lui qui "
              "prouve s'il y a une pratique ou s'il y a eu de l'enthousiasme."},

    "El número. Recuerdos hechos frente a previstos, sacado del cuaderno. Por encima del "
    "setenta por ciento hay práctica.": {
        "en": "The number. Recollections done against those planned, taken from the notebook. "
              "Above seventy per cent there is a practice.",
        "fr": "Le nombre. Rappels faits face aux rappels prévus, tiré du carnet. Au-dessus de "
              "soixante-dix pour cent, il y a une pratique."},

    "La recuperación. Cuánto tardas en volver después de dejarlo una semana. Al principio "
    "son semanas; con el hábito instalado, días. Es el indicador más fiable de los tres.": {
        "en": "Recovery. How long you take to come back after dropping it for a week. At first "
              "it is weeks; with the habit installed, days. It is the most reliable of the "
              "three indicators.",
        "fr": "La récupération. Le temps que vous mettez à revenir après avoir laissé tomber "
              "une semaine. Au début ce sont des semaines ; l'habitude installée, des jours. "
              "C'est le plus fiable des trois indicateurs."},

    "El testimonio ajeno. Lo que nota la gente que convive contigo, preguntado "
    "directamente.": {
        "en": "Outside testimony. What the people who live with you notice, asked directly.",
        "fr": "Le témoignage d'autrui. Ce que remarquent les gens qui vivent avec vous, "
              "demandé directement."},

    # ── La plantilla del cuaderno ──────────────────────────────────────────
    "Mis seis horas": {"en": "My six hours", "fr": "Mes six heures"},
    "Mi reacción física característica": {
        "en": "My characteristic physical reaction",
        "fr": "Ma réaction physique caractéristique"},
    "El papel que más sostengo": {
        "en": "The role I hold most", "fr": "Le rôle que je tiens le plus"},
    "Lo que no quiero mirar": {
        "en": "What I do not want to look at", "fr": "Ce que je ne veux pas regarder"},
    "Escríbela. Es la más informativa de las seis y la que casi nadie rellena. Dentro de un "
    "año, releerla explicará bastante de lo que haya pasado en medio.": {
        "en": "Write it. It is the most informative of the six and the one almost nobody fills "
              "in. A year from now, rereading it will explain a good deal of what happened in "
              "between.",
        "fr": "Écrivez-la. C'est la plus informative des six et celle que presque personne ne "
              "remplit. Dans un an, la relire expliquera pas mal de ce qui sera arrivé entre "
              "les deux."},

    "Plantilla diaria": {"en": "Daily template", "fr": "Modèle quotidien"},
    "Recuerdos hechos": {"en": "Recollections done", "fr": "Rappels faits"},
    "Dónde la noté en el cuerpo": {
        "en": "Where I felt it in the body", "fr": "Où je l'ai sentie dans le corps"},
    "Recuerdos previstos / hechos": {
        "en": "Recollections planned / done", "fr": "Rappels prévus / faits"},
    "El estado que más se repite": {
        "en": "The state that repeats most", "fr": "L'état qui se répète le plus"},
    "El disparador que más se repite": {
        "en": "The trigger that repeats most", "fr": "Le déclencheur qui revient le plus"},
    "Lo que he dejado de anotar": {
        "en": "What I have stopped writing down", "fr": "Ce que j'ai cessé de noter"},
    "Qué añado el trimestre que viene": {
        "en": "What I add next quarter", "fr": "Ce que j'ajoute au trimestre prochain"},
    "Una cosa que creía de mí y era falsa": {
        "en": "One thing I believed about myself that was false",
        "fr": "Une chose que je croyais de moi et qui était fausse"},

    # ── Cierre ─────────────────────────────────────────────────────────────
    "Esa penúltima pregunta es el objetivo de todo el libro, y conviene decirlo al final "
    "para que no se pierda. No se practica la observación de sí para llegar a ningún estado, "
    "ni para conseguir calma, ni para pertenecer a nada. Se practica para averiguar cosas "
    "que uno tenía por seguras sobre sí mismo y que no eran verdad. Cada una de esas "
    "correcciones devuelve un pedazo de vida que estaba funcionando en automático.": {
        "en": "That next-to-last question is the aim of the whole book, and it is worth saying "
              "so at the end so that it does not get lost. Self-observation is not practised in "
              "order to reach any state, or to obtain calm, or to belong to anything. It is "
              "practised in order to find out things you took as certain about yourself and "
              "that were not true. Each of those corrections gives back a piece of life that "
              "was running on automatic.",
        "fr": "Cette avant-dernière question est l'objectif de tout le livre, et il vaut mieux "
              "le dire à la fin pour que cela ne se perde pas. On ne pratique pas l'observation "
              "de soi pour atteindre un état, ni pour obtenir du calme, ni pour appartenir à "
              "quoi que ce soit. On la pratique pour découvrir des choses que l'on tenait pour "
              "certaines sur soi-même et qui n'étaient pas vraies. Chacune de ces corrections "
              "rend un morceau de vie qui tournait en automatique."},

    "Y si al cabo del año tienes doce meses de cuaderno con tu letra, una creencia menos "
    "sobre ti mismo y la gente de tu alrededor te encuentra algo más presente, entonces esto "
    "ha funcionado. No hay nada más al final del camino, y resulta que es bastante.": {
        "en": "And if at the end of the year you have twelve months of notebook in your own "
              "hand, one belief less about yourself and the people around you find you a "
              "little more present, then this has worked. There is nothing more at the end of "
              "the road, and it turns out to be quite a lot.",
        "fr": "Et si au bout de l'année vous avez douze mois de carnet de votre écriture, une "
              "croyance de moins sur vous-même et que les gens autour de vous vous trouvent un "
              "peu plus présent, alors cela a fonctionné. Il n'y a rien de plus au bout du "
              "chemin, et il se trouve que c'est déjà beaucoup."},
}
