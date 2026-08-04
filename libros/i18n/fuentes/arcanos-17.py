# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · vocabulario y cierre
============================================
La cifra de la gematría —1 495, la suma de los valores de las veintidós
letras— es una de las que el generador comprueba antes de escribir, así que se
copia sin tocar y solo cambia el separador de millares: espacio fino en
español y en francés, coma en inglés.

«Cartomancia» aparece en el glosario para distinguirla de lo que el libro
enseña, no como sinónimo. En los tres idiomas mantiene su forma técnica y su
aclaración detrás.
"""

T = {
    "Arcano": {"en": "Arcanum", "fr": "Arcane"},
    "Cada una de las setenta y ocho cartas. Mayor si pertenece a la serie de veintidós; "
    "menor si pertenece a un palo.": {
        "en": "Each of the seventy-eight cards. Major if it belongs to the series of "
              "twenty-two; minor if it belongs to a suit.",
        "fr": "Chacune des soixante-dix-huit cartes. Majeur s'il appartient à la série des "
              "vingt-deux ; mineur s'il appartient à une couleur."},

    "As": {"en": "Ace", "fr": "As"},
    "La primera carta de cada palo. No es el número uno: es el elemento puro, antes de "
    "forma.": {
        "en": "The first card of each suit. It is not the number one: it is the pure element, "
              "before form.",
        "fr": "La première carte de chaque couleur. Ce n'est pas le nombre un : c'est l'élément "
              "pur, avant la forme."},

    "Cartomancia": {"en": "Cartomancy", "fr": "Cartomancie"},
    "Lectura de cartas con fines de adivinación. Se nombra aquí para distinguirla: no es lo "
    "que este libro enseña.": {
        "en": "Card reading for purposes of divination. It is named here in order to "
              "distinguish it: it is not what this book teaches.",
        "fr": "Lecture des cartes à des fins divinatoires. Elle est nommée ici pour la "
              "distinguer : ce n'est pas ce qu'enseigne ce livre."},

    "Tramo de diez grados de un signo. Hay treinta y seis, y a cada uno le corresponde una "
    "carta del dos al diez.": {
        "en": "A stretch of ten degrees of a sign. There are thirty-six, and each one "
              "corresponds to a card from two to ten.",
        "fr": "Tronçon de dix degrés d'un signe. Il y en a trente-six, et à chacun correspond "
              "une carte du deux au dix."},

    "Escala del número": {"en": "Scale of number", "fr": "Échelle du nombre"},
    "La secuencia de significados del dos al diez, común a los cuatro palos.": {
        "en": "The sequence of meanings from two to ten, common to all four suits.",
        "fr": "La séquence de significations du deux au dix, commune aux quatre couleurs."},

    "Figura": {"en": "Court card", "fr": "Figure"},
    "Sota, Caballo, Reina o Rey. Cuatro por palo, dieciséis en total.": {
        "en": "Page, Knight, Queen or King. Four per suit, sixteen in all.",
        "fr": "Valet, Cavalier, Reine ou Roi. Quatre par couleur, seize en tout."},

    "Gematría": {"en": "Gematria", "fr": "Guématrie"},
    "Suma de los valores numéricos de las letras de una palabra. Las veintidós letras suman "
    "1 495 entre todas, y esa cifra se comprueba en este libro.": {
        "en": "The sum of the numerical values of the letters of a word. The twenty-two "
              "letters add up to 1,495 between them, and that figure is checked in this book.",
        "fr": "Somme des valeurs numériques des lettres d'un mot. Les vingt-deux lettres font "
              "1 495 à elles toutes, et ce chiffre est vérifié dans ce livre."},

    "Inversión": {"en": "Reversal", "fr": "Inversion"},
    "Carta que sale del revés. Se lee como exceso, defecto, bloqueo o interioridad — "
    "elegido de antemano.": {
        "en": "A card that comes up the wrong way round. It is read as excess, deficiency, "
              "blockage or inwardness — chosen in advance.",
        "fr": "Carte qui sort à l'envers. Elle se lit comme excès, défaut, blocage ou "
              "intériorité — choisi d'avance."},

    "Marsella": {"en": "Marseille", "fr": "Marseille"},
    "Patrón de grabados francés estabilizado entre el XVII y el XVIII. El que este libro "
    "sigue. Justicia en el VIII, Fuerza en el XI.": {
        "en": "The French engraving pattern settled between the seventeenth and eighteenth "
              "centuries. The one this book follows. Justice at VIII, Strength at XI.",
        "fr": "Patron de gravures français stabilisé entre le XVIIe et le XVIIIe siècle. Celui "
              "que suit ce livre. Justice au VIII, Force au XI."},

    "Numeral": {"en": "Numeral", "fr": "Numérale"},
    "Carta del dos al diez de un palo. Hay treinta y seis.": {
        "en": "A card from two to ten of a suit. There are thirty-six.",
        "fr": "Carte du deux au dix d'une couleur. Il y en a trente-six."},

    "Palo": {"en": "Suit", "fr": "Couleur"},
    "Bastos, Copas, Espadas u Oros. Cada uno un elemento y un área de la vida.": {
        "en": "Wands, Cups, Swords or Pentacles. Each one an element and an area of life.",
        "fr": "Bâtons, Coupes, Épées ou Deniers. Chacune un élément et un domaine de la vie."},

    "Proyectivo": {"en": "Projective", "fr": "Projectif"},
    "Instrumento cuya utilidad consiste en que quien lo mira proyecte su propia situación "
    "sobre una imagen ambigua pero acotada. Es lo que el tarot es.": {
        "en": "An instrument whose usefulness consists in the viewer projecting their own "
              "situation onto an image that is ambiguous but bounded. It is what tarot is.",
        "fr": "Instrument dont l'utilité consiste en ce que celui qui le regarde projette sa "
              "propre situation sur une image ambiguë mais bornée. C'est ce qu'est le tarot."},

    "Regente del decanato": {
        "en": "Ruler of the decan", "fr": "Régent du décan"},
    "Planeta que rige un tramo de diez grados. Sale del orden caldeo empezando en Marte.": {
        "en": "The planet that rules a stretch of ten degrees. It comes from the Chaldean "
              "order beginning at Mars.",
        "fr": "Planète qui régit un tronçon de dix degrés. Elle vient de l'ordre chaldéen à "
              "partir de Mars."},

    "Reparto 3-7-12": {"en": "The 3-7-12 division", "fr": "Répartition 3-7-12"},
    "División de las veintidós letras en tres madres, siete dobles y doce simples. De él "
    "heredan los mayores su atribución.": {
        "en": "The division of the twenty-two letters into three mothers, seven doubles and "
              "twelve simples. It is from this that the majors inherit their attribution.",
        "fr": "Division des vingt-deux lettres en trois mères, sept doubles et douze simples. "
              "C'est d'elle que les majeurs héritent leur attribution."},

    "Disposición de un número fijo de cartas en posiciones con significado asignado.": {
        "en": "The layout of a fixed number of cards in positions with assigned meanings.",
        "fr": "Disposition d'un nombre fixe de cartes dans des positions au sens assigné."},

    "Triunfos": {"en": "Trumps", "fr": "Triomphes"},
    "Nombre original de los arcanos mayores en los mazos italianos del siglo XV. De ahí "
    "«tarocchi» y «tarot».": {
        "en": "The original name of the major arcana in the Italian decks of the fifteenth "
              "century. Hence «tarocchi» and «tarot».",
        "fr": "Nom d'origine des arcanes majeurs dans les jeux italiens du XVe siècle. De là "
              "« tarocchi » et « tarot »."},

    # ── Cierre ─────────────────────────────────────────────────────────────
    "Y con esto se cierra el libro. Setenta y ocho figuras, veintidós letras, treinta y "
    "seis decanatos, cuatro palos, tres tiradas y un cuaderno: un lenguaje entero para la "
    "misma tarea de siempre, que es mirarse con algo más de precisión de la que se tiene "
    "por defecto.": {
        "en": "And with that the book closes. Seventy-eight figures, twenty-two letters, "
              "thirty-six decans, four suits, three spreads and a notebook: a whole language "
              "for the same old task, which is looking at yourself with a little more "
              "precision than you have by default.",
        "fr": "Et sur cela le livre se referme. Soixante-dix-huit figures, vingt-deux lettres, "
              "trente-six décans, quatre couleurs, trois tirages et un carnet : une langue "
              "entière pour la même tâche de toujours, qui est de se regarder avec un peu plus "
              "de précision qu'on n'en a par défaut."},

    "No promete nada, y eso es a propósito. Lo que ofrece es estructura donde había "
    "intuición, y un cuaderno para comprobar si la estructura sirve. Con eso, quien "
    "practique de verdad averiguará cosas sobre sí mismo que no sabía. Y quien no practique "
    "tendrá un libro bonito, que también es un destino digno pero es otro.": {
        "en": "It promises nothing, and that is on purpose. What it offers is structure where "
              "there was intuition, and a notebook for checking whether the structure works. "
              "With that, anyone who really practises will find out things about themselves "
              "they did not know. And anyone who does not practise will have a handsome book, "
              "which is also a worthy fate but a different one.",
        "fr": "Il ne promet rien, et c'est exprès. Ce qu'il offre, c'est de la structure là où "
              "il y avait de l'intuition, et un carnet pour vérifier si la structure sert. "
              "Avec cela, qui pratique vraiment découvrira sur lui-même des choses qu'il ne "
              "savait pas. Et qui ne pratique pas aura un beau livre, ce qui est aussi un sort "
              "digne mais un autre."},
}
