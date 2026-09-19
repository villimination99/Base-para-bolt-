#!/usr/bin/env python3
"""
QUÉ FALTA POR TRADUCIR
======================
Vuelca los segmentos de un documento que todavía no tienen traducción, en el
formato exacto que espera un módulo de i18n/fuentes/. Así el original se copia
de la máquina y no de la vista, que es de donde salían los desajustes de un
salto de línea.

    python3 tools/faltan.py 03          # los que faltan del plan 03
    python3 tools/faltan.py 03 --todos  # todos sus segmentos
    python3 tools/faltan.py             # cuántos faltan en cada plan
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import i18n                                                    # noqa: E402
from build import assemble                                     # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def documentos() -> list[Path]:
    return sorted((RAIZ / "src").glob("*.html"))


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    todos = "--todos" in sys.argv
    cat = i18n.cargar()

    if not args:
        for ruta in documentos():
            inv = i18n.inventario([assemble(ruta.read_text(encoding="utf-8"))])
            falta = [k for k in inv
                     if not all(cat.get(k, {}).get(c)
                                for c in i18n.IDIOMAS if c != "es")]
            print(f"  {ruta.stem[:44]:<46} faltan {len(falta):>4} de {len(inv)}")
        return

    rutas = [r for r in documentos() if any(a in r.stem for a in args)]
    if not rutas:
        raise SystemExit(f"Ningún plan coincide con {args}")

    for ruta in rutas:
        inv = i18n.inventario([assemble(ruta.read_text(encoding="utf-8"))])
        print(f"# ── {ruta.stem} ──")
        n = 0
        for k, texto in inv.items():
            hecho = all(cat.get(k, {}).get(c)
                        for c in i18n.IDIOMAS if c != "es")
            if hecho and not todos:
                continue
            n += 1
            print(f'    """{texto}""":')
            print('        {"en": "", "fr": ""},')
        print(f"# {n} segmento(s)\n")


if __name__ == "__main__":
    main()
