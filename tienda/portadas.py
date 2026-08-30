#!/usr/bin/env python3
"""
VILLUMINATIONS — Las portadas de colección que faltaban
=======================================================

    python3 tienda/portadas.py           # rehace tienda/portadas/*.png

De las seis colecciones, cuatro tenían foto y **dos estaban sin imagen**:
`planes` y `cuidado-personal`. Una colección sin imagen sale como un hueco en
la rejilla del tema, en el resultado del buscador y en cualquier enlace que se
comparta. Es de los defectos que solo se ven preguntándole a la tienda: ningún
comprobador del repositorio podía saberlo.

Se dibuja con lo nuestro
------------------------
La tarjeta se compone con `vi-sigilo`, que es de `ropa/partials/marca.svg` y es
propiedad entera. No hace falta banco de imágenes ni encargo fuera, que es la
misma ventaja que aprovecha `tienda/ropa.py`.

Dos cosas aprendidas al mirarlas renderizadas
---------------------------------------------
· **Los emblemas de `planes/partials/` no valen aquí.** Están dibujados en
  tinta oscura para página blanca, así que sobre el fondo negro de la tarjeta
  desaparecen; y llevan texto castellano incrustado —«4 semanas»,
  «MEDITERRÁNEA»— que no sirve en una portada que se ve en tres lenguas.
· **`r-ojo` tampoco.** Extraer un `<symbol>` de su fichero deja fuera los
  degradados y las máscaras a las que apunta, y lo que sale son cuatro puntos.
  Una lámina no es portátil solo por estar en un `<symbol>`.

Por eso aquí solo entran láminas **autocontenidas y ya pensadas para fondo
oscuro**, que son las de `ropa/partials/`.

Cuál falta y por qué
--------------------
`cuidado-personal` sigue sin portada **a propósito**: sus dos jabones están en
UNLISTED, así que en la tienda esa colección está vacía. Ponerle portada sería
adornar un escaparate sin género. El día que se publiquen, se añade aquí.

Subirla a la tienda
-------------------
No hay mutación que acepte un fichero local. Son tres pasos:
`stagedUploadsCreate` con `resource: COLLECTION_IMAGE`, un POST multipart al
destino que devuelve —con **todos** sus parámetros, en orden— y después
`collectionUpdate` con `image.src` apuntando al `resourceUrl`. Y con
`altText`, que es lo que lee quien no ve la imagen.
"""

import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "tienda" / "portadas"

# Solo láminas autocontenidas y pensadas para fondo oscuro. Véase la cabecera.
LAMINAS = ("ropa/partials/marca.svg",)

PORTADAS = {
    "planes": {
        "gid": "gid://shopify/Collection/276253900849",
        "nombre": "Planes de entrenamiento",
        "sub": "Tres niveles · español, inglés y francés · PDF",
        "lamina": ("vi-sigilo", "0 0 600 600", 520),
        "acento": "#c9a227",
        "alt": ("Sigilo VILLUMINATIONS sobre fondo negro, con el nombre de "
                "la colección Planes de entrenamiento"),
    },
}

# Las que no se hacen, y por qué. Está escrito para que no se rehaga la
# pregunta dentro de tres meses.
SIN_PORTADA = {
    "cuidado-personal": ("los dos jabones están en UNLISTED, así que la "
                         "colección está vacía en la tienda"),
}

ANCHO, ALTO = 1600, 1000


def simbolos() -> str:
    fuera = []
    for r in LAMINAS:
        t = (RAIZ / r).read_text(encoding="utf-8")
        fuera += re.findall(r"<symbol\b.*?</symbol>", t, re.S)
    return "\n".join(fuera)


def tarjeta(p: dict) -> str:
    sid, vb, ancho = p["lamina"]
    a = p["acento"]
    return f"""<!doctype html><meta charset=utf-8><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{ANCHO}px;height:{ALTO}px;background:#0a0a0c;overflow:hidden;
 font-family:Georgia,'Times New Roman',serif;color:#f2f0ea;position:relative}}
.velo{{position:absolute;inset:0;background:
 radial-gradient(1100px 700px at 50% 38%, {a}22, transparent 68%)}}
.arte{{position:absolute;inset:0;display:flex;align-items:center;
 justify-content:center}}
.arte svg{{filter:drop-shadow(0 0 34px {a}55)}}
.pie{{position:absolute;left:0;right:0;bottom:96px;text-align:center}}
h1{{font-weight:400;font-size:70px;letter-spacing:.16em}}
p{{margin-top:20px;font-size:25px;letter-spacing:.05em;opacity:.66}}
.marca{{position:absolute;top:64px;left:0;right:0;text-align:center;
 font-size:19px;letter-spacing:.62em;opacity:.5}}
.regla{{position:absolute;left:50%;transform:translateX(-50%);bottom:74px;
 width:190px;height:2px;background:{a};opacity:.8}}
</style><svg width="0" height="0" style="position:absolute">{simbolos()}</svg>
<div class=velo></div>
<div class=arte><svg viewBox="{vb}" width="{ancho}"><use href="#{sid}"/></svg></div>
<div class=marca>VILLUMINATIONS</div>
<div class=pie><h1>{p['nombre']}</h1><p>{p['sub']}</p></div>
<div class=regla></div>"""


def comprobar() -> list:
    """Lo que impide dar una portada por buena."""
    malos = []
    disponibles = set()
    for r in LAMINAS:
        disponibles |= set(re.findall(r'<symbol[^>]*\bid="([^"]+)"',
                                      (RAIZ / r).read_text(encoding="utf-8")))
    for mango, p in PORTADAS.items():
        if p["lamina"][0] not in disponibles:
            malos.append(f"{mango} · la lámina «{p['lamina'][0]}» no está en "
                         f"ninguna de {LAMINAS}")
        if not p.get("alt"):
            malos.append(f"{mango} · sin texto alternativo: quien no ve la "
                         f"imagen no se entera de nada")
        elif len(p["alt"]) > 125:
            malos.append(f"{mango} · alt de {len(p['alt'])}/125")
    return malos


def main() -> int:
    malos = comprobar()
    print(f"\n  {len(PORTADAS)} portadas · {len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if malos:
        return 1

    DESTINO.mkdir(parents=True, exist_ok=True)
    guion = DESTINO / "_render.mjs"
    tareas = []
    for mango, p in PORTADAS.items():
        (DESTINO / f"{mango}.html").write_text(tarjeta(p), encoding="utf-8")
        tareas.append((str(DESTINO / f"{mango}.html"),
                       str(DESTINO / f"{mango}.png")))

    guion.write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        + "".join(
            f"{{const p = await b.newPage({{viewport:{{width:{ANCHO},"
            f"height:{ALTO}}}}});"
            f"await p.goto('file://{h}');"
            f"await p.screenshot({{path:'{o}'}});}}\n"
            for h, o in tareas)
        + "await b.close();\n", encoding="utf-8")

    r = subprocess.run(["node", str(guion)], capture_output=True, text=True)
    if r.returncode:
        print(f"    no se pudo renderizar:\n{r.stderr}")
        return 1

    for mango in PORTADAS:
        png = DESTINO / f"{mango}.png"
        print(f"    {png.relative_to(RAIZ)}  {png.stat().st_size // 1024} KB")
    print()
    for mango, razon in SIN_PORTADA.items():
        print(f"    sin portada a propósito · {mango}: {razon}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
