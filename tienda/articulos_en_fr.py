#!/usr/bin/env python3
"""
VILLUMINATIONS — El Diario en inglés y en francés
==================================================
La tienda vende en Canadá y todo el Diario estaba en castellano. Nueve
artículos escritos para interceptar la pregunta que la gente teclea, y la
gente que compra aquí la teclea en inglés y en francés.

    python3 tienda/articulos_en_fr.py

Este fichero tiene el mismo papel que `cuerpos_en_fr.py`: guarda el texto
traducido como **datos**, para que `blog.py` lo mande sin que pase por un
teclado. Es la misma razón por la que existe `traducir.py`; el «veintivún» de
aquella vez costó cotejar ocho artículos carácter a carácter.

Se traduce **lo que está escrito aquí**, no la fuente original. Las cifras
salen de organismos del Gobierno de EE. UU. y se pueden comprobar una por una;
la redacción es propia y se traduce como tal.

Las dos bases legales siguen sin mezclarse
------------------------------------------
`_fuentes()` del castellano exige `base="federal"` o `base="tradicion"` porque
una vez firmó el artículo del decanato con el 17 U.S.C. § 105, que no le
tocaba. Aquí pasa igual: `CIERRE` tiene las dos entradas en las dos lenguas y
ningún valor por defecto.

Los dos enlaces que aquí no se escriben a ojo
---------------------------------------------
**Las colecciones.** El castellano remata con un enlace a
`/collections/suplementos`. Los handles de las seis están traducidos en la
tienda, pero **cuál es el handle traducido no consta en el repositorio**, y
escribir un enlace a ojo es escribir un 404. `COLECCION` los deja en `None` y
la frase sale sin enlace; el informe los enumera para rellenarlos cuando se
pueda preguntar a la tienda.

**Los artículos entre sí.** Un artículo inglés puede citar a otro que todavía
solo existe en castellano. Con el prefijo `/en/` delante, ese enlace es un 404.
`_descolgar()` lo resuelve al componer: si el destino no está traducido, cae el
ancla y queda el texto. No hay que acordarse de nada, y el día que el destino
se traduzca el enlace vuelve solo.

Un enlace inventado es peor que ninguno, y uno que hay que mantener a mano
acaba siendo inventado.

Cobertura
---------
Va por artículos: `lecturas.disponibles()` pregunta cuáles están y solo esos
salen enlazados desde las fichas. Un artículo a medio traducir no existe para
el resto del sistema, así que esto se puede llenar poco a poco sin publicar
nada roto.
"""

import re

TOPE_TITULO = 60
TOPE_DESCRIPCION = 155

LENGUAS = ("en", "fr")

FIRMA = {
    "en": ('<p><em>Published by VILLUMINATIONS. This text is informational '
           'and does not replace the care of a licensed health '
           'professional.</em></p>'),
    "fr": ('<p><em>Publié par VILLUMINATIONS. Ce texte est informatif et ne '
           'remplace pas le suivi d\'un professionnel de santé '
           'agréé.</em></p>'),
}

# Las dos bases legales, en las dos lenguas. Sin valor por defecto: se elige.
CIERRE = {
    "en": {
        "federal": (
            "<p>United States Government agencies publish in the open and "
            "their works are <strong>not subject to copyright under "
            "17 U.S.C. § 105</strong>. Every figure can be checked one by "
            "one; the writing of this article is our own work.</p>\n"),
        "tradicion": (
            "<p>This article does not rest on official sources but on "
            "<strong>common tradition and the public domain</strong>: "
            "material handed down in writing for centuries and belonging to "
            "no one. The writing, the selection and the order are our own "
            "work.</p>\n"),
    },
    "fr": {
        "federal": (
            "<p>Les organismes du Gouvernement des États-Unis publient en "
            "libre accès et leurs œuvres <strong>ne sont pas soumises au "
            "droit d'auteur en vertu du 17 U.S.C. § 105</strong>. Chaque "
            "chiffre peut être vérifié un par un ; la rédaction de cet "
            "article est un travail propre.</p>\n"),
        "tradicion": (
            "<p>Cet article ne s'appuie pas sur des sources officielles mais "
            "sur la <strong>tradition commune et le domaine public</strong> : "
            "une matière transmise par écrit depuis des siècles et qui "
            "n'appartient à personne. La rédaction, la sélection et l'ordre "
            "sont un travail propre.</p>\n"),
    },
}

TITULO_FUENTES = {
    "en": {"federal": "Where each figure comes from",
           "tradicion": "Where all this comes from"},
    "fr": {"federal": "D'où vient chaque chiffre",
           "tradicion": "D'où vient ce qui est raconté ici"},
}

ETIQUETA = {
    "en": ('<p><strong>This is a summary.</strong> {frase} It is in '
           '<a href="/en/products/{handle}">{libro}</a>, a {paginas}-page PDF '
           'in Spanish, English and French.</p>'),
    "fr": ('<p><strong>Ceci est un résumé.</strong> {frase} Cela se trouve '
           'dans <a href="/fr/products/{handle}">{libro}</a>, un PDF de '
           '{paginas} pages en espagnol, anglais et français.</p>'),
}

LIBRO = {
    "codice-de-la-mesa": {"en": "the Codex of the Table",
                          "fr": "le Codex de la Table", "paginas": 78},
    "codice-de-la-carga": {"en": "the Codex of the Load",
                           "fr": "le Codex de la Charge", "paginas": 74},
    "codice-del-descanso": {"en": "the Codex of Rest",
                            "fr": "le Codex du Repos", "paginas": 71},
    "codice-zodiacal": {"en": "the Zodiacal Codex",
                        "fr": "le Codex Zodiacal", "paginas": 96},
    "codice-de-los-arcanos": {"en": "the Codex of the Arcana",
                              "fr": "le Codex des Arcanes", "paginas": 82},
}

# Handle traducido de cada colección en la tienda. No consta en el
# repositorio: hasta que se pueda preguntar, la frase sale sin enlace.
COLECCION = {
    "suplementos": {"en": None, "fr": None},
    "equipo": {"en": None, "fr": None},
}


def fuentes(filas: str, lengua: str, base: str) -> str:
    if base not in CIERRE[lengua]:
        raise ValueError(f"base legal desconocida: {base}")
    return (f"<h3>{TITULO_FUENTES[lengua][base]}</h3>\n"
            "<ul>\n" + filas + "</ul>\n" + CIERRE[lengua][base])


def etiqueta(handle: str, lengua: str, frase: str) -> str:
    libro = LIBRO[handle]
    return ETIQUETA[lengua].format(frase=frase, handle=handle,
                                   libro=libro[lengua],
                                   paginas=libro["paginas"])


# ---------------------------------------------------------------------------
# Los artículos
# ---------------------------------------------------------------------------
# handle -> lengua -> {titulo, resumen, meta, cuerpo}
CUERPOS = {}

CUERPOS["cuanta-proteina-hace-falta-al-dia"] = {
    "en": {
        "titulo": "How much protein you need a day",
        "resumen": (
            "The official figure, why it is a floor and not a target, how to "
            "work it out from your body weight, and what actually happens if "
            "you go over."),
        "meta": (
            "How much protein you need a day | VILLUMINATIONS",
            "0.8 g per kilo is the official minimum, not the target for "
            "someone who trains. How to work it out, and what happens if you "
            "go over."),
        "cuerpo": """
<p>It is the most-typed question in nutrition and the worst answered, because
two different figures are in circulation and almost nobody explains that they
answer different questions.</p>

<h2>The official figure: 0.8 g per kilo</h2>

<p>The public recommendation for a healthy adult is <strong>0.8 grams of
protein per kilo of body weight per day</strong>. For seventy kilos that is 56
grams. The federal dietary guidance repeats it, and the label panel uses a
daily value of <strong>50 grams</strong> as its reference.</p>

<p>What almost nobody says is what that figure means. It is not an optimum: it
is the amount that covers the needs of <strong>almost the whole</strong>
healthy population. It is a floor, set so that nobody falls short — not a
ceiling and not a goal. Mistaking the floor for the target is the error every
other one grows out of.</p>

<h2>The other range: for people who train</h2>

<p>When strength training is involved, sports nutrition reviews work with a
considerably higher range, between <strong>1.2 and 2.0 grams per kilo</strong>,
with the top of it reserved for calorie deficits, where protein protects lean
mass while the weight comes down.</p>

<p>It is worth saying where each thing comes from: the 0.8 g/kg is a public
recommendation from federal agencies; the 1.2 to 2.0 range comes from the
sports nutrition literature and from professional society position stands. They
are two different sources and they are not cited as if they were one.</p>

<h2>The 10 to 35 % band</h2>

<p>There is a third way of looking at it, by percentage of calories. The
acceptable range for protein in an adult diet runs from <strong>10 to 35 % of
total calories</strong>. It is deliberately wide: inside that band there are
many correct diets, very different from one another.</p>

<p>It works as a cross-check. If you do the grams per kilo and the result falls
outside 35 % of your calories, something in the split does not add up.</p>

<h2>&laquo;You can only absorb 30 grams at a time&raquo;</h2>

<p>This gets repeated a lot and it is false as stated. The gut absorbs
practically all the protein that reaches it; what saturates is not absorption
but the <strong>muscle protein synthesis response</strong> to a single meal,
which tops out somewhere between twenty and forty grams depending on the person
and how much muscle they carry.</p>

<p>The practical consequence is not &laquo;never eat more than thirty&raquo;
but <strong>spread it out</strong>: three or four servings of protein across
the day do more than one enormous dinner.</p>

<h2>What happens if you go over</h2>

<p>In a person with healthy kidneys there is no public evidence of kidney
damage from eating more protein than recommended. What does happen is more
prosaic: protein is very filling, and every gram that comes in there is a gram
that does not come in somewhere else. Eating 3 g/kg is not dangerous, it is
simply <strong>unnecessary</strong>, and it crowds out the carbohydrate that
feeds the training.</p>

<p>Anyone with diagnosed kidney disease is in a different situation, and that
figure is set by their doctor, not by an article.</p>

<h2>How to work it out in thirty seconds</h2>

<ul>
  <li>Weight in kilos × 0.8 → the minimum for not falling short.</li>
  <li>Weight in kilos × 1.6 → a reasonable starting point if you train for
  strength.</li>
  <li>Divide the result by the number of meals you eat a day.</li>
</ul>

<p>At seventy kilos: 56 g as the floor, 112 g as the target while training,
about 28 g in each of four meals.</p>
""",
        "fuentes": (
            "<li>The 0.8 g/kg figure and the 10 to 35 % of calories range are "
            "recommendations published by United States Government "
            "agencies.</li>\n"
            "<li>The 50 g daily value is the one set by the labelling "
            "regulation for the nutrition panel.</li>\n"
            "<li>The 1.2 to 2.0 g/kg range comes from the sports nutrition "
            "literature, not from a federal recommendation, and the text says "
            "so.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("The split across meals, the tables of protein content by "
                  "food and how protein fits into the rest of the day are "
                  "worked through in full."),
    },
    "fr": {
        "titulo": "Combien de protéines par jour",
        "resumen": (
            "Le chiffre officiel, pourquoi c'est un plancher et non un "
            "objectif, comment le calculer avec son poids et ce qui se passe "
            "vraiment si l'on dépasse."),
        "meta": (
            "Combien de protéines par jour | VILLUMINATIONS",
            "0,8 g par kilo est le minimum officiel, pas l'objectif de qui "
            "s'entraîne. Comment le calculer et ce qui arrive si l'on "
            "dépasse."),
        "cuerpo": """
<p>C'est la question la plus tapée en nutrition et la plus mal répondue, parce
que deux chiffres différents circulent et que presque personne ne précise
qu'ils répondent à des questions différentes.</p>

<h2>Le chiffre officiel : 0,8 g par kilo</h2>

<p>La recommandation publique pour une personne adulte en bonne santé est de
<strong>0,8 gramme de protéines par kilo de poids corporel et par jour</strong>.
Pour soixante-dix kilos, cela fait 56 grammes. Le guide alimentaire fédéral le
répète et le panneau de l'étiquette utilise une valeur quotidienne de
<strong>50 grammes</strong> comme référence.</p>

<p>Ce que l'on ne dit presque jamais, c'est ce que ce chiffre signifie. Ce
n'est pas un optimum : c'est la quantité qui couvre les besoins de
<strong>presque toute</strong> la population en bonne santé. C'est un plancher
pensé pour que personne ne soit en dessous, pas un plafond ni un but. Confondre
le plancher avec l'objectif est l'erreur d'où viennent toutes les autres.</p>

<h2>L'autre fourchette : celle de qui s'entraîne</h2>

<p>Lorsqu'il y a de l'entraînement de force, les revues de nutrition sportive
travaillent avec une fourchette nettement plus haute, entre <strong>1,2 et
2,0 grammes par kilo</strong>, le haut étant réservé aux phases de déficit
calorique, où les protéines protègent la masse maigre pendant que le poids
descend.</p>

<p>Il convient de dire d'où vient chaque chose : les 0,8 g/kg sont une
recommandation publique d'organismes fédéraux ; la fourchette de 1,2 à 2,0
provient de la littérature de nutrition sportive et des prises de position de
sociétés professionnelles. Ce sont deux sources distinctes et elles ne sont pas
citées comme si elles n'en faisaient qu'une.</p>

<h2>La marge de 10 à 35 %</h2>

<p>Il y a une troisième façon de le regarder, en pourcentage de calories. La
fourchette acceptable pour les protéines dans un régime adulte va de
<strong>10 à 35 % des calories totales</strong>. Elle est large à dessein :
dans cette marge il y a beaucoup de régimes corrects et très différents les uns
des autres.</p>

<p>Cela sert de vérification croisée. Si vous faites les grammes par kilo et
que le résultat sort des 35 % de vos calories, quelque chose ne va pas dans la
répartition.</p>

<h2>&laquo; On n'absorbe que 30 grammes à la fois &raquo;</h2>

<p>Cela se répète beaucoup et c'est faux tel quel. L'intestin absorbe
pratiquement toutes les protéines qui lui parviennent ; ce qui sature n'est pas
l'absorption mais le <strong>stimulus de synthèse musculaire</strong> d'un seul
repas, qui atteint son plafond quelque part entre vingt et quarante grammes
selon la personne et la quantité de muscle qu'elle porte.</p>

<p>La conséquence pratique n'est pas &laquo; ne mangez pas plus de trente
&raquo; mais <strong>répartir</strong> : trois ou quatre prises de protéines
dans la journée valent mieux qu'un dîner énorme.</p>

<h2>Ce qui arrive si l'on dépasse</h2>

<p>Chez une personne aux reins sains, il n'existe pas de preuve publique d'une
atteinte rénale due à une consommation de protéines supérieure à la
recommandation. Ce qui arrive est plus prosaïque : les protéines rassasient
beaucoup, et chaque gramme qui entre par là est un gramme qui n'entre pas
ailleurs. Manger 3 g/kg n'est pas dangereux, c'est simplement
<strong>inutile</strong> et cela évince les glucides qui alimentent
l'entraînement.</p>

<p>Qui a une maladie rénale diagnostiquée est dans un autre cas de figure, et
ce chiffre est fixé par son médecin, pas par un article.</p>

<h2>Comment le calculer en trente secondes</h2>

<ul>
  <li>Poids en kilos × 0,8 → le minimum pour ne pas être en dessous.</li>
  <li>Poids en kilos × 1,6 → point de départ raisonnable si vous vous entraînez
  en force.</li>
  <li>Divisez le résultat par le nombre de repas que vous faites par jour.</li>
</ul>

<p>Avec soixante-dix kilos : 56 g de plancher, 112 g comme objectif à
l'entraînement, environ 28 g à chacun de quatre repas.</p>
""",
        "fuentes": (
            "<li>Les 0,8 g/kg et la fourchette de 10 à 35 % des calories sont "
            "des recommandations publiées par des organismes du Gouvernement "
            "des États-Unis.</li>\n"
            "<li>La valeur quotidienne de 50 g est celle que fixe la norme "
            "d'étiquetage pour le panneau nutritionnel.</li>\n"
            "<li>La fourchette de 1,2 à 2,0 g/kg provient de la littérature de "
            "nutrition sportive, non d'une recommandation fédérale, et le "
            "texte le dit.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("La répartition par repas, les tables de teneur en "
                  "protéines par aliment et la façon dont cela s'articule "
                  "avec le reste de la journée y sont développées en "
                  "entier."),
    },
}

CUERPOS["como-elegir-una-proteina-en-polvo"] = {
    "en": {
        "titulo": "How to choose a protein powder",
        "resumen": (
            "Concentrate, isolate or plant; what to read on the panel before "
            "the price on the tub, and the two label tricks that make you pay "
            "for less protein than you think."),
        "meta": (
            "How to choose a protein powder | VILLUMINATIONS",
            "Concentrate, isolate or plant, the cost per gram of protein and "
            "the two label tricks that make you pay for less than you "
            "think."),
        "cuerpo": """
<p>Almost everyone chooses their protein by the price on the tub, and the price
on the tub is the least informative figure on the label. Here are the four real
decisions, in the order in which they matter.</p>

<h2>1. Cost per gram of protein, not per tub</h2>

<p>It is the only honest comparison and it takes ten seconds: divide the price
by the total grams of protein in the container. The total is <em>servings per
container × grams of protein per serving</em>, and both figures are on the
panel.</p>

<p>Two tubs at the same price can hold twice as much protein one as the other,
because the weight of the container includes cocoa, flavourings, thickeners and
sugar. The scale weighs the powder; you are paying for the protein.</p>

<h2>2. Concentrate, isolate or plant</h2>

<p>The difference between the first two is how far the whey has been
filtered:</p>

<ul>
  <li><strong>Concentrate.</strong> Less filtered, so it carries a little more
  fat and lactose and a little less protein per gram of powder. It is the
  cheapest and, if lactose gives you no trouble, a perfectly reasonable
  choice.</li>
  <li><strong>Isolate.</strong> More filtered: more protein per gram and very
  little lactose. It costs more. It makes sense if concentrate does not sit
  well with you, or if you count macros precisely.</li>
  <li><strong>Plant.</strong> Pea, fava, rice or blends. The reason to choose
  it is not that it is &laquo;better&raquo;: it is that it carries no dairy.
  The essential amino acid profile should be complete, and blends manage that
  better than a single source.</li>
</ul>

<p>For almost everyone, the practical difference between the three is small
next to reaching the day's total protein, which is what actually moves the
needle.</p>

<h2>3. The two label tricks</h2>

<h3>The blend with no amounts</h3>

<p>If the label lists a &laquo;proprietary blend&raquo; of eight ingredients
with a single figure at the end, you cannot know how much of each there is.
That is exactly why it is presented that way. The rule is simple: <strong>if
you cannot compare two products with what the label says, the label is doing
its job and you cannot do yours</strong>.</p>

<h3>Padding with free amino acids</h3>

<p>The declared protein content is, in practice, calculated from nitrogen.
Cheap amino acids such as glycine or taurine contribute nitrogen without
contributing a complete protein, so adding them raises the figure on the panel
without raising what is useful to the muscle.</p>

<p>How to spot it: read the ingredient list. If free amino acids appear
<em>before</em> or just after the protein source, and the product is
conspicuously cheap per gram, be suspicious. An honest protein starts its list
with the protein.</p>

<h2>4. What should not weigh on the decision</h2>

<ul>
  <li><strong>The flavour in the photo.</strong> It changes between batches and
  says nothing about the contents.</li>
  <li><strong>&laquo;Sugar free&raquo;.</strong> It usually means sweetened
  with something else. Legitimate, but not a quality signal.</li>
  <li><strong>The promises on the tub.</strong> A food supplement goes through
  no prior authorisation before being sold, so what the tub promises has been
  validated by nobody. It is worked through in
  <a href="/en/blogs/diario/que-suplementos-tienen-evidencia">which supplements
  have evidence and which do not</a>.</li>
</ul>

<h2>The thirty-second check</h2>

<ol>
  <li>Grams of protein per serving ÷ grams of powder per serving. Above 0.7 is
  a dense product; below 0.6, you are buying a fair amount of filler.</li>
  <li>Price ÷ grams of protein in the container. That is the number that
  compares.</li>
  <li>First line of the ingredient list: is it the protein?</li>
  <li>Is there a &laquo;proprietary blend&raquo; with no amounts? If there is,
  next product.</li>
</ol>

<p>That rules out most of the market without reading a single review. The ones
in this shop declare grams per serving and the full ingredient list on the
product page, which is what you need to do this arithmetic.</p>
""",
        "fuentes": (
            "<li>The rules for the nutrition facts panel, the ingredient list "
            "in order of weight and the regime for food supplements —with no "
            "authorisation prior to sale— are published by the federal food "
            "and drug authority.</li>\n"
            "<li>Calculating protein from nitrogen is the analytical method "
            "set out in the labelling regulation itself.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("The split of protein across meals, the tables of content "
                  "by food and how it fits into the rest of the day are "
                  "worked through in full."),
    },
    "fr": {
        "titulo": "Comment choisir une protéine en poudre",
        "resumen": (
            "Concentré, isolat ou végétal ; ce qu'il faut lire sur le panneau "
            "avant le prix du pot, et les deux pièges d'étiquette qui font "
            "payer moins de protéines qu'on ne croit."),
        "meta": (
            "Comment choisir une protéine en poudre | VILLUMINATIONS",
            "Concentré, isolat ou végétal, le coût par gramme de protéines et "
            "les deux pièges d'étiquette qui font payer moins qu'on ne "
            "croit."),
        "cuerpo": """
<p>Presque tout le monde choisit sa protéine au prix du pot, et le prix du pot
est la donnée la moins informative de l'étiquette. Voici les quatre décisions
réelles, dans l'ordre où elles comptent.</p>

<h2>1. Le coût par gramme de protéines, pas par pot</h2>

<p>C'est la seule comparaison honnête et elle se fait en dix secondes : divisez
le prix par les grammes de protéines totaux de l'emballage. Le total, ce sont
<em>les prises par emballage × les grammes de protéines par prise</em>, et les
deux chiffres sont sur le panneau.</p>

<p>Deux pots au même prix peuvent contenir deux fois plus de protéines l'un que
l'autre, parce que le poids de l'emballage comprend cacao, arômes, épaississants
et sucre. La balance pèse la poudre ; vous payez la protéine.</p>

<h2>2. Concentré, isolat ou végétal</h2>

<p>La différence entre les deux premiers tient au degré de filtration du
lactosérum :</p>

<ul>
  <li><strong>Concentré.</strong> Moins filtré, donc un peu plus de gras et de
  lactose et un peu moins de protéines par gramme de poudre. C'est le moins
  cher et, si le lactose ne vous pose pas de problème, c'est un choix
  parfaitement raisonnable.</li>
  <li><strong>Isolat.</strong> Plus filtré : plus de protéines par gramme et
  très peu de lactose. Il coûte davantage. Il a du sens si le concentré passe
  mal ou si vous comptez les macros avec précision.</li>
  <li><strong>Végétal.</strong> Pois, féverole, riz ou mélanges. La raison de
  le choisir n'est pas qu'il soit &laquo; meilleur &raquo; : c'est qu'il ne
  contient pas de produits laitiers. Il vaut mieux que le profil d'acides
  aminés essentiels soit complet, et les mélanges y parviennent mieux qu'une
  source unique.</li>
</ul>

<p>Pour presque tout le monde, la différence pratique entre les trois est
petite à côté d'atteindre le total de protéines de la journée, qui est ce qui
change vraiment les choses.</p>

<h2>3. Les deux pièges de l'étiquette</h2>

<h3>Le mélange sans quantités</h3>

<p>Si l'étiquette annonce un &laquo; mélange breveté &raquo; de huit
ingrédients avec un seul chiffre à la fin, vous ne pouvez pas savoir combien il
y a de chacun. C'est exactement pour cela qu'il est présenté ainsi. La règle
est simple : <strong>si vous ne pouvez pas comparer deux produits avec ce que
dit l'étiquette, l'étiquette fait son travail et vous ne pouvez pas faire le
vôtre</strong>.</p>

<h3>Le remplissage aux acides aminés libres</h3>

<p>La quantité de protéines déclarée se calcule, en pratique, à partir de
l'azote. Des acides aminés bon marché comme la glycine ou la taurine apportent
de l'azote sans apporter une protéine complète : les ajouter fait monter le
chiffre du panneau sans faire monter ce qui sert au muscle.</p>

<p>Comment le repérer : regardez la liste des ingrédients. Si des acides aminés
libres apparaissent <em>avant</em> ou juste après la source protéique, et que
le produit est remarquablement bon marché au gramme, méfiez-vous. Une protéine
honnête commence sa liste par la protéine.</p>

<h2>4. Ce qui ne devrait pas peser dans la décision</h2>

<ul>
  <li><strong>Le parfum sur la photo.</strong> Il change d'un lot à l'autre et
  ne dit rien du contenu.</li>
  <li><strong>&laquo; Sans sucre &raquo;.</strong> Cela signifie en général
  édulcoré avec autre chose. Légitime, mais ce n'est pas une donnée de
  qualité.</li>
  <li><strong>Les promesses de l'emballage.</strong> Un complément alimentaire
  ne passe par aucune autorisation préalable avant d'être vendu : ce que promet
  le pot n'a été validé par personne. C'est développé dans
  <a href="/fr/blogs/diario/que-suplementos-tienen-evidencia">quels compléments
  ont des preuves et lesquels n'en ont pas</a>.</li>
</ul>

<h2>La vérification de trente secondes</h2>

<ol>
  <li>Grammes de protéines par prise ÷ grammes de poudre par prise. Au-dessus
  de 0,7 le produit est dense ; en dessous de 0,6, vous achetez pas mal de
  remplissage.</li>
  <li>Prix ÷ grammes de protéines de l'emballage. C'est le nombre qui
  compare.</li>
  <li>Première ligne de la liste des ingrédients : est-ce la protéine ?</li>
  <li>Y a-t-il un &laquo; mélange breveté &raquo; sans quantités ? S'il y en a
  un, produit suivant.</li>
</ol>

<p>Cela écarte la plus grande partie du marché sans lire un seul avis. Celles
de cette boutique déclarent les grammes par prise et la liste complète des
ingrédients sur la fiche, ce qu'il faut pour faire ce calcul.</p>
""",
        "fuentes": (
            "<li>Les règles du panneau d'information nutritionnelle, la liste "
            "des ingrédients par ordre de poids et le régime des compléments "
            "alimentaires —sans autorisation préalable à la vente— sont "
            "publiés par l'autorité fédérale des aliments et des "
            "médicaments.</li>\n"
            "<li>Le calcul des protéines à partir de l'azote est la méthode "
            "analytique inscrite dans la norme d'étiquetage elle-même.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("La répartition des protéines par repas, les tables de "
                  "teneur par aliment et la façon dont cela s'articule avec "
                  "le reste de la journée y sont développées en entier."),
    },
}


_ENLACE_DIARIO = re.compile(
    r'<a href="/(en|fr)/blogs/diario/([^"]+)">(.*?)</a>', re.S)


def _descolgar(texto: str, lengua: str) -> str:
    """Quita el ancla de los enlaces a artículos que aún no están en esa
    lengua, y deja el texto.

    Un artículo inglés que enlaza a otro que solo existe en castellano manda
    al comprador a una página que no puede leer, y con el prefijo /en/ delante
    ni siquiera existe: es un 404. En vez de acordarse de poner y quitar el
    ancla a mano cada vez que se traduce uno, se resuelve al componer. El día
    que el destino esté traducido, el enlace vuelve solo.
    """
    def uno(m):
        _, destino, dentro = m.groups()
        if lengua in CUERPOS.get(destino, {}):
            return m.group(0)
        return dentro
    return _ENLACE_DIARIO.sub(uno, texto)


def cuerpo(handle: str, lengua: str) -> str:
    """El cuerpo completo, con su pie de fuentes, su etiqueta y su firma."""
    a = CUERPOS[handle][lengua]
    compuesto = (a["cuerpo"].strip() + "\n\n"
                 + fuentes(a["fuentes"], lengua, a["base"])
                 + etiqueta(a["libro"], lengua, a["frase"])
                 + FIRMA[lengua])
    return _descolgar(compuesto, lengua)


def descolgados() -> list:
    """Los enlaces que hoy salen sin ancla, por faltar la traducción."""
    fuera = []
    for handle, lenguas in CUERPOS.items():
        for lengua in lenguas:
            crudo = lenguas[lengua]["cuerpo"]
            for _, destino, _dentro in _ENLACE_DIARIO.findall(crudo):
                if lengua not in CUERPOS.get(destino, {}):
                    fuera.append(f"{handle[:34]} [{lengua}] → {destino}")
    return fuera


def comprobar() -> list:
    """Medidas de buscador, bases legales y enlaces sin destino."""
    import articulos
    en_castellano = {a["handle"] for a in articulos.ARTICULOS}
    malos = []

    for handle, lenguas in CUERPOS.items():
        if handle not in en_castellano:
            malos.append(f"{handle} · no existe en castellano")
        for lengua, a in lenguas.items():
            if lengua not in LENGUAS:
                malos.append(f"{handle} · lengua desconocida: {lengua}")
                continue
            titulo, descripcion = a["meta"]
            if len(titulo) > TOPE_TITULO:
                malos.append(f"{handle} [{lengua}] · título "
                             f"{len(titulo)}/{TOPE_TITULO}")
            if len(descripcion) > TOPE_DESCRIPCION:
                malos.append(f"{handle} [{lengua}] · descripción "
                             f"{len(descripcion)}/{TOPE_DESCRIPCION}")
            if "VILLUMINATIONS" not in titulo:
                malos.append(f"{handle} [{lengua}] · el título no firma")
            if a["base"] not in CIERRE[lengua]:
                malos.append(f"{handle} [{lengua}] · base legal "
                             f"desconocida: {a['base']}")
            if a["libro"] not in LIBRO:
                malos.append(f"{handle} [{lengua}] · libro desconocido")
            # el cuerpo compuesto no puede llevar enlaces sin prefijo de
            # idioma: mandarían al comprador a la versión castellana
            texto = cuerpo(handle, lengua)
            for trozo in ('href="/products/', 'href="/blogs/',
                          'href="/collections/'):
                if trozo in texto:
                    malos.append(f"{handle} [{lengua}] · enlace sin prefijo "
                                 f"de idioma: {trozo}")
    return malos


def faltan() -> list:
    """Artículos castellanos que aún no están traducidos."""
    import articulos
    return sorted({a["handle"] for a in articulos.ARTICULOS} - set(CUERPOS))


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    malos, pendientes = comprobar(), faltan()
    total = sum(len(v) for v in CUERPOS.values())
    print(f"\n  {len(CUERPOS)} artículos traducidos · {total} versiones · "
          f"{len(malos)} problemas\n")
    for handle in CUERPOS:
        for lengua in LENGUAS:
            if lengua in CUERPOS[handle]:
                n = len(cuerpo(handle, lengua))
                print(f"    {handle[:40]:42} {lengua}  {n:6} caracteres")
    for m in malos:
        print(f"    {m}")
    if pendientes:
        print(f"\n    faltan {len(pendientes)} por traducir:")
        for h in pendientes:
            print(f"      {h}")
    sin = [c for c, l in COLECCION.items() if not all(l.values())]
    if sin:
        print(f"\n    colecciones sin handle traducido: {', '.join(sin)} "
              f"— hay que preguntárselo a la tienda")
    for d in descolgados():
        print(f"    enlace sin ancla hasta traducir el destino: {d}")
    print()
