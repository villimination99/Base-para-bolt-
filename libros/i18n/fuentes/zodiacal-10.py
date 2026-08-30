# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · la precesión, los dos zodiacos y la doctrina de la secta
==========================================================================
Todas las cifras del capítulo son datos y se copian: 50,3 segundos de arco al
año, un grado cada 71 años y medio, 25 800 años de ciclo, 24 grados desde el
siglo II y 2 150 años por era, que es 25 800 dividido entre 12 y el texto lo
dice. En inglés llevan punto decimal y coma de millar; en francés, coma
decimal y espacio.

Ayanamsa conserva su nombre sánscrito. Es el término que la astrología india
usa para su propia corrección y no tiene equivalente en las otras dos lenguas.

El párrafo de la posición del libro corta por los dos lados: ni la precesión
refuta la astrología ni la precesión da igual. Se traduce sin inclinar la
balanza a ningún lado, que es lo que hace que valga.
"""

T = {
    "Los números, que no se discuten": {
        "en": "The numbers, which are not in dispute",
        "fr": "Les nombres, qui ne se discutent pas"},

    "Velocidad": {"en": "Speed", "fr": "Vitesse"},
    "Unos 50,3 segundos de arco al año": {
        "en": "About 50.3 arcseconds a year",
        "fr": "Environ 50,3 secondes d'arc par an"},

    "Un grado": {"en": "One degree", "fr": "Un degré"},
    "Cada 71 años y medio, aproximadamente": {
        "en": "Every 71 and a half years, approximately",
        "fr": "Tous les 71 ans et demi, environ"},

    "Ciclo completo": {"en": "Complete cycle", "fr": "Cycle complet"},
    "Unos 25 800 años": {"en": "About 25,800 years", "fr": "Environ 25 800 ans"},

    "Desde Ptolomeo": {"en": "Since Ptolemy", "fr": "Depuis Ptolémée"},
    "Unos 24 grados acumulados desde el siglo II": {
        "en": "About 24 degrees accumulated since the second century",
        "fr": "Environ 24 degrés accumulés depuis le IIe siècle"},

    "Consecuencia": {"en": "Consequence", "fr": "Conséquence"},
    "El signo de Aries ya no coincide con la constelación de Aries": {
        "en": "The sign of Aries no longer coincides with the constellation of Aries",
        "fr": "Le signe du Bélier ne coïncide plus avec la constellation du Bélier"},

    '<span class="fig-n">Lám. 10</span> Dos rejillas sobre el mismo círculo: fuera, los doce '
    "signos donde los fijó la tradición; dentro, las constelaciones del mismo nombre, corridas "
    "veinticuatro grados por la precesión. El hueco entre las dos es el dato de este "
    "capítulo.": {
        "en": '<span class="fig-n">Pl. 10</span> Two grids on the same circle: outside, the '
              "twelve signs where the tradition fixed them; inside, the constellations of the "
              "same name, shifted twenty-four degrees by precession. The gap between the two is "
              "this chapter's datum.",
        "fr": '<span class="fig-n">Pl. 10</span> Deux grilles sur le même cercle : dehors, les '
              "douze signes là où la tradition les a fixés ; dedans, les constellations du même "
              "nom, décalées de vingt-quatre degrés par la précession. L'écart entre les deux "
              "est la donnée de ce chapitre."},

    "Lo que esto significa, dicho sin rodeos": {
        "en": "What this means, said plainly", "fr": "Ce que cela signifie, sans détour"},

    "Que cuando alguien dice «soy Aries» no está diciendo que el Sol estuviera delante de la "
    "constelación de Aries el día de su nacimiento. Estaba delante de la de Piscis. El signo y "
    "la constelación comparten nombre y ya no comparten sitio.": {
        "en": "That when somebody says «I'm an Aries» they are not saying the Sun was in front "
              "of the constellation of Aries on the day they were born. It was in front of "
              "Pisces. The sign and the constellation share a name and no longer share a place.",
        "fr": "Que lorsque quelqu'un dit « je suis Bélier », il ne dit pas que le Soleil se "
              "trouvait devant la constellation du Bélier le jour de sa naissance. Il se "
              "trouvait devant celle des Poissons. Le signe et la constellation partagent un nom "
              "et ne partagent plus de place."},

    "Las dos respuestas que existen, y son las dos legítimas": {
        "en": "The two answers that exist, and both are legitimate",
        "fr": "Les deux réponses qui existent, et toutes deux sont légitimes"},

    "Zodiaco tropical y zodiaco sidéreo": {
        "en": "Tropical zodiac and sidereal zodiac",
        "fr": "Zodiaque tropique et zodiaque sidéral"},

    "Tropical": {"en": "Tropical", "fr": "Tropique"},
    "Cuenta desde el equinoccio de primavera, que es un hecho estacional. El 0° de Aries es "
    "«el día en que empieza la primavera», no «la constelación de Aries». Es el que usa la "
    "astrología occidental y el que usa este libro.": {
        "en": "It counts from the spring equinox, which is a seasonal fact. 0° Aries is «the "
              "day spring begins», not «the constellation of Aries». It is the one Western "
              "astrology uses and the one this book uses.",
        "fr": "Il compte depuis l'équinoxe de printemps, qui est un fait saisonnier. Le 0° du "
              "Bélier est « le jour où commence le printemps », non « la constellation du "
              "Bélier ». C'est celui qu'emploie l'astrologie occidentale et celui qu'emploie ce "
              "livre."},

    "Sidéreo": {"en": "Sidereal", "fr": "Sidéral"},
    "Cuenta desde las estrellas y corrige la deriva. Es el que usa la astrología india, y es "
    "astronómicamente más literal. La diferencia entre los dos se llama ayanamsa y hoy vale "
    "unos 24 grados.": {
        "en": "It counts from the stars and corrects the drift. It is the one Indian astrology "
              "uses, and it is astronomically more literal. The difference between the two is "
              "called the ayanamsa and today it is worth about 24 degrees.",
        "fr": "Il compte depuis les étoiles et corrige la dérive. C'est celui qu'emploie "
              "l'astrologie indienne, et il est astronomiquement plus littéral. La différence "
              "entre les deux s'appelle l'ayanamsa et vaut aujourd'hui quelque 24 degrés."},

    "Que existan dos zodiacos incompatibles y que ambas tradiciones lleven siglos funcionando "
    "con el suyo dice algo importante sobre qué clase de sistema es este. Si midiera una "
    "influencia física de las estrellas, uno de los dos tendría que estar equivocado y sería "
    "comprobable cuál. Como es un sistema simbólico de clasificación, los dos funcionan igual "
    "de bien dentro de sus propias reglas — y eso, más que una defensa, es una descripción.": {
        "en": "That two incompatible zodiacs should exist and that both traditions should have "
              "been working with their own for centuries says something important about what "
              "kind of system this is. If it measured a physical influence of the stars, one of "
              "the two would have to be wrong and it would be verifiable which. Since it is a "
              "symbolic system of classification, both work equally well inside their own "
              "rules — and that, more than a defence, is a description.",
        "fr": "Qu'il existe deux zodiaques incompatibles et que les deux traditions fonctionnent "
              "depuis des siècles avec le leur dit quelque chose d'important sur le genre de "
              "système dont il s'agit. S'il mesurait une influence physique des étoiles, l'un "
              "des deux devrait avoir tort et l'on pourrait vérifier lequel. Comme c'est un "
              "système symbolique de classification, tous deux fonctionnent aussi bien dans "
              "leurs propres règles — et cela, plus qu'une défense, est une description."},

    "La posición de este libro": {
        "en": "This book's position", "fr": "La position de ce livre"},

    "Se usa el zodiaco tropical y se dice por qué: porque lo que este libro hace con los doce "
    "signos es un calendario del temperamento anclado en las estaciones, y el ciclo de las "
    "estaciones es real, comprobable y no se ha movido de sitio. Aries es el impulso que rompe "
    "el invierno; eso sigue ocurriendo cada marzo con independencia de qué estrellas haya "
    "detrás. Si alguien te dice que la precesión «refuta» la astrología, ha refutado una "
    "versión que ningún astrólogo serio sostiene desde Ptolomeo — y si te dice que la "
    "precesión no importa, tampoco te está diciendo la verdad.": {
        "en": "The tropical zodiac is used, and why is stated: because what this book does with "
              "the twelve signs is a calendar of temperament anchored in the seasons, and the "
              "cycle of the seasons is real, verifiable and has not shifted. Aries is the "
              "impulse that breaks winter; that goes on happening every March regardless of "
              "which stars lie behind it. If somebody tells you that precession «refutes» "
              "astrology, they have refuted a version no serious astrologer has held since "
              "Ptolemy — and if they tell you precession does not matter, they are not telling "
              "you the truth either.",
        "fr": "On emploie le zodiaque tropique et l'on dit pourquoi : parce que ce que ce livre "
              "fait des douze signes est un calendrier du tempérament ancré dans les saisons, et "
              "que le cycle des saisons est réel, vérifiable et n'a pas bougé de place. Le "
              "Bélier est l'élan qui rompt l'hiver ; cela continue de se produire chaque mars "
              "quelles que soient les étoiles qu'il y a derrière. Si l'on vous dit que la "
              "précession « réfute » l'astrologie, on a réfuté une version qu'aucun astrologue "
              "sérieux ne soutient depuis Ptolémée — et si l'on vous dit que la précession n'a "
              "pas d'importance, on ne vous dit pas la vérité non plus."},

    "El bonus, que es lo que vale el capítulo": {
        "en": "The bonus, which is what the chapter is worth",
        "fr": "Le bonus, qui est ce que vaut le chapitre"},

    "Los famosos «signos de los tiempos» —la era de Piscis, la era de Acuario— salen "
    "exactamente de aquí. Como el punto vernal retrocede un signo cada 2 150 años "
    "aproximadamente (25 800 dividido entre 12), la constelación que aloja el equinoccio de "
    "primavera cambia cada dos milenios. De ahí la era de Aries, la de Piscis y la de Acuario. "
    "La aritmética es impecable; las fechas exactas de los cambios no, porque las "
    "constelaciones no tienen fronteras iguales y cada autor pone el límite donde le conviene. "
    "Cuando leas una fecha muy precisa para el comienzo de la era de Acuario, sabes ya que "
    "alguien ha elegido una frontera y no te lo ha dicho.": {
        "en": "The famous «signs of the times» —the age of Pisces, the age of Aquarius— come "
              "exactly from here. Since the vernal point moves back one sign every 2,150 years "
              "approximately (25,800 divided by 12), the constellation housing the spring "
              "equinox changes every two millennia. Hence the age of Aries, that of Pisces and "
              "that of Aquarius. The arithmetic is impeccable; the exact dates of the changes "
              "are not, because the constellations do not have equal borders and every author "
              "puts the limit where it suits them. When you read a very precise date for the "
              "beginning of the age of Aquarius, you already know somebody has chosen a border "
              "and not told you.",
        "fr": "Les fameux « signes des temps » —l'ère des Poissons, l'ère du Verseau— sortent "
              "exactement de là. Comme le point vernal recule d'un signe tous les 2 150 ans "
              "environ (25 800 divisé par 12), la constellation qui abrite l'équinoxe de "
              "printemps change tous les deux millénaires. D'où l'ère du Bélier, celle des "
              "Poissons et celle du Verseau. L'arithmétique est impeccable ; les dates exactes "
              "des changements ne le sont pas, car les constellations n'ont pas des frontières "
              "égales et chaque auteur place la limite où cela l'arrange. Quand vous lirez une "
              "date très précise pour le début de l'ère du Verseau, vous saurez déjà que "
              "quelqu'un a choisi une frontière et ne vous l'a pas dit."},

    # ── La secta ───────────────────────────────────────────────────────────
    "Una última pieza recuperada, breve y de las que más cambian la lectura: la doctrina de la "
    "secta, que la astrología helenística usaba en todo momento y que la moderna abandonó casi "
    "por entero.": {
        "en": "One last recovered piece, brief and among those that change the reading most: "
              "the doctrine of sect, which Hellenistic astrology used at every turn and which "
              "the modern kind abandoned almost entirely.",
        "fr": "Une dernière pièce récupérée, brève et de celles qui changent le plus la lecture : "
              "la doctrine de la secte, dont l'astrologie hellénistique se servait à tout moment "
              "et que la moderne a presque entièrement abandonnée."},

    "La división": {"en": "The division", "fr": "La division"},

    "Los siete planetas se reparten en dos bandos. Uno diurno, encabezado por el Sol; otro "
    "nocturno, encabezado por la Luna. Y la pertenencia importa porque un planeta de la secta "
    "que coincide con la hora del nacimiento opera con más soltura que el mismo planeta a "
    "contramano.": {
        "en": "The seven planets are shared between two camps. One diurnal, headed by the Sun; "
              "the other nocturnal, headed by the Moon. And membership matters because a planet "
              "of the sect that matches the hour of birth operates with more ease than the same "
              "planet going against the grain.",
        "fr": "Les sept planètes se répartissent en deux camps. L'un diurne, mené par le Soleil ; "
              "l'autre nocturne, mené par la Lune. Et l'appartenance compte, car une planète de "
              "la secte qui coïncide avec l'heure de la naissance opère avec plus d'aisance que "
              "la même planète à contre-courant."},

    "Los dos bandos": {"en": "The two camps", "fr": "Les deux camps"},
    "Secta diurna": {"en": "Diurnal sect", "fr": "Secte diurne"},
}
