#!/usr/bin/env python3
"""
VILLUMINATIONS — Un paquete por producto, para la app de descargas
-------------------------------------------------------------------
`empaquetar.py` agrupa los PDF **por idioma**: todos los libros juntos, todos
los planes en español juntos. Sirve para archivar y para mandarle el lote a
alguien de una vez.

Lo que la tienda necesita es otra cosa. La app de descargas digitales adjunta
un fichero **a cada producto**, así que hacen falta once paquetes con los mismos
límites que el catálogo: uno por libro y uno por nivel. Quien compra el Códice
del Descanso no debe recibir los otros siete.

Qué lleva cada paquete:

· **Un libro** — sus tres ediciones: española, inglesa y francesa. 3 PDF.
· **Un nivel** — sus documentos en los tres idiomas, en versión de pantalla y
  en versión preparada para imprimir, que es lo que promete la ficha. Básico
  son 6 PDF; Pro, 30; Elite, 66.

Elite es acumulativo por definición: incluye los cinco de Pro y los once del
catálogo entero. Eso no es un descuido del empaquetado, es lo que se vende.

Los ZIP son deterministas —fecha fija y compresión fija—, así que dos pasadas
sobre las mismas fuentes dan ficheros idénticos byte a byte. Si el ZIP cambia
es porque cambió un PDF, no porque se haya vuelto a lanzar el script.

Uso:  python3 entregas.py            escribe entrega/productos/
      python3 entregas.py --listar   enseña qué va dentro de cada uno
"""

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIBROS = ROOT / "libros" / "dist"
PLANES = ROOT / "planes" / "dist"
SALIDA = ROOT / "entrega" / "productos"

FECHA = (2026, 1, 1, 0, 0, 0)

# handle en la tienda -> (nombre del libro, raíz del fichero en dist)
BIBLIOTECA = {
    "codice-de-la-mesa": "codice-mesa",
    "codice-de-la-carga": "codice-carga",
    "codice-del-descanso": "codice-descanso",
    "codice-de-la-voluntad": "codice-voluntad",
    "codice-de-los-arcanos": "codice-arcanos",
    "codice-del-si-mismo": "codice-si-mismo",
    "codice-zodiacal": "codice-zodiacal",
    "codice-de-las-invocaciones": "codice-invocaciones",
}

# handle en la tienda -> prefijos de los documentos que incluye
NIVELES = {
    "basico-volumen-limpio": ["01-basico"],
    "pro-definicion-volumen": ["01-basico", "02-pro", "03-pro", "04-pro",
                               "05-pro"],
    "elite-todo-incluido-coaching": ["01-basico", "02-pro", "03-pro", "04-pro",
                                     "05-pro", "06-elite", "07-elite",
                                     "08-elite", "09-elite", "10-elite",
                                     "11-elite"],
}

IDIOMAS = [("", "espanol"), ("en", "english"), ("fr", "francais")]


def libro(raiz: str) -> list[tuple[Path, str]]:
    """Las tres ediciones de un libro, con el nombre que verá el comprador."""
    piezas = []
    for sufijo, carpeta in IDIOMAS:
        sub = LIBROS / sufijo if sufijo else LIBROS
        nombre = f"{raiz}-{sufijo}.pdf" if sufijo else f"{raiz}.pdf"
        ruta = sub / nombre
        if not ruta.is_file():
            raise SystemExit(f"  Falta {ruta.relative_to(ROOT)}. "
                             "Lanza libros/build.py antes de empaquetar.")
        piezas.append((ruta, f"{carpeta}/{nombre}"))
    return piezas


def nivel(prefijos: list[str]) -> list[tuple[Path, str]]:
    """Los documentos de un nivel: tres idiomas por dos ediciones.

    La edición de impresión va en su propia carpeta dentro del ZIP. Mezclarlas
    en la misma haría que dos ficheros con el mismo nombre se pisaran.
    """
    piezas = []
    for edicion, base in (("pantalla", PLANES),
                          ("impresion", PLANES / "impresion")):
        for sufijo, carpeta in IDIOMAS:
            sub = base / sufijo if sufijo else base
            if not sub.is_dir():
                raise SystemExit(f"  Falta la carpeta {sub.relative_to(ROOT)}.")
            for pdf in sorted(sub.glob("*.pdf")):
                if any(pdf.name.startswith(p) for p in prefijos):
                    piezas.append((pdf, f"{edicion}/{carpeta}/{pdf.name}"))
    return piezas


def escribir(handle: str, piezas: list[tuple[Path, str]], listar: bool) -> int:
    destino = SALIDA / f"{handle}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=9) as z:
        for ruta, dentro in piezas:
            info = zipfile.ZipInfo(dentro, date_time=FECHA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, ruta.read_bytes())
    mb = destino.stat().st_size / 1_048_576
    print(f"    {handle + '.zip':40} {len(piezas):3} PDF · {mb:6.1f} MB")
    if listar:
        for _, dentro in piezas:
            print(f"        {dentro}")
    return len(piezas)


def main() -> None:
    listar = "--listar" in sys.argv
    SALIDA.mkdir(parents=True, exist_ok=True)
    print(f"\n  Paquetes por producto → {SALIDA.relative_to(ROOT)}\n")

    total = 0
    for handle, raiz in BIBLIOTECA.items():
        total += escribir(handle, libro(raiz), listar)
    print()
    for handle, prefijos in NIVELES.items():
        total += escribir(handle, nivel(prefijos), listar)

    cuantos = len(BIBLIOTECA) + len(NIVELES)
    print(f"\n  {cuantos} paquetes · {total} PDF adjuntados en total\n")


if __name__ == "__main__":
    main()
