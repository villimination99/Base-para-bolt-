#!/usr/bin/env python3
"""
Prepara las fuentes de marca (Orbitron y Rajdhani) para incrustarlas en PDF.

Por qué hace falta este paso
----------------------------
Orbitron se distribuye como *fuente variable* (un solo archivo con el eje
`wght` de 400 a 900). Chromium no sabe incrustar fuentes variables en un PDF:
las convierte en fuentes Type3, es decir, dibuja cada letra como un programa
de trazos independiente y crea una fuente distinta por cada tamaño usado.
El resultado son PDFs enormes con texto no seleccionable.

La solución es fijar («instanciar») el eje de peso para obtener fuentes
estáticas normales, que Chromium sí incrusta como TrueType y subconjunta.

Uso:  python3 tools/preparar-fuentes.py
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "fonts"
CSS = ROOT / "assets" / "fonts.css"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

FAMILIES = {
    "Orbitron": [400, 700, 900],
    "Rajdhani": [300, 400, 500, 600, 700],
}


def fetch(url: str, binary: bool = False):
    res = subprocess.run(
        ["curl", "-sSL", url, "-H", f"User-Agent: {UA}"], capture_output=True
    )
    if res.returncode != 0:
        raise SystemExit(f"No se pudo descargar {url}")
    return res.stdout if binary else res.stdout.decode()


def main() -> None:
    try:
        from fontTools.ttLib import TTFont
        from fontTools.varLib import instancer
    except ImportError:
        raise SystemExit("Falta fontTools:  pip install fonttools brotli")

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*"):
        old.unlink()

    faces = []
    for family, weights in FAMILIES.items():
        spec = ";".join(str(w) for w in weights)
        css = fetch(f"https://fonts.googleapis.com/css2?family={family}:wght@{spec}")

        # Solo nos interesan los subconjuntos latin y latin-ext.
        seen_weights = set()
        for block in css.split("/*"):
            name = block.split("*/")[0].strip()
            if name not in ("latin", "latin-ext"):
                continue
            weight = re.search(r"font-weight:\s*(\d+)", block)
            url = re.search(r"url\((https://[^)]+)\)", block)
            if not (weight and url):
                continue
            weight = int(weight.group(1))
            # El subconjunto latin-ext repite pesos: nos quedamos con el primero,
            # que tras instanciar contiene ya todos los glifos que usamos.
            if weight in seen_weights:
                continue
            seen_weights.add(weight)

            raw = fetch(url.group(1), binary=True)
            tmp = OUT / f".{family}-{weight}.woff2"
            tmp.write_bytes(raw)

            font = TTFont(str(tmp))
            if "fvar" in font:
                font = instancer.instantiateVariableFont(font, {"wght": weight})
                estado = "instanciada"
            else:
                estado = "ya estática"
            font.flavor = None  # guardar como TTF sin comprimir
            dest = OUT / f"{family.lower()}-{weight}.ttf"
            font.save(str(dest))
            tmp.unlink()

            faces.append((family, weight, dest.name))
            print(f"  {family} {weight}: {estado} → {dest.name} "
                  f"({dest.stat().st_size / 1024:.0f} KB)")

    lines = [
        "/* Fuentes de marca. Generado por tools/preparar-fuentes.py — no editar a mano.",
        "   Instancias estáticas: Chromium no incrusta fuentes variables en PDF. */",
    ]
    for family, weight, filename in faces:
        lines.append(
            f"@font-face{{font-family:'{family}';font-style:normal;"
            f"font-weight:{weight};font-display:block;"
            f"src:url(fonts/{filename}) format('truetype')}}"
        )
    CSS.write_text("\n".join(lines) + "\n")
    print(f"\n{len(faces)} fuentes listas · {CSS.relative_to(ROOT)} actualizado")


if __name__ == "__main__":
    sys.exit(main())
