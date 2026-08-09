#!/usr/bin/env python3
"""
VILLUMINATIONS — SEO del catálogo que no son libros ni planes
-------------------------------------------------------------
Los once productos propios (ocho libros y tres niveles) tienen su ficha
escrita a mano en descripciones.py y fichas_libros.py. Los veintinueve
restantes —suplementos, equipo, ropa y jabones— llegaron de proveedor con la
descripción en inglés y sin nada más: sin metaetiquetas, sin etiquetas, sin
texto alternativo y, catorce de ellos, sin tipo de producto.

Este fichero pone lo que faltaba. No reescribe la descripción del proveedor:
esa es suya y describe su mercancía. Lo que se escribe aquí es lo que ve el
buscador y lo que lee alguien que no puede ver la foto.

Dos reglas al redactar, y conviene respetarlas si se añaden productos:

· Nada de promesas de salud. En un suplemento se dice qué lleva, cuánto y en
  qué formato; no lo que cura, previene o mejora. Un texto de tienda no es un
  prospecto y la ley europea sobre declaraciones de salud es estricta.

· Ninguna cifra que no esté en la ficha del proveedor. Cuando la descripción
  original se contradice —el banco dice 1000 libras en un sitio y 660 en
  otro—, la cifra no se pone.

Medidas: el título de buscador se corta a 60 caracteres y la descripción a
155, que es lo que Google enseña. Se comprueba abajo, no se confía.
"""

MARCA = "VILLUMINATIONS"

# El vendedor de los cuarenta productos. En la tienda había tres valores
# distintos: «Ma boutique» (el que pone Shopify por defecto en francés),
# «VIllumination» (el nombre de la cuenta) y el correcto. Los tres primeros
# salen en la ficha del producto, así que el comprador veía tres marcas.
VENDEDOR = MARCA

# El tipo se escribe siempre, aunque el producto ya traiga uno. Los que venían
# de proveedor lo tenían en inglés y muy fino —«Specialty Supplements»,
# «Post-Workout Recovery», «EMBROIDERY»—, así que la tienda mezclaba dos
# idiomas y catorce categorías para cuarenta productos. El matiz no se pierde:
# vive en las etiquetas, que es donde sirve para filtrar.
TIPOS = {
    "suplemento": "Suplemento",
    "equipo": "Equipo de entrenamiento",
    "ropa": "Ropa deportiva",
    "accesorio": "Accesorio",
    "bano": "Cuidado personal",
}

# handle -> (título de buscador, descripción de buscador, alternativo, familia, etiquetas)
FICHAS = {
    "nad": (
        "NAD+ 500 mg en cápsulas | VILLUMINATIONS",
        "Suplemento de NAD+ con 500 mg de nicotinamida adenina dinucleótido "
        "por toma. Coenzima del metabolismo energético celular.",
        "Bote de NAD+ en cápsulas de VILLUMINATIONS",
        "suplemento", ["suplementos", "NAD+", "cápsulas"],
    ),
    "creatine-hydration-powder": (
        "Creatina con electrolitos en polvo | VILLUMINATIONS",
        "Creatina monohidrato mezclada con electrolitos, en polvo. Pensada "
        "para el entrenamiento de fuerza y las series cortas e intensas.",
        "Bote de creatina con electrolitos en polvo de VILLUMINATIONS",
        "suplemento", ["suplementos", "creatina", "fuerza", "polvo"],
    ),
    "nmn": (
        "NMN 500 mg, pureza 99,9 % | VILLUMINATIONS",
        "Cápsulas de ß-nicotinamida mononucleótido con 500 mg por toma y "
        "pureza del 99,9 %. Precursor del NAD+ en el metabolismo celular.",
        "Bote de NMN en cápsulas de VILLUMINATIONS",
        "suplemento", ["suplementos", "NMN", "cápsulas"],
    ),
    "greens-superfood": (
        "Greens Superfood en polvo | VILLUMINATIONS",
        "Polvo de verduras y plantas con hierba de cebada, espirulina y té "
        "verde. Vitaminas y minerales de origen vegetal en una sola toma.",
        "Bote de Greens Superfood en polvo de VILLUMINATIONS",
        "suplemento", ["suplementos", "verde", "vegetal", "polvo"],
    ),
    "reds-superfood": (
        "Reds Superfood en polvo | VILLUMINATIONS",
        "Polvo de frutas rojas y botánicos con remolacha, fresa e hibisco. "
        "Antioxidantes y fibra de origen vegetal en una sola toma.",
        "Bote de Reds Superfood en polvo de VILLUMINATIONS",
        "suplemento", ["suplementos", "rojo", "vegetal", "polvo"],
    ),
    "advanced-100-whey-protein-isolate-chocolate": (
        "Aislado de proteína de suero, chocolate | VILLUMINATIONS",
        "Proteína de suero aislada al 100 %, sabor chocolate. Para después "
        "de entrenar o para completar la proteína del día.",
        "Bote de aislado de proteína de suero sabor chocolate de VILLUMINATIONS",
        "suplemento", ["suplementos", "proteína", "suero", "chocolate"],
    ),
    "plant-protein-vanilla": (
        "Proteína vegetal sabor vainilla | VILLUMINATIONS",
        "Proteína de origen vegetal con perfil completo de aminoácidos y "
        "sabor a vainilla. Alternativa sin lácteos a la de suero.",
        "Bote de proteína vegetal sabor vainilla de VILLUMINATIONS",
        "suplemento", ["suplementos", "proteína", "vegetal", "vainilla"],
    ),
    "bcaa-post-workout-powder-honeydew-watermelon": (
        "BCAA en polvo, melón y sandía | VILLUMINATIONS",
        "5000 mg de aminoácidos ramificados con glutamina, en proporción "
        "2:1:1. Sabor a melón y sandía, para después de entrenar.",
        "Bote de BCAA en polvo sabor melón y sandía de VILLUMINATIONS",
        "suplemento", ["suplementos", "BCAA", "recuperación", "polvo"],
    ),
    "methylene-blue-drops": (
        "Azul de metileno en gotas, 10 mg | VILLUMINATIONS",
        "Gotas con 10 mg de azul de metileno por toma. Formato líquido, "
        "dosificable con cuentagotas.",
        "Frasco de azul de metileno en gotas de VILLUMINATIONS",
        "suplemento", ["suplementos", "azul de metileno", "gotas"],
    ),
    "nitric-shock-pre-workout-powder-fruit-punch": (
        "Preentreno en polvo, ponche de frutas | VILLUMINATIONS",
        "Preentrenamiento en polvo con sabor a ponche de frutas. Para las "
        "sesiones de primera hora o las de después de un día largo.",
        "Bote de preentrenamiento en polvo sabor ponche de frutas de VILLUMINATIONS",
        "suplemento", ["suplementos", "preentreno", "polvo"],
    ),
    "steel-plyo-box-12-18-24-inch-high-anti-slip-pre-assembled-plyometric-jump-box-for-home-gym-conditioning-and-strength-training-sold-individually-plyometric-platform-step": (
        "Cajón pliométrico de acero antideslizante | VILLUMINATIONS",
        "Cajón de salto de acero, ya montado, con superficie antideslizante "
        "y varias alturas. Para pliometría, step y acondicionamiento.",
        "Cajón pliométrico de acero para saltos, de VILLUMINATIONS",
        "equipo", ["equipo", "pliometría", "salto", "acero"],
    ),
    "finer-form-multi-functional-fid-weight-bench-for-full-all-in-one-body-workout-hyper-back-extension-roman-chair-adjustable-ab-sit-up-bench-incline-decline-bench-flat-bench": (
        "Banco de musculación multifunción | VILLUMINATIONS",
        "Banco regulable plano, inclinado y declinado, con silla romana para "
        "lumbares y abdominales. Plegable y con ruedas de transporte.",
        "Banco de musculación multifunción regulable, de VILLUMINATIONS",
        "equipo", ["equipo", "banco", "musculación"],
    ),
    "sport-basketball-backpack-travel-outdoor-waterproof-swimming-fitness-travel-sports-bag-basketball-pouch-hiking-climbing-backpack": (
        "Mochila deportiva impermeable de 20 L | VILLUMINATIONS",
        "Mochila de nailon impermeable de menos de veinte litros, con hueco "
        "para el balón. Para gimnasio, piscina y salidas de un día.",
        "Mochila deportiva impermeable de nailon, de VILLUMINATIONS",
        "accesorio", ["accesorios", "mochila", "impermeable"],
    ),
    "yoga-shorts-cross-border-honey-buttocks-buttocks-sports-high-waist-abdomen-stretch-tight-fitting-anti-glare-quick-drying-fitness": (
        "Short de yoga de talle alto | VILLUMINATIONS",
        "Short deportivo de talle alto en poliéster, elastano y nailon. "
        "Tejido elástico, de secado rápido y no transparente.",
        "Short de yoga de talle alto, de VILLUMINATIONS",
        "ropa", ["ropa", "yoga", "short", "mujer"],
    ),
    "weight-lifting-belt-premium-4-wide-functional-fitness-belt-for-men-women-squat-deadlift-support": (
        "Cinturón de halterofilia de cuero, 10 cm | VILLUMINATIONS",
        "Cinturón de cuero de cuatro pulgadas, ya ablandado, para sentadilla "
        "y peso muerto. Sujeción lumbar y estabilidad del tronco.",
        "Cinturón de halterofilia de cuero, de VILLUMINATIONS",
        "accesorio", ["accesorios", "cinturón", "fuerza", "cuero"],
    ),
    "weighted-vest-6lb-8lb-10lb-12lb-15lb-18lb-20lb-24lb-30lb-for-men-women-reflective-stripe-adjustable-buckle-comfortable-durable-rucking-vest-for-walking-running-strength-training": (
        "Chaleco lastrado ajustable, 2,7 a 13,6 kg | VILLUMINATIONS",
        "Chaleco con lastre en neopreno, de seis a treinta libras, con banda "
        "reflectante y hebilla regulable. Para andar, correr y rucking.",
        "Chaleco lastrado ajustable con banda reflectante, de VILLUMINATIONS",
        "equipo", ["equipo", "chaleco lastrado", "rucking"],
    ),
    "steel-mace-bell-for-strength-training-support-full-body-muscles-shoulder-grips-forearms-workouts-stretching-5-7-10-15-20-25-30-lb-for-woman-man": (
        "Maza de acero, de 2,3 a 13,6 kg | VILLUMINATIONS",
        "Maza de acero macizo, de cinco a treinta libras. Trabaja el agarre, "
        "la movilidad del hombro y la estabilidad en cada balanceo.",
        "Maza de acero para entrenamiento de fuerza, de VILLUMINATIONS",
        "equipo", ["equipo", "maza", "agarre", "acero"],
    ),
    "yoga-shorts-women-fitness-elastic-running-workout-short-leggings-for-ladies-gym-sport-shorts-fitness-sportwear": (
        "Short de deporte sin costuras para mujer | VILLUMINATIONS",
        "Short de nailon con tejido sin costuras de cuatro direcciones. "
        "Cintura compresiva, ligero, transpirable y de secado rápido.",
        "Short de deporte sin costuras para mujer, de VILLUMINATIONS",
        "ropa", ["ropa", "short", "mujer", "sin costuras"],
    ),
    "glute-bridge-plate-loaded-hip-thrust-machine-black-steel-frame-176-37-lb": (
        "Máquina de hip thrust con discos, 80 kg | VILLUMINATIONS",
        "Máquina de puente de glúteo con carga de discos y estructura de "
        "acero negro. Aísla el glúteo y estabiliza cadera y tronco.",
        "Máquina de hip thrust con carga de discos, de VILLUMINATIONS",
        "equipo", ["equipo", "glúteo", "hip thrust", "máquina"],
    ),
    "gym-exercise-foot-pedal-adjustable-cardio-pedal-exerciser-non-slip-stable-200kg-load-bearing-portable-fitness-equipment": (
        "Stepper de cardio regulable, 200 kg | VILLUMINATIONS",
        "Stepper portátil de ABS moldeado en una pieza, con altura "
        "regulable, base antideslizante y 200 kg de carga admitida.",
        "Stepper de cardio regulable y portátil, de VILLUMINATIONS",
        "equipo", ["equipo", "cardio", "stepper", "portátil"],
    ),
    "8-16-pcs-foam-fitness-non-slip-yoga-mat-fitness-floor-tile-protection-pad-fitness-equipment-mat-suitable-for-indoor-fitness": (
        "Losetas de espuma para suelo de gimnasio | VILLUMINATIONS",
        "Losetas encajables de espuma de 30 × 30 × 1 cm, antideslizantes. "
        "Protegen el suelo y amortiguan las articulaciones.",
        "Losetas de espuma antideslizantes para suelo de gimnasio, de VILLUMINATIONS",
        "equipo", ["equipo", "suelo", "losetas", "espuma"],
    ),
    "universal-olympic-trap-shrug-bar-500-lb-acity": (
        "Barra hexagonal olímpica, 227 kg | VILLUMINATIONS",
        "Barra de trapecio en acero tubular para peso muerto y encogimientos. "
        "Admite 500 libras y ocupa poco en un gimnasio de casa.",
        "Barra hexagonal olímpica de acero, de VILLUMINATIONS",
        "equipo", ["equipo", "barra", "peso muerto", "olímpica"],
    ),
    "power-rack-phone-mount-hook-on-smartphone-holder-for-2-2-3-3-squat-rack-upright-tool-free-installation-vertical-horizontal-viewing-fits-phones-up-to-3-22-wide": (
        "Soporte de móvil para jaula de fuerza | VILLUMINATIONS",
        "Soporte que se engancha al perfil de la jaula sin herramientas. "
        "Vista vertical u horizontal, para móviles de hasta 8 cm de ancho.",
        "Soporte de móvil enganchado a una jaula de fuerza, de VILLUMINATIONS",
        "accesorio", ["accesorios", "jaula", "soporte", "móvil"],
    ),
    "portable-breathing-trainer-with-adjustable-resistance-settings": (
        "Entrenador respiratorio con resistencia | VILLUMINATIONS",
        "Dispositivo portátil de entrenamiento respiratorio con resistencia "
        "regulable. Cabe en un bolsillo.",
        "Entrenador respiratorio portátil con resistencia regulable, de VILLUMINATIONS",
        "equipo", ["equipo", "respiración", "portátil"],
    ),
    "ankle-resistance-bands-with-cuffs-for-women-men-3-level-adjustable-leg-glute-workout-equipment-portable-home-gym-exercise-bands-for-kickbacks-hip-thrusts-yoga-strength-training": (
        "Bandas de resistencia con tobilleras | VILLUMINATIONS",
        "Bandas de TPE con tobilleras y tres niveles de resistencia. Para "
        "patadas de glúteo, hip thrust y abducciones de cadera.",
        "Bandas de resistencia con tobilleras, de VILLUMINATIONS",
        "equipo", ["equipo", "bandas", "glúteo", "portátil"],
    ),
    "dryblend®-t-shirt": (
        "Camiseta DryBlend, algodón y poliéster | VILLUMINATIONS",
        "Camiseta de corte clásico en tejido DryBlend, que aparta la "
        "humedad. Mitad algodón y mitad poliéster.",
        "Camiseta DryBlend de VILLUMINATIONS",
        "ropa", ["ropa", "camiseta", "algodón"],
    ),
    "unisex-sports-jersey": (
        "Camiseta de deporte unisex en malla | VILLUMINATIONS",
        "Camiseta unisex en malla de poliéster transpirable. Corte holgado, "
        "largo extra y ribete en el cuello.",
        "Camiseta de deporte unisex en malla, de VILLUMINATIONS",
        "ropa", ["ropa", "camiseta", "unisex", "malla"],
    ),
    "charcoal-soap": (
        "Jabón artesanal de carbón activado | VILLUMINATIONS",
        "Jabón artesanal con carbón activado, para cara y cuerpo. Limpieza "
        "en pastilla, sin envase de plástico.",
        "Pastilla de jabón artesanal de carbón activado, de VILLUMINATIONS",
        "bano", ["cuidado personal", "jabón", "carbón activado"],
    ),
    "rich-sandalwood-soap": (
        "Jabón artesanal de sándalo | VILLUMINATIONS",
        "Jabón artesanal de sándalo, de aroma amaderado. Apto para todo tipo "
        "de piel, también la sensible.",
        "Pastilla de jabón artesanal de sándalo, de VILLUMINATIONS",
        "bano", ["cuidado personal", "jabón", "sándalo"],
    ),
}

# Las tres colecciones de proveedor. Las dos propias —conocimiento y planes—
# viven en publicar.py, porque allí se crean junto con sus productos. Estas ya
# existían en la tienda vacías: sin descripción, sin SEO y sin alternativo en la
# imagen, que en una página de categoría es justo lo que el buscador lee.
COLECCIONES = {
    "suplementos": (
        "Suplementos deportivos y de bienestar | VILLUMINATIONS",
        "Proteína, creatina, preentreno, verdes y rojos, NAD+ y NMN. Cada ficha "
        "dice qué lleva y cuánto, sin prometer nada sobre tu salud.",
        "Suplementos de VILLUMINATIONS",
    ),
    "equipo": (
        "Equipo de entrenamiento para casa | VILLUMINATIONS",
        "Bancos, barras, cajones pliométricos, chalecos lastrados, bandas y "
        "losetas de suelo. Para montar o completar un gimnasio en casa.",
        "Equipo de entrenamiento de VILLUMINATIONS",
    ),
    "ropa": (
        "Ropa deportiva | VILLUMINATIONS",
        "Camisetas y shorts para entrenar: tejidos que apartan la humedad, sin "
        "costuras y de secado rápido. Corte unisex y de mujer.",
        "Ropa deportiva de VILLUMINATIONS",
    ),
}


# ---------------------------------------------------------------------------
# El cuerpo de la ficha, en castellano
# ---------------------------------------------------------------------------
# Los veintinueve productos de proveedor llegaron con la descripción en inglés,
# en una tienda cuyo idioma primario es el castellano. Google leía un título en
# español y un cuerpo en inglés, que es una señal de mezcla que penaliza.
#
# Esto NO es una traducción del texto del proveedor, y la diferencia importa.
# El original está lleno de declaraciones de salud —«supports cognitive
# wellness», «promotes healthy mitochondrial function», «increase protein
# synthesis»—. Traducirlas habría metido veintinueve fichas de promesas
# prohibidas en la tienda y roto la primera regla de este fichero. Lo que se
# escribe aquí es lo que sí se puede afirmar: qué lleva, cuánto, en qué
# formato, cómo se toma y qué advertencias trae.
#
# Dos productos llevan advertencia propia en vez de la genérica, porque su
# propia documentación lo pide: el azul de metileno, cuya seguridad el
# proveedor declara no determinada y que interacciona con antidepresivos
# serotoninérgicos, y el preentrenamiento, que lleva cafeína y arrastra una
# lista larga de contraindicaciones.
#
# Las traducciones al inglés y al francés están pendientes y hay que
# escribirlas con este mismo criterio. Registrar el texto original del
# proveedor como traducción inglesa devolvería las declaraciones por la puerta
# de atrás.

PIE = ("<p><em>Complemento alimenticio. No sustituye una dieta variada y "
       "equilibrada ni un estilo de vida saludable. Este producto no está "
       "destinado a diagnosticar, tratar, curar ni prevenir ninguna "
       "enfermedad.</em></p>")

AVISO = ("<h3>Advertencias</h3>\n<p>No superar la dosis recomendada. Las "
         "personas embarazadas o en periodo de lactancia, los menores de 18 "
         "años y quienes tengan alguna patología deben consultar con un "
         "profesional sanitario antes de tomarlo. Mantener fuera del alcance "
         "de los niños. No usar si el precinto está roto o ausente. Conservar "
         "en un lugar fresco y seco.</p>")


def ficha(intro, composicion, formato, empleo, aviso=AVISO):
    return (f"<p>{intro}</p>\n\n"
            f"<h3>Composición</h3>\n<p>{composicion}</p>\n\n"
            f"<h3>Formato</h3>\n<ul>\n{formato}</ul>\n\n"
            f"<h3>Modo de empleo</h3>\n<p>{empleo}</p>\n\n"
            f"{aviso}\n{PIE}")


CUERPOS = {
"nad": ficha(
 "Cápsulas con <strong>500 mg de NAD+</strong> (nicotinamida adenina "
 "dinucleótido) por toma, acompañadas de quercetina y resveratrol de origen "
 "vegetal. El NAD+ es una coenzima que participa en el metabolismo energético "
 "de la célula.",
 "NAD+ (nicotinamida adenina dinucleótido) 500 mg; extracto de quercetina "
 "dihidratada <em>(Sophora japonica</em>, botón floral) 250 mg; extracto de "
 "polígono japonés <em>(Polygonum cuspidatum</em>, raíz, 98 % resveratrol) "
 "150 mg. Cápsula vegetal de HPMC, celulosa microcristalina, harina de arroz "
 "integral, aceite de oliva, dióxido de silicio y estearato de magnesio.",
 "<li><strong>60 cápsulas</strong> · 50 g netos</li>\n"
 "<li>Peso bruto 68 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Dos cápsulas al día, con unos 175 ml de agua, o según indique un "
 "profesional sanitario."),

"creatine-hydration-powder": ficha(
 "Polvo que combina <strong>5 g de creatina monohidrato</strong> con "
 "electrolitos —magnesio, sodio y potasio— en cada toma. Sabor a limón, con "
 "estevia y sin colorantes.",
 "Creatina (como creatina monohidrato) 5000 mg; magnesio (como malato de "
 "magnesio) 60 mg; sodio (como sal marina) 1000 mg; potasio (como cloruro "
 "potásico) 200 mg. Aromas naturales, extracto de estevia (hoja) y dióxido "
 "de silicio.",
 "<li><strong>300 g</strong> de polvo · sabor limón</li>\n"
 "<li>Peso bruto 386 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Un cacito (10 g) al día disuelto en 175–235 ml de agua o de la bebida que "
 "prefieras."),

"nmn": ficha(
 "Cápsulas con <strong>500 mg de ß-nicotinamida mononucleótido</strong> "
 "(pureza del 99,9 %) por toma, sin nada más añadido. El NMN es un precursor "
 "del NAD+ en la ruta que la célula usa para producirlo.",
 "β-nicotinamida mononucleótido 500 mg. Cápsula vegetal de HPMC, celulosa "
 "microcristalina, dióxido de silicio y estearato de magnesio. Un solo "
 "principio activo: sin mezclas ni añadidos innecesarios.",
 "<li><strong>30 cápsulas</strong> · 36 g netos</li>\n"
 "<li>Peso bruto 45 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Una cápsula al día, con 175–235 ml de agua, o según indique un profesional "
 "sanitario."),

"greens-superfood": ficha(
 "Polvo de verduras, algas, frutas y raíces concentradas, para tomar una vez "
 "al día disuelto en agua. Reúne más de veinte ingredientes vegetales sin "
 "aditivos artificiales.",
 "Hierba de cebada (hoja), brócoli (hoja), espirulina (planta entera), té "
 "verde (hoja), extracto de alfalfa, hierba de trigo (hoja), remolacha "
 "(raíz), hibisco (flor), zumo de fresa, arándano rojo, zumo de açaí, "
 "extracto de arándano, granada, canela (corteza), extracto de cúrcuma "
 "(raíz), ginseng <em>Panax</em> (raíz), ashwagandha (raíz), extracto de "
 "mangostán (pericarpio), extracto de pimienta negra (fruto), inulina "
 "(raíz de aguaturma), jengibre (raíz) y alginato sódico.",
 "<li><strong>126 g</strong> de polvo</li>\n"
 "<li>Peso bruto 181 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Un cacito al día disuelto en 175–235 ml de agua fría o de la bebida que "
 "prefieras. Se toma dentro de los diez minutos siguientes a mezclarlo."),

"reds-superfood": ficha(
 "Polvo de frutos rojos, botánicos y fermentos, para tomar una vez al día "
 "disuelto en agua. La contrapartida del verde: remolacha, bayas y granada, "
 "con fibra de avena e inulina.",
 "Remolacha (raíz), zumo de fresa, hibisco (flor), frambuesa, grosella "
 "negra, zumo de açaí, extracto de arándano, arándano rojo, extracto de "
 "semilla de uva, extracto de mango africano (semilla), granada, fibra de "
 "avena, inulina (raíz de aguaturma), nueve cultivos de <em>Lactobacillus</em> "
 "y <em>Bifidobacterium</em>, canela (corteza), té verde (hoja), jengibre "
 "(raíz), cúrcuma (raíz), extracto de shilajit, extracto de melón amargo "
 "(fruto) y extracto de pimienta negra (fruto).",
 "<li><strong>120 g</strong> de polvo</li>\n"
 "<li>Peso bruto 172 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Un cacito al día disuelto en 175–235 ml de agua fría o de la bebida que "
 "prefieras. Se toma dentro de los diez minutos siguientes a mezclarlo."),

"advanced-100-whey-protein-isolate-chocolate": ficha(
 "Aislado de proteína de suero al 100 %, sabor chocolate, con "
 "<strong>22 g de proteína por toma</strong>. Lleva aceite MCT en polvo y "
 "pectina de manzana, y se endulza con estevia.",
 "Aislado de proteína de suero, cacao en polvo, aceite MCT en polvo, aromas "
 "naturales, lecitina de girasol, pectina de manzana en polvo, sal marina, "
 "extracto de estevia (hoja) y dióxido de silicio.",
 "<li><strong>839 g</strong> de polvo · sabor chocolate</li>\n"
 "<li>22 g de proteína por toma</li>\n"
 "<li>Peso bruto 910 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Dos cacitos al día disueltos en 175–235 ml de agua o de la bebida que "
 "prefieras."),

"plant-protein-vanilla": ficha(
 "Proteína de origen vegetal con sabor a vainilla y <strong>20 g de proteína "
 "por toma</strong>, con perfil completo de aminoácidos esenciales. "
 "<strong>Sin lácteos, sin soja y sin gluten</strong>: la alternativa cuando "
 "el suero no entra.",
 "Aislado de proteína de haba, aromas naturales, proteína de levadura "
 "nutricional fermentada YESTEIN™, aceite MCT en polvo, pectina de manzana "
 "en polvo, sal marina, extracto de estevia (hoja) y dióxido de silicio.",
 "<li><strong>844 g</strong> de polvo · sabor vainilla</li>\n"
 "<li>20 g de proteína y 110 kcal por toma</li>\n"
 "<li>Peso bruto 910 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Dos cacitos al día disueltos en 175–235 ml de agua o de la bebida que "
 "prefieras."),

"bcaa-post-workout-powder-honeydew-watermelon": ficha(
 "Polvo con <strong>5000 mg de aminoácidos ramificados</strong> en proporción "
 "2:1:1 —dos partes de leucina por una de isoleucina y una de valina— más "
 "glutamina. Sabor a melón y sandía.",
 "Vitamina B6 (como clorhidrato de piridoxina), L-glutamina, BCAA 2:1:1, "
 "ácido cítrico, aromas de melón y sandía, citrato potásico, dióxido de "
 "silicio, sucralosa, sal marina, remolacha en polvo (color), extracto de "
 "piel de uva (color) y acesulfamo potásico.",
 "<li><strong>292 g</strong> de polvo · sabor melón y sandía</li>\n"
 "<li>Peso bruto 408 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Medio cacito (6,5 g) disuelto en 235–295 ml de bebida fría. Tarda unos "
 "minutos en disolverse del todo. Antes de entrenar, después, o entre comidas."),

"methylene-blue-drops": ficha(
 "Azul de metileno en gotas, con <strong>10 mg por toma</strong>. Formato "
 "líquido con cuentagotas, de tres ingredientes.",
 "Azul de metileno en polvo (10 mg), agua y sorbato potásico.",
 "<li><strong>60 ml</strong> · frasco con cuentagotas</li>\n"
 "<li>Peso bruto 77 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Agitar antes de usar. Adultos: 1 ml (20 gotas) al día por vía oral, "
 "preferentemente por la mañana, directamente o añadido a una bebida.",
 "<h3>Advertencias</h3>\n<p><strong>La seguridad de este producto no está "
 "determinada.</strong> Las personas embarazadas o en periodo de lactancia, "
 "los menores de 18 años y quienes tengan alguna patología deben consultar "
 "con un profesional sanitario antes de tomarlo. El azul de metileno puede "
 "interaccionar con medicación, en particular con antidepresivos "
 "serotoninérgicos: si tomas cualquier fármaco, consulta antes. Mantener "
 "fuera del alcance de los niños. No usar si el precinto está roto o "
 "ausente. Conservar en un lugar fresco y seco.</p>"),

"nitric-shock-pre-workout-powder-fruit-punch": ficha(
 "Preentrenamiento en polvo con sabor a ponche de frutas. Reúne "
 "<strong>veintitrés ingredientes</strong>: creatina, arginina AKG, "
 "beta-alanina, taurina, cafeína, L-tirosina, 290 mg de electrolitos y un "
 "complejo de vitaminas del grupo B.",
 "Sodio (citrato sódico), potasio (citrato potásico), vitaminas B1, B2, B3, "
 "B6 y B12, ácido fólico, ácido pantoténico, calcio y fósforo (fosfato "
 "dicálcico), magnesio (óxido de magnesio), cromo (nicotinato de cromo), "
 "dicreatina malato, alfa-cetoglutarato de L-arginina, beta-alanina, cafeína "
 "y una matriz de L-taurina, betaína anhidra, maíz ceroso, citrulina malato, "
 "glicociamina, glucuronolactona, L-tirosina, maltodextrina, ácido cítrico, "
 "aroma de ponche de frutas, dextrosa, sucralosa y dióxido de silicio.",
 "<li><strong>300 g</strong> de polvo · sabor ponche de frutas</li>\n"
 "<li>Peso bruto 408 g</li>\n<li>Fabricado en Estados Unidos</li>\n",
 "Empieza por un cacito en 175–235 ml de bebida fría para comprobar la "
 "tolerancia. Si sienta bien, de uno a dos cacitos treinta minutos antes de "
 "entrenar. <strong>No pasar de dos cacitos al día.</strong>",
 "<h3>Advertencias</h3>\n<p><strong>Contiene cafeína.</strong> No apto para "
 "menores de 18 años, embarazadas ni en periodo de lactancia. Consulta con "
 "un médico antes de tomarlo si tienes o has tenido en la familia hipotensión "
 "o hipertensión, cardiopatía, enfermedad hepática o tiroidea, diabetes, "
 "enfermedad psiquiátrica, asma, anemia perniciosa, ansiedad, depresión, "
 "epilepsia, arritmia, ictus o hipertrofia prostática, o si tomas cualquier "
 "medicamento con receta. Mantener fuera del alcance de los niños. No usar si "
 "el precinto está roto o ausente. Conservar en un lugar fresco y seco.</p>"),
}


# Los diecinueve que no son suplementos. Aquí no hay declaraciones
# de salud que esquivar, pero sí marketing del proveedor que no dice nada
# —«sexy glutes», «butt blaster», «transforming routine workout into
# efficient calorie-burning»— y que se ha dejado fuera. Lo que queda son
# las medidas, los materiales y la advertencia cuando la hay.
def art(intro, puntos, especificaciones=None, cierre=None):
    t = f"<p>{intro}</p>\n\n<h3>Qué lo distingue</h3>\n<ul>\n{puntos}</ul>\n"
    if especificaciones:
        t += f"\n<h3>Medidas y materiales</h3>\n<ul>\n{especificaciones}</ul>\n"
    if cierre:
        t += f"\n<p>{cierre}</p>"
    return t

CUERPOS.update({
"steel-plyo-box-12-18-24-inch-high-anti-slip-pre-assembled-plyometric-jump-box-for-home-gym-conditioning-and-strength-training-sold-individually-plyometric-platform-step": art(
 "Cajón de salto de acero tubular de calibre grueso con goma arriba y abajo. "
 "<strong>Llega montado</strong>: se saca de la caja y se usa. Se vende por "
 "unidades, no en juego.",
 "<li><strong>No resbala ni vuelca.</strong> La goma superior e inferior "
 "agarra y el bastidor de acero pesa lo suficiente para no bailar.</li>\n"
 "<li><strong>Sirve para más que saltar.</strong> Saltos al cajón, flexiones, "
 "fondos, subidas, agilidad y trabajo de acondicionamiento.</li>\n"
 "<li><strong>Ya construido.</strong> No hay tornillos que apretar.</li>\n",
 "<li><strong>12 pulgadas</strong> · base 38 × 38 cm, superficie 32 × 31 cm · "
 "pesa 5,4 kg · admite hasta 254 kg</li>\n"
 "<li><strong>18 pulgadas</strong> · base 46 × 46 cm, superficie 36 × 36 cm · "
 "pesa 7,1 kg · admite hasta 249 kg</li>\n"
 "<li><strong>24 pulgadas</strong> · base 53 × 53 cm, superficie 38 × 38 cm · "
 "pesa 8,5 kg · admite hasta 234 kg</li>\n"
 "<li>Acero tubular de calibre grueso y goma</li>\n",
 "El salto al cajón tiene un riesgo que conviene conocer: el fallo se paga en "
 "la espinilla. Empieza por la altura que puedas subir andando y sube cuando "
 "el aterrizaje sea silencioso."),

"finer-form-multi-functional-fid-weight-bench-for-full-all-in-one-body-workout-hyper-back-extension-roman-chair-adjustable-ab-sit-up-bench-incline-decline-bench-flat-bench": art(
 "Banco regulable que hace de <strong>banco plano, inclinado y "
 "declinado</strong>, de silla romana para hiperextensiones, de banco de "
 "abdominales y de banco de predicador. Plegable y con ruedas.",
 "<li><strong>Cinco posiciones en un solo mueble.</strong> Es el banco que "
 "compras cuando no tienes sitio para cinco.</li>\n"
 "<li><strong>Se ajusta al cuerpo, no al revés.</strong> Ocho posiciones de "
 "respaldo, tres de asiento, ocho del rodillo de apoyo y cuatro de "
 "pantorrillas.</li>\n"
 "<li><strong>Hiperextensiones de verdad.</strong> La posición de silla "
 "romana trabaja lumbares, glúteo y core sin necesidad de otra máquina.</li>\n"
 "<li><strong>Se pliega y se mueve.</strong> Ruedas de transporte para "
 "sacarlo del medio.</li>\n",
 "<li>Estructura de acero</li>\n<li>Se pliega para guardar</li>\n"
 "<li>Ruedas de transporte</li>\n",
 "La capacidad máxima no se indica aquí a propósito: la documentación del "
 "fabricante da cuatro cifras distintas para este modelo y no publicamos un "
 "número que no podemos sostener. Si la necesitas para tu caso, pregúntanos y "
 "la confirmamos con el proveedor antes de que compres."),

"sport-basketball-backpack-travel-outdoor-waterproof-swimming-fitness-travel-sports-bag-basketball-pouch-hiking-climbing-backpack": art(
 "Mochila deportiva de nailon impermeable de <strong>menos de veinte "
 "litros</strong>, con hueco para el balón. Del tamaño justo para el "
 "gimnasio, la piscina o una salida de un día.",
 "<li><strong>Compacta a propósito.</strong> Cabe lo necesario y no invita a "
 "cargar de más.</li>\n"
 "<li><strong>Nailon resistente</strong>, tratado para aguantar la lluvia y "
 "la humedad.</li>\n"
 "<li><strong>Compartimento para el balón</strong>, que también sirve para "
 "el calzado o la ropa mojada.</li>\n"
 "<li>Corte unisex.</li>\n",
 "<li>Capacidad inferior a 20 litros</li>\n<li>Nailon impermeable</li>\n"),

"weight-lifting-belt-premium-4-wide-functional-fitness-belt-for-men-women-squat-deadlift-support": art(
 "Cinturón de <strong>cuero auténtico de cuatro pulgadas</strong> (unos 10 "
 "cm) ya ablandado, para sentadilla y peso muerto. No hay que domarlo: se "
 "puede usar el primer día.",
 "<li><strong>Cuero ya ablandado.</strong> La mayoría de los cinturones de "
 "cuero piden semanas de uso antes de dejar de clavarse.</li>\n"
 "<li><strong>Doble pasador y costura reforzada.</strong> El punto por donde "
 "un cinturón cede es siempre la hebilla.</li>\n"
 "<li><strong>Interior de ante</strong>, suave contra la piel.</li>\n"
 "<li><strong>Ancho constante</strong>, para presión repartida en todo el "
 "contorno.</li>\n",
 "<li>Cuero 100 % · 10 cm de ancho</li>\n<li>Hebilla de doble pasador</li>\n"
 "<li>Interior de ante</li>\n",
 "Un cinturón no sustituye a la técnica ni a un core fuerte: da algo contra "
 "lo que empujar cuando la carga ya es alta."),

"weighted-vest-6lb-8lb-10lb-12lb-15lb-18lb-20lb-24lb-30lb-for-men-women-reflective-stripe-adjustable-buckle-comfortable-durable-rucking-vest-for-walking-running-strength-training": art(
 "Chaleco lastrado de neopreno, en <strong>ocho pesos distintos</strong>, con "
 "banda reflectante y hebilla regulable. Para caminar, correr, rucking y "
 "trabajo con el propio peso.",
 "<li><strong>Neopreno sellado por dentro.</strong> No roza y no deja escapar "
 "las partículas de hierro del lastre, que es el fallo típico de los chalecos "
 "baratos.</li>\n"
 "<li><strong>No baila.</strong> Hombreras gruesas que reparten la presión, "
 "banda elástica y hebilla que lo ciñen al cuerpo.</li>\n"
 "<li><strong>Se sube de peso poco a poco.</strong> Ocho escalones, de 6 a 30 "
 "libras, para no saltar de golpe.</li>\n"
 "<li><strong>Banda reflectante</strong>, para salir cuando ya no hay luz.</li>\n",
 "<li>Pesos: 6, 8, 10, 12, 15, 18, 24 y 30 libras (de 2,7 a 13,6 kg)</li>\n"
 "<li>Neopreno con costuras dobles reforzadas</li>\n"
 "<li>Hebilla regulable y banda elástica</li>\n"),

"steel-mace-bell-for-strength-training-support-full-body-muscles-shoulder-grips-forearms-workouts-stretching-5-7-10-15-20-25-30-lb-for-woman-man": art(
 "Maza de <strong>acero macizo</strong> con mango moleteado en rombo, en siete "
 "pesos. El peso está en un extremo, así que el esfuerzo cambia según dónde "
 "esté la maza en el recorrido — eso es lo que la hace distinta de una "
 "mancuerna.",
 "<li><strong>Trabaja el agarre y el hombro.</strong> Cada balanceo pide "
 "estabilizar, no solo levantar.</li>\n"
 "<li><strong>Moleteado en rombo</strong>, para que no se escurra en el giro "
 "de 360 grados.</li>\n"
 "<li><strong>Acero macizo</strong>, de una pieza.</li>\n"
 "<li><strong>Movimientos en varios planos</strong>: sentadillas, zancadas, "
 "peso muerto, balanceos, giros de 360 y press por encima de la cabeza.</li>\n",
 "<li>Pesos: 5, 7, 10, 15, 20, 25 y 30 libras (de 2,3 a 13,6 kg)</li>\n"
 "<li>Acero macizo · mango moleteado en rombo</li>\n",
 "Empieza más ligero de lo que crees. El giro de 360 con una maza demasiado "
 "pesada termina en el hombro o en la nuca."),

"glute-bridge-plate-loaded-hip-thrust-machine-black-steel-frame-176-37-lb": art(
 "Máquina de <strong>empuje de cadera con carga de discos</strong> y "
 "estructura de acero negro. Resuelve el problema del hip thrust con barra: "
 "meterse debajo de la carga, colocarla y controlarla.",
 "<li><strong>Aísla el glúteo</strong> con la cadera y la columna sujetas en "
 "todo el recorrido.</li>\n"
 "<li><strong>Respaldo articulado</strong> que acompaña la espalda entera y "
 "obliga a bisagrar por la cadera, no por la lumbar.</li>\n"
 "<li><strong>Cinturón de sujeción</strong> de grado industrial y plataforma "
 "de pies sobredimensionada.</li>\n"
 "<li><strong>Doble mecanismo de seguridad</strong> a los dos lados, con tope "
 "inferior.</li>\n"
 "<li><strong>Admite bandas elásticas</strong> en sus anclajes, para cambiar "
 "la curva de resistencia.</li>\n",
 "<li>Peso de la máquina: 80 kg</li>\n"
 "<li>Carga máxima 163 kg · hasta cuatro discos de 20 kg por lado</li>\n"
 "<li>Resistencia inicial 6,8 kg (el carro vacío)</li>\n"
 "<li>Discos olímpicos de 5 cm de diámetro interior</li>\n"
 "<li>Acero industrial de 3 mm de pared · rodamientos de doble pivote</li>\n"
 "<li>Uso doméstico</li>\n",
 "Los discos, las bandas y las pinzas <strong>se venden aparte</strong>."),
})

# Sin <p> propio: art() ya envuelve el cierre en un párrafo, y anidar uno
# dentro de otro es HTML inválido — el navegador cierra el primero por su
# cuenta y la maqueta se descoloca.
CUIDADO = ("<em>Uso externo. En caso de contacto con los ojos, aclarar "
           "abundantemente con agua limpia. Si la irritación persiste, dejar "
           "de usarlo.</em>")

CUERPOS.update({
"gym-exercise-foot-pedal-adjustable-cardio-pedal-exerciser-non-slip-stable-200kg-load-bearing-portable-fitness-equipment": art(
 "Step de aeróbic moldeado en <strong>una sola pieza de ABS</strong>, con "
 "altura regulable mediante alzas. Se guarda de pie contra la pared.",
 "<li><strong>Admite 200 kg.</strong> La pieza única, sin uniones, es lo que "
 "le da esa capacidad.</li>\n"
 "<li><strong>Superficie en panal antideslizante</strong> y tacos de goma "
 "abajo.</li>\n"
 "<li><strong>Columna de refuerzo en malla</strong>, que es lo que lo "
 "diferencia de un step corriente.</li>\n"
 "<li><strong>Tres alturas.</strong> Con las alzas puestas sube a 10, 16 o "
 "21 cm, según cómo se combinen.</li>\n",
 "<li>ABS moldeado en una pieza</li>\n<li>Carga admitida: 200 kg</li>\n"
 "<li>Caja de 46,5 × 30 × 11 cm · peso bruto 1,5 kg</li>\n"
 "<li>Incluye el step y dos alzas</li>\n",
 "Tolerancia de 1 a 2 cm en las medidas, que están tomadas a mano."),

"8-16-pcs-foam-fitness-non-slip-yoga-mat-fitness-floor-tile-protection-pad-fitness-equipment-mat-suitable-for-indoor-fitness": art(
 "Losetas de espuma que encajan entre sí para cubrir el suelo donde entrenas. "
 "Protegen la tarima de las pesas y amortiguan rodillas y codos.",
 "<li><strong>Encajan sin pegamento</strong> y se levantan igual de fácil "
 "cuando hay que recoger.</li>\n"
 "<li><strong>Superficie antideslizante</strong>, para que la loseta no viaje "
 "con el ejercicio.</li>\n"
 "<li><strong>Se limpian pasando un paño.</strong></li>\n"
 "<li><strong>Se apilan planas</strong> y caben en cualquier hueco.</li>\n"
 "<li>Cada loseta trae su <strong>remate de borde</strong>, para que el "
 "perímetro quede recto.</li>\n",
 "<li>30 × 30 × 1 cm por loseta</li>\n<li>Espuma con remate de borde incluido</li>\n"),

"universal-olympic-trap-shrug-bar-500-lb-acity": art(
 "Barra hexagonal de acero tubular para <strong>peso muerto y "
 "encogimientos</strong>. Los agarres van en posición neutra y las mangas "
 "elevadas, lo que acorta el recorrido y descarga la espalda respecto a una "
 "barra recta.",
 "<li><strong>Agarres neutros.</strong> Las manos a los lados del cuerpo, no "
 "por delante: la cadera entra antes y la lumbar trabaja menos.</li>\n"
 "<li><strong>Mangas elevadas</strong>, que suben el disco del suelo y "
 "acortan el recorrido.</li>\n"
 "<li><strong>Pies integrados.</strong> No raya el suelo y la barra se "
 "sostiene sola mientras cargas y descargas.</li>\n"
 "<li><strong>Ocupa poco</strong> guardada de canto.</li>\n",
 "<li>127 × 74 × 36 cm · pesa 12,7 kg</li>\n"
 "<li>Carga máxima recomendada 227 kg (500 libras)</li>\n"
 "<li>Manga cargable de 24 cm · discos olímpicos de 5 cm</li>\n"
 "<li>Acero tubular</li>\n"),

"power-rack-phone-mount-hook-on-smartphone-holder-for-2-2-3-3-squat-rack-upright-tool-free-installation-vertical-horizontal-viewing-fits-phones-up-to-3-22-wide": art(
 "Soporte que se engancha al perfil de la jaula de fuerza <strong>sin "
 "herramientas</strong>. Deja el móvil a la altura de los ojos mientras "
 "entrenas.",
 "<li><strong>Se cuelga y se quita en un gesto.</strong> Nada de tornillos "
 "ni abrazaderas.</li>\n"
 "<li><strong>Encaja en la mayoría de jaulas</strong> con agujeros de 16 a 25 "
 "mm de diámetro.</li>\n"
 "<li><strong>Tacos antideslizantes</strong> incluidos, para que el móvil no "
 "se mueva entre series.</li>\n"
 "<li><strong>Bolsa de malla</strong> para llevarlo en la mochila.</li>\n",
 "<li>Dos tamaños: para perfiles de 2×2 y de 3×3 pulgadas</li>\n"
 "<li>Cabida interior 8,2 cm: la mayoría de móviles, con funda fina</li>\n"
 "<li>Agujeros de jaula de 5/8 a 1 pulgada</li>\n",
 "Mide el ancho de tu móvil antes de pedirlo. Si tu jaula es de 2×3 pulgadas, "
 "elige el tamaño que más se acerque. En horizontal aguanta, pero se "
 "recomienda usarlo en vertical."),

"ankle-resistance-bands-with-cuffs-for-women-men-3-level-adjustable-leg-glute-workout-equipment-portable-home-gym-exercise-bands-for-kickbacks-hip-thrusts-yoga-strength-training": art(
 "Bandas elásticas de TPE con <strong>tobilleras acolchadas</strong> y tres "
 "niveles de resistencia. Para patadas de glúteo, puentes, abducciones y "
 "extensiones de pierna.",
 "<li><strong>Tobilleras con velcro</strong>, acolchadas: no se clavan ni se "
 "escurren a mitad de serie.</li>\n"
 "<li><strong>TPE de buena elasticidad</strong>, que recupera la forma y no "
 "se resquebraja como el látex barato.</li>\n"
 "<li><strong>Tres resistencias</strong>, para subir cuando la serie deje de "
 "costar.</li>\n"
 "<li><strong>Caben en cualquier bolsa.</strong> Es el equipo que sí te "
 "llevas de viaje.</li>\n",
 "<li>Material TPE</li>\n<li>Tres niveles de resistencia</li>\n"
 "<li>Tobilleras acolchadas con cierre de velcro</li>\n"),

"yoga-shorts-cross-border-honey-buttocks-buttocks-sports-high-waist-abdomen-stretch-tight-fitting-anti-glare-quick-drying-fitness": art(
 "Short deportivo de <strong>talle alto</strong> y tejido elástico, que "
 "sujeta el abdomen sin apretar. No transparenta al agacharse.",
 "<li><strong>Talle alto</strong>, que se queda donde lo pones.</li>\n"
 "<li><strong>No transparenta</strong> en la sentadilla ni en el suelo.</li>\n"
 "<li><strong>Secado rápido.</strong></li>\n"
 "<li><strong>Ligero</strong>: 85 gramos la prenda.</li>\n",
 "<li>Poliéster, elastano y nailon</li>\n<li>Tallas M y L</li>\n"
 "<li>85 g por prenda (±5 g)</li>\n",
 "<strong>Cuidados:</strong> lavar antes del primer uso. Mejor a mano y secar "
 "al aire; si va a la lavadora, en bolsa de malla, con agua fría y colores "
 "parecidos, y secar en plano."),

"yoga-shorts-women-fitness-elastic-running-workout-short-leggings-for-ladies-gym-sport-shorts-fitness-sportwear": art(
 "Short de deporte de mujer en tejido <strong>sin costuras</strong>, con "
 "elasticidad en las cuatro direcciones. La cintura comprime y el corte sigue "
 "la forma de la pierna.",
 "<li><strong>Sin costuras.</strong> Tejido de punto continuo: nada que roce "
 "en la cara interna del muslo.</li>\n"
 "<li><strong>Elástico en cuatro direcciones</strong>, así que acompaña el "
 "movimiento en vez de frenarlo.</li>\n"
 "<li><strong>Cintura compresiva</strong>, que no se enrolla.</li>\n"
 "<li><strong>Aparta la humedad y seca rápido.</strong></li>\n",
 "<li>Nailon y elastano</li>\n<li>Tallas S, M y L · color negro</li>\n",
 "Tolerancia de 1 a 3 cm en las medidas, tomadas a mano."),

"dryblend®-t-shirt": art(
 "Camiseta de corte clásico en tejido <strong>DryBlend</strong>, mitad "
 "algodón y mitad poliéster. El algodón da el tacto y el poliéster aparta el "
 "sudor: ni cerco en la espalda ni tela pegada.",
 "<li><strong>Corte clásico moderno</strong>, ni holgado ni ceñido.</li>\n"
 "<li><strong>Cuello de canalé</strong> de ancho clásico, que no se da de "
 "sí.</li>\n"
 "<li><strong>Cuello y hombros reforzados con cinta</strong>: es la costura "
 "que primero cede en una camiseta barata.</li>\n"
 "<li><strong>Etiqueta arrancable</strong>, para que no roce la nuca.</li>\n",
 "<li>50 % algodón y 50 % poliéster</li>\n"
 "<li>Gramaje 186 g/m²</li>\n<li>Confeccionada en Honduras</li>\n",
 "El color blanco tira a hueso, no a blanco óptico: es una propiedad del "
 "tejido, no un defecto de la prenda."),

"unisex-sports-jersey": art(
 "Camiseta unisex en <strong>malla de poliéster</strong>, de corte holgado y "
 "largo extra. La malla ventila donde una camiseta normal se pega.",
 "<li><strong>Malla transpirable</strong> al cien por cien de poliéster.</li>\n"
 "<li><strong>Largo extra</strong>, que cubre por debajo de la cintura y no "
 "se sube al levantar los brazos.</li>\n"
 "<li><strong>Manga ranglán corta</strong>, sin costura en el hombro.</li>\n"
 "<li><strong>Costura lateral</strong> y <strong>ribete en el cuello</strong>, "
 "que es lo que aguanta el lavado.</li>\n",
 "<li>100 % poliéster en malla</li>\n<li>Gramaje 140 g/m²</li>\n"
 "<li>Corte holgado unisex · cuello redondo clásico</li>\n"
 "<li>Confeccionada en China</li>\n",
 "Prenda para adultos. Dos años de garantía en la UE. Cumple los requisitos "
 "de inflamabilidad y de contenido de cadmio, bisfenoles y ftalatos."),

"charcoal-soap": art(
 "Jabón artesanal con <strong>carbón activado</strong>, aceite esencial de "
 "menta y de árbol del té. Para cara y cuerpo, en pastilla y sin envase de "
 "plástico.",
 "<li><strong>No mancha.</strong> La proporción de carbón está ajustada para "
 "limpiar sin dejar rastro gris en la piel ni en la toalla.</li>\n"
 "<li><strong>Limpieza profunda</strong> de poros y de los restos que deja "
 "el día.</li>\n"
 "<li><strong>Menta y árbol del té</strong>: un aroma que despeja, para la "
 "ducha de la mañana o la de después de entrenar.</li>\n"
 "<li><strong>Aceites de comercio justo</strong> y palma sostenible.</li>\n",
 "<li>113 g por pastilla · peso bruto 122 g</li>\n"
 "<li>Aceites saponificados de palma, coco, girasol y oliva virgen extra "
 "ecológicos; aceite esencial de menta; aceite esencial de árbol del té; "
 "carbón activado</li>\n"
 "<li>Elaborado en Estados Unidos</li>\n",
 "<strong>Modo de empleo:</strong> añade agua templada para hacer espuma "
 "densa. Déjala secar entre usos y durará bastante más.<br>" + CUIDADO),

"rich-sandalwood-soap": art(
 "Jabón artesanal de <strong>sándalo</strong>, con manteca de karité entre "
 "sus aceites saponificados. Aroma amaderado y espuma densa.",
 "<li><strong>Con manteca de karité</strong>, que es lo que deja la piel "
 "suave en vez de tirante.</li>\n"
 "<li><strong>Apto para todo tipo de piel</strong>, incluida la sensible.</li>\n"
 "<li><strong>Aroma a sándalo</strong>, hondo y amaderado.</li>\n"
 "<li><strong>Aceites de comercio justo</strong> y palma sostenible.</li>\n",
 "<li>113 g por pastilla · peso bruto 127 g</li>\n"
 "<li>Aceites saponificados de oliva virgen extra, palma, coco y manteca de "
 "karité ecológicos; fragancia</li>\n"
 "<li>Elaborado en Estados Unidos</li>\n",
 "<strong>Modo de empleo:</strong> añade agua templada para hacer espuma "
 "densa. Déjala secar entre usos y durará bastante más.<br>" + CUIDADO),

"portable-breathing-trainer-with-adjustable-resistance-settings": art(
 "Entrenador respiratorio portátil con <strong>resistencia regulable</strong>. "
 "Se respira a través del aparato, que opone resistencia al inspirar y al "
 "espirar.",
 "<li><strong>Resistencia regulable</strong>: varios niveles, para empezar "
 "suave y subir cuando cueste menos.</li>\n"
 "<li><strong>Trabaja la musculatura respiratoria.</strong> El esfuerzo lo "
 "pone el nivel elegido, no el aparato.</li>\n"
 "<li><strong>Cabe en un bolsillo.</strong></li>\n"
 "<li><strong>Para quien usa el aire</strong>: nadadores, cantantes, "
 "instrumentistas de viento y cualquiera que entrene resistencia.</li>\n",
 "<li>Plástico no tóxico</li>\n<li>Resistencia regulable</li>\n",
 "No es un producto sanitario y no trata ninguna dolencia respiratoria. Si "
 "tienes asma, EPOC o cualquier problema pulmonar, consulta con tu médico "
 "antes de usarlo."),
})


# ---------------------------------------------------------------------------
# Títulos en las tres lenguas: (es, en, fr)
# ---------------------------------------------------------------------------
# Los títulos del proveedor venían en inglés y con defectos a la vista:
# «Glutes & Hip Thrust Machine.» con punto final, «Yoga Shorts Cross-Border»
# —jerga de comercio chino que el comprador no tiene por qué entender— y
# «Unisex sports jersey» en minúsculas. El castellano es el título del
# producto; el inglés y el francés se registran como traducciones. Los
# handles NO se tocan: cambiarlos rompería las URL ya indexadas.
TITULOS = {
"nad": ("NAD+ en cápsulas", "NAD+ Capsules", "NAD+ en gélules"),
"nmn": ("NMN en cápsulas", "NMN Capsules", "NMN en gélules"),
"creatine-hydration-powder": ("Creatina con electrolitos",
    "Creatine with Electrolytes", "Créatine et électrolytes"),
"greens-superfood": ("Greens Superfood en polvo", "Greens Superfood Powder",
    "Greens Superfood en poudre"),
"reds-superfood": ("Reds Superfood en polvo", "Reds Superfood Powder",
    "Reds Superfood en poudre"),
"advanced-100-whey-protein-isolate-chocolate": (
    "Aislado de proteína de suero · Chocolate",
    "100 % Whey Protein Isolate · Chocolate",
    "Isolat de protéine de lactosérum · Chocolat"),
"plant-protein-vanilla": ("Proteína vegetal · Vainilla",
    "Plant Protein · Vanilla", "Protéine végétale · Vanille"),
"bcaa-post-workout-powder-honeydew-watermelon": (
    "BCAA en polvo · Melón y sandía",
    "BCAA Powder · Honeydew and Watermelon",
    "BCAA en poudre · Melon et pastèque"),
"methylene-blue-drops": ("Azul de metileno en gotas", "Methylene Blue Drops",
    "Bleu de méthylène en gouttes"),
"nitric-shock-pre-workout-powder-fruit-punch": (
    "Preentreno Nitric Shock · Ponche de frutas",
    "Nitric Shock Pre-Workout · Fruit Punch",
    "Pré-entraînement Nitric Shock · Punch aux fruits"),

"steel-plyo-box-12-18-24-inch-high-anti-slip-pre-assembled-plyometric-jump-box-for-home-gym-conditioning-and-strength-training-sold-individually-plyometric-platform-step": (
    "Cajón pliométrico de acero", "Steel Plyometric Jump Box",
    "Caisson pliométrique en acier"),
"finer-form-multi-functional-fid-weight-bench-for-full-all-in-one-body-workout-hyper-back-extension-roman-chair-adjustable-ab-sit-up-bench-incline-decline-bench-flat-bench": (
    "Banco de musculación multifunción", "Multi-Functional Weight Bench",
    "Banc de musculation multifonction"),
"sport-basketball-backpack-travel-outdoor-waterproof-swimming-fitness-travel-sports-bag-basketball-pouch-hiking-climbing-backpack": (
    "Mochila deportiva impermeable", "Waterproof Sport Backpack",
    "Sac à dos de sport imperméable"),
"weight-lifting-belt-premium-4-wide-functional-fitness-belt-for-men-women-squat-deadlift-support": (
    "Cinturón de halterofilia de cuero", "Leather Weightlifting Belt",
    "Ceinture d'haltérophilie en cuir"),
"weighted-vest-6lb-8lb-10lb-12lb-15lb-18lb-20lb-24lb-30lb-for-men-women-reflective-stripe-adjustable-buckle-comfortable-durable-rucking-vest-for-walking-running-strength-training": (
    "Chaleco lastrado ajustable", "Adjustable Weighted Vest",
    "Gilet lesté réglable"),
"steel-mace-bell-for-strength-training-support-full-body-muscles-shoulder-grips-forearms-workouts-stretching-5-7-10-15-20-25-30-lb-for-woman-man": (
    "Maza de acero para entrenamiento de fuerza", "Steel Mace Bell",
    "Masse en acier pour la force"),
"glute-bridge-plate-loaded-hip-thrust-machine-black-steel-frame-176-37-lb": (
    "Máquina de hip thrust con discos", "Plate-Loaded Hip Thrust Machine",
    "Machine à hip thrust à disques"),
"gym-exercise-foot-pedal-adjustable-cardio-pedal-exerciser-non-slip-stable-200kg-load-bearing-portable-fitness-equipment": (
    "Step de cardio regulable", "Adjustable Cardio Stepper",
    "Stepper de cardio réglable"),
"8-16-pcs-foam-fitness-non-slip-yoga-mat-fitness-floor-tile-protection-pad-fitness-equipment-mat-suitable-for-indoor-fitness": (
    "Losetas de espuma para el suelo", "Foam Floor Tiles",
    "Dalles de sol en mousse"),
"universal-olympic-trap-shrug-bar-500-lb-acity": (
    "Barra hexagonal olímpica", "Olympic Trap-Shrug Bar",
    "Barre hexagonale olympique"),
"power-rack-phone-mount-hook-on-smartphone-holder-for-2-2-3-3-squat-rack-upright-tool-free-installation-vertical-horizontal-viewing-fits-phones-up-to-3-22-wide": (
    "Soporte de móvil para jaula de fuerza", "Power Rack Phone Mount",
    "Support de téléphone pour cage à squat"),
"portable-breathing-trainer-with-adjustable-resistance-settings": (
    "Entrenador respiratorio portátil", "Portable Breathing Trainer",
    "Entraîneur respiratoire portable"),
"ankle-resistance-bands-with-cuffs-for-women-men-3-level-adjustable-leg-glute-workout-equipment-portable-home-gym-exercise-bands-for-kickbacks-hip-thrusts-yoga-strength-training": (
    "Bandas de resistencia con tobilleras", "Ankle Resistance Bands",
    "Bandes de résistance avec chevillères"),

"yoga-shorts-cross-border-honey-buttocks-buttocks-sports-high-waist-abdomen-stretch-tight-fitting-anti-glare-quick-drying-fitness": (
    "Short de yoga de talle alto", "High-Waist Yoga Shorts",
    "Short de yoga taille haute"),
"yoga-shorts-women-fitness-elastic-running-workout-short-leggings-for-ladies-gym-sport-shorts-fitness-sportwear": (
    "Short de deporte sin costuras", "Seamless Sport Shorts",
    "Short de sport sans coutures"),
"dryblend®-t-shirt": ("Camiseta DryBlend", "DryBlend® T-Shirt",
    "T-shirt DryBlend®"),
"unisex-sports-jersey": ("Camiseta de deporte unisex", "Unisex Sports Jersey",
    "Maillot de sport unisexe"),

"charcoal-soap": ("Jabón de carbón activado", "Activated Charcoal Soap",
    "Savon au charbon actif"),
"rich-sandalwood-soap": ("Jabón de sándalo", "Rich Sandalwood Soap",
    "Savon au santal"),
}

TOPE_TITULO = 60
TOPE_DESCRIPCION = 155
TOPE_ALT = 125


def comprobar() -> list:
    """Las cadenas que se pasan de largo. Vacío es lo que hay que ver."""
    largas = []
    for handle, (titulo, descripcion, alt) in COLECCIONES.items():
        if len(titulo) > TOPE_TITULO:
            largas.append(f"colección {handle} · título {len(titulo)}/{TOPE_TITULO}")
        if len(descripcion) > TOPE_DESCRIPCION:
            largas.append(f"colección {handle} · descripción {len(descripcion)}")
    for handle, (titulo, descripcion, alt, familia, _) in FICHAS.items():
        for texto, tope, que in ((titulo, TOPE_TITULO, "título"),
                                 (descripcion, TOPE_DESCRIPCION, "descripción"),
                                 (alt, TOPE_ALT, "alternativo")):
            if len(texto) > tope:
                largas.append(f"{handle} · {que} {len(texto)}/{tope}: {texto}")
        if familia not in TIPOS:
            largas.append(f"{handle} · familia desconocida: {familia}")
    return largas


if __name__ == "__main__":
    malas = comprobar()
    print(f"\n  {len(FICHAS)} fichas y {len(COLECCIONES)} colecciones · "
          f"{len(malas)} fuera de medida\n")
    for m in malas:
        print(f"    {m}")
    print()
