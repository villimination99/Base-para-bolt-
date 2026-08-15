#!/usr/bin/env python3
"""
VILLUMINATIONS — Paquete para la estampadora
=============================================
Convierte los SVG de `ropa/dist/` en PNG a resolución de impresión, con fondo
transparente, y lo mete todo en un ZIP.

    python3 ropa/tools/empaquetar.py

**Por qué PNG si el SVG es mejor.** Lo es, y por eso va también: escala sin
perder filo. Pero casi ninguna aplicación de estampación bajo demanda acepta
SVG —Printful y Printify piden PNG—, así que el paquete lleva las dos cosas: el
SVG como original del que se puede volver a sacar cualquier tamaño, y el PNG
listo para arrastrar.

**300 puntos por pulgada, fondo transparente.** Son las dos condiciones que
piden todas: menos de 300 y la estampación sale borrosa; con fondo blanco sale
un recuadro blanco alrededor del dibujo sobre una camiseta negra.

El ZIP se escribe con fecha fija para que dos pasadas den el mismo fichero.
"""

import shutil
import subprocess
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIST = RAIZ / "dist"
PNG = RAIZ / "dist" / "png"
ZIP = RAIZ / "dist" / "VILLUMINATIONS-VI-estampacion.zip"

CHROMIUM = "/opt/pw-browsers/chromium"
DPI = 300

# pieza -> (ancho_px, alto_px, pulgadas, para qué)
MEDIDAS = {
    "vi-dorsal": (3600, 4800, "12 × 16 pulgadas",
                  "espalda completa · sudadera y camiseta"),
    "vi-sigilo": (3000, 3000, "10 × 10 pulgadas",
                  "pecho centrado, o reducido a 4 pulgadas para el corazón"),
    "vi-manga":  (1200, 4400, "4 × 14,7 pulgadas",
                  "manga, de hombro a puño"),
}

LEEME = """VILLUMINATIONS · VI — grafismos para estampar
=============================================

Qué hay aquí
------------
  svg/    los originales vectoriales. Escalan a cualquier tamaño sin
          perder filo. Guárdalos: de aquí sale todo lo demás.
  png/    a 300 puntos por pulgada y con fondo transparente, que es lo
          que piden Printful, Printify y las demás.

Las tres piezas
---------------
{piezas}

Los colores
-----------
  cian, magenta, verde, naranja, púrpura, hueso   para prenda NEGRA
  tinta                                            para prenda CLARA

  Los neones no se ven sobre blanco. Si vas a sacar la prenda en color
  claro, usa «tinta».

Cómo subirlo
------------
  1. En la aplicación de estampación, crea el producto y elige la prenda
     blanca.
  2. Sube el PNG que toque —dorsal para la espalda, sigilo para el
     pecho, manga para la manga.
  3. Encájalo dentro del área imprimible SIN estirarlo. Si la aplicación
     avisa de baja resolución, algo se ha reescalado: vuelve al PNG
     original.
  4. Para la ficha del producto, pásame la hoja de especificaciones de
     la prenda —composición, gramaje, tallas, colores y método— y la
     escribo en las tres lenguas.

De dónde salen
--------------
Están dibujados por geometría, con la misma construcción que las láminas
de los códices: ruedas de grados, anillos de conteo y escalas que se
pueden contar con el dedo. El monograma es VI, de VILLUMINATIONS, montado
como un sextante: los dos brazos son el arco graduado y la I es la barra
índice que cae a plomo.

El dibujo es propio. No es una imagen de banco ni un encargo de fuera, y
se regenera entero con:

    python3 ropa/tools/dibujar-marca.py
"""


def a_png(svg: Path, ancho: int, alto: int, destino: Path) -> None:
    """Rasteriza un SVG al tamaño exacto, con el fondo transparente."""
    envoltura = destino.parent / f"_{destino.stem}.html"
    envoltura.write_text(
        f'<!doctype html><meta charset="utf-8">'
        f'<style>html,body{{margin:0;padding:0;background:transparent}}'
        f'img{{display:block;width:{ancho}px;height:{alto}px}}</style>'
        f'<img src="{svg.name}">', encoding="utf-8")
    shutil.copy(svg, destino.parent / svg.name)
    subprocess.run(
        [CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox",
         "--hide-scrollbars", "--default-background-color=00000000",
         f"--screenshot={destino}", f"--window-size={ancho},{alto}",
         str(envoltura)],
        capture_output=True, timeout=180)
    envoltura.unlink(missing_ok=True)
    (destino.parent / svg.name).unlink(missing_ok=True)


def main() -> int:
    PNG.mkdir(parents=True, exist_ok=True)
    hechos = []
    for svg in sorted(DIST.glob("vi-*.svg")):
        pieza = "-".join(svg.stem.split("-")[:2])
        if pieza not in MEDIDAS:
            continue
        ancho, alto, _, _ = MEDIDAS[pieza]
        destino = PNG / f"{svg.stem}.png"
        a_png(svg, ancho, alto, destino)
        hechos.append(destino)
        print(f"    {destino.name:28} {ancho}×{alto}")

    piezas = "\n".join(
        f"  {n:12} {m[2]:22} {m[3]}" for n, m in MEDIDAS.items())
    leeme = LEEME.format(piezas=piezas)

    fijo = (2026, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        info = zipfile.ZipInfo("LEEME.txt", fijo)
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, leeme)
        for svg in sorted(DIST.glob("vi-*.svg")):
            info = zipfile.ZipInfo(f"svg/{svg.name}", fijo)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, svg.read_bytes())
        for png in sorted(hechos):
            info = zipfile.ZipInfo(f"png/{png.name}", fijo)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, png.read_bytes())

    print(f"\n  {ZIP.relative_to(RAIZ.parent)} · "
          f"{ZIP.stat().st_size / 1024 / 1024:.1f} MB · "
          f"{len(hechos)} PNG y {len(list(DIST.glob('vi-*.svg')))} SVG\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
