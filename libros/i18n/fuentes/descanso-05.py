# -*- coding: utf-8 -*-
"""
CÓDICE DEL DESCANSO · capítulos 4 y 5
=====================================
La aritmética de la cafeína —vida media de unas cinco horas, la mitad a las
cinco, un cuarto a las diez— sale del módulo de datos comprobados. Las cifras
se copian idénticas en los tres idiomas.
"""

T = {
    # ── Capítulo 4 · la deuda ──────────────────────────────────────────────
    "No se percibe": {"en": "It is not perceived", "fr": "Elle ne se perçoit pas"},
    "La percepción subjetiva de somnolencia se aplana mientras el rendimiento sigue "
    "cayendo. Quien lleva una semana durmiendo poco cree haberse adaptado, y lo que ha "
    "hecho es perder la capacidad de notarlo.": {
        "en": "The subjective sense of sleepiness flattens out while performance keeps "
              "falling. Someone who has slept badly for a week believes they have adapted, "
              "and what they have actually done is lose the ability to notice.",
        "fr": "La perception subjective de la somnolence s'aplatit tandis que la "
              "performance continue de baisser. Qui dort peu depuis une semaine croit "
              "s'être adapté, alors qu'il a simplement perdu la capacité de s'en rendre "
              "compte."},

    "Se paga con recargo": {
        "en": "It is repaid with a surcharge", "fr": "Elle se rembourse avec majoration"},
    "El cuerpo prioriza recuperar el sueño profundo, y en las noches de recuperación "
    "aparece más cantidad de la habitual. El de la segunda mitad se recupera peor, y es el "
    "que se había perdido.": {
        "en": "The body gives priority to recovering deep sleep, and on recovery nights "
              "more of it appears than usual. The sleep of the second half recovers less "
              "well — and that is the one that had been lost.",
        "fr": "Le corps donne la priorité à la récupération du sommeil profond, et les "
              "nuits de récupération en contiennent plus que d'habitude. Celui de la "
              "seconde moitié se récupère moins bien, et c'est justement celui qui avait "
              "été perdu."},

    "El segundo punto es el que más consecuencias tiene fuera del gimnasio. La sensación "
    "de estar bien no es un indicador fiable de estar bien, y la situación en la que eso "
    "importa de verdad es al volante. Conducir con sueño acumulado deteriora la atención y "
    "el tiempo de reacción de forma documentada, y a diferencia de otras causas de mala "
    "conducción, esta no se compensa con voluntad.": {
        "en": "The second point is the one with the most consequences outside the gym. "
              "Feeling fine is not a reliable indicator of being fine, and the situation "
              "where that really matters is behind the wheel. Driving with accumulated "
              "sleep debt degrades attention and reaction time in documented ways, and "
              "unlike other causes of poor driving, this one is not compensated for by "
              "willpower.",
        "fr": "Le deuxième point est celui qui a le plus de conséquences en dehors de la "
              "salle. Se sentir bien n'est pas un indicateur fiable d'aller bien, et la "
              "situation où cela compte vraiment, c'est au volant. Conduire avec une dette "
              "de sommeil dégrade l'attention et le temps de réaction de façon documentée, "
              "et contrairement à d'autres causes de mauvaise conduite, celle-ci ne se "
              "compense pas par la volonté."},

    "El fin de semana: qué recupera y qué estropea": {
        "en": "The weekend: what it recovers and what it spoils",
        "fr": "Le week-end : ce qu'il récupère et ce qu'il abîme"},

    "Dormir más el sábado y el domingo es mejor que no hacerlo, y conviene decirlo porque "
    "el consejo de mantener horarios rígidos suena a que dormir de más está mal. No lo "
    "está. Lo que ocurre es que tiene un coste: levantarse tres horas más tarde el domingo "
    "es, para el reloj interno, parecido a viajar a otro huso horario, y el domingo por la "
    "noche el sueño llega tarde. Es la causa más común del insomnio del domingo y del "
    "lunes espantoso.": {
        "en": "Sleeping more on Saturday and Sunday is better than not doing it, and that "
              "is worth saying because the advice to keep rigid hours sounds like sleeping "
              "in is wrong. It is not. What happens is that it has a cost: getting up three "
              "hours later on Sunday is, for the internal clock, much like travelling to "
              "another time zone, and on Sunday night sleep arrives late. It is the most "
              "common cause of Sunday insomnia and the dreadful Monday.",
        "fr": "Dormir davantage le samedi et le dimanche vaut mieux que de ne pas le faire, "
              "et il faut le dire, parce que le conseil de garder des horaires rigides "
              "donne l'impression que faire la grasse matinée serait une faute. Ce n'en est "
              "pas une. Simplement, cela a un coût : se lever trois heures plus tard le "
              "dimanche revient, pour l'horloge interne, à voyager dans un autre fuseau "
              "horaire, et le dimanche soir le sommeil arrive tard. C'est la cause la plus "
              "fréquente de l'insomnie du dimanche et du lundi épouvantable."},

    "Recuperar sí, pero acotado: hasta una hora más de lo habitual mueve poco el reloj; "
    "tres horas lo mueven bastante.": {
        "en": "Recover, yes, but within bounds: up to an hour more than usual barely moves "
              "the clock; three hours move it considerably.",
        "fr": "Récupérer, oui, mais dans des limites : jusqu'à une heure de plus que "
              "d'habitude déplace peu l'horloge ; trois heures la déplacent nettement."},

    "Es mejor adelantar la hora de acostarse el fin de semana que retrasar la de "
    "levantarse. Consigues las mismas horas sin desplazar el ancla.": {
        "en": "It is better to move bedtime earlier at the weekend than to move the "
              "get-up time later. You get the same hours without shifting the anchor.",
        "fr": "Mieux vaut avancer l'heure du coucher le week-end que reculer celle du "
              "lever. Vous obtenez les mêmes heures sans déplacer l'ancre."},

    "La hora de levantarse es el ancla más fuerte del reloj interno, sobre todo si va "
    "acompañada de luz. Si solo puedes fijar una cosa de tu horario, fija esa.": {
        "en": "Get-up time is the strongest anchor of the internal clock, above all when it "
              "comes with light. If you can fix only one thing about your schedule, fix "
              "that one.",
        "fr": "L'heure du lever est l'ancre la plus forte de l'horloge interne, surtout si "
              "elle s'accompagne de lumière. Si vous ne pouvez fixer qu'une seule chose "
              "dans votre emploi du temps, fixez celle-là."},

    # ── Capítulo 5 · la cuenta atrás ───────────────────────────────────────
    "La higiene del sueño suele presentarse como una lista de consejos desordenada y de "
    "eficacia desigual. Ordenada en el tiempo funciona mucho mejor, porque cada elemento "
    "tiene una hora a la que deja de poder arreglarse.": {
        "en": "Sleep hygiene is usually presented as a disordered list of tips of uneven "
              "effectiveness. Ordered in time it works much better, because every item has "
              "an hour after which it can no longer be fixed.",
        "fr": "L'hygiène du sommeil se présente d'ordinaire comme une liste de conseils en "
              "vrac, d'efficacité inégale. Ordonnée dans le temps, elle fonctionne bien "
              "mieux, parce que chaque élément a une heure au-delà de laquelle on ne peut "
              "plus le rattraper."},

    '<span class="fig-n">Qué se corta y cuándo, contando hacia atrás desde la hora de '
    "acostarse</span> Los tiempos son órdenes de magnitud razonables, no umbrales exactos. "
    "El de la cafeína sale de su vida media, que ronda las cinco horas en un adulto medio: "
    "a las diez horas queda todavía cerca de un octavo de la dosis circulando.": {
        "en": '<span class="fig-n">What gets cut and when, counting back from '
              "bedtime</span> The times are reasonable orders of magnitude, not exact "
              "thresholds. The caffeine one comes from its half-life, which is around five "
              "hours in an average adult: at ten hours roughly an eighth of the dose is "
              "still circulating.",
        "fr": '<span class="fig-n">Ce que l\'on coupe et quand, en comptant à rebours '
              "depuis l'heure du coucher</span> Les durées sont des ordres de grandeur "
              "raisonnables, pas des seuils exacts. Celle de la caféine découle de sa "
              "demi-vie, d'environ cinq heures chez un adulte moyen : à dix heures, il "
              "circule encore près d'un huitième de la dose."},

    "La cafeína, con su aritmética": {
        "en": "Caffeine, with its arithmetic", "fr": "La caféine, avec son arithmétique"},

    "La vida media es el tiempo que tarda el cuerpo en eliminar la mitad. Con unas cinco "
    "horas de vida media, un café de las cinco de la tarde deja la mitad de su cafeína a "
    "las diez de la noche y la cuarta parte a las tres de la madrugada. No impide dormirse "
    "necesariamente, y sí reduce la cantidad de sueño profundo de esa noche, que es un "
    "efecto que no se percibe.": {
        "en": "The half-life is the time the body takes to clear half of it. With a "
              "half-life of about five hours, a coffee at five in the afternoon leaves half "
              "its caffeine at ten at night and a quarter at three in the morning. It does "
              "not necessarily stop you falling asleep, and it does reduce the amount of "
              "deep sleep that night — an effect you do not perceive.",
        "fr": "La demi-vie est le temps que met le corps à en éliminer la moitié. Avec une "
              "demi-vie d'environ cinq heures, un café de dix-sept heures laisse la moitié "
              "de sa caféine à vingt-deux heures et le quart à trois heures du matin. Cela "
              "n'empêche pas nécessairement de s'endormir, mais cela réduit la quantité de "
              "sommeil profond de cette nuit-là — un effet que l'on ne perçoit pas."},

    "Hay además una variación individual grande en la velocidad de eliminación: hay quien "
    "metaboliza la cafeína al doble de velocidad que otro. Por eso el argumento «a mí no "
    "me afecta» puede ser literalmente cierto en unas personas y ser un error de "
    "percepción en otras. La forma de saberlo es quitarla dos semanas y comparar, no "
    "razonarlo.": {
        "en": "There is also a large individual variation in clearance speed: some people "
              "metabolise caffeine twice as fast as others. That is why the argument “it "
              "does not affect me” can be literally true for some people and a perception "
              "error for others. The way to find out is to drop it for two weeks and "
              "compare, not to reason about it.",
        "fr": "Il existe en outre une grande variation individuelle de la vitesse "
              "d'élimination : certains métabolisent la caféine deux fois plus vite que "
              "d'autres. C'est pourquoi l'argument « moi, ça ne me fait rien » peut être "
              "littéralement vrai chez les uns et relever d'une erreur de perception chez "
              "les autres. La façon de le savoir est de la supprimer deux semaines et de "
              "comparer, pas de raisonner."},

    "El alcohol, que es el engaño más extendido": {
        "en": "Alcohol, which is the most widespread deception",
        "fr": "L'alcool, qui est la tromperie la plus répandue"},

    "El alcohol acorta el tiempo que se tarda en dormirse, y de ahí viene su fama de "
    "ayudar a dormir. Lo que hace después es lo contrario: fragmenta la segunda mitad de "
    "la noche y suprime parte del sueño con movimientos oculares rápidos, que ya vimos que "
    "es justo el que vive ahí. El resultado es una noche que empieza fácil y termina mal, "
    "con más despertares y peor sensación de descanso.": {
        "en": "Alcohol shortens the time it takes to fall asleep, and that is where its "
              "reputation for helping you sleep comes from. What it does afterwards is the "
              "opposite: it fragments the second half of the night and suppresses part of "
              "the rapid eye movement sleep, which we have already seen is precisely the "
              "sleep that lives there. The result is a night that starts easy and ends "
              "badly, with more awakenings and a worse sense of rest.",
        "fr": "L'alcool raccourcit le temps qu'il faut pour s'endormir, et c'est de là que "
              "vient sa réputation d'aider à dormir. Ce qu'il fait ensuite est l'inverse : "
              "il fragmente la seconde moitié de la nuit et supprime une partie du sommeil "
              "à mouvements oculaires rapides — celui-là même qui, on l'a vu, se loge là. "
              "Le résultat est une nuit qui commence facilement et finit mal, avec plus de "
              "réveils et une moins bonne sensation de repos."},

    "Luz y temperatura, que son las dos palancas grandes": {
        "en": "Light and temperature, which are the two big levers",
        "fr": "La lumière et la température, les deux grands leviers"},
    "Las dos señales que el reloj interno lee de verdad": {
        "en": "The two signals the internal clock actually reads",
        "fr": "Les deux signaux que l'horloge interne lit réellement"},

    "Luz por la mañana": {"en": "Light in the morning", "fr": "Lumière le matin"},
    "Es la señal más potente para fijar el reloj. Diez o quince minutos de luz exterior "
    "poco después de levantarse hacen más que cualquier ritual nocturno, y es el consejo "
    "más subestimado del capítulo.": {
        "en": "It is the most powerful signal for setting the clock. Ten or fifteen minutes "
              "of outdoor light shortly after getting up do more than any night-time "
              "ritual, and it is the most underrated piece of advice in the chapter.",
        "fr": "C'est le signal le plus puissant pour caler l'horloge. Dix ou quinze minutes "
              "de lumière extérieure peu après le lever font plus que n'importe quel rituel "
              "du soir, et c'est le conseil le plus sous-estimé du chapitre."},

    "Oscuridad por la noche": {"en": "Darkness at night", "fr": "Obscurité le soir"},
    "Luz tenue y cálida en la última hora. El problema de las pantallas no es solo la luz: "
    "es lo que se hace en ellas, que activa.": {
        "en": "Dim, warm light in the last hour. The problem with screens is not only the "
              "light: it is what you do on them, which is activating.",
        "fr": "Lumière tamisée et chaude dans la dernière heure. Le problème des écrans "
              "n'est pas seulement la lumière : c'est ce qu'on y fait, et qui active."},

    "Dormir es un proceso que necesita que la temperatura central baje. Habitación fresca "
    "ayuda; una ducha caliente un par de horas antes también, porque provoca una caída "
    "posterior.": {
        "en": "Sleeping is a process that requires core temperature to fall. A cool room "
              "helps; so does a hot shower a couple of hours beforehand, because it causes "
              "a subsequent drop.",
        "fr": "Dormir est un processus qui exige que la température centrale baisse. Une "
              "chambre fraîche aide ; une douche chaude deux heures avant aussi, parce "
              "qu'elle provoque une chute ultérieure."},

    "Ruido y horario": {"en": "Noise and schedule", "fr": "Bruit et horaire"},
}
