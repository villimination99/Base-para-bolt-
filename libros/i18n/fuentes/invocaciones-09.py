# -*- coding: utf-8 -*-
"""
CÓDICE DE LAS INVOCACIONES · cierre del árbol y los cuadrados planetarios
=========================================================================
La regla práctica del árbol —toda operación empieza en Maljut y si el
resultado no vuelve a Maljut la operación no ha ocurrido— es la mejor defensa
del libro contra la espiritualidad de salón, y así se llama en las tres
lenguas. La expresión es despectiva a propósito y se traduce por la despectiva
equivalente, no por una neutra.

Las descripciones de los cuadrados llevan sus tres cifras: el lado, el rango
de números y la suma constante. Son las que el lector va a comprobar con un
lápiz, que es lo que el capítulo le invita a hacer.
"""

T = {
    "4 · Jésed": {"en": "4 · Chesed", "fr": "4 · Hésed"},
    "La clemencia. Lo que se da y se expande.": {
        "en": "Mercy. What is given and what expands.",
        "fr": "La clémence. Ce qui se donne et s'étend."},

    "5 · Guevurá": {"en": "5 · Gevurah", "fr": "5 · Guevourah"},
    "El rigor. Lo que se recorta y se pone en su sitio.": {
        "en": "Severity. What is cut back and put in its place.",
        "fr": "La rigueur. Ce qui se retranche et se remet à sa place."},

    "6 · Tiféret": {"en": "6 · Tiferet", "fr": "6 · Tiphéret"},
    "La belleza. El equilibrio de los dos anteriores; el centro del árbol y el lugar del "
    "operante consciente.": {
        "en": "Beauty. The balance of the two before it; the centre of the tree and the place "
              "of the conscious operator.",
        "fr": "La beauté. L'équilibre des deux précédentes ; le centre de l'arbre et la place "
              "de l'opérant conscient."},

    "7 · Nétsaj": {"en": "7 · Netzach", "fr": "7 · Netsah"},
    "La victoria. Lo que persiste, el impulso sostenido.": {
        "en": "Victory. What persists, the sustained impulse.",
        "fr": "La victoire. Ce qui persiste, l'impulsion soutenue."},

    "8 · Hod": {"en": "8 · Hod", "fr": "8 · Hod"},
    "La gloria. La forma acabada, el detalle, el estilo.": {
        "en": "Splendour. The finished form, the detail, the style.",
        "fr": "La gloire. La forme achevée, le détail, le style."},

    "9 · Yesod": {"en": "9 · Yesod", "fr": "9 · Yesod"},
    "El fundamento. Donde todo lo anterior se reúne antes de concretarse. La imaginación.": {
        "en": "Foundation. Where everything above gathers before taking concrete shape. The "
              "imagination.",
        "fr": "Le fondement. Où tout ce qui précède se rassemble avant de se concrétiser. "
              "L'imagination."},

    "10 · Maljut": {"en": "10 · Malkuth", "fr": "10 · Malkhout"},
    "El reino. El cuerpo, el hecho, el mundo. Donde una operación se comprueba o no se "
    "comprueba.": {
        "en": "Kingdom. The body, the fact, the world. Where an operation is verified or is "
              "not verified.",
        "fr": "Le royaume. Le corps, le fait, le monde. Où une opération se vérifie ou ne se "
              "vérifie pas."},

    "Las tres columnas": {"en": "The three columns", "fr": "Les trois colonnes"},

    "La columna de la derecha expande, la de la izquierda limita y la del centro equilibra. "
    "Es la misma estructura que aparece en el pentagrama —voluntad frente a memoria, con la "
    "atención arriba— y en el hexagrama —Júpiter frente a Saturno, con el Sol en medio—. El "
    "sistema repite su figura básica en todas las escalas, y esa coherencia es lo que lo "
    "hace utilizable.": {
        "en": "The right-hand column expands, the left-hand one limits and the central one "
              "balances. It is the same structure that appears in the pentagram —will against "
              "memory, with attention above— and in the hexagram —Jupiter against Saturn, with "
              "the Sun in the middle. The system repeats its basic figure at every scale, and "
              "that coherence is what makes it usable.",
        "fr": "La colonne de droite étend, celle de gauche limite et celle du centre équilibre. "
              "C'est la même structure qui apparaît dans le pentagramme —la volonté face à la "
              "mémoire, avec l'attention en haut— et dans l'hexagramme —Jupiter face à Saturne, "
              "avec le Soleil au milieu. Le système répète sa figure de base à toutes les "
              "échelles, et cette cohérence est ce qui le rend utilisable."},

    "Cómo usar el árbol sin estudiar cábala diez años": {
        "en": "How to use the tree without studying kabbalah for ten years",
        "fr": "Comment se servir de l'arbre sans étudier la kabbale dix ans"},

    "Para operar basta con una cosa: saber que toda operación empieza en Maljut, el cuerpo y "
    "la habitación, y que si el resultado no vuelve a Maljut la operación no ha ocurrido. Es "
    "la mejor defensa contra la espiritualidad de salón. Si algo cambió, se nota en la vida "
    "concreta; si no se nota en ninguna parte, no cambió.": {
        "en": "To operate, one thing is enough: knowing that every operation begins in "
              "Malkuth, the body and the room, and that if the result does not come back to "
              "Malkuth the operation has not happened. It is the best defence against "
              "drawing-room spirituality. If something changed, it shows in concrete life; if "
              "it shows nowhere, it did not change.",
        "fr": "Pour opérer, une seule chose suffit : savoir que toute opération commence à "
              "Malkhout, le corps et la pièce, et que si le résultat ne revient pas à Malkhout "
              "l'opération n'a pas eu lieu. C'est la meilleure défense contre la spiritualité "
              "de salon. Si quelque chose a changé, cela se voit dans la vie concrète ; si cela "
              "ne se voit nulle part, rien n'a changé."},

    "Los veintidós senderos": {
        "en": "The twenty-two paths", "fr": "Les vingt-deux sentiers"},

    "Las veintidós líneas que unen los números llevan atribuidas tradicionalmente las "
    "veintidós letras del alfabeto hebreo y los veintidós arcanos mayores del tarot. Es un "
    "sistema de correspondencias vasto y bello, y queda fuera de este libro por una razón "
    "práctica: no hace falta para nada de lo que aquí se propone, y meterlo sin "
    "desarrollarlo sería decoración. Si sigues por tu cuenta, ese es el paso siguiente.": {
        "en": "The twenty-two lines joining the numbers traditionally carry the twenty-two "
              "letters of the Hebrew alphabet and the twenty-two major arcana of tarot "
              "attributed to them. It is a vast and beautiful system of correspondences, and "
              "it stays outside this book for a practical reason: it is not needed for "
              "anything proposed here, and putting it in without developing it would be "
              "decoration. If you carry on by yourself, that is the next step.",
        "fr": "Les vingt-deux lignes qui joignent les nombres portent traditionnellement les "
              "vingt-deux lettres de l'alphabet hébraïque et les vingt-deux arcanes majeurs du "
              "tarot. C'est un système de correspondances vaste et beau, et il reste hors de ce "
              "livre pour une raison pratique : il n'est nécessaire à rien de ce qui est "
              "proposé ici, et l'y mettre sans le développer serait de la décoration. Si vous "
              "continuez de votre côté, c'est l'étape suivante."},

    # ── Los cuadrados planetarios ──────────────────────────────────────────
    "Cada planeta lleva asociado un cuadrado de números en el que todas las filas, todas las "
    "columnas y las dos diagonales suman exactamente lo mismo. Son los kameas, aparecen en "
    "Agrippa y en los grimorios posteriores, y tienen la particularidad de ser la única "
    "pieza de este libro que se puede verificar con un lápiz.": {
        "en": "Each planet has associated with it a square of numbers in which every row, "
              "every column and the two diagonals add up to exactly the same. These are the "
              "kameas, they appear in Agrippa and in the later grimoires, and they have the "
              "peculiarity of being the only piece in this book that can be verified with a "
              "pencil.",
        "fr": "Chaque planète a un carré de nombres associé où toutes les lignes, toutes les "
              "colonnes et les deux diagonales font exactement le même total. Ce sont les "
              "kameas, ils apparaissent chez Agrippa et dans les grimoires postérieurs, et ils "
              "ont la particularité d'être la seule pièce de ce livre que l'on puisse vérifier "
              "avec un crayon."},

    '<span class="fig-n">Lám. 6</span> Los cuatro primeros cuadrados: Saturno de tres, '
    "Júpiter de cuatro, Marte de cinco y el Sol de seis. Cada uno con su suma constante. Los "
    "de Venus, Mercurio y la Luna siguen la misma lógica en siete, ocho y nueve.": {
        "en": '<span class="fig-n">Pl. 6</span> The first four squares: Saturn of three, '
              "Jupiter of four, Mars of five and the Sun of six. Each with its constant sum. "
              "Those of Venus, Mercury and the Moon follow the same logic in seven, eight and "
              "nine.",
        "fr": '<span class="fig-n">Pl. 6</span> Les quatre premiers carrés : Saturne de trois, '
              "Jupiter de quatre, Mars de cinq et le Soleil de six. Chacun avec sa somme "
              "constante. Ceux de Vénus, Mercure et la Lune suivent la même logique en sept, "
              "huit et neuf."},

    "Los siete cuadrados": {"en": "The seven squares", "fr": "Les sept carrés"},

    "3×3 · números del 1 al 9 · suma constante 15": {
        "en": "3×3 · numbers 1 to 9 · constant sum 15",
        "fr": "3×3 · nombres de 1 à 9 · somme constante 15"},
    "4×4 · del 1 al 16 · suma 34": {
        "en": "4×4 · 1 to 16 · sum 34", "fr": "4×4 · de 1 à 16 · somme 34"},
    "5×5 · del 1 al 25 · suma 65": {
        "en": "5×5 · 1 to 25 · sum 65", "fr": "5×5 · de 1 à 25 · somme 65"},
}
