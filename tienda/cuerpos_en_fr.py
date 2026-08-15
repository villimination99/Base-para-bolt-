#!/usr/bin/env python3
"""
VILLUMINATIONS — Cuerpos de proveedor en inglés y en francés
------------------------------------------------------------
La ficha en castellano de `catalogo.py` es el original. Esto la traduce.

**No se traduce el texto del proveedor.** Viene lleno de declaraciones de salud
—«boosts energy», «anti-aging», «supports immunity»— y copiarlo como versión
inglesa metería por la puerta de atrás justo lo que la ficha castellana quitó
por delante. Se traduce lo que está escrito en `CUERPOS`, y nada más.

Se compone igual que el original: un molde por lengua, y por producto solo las
cuatro partes que cambian. Las advertencias y el aviso legal son constantes,
así que existen una vez por lengua en vez de treinta.

    python3 tienda/cuerpos_en_fr.py     # comprueba y enseña qué falta
"""

# ---------------------------------------------------------------------------
# Moldes
# ---------------------------------------------------------------------------
AVISO_EN = (
    "<h3>Warnings</h3>\n"
    "<p>Do not exceed the recommended dose. If you are pregnant or "
    "breastfeeding, under 18, or have any medical condition, consult a health "
    "professional before taking it. Keep out of reach of children. Do not use "
    "if the seal is broken or missing. Store in a cool, dry place.</p>"
)
PIE_EN = (
    "<p><em>Food supplement. It does not replace a varied, balanced diet or a "
    "healthy lifestyle. This product is not intended to diagnose, treat, cure "
    "or prevent any disease.</em></p>"
)

AVISO_FR = (
    "<h3>Avertissements</h3>\n"
    "<p>Ne pas dépasser la dose recommandée. Les personnes enceintes ou "
    "allaitantes, les moins de 18 ans et les personnes atteintes d'une "
    "pathologie doivent consulter un professionnel de santé avant d'en "
    "prendre. Tenir hors de portée des enfants. Ne pas utiliser si l'opercule "
    "est brisé ou absent. Conserver dans un endroit frais et sec.</p>"
)
PIE_FR = (
    "<p><em>Complément alimentaire. Il ne remplace ni une alimentation variée "
    "et équilibrée ni un mode de vie sain. Ce produit n'est pas destiné à "
    "diagnostiquer, traiter, guérir ou prévenir une maladie.</em></p>"
)


def ficha_en(intro, composicion, formato, empleo):
    return (f"<p>{intro}</p>\n\n"
            f"<h3>Composition</h3>\n<p>{composicion}</p>\n\n"
            f"<h3>Format</h3>\n<ul>\n{formato}</ul>\n\n"
            f"<h3>How to take it</h3>\n<p>{empleo}</p>\n\n"
            f"{AVISO_EN}\n{PIE_EN}")


def ficha_fr(intro, composicion, formato, empleo):
    return (f"<p>{intro}</p>\n\n"
            f"<h3>Composition</h3>\n<p>{composicion}</p>\n\n"
            f"<h3>Format</h3>\n<ul>\n{formato}</ul>\n\n"
            f"<h3>Mode d'emploi</h3>\n<p>{empleo}</p>\n\n"
            f"{AVISO_FR}\n{PIE_FR}")


# Las tres líneas que se repiten en todos los formatos.
_HECHO_EN = "<li>Made in the United States</li>\n"
_HECHO_FR = "<li>Fabriqué aux États-Unis</li>\n"


def _bruto_en(g):
    return f"<li>Gross weight {g} g</li>\n"


def _bruto_fr(g):
    return f"<li>Poids brut {g} g</li>\n"


# ---------------------------------------------------------------------------
# Los diez suplementos
# ---------------------------------------------------------------------------
CUERPOS_EN = {}
CUERPOS_FR = {}

CUERPOS_EN["nad"] = ficha_en(
    "Capsules with <strong>500 mg of NAD+</strong> (nicotinamide adenine "
    "dinucleotide) per serving, alongside plant-sourced quercetin and "
    "resveratrol. NAD+ is a coenzyme involved in the energy metabolism of the "
    "cell.",
    "NAD+ (nicotinamide adenine dinucleotide) 500 mg; dihydrated quercetin "
    "extract <em>(Sophora japonica</em>, flower bud) 250 mg; Japanese knotweed "
    "extract <em>(Polygonum cuspidatum</em>, root, 98 % resveratrol) 150 mg. "
    "HPMC vegetable capsule, microcrystalline cellulose, brown rice flour, "
    "olive oil, silicon dioxide and magnesium stearate.",
    "<li><strong>60 capsules</strong> · 50 g net</li>\n"
    + _bruto_en(68) + _HECHO_EN,
    "Two capsules a day with about 175 ml of water, or as directed by a health "
    "professional.")
CUERPOS_FR["nad"] = ficha_fr(
    "Gélules apportant <strong>500 mg de NAD+</strong> (nicotinamide adénine "
    "dinucléotide) par prise, accompagnées de quercétine et de resvératrol "
    "d'origine végétale. Le NAD+ est une coenzyme qui participe au métabolisme "
    "énergétique de la cellule.",
    "NAD+ (nicotinamide adénine dinucléotide) 500 mg ; extrait de quercétine "
    "dihydratée <em>(Sophora japonica</em>, bouton floral) 250 mg ; extrait de "
    "renouée du Japon <em>(Polygonum cuspidatum</em>, racine, 98 % de "
    "resvératrol) 150 mg. Gélule végétale en HPMC, cellulose "
    "microcristalline, farine de riz complet, huile d'olive, dioxyde de "
    "silicium et stéarate de magnésium.",
    "<li><strong>60 gélules</strong> · 50 g net</li>\n"
    + _bruto_fr(68) + _HECHO_FR,
    "Deux gélules par jour avec environ 175 ml d'eau, ou selon l'avis d'un "
    "professionnel de santé.")

CUERPOS_EN["creatine-hydration-powder"] = ficha_en(
    "A powder combining <strong>5 g of creatine monohydrate</strong> with "
    "electrolytes — magnesium, sodium and potassium — in every serving. Lemon "
    "flavour, sweetened with stevia and free of colourings.",
    "Creatine (as creatine monohydrate) 5000 mg; magnesium (as magnesium "
    "malate) 60 mg; sodium (as sea salt) 1000 mg; potassium (as potassium "
    "chloride) 200 mg. Natural flavours, stevia leaf extract and silicon "
    "dioxide.",
    "<li><strong>300 g</strong> of powder · lemon flavour</li>\n"
    + _bruto_en(386) + _HECHO_EN,
    "One scoop (10 g) a day dissolved in 175–235 ml of water or the drink of "
    "your choice.")
CUERPOS_FR["creatine-hydration-powder"] = ficha_fr(
    "Poudre qui associe <strong>5 g de créatine monohydrate</strong> à des "
    "électrolytes — magnésium, sodium et potassium — à chaque prise. Saveur "
    "citron, à la stévia et sans colorants.",
    "Créatine (sous forme de créatine monohydrate) 5000 mg ; magnésium (sous "
    "forme de malate de magnésium) 60 mg ; sodium (sous forme de sel marin) "
    "1000 mg ; potassium (sous forme de chlorure de potassium) 200 mg. Arômes "
    "naturels, extrait de stévia (feuille) et dioxyde de silicium.",
    "<li><strong>300 g</strong> de poudre · saveur citron</li>\n"
    + _bruto_fr(386) + _HECHO_FR,
    "Une dosette (10 g) par jour dissoute dans 175 à 235 ml d'eau ou de la "
    "boisson de votre choix.")

CUERPOS_EN["nmn"] = ficha_en(
    "Capsules with <strong>500 mg of ß-nicotinamide mononucleotide</strong> "
    "(99.9 % purity) per serving and nothing else added. NMN is a precursor of "
    "NAD+ in the pathway the cell uses to produce it.",
    "β-nicotinamide mononucleotide 500 mg. HPMC vegetable capsule, "
    "microcrystalline cellulose, silicon dioxide and magnesium stearate. A "
    "single active ingredient: no blends, no unnecessary additions.",
    "<li><strong>30 capsules</strong> · 36 g net</li>\n"
    + _bruto_en(45) + _HECHO_EN,
    "One capsule a day with 175–235 ml of water, or as directed by a health "
    "professional.")
CUERPOS_FR["nmn"] = ficha_fr(
    "Gélules apportant <strong>500 mg de ß-nicotinamide mononucléotide</strong> "
    "(pureté de 99,9 %) par prise, sans rien d'autre. Le NMN est un précurseur "
    "du NAD+ dans la voie que la cellule emprunte pour le produire.",
    "β-nicotinamide mononucléotide 500 mg. Gélule végétale en HPMC, cellulose "
    "microcristalline, dioxyde de silicium et stéarate de magnésium. Un seul "
    "principe actif : ni mélange ni ajouts superflus.",
    "<li><strong>30 gélules</strong> · 36 g net</li>\n"
    + _bruto_fr(45) + _HECHO_FR,
    "Une gélule par jour avec 175 à 235 ml d'eau, ou selon l'avis d'un "
    "professionnel de santé.")

CUERPOS_EN["greens-superfood"] = ficha_en(
    "A powder of concentrated vegetables, algae, fruits and roots, taken once "
    "a day dissolved in water. It brings together more than twenty plant "
    "ingredients with no artificial additives.",
    "Barley grass (leaf), broccoli (leaf), spirulina (whole plant), green tea "
    "(leaf), alfalfa extract, wheatgrass (leaf), beetroot (root), hibiscus "
    "(flower), strawberry juice, cranberry, açaí juice, blueberry extract, "
    "pomegranate, cinnamon (bark), turmeric extract (root), <em>Panax</em> "
    "ginseng (root), ashwagandha (root), mangosteen extract (pericarp), black "
    "pepper extract (fruit), inulin (Jerusalem artichoke root), ginger (root) "
    "and sodium alginate.",
    "<li><strong>126 g</strong> of powder</li>\n"
    + _bruto_en(181) + _HECHO_EN,
    "One scoop a day dissolved in 175–235 ml of cold water or the drink of "
    "your choice. Drink it within ten minutes of mixing.")
CUERPOS_FR["greens-superfood"] = ficha_fr(
    "Poudre de légumes, d'algues, de fruits et de racines concentrés, à "
    "prendre une fois par jour dans de l'eau. Elle réunit plus de vingt "
    "ingrédients végétaux sans additifs artificiels.",
    "Herbe d'orge (feuille), brocoli (feuille), spiruline (plante entière), "
    "thé vert (feuille), extrait de luzerne, herbe de blé (feuille), betterave "
    "(racine), hibiscus (fleur), jus de fraise, canneberge, jus d'açaï, "
    "extrait de myrtille, grenade, cannelle (écorce), extrait de curcuma "
    "(racine), ginseng <em>Panax</em> (racine), ashwagandha (racine), extrait "
    "de mangoustan (péricarpe), extrait de poivre noir (fruit), inuline "
    "(racine de topinambour), gingembre (racine) et alginate de sodium.",
    "<li><strong>126 g</strong> de poudre</li>\n"
    + _bruto_fr(181) + _HECHO_FR,
    "Une dosette par jour dissoute dans 175 à 235 ml d'eau froide ou de la "
    "boisson de votre choix. À boire dans les dix minutes qui suivent le "
    "mélange.")

CUERPOS_EN["reds-superfood"] = ficha_en(
    "A powder of red fruits, botanicals and ferments, taken once a day "
    "dissolved in water. The counterpart to the green one: beetroot, berries "
    "and pomegranate, with oat fibre and inulin.",
    "Beetroot (root), strawberry juice, hibiscus (flower), raspberry, "
    "blackcurrant, açaí juice, blueberry extract, cranberry, grape seed "
    "extract, African mango extract (seed), pomegranate, oat fibre, inulin "
    "(Jerusalem artichoke root), nine <em>Lactobacillus</em> and "
    "<em>Bifidobacterium</em> cultures, cinnamon (bark), green tea (leaf), "
    "ginger (root), turmeric (root), shilajit extract, bitter melon extract "
    "(fruit) and black pepper extract (fruit).",
    "<li><strong>120 g</strong> of powder</li>\n"
    + _bruto_en(172) + _HECHO_EN,
    "One scoop a day dissolved in 175–235 ml of cold water or the drink of "
    "your choice. Drink it within ten minutes of mixing.")
CUERPOS_FR["reds-superfood"] = ficha_fr(
    "Poudre de fruits rouges, de plantes et de ferments, à prendre une fois "
    "par jour dans de l'eau. Le pendant de la verte : betterave, baies et "
    "grenade, avec fibre d'avoine et inuline.",
    "Betterave (racine), jus de fraise, hibiscus (fleur), framboise, cassis, "
    "jus d'açaï, extrait de myrtille, canneberge, extrait de pépins de raisin, "
    "extrait de mangue africaine (graine), grenade, fibre d'avoine, inuline "
    "(racine de topinambour), neuf cultures de <em>Lactobacillus</em> et de "
    "<em>Bifidobacterium</em>, cannelle (écorce), thé vert (feuille), "
    "gingembre (racine), curcuma (racine), extrait de shilajit, extrait de "
    "melon amer (fruit) et extrait de poivre noir (fruit).",
    "<li><strong>120 g</strong> de poudre</li>\n"
    + _bruto_fr(172) + _HECHO_FR,
    "Une dosette par jour dissoute dans 175 à 235 ml d'eau froide ou de la "
    "boisson de votre choix. À boire dans les dix minutes qui suivent le "
    "mélange.")

CUERPOS_EN["advanced-100-whey-protein-isolate-chocolate"] = ficha_en(
    "100 % whey protein isolate, chocolate flavour, with <strong>22 g of "
    "protein per serving</strong>. It carries MCT oil powder and apple pectin, "
    "and is sweetened with stevia.",
    "Whey protein isolate, cocoa powder, MCT oil powder, natural flavours, "
    "sunflower lecithin, apple pectin powder, sea salt, stevia leaf extract "
    "and silicon dioxide.",
    "<li><strong>839 g</strong> of powder · chocolate flavour</li>\n"
    "<li>22 g of protein per serving</li>\n"
    + _bruto_en(910) + _HECHO_EN,
    "Two scoops a day dissolved in 175–235 ml of water or the drink of your "
    "choice.")
CUERPOS_FR["advanced-100-whey-protein-isolate-chocolate"] = ficha_fr(
    "Isolat de protéine de lactosérum à 100 %, saveur chocolat, avec "
    "<strong>22 g de protéines par prise</strong>. Il contient de l'huile TCM "
    "en poudre et de la pectine de pomme, et il est sucré à la stévia.",
    "Isolat de protéine de lactosérum, cacao en poudre, huile TCM en poudre, "
    "arômes naturels, lécithine de tournesol, pectine de pomme en poudre, sel "
    "marin, extrait de stévia (feuille) et dioxyde de silicium.",
    "<li><strong>839 g</strong> de poudre · saveur chocolat</li>\n"
    "<li>22 g de protéines par prise</li>\n"
    + _bruto_fr(910) + _HECHO_FR,
    "Deux dosettes par jour dissoutes dans 175 à 235 ml d'eau ou de la boisson "
    "de votre choix.")

CUERPOS_EN["plant-protein-vanilla"] = ficha_en(
    "Plant-based protein with vanilla flavour and <strong>20 g of protein per "
    "serving</strong>, with a complete essential amino acid profile. "
    "<strong>No dairy, no soy and no gluten</strong>: the alternative for when "
    "whey does not sit well.",
    "Fava bean protein isolate, natural flavours, YESTEIN™ fermented "
    "nutritional yeast protein, MCT oil powder, apple pectin powder, sea salt, "
    "stevia leaf extract and silicon dioxide.",
    "<li><strong>844 g</strong> of powder · vanilla flavour</li>\n"
    "<li>20 g of protein and 110 kcal per serving</li>\n"
    + _bruto_en(910) + _HECHO_EN,
    "Two scoops a day dissolved in 175–235 ml of water or the drink of your "
    "choice.")
CUERPOS_FR["plant-protein-vanilla"] = ficha_fr(
    "Protéine d'origine végétale à la vanille, avec <strong>20 g de protéines "
    "par prise</strong> et un profil complet en acides aminés essentiels. "
    "<strong>Sans lactose, sans soja et sans gluten</strong> : l'alternative "
    "quand le lactosérum ne passe pas.",
    "Isolat de protéine de fève, arômes naturels, protéine de levure "
    "nutritionnelle fermentée YESTEIN™, huile TCM en poudre, pectine de pomme "
    "en poudre, sel marin, extrait de stévia (feuille) et dioxyde de silicium.",
    "<li><strong>844 g</strong> de poudre · saveur vanille</li>\n"
    "<li>20 g de protéines et 110 kcal par prise</li>\n"
    + _bruto_fr(910) + _HECHO_FR,
    "Deux dosettes par jour dissoutes dans 175 à 235 ml d'eau ou de la boisson "
    "de votre choix.")

CUERPOS_EN["bcaa-post-workout-powder-honeydew-watermelon"] = ficha_en(
    "A powder with <strong>5000 mg of branched-chain amino acids</strong> in a "
    "2:1:1 ratio — two parts leucine to one of isoleucine and one of valine — "
    "plus glutamine. Honeydew and watermelon flavour.",
    "Vitamin B6 (as pyridoxine hydrochloride), L-glutamine, BCAA 2:1:1, citric "
    "acid, honeydew and watermelon flavours, potassium citrate, silicon "
    "dioxide, sucralose, sea salt, beetroot powder (colour), grape skin "
    "extract (colour) and acesulfame potassium.",
    "<li><strong>292 g</strong> of powder · honeydew and watermelon</li>\n"
    + _bruto_en(408) + _HECHO_EN,
    "Half a scoop (6.5 g) dissolved in 235–295 ml of a cold drink. It takes a "
    "few minutes to dissolve fully. Before training, after, or between meals.")
CUERPOS_FR["bcaa-post-workout-powder-honeydew-watermelon"] = ficha_fr(
    "Poudre apportant <strong>5000 mg d'acides aminés ramifiés</strong> en "
    "proportion 2:1:1 — deux parts de leucine pour une d'isoleucine et une de "
    "valine — plus de la glutamine. Saveur melon et pastèque.",
    "Vitamine B6 (sous forme de chlorhydrate de pyridoxine), L-glutamine, BCAA "
    "2:1:1, acide citrique, arômes de melon et de pastèque, citrate de "
    "potassium, dioxyde de silicium, sucralose, sel marin, betterave en poudre "
    "(colorant), extrait de peau de raisin (colorant) et acésulfame de "
    "potassium.",
    "<li><strong>292 g</strong> de poudre · melon et pastèque</li>\n"
    + _bruto_fr(408) + _HECHO_FR,
    "Une demi-dosette (6,5 g) dissoute dans 235 à 295 ml de boisson froide. "
    "Elle met quelques minutes à se dissoudre entièrement. Avant "
    "l'entraînement, après, ou entre les repas.")

CUERPOS_EN["methylene-blue-drops"] = ficha_en(
    "Methylene blue in drops, with <strong>10 mg per serving</strong>. Liquid "
    "format with a dropper, three ingredients.",
    "Methylene blue powder (10 mg), water and potassium sorbate.",
    "<li><strong>60 ml</strong> · bottle with dropper</li>\n"
    + _bruto_en(77) + _HECHO_EN,
    "Shake before use. Adults: 1 ml (20 drops) a day by mouth, preferably in "
    "the morning, straight or added to a drink.")
CUERPOS_FR["methylene-blue-drops"] = ficha_fr(
    "Bleu de méthylène en gouttes, à <strong>10 mg par prise</strong>. Format "
    "liquide avec compte-gouttes, trois ingrédients.",
    "Bleu de méthylène en poudre (10 mg), eau et sorbate de potassium.",
    "<li><strong>60 ml</strong> · flacon compte-gouttes</li>\n"
    + _bruto_fr(77) + _HECHO_FR,
    "Agiter avant emploi. Adultes : 1 ml (20 gouttes) par jour par voie orale, "
    "de préférence le matin, pur ou ajouté à une boisson.")

CUERPOS_EN["nitric-shock-pre-workout-powder-fruit-punch"] = ficha_en(
    "Pre-workout powder with fruit punch flavour. It brings together "
    "<strong>twenty-three ingredients</strong>: creatine, arginine AKG, "
    "beta-alanine, taurine, caffeine, L-tyrosine, 290 mg of electrolytes and a "
    "B-vitamin complex.",
    "Sodium (sodium citrate), potassium (potassium citrate), vitamins B1, B2, "
    "B3, B6 and B12, folic acid, pantothenic acid, calcium and phosphorus "
    "(dicalcium phosphate), magnesium (magnesium oxide), chromium (chromium "
    "nicotinate), dicreatine malate, L-arginine alpha-ketoglutarate, "
    "beta-alanine, caffeine and a matrix of L-taurine, anhydrous betaine, waxy "
    "maize, citrulline malate, glycocyamine, glucuronolactone, L-tyrosine, "
    "maltodextrin, citric acid, fruit punch flavour, dextrose, sucralose and "
    "silicon dioxide.",
    "<li><strong>300 g</strong> of powder · fruit punch flavour</li>\n"
    + _bruto_en(408) + _HECHO_EN,
    "Start with one scoop in 175–235 ml of a cold drink to check tolerance. If "
    "it agrees with you, one to two scoops thirty minutes before training. "
    "<strong>Do not go beyond two scoops a day.</strong>")
CUERPOS_FR["nitric-shock-pre-workout-powder-fruit-punch"] = ficha_fr(
    "Pré-entraînement en poudre saveur punch aux fruits. Il réunit "
    "<strong>vingt-trois ingrédients</strong> : créatine, arginine AKG, "
    "bêta-alanine, taurine, caféine, L-tyrosine, 290 mg d'électrolytes et un "
    "complexe de vitamines du groupe B.",
    "Sodium (citrate de sodium), potassium (citrate de potassium), vitamines "
    "B1, B2, B3, B6 et B12, acide folique, acide pantothénique, calcium et "
    "phosphore (phosphate dicalcique), magnésium (oxyde de magnésium), chrome "
    "(nicotinate de chrome), dicréatine malate, alpha-cétoglutarate de "
    "L-arginine, bêta-alanine, caféine et une matrice de L-taurine, bétaïne "
    "anhydre, maïs cireux, citrulline malate, glycocyamine, glucuronolactone, "
    "L-tyrosine, maltodextrine, acide citrique, arôme de punch aux fruits, "
    "dextrose, sucralose et dioxyde de silicium.",
    "<li><strong>300 g</strong> de poudre · saveur punch aux fruits</li>\n"
    + _bruto_fr(408) + _HECHO_FR,
    "Commencez par une dosette dans 175 à 235 ml de boisson froide pour "
    "vérifier la tolérance. Si elle passe bien, une à deux dosettes trente "
    "minutes avant l'entraînement. <strong>Ne pas dépasser deux dosettes par "
    "jour.</strong>")


# El riesgo de traducir fichas de suplementos no es la gramática: es que se
# cuele por descuido una declaración de salud del texto del proveedor. Estas
# son las que traía el original inglés que descartamos. Se miran solo en la
# parte redactada, porque el aviso legal contiene «cure» y «healthy» a
# propósito y es justo lo que debe decir.
PROHIBIDAS_EN = ("boost", "anti-aging", "anti aging", "immune support",
                 "supports immunity", "burns fat", "burn fat", "detox",
                 "increases energy", "improves health", "clinically proven")
PROHIBIDAS_FR = ("stimule", "anti-âge", "renforce l'immunité", "brûle les "
                 "graisses", "détox", "améliore la santé", "cliniquement "
                 "prouvé", "augmente l'énergie")


def _redactado(cuerpo: str, lengua: str) -> str:
    corte = "<h3>Warnings</h3>" if lengua == "en" else "<h3>Avertissements</h3>"
    return cuerpo.split(corte)[0].lower()


def comprobar() -> list:
    """Handles que no existen, lenguas descuadradas y promesas de salud."""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import catalogo as c

    malos = []
    for lengua, cuerpos, prohibidas in (("en", CUERPOS_EN, PROHIBIDAS_EN),
                                        ("fr", CUERPOS_FR, PROHIBIDAS_FR)):
        for handle, cuerpo in cuerpos.items():
            if handle not in c.CUERPOS:
                malos.append(f"{lengua} · {handle} no existe en CUERPOS")
            texto = _redactado(cuerpo, lengua)
            for frase in prohibidas:
                if frase in texto:
                    malos.append(f"{lengua} · {handle} · promesa de salud: "
                                 f"«{frase}»")
            # El aviso de complemento alimenticio solo le toca a los
            # suplementos. Una loseta de espuma no se ingiere.
            if c.FICHAS.get(handle, (None,) * 5)[3] == "suplemento":
                pie = PIE_EN if lengua == "en" else PIE_FR
                if pie not in cuerpo:
                    malos.append(f"{lengua} · {handle} · sin el aviso legal")
    if set(CUERPOS_EN) != set(CUERPOS_FR):
        for h in set(CUERPOS_EN) ^ set(CUERPOS_FR):
            malos.append(f"{h} · traducido a una lengua y no a la otra")
    return malos


def faltan() -> list:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import catalogo as c
    return sorted(set(c.CUERPOS) - set(CUERPOS_EN))




# ---------------------------------------------------------------------------
# Equipo, accesorios, ropa y jabones
# ---------------------------------------------------------------------------
# Estos no llevan aviso de complemento alimenticio, así que usan el otro molde:
# el mismo `art()` del original, con sus dos encabezados.
def art_en(intro, puntos, especificaciones=None, cierre=None):
    t = f"<p>{intro}</p>\n\n<h3>What sets it apart</h3>\n<ul>\n{puntos}</ul>\n"
    if especificaciones:
        t += f"\n<h3>Measurements and materials</h3>\n<ul>\n{especificaciones}</ul>\n"
    if cierre:
        t += f"\n<p>{cierre}</p>"
    return t


def art_fr(intro, puntos, especificaciones=None, cierre=None):
    t = f"<p>{intro}</p>\n\n<h3>Ce qui le distingue</h3>\n<ul>\n{puntos}</ul>\n"
    if especificaciones:
        t += f"\n<h3>Dimensions et matériaux</h3>\n<ul>\n{especificaciones}</ul>\n"
    if cierre:
        t += f"\n<p>{cierre}</p>"
    return t


CUIDADO_EN = ("<em>External use only. In case of contact with the eyes, rinse "
              "thoroughly with clean water. If irritation persists, stop "
              "using it.</em>")
CUIDADO_FR = ("<em>Usage externe. En cas de contact avec les yeux, rincer "
              "abondamment à l'eau claire. Si l'irritation persiste, cesser "
              "l'utilisation.</em>")

EMPLEO_JABON_EN = ("<strong>How to use it:</strong> add warm water to work up a "
                   "dense lather. Let it dry between uses and it will last a "
                   "good deal longer.<br>")
EMPLEO_JABON_FR = ("<strong>Mode d'emploi :</strong> ajoutez de l'eau tiède "
                   "pour obtenir une mousse dense. Laissez-le sécher entre "
                   "deux utilisations et il durera bien plus longtemps.<br>")

_ = CUERPOS_EN.__setitem__
__ = CUERPOS_FR.__setitem__

# --- cajón pliométrico ------------------------------------------------------
h = ("steel-plyo-box-12-18-24-inch-high-anti-slip-pre-assembled-plyometric-"
     "jump-box-for-home-gym-conditioning-and-strength-training-sold-"
     "individually-plyometric-platform-step")
_(h, art_en(
    "Heavy-gauge tubular steel jump box with rubber on top and underneath. "
    "<strong>It arrives assembled</strong>: out of the box and into use. Sold "
    "individually, not as a set.",
    "<li><strong>It does not slip or tip.</strong> The rubber above and below "
    "grips, and the steel frame is heavy enough not to shift.</li>\n"
    "<li><strong>It does more than jumps.</strong> Box jumps, push-ups, dips, "
    "step-ups, agility work and conditioning.</li>\n"
    "<li><strong>Already built.</strong> There are no bolts to tighten.</li>\n",
    "<li><strong>12 inches</strong> · base 38 × 38 cm, surface 32 × 31 cm · "
    "weighs 5.4 kg · rated to 254 kg</li>\n"
    "<li><strong>18 inches</strong> · base 46 × 46 cm, surface 36 × 36 cm · "
    "weighs 7.1 kg · rated to 249 kg</li>\n"
    "<li><strong>24 inches</strong> · base 53 × 53 cm, surface 38 × 38 cm · "
    "weighs 8.5 kg · rated to 234 kg</li>\n"
    "<li>Heavy-gauge tubular steel and rubber</li>\n",
    "The box jump carries a risk worth knowing about: a miss is paid for in "
    "the shin. Start at a height you can step up onto and go higher once the "
    "landing is silent."))
__(h, art_fr(
    "Caisson de saut en acier tubulaire de forte épaisseur, avec du caoutchouc "
    "dessus et dessous. <strong>Il arrive monté</strong> : on le sort du carton "
    "et on s'en sert. Vendu à l'unité, pas en lot.",
    "<li><strong>Il ne glisse pas et ne bascule pas.</strong> Le caoutchouc du "
    "dessus et du dessous accroche, et le châssis en acier pèse assez pour ne "
    "pas bouger.</li>\n"
    "<li><strong>Il sert à plus qu'à sauter.</strong> Sauts sur caisson, "
    "pompes, dips, montées, agilité et travail de conditionnement.</li>\n"
    "<li><strong>Déjà assemblé.</strong> Aucun boulon à serrer.</li>\n",
    "<li><strong>12 pouces</strong> · base 38 × 38 cm, surface 32 × 31 cm · "
    "pèse 5,4 kg · admet jusqu'à 254 kg</li>\n"
    "<li><strong>18 pouces</strong> · base 46 × 46 cm, surface 36 × 36 cm · "
    "pèse 7,1 kg · admet jusqu'à 249 kg</li>\n"
    "<li><strong>24 pouces</strong> · base 53 × 53 cm, surface 38 × 38 cm · "
    "pèse 8,5 kg · admet jusqu'à 234 kg</li>\n"
    "<li>Acier tubulaire de forte épaisseur et caoutchouc</li>\n",
    "Le saut sur caisson comporte un risque qu'il vaut mieux connaître : "
    "l'échec se paie sur le tibia. Commencez par la hauteur que vous pouvez "
    "monter en marchant, et montez quand l'atterrissage est silencieux."))

# --- banco multifunción -----------------------------------------------------
h = ("finer-form-multi-functional-fid-weight-bench-for-full-all-in-one-body-"
     "workout-hyper-back-extension-roman-chair-adjustable-ab-sit-up-bench-"
     "incline-decline-bench-flat-bench")
_(h, art_en(
    "An adjustable bench that works as a <strong>flat, incline and decline "
    "bench</strong>, a roman chair for back extensions, an ab bench and a "
    "preacher bench. Foldable, with wheels.",
    "<li><strong>Five positions in one piece of furniture.</strong> It is the "
    "bench you buy when you have no room for five.</li>\n"
    "<li><strong>It adjusts to the body, not the other way round.</strong> "
    "Eight backrest positions, three seat positions, eight for the support "
    "roller and four for the calves.</li>\n"
    "<li><strong>Real back extensions.</strong> The roman chair position works "
    "the lower back, glutes and core without a second machine.</li>\n"
    "<li><strong>It folds and it moves.</strong> Transport wheels to get it out "
    "of the way.</li>\n",
    "<li>Steel frame</li>\n<li>Folds for storage</li>\n"
    "<li>Transport wheels</li>\n",
    "The maximum capacity is deliberately not stated here: the manufacturer's "
    "own documentation gives four different figures for this model, and we do "
    "not publish a number we cannot stand behind. If you need it for your "
    "case, ask us and we will confirm it with the supplier before you buy."))
__(h, art_fr(
    "Banc réglable qui fait office de <strong>banc plat, incliné et "
    "décliné</strong>, de chaise romaine pour les hyperextensions, de banc "
    "d'abdominaux et de banc de prédicateur. Pliable et sur roulettes.",
    "<li><strong>Cinq positions dans un seul meuble.</strong> C'est le banc "
    "qu'on achète quand on n'a pas la place pour cinq.</li>\n"
    "<li><strong>Il s'ajuste au corps, et non l'inverse.</strong> Huit "
    "positions de dossier, trois d'assise, huit pour le rouleau d'appui et "
    "quatre pour les mollets.</li>\n"
    "<li><strong>De vraies hyperextensions.</strong> La position chaise "
    "romaine travaille les lombaires, le fessier et le tronc sans autre "
    "machine.</li>\n"
    "<li><strong>Il se plie et se déplace.</strong> Roulettes de transport "
    "pour le sortir du passage.</li>\n",
    "<li>Structure en acier</li>\n<li>Se plie pour le rangement</li>\n"
    "<li>Roulettes de transport</li>\n",
    "La charge maximale n'est pas indiquée ici, et c'est volontaire : la "
    "documentation du fabricant donne quatre chiffres différents pour ce "
    "modèle, et nous ne publions pas un nombre que nous ne pouvons pas "
    "soutenir. Si vous en avez besoin, demandez-nous et nous le confirmerons "
    "auprès du fournisseur avant votre achat."))

# --- chaleco lastrado -------------------------------------------------------
h = ("weighted-vest-6lb-8lb-10lb-12lb-15lb-18lb-20lb-24lb-30lb-for-men-women-"
     "reflective-stripe-adjustable-buckle-comfortable-durable-rucking-vest-"
     "for-walking-running-strength-training")
_(h, art_en(
    "Neoprene weighted vest in <strong>eight different weights</strong>, with "
    "a reflective stripe and an adjustable buckle. For walking, running, "
    "rucking and bodyweight work.",
    "<li><strong>Sealed neoprene inside.</strong> It does not chafe and it does "
    "not leak the iron particles of the ballast, which is where cheap vests "
    "fail.</li>\n"
    "<li><strong>It does not bounce.</strong> Thick shoulder pads spread the "
    "pressure, and an elastic band and buckle pull it against the body.</li>\n"
    "<li><strong>The weight goes up gradually.</strong> Eight steps, from 6 to "
    "30 pounds, so you never jump.</li>\n"
    "<li><strong>Reflective stripe</strong>, for going out once the light has "
    "gone.</li>\n",
    "<li>Weights: 6, 8, 10, 12, 15, 18, 24 and 30 pounds (2.7 to 13.6 kg)</li>\n"
    "<li>Neoprene with reinforced double stitching</li>\n"
    "<li>Adjustable buckle and elastic band</li>\n"))
__(h, art_fr(
    "Gilet lesté en néoprène, en <strong>huit poids différents</strong>, avec "
    "bande réfléchissante et boucle réglable. Pour la marche, la course, le "
    "rucking et le travail au poids du corps.",
    "<li><strong>Néoprène scellé à l'intérieur.</strong> Il ne frotte pas et "
    "ne laisse pas échapper les particules de fer du lest, qui est le défaut "
    "des gilets bon marché.</li>\n"
    "<li><strong>Il ne ballotte pas.</strong> Des épaulières épaisses "
    "répartissent la pression, et une bande élastique et une boucle le "
    "plaquent au corps.</li>\n"
    "<li><strong>Le poids monte petit à petit.</strong> Huit paliers, de 6 à "
    "30 livres, pour ne jamais sauter d'étape.</li>\n"
    "<li><strong>Bande réfléchissante</strong>, pour sortir quand la lumière "
    "est tombée.</li>\n",
    "<li>Poids : 6, 8, 10, 12, 15, 18, 24 et 30 livres (de 2,7 à 13,6 kg)</li>\n"
    "<li>Néoprène à coutures doubles renforcées</li>\n"
    "<li>Boucle réglable et bande élastique</li>\n"))

# --- maza de acero ----------------------------------------------------------
h = ("steel-mace-bell-for-strength-training-support-full-body-muscles-shoulder-"
     "grips-forearms-workouts-stretching-5-7-10-15-20-25-30-lb-for-woman-man")
_(h, art_en(
    "<strong>Solid steel</strong> mace with a diamond-knurled handle, in seven "
    "weights. The weight sits at one end, so the effort changes depending on "
    "where the mace is in the arc — that is what makes it different from a "
    "dumbbell.",
    "<li><strong>It works the grip and the shoulder.</strong> Every swing asks "
    "you to stabilise, not just to lift.</li>\n"
    "<li><strong>Diamond knurling</strong>, so it does not slip through the "
    "360-degree turn.</li>\n"
    "<li><strong>Solid steel</strong>, in one piece.</li>\n"
    "<li><strong>Movement in several planes</strong>: squats, lunges, "
    "deadlifts, swings, 360s and overhead press.</li>\n",
    "<li>Weights: 5, 7, 10, 15, 20, 25 and 30 pounds (2.3 to 13.6 kg)</li>\n"
    "<li>Solid steel · diamond-knurled handle</li>\n",
    "Start lighter than you think. A 360 with too heavy a mace ends in the "
    "shoulder or the back of the neck."))
__(h, art_fr(
    "Masse en <strong>acier massif</strong> à manche moleté en losange, en "
    "sept poids. La masse est à une extrémité : l'effort change donc selon "
    "l'endroit du parcours où elle se trouve — c'est ce qui la distingue d'un "
    "haltère.",
    "<li><strong>Elle travaille la prise et l'épaule.</strong> Chaque balancé "
    "demande de stabiliser, pas seulement de soulever.</li>\n"
    "<li><strong>Moletage en losange</strong>, pour qu'elle ne file pas dans "
    "le tour à 360 degrés.</li>\n"
    "<li><strong>Acier massif</strong>, d'une seule pièce.</li>\n"
    "<li><strong>Mouvements dans plusieurs plans</strong> : squats, fentes, "
    "soulevé de terre, balancés, tours à 360 et développé au-dessus de la "
    "tête.</li>\n",
    "<li>Poids : 5, 7, 10, 15, 20, 25 et 30 livres (de 2,3 à 13,6 kg)</li>\n"
    "<li>Acier massif · manche moleté en losange</li>\n",
    "Commencez plus léger que vous ne le pensez. Un tour à 360 avec une masse "
    "trop lourde finit dans l'épaule ou dans la nuque."))

# --- máquina de hip thrust --------------------------------------------------
h = "glute-bridge-plate-loaded-hip-thrust-machine-black-steel-frame-176-37-lb"
_(h, art_en(
    "<strong>Plate-loaded hip thrust machine</strong> with a black steel "
    "frame. It solves the problem of the barbell hip thrust: getting under the "
    "load, setting it and controlling it.",
    "<li><strong>It isolates the glute</strong> with the hip and the spine "
    "supported through the whole range.</li>\n"
    "<li><strong>Articulated backrest</strong> that follows the whole back and "
    "forces you to hinge at the hip, not at the lower back.</li>\n"
    "<li><strong>Industrial-grade restraint belt</strong> and an oversized "
    "foot platform.</li>\n"
    "<li><strong>Double safety mechanism</strong> on both sides, with a bottom "
    "stop.</li>\n"
    "<li><strong>It takes resistance bands</strong> on its anchor points, to "
    "change the resistance curve.</li>\n",
    "<li>Machine weight: 80 kg</li>\n"
    "<li>Maximum load 163 kg · up to four 20 kg plates per side</li>\n"
    "<li>Starting resistance 6.8 kg (the empty carriage)</li>\n"
    "<li>Olympic plates, 5 cm inner diameter</li>\n"
    "<li>Industrial steel with 3 mm walls · double-pivot bearings</li>\n"
    "<li>Home use</li>\n",
    "Plates, bands and collars are <strong>sold separately</strong>."))
__(h, art_fr(
    "<strong>Machine à hip thrust à charge de disques</strong>, châssis en "
    "acier noir. Elle règle le problème du hip thrust à la barre : passer sous "
    "la charge, la placer et la contrôler.",
    "<li><strong>Elle isole le fessier</strong>, hanche et colonne soutenues "
    "sur toute l'amplitude.</li>\n"
    "<li><strong>Dossier articulé</strong> qui accompagne tout le dos et "
    "oblige à charnière depuis la hanche, pas depuis les lombaires.</li>\n"
    "<li><strong>Ceinture de maintien</strong> de qualité industrielle et "
    "plateforme de pieds surdimensionnée.</li>\n"
    "<li><strong>Double mécanisme de sécurité</strong> des deux côtés, avec "
    "butée basse.</li>\n"
    "<li><strong>Elle accepte les bandes élastiques</strong> sur ses ancrages, "
    "pour modifier la courbe de résistance.</li>\n",
    "<li>Poids de la machine : 80 kg</li>\n"
    "<li>Charge maximale 163 kg · jusqu'à quatre disques de 20 kg par "
    "côté</li>\n"
    "<li>Résistance initiale 6,8 kg (le chariot à vide)</li>\n"
    "<li>Disques olympiques de 5 cm de diamètre intérieur</li>\n"
    "<li>Acier industriel de 3 mm d'épaisseur · roulements à double "
    "pivot</li>\n"
    "<li>Usage domestique</li>\n",
    "Les disques, les bandes et les colliers <strong>sont vendus "
    "séparément</strong>."))

# --- step de cardio ---------------------------------------------------------
h = ("gym-exercise-foot-pedal-adjustable-cardio-pedal-exerciser-non-slip-"
     "stable-200kg-load-bearing-portable-fitness-equipment")
_(h, art_en(
    "Aerobic step moulded from <strong>a single piece of ABS</strong>, with "
    "height adjustable through risers. It stores upright against the wall.",
    "<li><strong>Rated to 200 kg.</strong> The single piece, with no joints, "
    "is what gives it that capacity.</li>\n"
    "<li><strong>Anti-slip honeycomb surface</strong> and rubber feet "
    "underneath.</li>\n"
    "<li><strong>Mesh reinforcement column</strong>, which is what sets it "
    "apart from an ordinary step.</li>\n"
    "<li><strong>Three heights.</strong> With the risers fitted it goes to 10, "
    "16 or 21 cm, depending on how they are combined.</li>\n",
    "<li>ABS moulded in one piece</li>\n<li>Rated load: 200 kg</li>\n"
    "<li>Box 46.5 × 30 × 11 cm · gross weight 1.5 kg</li>\n"
    "<li>Includes the step and two risers</li>\n",
    "Tolerance of 1 to 2 cm on the measurements, which are taken by hand."))
__(h, art_fr(
    "Step d'aérobic moulé dans <strong>une seule pièce d'ABS</strong>, hauteur "
    "réglable par cales. Il se range debout contre le mur.",
    "<li><strong>Il admet 200 kg.</strong> C'est la pièce unique, sans "
    "assemblage, qui lui donne cette capacité.</li>\n"
    "<li><strong>Surface en nid d'abeille antidérapante</strong> et patins en "
    "caoutchouc dessous.</li>\n"
    "<li><strong>Colonne de renfort en maille</strong>, ce qui le distingue "
    "d'un step ordinaire.</li>\n"
    "<li><strong>Trois hauteurs.</strong> Avec les cales, il monte à 10, 16 ou "
    "21 cm selon la combinaison.</li>\n",
    "<li>ABS moulé d'une pièce</li>\n<li>Charge admise : 200 kg</li>\n"
    "<li>Carton de 46,5 × 30 × 11 cm · poids brut 1,5 kg</li>\n"
    "<li>Comprend le step et deux cales</li>\n",
    "Tolérance de 1 à 2 cm sur les dimensions, prises à la main."))

# --- losetas de suelo -------------------------------------------------------
h = ("8-16-pcs-foam-fitness-non-slip-yoga-mat-fitness-floor-tile-protection-"
     "pad-fitness-equipment-mat-suitable-for-indoor-fitness")
_(h, art_en(
    "Foam tiles that interlock to cover the floor where you train. They "
    "protect the boards from the weights and cushion knees and elbows.",
    "<li><strong>They interlock without glue</strong> and lift just as easily "
    "when it is time to pack up.</li>\n"
    "<li><strong>Anti-slip surface</strong>, so the tile does not travel with "
    "the exercise.</li>\n"
    "<li><strong>They wipe clean with a cloth.</strong></li>\n"
    "<li><strong>They stack flat</strong> and fit into any gap.</li>\n"
    "<li>Each tile comes with its <strong>edge trim</strong>, so the perimeter "
    "finishes straight.</li>\n",
    "<li>30 × 30 × 1 cm per tile</li>\n"
    "<li>Foam with edge trim included</li>\n"))
__(h, art_fr(
    "Dalles en mousse qui s'emboîtent pour couvrir le sol où vous vous "
    "entraînez. Elles protègent le parquet des charges et amortissent genoux "
    "et coudes.",
    "<li><strong>Elles s'emboîtent sans colle</strong> et se relèvent tout "
    "aussi facilement au moment de ranger.</li>\n"
    "<li><strong>Surface antidérapante</strong>, pour que la dalle ne voyage "
    "pas avec l'exercice.</li>\n"
    "<li><strong>Elles se nettoient d'un coup de chiffon.</strong></li>\n"
    "<li><strong>Elles s'empilent à plat</strong> et tiennent dans n'importe "
    "quel recoin.</li>\n"
    "<li>Chaque dalle est livrée avec sa <strong>bordure de "
    "finition</strong>, pour un périmètre droit.</li>\n",
    "<li>30 × 30 × 1 cm par dalle</li>\n"
    "<li>Mousse avec bordure de finition incluse</li>\n"))

# --- barra hexagonal --------------------------------------------------------
h = "universal-olympic-trap-shrug-bar-500-lb-acity"
_(h, art_en(
    "Tubular steel hex bar for <strong>deadlifts and shrugs</strong>. The "
    "handles sit in a neutral position and the sleeves are raised, which "
    "shortens the range and takes load off the back compared with a straight "
    "bar.",
    "<li><strong>Neutral handles.</strong> Hands at your sides rather than in "
    "front: the hip comes in earlier and the lower back works less.</li>\n"
    "<li><strong>Raised sleeves</strong>, which lift the plate off the floor "
    "and shorten the range.</li>\n"
    "<li><strong>Integrated feet.</strong> It does not scratch the floor and "
    "the bar holds itself up while you load and unload.</li>\n"
    "<li><strong>It takes up little room</strong> stored on edge.</li>\n",
    "<li>127 × 74 × 36 cm · weighs 12.7 kg</li>\n"
    "<li>Maximum recommended load 227 kg (500 pounds)</li>\n"
    "<li>24 cm loadable sleeve · 5 cm Olympic plates</li>\n"
    "<li>Tubular steel</li>\n"))
__(h, art_fr(
    "Barre hexagonale en acier tubulaire pour le <strong>soulevé de terre et "
    "les shrugs</strong>. Les poignées sont en prise neutre et les manchons "
    "surélevés, ce qui raccourcit l'amplitude et soulage le dos par rapport à "
    "une barre droite.",
    "<li><strong>Poignées neutres.</strong> Les mains le long du corps et non "
    "devant : la hanche entre plus tôt et les lombaires travaillent "
    "moins.</li>\n"
    "<li><strong>Manchons surélevés</strong>, qui décollent le disque du sol "
    "et raccourcissent l'amplitude.</li>\n"
    "<li><strong>Pieds intégrés.</strong> Elle ne raye pas le sol et tient "
    "seule pendant que vous chargez et déchargez.</li>\n"
    "<li><strong>Peu encombrante</strong> rangée sur la tranche.</li>\n",
    "<li>127 × 74 × 36 cm · pèse 12,7 kg</li>\n"
    "<li>Charge maximale recommandée 227 kg (500 livres)</li>\n"
    "<li>Manchon chargeable de 24 cm · disques olympiques de 5 cm</li>\n"
    "<li>Acier tubulaire</li>\n"))

# --- bandas con tobilleras --------------------------------------------------
h = ("ankle-resistance-bands-with-cuffs-for-women-men-3-level-adjustable-leg-"
     "glute-workout-equipment-portable-home-gym-exercise-bands-for-kickbacks-"
     "hip-thrusts-yoga-strength-training")
_(h, art_en(
    "TPE resistance bands with <strong>padded ankle cuffs</strong> and three "
    "resistance levels. For glute kickbacks, bridges, abductions and leg "
    "extensions.",
    "<li><strong>Padded velcro cuffs</strong>: they do not dig in and they do "
    "not slide down mid-set.</li>\n"
    "<li><strong>TPE with good elasticity</strong>, which returns to shape and "
    "does not crack the way cheap latex does.</li>\n"
    "<li><strong>Three resistances</strong>, to move up once the set stops "
    "costing you.</li>\n"
    "<li><strong>They fit in any bag.</strong> This is the equipment you "
    "actually travel with.</li>\n",
    "<li>TPE material</li>\n<li>Three resistance levels</li>\n"
    "<li>Padded cuffs with velcro fastening</li>\n"))
__(h, art_fr(
    "Bandes élastiques en TPE avec <strong>chevillères rembourrées</strong> et "
    "trois niveaux de résistance. Pour les extensions de fessier, les ponts, "
    "les abductions et les extensions de jambe.",
    "<li><strong>Chevillères rembourrées à velcro</strong> : elles ne "
    "s'incrustent pas et ne glissent pas au milieu de la série.</li>\n"
    "<li><strong>TPE bien élastique</strong>, qui reprend sa forme et ne se "
    "craquelle pas comme le latex bon marché.</li>\n"
    "<li><strong>Trois résistances</strong>, pour monter quand la série cesse "
    "de coûter.</li>\n"
    "<li><strong>Elles tiennent dans n'importe quel sac.</strong> C'est "
    "l'équipement qu'on emporte vraiment en voyage.</li>\n",
    "<li>Matière TPE</li>\n<li>Trois niveaux de résistance</li>\n"
    "<li>Chevillères rembourrées à fermeture velcro</li>\n"))

# --- entrenador respiratorio ------------------------------------------------
h = "portable-breathing-trainer-with-adjustable-resistance-settings"
_(h, art_en(
    "Portable breathing trainer with <strong>adjustable resistance</strong>. "
    "You breathe through the device, which resists both on the way in and on "
    "the way out.",
    "<li><strong>Adjustable resistance</strong>: several levels, to start "
    "gently and move up once it costs less.</li>\n"
    "<li><strong>It works the breathing muscles.</strong> The effort comes "
    "from the level you choose, not from the device.</li>\n"
    "<li><strong>It fits in a pocket.</strong></li>\n"
    "<li><strong>For people who use their air</strong>: swimmers, singers, "
    "wind players and anyone training endurance.</li>\n",
    "<li>Non-toxic plastic</li>\n<li>Adjustable resistance</li>\n",
    "It is not a medical device and it does not treat any respiratory "
    "condition. If you have asthma, COPD or any lung problem, talk to your "
    "doctor before using it."))
__(h, art_fr(
    "Entraîneur respiratoire portable à <strong>résistance réglable</strong>. "
    "On respire à travers l'appareil, qui oppose une résistance à "
    "l'inspiration comme à l'expiration.",
    "<li><strong>Résistance réglable</strong> : plusieurs niveaux, pour "
    "commencer en douceur et monter quand cela coûte moins.</li>\n"
    "<li><strong>Il travaille la musculature respiratoire.</strong> L'effort "
    "vient du niveau choisi, pas de l'appareil.</li>\n"
    "<li><strong>Il tient dans une poche.</strong></li>\n"
    "<li><strong>Pour qui se sert de son air</strong> : nageurs, chanteurs, "
    "instrumentistes à vent et toute personne qui travaille l'endurance.</li>\n",
    "<li>Plastique non toxique</li>\n<li>Résistance réglable</li>\n",
    "Ce n'est pas un dispositif médical et il ne traite aucune affection "
    "respiratoire. En cas d'asthme, de BPCO ou de tout problème pulmonaire, "
    "consultez votre médecin avant de l'utiliser."))

# --- mochila ----------------------------------------------------------------
h = ("sport-basketball-backpack-travel-outdoor-waterproof-swimming-fitness-"
     "travel-sports-bag-basketball-pouch-hiking-climbing-backpack")
_(h, art_en(
    "Waterproof nylon sports backpack of <strong>under twenty litres</strong>, "
    "with a compartment for the ball. Exactly the size for the gym, the pool "
    "or a day out.",
    "<li><strong>Deliberately compact.</strong> It holds what you need and "
    "does not invite you to carry more.</li>\n"
    "<li><strong>Hard-wearing nylon</strong>, treated to take rain and "
    "damp.</li>\n"
    "<li><strong>Ball compartment</strong>, which also takes shoes or wet "
    "clothes.</li>\n"
    "<li>Unisex cut.</li>\n",
    "<li>Capacity under 20 litres</li>\n<li>Waterproof nylon</li>\n"))
__(h, art_fr(
    "Sac à dos de sport en nylon imperméable de <strong>moins de vingt "
    "litres</strong>, avec un compartiment pour le ballon. Juste la taille "
    "qu'il faut pour la salle, la piscine ou une sortie à la journée.",
    "<li><strong>Compact à dessein.</strong> Il contient le nécessaire et "
    "n'invite pas à charger davantage.</li>\n"
    "<li><strong>Nylon résistant</strong>, traité pour supporter la pluie et "
    "l'humidité.</li>\n"
    "<li><strong>Compartiment ballon</strong>, qui sert aussi pour les "
    "chaussures ou les vêtements mouillés.</li>\n"
    "<li>Coupe unisexe.</li>\n",
    "<li>Capacité inférieure à 20 litres</li>\n<li>Nylon imperméable</li>\n"))

# --- cinturón de cuero ------------------------------------------------------
h = ("weight-lifting-belt-premium-4-wide-functional-fitness-belt-for-men-women-"
     "squat-deadlift-support")
_(h, art_en(
    "<strong>Genuine four-inch leather belt</strong> (about 10 cm), already "
    "broken in, for squats and deadlifts. There is nothing to tame: you can "
    "use it on day one.",
    "<li><strong>Leather already broken in.</strong> Most leather belts ask "
    "for weeks of use before they stop digging in.</li>\n"
    "<li><strong>Double prong and reinforced stitching.</strong> The point "
    "where a belt gives way is always the buckle.</li>\n"
    "<li><strong>Suede lining</strong>, soft against the skin.</li>\n"
    "<li><strong>Constant width</strong>, so the pressure is spread around the "
    "whole waist.</li>\n",
    "<li>100 % leather · 10 cm wide</li>\n<li>Double-prong buckle</li>\n"
    "<li>Suede lining</li>\n",
    "A belt does not replace technique or a strong core: it gives you "
    "something to push against once the load is already heavy."))
__(h, art_fr(
    "<strong>Ceinture en cuir véritable de quatre pouces</strong> (environ "
    "10 cm), déjà assouplie, pour le squat et le soulevé de terre. Rien à "
    "roder : elle s'utilise dès le premier jour.",
    "<li><strong>Cuir déjà assoupli.</strong> La plupart des ceintures en cuir "
    "réclament des semaines d'usage avant de cesser de rentrer dans la "
    "peau.</li>\n"
    "<li><strong>Double ardillon et couture renforcée.</strong> L'endroit où "
    "une ceinture cède, c'est toujours la boucle.</li>\n"
    "<li><strong>Intérieur en daim</strong>, doux contre la peau.</li>\n"
    "<li><strong>Largeur constante</strong>, pour une pression répartie sur "
    "tout le tour.</li>\n",
    "<li>Cuir 100 % · 10 cm de large</li>\n<li>Boucle à double ardillon</li>\n"
    "<li>Intérieur en daim</li>\n",
    "Une ceinture ne remplace ni la technique ni un tronc solide : elle donne "
    "quelque chose contre quoi pousser quand la charge est déjà lourde."))

# --- soporte de móvil -------------------------------------------------------
h = ("power-rack-phone-mount-hook-on-smartphone-holder-for-2-2-3-3-squat-rack-"
     "upright-tool-free-installation-vertical-horizontal-viewing-fits-phones-"
     "up-to-3-22-wide")
_(h, art_en(
    "A mount that hooks onto the upright of the power rack <strong>with no "
    "tools</strong>. It puts your phone at eye level while you train.",
    "<li><strong>On and off in one movement.</strong> No screws, no "
    "clamps.</li>\n"
    "<li><strong>It fits most racks</strong> with holes 16 to 25 mm "
    "across.</li>\n"
    "<li><strong>Anti-slip pads</strong> included, so the phone does not shift "
    "between sets.</li>\n"
    "<li><strong>Mesh bag</strong> for carrying it in your backpack.</li>\n",
    "<li>Two sizes: for 2×2 and 3×3 inch uprights</li>\n"
    "<li>8.2 cm inner width: most phones, with a thin case</li>\n"
    "<li>Rack holes from 5/8 to 1 inch</li>\n",
    "Measure the width of your phone before ordering. If your rack is 2×3 "
    "inches, pick the closest size. It holds in landscape, but vertical is "
    "recommended."))
__(h, art_fr(
    "Support qui s'accroche au montant de la cage à squat <strong>sans "
    "outils</strong>. Il place le téléphone à hauteur des yeux pendant "
    "l'entraînement.",
    "<li><strong>On l'accroche et on le retire d'un geste.</strong> Ni vis ni "
    "colliers.</li>\n"
    "<li><strong>Il s'adapte à la plupart des cages</strong> à trous de 16 à "
    "25 mm de diamètre.</li>\n"
    "<li><strong>Patins antidérapants</strong> inclus, pour que le téléphone "
    "ne bouge pas entre les séries.</li>\n"
    "<li><strong>Pochette en filet</strong> pour l'emporter dans le sac.</li>\n",
    "<li>Deux tailles : pour montants de 2×2 et de 3×3 pouces</li>\n"
    "<li>Largeur intérieure de 8,2 cm : la plupart des téléphones, avec une "
    "coque fine</li>\n"
    "<li>Trous de cage de 5/8 à 1 pouce</li>\n",
    "Mesurez la largeur de votre téléphone avant de commander. Si votre cage "
    "est en 2×3 pouces, choisissez la taille la plus proche. À l'horizontale "
    "il tient, mais la verticale est recommandée."))

# --- short de talle alto ----------------------------------------------------
h = ("yoga-shorts-cross-border-honey-buttocks-buttocks-sports-high-waist-"
     "abdomen-stretch-tight-fitting-anti-glare-quick-drying-fitness")
_(h, art_en(
    "<strong>High-waisted</strong> sport shorts in a stretch fabric that holds "
    "the abdomen without squeezing. They do not go see-through when you bend.",
    "<li><strong>High waist</strong>, which stays where you put it.</li>\n"
    "<li><strong>They do not go see-through</strong> in the squat or on the "
    "floor.</li>\n"
    "<li><strong>Quick drying.</strong></li>\n"
    "<li><strong>Light</strong>: 85 grams the garment.</li>\n",
    "<li>Polyester, spandex and nylon</li>\n<li>Sizes M and L</li>\n"
    "<li>85 g per garment (±5 g)</li>\n",
    "<strong>Care:</strong> wash before first use. Hand washing and air drying "
    "are best; in the machine, use a mesh bag, cold water and similar colours, "
    "and dry flat."))
__(h, art_fr(
    "Short de sport <strong>taille haute</strong> en tissu extensible, qui "
    "maintient le ventre sans serrer. Il ne devient pas transparent quand on "
    "se penche.",
    "<li><strong>Taille haute</strong>, qui reste là où on la met.</li>\n"
    "<li><strong>Il ne devient pas transparent</strong> au squat ni au "
    "sol.</li>\n"
    "<li><strong>Séchage rapide.</strong></li>\n"
    "<li><strong>Léger</strong> : 85 grammes le vêtement.</li>\n",
    "<li>Polyester, élasthanne et nylon</li>\n<li>Tailles M et L</li>\n"
    "<li>85 g par vêtement (±5 g)</li>\n",
    "<strong>Entretien :</strong> laver avant la première utilisation. De "
    "préférence à la main et séchage à l'air ; en machine, dans un filet, à "
    "l'eau froide et avec des couleurs proches, puis séchage à plat."))

# --- short sin costuras -----------------------------------------------------
h = ("yoga-shorts-women-fitness-elastic-running-workout-short-leggings-for-"
     "ladies-gym-sport-shorts-fitness-sportwear")
_(h, art_en(
    "Women's sport shorts in a <strong>seamless</strong> fabric with four-way "
    "stretch. The waist compresses and the cut follows the shape of the leg.",
    "<li><strong>Seamless.</strong> Continuous knit: nothing to rub on the "
    "inner thigh.</li>\n"
    "<li><strong>Four-way stretch</strong>, so it follows the movement instead "
    "of fighting it.</li>\n"
    "<li><strong>Compressive waistband</strong>, which does not roll.</li>\n"
    "<li><strong>It moves moisture away and dries fast.</strong></li>\n",
    "<li>Nylon and spandex</li>\n<li>Sizes S, M and L · black</li>\n",
    "Tolerance of 1 to 3 cm on the measurements, taken by hand."))
__(h, art_fr(
    "Short de sport femme en tissu <strong>sans coutures</strong>, extensible "
    "dans les quatre sens. La taille comprime et la coupe suit la forme de la "
    "jambe.",
    "<li><strong>Sans coutures.</strong> Tricot continu : rien qui frotte à "
    "l'intérieur de la cuisse.</li>\n"
    "<li><strong>Extensible dans quatre directions</strong>, il accompagne "
    "donc le mouvement au lieu de le freiner.</li>\n"
    "<li><strong>Ceinture compressive</strong>, qui ne roule pas.</li>\n"
    "<li><strong>Il évacue l'humidité et sèche vite.</strong></li>\n",
    "<li>Nylon et élasthanne</li>\n<li>Tailles S, M et L · noir</li>\n",
    "Tolérance de 1 à 3 cm sur les dimensions, prises à la main."))

# --- camiseta DryBlend ------------------------------------------------------
h = "dryblend®-t-shirt"
_(h, art_en(
    "Classic-fit tee in <strong>DryBlend</strong> fabric, half cotton and half "
    "polyester. The cotton gives the hand and the polyester moves the sweat: "
    "no ring on the back, no fabric stuck to you.",
    "<li><strong>Modern classic fit</strong>, neither loose nor tight.</li>\n"
    "<li><strong>Ribbed collar</strong> of classic width, which does not "
    "stretch out.</li>\n"
    "<li><strong>Taped neck and shoulders</strong>: that is the seam that goes "
    "first on a cheap tee.</li>\n"
    "<li><strong>Tear-away label</strong>, so nothing rubs the back of the "
    "neck.</li>\n",
    "<li>50 % cotton and 50 % polyester</li>\n<li>186 g/m²</li>\n"
    "<li>Made in Honduras</li>\n",
    "The white runs towards bone rather than optical white: that is a property "
    "of the fabric, not a fault in the garment."))
__(h, art_fr(
    "T-shirt de coupe classique en tissu <strong>DryBlend</strong>, moitié "
    "coton, moitié polyester. Le coton donne le toucher et le polyester évacue "
    "la sueur : ni auréole dans le dos, ni tissu collé à la peau.",
    "<li><strong>Coupe classique moderne</strong>, ni ample ni ajustée.</li>\n"
    "<li><strong>Col côtelé</strong> de largeur classique, qui ne se détend "
    "pas.</li>\n"
    "<li><strong>Col et épaules renforcés par un ruban</strong> : c'est la "
    "couture qui lâche en premier sur un t-shirt bon marché.</li>\n"
    "<li><strong>Étiquette détachable</strong>, pour que rien ne frotte la "
    "nuque.</li>\n",
    "<li>50 % coton et 50 % polyester</li>\n<li>186 g/m²</li>\n"
    "<li>Confectionné au Honduras</li>\n",
    "Le blanc tire vers l'os plutôt que vers le blanc optique : c'est une "
    "propriété du tissu, pas un défaut du vêtement."))

# --- maillot unisex ---------------------------------------------------------
h = "unisex-sports-jersey"
_(h, art_en(
    "Unisex jersey in <strong>polyester mesh</strong>, relaxed cut and extra "
    "length. The mesh ventilates where an ordinary tee sticks.",
    "<li><strong>Breathable mesh</strong> in 100 % polyester.</li>\n"
    "<li><strong>Extra length</strong>, which covers below the waist and does "
    "not ride up when you raise your arms.</li>\n"
    "<li><strong>Short raglan sleeve</strong>, with no shoulder seam.</li>\n"
    "<li><strong>Side seam</strong> and <strong>bound collar</strong>, which "
    "is what survives the wash.</li>\n",
    "<li>100 % polyester mesh</li>\n<li>140 g/m²</li>\n"
    "<li>Relaxed unisex cut · classic crew neck</li>\n"
    "<li>Made in China</li>\n",
    "Adult garment. Two-year guarantee in the EU. It meets the requirements "
    "for flammability and for cadmium, bisphenol and phthalate content."))
__(h, art_fr(
    "Maillot unisexe en <strong>mesh de polyester</strong>, coupe ample et "
    "longueur étendue. Le mesh ventile là où un t-shirt ordinaire colle.",
    "<li><strong>Mesh respirant</strong> en 100 % polyester.</li>\n"
    "<li><strong>Longueur étendue</strong>, qui couvre sous la taille et ne "
    "remonte pas quand on lève les bras.</li>\n"
    "<li><strong>Manche raglan courte</strong>, sans couture d'épaule.</li>\n"
    "<li><strong>Couture latérale</strong> et <strong>col bordé</strong>, ce "
    "qui résiste au lavage.</li>\n",
    "<li>100 % polyester en mesh</li>\n<li>140 g/m²</li>\n"
    "<li>Coupe ample unisexe · col rond classique</li>\n"
    "<li>Confectionné en Chine</li>\n",
    "Vêtement pour adultes. Deux ans de garantie dans l'UE. Il satisfait aux "
    "exigences d'inflammabilité et de teneur en cadmium, bisphénols et "
    "phtalates."))

# --- jabón de carbón --------------------------------------------------------
h = "charcoal-soap"
_(h, art_en(
    "Handmade soap with <strong>activated charcoal</strong>, peppermint "
    "essential oil and tea tree essential oil. For face and body, in bar form "
    "and with no plastic packaging.",
    "<li><strong>It does not stain.</strong> The proportion of charcoal is set "
    "to clean without leaving a grey trace on the skin or the towel.</li>\n"
    "<li><strong>Deep cleaning</strong> of pores and of what the day leaves "
    "behind.</li>\n"
    "<li><strong>Peppermint and tea tree</strong>: a scent that clears the "
    "head, for the morning shower or the one after training.</li>\n"
    "<li><strong>Fair trade oils</strong> and sustainable palm.</li>\n",
    "<li>113 g per bar · gross weight 122 g</li>\n"
    "<li>Saponified organic palm, coconut, sunflower and extra virgin olive "
    "oils; peppermint essential oil; tea tree essential oil; activated "
    "charcoal</li>\n"
    "<li>Made in the United States</li>\n",
    EMPLEO_JABON_EN + CUIDADO_EN))
__(h, art_fr(
    "Savon artisanal au <strong>charbon actif</strong>, à l'huile essentielle "
    "de menthe poivrée et à celle d'arbre à thé. Pour le visage et le corps, "
    "en pain et sans emballage plastique.",
    "<li><strong>Il ne tache pas.</strong> La proportion de charbon est réglée "
    "pour nettoyer sans laisser de trace grise sur la peau ni sur la "
    "serviette.</li>\n"
    "<li><strong>Nettoyage en profondeur</strong> des pores et de ce que la "
    "journée dépose.</li>\n"
    "<li><strong>Menthe poivrée et arbre à thé</strong> : un parfum qui "
    "dégage, pour la douche du matin ou celle d'après l'entraînement.</li>\n"
    "<li><strong>Huiles issues du commerce équitable</strong> et palme "
    "durable.</li>\n",
    "<li>113 g par pain · poids brut 122 g</li>\n"
    "<li>Huiles saponifiées de palme, de coco, de tournesol et d'olive vierge "
    "extra biologiques ; huile essentielle de menthe poivrée ; huile "
    "essentielle d'arbre à thé ; charbon actif</li>\n"
    "<li>Fabriqué aux États-Unis</li>\n",
    EMPLEO_JABON_FR + CUIDADO_FR))

# --- jabón de sándalo -------------------------------------------------------
h = "rich-sandalwood-soap"
_(h, art_en(
    "Handmade <strong>sandalwood</strong> soap, with shea butter among its "
    "saponified oils. Woody scent and a dense lather.",
    "<li><strong>With shea butter</strong>, which is what leaves the skin soft "
    "rather than tight.</li>\n"
    "<li><strong>Suitable for every skin type</strong>, sensitive "
    "included.</li>\n"
    "<li><strong>Sandalwood scent</strong>, deep and woody.</li>\n"
    "<li><strong>Fair trade oils</strong> and sustainable palm.</li>\n",
    "<li>113 g per bar · gross weight 127 g</li>\n"
    "<li>Saponified organic extra virgin olive, palm and coconut oils and shea "
    "butter; fragrance</li>\n"
    "<li>Made in the United States</li>\n",
    EMPLEO_JABON_EN + CUIDADO_EN))
__(h, art_fr(
    "Savon artisanal au <strong>santal</strong>, avec du beurre de karité "
    "parmi ses huiles saponifiées. Parfum boisé et mousse dense.",
    "<li><strong>Au beurre de karité</strong>, c'est ce qui laisse la peau "
    "souple plutôt que tiraillée.</li>\n"
    "<li><strong>Convient à tous les types de peau</strong>, y compris "
    "sensible.</li>\n"
    "<li><strong>Parfum de santal</strong>, profond et boisé.</li>\n"
    "<li><strong>Huiles issues du commerce équitable</strong> et palme "
    "durable.</li>\n",
    "<li>113 g par pain · poids brut 127 g</li>\n"
    "<li>Huiles saponifiées d'olive vierge extra, de palme et de coco et "
    "beurre de karité biologiques ; parfum</li>\n"
    "<li>Fabriqué aux États-Unis</li>\n",
    EMPLEO_JABON_FR + CUIDADO_FR))

del _, __, h


if __name__ == "__main__":
    malos, pendientes = comprobar(), faltan()
    print(f"\n  {len(CUERPOS_EN)} de 29 cuerpos en inglés y francés · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if pendientes:
        print(f"    faltan {len(pendientes)}:")
        for h in pendientes:
            print(f"      {h[:60]}")
    print()
