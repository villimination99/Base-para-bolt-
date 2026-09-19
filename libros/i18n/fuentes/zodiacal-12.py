# -*- coding: utf-8 -*-
"""
CÓDICE ZODIACAL · Aries · fuerza, sombra, eje, decanatos, cuerpo, mesa y práctica
=================================================================================
Los siete epígrafes de la ficha de signo se fijan aquí para los doce
capítulos: la fuerza, la sombra, el eje, los tres decanatos, las tres caras
del signo, la mesa y la práctica del signo. El catálogo los comparte, así que
esta entrega los deja resueltos para el resto del libro.

Los tramos de decanato llevan grados y fechas: «0° a 10° · 21–31 de marzo» se
vuelve «0° to 10° · 21–31 March» y «0° à 10° · 21–31 mars». La raya de las
fechas es la del original y no se toca.

El eje se nombra con la raya que une los dos signos —Aries–Libra, Aries–Libra,
Bélier–Balance— y esa forma se repetirá en los seis ejes.

La sección del cuerpo dice que a Aries el cuidado que le toca no es descansar
sino canalizar, y esa distinción es el contenido entero del apartado: se
traduce sin convertirla en un consejo de descanso.
"""

T = {
    "La fuerza": {"en": "The strength", "fr": "La force"},

    "Aries arranca lo que otros llevan meses considerando. Tiene una relación limpia con la "
    "acción: si algo hay que hacer, se hace, y la deliberación viene después o no viene. Esa "
    "capacidad de iniciar sin garantías es rara y extraordinariamente valiosa, porque casi "
    "ningún proyecto nace con las condiciones aseguradas.": {
        "en": "Aries starts what others have been considering for months. It has a clean "
              "relationship with action: if something has to be done, it gets done, and "
              "deliberation comes afterwards or not at all. That capacity to begin without "
              "guarantees is rare and extraordinarily valuable, because hardly any project is "
              "born with its conditions assured.",
        "fr": "Le Bélier démarre ce que d'autres considèrent depuis des mois. Il a un rapport "
              "net à l'action : s'il y a quelque chose à faire, on le fait, et la délibération "
              "vient ensuite ou ne vient pas. Cette capacité à commencer sans garanties est rare "
              "et extraordinairement précieuse, car presque aucun projet ne naît avec ses "
              "conditions assurées."},

    "Es también un signo sin doblez. La franqueza de Aries puede resultar brusca, pero rara "
    "vez es traicionera: lo que te dice es lo que piensa, y lo que piensa lo piensa ahora. No "
    "guarda rencor porque no guarda casi nada — descarga y sigue.": {
        "en": "It is also a sign with no duplicity. The frankness of Aries can come across as "
              "brusque, but it is seldom treacherous: what it tells you is what it thinks, and "
              "what it thinks it thinks now. It holds no grudge because it holds hardly "
              "anything — it discharges and moves on.",
        "fr": "C'est aussi un signe sans duplicité. La franchise du Bélier peut paraître "
              "brusque, mais elle est rarement traître : ce qu'il vous dit est ce qu'il pense, "
              "et ce qu'il pense, il le pense maintenant. Il ne garde pas rancune parce qu'il ne "
              "garde presque rien — il décharge et il continue."},

    "La sombra": {"en": "The shadow", "fr": "L'ombre"},

    "La misma velocidad que le permite empezar le impide terminar. Aries acumula proyectos "
    "abiertos como otros acumulan objetos, y confunde el entusiasmo inicial con la capacidad "
    "de sostenerlo. El resultado es un historial de comienzos brillantes y cierres ajenos.": {
        "en": "The same speed that lets it begin stops it finishing. Aries accumulates open "
              "projects the way others accumulate objects, and confuses initial enthusiasm with "
              "the capacity to sustain it. The result is a record of brilliant beginnings and "
              "endings carried out by somebody else.",
        "fr": "La vitesse même qui lui permet de commencer l'empêche de finir. Le Bélier "
              "accumule les projets ouverts comme d'autres accumulent les objets, et confond "
              "l'enthousiasme initial avec la capacité de le tenir. Le résultat est un "
              "historique de débuts brillants et de fins menées par autrui."},

    "Su segunda sombra es la irritabilidad. La energía marciana que no encuentra una salida "
    "constructiva se convierte en fricción con lo que tiene delante, y eso desgasta relaciones "
    "que Aries valora de verdad. No es agresividad: es energía sin cauce.": {
        "en": "Its second shadow is irritability. Martial energy that finds no constructive "
              "outlet turns into friction with whatever is in front of it, and that wears down "
              "relationships Aries genuinely values. It is not aggression: it is energy with no "
              "channel.",
        "fr": "Sa deuxième ombre est l'irritabilité. L'énergie martienne qui ne trouve pas de "
              "sortie constructive devient friction avec ce qu'elle a devant elle, et cela use "
              "des relations auxquelles le Bélier tient vraiment. Ce n'est pas de l'agressivité : "
              "c'est de l'énergie sans lit."},

    "La tercera es la impaciencia con el ritmo de los demás. Aries interpreta la cautela como "
    "cobardía cuando muchas veces es simple prudencia.": {
        "en": "The third is impatience with other people's pace. Aries reads caution as "
              "cowardice when very often it is plain prudence.",
        "fr": "La troisième est l'impatience devant le rythme des autres. Le Bélier interprète "
              "la prudence comme de la lâcheté alors que bien souvent c'est simplement de la "
              "prudence."},

    "El eje Aries–Libra": {
        "en": "The Aries–Libra axis", "fr": "L'axe Bélier–Balance"},

    "El eje del yo y del nosotros. Aries sabe lo que quiere y no sabe consultarlo; Libra sabe "
    "consultarlo y no sabe lo que quiere. Cada uno tiene exactamente la mitad que al otro le "
    "falta.": {
        "en": "The axis of the I and the we. Aries knows what it wants and does not know how to "
              "consult about it; Libra knows how to consult and does not know what it wants. "
              "Each has exactly the half the other lacks.",
        "fr": "L'axe du moi et du nous. Le Bélier sait ce qu'il veut et ne sait pas en "
              "délibérer ; la Balance sait en délibérer et ne sait pas ce qu'elle veut. Chacun a "
              "exactement la moitié qui manque à l'autre."},

    "Los tres decanatos": {"en": "The three decans", "fr": "Les trois décans"},

    "Los treinta grados de Aries no son homogéneos. La tradición los divide en tres tramos de "
    "diez y pone al frente de cada uno un planeta distinto, que matiza el signo sin cambiarlo. "
    "Busca tu fecha: si nunca te has reconocido del todo en la descripción general, aquí suele "
    "estar la explicación.": {
        "en": "The thirty degrees of Aries are not homogeneous. The tradition divides them into "
              "three stretches of ten and puts a different planet at the head of each, which "
              "shades the sign without changing it. Find your date: if you have never quite "
              "recognised yourself in the general description, the explanation is usually here.",
        "fr": "Les trente degrés du Bélier ne sont pas homogènes. La tradition les divise en "
              "trois tronçons de dix et place à la tête de chacun une planète différente, qui "
              "nuance le signe sans le changer. Cherchez votre date : si vous ne vous êtes "
              "jamais tout à fait reconnu dans la description générale, c'est ici que se trouve "
              "d'ordinaire l'explication."},

    "Las tres caras del signo": {
        "en": "The three faces of the sign", "fr": "Les trois faces du signe"},

    "0° a 10° · 21–31 de marzo": {
        "en": "0° to 10° · 21–31 March", "fr": "0° à 10° · 21–31 mars"},
    "Marte — El impulso sin filtro. Arranca lo que nadie se atreve a arrancar y se aburre en "
    "cuanto la cosa ya funciona.": {
        "en": "Mars — Impulse with no filter. It starts what nobody dares to start and gets "
              "bored the moment the thing is working.",
        "fr": "Mars — L'élan sans filtre. Il démarre ce que personne n'ose démarrer et s'ennuie "
              "dès que la chose fonctionne."},

    "10° a 20° · 1–10 de abril": {
        "en": "10° to 20° · 1–10 April", "fr": "10° à 20° · 1–10 avril"},
    "Sol — El impulso con dirección. Aquí el arranque quiere ser visto, y eso — "
    "paradójicamente — lo hace más constante.": {
        "en": "Sun — Impulse with direction. Here the start wants to be seen, and that — "
              "paradoxically — makes it more constant.",
        "fr": "Soleil — L'élan avec une direction. Ici le démarrage veut être vu, et cela — "
              "paradoxalement — le rend plus constant."},

    "20° a 30° · 11–20 de abril": {
        "en": "20° to 30° · 11–20 April", "fr": "20° à 30° · 11–20 avril"},
    "Venus — El impulso que busca compañía. El más negociador de los tres, y el que menos "
    "disfruta ganando solo.": {
        "en": "Venus — Impulse that looks for company. The most negotiating of the three, and "
              "the one that least enjoys winning alone.",
        "fr": "Vénus — L'élan qui cherche de la compagnie. Le plus négociateur des trois, et "
              "celui qui prend le moins de plaisir à gagner seul."},

    "La tradición le asigna la cabeza, la cara y el cerebro, y de ahí vienen sus dos "
    "vulnerabilidades reales: la tensión mandibular y la cefalea de origen tensional. Aries "
    "aprieta los dientes — literalmente — y suele descubrirlo cuando ya le duele la "
    "articulación.": {
        "en": "The tradition assigns it the head, the face and the brain, and from there come "
              "its two real vulnerabilities: jaw tension and headaches of tensional origin. "
              "Aries clenches its teeth — literally — and usually finds out when the joint is "
              "already hurting.",
        "fr": "La tradition lui assigne la tête, le visage et le cerveau, et de là viennent ses "
              "deux vulnérabilités réelles : la tension de la mâchoire et la céphalée d'origine "
              "tensionnelle. Le Bélier serre les dents — littéralement — et le découvre "
              "d'ordinaire quand l'articulation lui fait déjà mal."},

    "El cuidado que le corresponde no es descansar, porque el reposo forzado le resulta "
    "insoportable. Es canalizar. Aries necesita gasto físico intenso y regular, no como "
    "estética sino como válvula: sin él, la energía se le queda dentro y se le convierte en "
    "tensión.": {
        "en": "The care that belongs to it is not resting, because forced repose is unbearable "
              "to it. It is channelling. Aries needs intense and regular physical expenditure, "
              "not as aesthetics but as a valve: without it, the energy stays inside and turns "
              "into tension.",
        "fr": "Le soin qui lui revient n'est pas de se reposer, car le repos forcé lui est "
              "insupportable. C'est de canaliser. Le Bélier a besoin d'une dépense physique "
              "intense et régulière, non comme esthétique mais comme soupape : sans elle, "
              "l'énergie lui reste dedans et se change en tension."},

    "La mesa": {"en": "The table", "fr": "La table"},

    "Comer despacio, que para Aries es la práctica más difícil de este libro. Poner el "
    "cubierto en la mesa entre bocados.": {
        "en": "Eating slowly, which for Aries is the hardest practice in this book. Putting the "
              "cutlery down on the table between mouthfuls.",
        "fr": "Manger lentement, ce qui est pour le Bélier la pratique la plus difficile de ce "
              "livre. Reposer les couverts sur la table entre deux bouchées."},

    "Hierro de fuentes reales — carne roja magra, legumbre con vitamina C, hoja verde oscura — "
    "porque su regente lo pide y porque gasta mucho.": {
        "en": "Iron from real sources — lean red meat, pulses with vitamin C, dark green "
              "leaves — because its ruler calls for it and because it spends a great deal.",
        "fr": "Du fer de sources réelles — viande rouge maigre, légumineuses avec de la vitamine "
              "C, feuilles vert foncé — parce que son régent le demande et parce qu'il dépense "
              "beaucoup."},

    "Vigilar el estimulante. Aries no necesita cafeína: necesita menos. Es el signo que peor "
    "tolera sumar aceleración a la que ya trae.": {
        "en": "Watching the stimulants. Aries does not need caffeine: it needs less. It is the "
              "sign that worst tolerates adding acceleration to the acceleration it already "
              "carries.",
        "fr": "Surveiller les excitants. Le Bélier n'a pas besoin de caféine : il en a besoin de "
              "moins. C'est le signe qui tolère le plus mal d'ajouter de l'accélération à celle "
              "qu'il porte déjà."},

    "Cena temprana y ligera. La cabeza acelerada no se apaga con el estómago lleno.": {
        "en": "An early, light dinner. A racing head does not switch off on a full stomach.",
        "fr": "Un dîner tôt et léger. Une tête emballée ne s'éteint pas l'estomac plein."},

    "La práctica del signo": {
        "en": "The practice of the sign", "fr": "La pratique du signe"},

    "Aries no aprende a esperar leyendo sobre la espera. Aprende poniéndole un número, un "
    "plazo y un testigo.": {
        "en": "Aries does not learn to wait by reading about waiting. It learns by giving it a "
              "number, a deadline and a witness.",
        "fr": "Le Bélier n'apprend pas à attendre en lisant sur l'attente. Il apprend en y "
              "mettant un nombre, un délai et un témoin."},

    "Elige una sola cosa empezada y sin terminar. Una. Escríbela en un papel y ponla donde la "
    "veas cada mañana.": {
        "en": "Choose one single thing you have started and not finished. One. Write it on a "
              "piece of paper and put it where you will see it every morning.",
        "fr": "Choisissez une seule chose commencée et non terminée. Une. Écrivez-la sur un "
              "papier et posez-le là où vous la verrez chaque matin."},

    "Divídela en cuatro partes que puedas cerrar en una semana cada una. Si una parte no cabe "
    "en una semana, divídela otra vez.": {
        "en": "Divide it into four parts you can close in a week each. If one part does not fit "
              "into a week, divide it again.",
        "fr": "Divisez-la en quatre parties que vous puissiez clore en une semaine chacune. Si "
              "une partie ne tient pas dans une semaine, divisez-la encore."},

    "Cada semana cierras una parte y la marcas. No empiezas nada nuevo hasta que el papel esté "
    "completo — y esta es la regla que dolerá.": {
        "en": "Each week you close one part and tick it off. You start nothing new until the "
              "paper is complete — and this is the rule that will hurt.",
        "fr": "Chaque semaine vous clôturez une partie et vous la cochez. Vous ne commencez rien "
              "de nouveau avant que le papier soit complet — et c'est la règle qui fera mal."},
}
