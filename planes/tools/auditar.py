#!/usr/bin/env python3
"""
AUDITORÍA DE LOS PDF PUBLICADOS
===============================
Lo que se vende es el PDF, no el HTML. Este script abre cada archivo de dist/
y comprueba, uno por uno, lo que un comprador notaría:

  1. El texto se puede seleccionar y buscar (fuentes Type0 incrustadas). Una
     fuente Type3 significa que Chromium dibujó las letras como trazos: el PDF
     pesa el triple y no se puede copiar ni una palabra.
  2. Hay marcadores de navegación, uno por página.
  3. Título, autor y asunto están puestos: es lo que se ve en la pestaña del
     lector y en la biblioteca del comprador.
  4. La marca aparece como VILLUMINATIONS, nunca «VILLUMINATIONS 99».
  5. La edición inglesa y la francesa no arrastran español. Los centinelas son
     POR IDIOMA: «muscular» es correcto en inglés y es un fallo en francés, así
     que vigilarlo en los dos daría un falso positivo cada vez.
  6. Las tres ediciones de un mismo documento tienen el mismo número de
     páginas. Si la francesa tiene una de más, algo se ha desbordado.

    python3 tools/auditar.py            # dist/ entero
    python3 tools/auditar.py dist/en    # solo una edición

La comprobación 6 vale para los planes y NO vale para los libros. Un plan tiene
una retícula fija: cada apartado ocupa el sitio que se le asignó, y una página
de más significa que una traducción larga ha empujado algo fuera de su caja. Un
libro fluye, se pagina solo y lleva un índice que se recompone: que la edición
francesa tenga cuatro páginas más que la inglesa es lo normal y no delata nada.
Por eso los libros se auditan con --paginas-libres, que hace las cinco primeras
comprobaciones y se salta la sexta en vez de fingir un descuadre.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Español que no debería sobrevivir a una traducción. Se eligen palabras y
# signos que no existen en el idioma de destino: los nombres propios de plato
# (gazpacho, paella, salmorejo) se conservan a propósito y por eso no están.
CENTINELAS = {
    "en": ["¿", "¡", " los ", " las ", " del ", " para ", " una ", " este ",
           " esta ", " pero ", " porque ", " siempre ", " nunca ", " más ",
           " muy ", " según", " también", " días", " semana", " entrenamiento",
           " proteína", " ejercicio", "musculaire"],
    "fr": ["¿", "¡", " los ", " las ", " del ", " para ", " una ", " este ",
           " esta ", " pero ", " porque ", " siempre ", " nunca ", " más ",
           " muy ", " según", " también", " días", " semana", " entrenamiento",
           " proteína", " ejercicio", " muscular", " weight ", " training "],
}
# «ñ» se comprueba aparte: como carácter suelto es la señal más limpia de que
# ha quedado una cadena sin traducir, y no existe ni en inglés ni en francés.


def texto(pdf: Path) -> str:
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    partes = [doc[i].get_textpage().get_text_range() for i in range(len(doc))]
    doc.close()
    return re.sub(r"\s+", " ", " ".join(partes))


def fuentes(pdf: Path) -> set:
    from pypdf import PdfReader

    tipos = set()
    for pagina in PdfReader(str(pdf)).pages:
        recursos = pagina.get("/Resources", {})
        for fuente in (recursos.get("/Font") or {}).values():
            obj = fuente.get_object()
            tipos.add(str(obj.get("/Subtype", "?")))
    return tipos


def contar_marcadores(nodo) -> int:
    """Cuenta el árbol de marcadores entero, no solo su primer nivel.

    Un plan trae una lista plana, un marcador por página. Un libro trae un
    árbol: el título del volumen y, colgando de él, un marcador por capítulo.
    len() sobre ese árbol devuelve 2 —el tronco y la lista de hijos— y eso
    hacía que los ocho libros fallaran a la vez por un defecto que no tenían.
    """
    if isinstance(nodo, list):
        return sum(contar_marcadores(hijo) for hijo in nodo)
    return 1


def auditar(pdf: Path, idioma: str, paginas_libres: bool = False) -> list[str]:
    from pypdf import PdfReader

    fallos = []
    lector = PdfReader(str(pdf))
    paginas = len(lector.pages)

    tipos = fuentes(pdf)
    if "/Type3" in tipos:
        fallos.append("fuentes Type3: el texto está dibujado, no se puede copiar")
    if not tipos:
        fallos.append("ninguna fuente incrustada")

    try:
        marcadores = contar_marcadores(lector.outline)
    except Exception:
        marcadores = 0
    # Un plan lleva un marcador por página porque cada página es un apartado.
    # Un libro lleva uno por capítulo, y el criterio pasa a ser el del lector:
    # que nadie tenga que recorrer más de diez páginas para saber dónde está.
    minimo = -(-paginas // 10) if paginas_libres else paginas - 1
    if marcadores < minimo:
        fallos.append(f"solo {marcadores} marcadores para {paginas} páginas "
                      f"(hacen falta {minimo})")

    meta = lector.metadata or {}
    for clave in ("/Title", "/Author", "/Subject"):
        if not meta.get(clave):
            fallos.append(f"falta {clave} en los metadatos")

    cuerpo = texto(pdf)
    # El logotipo lleva letter-spacing, así que el extractor devuelve
    # «V I L L U M I N AT I O N S». Buscar la marca sobre el texto tal cual
    # daría un falso negativo en cada portada: se compara sin espacios.
    apretado = cuerpo.replace(" ", "").replace(" ", "")
    if "VILLUMINATIONS99" in apretado:
        fallos.append("aparece «VILLUMINATIONS 99»")
    if "VILLUMINATIONS" not in apretado:
        fallos.append("la marca no aparece en el texto")

    if idioma != "es":
        residuo = [c for c in CENTINELAS[idioma] if c in cuerpo]
        if "ñ" in cuerpo:
            residuo.append("ñ")
        if residuo:
            fallos.append("español sin traducir → " + ", ".join(repr(r) for r in residuo[:6]))

    return fallos


def raiz_dist(pdf: Path) -> Path:
    """El dist/ que contiene a este PDF, sea el de planes o el de libros.

    Se busca hacia arriba en vez de darlo por sentado: el script se invoca
    también sobre libros/dist, y colgar la ruta de la raíz de planes convertía
    una auditoría de libros en un ValueError."""
    for padre in pdf.parents:
        if padre.name == "dist":
            return padre
    return pdf.parent


def main() -> None:
    argumentos = [a for a in sys.argv[1:] if a != "--paginas-libres"]
    comparar_paginas = "--paginas-libres" not in sys.argv[1:]
    objetivos = [Path(a) for a in argumentos] or [RAIZ / "dist"]
    archivos = []
    for o in objetivos:
        archivos.extend(sorted(o.rglob("*.pdf")) if o.is_dir() else [o])
    if not archivos:
        raise SystemExit("No hay PDF que auditar. ¿Has ejecutado build.py?")

    from pypdf import PdfReader

    total, malos = 0, 0
    por_documento = defaultdict(dict)
    for pdf in archivos:
        # dist/[impresion/][<idioma>/]<stem>[-<idioma>].pdf
        #
        # La edición de impresión tiene su propia paginación (no lleva las
        # mismas separatas que la de pantalla), así que forma una familia
        # aparte: compararla con la de pantalla daría un descuadre falso.
        partes = pdf.relative_to(raiz_dist(pdf)).parts
        idioma = next((p for p in partes if p in ("en", "fr")), "es")
        familia = ("impresion · " if "impresion" in partes else "pantalla · ")
        base = familia + re.sub(r"-(en|fr)\.pdf$", ".pdf", pdf.name)
        por_documento[base][idioma] = len(PdfReader(str(pdf)).pages)

        total += 1
        fallos = auditar(pdf, idioma, paginas_libres=not comparar_paginas)
        if fallos:
            malos += 1
            print(f"\n  {raiz_dist(pdf).name}/{'/'.join(partes)}")
            for f in fallos:
                print(f"      · {f}")

    descuadres = 0
    if comparar_paginas:
        print("\n  Paginación comparada")
        for base, cuentas in sorted(por_documento.items()):
            if len(set(cuentas.values())) > 1:
                descuadres += 1
                detalle = "  ".join(f"{k} {v}" for k, v in sorted(cuentas.items()))
                print(f"    DESCUADRE  {base:<58} {detalle}")
        if not descuadres:
            print("    Las tres ediciones de cada documento tienen las mismas páginas.")
    else:
        print("\n  Paginación libre: no se comparan las ediciones entre sí.")

    print(f"\n  {total} PDF auditados · {malos} con problemas · "
          f"{descuadres} descuadres de paginación")
    raise SystemExit(1 if (malos or descuadres) else 0)


if __name__ == "__main__":
    main()
