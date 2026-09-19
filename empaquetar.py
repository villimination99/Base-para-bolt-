#!/usr/bin/env python3
"""
VILLUMINATIONS — Empaquetado de entrega
---------------------------------------
Junta los PDF de planes/dist y libros/dist en los ZIP que se suben a la
tienda. No renderiza nada: se lanza después de build.py y de la auditoría, y
lo único que hace es recoger lo que ya está aprobado.

Existe porque los ZIP se habían montado a mano y se quedaron atrás: el de
libros llevaba dos títulos cuando el catálogo ya tenía ocho. Un paquete que se
arma a mano se desactualiza en cuanto el catálogo crece, y el comprador no
tiene forma de saberlo — recibe menos de lo que pagó y nadie se entera.

Cada paquete declara qué espera encontrar. Si falta un PDF o sobra uno que no
estaba previsto, no se escribe el ZIP: se dice qué pasa y se sale con error.
Es la misma regla que la cobertura de traducción — más vale no publicar que
publicar incompleto.

Uso:  python3 empaquetar.py            escribe entrega/*.zip
      python3 empaquetar.py --listar   solo dice qué llevaría cada uno
"""

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTREGA = ROOT / "entrega"

# Fecha fija en las entradas del ZIP. El contenido manda: si los PDF no han
# cambiado, el ZIP sale byte a byte idéntico y el repositorio no se ensucia
# con un binario nuevo cada vez que se lanza esto.
FECHA = (2026, 1, 1, 0, 0, 0)

PLANES = ROOT / "planes" / "dist"
LIBROS = ROOT / "libros" / "dist"

# nombre del ZIP -> [(carpeta de origen, prefijo dentro del ZIP, nº de PDF)]
PAQUETES: dict[str, list[tuple[Path, str, int]]] = {
    "VILLUMINATIONS-planes-espanol": [(PLANES, "", 11)],
    "VILLUMINATIONS-planes-english": [(PLANES / "en", "en/", 11)],
    "VILLUMINATIONS-planes-francais": [(PLANES / "fr", "fr/", 11)],
    "VILLUMINATIONS-planes-impresion": [
        (PLANES / "impresion", "impresion/", 11),
        (PLANES / "impresion" / "en", "impresion/en/", 11),
        (PLANES / "impresion" / "fr", "impresion/fr/", 11),
    ],
    "VILLUMINATIONS-libros-trilingues": [
        (LIBROS, "", 8),
        (LIBROS / "en", "en/", 8),
        (LIBROS / "fr", "fr/", 8),
    ],
}


def recoger(carpeta: Path, esperados: int) -> list[Path]:
    """Los PDF de una carpeta, sin bajar a las subcarpetas y en orden.

    Sin recursión a propósito: dist/ anida los idiomas y la edición de
    impresión unos dentro de otros, así que un glob recursivo metería el
    inglés dentro del paquete español sin avisar. Cada tramo del paquete
    nombra su carpeta y solo esa.
    """
    if not carpeta.is_dir():
        raise SystemExit(f"  Falta la carpeta {carpeta.relative_to(ROOT)}. "
                         "Lanza build.py antes de empaquetar.")
    pdfs = sorted(p for p in carpeta.glob("*.pdf") if p.is_file())
    if len(pdfs) != esperados:
        raise SystemExit(
            f"  {carpeta.relative_to(ROOT)}: {len(pdfs)} PDF y se esperaban "
            f"{esperados}. El paquete no se escribe hasta que cuadre.")
    return pdfs


def escribir(nombre: str, tramos: list[tuple[Path, str, int]],
             listar: bool) -> int:
    total = 0
    contenido: list[tuple[str, Path]] = []
    for carpeta, prefijo, esperados in tramos:
        for pdf in recoger(carpeta, esperados):
            contenido.append((prefijo + pdf.name, pdf))
            total += 1

    if listar:
        print(f"\n  {nombre}.zip · {total} PDF")
        for interno, _ in contenido:
            print(f"    {interno}")
        return total

    ENTREGA.mkdir(exist_ok=True)
    destino = ENTREGA / f"{nombre}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        # Las carpetas se declaran para que el ZIP se abra igual en todos los
        # descompresores, incluido el de Windows, que con algunos no crea los
        # directorios implícitos.
        for prefijo in dict.fromkeys(p for _, p, _ in tramos if p):
            info = zipfile.ZipInfo(prefijo, FECHA)
            info.external_attr = (0o40755 << 16) | 0x10
            z.writestr(info, b"")
        for interno, pdf in contenido:
            info = zipfile.ZipInfo(interno, FECHA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, pdf.read_bytes())

    peso = destino.stat().st_size / 1024 / 1024
    print(f"  {destino.name:<42} {total:>3} PDF  {peso:>6.1f} MB")
    return total


def main() -> None:
    listar = "--listar" in sys.argv[1:]
    print("\n  Entrega VILLUMINATIONS" + ("  ·  solo listado" if listar else ""))
    total = sum(escribir(n, t, listar) for n, t in PAQUETES.items())
    print(f"\n  {len(PAQUETES)} paquetes · {total} PDF en total\n")


if __name__ == "__main__":
    main()
