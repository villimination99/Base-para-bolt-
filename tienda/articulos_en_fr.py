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
from pathlib import Path

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

# El nombre del libro en cada lengua, y de qué PDF sale su número de páginas.
#
# Las páginas NO se escriben aquí. Se escribieron a mano una vez y salieron
# mal cuatro de cinco —la Carga con 74 en vez de 70, el Descanso con 71 en vez
# de 53, el Zodiacal con 96 en vez de 144—, y esas cifras iban a publicarse en
# inglés y en francés al lado de las castellanas, que sí eran correctas. Ahora
# se cuentan del propio PDF y `comprobar()` las coteja además con lo que dice
# el artículo castellano. Una cifra que se puede contar no se teclea.
LIBRO = {
    "codice-de-la-mesa": {"en": "the Codex of the Table",
                          "fr": "le Codex de la Table", "pdf": "codice-mesa"},
    "codice-de-la-carga": {"en": "the Codex of the Load",
                           "fr": "le Codex de la Charge", "pdf": "codice-carga"},
    "codice-del-descanso": {"en": "the Codex of Rest",
                            "fr": "le Codex du Repos", "pdf": "codice-descanso"},
    "codice-zodiacal": {"en": "the Zodiacal Codex",
                        "fr": "le Codex Zodiacal", "pdf": "codice-zodiacal"},
    "codice-de-los-arcanos": {"en": "the Codex of the Arcana",
                              "fr": "le Codex des Arcanes",
                              "pdf": "codice-arcanos"},
}

DIST = Path(__file__).resolve().parent.parent / "libros" / "dist"


def paginas(handle: str) -> int:
    """Cuántas páginas tiene el PDF de ese libro, contadas del fichero."""
    pdf = DIST / f"{LIBRO[handle]['pdf']}.pdf"
    if not pdf.exists():
        raise FileNotFoundError(
            f"No está {pdf}. El número de páginas se cuenta del PDF, no se "
            f"escribe: reconstrúyelo con python3 libros/build.py")
    return len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))

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
    return ETIQUETA[lengua].format(frase=frase, handle=handle,
                                   libro=LIBRO[handle][lengua],
                                   paginas=paginas(handle))


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


CUERPOS["cuanta-actividad-fisica-hace-falta"] = {
    "en": {
        "titulo": "How much physical activity you actually need",
        "resumen": (
            "There is a dose, it is written down, and it is not the one "
            "repeated in the gym. How many minutes, of what kind, and why the "
            "first stretch is worth more than all the rest."),
        "meta": (
            "How much physical activity you need | VILLUMINATIONS",
            "The weekly dose the public guidelines recommend, the 2-for-1 "
            "exchange between moderate and vigorous, and the real shape of "
            "the curve."),
        "cuerpo": """
<p>The question has a published answer, and it is more specific than most
people imagine. It is not &laquo;move more&raquo;: it is an amount, with
units.</p>

<h2>The dose, in one line</h2>

<p>For a healthy adult, the public physical activity guidelines recommend, per
week:</p>

<ul>
  <li><strong>150 to 300 minutes</strong> of <em>moderate</em> intensity
  aerobic activity, or</li>
  <li><strong>75 to 150 minutes</strong> of <em>vigorous</em> intensity, or any
  equivalent combination of the two, and</li>
  <li><strong>two days or more</strong> of strength work involving all the
  major muscle groups.</li>
</ul>

<p>The exchange between the two is <strong>two for one</strong>: one vigorous
minute counts as two moderate ones. That way you can split it without odd
arithmetic.</p>

<h3>Where the line between moderate and vigorous falls</h3>

<p>Without a heart rate monitor, use the talk test: at <strong>moderate</strong>
intensity you can talk but not sing. At <strong>vigorous</strong> you cannot
say more than a few words in a row without stopping to breathe.</p>

<h2>The curve is not a straight line</h2>

<p>This is what changes how you approach the whole thing. The benefit does not
grow in proportion to the effort: <strong>by far the stretch that pays most is
the one from nothing to a little</strong>. Someone who does nothing and starts
moving gains vastly more than someone who already meets the dose and
doubles it.</p>

<p>Two practical consequences, and both go against what you usually hear:</p>

<ul>
  <li>If you do nothing, <strong>you do not have to reach 150 minutes for it to
  be worth it</strong>. Twenty minutes of walking three times a week is already
  buying the expensive stretch of the curve.</li>
  <li>If you already meet it, <strong>doubling the volume pays little</strong>.
  There the margin is in quality, strength and rest, not in more minutes.</li>
</ul>

<h2>The ten-minute minimum is gone</h2>

<p>For years it was repeated that a session had to last at least ten minutes to
count. <strong>That condition was removed</strong> in the revision of the
guidelines: everything counts. Climbing stairs, carrying the shopping, three
minutes of brisk walking. Activity accumulates; it does not need permission to
be long enough.</p>

<h2>Strength is not optional</h2>

<p>The two days a week of muscle work are in the recommendation with the same
standing as the aerobic part, and they are the part most people skip. No gym is
needed: body weight counts, so do bands and the loads of daily life, as long as
the muscle reaches a point where repeating is hard.</p>

<p>And from sixty-five onwards a third leg is added that almost nobody
mentions: <strong>balance training</strong>. It is the one that prevents the
fall, which in that age bracket does more damage than almost anything else.</p>

<h2>Sitting counts separately</h2>

<p>The other half of the message: <strong>moving more and sitting less are two
different recommendations</strong>, not the same one said twice. You can meet
the weekly dose and spend the rest of the day sitting, and that is still a
problem in its own right.</p>
""",
        "fuentes": (
            "<li><strong>health.gov</strong> — Physical Activity "
            "Guidelines, second edition: weekly dose, the 2-for-1 exchange, "
            "removal of the ten-minute minimum, balance from 65 onwards.</li>\n"
            "<li><strong>FM 7-22</strong> — Physical readiness doctrine: "
            "movement patterns and programming.</li>\n"
            "<li><strong>CDC / NIOSH</strong> — Criteria for manual "
            "handling of loads.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-carga",
        "frase": ("The eight movement patterns, the six variables a week is "
                  "programmed with and the lifting equation with its factors "
                  "worked through one by one take up a good deal more."),
    },
    "fr": {
        "titulo": "Combien d'activité physique il faut vraiment",
        "resumen": (
            "Il existe une dose, elle est écrite et ce n'est pas celle que "
            "l'on répète à la salle. Combien de minutes, de quelle sorte, et "
            "pourquoi le premier palier vaut plus que tous les autres."),
        "meta": (
            "Combien d'activité physique il faut | VILLUMINATIONS",
            "La dose hebdomadaire que recommandent les guides publics, "
            "l'échange 2 pour 1 entre modérée et vigoureuse, et la vraie forme "
            "de la courbe."),
        "cuerpo": """
<p>La question a une réponse publiée, et elle est plus précise que la plupart
ne l'imaginent. Ce n'est pas &laquo; bougez plus &raquo; : c'est une quantité,
avec des unités.</p>

<h2>La dose, en une ligne</h2>

<p>Pour une personne adulte en bonne santé, les guides publics d'activité
physique recommandent, par semaine :</p>

<ul>
  <li><strong>De 150 à 300 minutes</strong> d'activité aérobie d'intensité
  <em>modérée</em>, ou</li>
  <li><strong>de 75 à 150 minutes</strong> d'intensité <em>vigoureuse</em>, ou
  toute combinaison équivalente des deux, et</li>
  <li><strong>deux jours ou plus</strong> de travail de force sollicitant tous
  les grands groupes musculaires.</li>
</ul>

<p>L'échange entre les deux se fait <strong>deux pour un</strong> : une minute
vigoureuse compte pour deux modérées. On peut ainsi répartir sans calculs
bizarres.</p>

<h3>Où passe la frontière entre modérée et vigoureuse</h3>

<p>Sans cardiofréquencemètre, avec le test de la conversation : en activité
<strong>modérée</strong> vous pouvez parler mais pas chanter. En
<strong>vigoureuse</strong> vous ne pouvez pas dire plus de quelques mots
d'affilée sans vous arrêter pour respirer.</p>

<h2>La courbe n'est pas une droite</h2>

<p>C'est ce qui change la façon d'aborder la chose. Le bénéfice ne croît pas
proportionnellement à l'effort : <strong>le palier qui rend le plus, et de
loin, est celui qui va de rien à un peu</strong>. Quelqu'un qui ne fait rien et
se met à bouger gagne infiniment plus que quelqu'un qui remplit déjà la dose
et la double.</p>

<p>Deux conséquences pratiques, et les deux vont à l'encontre de ce qu'on
entend d'habitude :</p>

<ul>
  <li>Si vous ne faites rien, <strong>inutile d'atteindre les 150 minutes pour
  que ça vaille la peine</strong>. Vingt minutes de marche trois fois par
  semaine achètent déjà le palier cher de la courbe.</li>
  <li>Si vous remplissez déjà la dose, <strong>doubler le volume rend
  peu</strong>. Là, la marge est dans la qualité, la force et le repos, pas
  dans plus de minutes.</li>
</ul>

<h2>Le minimum de dix minutes n'existe plus</h2>

<p>Pendant des années on a répété qu'une séance devait durer au moins dix
minutes pour compter. <strong>Cette condition a été supprimée</strong> lors de
la révision des guides : tout compte. Monter les escaliers, porter les courses,
trois minutes de marche rapide. L'activité s'accumule, elle n'a pas besoin
d'une autorisation de durée.</p>

<h2>La force n'est pas facultative</h2>

<p>Les deux jours de travail musculaire par semaine figurent dans la
recommandation au même titre que la partie aérobie, et c'est la partie que le
plus de gens sautent. Pas besoin de salle : le poids du corps compte, les
élastiques aussi, et les charges de la vie quotidienne, pourvu que le muscle
atteigne un point où répéter coûte.</p>

<p>Et à partir de soixante-cinq ans s'ajoute un troisième pied dont on ne parle
presque jamais : <strong>l'entraînement de l'équilibre</strong>. C'est celui
qui prévient la chute, laquelle à cet âge fait plus de dégâts que presque tout
le reste.</p>

<h2>Rester assis compte à part</h2>

<p>L'autre moitié du message : <strong>bouger plus et rester assis moins sont
deux recommandations distinctes</strong>, pas la même dite deux fois. On peut
remplir la dose hebdomadaire et passer le reste de la journée assis, et cela
reste un problème en soi.</p>
""",
        "fuentes": (
            "<li><strong>health.gov</strong> — Guides d'activité physique, "
            "deuxième édition : dose hebdomadaire, échange 2 pour 1, retrait du "
            "minimum de dix minutes, équilibre à partir de 65 ans.</li>\n"
            "<li><strong>FM 7-22</strong> — Doctrine de préparation "
            "physique : schémas de mouvement et programmation.</li>\n"
            "<li><strong>CDC / NIOSH</strong> — Critères de manutention "
            "manuelle de charges.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-carga",
        "frase": ("Les huit schémas de mouvement, les six variables avec "
                  "lesquelles se programme une semaine et l'équation de "
                  "levage avec ses facteurs développés un à un occupent "
                  "bien davantage."),
    },
}


CUERPOS["gimnasio-en-casa-que-comprar-primero"] = {
    "en": {
        "titulo": "Home gym: what to buy first",
        "resumen": (
            "The order in which the money is best spent, what each piece "
            "solves, and the three purchases almost everyone makes too "
            "early."),
        "meta": (
            "Home gym: what to buy first | VILLUMINATIONS",
            "The order to spend in: floor, bench, bar, bands. What each piece "
            "solves and the three purchases made far too early."),
        "cuerpo": """
<p>Setting up a home gym goes wrong almost always for the same reason: things
get bought out of enthusiasm rather than in order. This is the order that
holds, with the reasoning behind each step.</p>

<h2>Before buying anything: how much training is needed</h2>

<p>The public physical activity recommendation for adults is <strong>150
minutes a week</strong> of moderate aerobic activity — or 75 of high intensity
— plus <strong>two days of strength work</strong> involving the major muscle
groups.</p>

<p>That defines what to buy. Two strength sessions a week do not call for a
whole room: they call for being able to load the basic patterns — push, pull,
hinge at the hip and bend at the knee — with a progression that is actually
possible.</p>

<h2>1. The floor, before the iron</h2>

<p>It is the least exciting purchase and the one you are most grateful for.
Interlocking tiles do three things: they protect the house floor, they cushion
your joints and they mark out a space your head recognises as &laquo;this is
where training happens&raquo;. The third is not mystical: it lowers the
friction of starting, which is where people give up.</p>

<h2>2. An adjustable bench</h2>

<p>It is the piece that unlocks the most exercises per dollar spent. With a
bench that inclines, declines and lies flat you get pressing at three angles,
supported rows, back extensions and all the seated arm work. Without one, half
the exercise list does not exist.</p>

<p>When comparing benches, look at the load capacity the manufacturer states
and the actual number of backrest positions. A three-position bench and a
seven-position bench are not the same piece of furniture.</p>

<h2>3. Load that progresses</h2>

<p>Strength depends on being able to <strong>raise the load little by
little</strong>. That is the criterion for choosing between a bar with plates,
a set of adjustable dumbbells or a plate-loaded machine: the question is not
how much it lifts today, but in how many steps it can go up.</p>

<p>A hex bar is, for home, the most rewarding: it allows deadlifting with the
back in a better position than a straight bar, and it also serves for shrugs
and lunges.</p>

<h2>4. Bands and vest, once there is a routine</h2>

<p>Bands solve what free weight does worst — abductions, glute activation,
accessory work — and they fit in a drawer. A weighted vest turns something you
already did, walking, into training. Neither is a first purchase; both are
excellent fourth ones.</p>

<h2>The three premature purchases</h2>

<ul>
  <li><strong>A large single-exercise machine.</strong> It takes up what a
  bench and a bar take up together and does one thing. It makes sense when that
  particular exercise is the axis of your programme, not before.</li>
  <li><strong>Fixed dumbbells in pairs.</strong> They fall short within two
  months and there is no next step up.</li>
  <li><strong>Accessories before load.</strong> Rollers, small pulleys, grips.
  All useful, none of them moves the needle if you still cannot progress on the
  basics.</li>
</ul>

<h2>The short list</h2>

<ul>
  <li>Tiles for two square metres.</li>
  <li>An adjustable bench.</li>
  <li>A bar and plates, or equivalent adjustable load.</li>
  <li>A set of bands.</li>
</ul>

<p>That covers the two strength days of the public recommendation for years.
Everything else is fine-tuning, and gets bought when the programme asks for
it.</p>
""",
        "fuentes": (
            "<li>The 150 weekly minutes and the two strength days are the "
            "physical activity recommendation published by the United States "
            "Government.</li>\n"
            "<li>The load capacities and measurements of each piece come from "
            "the manufacturer's documentation, and are only published when "
            "that documentation does not contradict itself.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-carga",
        "frase": ("The week-by-week load progression, the basic patterns and "
                  "how a session is ordered with this equipment are worked "
                  "through in full."),
    },
    "fr": {
        "titulo": "Salle à la maison : quoi acheter en premier",
        "resumen": (
            "L'ordre dans lequel il vaut mieux dépenser, ce que règle chaque "
            "pièce et les trois achats que presque tout le monde fait trop "
            "tôt."),
        "meta": (
            "Salle à la maison : quoi acheter d'abord | VILLUMINATIONS",
            "L'ordre pour dépenser : sol, banc, barre, élastiques. Ce que "
            "règle chaque pièce et les trois achats faits bien trop tôt."),
        "cuerpo": """
<p>Monter une salle à la maison rate presque toujours pour la même raison : on
achète par enthousiasme et non dans l'ordre. Voici l'ordre qui tient, avec le
raisonnement derrière chaque étape.</p>

<h2>Avant d'acheter quoi que ce soit : combien faut-il s'entraîner</h2>

<p>La recommandation publique d'activité physique pour les personnes adultes,
c'est <strong>150 minutes par semaine</strong> d'activité aérobie modérée — ou
75 d'intensité élevée — plus <strong>deux jours de travail de force</strong>
sollicitant les grands groupes musculaires.</p>

<p>Cela définit ce qu'il faut acheter. Deux séances de force par semaine ne
réclament pas une salle entière : elles réclament de pouvoir charger les
schémas de base — pousser, tirer, fléchir la hanche et le genou — avec une
progression réellement possible.</p>

<h2>1. Le sol, avant la fonte</h2>

<p>C'est l'achat le moins excitant et celui qu'on remercie le plus. Des dalles
emboîtables font trois choses : elles protègent le sol de la maison, elles
amortissent les articulations et elles délimitent un espace que votre tête
reconnaît comme &laquo; ici on s'entraîne &raquo;. Le troisième point n'a rien
de mystique : il réduit la friction du démarrage, et c'est là qu'on
abandonne.</p>

<h2>2. Un banc réglable</h2>

<p>C'est la pièce qui débloque le plus d'exercices par dollar dépensé. Avec un
banc qui s'incline, se décline et se met à plat, vous avez le développé sous
trois angles, le rowing en appui, les extensions lombaires et tout le travail
de bras assis. Sans lui, la moitié de la liste d'exercices n'existe pas.</p>

<p>En comparant des bancs, regardez la charge admise que déclare le fabricant
et le nombre réel de positions de dossier. Un banc à trois positions et un banc
à sept ne sont pas le même meuble.</p>

<h2>3. Une charge qui progresse</h2>

<p>La force dépend de pouvoir <strong>monter la charge petit à petit</strong>.
C'est le critère pour choisir entre une barre à disques, un jeu d'haltères
réglables ou une machine à charge de disques : la question n'est pas combien
elle soulève aujourd'hui, mais en combien de paliers elle peut monter.</p>

<p>Une barre hexagonale est, à la maison, la plus reconnaissante : elle permet
le soulevé de terre avec le dos en meilleure position qu'une barre droite, et
elle sert aussi pour les shrugs et les fentes.</p>

<h2>4. Élastiques et gilet, quand la routine est là</h2>

<p>Les élastiques règlent ce que le poids libre fait le moins bien —
abductions, activation du fessier, travail accessoire — et tiennent dans un
tiroir. Le gilet lesté transforme en entraînement quelque chose que vous
faisiez déjà : marcher. Aucun des deux n'est un premier achat ; les deux sont
d'excellents quatrièmes.</p>

<h2>Les trois achats prématurés</h2>

<ul>
  <li><strong>Une grande machine à un seul exercice.</strong> Elle occupe ce
  qu'occupent un banc et une barre réunis et fait une seule chose. Elle a du
  sens quand cet exercice précis est l'axe de votre programme, pas avant.</li>
  <li><strong>Des haltères fixes par paires.</strong> Ils deviennent trop
  légers en deux mois et il n'y a pas de palier suivant.</li>
  <li><strong>Des accessoires avant la charge.</strong> Rouleaux, petites
  poulies, poignées. Tous utiles, aucun ne change les choses si vous ne pouvez
  pas encore progresser sur les bases.</li>
</ul>

<h2>La liste courte</h2>

<ul>
  <li>Des dalles pour deux mètres carrés.</li>
  <li>Un banc réglable.</li>
  <li>Une barre et des disques, ou une charge réglable équivalente.</li>
  <li>Un jeu d'élastiques.</li>
</ul>

<p>Cela couvre les deux jours de force de la recommandation publique pendant
des années. Tout le reste est du réglage fin, et s'achète quand le programme le
demande.</p>
""",
        "fuentes": (
            "<li>Les 150 minutes hebdomadaires et les deux jours de force sont "
            "la recommandation d'activité physique publiée par le Gouvernement "
            "des États-Unis.</li>\n"
            "<li>Les charges admises et les dimensions de chaque pièce "
            "proviennent de la documentation du fabricant, et ne sont publiées "
            "que lorsque cette documentation ne se contredit pas.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-carga",
        "frase": ("La progression des charges semaine après semaine, les "
                  "schémas de base et la façon d'ordonner une séance avec ce "
                  "matériel y sont développées en entier."),
    },
}


CUERPOS["como-se-lee-una-etiqueta-nutricional"] = {
    "en": {
        "titulo": "How to read a nutrition label",
        "resumen": (
            "The percentage almost nobody knows how to read, the 5 and 20 "
            "rule, the legal tolerance that lets the figure be inexact, and "
            "the three commonest tricks."),
        "meta": (
            "How to read a nutrition label | VILLUMINATIONS",
            "The 5 and 20 rule, the percent daily value, the legal tolerance "
            "and why «0 g trans fat» may not be zero."),
        "cuerpo": """
<p>A nutrition label is not written so you can understand it at a glance: it is
written to comply with a regulation. That makes it reliable and opaque at the
same time. These are the four things you need in order to read one in ten
seconds.</p>

<h2>1. The serving rules over everything else</h2>

<p>Every figure on the panel refers to <strong>one serving</strong>, not to the
package. It is the commonest mistake and the most expensive: a bag that looks
like a single portion can declare two and a half servings, and then the
calories you just read have to be multiplied by two and a half.</p>

<p>Before looking at anything else, read two lines: <em>serving size</em> and
<em>servings per container</em>. If they do not match what you are about to
eat, the rest of the panel does not say what you think it says.</p>

<h2>2. The percentage refers to a person who is not you</h2>

<p>The <strong>percent daily value</strong> is calculated against a reference
diet of <strong>2,000 kcal</strong>. It is not your diet: it is a convention so
that labels can be compared with one another. If you eat 2,600 kcal, all those
percentages run high for you; if you eat 1,600, they run short.</p>

<p>It is for comparing two products, not for planning your day.</p>

<h2>3. The 5 and 20 rule</h2>

<p>It is the shortcut published by the labelling authority itself, and it works
without a calculator:</p>

<ul>
  <li><strong>5 % or less</strong> of the daily value in a nutrient: that
  product is <em>low</em> in it.</li>
  <li><strong>20 % or more</strong>: it is <em>high</em> in it.</li>
</ul>

<p>What makes it useful is applying it in both directions. You want 20 % or
more in fibre, calcium, iron or potassium. You want 5 % or less in saturated
fat, sodium and added sugars. With two products in your hands, that comparison
takes five seconds and is right almost every time.</p>

<h2>4. The printed figure has legal leeway</h2>

<p>Here is what almost nobody knows. The figure on the label <strong>is not
exact, and it does not have to be</strong>: the regulation allows a tolerance,
and it allows it in two different directions depending on the nutrient.</p>

<ul>
  <li>For nutrients you want to get — added vitamins and minerals, protein,
  fibre — the product must contain <strong>at least</strong> what is declared.
  It may have more.</li>
  <li>For those you want to limit — calories, sugars, total fat, saturated fat,
  sodium — the product <strong>may not exceed</strong> what is declared beyond
  a margin. It may have less.</li>
</ul>

<p>In other words: the manufacturer has an incentive to declare protein on the
low side and sodium on the high side, because that way it complies comfortably
in both directions. The label is honest and is still giving you the scenario
that suits it best.</p>

<h3>The rounding trick</h3>

<p>When an amount falls below a certain threshold, the regulation allows it to
be declared as zero. That is why products exist that advertise <strong>&laquo;0 g
trans fat&raquo;</strong> and carry partially hydrogenated oil in the ingredient
list. Each serving has little; three servings no longer do.</p>

<p>The practical rule: <strong>when the panel says zero and the ingredient list
says otherwise, the ingredient list wins.</strong></p>

<h2>The ingredient list, in order of weight</h2>

<p>Ingredients are ordered from most to least by amount. That turns the list
into a bar chart without bars: if sugar appears third, there is more sugar than
everything that comes after it put together.</p>

<p>The trick to distrust is <strong>splitting the sugar</strong>: a product
carrying glucose syrup, brown sugar, dextrose and juice concentrate spreads the
same thing across four names, so none of them climbs to the top places. Added
together they would be first.</p>

<h2>What a claim can and cannot say</h2>

<p>&laquo;No added sugar&raquo; does not mean no sugar: apple juice has no added
sugar and is loaded with its own. &laquo;Light&raquo; may refer to the colour.
&laquo;Natural&raquo; has, in practice, no definition that obliges anything.</p>

<p>The claims that are regulated — those linking a nutrient to a function of the
body — have a public register where you can look up which were approved and,
more interestingly, <strong>which were applied for and rejected</strong>. That
second list is the one that really shows what is demonstrated and what is
not.</p>
""",
        "fuentes": (
            "<li><strong>FDA</strong> — Nutrition facts panel, the 5 and "
            "20 rule, tolerances and rounding rules.</li>\n"
            "<li><strong>ODS · NIH</strong> — Dietary reference "
            "intakes.</li>\n"
            "<li><strong>European register of nutrition and health "
            "claims</strong> — approved and rejected.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("The detail — the fine print of the reference tables, the "
                  "nineteen micronutrients with their recommendation and "
                  "upper limit, and the approved claims in their official "
                  "wording — needs more room."),
    },
    "fr": {
        "titulo": "Comment lire une étiquette nutritionnelle",
        "resumen": (
            "Le pourcentage que presque personne ne sait interpréter, la règle "
            "du 5 et du 20, la tolérance légale qui permet au chiffre de ne "
            "pas être exact et les trois pièges les plus fréquents."),
        "meta": (
            "Comment lire une étiquette nutritionnelle | VILLUMINATIONS",
            "La règle du 5 et du 20, le pourcentage de valeur quotidienne, la "
            "tolérance légale et pourquoi « 0 g de gras trans » peut ne pas "
            "être zéro."),
        "cuerpo": """
<p>Une étiquette nutritionnelle n'est pas écrite pour être comprise d'un coup
d'œil : elle est écrite pour respecter une norme. Cela la rend fiable et opaque
à la fois. Voici les quatre choses à savoir pour la lire en dix secondes.</p>

<h2>1. La portion commande sur tout le reste</h2>

<p>Tous les chiffres du panneau se rapportent à <strong>une portion</strong>,
non à l'emballage. C'est l'erreur la plus courante et la plus coûteuse : un
sachet qui semble individuel peut déclarer deux portions et demie, et alors les
calories que vous venez de lire doivent être multipliées par deux et demi.</p>

<p>Avant de regarder quoi que ce soit, lisez deux lignes : <em>taille de la
portion</em> et <em>portions par emballage</em>. Si elles ne correspondent pas à
ce que vous allez manger, le reste du panneau ne dit pas ce que vous croyez.</p>

<h2>2. Le pourcentage se rapporte à une personne qui n'est pas vous</h2>

<p>Le <strong>pourcentage de valeur quotidienne</strong> est calculé sur un
régime de référence de <strong>2 000 kcal</strong>. Ce n'est pas votre régime :
c'est une convention pour que les étiquettes puissent être comparées entre
elles. Si vous mangez 2 600 kcal, tous ces pourcentages sont trop hauts pour
vous ; si vous mangez 1 600, trop bas.</p>

<p>Cela sert à comparer deux produits, pas à planifier votre journée.</p>

<h2>3. La règle du 5 et du 20</h2>

<p>C'est le raccourci que publie l'autorité d'étiquetage elle-même, et il
fonctionne sans calculatrice :</p>

<ul>
  <li><strong>5 % ou moins</strong> de la valeur quotidienne pour un nutriment :
  ce produit en est <em>pauvre</em>.</li>
  <li><strong>20 % ou plus</strong> : il en est <em>riche</em>.</li>
</ul>

<p>L'utile est de l'appliquer dans les deux sens. Vous voulez 20 % ou plus en
fibres, calcium, fer ou potassium. Vous voulez 5 % ou moins en gras saturés,
sodium et sucres ajoutés. Avec deux produits en main, cette comparaison se fait
en cinq secondes et tombe juste presque à tous les coups.</p>

<h2>4. Le chiffre imprimé a une marge légale</h2>

<p>Voici ce que presque personne ne sait. Le chiffre de l'étiquette <strong>n'est
pas exact, et il n'a pas à l'être</strong> : la norme admet une tolérance, et
elle l'admet dans deux directions distinctes selon le nutriment.</p>

<ul>
  <li>Pour les nutriments qu'il vaut mieux avoir — vitamines et minéraux
  ajoutés, protéines, fibres — le produit doit contenir <strong>au
  moins</strong> ce qui est déclaré. Il peut en avoir davantage.</li>
  <li>Pour ceux qu'il vaut mieux limiter — calories, sucres, matières grasses
  totales, gras saturés, sodium — le produit <strong>ne peut pas
  dépasser</strong> ce qui est déclaré au-delà d'une marge. Il peut en avoir
  moins.</li>
</ul>

<p>Autrement dit : le fabricant a intérêt à déclarer les protéines par le bas et
le sodium par le haut, car il respecte ainsi la norme avec de la marge dans les
deux sens. L'étiquette est honnête et vous donne quand même le scénario qui
l'arrange le plus.</p>

<h3>Le piège de l'arrondi</h3>

<p>Quand une quantité passe sous un certain seuil, la norme permet de la
déclarer à zéro. C'est pourquoi il existe des produits qui annoncent
<strong>« 0 g de gras trans »</strong> et portent de l'huile partiellement
hydrogénée dans la liste des ingrédients. Chaque portion en a peu ; trois
portions, non.</p>

<p>La règle pratique : <strong>quand le panneau dit zéro et que la liste des
ingrédients dit le contraire, c'est la liste des ingrédients qui gagne.</strong></p>

<h2>La liste des ingrédients, par ordre de poids</h2>

<p>Les ingrédients sont classés du plus au moins abondant. Cela transforme la
liste en graphique à barres sans barres : si le sucre apparaît en troisième
position, il y a plus de sucre que tout ce qui vient après réuni.</p>

<p>L'astuce dont il faut se méfier est la <strong>division du sucre</strong> :
un produit contenant sirop de glucose, sucre brun, dextrose et concentré de jus
répartit la même chose entre quatre noms, et ainsi aucun ne monte aux premières
places. Additionnés, ils seraient premiers.</p>

<h2>Ce qu'une allégation peut dire et ne peut pas dire</h2>

<p>« Sans sucre ajouté » ne veut pas dire sans sucre : un jus de pomme n'a pas
de sucre ajouté et est chargé du sien. « Léger » peut se rapporter à la
couleur. « Naturel » n'a, en pratique, aucune définition qui oblige à quoi que
ce soit.</p>

<p>Les allégations qui, elles, sont encadrées — celles qui relient un nutriment
à une fonction de l'organisme — disposent d'un registre public où l'on peut
consulter lesquelles ont été approuvées et, plus intéressant, <strong>lesquelles
ont été demandées et rejetées</strong>. Cette seconde liste est celle qui montre
vraiment ce qui est démontré et ce qui ne l'est pas.</p>
""",
        "fuentes": (
            "<li><strong>FDA</strong> — Panneau d'information "
            "nutritionnelle, règle du 5 et du 20, tolérances et règles "
            "d'arrondi.</li>\n"
            "<li><strong>ODS · NIH</strong> — Apports diététiques de "
            "référence.</li>\n"
            "<li><strong>Registre européen des allégations nutritionnelles et "
            "de santé</strong> — approuvées et rejetées.</li>\n"),
        "base": "federal",
        "libro": "codice-de-la-mesa",
        "frase": ("Le détail — les petits caractères des tables de référence, "
                  "les dix-neuf micronutriments avec leur recommandation et "
                  "leur limite supérieure, et les allégations approuvées dans "
                  "leur rédaction officielle — demande plus de place."),
    },
}


CUERPOS["cuantas-horas-hay-que-dormir"] = {
    "en": {
        "titulo": "How many hours you need to sleep",
        "resumen": (
            "The figure by age, what a short week does and does not give "
            "back, the countdown of the last few hours, and the sign that the "
            "problem is no longer one of sleep hygiene."),
        "meta": (
            "How many hours you need to sleep | VILLUMINATIONS",
            "The hours recommended by age, sleep debt, caffeine and alcohol "
            "with their timings, and when to stop reading advice."),
        "cuerpo": """
<p>The short answer has been published for years and still surprises people by
how inflexible it is.</p>

<h2>The figure, by age</h2>

<table>
  <thead><tr><th>Age</th><th>Hours per night</th></tr></thead>
  <tbody>
    <tr><td>13 to 18 years</td><td>8 to 10</td></tr>
    <tr><td>18 to 60 years</td><td>7 or more</td></tr>
    <tr><td>61 to 64 years</td><td>7 to 9</td></tr>
    <tr><td>65 years and over</td><td>7 to 8</td></tr>
  </tbody>
</table>

<p>Notice that the recommendation for adults is a <strong>floor</strong>, not a
target: seven or more. The belief that someone &laquo;only needs five
hours&raquo; almost never describes a person who functions on five hours; it
describes a person who has been tired for so long that they have forgotten what
not being tired feels like.</p>

<h2>The debt: what comes back and what does not</h2>

<p>Sleeping little from Monday to Friday and stretching out at the weekend
recovers <strong>part</strong> of what was lost, not all of it, and it has a
price: sleeping three extra hours on Saturday pushes the internal clock back
and means sleep does not come on Sunday night. Saturday is paid for with
Monday.</p>

<p>What recovers worst is what is noticed worst: sustained attention degrades
progressively and the perception of being degraded <strong>does not</strong>
keep pace with it. Someone a week into six-hour nights performs a good deal
worse than they think.</p>

<h2>The countdown of the last few hours</h2>

<p>Three substances with three different timings, and they are worth treating
separately:</p>

<ul>
  <li><strong>Caffeine.</strong> It takes on the order of five hours to clear
  half the dose, which means a four o'clock coffee still has a quarter in
  circulation at midnight. Sensitivity varies a great deal from person to
  person; a margin of six to eight hours before bed is the one that works for
  most people.</li>
  <li><strong>Alcohol.</strong> It is the most deceptive, because it helps you
  fall asleep and ruins what comes after: it <strong>fragments the second half
  of the night</strong>, exactly where the restorative sleep is. Falling asleep
  sooner and resting worse.</li>
  <li><strong>Nicotine.</strong> It is a stimulant and, on top of that,
  overnight withdrawal wakes you.</li>
</ul>

<h2>The room: three figures and no more</h2>

<p>Of everything said about the bedroom, what is actually measured comes down
to three things: <strong>cool, dark and quiet</strong>. Temperature below
daytime comfort; light as little as possible, phone included; and constant
noise disturbs less than intermittent noise.</p>

<p>The rest — pillows, scents, apps — you may like, but it is not on the same
level of evidence and it does not make up for an irregular schedule.</p>

<h2>The intervention that pays most is the dullest</h2>

<p>Above everything above: <strong>a fixed time to get up, every day, weekend
included</strong>. The internal clock anchors to the waking hour and to morning
light, not to bedtime. It is free, it requires buying nothing, and it beats any
supplement.</p>

<h3>The nap, done properly</h3>

<p>Ten to twenty minutes, and early. Longer than that enters deep sleep and you
wake up worse than before; later than that, it steals sleep pressure from the
night.</p>

<h2>When to stop reading advice</h2>

<p>All of the above is <strong>sleep hygiene for healthy people</strong>. There
are two situations where it does not apply and where carrying on reading
articles is wasting time:</p>

<ul>
  <li>You have been sleeping badly most nights for <strong>more than three
  months</strong>, with consequences during the day. That has a clinical name
  and a treatment, and the treatment that works is not advice from a blog.</li>
  <li>Someone has told you that <strong>you stop breathing while you
  sleep</strong>, or you snore and wake up tired with no explanation. That gets
  investigated, not corrected with the room temperature.</li>
</ul>

<p>In both cases, the next step is a doctor.</p>
""",
        "fuentes": (
            "<li><strong>CDC</strong> — Recommended sleep hours by age "
            "group.</li>\n"
            "<li><strong>NHLBI · NIH</strong> — Sleep debt, circadian "
            "rhythm and sleep hygiene.</li>\n"
            "<li><strong>NIOSH</strong> — Shift work and sleep.</li>\n"),
        "base": "federal",
        "libro": "codice-del-descanso",
        "frase": ("The architecture of a night phase by phase, what to do "
                  "when sleep does not come and in what order to try it, and "
                  "shifts and travel when the schedule is not yours to "
                  "choose, are worked through separately."),
    },
    "fr": {
        "titulo": "Combien d'heures faut-il dormir",
        "resumen": (
            "Le chiffre par âge, ce qu'une semaine courte rend et ce qu'elle "
            "ne rend pas, le compte à rebours des dernières heures et le "
            "signe que le problème n'est plus d'hygiène du sommeil."),
        "meta": (
            "Combien d'heures faut-il dormir | VILLUMINATIONS",
            "Les heures recommandées par âge, la dette de sommeil, la caféine "
            "et l'alcool avec leurs délais, et quand cesser de lire des "
            "conseils."),
        "cuerpo": """
<p>La réponse courte est publiée depuis des années et continue de surprendre
par le peu de souplesse qu'elle laisse.</p>

<h2>Le chiffre, par âge</h2>

<table>
  <thead><tr><th>Âge</th><th>Heures par nuit</th></tr></thead>
  <tbody>
    <tr><td>13 à 18 ans</td><td>De 8 à 10</td></tr>
    <tr><td>18 à 60 ans</td><td>7 ou plus</td></tr>
    <tr><td>61 à 64 ans</td><td>De 7 à 9</td></tr>
    <tr><td>65 ans et plus</td><td>De 7 à 8</td></tr>
  </tbody>
</table>

<p>Remarquez que la recommandation pour les adultes est un
<strong>plancher</strong>, non un objectif : sept ou plus. La croyance selon
laquelle on « n'a besoin que de cinq heures » ne décrit presque jamais quelqu'un
qui fonctionne avec cinq heures ; elle décrit quelqu'un qui est fatigué depuis
si longtemps qu'il a oublié ce que c'est que de ne pas l'être.</p>

<h2>La dette : ce qui se rattrape et ce qui ne se rattrape pas</h2>

<p>Dormir peu du lundi au vendredi et s'étirer le week-end récupère une
<strong>partie</strong> de ce qui a été perdu, pas tout, et cela a un prix :
dormir trois heures de plus le samedi retarde l'horloge interne et fait que le
sommeil ne vient pas le dimanche soir. On paie le samedi avec le lundi.</p>

<p>Ce qui se récupère le plus mal est ce qui se remarque le plus mal :
l'attention soutenue se dégrade progressivement et la perception d'être dégradé
<strong>ne</strong> suit <strong>pas</strong>. Qui dort six heures depuis une
semaine rend nettement moins bien qu'il ne le croit.</p>

<h2>Le compte à rebours des dernières heures</h2>

<p>Trois substances avec trois délais différents, et il vaut mieux les traiter
séparément :</p>

<ul>
  <li><strong>Caféine.</strong> Il faut de l'ordre de cinq heures pour éliminer
  la moitié de la dose, ce qui veut dire qu'un café de seize heures a encore un
  quart en circulation à minuit. La sensibilité varie beaucoup d'une personne à
  l'autre ; la marge de six à huit heures avant le coucher est celle qui
  fonctionne pour la plupart.</li>
  <li><strong>Alcool.</strong> C'est le plus trompeur, parce qu'il aide à
  s'endormir et abîme ce qui vient après : il <strong>fragmente la seconde
  moitié de la nuit</strong>, précisément là où se trouve le sommeil qui
  restaure. S'endormir plus tôt et se reposer moins bien.</li>
  <li><strong>Nicotine.</strong> C'est un stimulant et, de plus, le sevrage
  nocturne réveille.</li>
</ul>

<h2>La chambre : trois chiffres et pas un de plus</h2>

<p>De tout ce qui se dit sur la chambre, ce qui est mesuré se réduit à trois
choses : <strong>fraîche, sombre et silencieuse</strong>. La température sous
celle du confort diurne ; la lumière le moins possible, celle du téléphone
comprise ; et le bruit constant gêne moins que le bruit intermittent.</p>

<p>Le reste — oreillers, parfums, applications — peut vous plaire, mais n'est
pas au même niveau de preuve et ne compense pas un horaire irrégulier.</p>

<h2>L'intervention qui rend le plus est la plus ennuyeuse</h2>

<p>Au-dessus de tout ce qui précède : <strong>une heure fixe de lever, tous les
jours, week-end compris</strong>. L'horloge interne s'ancre sur l'heure du
réveil et sur la lumière du matin, pas sur l'heure du coucher. C'est gratuit,
cela n'oblige à rien acheter et cela bat n'importe quel complément.</p>

<h3>La sieste, si elle est bien faite</h3>

<p>De dix à vingt minutes, et tôt. Plus longue, elle entre dans le sommeil
profond et l'on se réveille moins bien qu'avant ; plus tard, elle vole de la
pression de sommeil à la nuit.</p>

<h2>Quand cesser de lire des conseils</h2>

<p>Tout ce qui précède est de l'<strong>hygiène du sommeil pour personnes en
bonne santé</strong>. Il y a deux situations où cela ne s'applique pas et où
continuer à lire des articles est une perte de temps :</p>

<ul>
  <li>Vous dormez mal la plupart des nuits depuis <strong>plus de trois
  mois</strong>, avec des conséquences dans la journée. Cela porte déjà un nom
  clinique et a un traitement, et le traitement qui marche n'est pas un conseil
  de blog.</li>
  <li>On vous a dit que <strong>vous cessez de respirer pendant votre
  sommeil</strong>, ou vous ronflez et vous levez fatigué sans explication. Cela
  s'explore, cela ne se corrige pas avec la température de la pièce.</li>
</ul>

<p>Dans les deux cas, l'étape suivante est un médecin.</p>
""",
        "fuentes": (
            "<li><strong>CDC</strong> — Heures de sommeil recommandées par "
            "groupe d'âge.</li>\n"
            "<li><strong>NHLBI · NIH</strong> — Dette de sommeil, rythme "
            "circadien et hygiène du sommeil.</li>\n"
            "<li><strong>NIOSH</strong> — Travail posté et sommeil.</li>\n"),
        "base": "federal",
        "libro": "codice-del-descanso",
        "frase": ("L'architecture d'une nuit phase par phase, quoi faire "
                  "quand le sommeil ne vient pas et dans quel ordre "
                  "l'essayer, et les quarts et les voyages quand l'horaire ne "
                  "se choisit pas, y sont développés à part."),
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

CUERPOS["que-suplementos-tienen-evidencia"] = {
    "en": {
        "titulo": "Which supplements have evidence and which do not",
        "resumen": (
            "The few that have passed the test, the many that have not, and "
            "the fact about how they are regulated that changes how you buy "
            "them."),
        "meta": (
            "Which supplements have evidence | VILLUMINATIONS",
            "Creatine, caffeine, protein and the ones that fall short. How "
            "supplements are really regulated and what seal to look for if "
            "you compete."),
        "cuerpo": """
<p>Before the list, the fact that reorders everything else.</p>

<h2>A supplement is not approved before it goes on sale</h2>

<p>Unlike a medicine, a food supplement <strong>does not go through a prior
authorisation</strong> that verifies it does what it says. The manufacturer is
responsible for the product being safe and for the label not misleading, and
the authority acts mostly <em>afterwards</em>, if something goes wrong.</p>

<p>That does not mean supplements are useless or dangerous. It means the phrase
&laquo;it is on sale&raquo; carries no information about whether it works. The
evidence has to be looked at separately, product by product.</p>

<h2>The ones that have passed the test</h2>

<h3>Creatine monohydrate</h3>
<p>It is the most studied sports supplement there is, by a wide margin and by
many years. It is researched in the range of <strong>3 to 5 grams a
day</strong>. It is also one of the cheapest, which says a fair amount about
the relationship between price and evidence in this market.</p>

<h3>Caffeine</h3>
<p>A recognised ergogenic aid, usually studied in the range of <strong>3 to
6 mg per kilo of body weight</strong> taken between half an hour and an hour
before. Going above that does not improve the effect and does worsen that
night's sleep — which, if you have read the article on rest, is paying on one
side what you gain on the other.</p>

<h3>Protein powder</h3>
<p>Here it is worth being exact: protein powder <strong>is not an active
compound, it is convenient food</strong>. What has evidence is reaching the
day's total protein; the powder is a practical way of getting there, not a
different route. If you already get there by eating, it adds nothing.</p>

<h3>Beta-alanine and citrulline malate</h3>
<p>Real but modest effects, and in fairly specific kinds of effort. They are
not at the level of the three above and they are not the first place to
spend.</p>

<h2>The ones that fall short</h2>

<p>This list is longer than the previous one. The usual case is not that a
supplement has been <em>refuted</em>, but that the studies supporting it are
small, in animals, or at doses nothing like the ones in the tub.</p>

<p>Three signs you are looking at one of those:</p>

<ul>
  <li><strong>The dose in the tub is not the dose in the study.</strong> It is
  the commonest trick. Serious research is cited, done with an amount the
  product does not come close to carrying.</li>
  <li><strong>A proprietary blend with no amounts.</strong> If the label says
  &laquo;patented complex&raquo; and lists twelve ingredients without saying
  how much of each, it cannot be compared with anything. That is the
  point.</li>
  <li><strong>It promises several things at once.</strong> Energy, focus, fat
  burning and better sleep are not the same mechanism.</li>
</ul>

<h3>The case of BCAAs</h3>
<p>They deserve a separate mention because they sell a lot. If your protein
intake for the day is already adequate, branched-chain amino acids on their
own add little: you are already taking them inside the complete protein.</p>

<h2>The hierarchy, and this is the important part</h2>

<p>The order in which things move the result, from most to least:</p>

<ol>
  <li>Total calories and the day's protein.</li>
  <li>Consistent training, with progression.</li>
  <li>Enough sleep.</li>
  <li><strong>And then, a long way after, supplements.</strong></li>
</ol>

<p>A supplement on top of a broken base fixes nothing. The honest way to put it
is that supplements are the final one per cent, and they only make sense once
the other ninety-nine is already in place.</p>

<h2>If you compete, check the seal</h2>

<p>A product can be contaminated with undeclared substances without the
manufacturer intending it. For anyone subject to anti-doping controls, the only
practical protection is a <strong>third-party verification</strong> programme
that tests batch by batch. The seal goes on the packaging and can be checked
against the programme's register.</p>

<p>And a general warning: <strong>if you take medication, are pregnant or have
a medical condition, ask first</strong>. Interactions exist and some of them
are serious.</p>
""",
        "fuentes": (
            "<li><strong>ODS \u00b7 NIH</strong> \u2014 Fact sheets on dietary "
            "supplements and their regulatory framework.</li>\n"
            "<li><strong>FDA</strong> \u2014 The regime for food supplements: "
            "manufacturer responsibility and the absence of prior "
            "authorisation.</li>\n"
            "<li><strong>European register of health claims</strong> \u2014 what "
            "was approved and what was rejected.</li>\n"),
        "base": "federal",
        "cierre": (
            "<p><strong>What we sell and what we say.</strong> This shop sells "
            "supplements, so it is worth being clear: this article describes "
            "what the public evidence says about certain substances, not what "
            "any particular tub does. Our product pages promise no health "
            "effects, and that is not modesty.</p>\n"
            "<p>The <a href=\"/en/products/pro-definicion-volumen\">supplement "
            "guide in the Pro tier</a> works this through with the full "
            "hierarchy, the meta-analysis dose criterion and a monthly budget "
            "by level.</p>"),
    },
    "fr": {
        "titulo": "Quels compl\u00e9ments ont des preuves et lesquels non",
        "resumen": (
            "Les quelques-uns qui ont pass\u00e9 l'\u00e9preuve, les nombreux qui ne "
            "l'ont pas pass\u00e9e, et le fait sur leur encadrement qui change la "
            "fa\u00e7on de les acheter."),
        "meta": (
            "Quels compl\u00e9ments ont des preuves | VILLUMINATIONS",
            "Cr\u00e9atine, caf\u00e9ine, prot\u00e9ines et ceux qui ne suivent pas. Comment "
            "les compl\u00e9ments sont vraiment encadr\u00e9s et quel sceau regarder si "
            "vous concourez."),
        "cuerpo": """
<p>Avant la liste, le fait qui remet tout le reste en ordre.</p>

<h2>Un compl\u00e9ment n'est pas approuv\u00e9 avant d'\u00eatre vendu</h2>

<p>Contrairement \u00e0 un m\u00e9dicament, un compl\u00e9ment alimentaire <strong>ne passe
pas par une autorisation pr\u00e9alable</strong> v\u00e9rifiant qu'il fait ce qu'il
annonce. Le fabricant est responsable de la s\u00e9curit\u00e9 de son produit et de
l'honn\u00eatet\u00e9 de l'\u00e9tiquette, et l'autorit\u00e9 intervient surtout <em>apr\u00e8s</em>,
si quelque chose tourne mal.</p>

<p>Cela ne veut pas dire qu'ils sont inutiles ni dangereux. Cela veut dire que
la phrase &laquo; c'est en vente &raquo; n'apporte aucune information sur son
efficacit\u00e9. Il faut regarder les preuves s\u00e9par\u00e9ment, produit par produit.</p>

<h2>Ceux qui ont pass\u00e9 l'\u00e9preuve</h2>

<h3>Cr\u00e9atine monohydrate</h3>
<p>C'est le compl\u00e9ment sportif le plus \u00e9tudi\u00e9 qui existe, de loin et avec
beaucoup d'ann\u00e9es d'avance. Il est \u00e9tudi\u00e9 dans une fourchette de <strong>3 \u00e0
5 grammes par jour</strong>. C'est aussi l'un des moins chers, ce qui en dit
long sur le rapport entre le prix et les preuves sur ce march\u00e9.</p>

<h3>Caf\u00e9ine</h3>
<p>Aide ergog\u00e9nique reconnue, \u00e9tudi\u00e9e habituellement dans une fourchette de
<strong>3 \u00e0 6 mg par kilo de poids</strong>, prise entre une demi-heure et une
heure avant. Monter au-dessus n'am\u00e9liore pas l'effet et d\u00e9grade le sommeil de
la nuit \u2014 ce qui, si vous avez lu l'article sur le repos, revient \u00e0 payer d'un
c\u00f4t\u00e9 ce que l'on gagne de l'autre.</p>

<h3>Prot\u00e9ines en poudre</h3>
<p>Ici il faut \u00eatre exact : la prot\u00e9ine en poudre <strong>n'est pas un compos\u00e9
actif, c'est de la nourriture commode</strong>. Ce qui a des preuves, c'est
d'atteindre le total de prot\u00e9ines de la journ\u00e9e ; la poudre est une fa\u00e7on
pratique d'y arriver, pas une autre voie. Si vous y arrivez d\u00e9j\u00e0 en mangeant,
elle n'ajoute rien.</p>

<h3>B\u00eata-alanine et citrulline malate</h3>
<p>Des effets r\u00e9els mais modestes, et sur des types d'effort assez pr\u00e9cis. Ils
ne sont pas au niveau des trois pr\u00e9c\u00e9dents et ce n'est pas le premier endroit
o\u00f9 d\u00e9penser.</p>

<h2>Ceux qui ne suivent pas</h2>

<p>La liste est plus longue que la pr\u00e9c\u00e9dente. Le cas habituel n'est pas qu'un
compl\u00e9ment soit <em>r\u00e9fut\u00e9</em>, mais que les \u00e9tudes qui le soutiennent soient
petites, faites sur des animaux, ou \u00e0 des doses qui ne ressemblent pas \u00e0
celles du pot.</p>

<p>Trois signes que vous \u00eates devant l'un de ceux-l\u00e0 :</p>

<ul>
  <li><strong>La dose du pot n'est pas celle de l'\u00e9tude.</strong> C'est le
  pi\u00e8ge le plus courant. On cite une recherche s\u00e9rieuse men\u00e9e avec une
  quantit\u00e9 que le produit est loin de contenir.</li>
  <li><strong>M\u00e9lange maison sans quantit\u00e9s.</strong> Si l'\u00e9tiquette annonce
  un &laquo; complexe brevet\u00e9 &raquo; et liste douze ingr\u00e9dients sans dire
  combien il y a de chacun, il ne peut \u00eatre compar\u00e9 \u00e0 rien. C'est le
  but.</li>
  <li><strong>Il promet plusieurs choses \u00e0 la fois.</strong> \u00c9nergie,
  concentration, perte de gras et meilleur sommeil ne sont pas le m\u00eame
  m\u00e9canisme.</li>
</ul>

<h3>Le cas des BCAA</h3>
<p>Ils m\u00e9ritent une mention \u00e0 part parce qu'ils se vendent beaucoup. Si votre
apport en prot\u00e9ines de la journ\u00e9e est d\u00e9j\u00e0 suffisant, les acides amin\u00e9s
ramifi\u00e9s pris \u00e0 part ajoutent peu : vous les prenez d\u00e9j\u00e0 dans la prot\u00e9ine
compl\u00e8te.</p>

<h2>La hi\u00e9rarchie, et c'est l\u00e0 l'essentiel</h2>

<p>L'ordre dans lequel les choses changent le r\u00e9sultat, du plus au moins :</p>

<ol>
  <li>Calories totales et prot\u00e9ines de la journ\u00e9e.</li>
  <li>Entra\u00eenement constant, avec progression.</li>
  <li>Sommeil suffisant.</li>
  <li><strong>Et ensuite, bien apr\u00e8s, les compl\u00e9ments.</strong></li>
</ol>

<p>Un compl\u00e9ment pos\u00e9 sur une base cass\u00e9e ne r\u00e9pare rien. La formule honn\u00eate
est que les compl\u00e9ments sont le dernier un pour cent, et qu'ils n'ont de sens
que lorsque les quatre-vingt-dix-neuf autres sont d\u00e9j\u00e0 en place.</p>

<h2>Si vous concourez, regardez le sceau</h2>

<p>Un produit peut \u00eatre contamin\u00e9 par des substances non d\u00e9clar\u00e9es sans que le
fabricant le veuille. Pour qui passe des contr\u00f4les antidopage, la seule
protection pratique tient aux programmes de <strong>v\u00e9rification par un
tiers</strong> qui analysent lot par lot. Le sceau figure sur l'emballage et se
v\u00e9rifie dans le registre du programme.</p>

<p>Et un avertissement g\u00e9n\u00e9ral : <strong>si vous prenez un m\u00e9dicament, si vous
\u00eates enceinte ou si vous avez une pathologie, demandez avant</strong>. Les
interactions existent et certaines sont s\u00e9rieuses.</p>
""",
        "fuentes": (
            "<li><strong>ODS \u00b7 NIH</strong> \u2014 Fiches de donn\u00e9es sur les "
            "compl\u00e9ments alimentaires et leur cadre r\u00e9glementaire.</li>\n"
            "<li><strong>FDA</strong> \u2014 R\u00e9gime des compl\u00e9ments alimentaires : "
            "responsabilit\u00e9 du fabricant et absence d'autorisation "
            "pr\u00e9alable.</li>\n"
            "<li><strong>Registre europ\u00e9en des all\u00e9gations de sant\u00e9</strong> "
            "\u2014 ce qui a \u00e9t\u00e9 approuv\u00e9 et ce qui a \u00e9t\u00e9 rejet\u00e9.</li>\n"),
        "base": "federal",
        "cierre": (
            "<p><strong>Ce que nous vendons et ce que nous disons.</strong> "
            "Cette boutique vend des compl\u00e9ments, alors autant \u00eatre clair : cet "
            "article d\u00e9crit ce que dit la preuve publique sur certaines "
            "substances, pas ce que fait un pot en particulier. Les fiches de "
            "nos produits ne promettent aucun effet sur la sant\u00e9, et ce n'est "
            "pas par modestie.</p>\n"
            "<p>Le <a href=\"/fr/products/pro-definicion-volumen\">guide de "
            "suppl\u00e9mentation de la formule Pro</a> d\u00e9veloppe cela avec la "
            "hi\u00e9rarchie compl\u00e8te, le crit\u00e8re de la dose des m\u00e9ta-analyses et "
            "un budget mensuel par niveau.</p>"),
    },
}


def cuerpo(handle: str, lengua: str) -> str:
    """El cuerpo completo, con su pie de fuentes, su remate y su firma.

    El remate normal es la etiqueta que señala el libro que desarrolla el
    tema. Algunos artículos cierran con sus propios párrafos —el de la
    evidencia dice de frente qué vende esta tienda y qué no promete— y esos
    traen `cierre` en vez de `libro`. Uno u otro, no los dos.
    """
    a = CUERPOS[handle][lengua]
    if "cierre" in a:
        remate = a["cierre"]
    else:
        remate = etiqueta(a["libro"], lengua, a["frase"])
    compuesto = (a["cuerpo"].strip() + "\n\n"
                 + fuentes(a["fuentes"], lengua, a["base"])
                 + remate + FIRMA[lengua])
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
            if ("libro" in a) == ("cierre" in a):
                malos.append(f"{handle} [{lengua}] · o remata con un libro o "
                             f"con su propio cierre, no las dos ni ninguna")
            elif "libro" in a:
                if a["libro"] not in LIBRO:
                    malos.append(f"{handle} [{lengua}] · libro desconocido")
                else:
                    # ¿coincide con lo que dice el castellano publicado?
                    original = next(x["cuerpo"] for x in articulos.ARTICULOS
                                    if x["handle"] == handle)
                    dice = re.search(r"PDF de (\d+) páginas", original)
                    real = paginas(a["libro"])
                    if dice and int(dice.group(1)) != real:
                        malos.append(
                            f"{handle} [{lengua}] · el castellano dice "
                            f"{dice.group(1)} páginas y el PDF tiene {real}")
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
