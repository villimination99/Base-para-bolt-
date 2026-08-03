#!/usr/bin/env python3
"""
CARGADOR DE TRADUCCIONES DE LOS LIBROS
======================================
Igual que el de los planes: las traducciones se escriben en i18n/fuentes/*.py
como diccionarios que van del ORIGINAL EN ESPAÑOL a sus versiones, y este
cargador comprueba tres cosas antes de aceptar nada.

  1. Que el original exista de verdad en algún libro. Una cadena mal copiada
     se quedaría en el catálogo pareciendo trabajo hecho mientras la página
     sigue en español.
  2. Que el marcado en línea coincida. Si el original lleva <em>…</em> y la
     traducción no, el diseño se rompe en silencio.
  3. Que el catálogo resultante se escriba indexado por hash, que es lo que
     consume el generador.

    python3 tools/cargar-traducciones.py
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tools"))
sys.path.insert(0, str(RAIZ))
import i18n                                                    # noqa: E402

FUENTES = RAIZ / "i18n" / "fuentes"


def etiquetas(texto: str) -> list[str]:
    """Las etiquetas de un segmento, en orden, sin atributos volátiles."""
    return [t.lower() for t in re.findall(r"<\s*(/?[a-zA-Z][\w:-]*)", texto)]


def pegado(t: str) -> str:
    """El texto con los espacios entre etiquetas colapsados.

    Al copiar un original es fácil dejar un salto de línea donde no lo había.
    Ese detalle invisible no debe costar una ronda de correcciones, así que se
    empareja también por esta vía — pero la CLAVE se calcula siempre desde el
    original real del libro, nunca desde lo que se tecleó.
    """
    return re.sub(r">\s+<", "><", re.sub(r"\s+", " ", t)).strip()


def main() -> None:
    documentos = dict(i18n._documentos_es())
    inv_total = i18n.inventario(d for docs in documentos.values() for d in docs)
    por_texto = {re.sub(r"\s+", " ", v).strip(): k for k, v in inv_total.items()}
    por_pegado = {}
    for k, v in inv_total.items():
        por_pegado.setdefault(pegado(v), (k, v))

    catalogo, errores, entradas = {}, [], 0
    for modulo in sorted(FUENTES.glob("*.py")):
        spec = importlib.util.spec_from_file_location(modulo.stem, modulo)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for original, versiones in getattr(mod, "T", {}).items():
            plano = re.sub(r"\s+", " ", original).strip()
            entradas += 1
            if plano in por_texto:
                clave_seg = por_texto[plano]
            elif pegado(original) in por_pegado:
                clave_seg, _ = por_pegado[pegado(original)]
            else:
                errores.append(f"{modulo.name}: original inexistente en los "
                               f"libros → «{plano[:70]}»")
                continue
            for idioma, destino in versiones.items():
                if idioma not in i18n.IDIOMAS:
                    errores.append(f"{modulo.name}: idioma «{idioma}» no soportado")
                    continue
                if etiquetas(destino) != etiquetas(plano):
                    errores.append(f"{modulo.name} [{idioma}]: el marcado no "
                                   f"coincide → «{plano[:50]}»")
                    continue
                catalogo.setdefault(clave_seg, {})[idioma] = destino

    if errores:
        print(f"\n{len(errores)} problema(s):")
        for e in errores[:25]:
            print("  ·", e)
        raise SystemExit("\nNo se escribe el catálogo con errores dentro.")

    i18n.guardar(catalogo)
    print(f"  {entradas} originales · {len(catalogo)} entradas de catálogo")
    for cod, (nombre, _) in i18n.IDIOMAS.items():
        if cod == "es":
            continue
        hechos = sum(1 for k in inv_total if catalogo.get(k, {}).get(cod))
        print(f"    {nombre:<10} {hechos:>5}/{len(inv_total)}  "
              f"{100 * hechos / max(len(inv_total), 1):5.1f} %")

    print("\n  Cobertura por libro")
    for nombre, docs in documentos.items():
        inv = i18n.inventario(docs)
        linea = f"    {nombre:<24}"
        for cod in i18n.IDIOMAS:
            if cod == "es":
                continue
            n = sum(1 for k in inv if catalogo.get(k, {}).get(cod))
            linea += f"  {cod} {n:>4}/{len(inv):<4}{'OK' if n == len(inv) else '  '}"
        print(linea)


if __name__ == "__main__":
    main()
