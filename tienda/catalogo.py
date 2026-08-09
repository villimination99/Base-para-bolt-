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
