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
