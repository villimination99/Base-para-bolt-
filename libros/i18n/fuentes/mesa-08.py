# -*- coding: utf-8 -*-
"""
CÓDICE DE LA MESA · las fichas de los nutrientes de margen estrecho
==================================================================
Las cifras de estas fichas salen de la misma tabla que ya está en el generador,
así que se copian sin tocar los números y solo se adapta la puntuación: el
inglés separa los millares con coma y usa punto decimal —«3,000 µg», «1.3 mg»—
mientras que el español y el francés usan espacio fino y coma. «UI» es unidad
internacional y en inglés es «IU»; es de las pocas siglas de la tabla que sí
cambian.
"""

T = {
    "Estos son los que exigen leer la etiqueta y, en varios casos, un análisis previo. No son "
    "peligrosos: son los que no perdonan la aritmética descuidada de tomar tres productos que "
    "llevan lo mismo.": {
        "en": "These are the ones that demand you read the label and, in several cases, get a "
              "blood test first. They are not dangerous: they are the ones that do not "
              "forgive the careless arithmetic of taking three products that all contain the "
              "same thing.",
        "fr": "Ce sont ceux qui exigent de lire l'étiquette et, dans plusieurs cas, une "
              "analyse préalable. Ils ne sont pas dangereux : ce sont ceux qui ne pardonnent "
              "pas l'arithmétique négligente consistant à prendre trois produits qui "
              "contiennent la même chose."},

    "Referencia": {"en": "Reference", "fr": "Référence"},
    "Techo (UL)": {"en": "Ceiling (UL)", "fr": "Plafond (UL)"},
    "Lo que hay que saber": {"en": "What you need to know", "fr": "Ce qu'il faut savoir"},

    # ── Magnesio ───────────────────────────────────────────────────────────
    "420 mg en hombres · 320 en mujeres": {
        "en": "420 mg in men · 320 in women",
        "fr": "420 mg chez les hommes · 320 chez les femmes"},
    "350 mg": {"en": "350 mg", "fr": "350 mg"},

    "Único caso en que el UL parece menor que el RDA: el UL de 350 mg se refiere SOLO al "
    "magnesio de suplementos, no al de los alimentos": {
        "en": "The only case where the UL looks lower than the RDA: the 350 mg UL refers ONLY "
              "to magnesium from supplements, not from food",
        "fr": "Seul cas où l'UL semble inférieur à l'AJR : l'UL de 350 mg ne concerne QUE le "
              "magnésium des compléments, pas celui des aliments"},

    "Es el único caso en que el techo parece menor que la recomendación, y esa aparente "
    "contradicción es de las cosas más útiles que enseña esta tabla: el techo se refiere SOLO "
    "al magnesio de los suplementos y de los medicamentos, no al de los alimentos. Se puede "
    "comer magnesio tranquilamente; el efecto laxante que limita la cifra viene de las sales "
    "concentradas, no de las almendras.": {
        "en": "It is the only case where the ceiling looks lower than the recommendation, and "
              "that apparent contradiction is one of the most useful things this table "
              "teaches: the ceiling refers ONLY to magnesium from supplements and medicines, "
              "not from food. You can eat magnesium with no worries; the laxative effect that "
              "sets the figure comes from concentrated salts, not from almonds.",
        "fr": "C'est le seul cas où le plafond semble inférieur à la recommandation, et cette "
              "contradiction apparente est l'une des choses les plus utiles qu'enseigne ce "
              "tableau : le plafond ne concerne QUE le magnésium des compléments et des "
              "médicaments, pas celui des aliments. On peut manger du magnésium sans crainte ; "
              "l'effet laxatif qui fixe le chiffre vient des sels concentrés, pas des amandes."},

    # ── Hierro ─────────────────────────────────────────────────────────────
    "8 mg en hombres · 18 en mujeres": {
        "en": "8 mg in men · 18 in women",
        "fr": "8 mg chez les hommes · 18 chez les femmes"},
    "45 mg": {"en": "45 mg", "fr": "45 mg"},

    "Los 18 mg son para mujeres con menstruación. Suplementar sin analítica es mala idea: el "
    "exceso se acumula": {
        "en": "The 18 mg figure is for menstruating women. Supplementing without a blood test "
              "is a bad idea: the excess accumulates",
        "fr": "Les 18 mg concernent les femmes réglées. Se complémenter sans analyse est une "
              "mauvaise idée : l'excès s'accumule"},

    "La diferencia entre sexos es la mayor de toda la tabla y tiene una causa obvia. Lo que no "
    "es obvio es la asimetría del error: quedarse corto de hierro se corrige; pasarse de forma "
    "sostenida deposita hierro en órganos y no hay una vía fisiológica cómoda de sacarlo. "
    "Existen además personas con una predisposición genética a absorber más de lo normal que "
    "no lo saben. De todos los suplementos de venta libre, este es el que menos sentido tiene "
    "tomar sin una analítica delante.": {
        "en": "The difference between the sexes is the largest in the whole table and it has "
              "an obvious cause. What is not obvious is the asymmetry of the error: falling "
              "short of iron can be corrected; going over it in a sustained way deposits iron "
              "in organs and there is no convenient physiological route to get it out. There "
              "are also people with a genetic predisposition to absorb more than normal who "
              "do not know it. Of all over-the-counter supplements, this is the one it makes "
              "least sense to take without a blood test in front of you.",
        "fr": "La différence entre les sexes est la plus grande de tout le tableau et elle a "
              "une cause évidente. Ce qui ne l'est pas, c'est l'asymétrie de l'erreur : "
              "manquer de fer se corrige ; en prendre trop de façon durable dépose du fer "
              "dans les organes et il n'existe pas de voie physiologique commode pour l'en "
              "retirer. Il existe en outre des personnes génétiquement prédisposées à en "
              "absorber plus que la normale et qui l'ignorent. De tous les compléments en "
              "vente libre, c'est celui qu'il est le moins sensé de prendre sans une analyse "
              "sous les yeux."},

    # ── Selenio ────────────────────────────────────────────────────────────
    "55 µg en hombres · 55 en mujeres": {
        "en": "55 µg in men · 55 in women",
        "fr": "55 µg chez les hommes · 55 chez les femmes"},

    "Margen estrecho: el exceso es tóxico y la fuente más común de exceso son las nueces de "
    "Brasil": {
        "en": "Narrow margin: excess is toxic and the commonest source of excess is Brazil "
              "nuts",
        "fr": "Marge étroite : l'excès est toxique et la source d'excès la plus fréquente est "
              "la noix du Brésil"},

    "El caso didáctico del libro. La nuez de Brasil es la fuente alimentaria más concentrada "
    "que se conoce, con del orden de setenta a noventa microgramos por unidad, lo que "
    "significa que un puñado generoso puede acercarse al techo diario con comida corriente y "
    "sin ningún suplemento. No es motivo de alarma —una o dos al día cubren la necesidad de "
    "sobra— sino la demostración de que «natural» y «sin techo» no son sinónimos.": {
        "en": "The teaching case of this book. The Brazil nut is the most concentrated food "
              "source known, at something like seventy to ninety micrograms per nut, which "
              "means a generous handful can approach the daily ceiling with ordinary food and "
              "no supplement at all. It is no cause for alarm —one or two a day cover the "
              "requirement with room to spare— but a demonstration that «natural» and «no "
              "ceiling» are not synonyms.",
        "fr": "Le cas pédagogique de ce livre. La noix du Brésil est la source alimentaire la "
              "plus concentrée que l'on connaisse, de l'ordre de soixante-dix à quatre-vingt-"
              "dix microgrammes par unité, ce qui signifie qu'une poignée généreuse peut "
              "approcher le plafond quotidien avec de la nourriture ordinaire et sans aucun "
              "complément. Il n'y a pas lieu de s'alarmer —une ou deux par jour couvrent "
              "largement le besoin— mais c'est la démonstration que « naturel » et « sans "
              "plafond » ne sont pas synonymes."},

    # ── Vitamina B6 ────────────────────────────────────────────────────────
    "1,3 mg en hombres · 1,3 en mujeres": {
        "en": "1.3 mg in men · 1.3 in women",
        "fr": "1,3 mg chez les hommes · 1,3 chez les femmes"},
    "100 mg": {"en": "100 mg", "fr": "100 mg"},

    "El exceso sostenido produce neuropatía. Es uno de los UL que más se rebasan sin saberlo": {
        "en": "Sustained excess produces neuropathy. It is one of the most frequently "
              "exceeded ULs, and unknowingly so",
        "fr": "L'excès prolongé provoque une neuropathie. C'est l'un des UL les plus souvent "
              "dépassés sans le savoir"},

    "Aquí el margen parece amplio, y lo es en números; el problema es que las dosis de los "
    "productos comerciales lo son también. Hay complejos que llevan cincuenta o cien "
    "miligramos por cápsula, es decir decenas de veces la referencia, y el efecto adverso "
    "descrito por exceso sostenido es una neuropatía sensitiva. Es el ejemplo más limpio de un "
    "techo que se rebasa sin mala intención, sumando dos productos que ya lo llevan.": {
        "en": "Here the margin looks wide, and in numbers it is; the problem is that the doses "
              "in commercial products are wide too. There are complexes carrying fifty or a "
              "hundred milligrams per capsule, that is, tens of times the reference, and the "
              "adverse effect described for sustained excess is a sensory neuropathy. It is "
              "the cleanest example of a ceiling crossed with no ill intent, by adding "
              "together two products that already contain it.",
        "fr": "Ici la marge paraît large, et elle l'est en chiffres ; le problème est que les "
              "doses des produits du commerce le sont aussi. Certains complexes contiennent "
              "cinquante ou cent milligrammes par gélule, soit des dizaines de fois la "
              "référence, et l'effet indésirable décrit en cas d'excès prolongé est une "
              "neuropathie sensitive. C'est l'exemple le plus net d'un plafond franchi sans "
              "mauvaise intention, en additionnant deux produits qui en contiennent déjà."},

    # ── Vitamina A ─────────────────────────────────────────────────────────
    "900 µg RAE en hombres · 700 en mujeres": {
        "en": "900 µg RAE in men · 700 in women",
        "fr": "900 µg RAE chez les hommes · 700 chez les femmes"},
    "3 000 µg RAE": {"en": "3,000 µg RAE", "fr": "3 000 µg RAE"},

    "El UL es solo para la forma preformada (retinol), no para los carotenoides de los "
    "vegetales": {
        "en": "The UL applies only to the preformed form (retinol), not to the carotenoids in "
              "vegetables",
        "fr": "L'UL ne vaut que pour la forme préformée (rétinol), pas pour les caroténoïdes "
              "des végétaux"},

    "Con la distinción de la unidad ya explicada: el techo vale para el retinol preformado, el "
    "de los suplementos, el hígado y algunos aceites. Los carotenoides de las verduras no lo "
    "comprometen. Es una de esas veces en que dos sustancias con el mismo nombre en la "
    "etiqueta no se comportan igual.": {
        "en": "With the distinction in the unit already explained: the ceiling applies to "
              "preformed retinol, the kind in supplements, in liver and in some oils. The "
              "carotenoids in vegetables do not put it at risk. It is one of those times when "
              "two substances bearing the same name on the label do not behave the same way.",
        "fr": "Avec la distinction d'unité déjà expliquée : le plafond vaut pour le rétinol "
              "préformé, celui des compléments, du foie et de certaines huiles. Les "
              "caroténoïdes des légumes ne le mettent pas en jeu. C'est l'une de ces fois où "
              "deux substances portant le même nom sur l'étiquette ne se comportent pas de la "
              "même manière."},

    # ── Vitamina D ─────────────────────────────────────────────────────────
    "Y el de margen ancho que aun así hay que vigilar": {
        "en": "And the wide-margin one that still needs watching",
        "fr": "Et celui à marge large qu'il faut malgré tout surveiller"},

    "15 µg en hombres · 15 en mujeres": {
        "en": "15 µg in men · 15 in women",
        "fr": "15 µg chez les hommes · 15 chez les femmes"},

    "15 µg son 600 UI. A partir de los 71 años, 20 µg. El UL de 100 µg son 4 000 UI": {
        "en": "15 µg is 600 IU. From age 71, 20 µg. The UL of 100 µg is 4,000 IU",
        "fr": "15 µg font 600 UI. À partir de 71 ans, 20 µg. L'UL de 100 µg fait 4 000 UI"},
}
