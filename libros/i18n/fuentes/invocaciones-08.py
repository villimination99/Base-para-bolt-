# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · el hexagrama y el árbol
====================================================
Las siete fichas planetarias siguen todas la misma forma: función, tres
verbos, metal, día. Los metales conservan su nombre corriente, incluido el
azogue del mercurio, que en inglés es quicksilver y en francés vif-argent —el
nombre alquímico y no el químico, que es el que empareja con el planeta.

Las sefirot vuelven aquí numeradas, y el número va delante como en el
original: el lector está mirando el diagrama y busca por número antes que por
nombre.
"""

T = {
    '<span class="fig-n">Lám. 4</span> Los seis planetas en las puntas y el Sol en el '
    "centro. Los dos triángulos entrelazados son la misma figura vista dos veces: lo que "
    "asciende y lo que desciende.": {
        "en": '<span class="fig-n">Pl. 4</span> The six planets at the points and the Sun at '
              "the centre. The two interlaced triangles are the same figure seen twice: what "
              "ascends and what descends.",
        "fr": '<span class="fig-n">Pl. 4</span> Les six planètes aux branches et le Soleil au '
              "centre. Les deux triangles entrelacés sont la même figure vue deux fois : ce "
              "qui monte et ce qui descend."},

    "Por qué seis fuera y uno dentro": {
        "en": "Why six outside and one inside",
        "fr": "Pourquoi six dehors et une dedans"},

    "Los siete cuerpos clásicos no caben en una figura de seis puntas, y esa aparente "
    "torpeza es en realidad la mejor parte del diseño. El Sol va al centro porque no es una "
    "función más: es el punto de referencia respecto del cual las otras seis se ordenan. En "
    "el vocabulario de este libro, el centro es la identidad del operante y las seis puntas "
    "son las funciones que orbitan alrededor de ella.": {
        "en": "The seven classical bodies do not fit into a six-pointed figure, and that "
              "apparent clumsiness is in fact the best part of the design. The Sun goes at the "
              "centre because it is not one more function: it is the reference point in "
              "relation to which the other six are ordered. In this book's vocabulary, the "
              "centre is the operator's identity and the six points are the functions that "
              "orbit around it.",
        "fr": "Les sept corps classiques ne tiennent pas dans une figure à six branches, et "
              "cette maladresse apparente est en réalité la meilleure part du dessin. Le "
              "Soleil va au centre parce qu'il n'est pas une fonction de plus : il est le point "
              "de référence par rapport auquel les six autres s'ordonnent. Dans le vocabulaire "
              "de ce livre, le centre est l'identité de l'opérant et les six branches sont les "
              "fonctions qui gravitent autour d'elle."},

    "Los siete y lo que nombran": {
        "en": "The seven and what they name", "fr": "Les sept et ce qu'elles nomment"},

    "El límite. Lo que se acaba, lo que se estructura, lo que dice no. Plomo. Sábado.": {
        "en": "The limit. What ends, what gets structured, what says no. Lead. Saturday.",
        "fr": "La limite. Ce qui s'achève, ce qui se structure, ce qui dit non. Plomb. Samedi."},

    "La expansión. Lo que crece, lo que se abre, lo que se concede. Estaño. Jueves.": {
        "en": "Expansion. What grows, what opens, what is granted. Tin. Thursday.",
        "fr": "L'expansion. Ce qui croît, ce qui s'ouvre, ce qui s'accorde. Étain. Jeudi."},

    "El empuje. Lo que corta, lo que insiste, lo que se defiende. Hierro. Martes.": {
        "en": "Drive. What cuts, what insists, what defends itself. Iron. Tuesday.",
        "fr": "L'élan. Ce qui coupe, ce qui insiste, ce qui se défend. Fer. Mardi."},

    "La identidad. El centro, la vitalidad, lo que se reconoce como propio. Oro. Domingo.": {
        "en": "Identity. The centre, vitality, what is recognised as one's own. Gold. Sunday.",
        "fr": "L'identité. Le centre, la vitalité, ce que l'on reconnaît comme sien. Or. "
              "Dimanche."},

    "El vínculo. Lo que atrae, lo que valora, lo que reconcilia. Cobre. Viernes.": {
        "en": "The bond. What attracts, what values, what reconciles. Copper. Friday.",
        "fr": "Le lien. Ce qui attire, ce qui apprécie, ce qui réconcilie. Cuivre. Vendredi."},

    "La palabra. Lo que se dice, se ordena y se traduce. Azogue. Miércoles.": {
        "en": "The word. What is said, ordered and translated. Quicksilver. Wednesday.",
        "fr": "La parole. Ce qui se dit, s'ordonne et se traduit. Vif-argent. Mercredi."},

    "El ritmo. Lo que fluctúa, lo que recuerda, lo que se repite. Plata. Lunes.": {
        "en": "Rhythm. What fluctuates, what remembers, what repeats. Silver. Monday.",
        "fr": "Le rythme. Ce qui fluctue, ce qui se souvient, ce qui se répète. Argent. Lundi."},

    "Los dos triángulos": {"en": "The two triangles", "fr": "Les deux triangles"},

    "El triángulo con la punta arriba y el que la tiene abajo se leen tradicionalmente como "
    "lo que sube y lo que baja: la aspiración y la manifestación, el fuego y el agua, lo que "
    "uno quiere y lo que uno hace. Que estén entrelazados y no simplemente superpuestos es "
    "la parte importante del dibujo: no se elige entre los dos.": {
        "en": "The triangle with the point upwards and the one with the point downwards are "
              "traditionally read as what rises and what falls: aspiration and manifestation, "
              "fire and water, what you want and what you do. That they are interlaced and not "
              "simply superimposed is the important part of the drawing: you do not choose "
              "between the two.",
        "fr": "Le triangle pointe en haut et celui pointe en bas se lisent traditionnellement "
              "comme ce qui monte et ce qui descend : l'aspiration et la manifestation, le feu "
              "et l'eau, ce que l'on veut et ce que l'on fait. Qu'ils soient entrelacés et non "
              "simplement superposés est la part importante du dessin : on ne choisit pas entre "
              "les deux."},

    "Cuándo se usa el hexagrama": {
        "en": "When the hexagram is used", "fr": "Quand on emploie l'hexagramme"},

    "Después del pentagrama, nunca antes. El pentagrama pone en orden los cuatro elementos "
    "del operante; el hexagrama trabaja funciones más generales sobre esa base ya ordenada. "
    "Hacerlo al revés es como afinar después del concierto: se puede, y no sirve para nada.": {
        "en": "After the pentagram, never before. The pentagram puts the operator's four "
              "elements in order; the hexagram works more general functions on that already "
              "ordered base. Doing it the other way round is like tuning up after the concert: "
              "you can, and it is no use at all.",
        "fr": "Après le pentagramme, jamais avant. Le pentagramme met en ordre les quatre "
              "éléments de l'opérant ; l'hexagramme travaille des fonctions plus générales sur "
              "cette base déjà ordonnée. Le faire à l'envers, c'est comme accorder après le "
              "concert : on peut, et cela ne sert à rien."},

    # ── El árbol ───────────────────────────────────────────────────────────
    "La cábala aporta al sistema occidental su columna vertebral: un diagrama de diez "
    "estaciones y veintidós caminos que organiza todo lo demás. Lo que sigue es una "
    "presentación práctica, no teológica, y se limita a lo que sirve para operar.": {
        "en": "Kabbalah gives the Western system its backbone: a diagram of ten stations and "
              "twenty-two paths that organises everything else. What follows is a practical "
              "presentation, not a theological one, and it confines itself to what is of use "
              "in operating.",
        "fr": "La kabbale donne au système occidental sa colonne vertébrale : un diagramme de "
              "dix stations et vingt-deux chemins qui organise tout le reste. Ce qui suit est "
              "une présentation pratique et non théologique, et elle se limite à ce qui sert à "
              "opérer."},

    '<span class="fig-n">Lám. 5</span> El árbol: diez números repartidos en tres columnas y '
    "unidos por veintidós senderos. A la izquierda el rigor, a la derecha la clemencia, en "
    "el centro el equilibrio.": {
        "en": '<span class="fig-n">Pl. 5</span> The tree: ten numbers distributed in three '
              "columns and joined by twenty-two paths. On the left severity, on the right "
              "mercy, in the centre balance.",
        "fr": '<span class="fig-n">Pl. 5</span> L\'arbre : dix nombres répartis en trois '
              "colonnes et reliés par vingt-deux sentiers. À gauche la rigueur, à droite la "
              "clémence, au centre l'équilibre."},

    "Diez estaciones de lo abstracto a lo concreto": {
        "en": "Ten stations from the abstract to the concrete",
        "fr": "Dix stations de l'abstrait au concret"},

    "Leído de arriba abajo, el árbol describe un descenso: de lo indeterminado a lo "
    "determinado, de la idea al objeto, del impulso al hecho. Leído de abajo arriba describe "
    "el camino inverso, que es el que recorre el operante. Ambos sentidos importan y el "
    "diagrama sirve para los dos.": {
        "en": "Read from top to bottom, the tree describes a descent: from the undetermined to "
              "the determined, from the idea to the object, from the impulse to the fact. Read "
              "from bottom to top it describes the reverse path, which is the one the operator "
              "travels. Both directions matter and the diagram serves for both.",
        "fr": "Lu de haut en bas, l'arbre décrit une descente : de l'indéterminé au déterminé, "
              "de l'idée à l'objet, de l'impulsion au fait. Lu de bas en haut, il décrit le "
              "chemin inverse, celui que parcourt l'opérant. Les deux sens comptent et le "
              "diagramme sert aux deux."},

    "Los diez números": {"en": "The ten numbers", "fr": "Les dix nombres"},

    "1 · Kéter": {"en": "1 · Keter", "fr": "1 · Kéter"},
    "La corona. El impulso antes de tener forma.": {
        "en": "Crown. The impulse before it has form.",
        "fr": "La couronne. L'impulsion avant d'avoir une forme."},

    "2 · Jojmá": {"en": "2 · Chokhmah", "fr": "2 · Hokhmah"},
    "La sabiduría. La chispa que aún no se ha delimitado.": {
        "en": "Wisdom. The spark that has not yet been bounded.",
        "fr": "La sagesse. L'étincelle qui n'est pas encore délimitée."},

    "3 · Biná": {"en": "3 · Binah", "fr": "3 · Binah"},
    "La inteligencia. La forma que delimita la chispa.": {
        "en": "Understanding. The form that bounds the spark.",
        "fr": "L'intelligence. La forme qui délimite l'étincelle."},
}
