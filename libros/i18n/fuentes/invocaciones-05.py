# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · el círculo y los cuatro cuartos
============================================================
Los cuatro cuartos emparejan punto cardinal, elemento, función y hora, y esos
cuatro datos van siempre en el mismo orden en las tres lenguas. El capítulo
dice que el recorrido es un inventario: el lector lo hace girando sobre sí
mismo, y una parada que llegue desordenada le rompe la vuelta.

La regla del triángulo termina mandando cerrar y volver mañana. Es una
instrucción y se traduce como tal, en imperativo, sin convertirla en consejo.
"""

T = {
    "Triángulo": {"en": "Triangle", "fr": "Triangle"},
    "Figura situada FUERA del círculo. En este libro es el lugar donde se pone lo que se "
    "quiere examinar sin identificarse con ello.": {
        "en": "A figure placed OUTSIDE the circle. In this book it is the place where you put "
              "whatever you want to examine without identifying with it.",
        "fr": "Figure située HORS du cercle. Dans ce livre, c'est l'endroit où l'on place ce "
              "que l'on veut examiner sans s'y identifier."},

    "Vibrar": {"en": "Vibrate", "fr": "Vibrer"},
    "Sostener una vocalización en el pecho hasta agotar el aire. Técnica respiratoria, "
    "descrita como tal en el capítulo 10.": {
        "en": "Sustaining a vocalisation in the chest until the air runs out. A breathing "
              "technique, described as such in chapter 10.",
        "fr": "Tenir une vocalisation dans la poitrine jusqu'à épuiser l'air. Technique "
              "respiratoire, décrite comme telle au chapitre 10."},

    # ── El círculo ─────────────────────────────────────────────────────────
    "El círculo es la primera pieza y la peor entendida. La imagen popular —el operante "
    "encerrado en un trazo de tiza para que no lo alcance lo que ha llamado— es literatura "
    "del siglo XIX y no resiste dos minutos de examen. Si nada exterior acude, no hay de qué "
    "protegerse.": {
        "en": "The circle is the first piece and the worst understood. The popular image —the "
              "operator shut inside a chalk line so that what they have called cannot reach "
              "them— is nineteenth-century literature and does not survive two minutes of "
              "examination. If nothing external comes, there is nothing to be protected from.",
        "fr": "Le cercle est la première pièce et la plus mal comprise. L'image populaire "
              "—l'opérant enfermé dans un trait de craie pour que ce qu'il a appelé ne "
              "l'atteigne pas— est de la littérature du XIXe siècle et ne résiste pas à deux "
              "minutes d'examen. Si rien d'extérieur ne vient, il n'y a rien contre quoi se "
              "protéger."},

    "Lo que el círculo hace es otra cosa, y es mucho más útil: establece un dentro y un "
    "fuera. Mientras estás dentro, esto es lo que haces; cuando sales, has terminado. Un "
    "límite físico convierte una intención difusa en un acto con principio y final, y esa "
    "conversión es la mitad del trabajo.": {
        "en": "What the circle does is something else, and it is far more useful: it "
              "establishes an inside and an outside. While you are inside, this is what you "
              "are doing; when you step out, you have finished. A physical boundary turns a "
              "blurred intention into an act with a beginning and an end, and that conversion "
              "is half the work.",
        "fr": "Ce que fait le cercle est autre chose, et c'est bien plus utile : il établit un "
              "dedans et un dehors. Tant que vous êtes dedans, voilà ce que vous faites ; "
              "quand vous sortez, vous avez terminé. Une limite physique transforme une "
              "intention floue en un acte avec un début et une fin, et cette transformation "
              "est la moitié du travail."},

    '<span class="fig-n">Lám. 1</span> El círculo con sus cuatro cuartos, cada uno con su '
    "elemento, su función y su hora. En el centro, el operante. A la derecha, fuera del "
    "trazo, el triángulo de examen.": {
        "en": '<span class="fig-n">Pl. 1</span> The circle with its four quarters, each with '
              "its element, its function and its hour. At the centre, the operator. On the "
              "right, outside the line, the triangle of examination.",
        "fr": '<span class="fig-n">Pl. 1</span> Le cercle avec ses quatre quartiers, chacun '
              "avec son élément, sa fonction et son heure. Au centre, l'opérant. À droite, hors "
              "du tracé, le triangle d'examen."},

    "Los cuatro cuartos": {"en": "The four quarters", "fr": "Les quatre quartiers"},

    "Cada punto cardinal lleva asignado un elemento, y cada elemento nombra una función del "
    "operante. La correspondencia es tradicional y se ha mantenido notablemente estable "
    "desde el Renacimiento.": {
        "en": "Each cardinal point has an element assigned to it, and each element names a "
              "function of the operator. The correspondence is traditional and has remained "
              "remarkably stable since the Renaissance.",
        "fr": "Chaque point cardinal se voit assigner un élément, et chaque élément nomme une "
              "fonction de l'opérant. La correspondance est traditionnelle et s'est maintenue "
              "remarquablement stable depuis la Renaissance."},

    "Los cuatro cuartos y lo que nombran": {
        "en": "The four quarters and what they name",
        "fr": "Les quatre quartiers et ce qu'ils nomment"},

    "Este · Aire": {"en": "East · Air", "fr": "Est · Air"},
    "El aliento. La respiración, la palabra, el pensamiento que se articula. Hora: el "
    "amanecer.": {
        "en": "Breath. Breathing, the word, thought as it takes shape. Hour: dawn.",
        "fr": "Le souffle. La respiration, la parole, la pensée qui s'articule. Heure : l'aube."},

    "Sur · Fuego": {"en": "South · Fire", "fr": "Sud · Feu"},
    "La voluntad. Lo que se decide y se sostiene. Hora: el mediodía.": {
        "en": "Will. What is decided and held to. Hour: noon.",
        "fr": "La volonté. Ce qui se décide et se tient. Heure : midi."},

    "Oeste · Agua": {"en": "West · Water", "fr": "Ouest · Eau"},
    "La memoria. Lo que se siente y lo que se recuerda. Hora: el atardecer.": {
        "en": "Memory. What is felt and what is remembered. Hour: dusk.",
        "fr": "La mémoire. Ce qui se ressent et ce dont on se souvient. Heure : le crépuscule."},

    "Norte · Tierra": {"en": "North · Earth", "fr": "Nord · Terre"},
    "El cuerpo. Lo que pesa, lo que se cansa, lo que sostiene todo lo demás. Hora: la "
    "medianoche.": {
        "en": "The body. What weighs, what tires, what holds up everything else. Hour: "
              "midnight.",
        "fr": "Le corps. Ce qui pèse, ce qui se fatigue, ce qui soutient tout le reste. "
              "Heure : minuit."},

    "El recorrido de los cuatro cuartos en una operación no es decorativo: es un inventario. "
    "Se pasa por el aliento, por la voluntad, por la memoria y por el cuerpo, y en cada "
    "parada se comprueba en qué estado están. Hecho con atención, el simple recorrido ya "
    "cambia el estado de partida.": {
        "en": "Going round the four quarters in an operation is not decorative: it is an "
              "inventory. You pass through breath, through will, through memory and through "
              "the body, and at each stop you check what state they are in. Done attentively, "
              "the round alone already changes the state you started from.",
        "fr": "Le parcours des quatre quartiers dans une opération n'est pas décoratif : c'est "
              "un inventaire. On passe par le souffle, par la volonté, par la mémoire et par "
              "le corps, et à chaque arrêt on vérifie dans quel état ils sont. Fait avec "
              "attention, le seul parcours change déjà l'état de départ."},

    "El triángulo, y por qué va fuera": {
        "en": "The triangle, and why it goes outside",
        "fr": "Le triangle, et pourquoi il va dehors"},

    "Los grimorios sitúan siempre el triángulo fuera del círculo: lo que se convoca se pone "
    "ahí, a la vista y a distancia. Leído en clave psicológica, el gesto es de una precisión "
    "notable. Poner algo fuera del círculo es mirarlo sin ser eso: nombrar un miedo, una "
    "obsesión o una cólera, colocarla enfrente y examinarla desde una posición que no es la "
    "suya. Es exactamente lo contrario de identificarse.": {
        "en": "The grimoires always place the triangle outside the circle: what is summoned "
              "goes there, in view and at a distance. Read psychologically, the gesture is "
              "remarkably precise. Putting something outside the circle is looking at it "
              "without being it: naming a fear, an obsession or a rage, placing it opposite "
              "and examining it from a position that is not its own. It is exactly the "
              "opposite of identifying.",
        "fr": "Les grimoires placent toujours le triangle hors du cercle : ce que l'on convoque "
              "s'y met, en vue et à distance. Lu en clé psychologique, le geste est d'une "
              "précision remarquable. Mettre quelque chose hors du cercle, c'est le regarder "
              "sans l'être : nommer une peur, une obsession ou une colère, la placer en face et "
              "l'examiner depuis une position qui n'est pas la sienne. C'est exactement le "
              "contraire de s'identifier."},

    "La regla del triángulo": {
        "en": "The rule of the triangle", "fr": "La règle du triangle"},

    "Nunca se examina algo estando dentro de ello. Si al poner un asunto en el triángulo "
    "notas que sigues dentro del asunto —que se te acelera el pulso, que empiezas a discutir "
    "mentalmente—, la operación de ese día ha terminado: cierra y vuelve mañana. Forzarlo no "
    "produce lucidez, produce agitación.": {
        "en": "You never examine something from inside it. If, on putting a matter in the "
              "triangle, you notice that you are still inside the matter —your pulse speeds "
              "up, you start arguing in your head— that day's operation is over: close and "
              "come back tomorrow. Forcing it does not produce lucidity, it produces "
              "agitation.",
        "fr": "On n'examine jamais quelque chose en étant dedans. Si, en mettant une affaire "
              "dans le triangle, vous remarquez que vous êtes toujours dans l'affaire —le "
              "pouls s'accélère, vous commencez à discuter dans votre tête— l'opération du jour "
              "est terminée : clôturez et revenez demain. Forcer ne produit pas de lucidité, "
              "cela produit de l'agitation."},

    "Cómo se traza en la práctica": {
        "en": "How it is traced in practice", "fr": "Comment on le trace en pratique"},

    "Despeja un espacio en el que puedas girar con los brazos extendidos sin tocar nada. "
    "Metro y medio de diámetro es suficiente.": {
        "en": "Clear a space in which you can turn with your arms outstretched without "
              "touching anything. A metre and a half across is enough.",
        "fr": "Dégagez un espace où vous pouvez tourner les bras tendus sans rien toucher. Un "
              "mètre cinquante de diamètre suffit."},

    "Sitúa el este. Si no sabes dónde está, cualquier brújula de teléfono sirve; y si te da "
    "igual, decide uno y no lo cambies nunca.": {
        "en": "Locate the east. If you do not know where it is, any phone compass will do; and "
              "if it makes no difference to you, decide on one and never change it.",
        "fr": "Repérez l'est. Si vous ne savez pas où il est, n'importe quelle boussole de "
              "téléphone fait l'affaire ; et si cela vous est égal, décidez-en un et n'en "
              "changez jamais."},
}
