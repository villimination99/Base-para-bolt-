#!/usr/bin/env python3
"""
VILLUMINATIONS — Del catálogo al Diario
========================================
`auditar.py` encontró que los nueve artículos del Diario son **huérfanos**: no
los enlaza ninguna ficha. El enlace interno iba en un solo sentido —del
artículo al producto— y así el Diario solo recibe visitas del buscador. Un
artículo enlazado desde la ficha del producto que le viene a cuento además
convierte, porque quien duda entre dos proteínas ya está en la página donde se
compra.

    python3 tienda/lecturas.py

Este fichero es el mapa, y solo el mapa: qué artículo se le ofrece a qué
producto. El bloque lo pegan `catalogo.py`, `cuerpos_en_fr.py`,
`descripciones.py` y `fichas_libros.py` al terminar de componer su cuerpo, así
que el texto vive en un sitio y sale en cuarenta.

**Un enlace no nombra otro producto.** La regla de que cada ficha se explica
sola sigue en pie: aquí solo se enlaza al Diario, que es material abierto y no
revela el catálogo.

**Un enlace no promete nada.** Ofrecer «Cuánta proteína hace falta al día»
desde un bote de proteína no es una declaración de salud: es la lectura, y el
artículo ya dice de dónde salen sus cifras.

Guarda
------
Los artículos están escritos en castellano. Enlazar desde el cuerpo inglés de
un producto a un artículo que solo existe en castellano manda al comprador a
una página que no puede leer, así que `disponibles()` pregunta antes y en
inglés y francés hoy devuelve el conjunto vacío: el bloque sencillamente no
sale. En cuanto exista `articulos_en_fr.py`, los mismos cuarenta cuerpos
empiezan a enlazar solos, sin tocar este fichero.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import articulos

BLOG = articulos.BLOG["handle"]

# El prefijo de idioma de la tienda. El castellano es el idioma primario y va
# sin prefijo; los demás cuelgan de /en/ y /fr/.
PREFIJO = {"es": "", "en": "/en", "fr": "/fr"}

ROTULO = {
    "es": "Del Diario",
    "en": "From the Journal",
    "fr": "Du Journal",
}

# handle del producto -> artículos que se le ofrecen, en orden.
#
# Dos como mucho. Tres ya es una lista de enlaces y nadie pincha ninguno; el
# segundo enlace solo se pone cuando responde a una pregunta distinta de la
# del primero.
MAPA = {
    # --- suplementos ---------------------------------------------------
    "nad": ("que-suplementos-tienen-evidencia",
            "como-se-lee-una-etiqueta-nutricional"),
    "nmn": ("que-suplementos-tienen-evidencia",
            "como-se-lee-una-etiqueta-nutricional"),
    "methylene-blue-drops": ("que-suplementos-tienen-evidencia",
                             "como-se-lee-una-etiqueta-nutricional"),
    # El bote de creatina enlaza al artículo de creatina. Estaba enlazando a
    # la etiqueta nutricional, que le viene mucho menos a cuento.
    "creatine-hydration-powder": ("creatina",
                                  "que-suplementos-tienen-evidencia"),
    # El preentreno enlaza al artículo que desglosa un preentreno. Antes
    # ofrecía el de evidencia general, que le queda ancho.
    "nitric-shock-pre-workout-powder-fruit-punch":
        ("que-lleva-un-preentreno",
         "que-suplementos-tienen-evidencia"),
    # Los dos botes de polvo enlazan al artículo que contesta la pregunta que
    # se hace de verdad antes de comprarlos. El de la etiqueta iba primero y
    # respondía a otra cosa.
    "greens-superfood": ("superalimentos-en-polvo-sustituyen-verdura",
                         "como-se-lee-una-etiqueta-nutricional"),
    "reds-superfood": ("superalimentos-en-polvo-sustituyen-verdura",
                       "como-se-lee-una-etiqueta-nutricional"),
    "advanced-100-whey-protein-isolate-chocolate":
        ("como-elegir-una-proteina-en-polvo",
         "cuanta-proteina-hace-falta-al-dia"),
    "plant-protein-vanilla": ("como-elegir-una-proteina-en-polvo",
                              "cuanta-proteina-hace-falta-al-dia"),
    "bcaa-post-workout-powder-honeydew-watermelon":
        ("cuanta-proteina-hace-falta-al-dia",
         "que-suplementos-tienen-evidencia"),

    # --- equipo --------------------------------------------------------
    "steel-plyo-box-12-18-24-inch-high-anti-slip-pre-assembled-plyometric-"
    "jump-box-for-home-gym-conditioning-and-strength-training-sold-"
    "individually-plyometric-platform-step":
        ("gimnasio-en-casa-que-comprar-primero",
         "cuanta-actividad-fisica-hace-falta"),
    "finer-form-multi-functional-fid-weight-bench-for-full-all-in-one-body-"
    "workout-hyper-back-extension-roman-chair-adjustable-ab-sit-up-bench-"
    "incline-decline-bench-flat-bench":
        ("gimnasio-en-casa-que-comprar-primero",),
    "weighted-vest-6lb-8lb-10lb-12lb-15lb-18lb-20lb-24lb-30lb-for-men-women-"
    "reflective-stripe-adjustable-buckle-comfortable-durable-rucking-vest-"
    "for-walking-running-strength-training":
        ("cuanta-actividad-fisica-hace-falta",
         "gimnasio-en-casa-que-comprar-primero"),
    "steel-mace-bell-for-strength-training-support-full-body-muscles-"
    "shoulder-grips-forearms-workouts-stretching-5-7-10-15-20-25-30-lb-for-"
    "woman-man":
        ("gimnasio-en-casa-que-comprar-primero",),
    "glute-bridge-plate-loaded-hip-thrust-machine-black-steel-frame-176-37-lb":
        ("gimnasio-en-casa-que-comprar-primero",),
    "gym-exercise-foot-pedal-adjustable-cardio-pedal-exerciser-non-slip-"
    "stable-200kg-load-bearing-portable-fitness-equipment":
        ("cuanta-actividad-fisica-hace-falta",),
    "8-16-pcs-foam-fitness-non-slip-yoga-mat-fitness-floor-tile-protection-"
    "pad-fitness-equipment-mat-suitable-for-indoor-fitness":
        ("gimnasio-en-casa-que-comprar-primero",),
    "universal-olympic-trap-shrug-bar-500-lb-acity":
        ("gimnasio-en-casa-que-comprar-primero",),
    "portable-breathing-trainer-with-adjustable-resistance-settings":
        ("cuanta-actividad-fisica-hace-falta",),
    "ankle-resistance-bands-with-cuffs-for-women-men-3-level-adjustable-leg-"
    "glute-workout-equipment-portable-home-gym-exercise-bands-for-kickbacks-"
    "hip-thrusts-yoga-strength-training":
        ("cuanta-actividad-fisica-hace-falta",
         "gimnasio-en-casa-que-comprar-primero"),

    # --- accesorios ----------------------------------------------------
    "sport-basketball-backpack-travel-outdoor-waterproof-swimming-fitness-"
    "travel-sports-bag-basketball-pouch-hiking-climbing-backpack":
        ("cuanta-actividad-fisica-hace-falta",),
    "weight-lifting-belt-premium-4-wide-functional-fitness-belt-for-men-"
    "women-squat-deadlift-support":
        ("gimnasio-en-casa-que-comprar-primero",),
    "power-rack-phone-mount-hook-on-smartphone-holder-for-2-2-3-3-squat-rack-"
    "upright-tool-free-installation-vertical-horizontal-viewing-fits-phones-"
    "up-to-3-22-wide":
        ("gimnasio-en-casa-que-comprar-primero",),

    # --- ropa ----------------------------------------------------------
    "yoga-shorts-cross-border-honey-buttocks-buttocks-sports-high-waist-"
    "abdomen-stretch-tight-fitting-anti-glare-quick-drying-fitness":
        ("cuanta-actividad-fisica-hace-falta",),
    "yoga-shorts-women-fitness-elastic-running-workout-short-leggings-for-"
    "ladies-gym-sport-shorts-fitness-sportwear":
        ("cuanta-actividad-fisica-hace-falta",),
    "dryblend®-t-shirt": ("cuanta-actividad-fisica-hace-falta",),
    "unisex-sports-jersey": ("cuanta-actividad-fisica-hace-falta",),

    # Los dos jabones no llevan lectura. No hay ningún artículo del Diario
    # sobre jabón, y colgarles el del sueño porque «también es cuidarse»
    # sería un enlace puesto para que no quede el hueco vacío.

    # --- los once propios ----------------------------------------------
    "codice-zodiacal": ("que-es-un-decanato", "que-es-un-arcano-mayor"),
    "codice-de-los-arcanos": ("que-es-un-arcano-mayor",),
    "codice-del-si-mismo": ("que-es-un-arcano-mayor", "que-es-un-decanato"),
    "codice-de-las-invocaciones": ("que-es-un-arcano-mayor",),
    "codice-de-la-mesa": ("como-se-lee-una-etiqueta-nutricional",
                          "cuanta-proteina-hace-falta-al-dia"),
    "codice-de-la-carga": ("gimnasio-en-casa-que-comprar-primero",
                           "cuanta-actividad-fisica-hace-falta"),
    "codice-del-descanso": ("cuantas-horas-hay-que-dormir",),
    "codice-de-la-voluntad": ("cuanta-actividad-fisica-hace-falta",),
    "basico-volumen-limpio": ("cuanta-proteina-hace-falta-al-dia",
                              "cuanta-actividad-fisica-hace-falta"),
    "pro-definicion-volumen": ("cuanta-proteina-hace-falta-al-dia",
                               "como-se-lee-una-etiqueta-nutricional"),
    "elite-todo-incluido-coaching": ("cuantas-horas-hay-que-dormir",
                                     "que-suplementos-tienen-evidencia"),
}

# Artículos cuyo castellano vive solo en la tienda: los escribió el dueño ahí
# y el repositorio no los compone. El título se copia para poder enlazarlos, y
# `cotejar.py` es quien avisa si allí cambia. Se dice de dónde sale, no se
# finge que este fichero manda sobre ellos.
EXTERNOS = {
    "creatina": "Creatina: cuánta, cuándo y por qué el monohidrato",
}

TITULOS = {a["handle"]: a["titulo"] for a in articulos.ARTICULOS}
TITULOS.update(EXTERNOS)


def disponibles(lengua: str) -> set:
    """Los artículos que se pueden leer en esa lengua.

    Hoy, en inglés y en francés, ninguno: el Diario está en castellano. En
    cuanto se escriba `articulos_en_fr.py` con la misma forma que
    `cuerpos_en_fr.py`, este conjunto deja de estar vacío y los cuarenta
    cuerpos empiezan a enlazar sin tocar nada más.
    """
    if lengua == "es":
        return set(TITULOS)
    try:
        import articulos_en_fr as t
    except ImportError:
        return set()
    return {h for h, l in getattr(t, "CUERPOS", {}).items() if lengua in l}


def bloque(handle: str, lengua: str = "es") -> str:
    """El bloque de lecturas de un producto, o cadena vacía si no le toca."""
    quiere = MAPA.get(handle, ())
    hay = disponibles(lengua)
    puestos = [h for h in quiere if h in hay]
    if not puestos:
        return ""
    filas = "".join(
        f'<li><a href="{PREFIJO[lengua]}/blogs/{BLOG}/{h}">'
        f'{_titulo(h, lengua)}</a></li>\n' for h in puestos)
    return (f"\n\n<h3>{ROTULO[lengua]}</h3>\n<ul>\n{filas}</ul>")


def _titulo(handle: str, lengua: str) -> str:
    if lengua == "es":
        return TITULOS[handle]
    import articulos_en_fr as t                      # ya se sabe que importa
    return t.CUERPOS[handle][lengua]["titulo"]


def pegar(cuerpos: dict, lengua: str = "es") -> dict:
    """Añade su bloque a cada cuerpo de un diccionario handle -> HTML."""
    return {h: c + bloque(h, lengua) for h, c in cuerpos.items()}


def comprobar() -> list:
    """Handles que no existen y artículos que se quedan sin quien los enlace."""
    problemas = []

    import catalogo
    conocidos = set(catalogo.FICHAS)
    import seo
    conocidos |= set(seo.META)

    for handle in MAPA:
        if handle not in conocidos:
            problemas.append(f"MAPA · producto desconocido: {handle[:60]}")
    for handle, arts in MAPA.items():
        for a in arts:
            if a not in TITULOS:
                problemas.append(f"{handle[:40]} · artículo inexistente: {a}")
        if len(set(arts)) != len(arts):
            problemas.append(f"{handle[:40]} · artículo repetido")
        if len(arts) > 2:
            problemas.append(f"{handle[:40]} · {len(arts)} enlaces, más de dos")

    apuntados = {a for arts in MAPA.values() for a in arts}
    for handle in sorted(set(TITULOS) - apuntados):
        problemas.append(f"artículo sin quien lo enlace: {handle}")

    return problemas


def sin_lectura() -> list:
    """Productos a los que no se les ofrece nada. No es un fallo: es una
    decisión, y conviene verla escrita cada vez que se pasa por aquí."""
    import catalogo
    import seo
    return sorted((set(catalogo.FICHAS) | set(seo.META)) - set(MAPA))


if __name__ == "__main__":
    malos = comprobar()
    enlaces = sum(len(v) for v in MAPA.values())
    print(f"\n  {enlaces} enlaces desde {len(MAPA)} fichas a "
          f"{len({a for v in MAPA.values() for a in v})} artículos · "
          f"{len(malos)} problemas\n")
    for lengua in ("es", "en", "fr"):
        n = len(disponibles(lengua))
        print(f"    {lengua} · {n} artículos legibles · "
              f"{'sale el bloque' if n else 'no sale el bloque'}")
    for m in malos:
        print(f"    {m}")
    sin = sin_lectura()
    if sin:
        print(f"\n    sin lectura, a propósito ({len(sin)}): "
              f"{', '.join(sin)}")
    print()
