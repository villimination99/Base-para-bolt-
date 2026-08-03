#!/usr/bin/env python3
"""
QUÉ FALTA POR TRADUCIR EN LOS LIBROS
====================================
Vuelca los segmentos que todavía no tienen traducción, en el formato exacto
que espera un módulo de i18n/fuentes/. El original se copia de la máquina y no
de la vista: es de copiarlo a mano de donde salían los desajustes por un salto
de línea.

    python3 tools/faltan.py voluntad            # los que faltan
    python3 tools/faltan.py voluntad --desde 200 --hasta 400
    python3 tools/faltan.py                     # cuántos faltan en cada libro
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tools"))
sys.path.insert(0, str(RAIZ))
import i18n                                                    # noqa: E402


def entero(bandera: str, defecto):
    if bandera in sys.argv:
        return int(sys.argv[sys.argv.index(bandera) + 1])
    return defecto


def main() -> None:
    filtros = [a for a in sys.argv[1:] if not a.startswith("--") and not a.isdigit()]
    cat = i18n.cargar()
    idiomas = [c for c in i18n.IDIOMAS if c != "es"]

    documentos = dict(i18n._documentos_es())
    if not filtros:
        for nombre, html in documentos.items():
            inv = i18n.inventario([html])
            falta = [k for k in inv
                     if not all(cat.get(k, {}).get(c) for c in idiomas)]
            print(f"  {nombre:<26} faltan {len(falta):>5} de {len(inv)}")
        return

    elegidos = {n: h for n, h in documentos.items() if any(f in n for f in filtros)}
    if not elegidos:
        raise SystemExit(f"Ningún libro coincide con {filtros}")

    desde, hasta = entero("--desde", 0), entero("--hasta", 10**9)
    for nombre, html in elegidos.items():
        inv = i18n.inventario([html])
        pendientes = [(k, t) for k, t in inv.items()
                      if not all(cat.get(k, {}).get(c) for c in idiomas)]
        print(f"# ── {nombre} · {len(pendientes)} pendientes ──")
        for i, (_, texto) in enumerate(pendientes):
            if not (desde <= i < hasta):
                continue
            print(f'    """{texto}""":')
            print('        {"en": "", "fr": ""},')
        print(f"# mostrados {max(0, min(hasta, len(pendientes)) - desde)}\n")


if __name__ == "__main__":
    main()
