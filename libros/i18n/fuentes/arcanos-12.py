# -*- coding: utf-8 -*-
"""
CÓDICE DE LOS ARCANOS · la regla de los decanatos y cómo se lee de verdad
=========================================================================
Los nombres de los signos y de los planetas ya tienen traducción en el
catálogo, puesta desde el libro del zodiaco, así que el sistema los comparte
en vez de duplicarlos. Lo que sí se traduce aquí es lo que los rodea: los
grados —0° a 10°—, las modalidades y el orden caldeo, que conserva su nombre
en las tres lenguas porque es el nombre de una secuencia concreta y no una
descripción.

El ejemplo de Aries se traduce con sus tres regentes en el mismo orden. Es una
demostración paso a paso y el lector la sigue con el dedo; reordenarla la
volvería incomprobable.
"""

T = {
    "La regla, que es lo bonito del asunto": {
        "en": "The rule, which is the beautiful part",
        "fr": "La règle, qui est le beau de l'affaire"},

    "El reparto no hay que memorizarlo porque se deduce con dos criterios.": {
        "en": "The distribution does not have to be memorised because it is deduced from two "
              "criteria.",
        "fr": "La répartition n'a pas à être mémorisée parce qu'elle se déduit de deux "
              "critères."},

    "El palo lo da el elemento del signo. Aries es Fuego, así que sus tres decanatos son de "
    "Bastos. Tauro es Tierra: Oros. Y así los doce.": {
        "en": "The suit comes from the element of the sign. Aries is Fire, so its three decans "
              "are Wands. Taurus is Earth: Pentacles. And so on for all twelve.",
        "fr": "La couleur vient de l'élément du signe. Le Bélier est Feu, donc ses trois décans "
              "sont de Bâtons. Le Taureau est Terre : Deniers. Et ainsi des douze."},

    "El trío de números lo da la modalidad. Los signos cardinales toman el dos, el tres y "
    "el cuatro; los fijos el cinco, el seis y el siete; los mutables el ocho, el nueve y el "
    "diez.": {
        "en": "The trio of numbers comes from the mode. Cardinal signs take the two, the three "
              "and the four; fixed signs the five, the six and the seven; mutable signs the "
              "eight, the nine and the ten.",
        "fr": "Le trio de nombres vient de la modalité. Les signes cardinaux prennent le deux, "
              "le trois et le quatre ; les fixes le cinq, le six et le sept ; les mutables le "
              "huit, le neuf et le dix."},

    "Dentro del signo, el primer decanato va al primer número del trío, el segundo al "
    "segundo y el tercero al tercero.": {
        "en": "Within the sign, the first decan goes to the first number of the trio, the "
              "second to the second and the third to the third.",
        "fr": "Dans le signe, le premier décan va au premier nombre du trio, le deuxième au "
              "deuxième et le troisième au troisième."},

    "Y el regente de cada decanato sale del orden caldeo empezando en Marte, que es el "
    "reparto clásico y el que cierra sin dejar huecos.": {
        "en": "And the ruler of each decan comes from the Chaldean order beginning at Mars, "
              "which is the classical distribution and the one that closes without leaving "
              "gaps.",
        "fr": "Et le régent de chaque décan vient de l'ordre chaldéen à partir de Mars, qui est "
              "la répartition classique et celle qui boucle sans laisser de trous."},

    "Un ejemplo entero": {"en": "A complete example", "fr": "Un exemple entier"},

    "Fuego cardinal → Bastos, trío 2-3-4": {
        "en": "Cardinal fire → Wands, trio 2-3-4",
        "fr": "Feu cardinal → Bâtons, trio 2-3-4"},
    "Aries 0° a 10° · regente Marte · el impulso sin filtro": {
        "en": "Aries 0° to 10° · ruler Mars · the impulse with no filter",
        "fr": "Bélier 0° à 10° · régent Mars · l'impulsion sans filtre"},
    "Aries 10° a 20° · regente Sol · el impulso con dirección": {
        "en": "Aries 10° to 20° · ruler Sun · the impulse with direction",
        "fr": "Bélier 10° à 20° · régent Soleil · l'impulsion avec une direction"},
    "Aries 20° a 30° · regente Venus · el impulso que busca compañía": {
        "en": "Aries 20° to 30° · ruler Venus · the impulse that seeks company",
        "fr": "Bélier 20° à 30° · régent Vénus · l'impulsion qui cherche de la compagnie"},

    "Por qué esto cierra sin sobrar nada": {
        "en": "Why this closes with nothing left over",
        "fr": "Pourquoi cela boucle sans rien laisser"},

    "Cuatro elementos por tres modalidades son doce signos, y ninguna casilla se repite. "
    "Doce signos por tres decanatos son treinta y seis. Cuatro palos por nueve números —del "
    "dos al diez— son también treinta y seis. Las dos rejillas tienen el mismo tamaño y "
    "encajan una en otra sin hueco. Que encajen no es una casualidad afortunada: es que "
    "quien montó el sistema en el siglo XIX contó primero.": {
        "en": "Four elements times three modes are twelve signs, and no cell repeats. Twelve "
              "signs times three decans are thirty-six. Four suits times nine numbers —from "
              "two to ten— are thirty-six as well. The two grids are the same size and fit "
              "into each other without a gap. That they fit is not a fortunate coincidence: it "
              "is that whoever assembled the system in the nineteenth century counted first.",
        "fr": "Quatre éléments par trois modalités font douze signes, et aucune case ne se "
              "répète. Douze signes par trois décans font trente-six. Quatre couleurs par neuf "
              "nombres —du deux au dix— font aussi trente-six. Les deux grilles ont la même "
              "taille et s'emboîtent sans trou. Qu'elles s'emboîtent n'est pas une heureuse "
              "coïncidence : c'est que celui qui a monté le système au XIXe siècle a compté "
              "d'abord."},

    "Qué se gana leyendo así": {
        "en": "What is gained by reading this way",
        "fr": "Ce qu'on gagne à lire ainsi"},

    "Precisión, y un puente. El seis de Copas dejará de ser «nostalgia» —que es lo que "
    "dicen la mayoría de los manuales— y será Escorpio en su segundo decanato, regido por "
    "el Sol: la intensidad con propósito. Es una lectura más específica, más difícil de "
    "estirar a conveniencia y con una tabla detrás que se puede comprobar.": {
        "en": "Precision, and a bridge. The six of Cups will stop being «nostalgia» —which is "
              "what most manuals say— and will be Scorpio in its second decan, ruled by the "
              "Sun: intensity with a purpose. It is a more specific reading, harder to stretch "
              "to suit, and with a table behind it that can be checked.",
        "fr": "De la précision, et un pont. Le six de Coupes cessera d'être « la nostalgie » "
              "—ce que disent la plupart des manuels— et sera le Scorpion à son deuxième "
              "décan, régi par le Soleil : l'intensité avec un but. C'est une lecture plus "
              "spécifique, plus difficile à étirer à sa convenance, et avec une table derrière "
              "qu'on peut vérifier."},

    "Y el puente funciona en los dos sentidos. Si trabajas también con astrología, cada "
    "decanato tiene ahora una carta que lo representa; si trabajas con el tarot, cada carta "
    "menor tiene ahora treinta grados de zodiaco y un planeta regente detrás. Los dos "
    "libros se leen mejor juntos, y eso es deliberado.": {
        "en": "And the bridge works both ways. If you also work with astrology, each decan now "
              "has a card that represents it; if you work with tarot, each minor card now has "
              "thirty degrees of zodiac and a ruling planet behind it. The two subjects read "
              "better together, and that is deliberate.",
        "fr": "Et le pont fonctionne dans les deux sens. Si vous travaillez aussi avec "
              "l'astrologie, chaque décan a désormais une carte qui le représente ; si vous "
              "travaillez avec le tarot, chaque carte mineure a désormais trente degrés de "
              "zodiaque et une planète régente derrière elle. Les deux se lisent mieux "
              "ensemble, et c'est délibéré."},

    "Esta correspondencia es una construcción del siglo XIX, elegante y coherente, y no la "
    "revelación de un vínculo real entre unos cartones y unos grados de cielo. Su valor es "
    "el de cualquier buen sistema de clasificación: da a cada elemento un lugar único y "
    "permite razonar. Con eso basta y es mucho.": {
        "en": "This correspondence is a nineteenth-century construction, elegant and coherent, "
              "and not the revelation of a real link between pieces of card and degrees of "
              "sky. Its value is that of any good classification system: it gives each element "
              "a unique place and makes reasoning possible. That is enough, and it is a great "
              "deal.",
        "fr": "Cette correspondance est une construction du XIXe siècle, élégante et cohérente, "
              "et non la révélation d'un lien réel entre des cartons et des degrés de ciel. Sa "
              "valeur est celle de n'importe quel bon système de classement : elle donne à "
              "chaque élément une place unique et permet de raisonner. Cela suffit, et c'est "
              "beaucoup."},

    # ── Cómo se lee de verdad ──────────────────────────────────────────────
    "El capítulo que la mayoría de los manuales se salta, porque explica el mecanismo y "
    "explicarlo parece quitarle magia. Ocurre lo contrario: entendido el mecanismo, la "
    "lectura mejora mucho.": {
        "en": "The chapter most manuals skip, because it explains the mechanism and explaining "
              "it looks like taking the magic away. The opposite happens: once the mechanism "
              "is understood, the reading improves a great deal.",
        "fr": "Le chapitre que la plupart des manuels sautent, parce qu'il explique le "
              "mécanisme et que l'expliquer semble lui ôter sa magie. C'est l'inverse qui se "
              "produit : le mécanisme compris, la lecture s'améliore beaucoup."},

    "Lo que pasa en una tirada": {
        "en": "What happens in a spread", "fr": "Ce qui se passe dans un tirage"},

    "Se formula una pregunta. El solo hecho de tener que formularla ya obliga a concretar "
    "un asunto que estaba difuso, y una parte del rendimiento de la tirada se produce aquí, "
    "antes de tocar el mazo.": {
        "en": "A question is formulated. The mere fact of having to formulate it already "
              "forces a blurred matter into focus, and part of the spread's yield is produced "
              "here, before the deck is touched.",
        "fr": "On formule une question. Le seul fait d'avoir à la formuler oblige déjà à "
              "préciser une affaire qui était floue, et une part du rendement du tirage se "
              "produit ici, avant de toucher le jeu."},

    "Se saca un número fijo de cartas en posiciones con significado asignado. El azar "
    "aporta las figuras; la estructura de la tirada aporta el papel de cada una.": {
        "en": "A fixed number of cards is drawn into positions with assigned meanings. Chance "
              "supplies the figures; the structure of the spread supplies the role of each one.",
        "fr": "On tire un nombre fixe de cartes dans des positions au sens assigné. Le hasard "
              "apporte les figures ; la structure du tirage apporte le rôle de chacune."},

    "Se mira lo que sale y se busca cómo encaja. Este es el paso donde ocurre el trabajo: "
    "la mente proyecta la situación sobre la figura y, al hacerlo, articula lo que sabía y "
    "no había dicho.": {
        "en": "You look at what comes up and search for how it fits. This is the step where "
              "the work happens: the mind projects the situation onto the figure and, in doing "
              "so, articulates what it knew and had not said.",
        "fr": "On regarde ce qui sort et on cherche comment cela s'ajuste. C'est l'étape où le "
              "travail se fait : l'esprit projette la situation sur la figure et, ce faisant, "
              "articule ce qu'il savait et n'avait pas dit."},

    "Se dice en voz alta o se escribe. Sin este paso la tirada se disuelve: lo que no se "
    "formula no queda.": {
        "en": "You say it out loud or write it down. Without this step the spread dissolves: "
              "what is not formulated does not stay.",
        "fr": "On le dit à voix haute ou on l'écrit. Sans cette étape le tirage se dissout : ce "
              "qui n'est pas formulé ne reste pas."},

    "Por qué el azar es imprescindible": {
        "en": "Why chance is indispensable", "fr": "Pourquoi le hasard est indispensable"},

    "Porque el valor del instrumento está en que te ponga delante figuras que no habrías "
    "elegido. Si eligieras las cartas, elegirías las que confirman lo que ya piensas — y no "
    "habría tirada, habría un espejo. El azar es lo que garantiza la incomodidad, y la "
    "incomodidad es lo que produce el hallazgo.": {
        "en": "Because the instrument's value lies in putting figures in front of you that you "
              "would not have chosen. If you chose the cards, you would choose the ones that "
              "confirm what you already think — and there would be no spread, there would be a "
              "mirror. Chance is what guarantees the discomfort, and the discomfort is what "
              "produces the finding.",
        "fr": "Parce que la valeur de l'instrument tient à ce qu'il vous mette devant des "
              "figures que vous n'auriez pas choisies. Si vous choisissiez les cartes, vous "
              "choisiriez celles qui confirment ce que vous pensez déjà — et il n'y aurait pas "
              "de tirage, il y aurait un miroir. Le hasard est ce qui garantit l'inconfort, et "
              "l'inconfort est ce qui produit la trouvaille."},

    "La objeción obvia, respondida": {
        "en": "The obvious objection, answered",
        "fr": "L'objection évidente, à laquelle il est répondu"},
}
