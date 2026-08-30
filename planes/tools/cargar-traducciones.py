#!/usr/bin/env python3
"""
CARGADOR DE TRADUCCIONES
========================
Las traducciones se escriben en i18n/fuentes/*.py como diccionarios que van
del ORIGINAL EN ESPAÑOL a sus versiones. Se escribe el español y no el hash,
por dos motivos: se lee, y sobre todo se puede verificar.

Este cargador hace tres cosas antes de aceptar nada:

  1. Comprueba que cada original exista de verdad en los planes. Una cadena
     que no aparece en ningún documento es un original mal copiado, y sin esta
     comprobación se quedaría en el catálogo pareciendo trabajo hecho mientras
     el documento sigue en español.
  2. Comprueba que el marcado en línea coincida. Si el original lleva
     <strong>…</strong> y la traducción no, el diseño se rompe en silencio; si
     lleva un <br> de menos, el salto de línea desaparece.
  3. Escribe el catálogo indexado por hash, que es lo que consume el
     generador.

    python3 tools/cargar-traducciones.py
"""

import importlib.util
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import i18n                                                    # noqa: E402
from build import assemble                                     # noqa: E402


def documento(ruta: Path) -> str:
    """El HTML tal y como lo verá el comprador, con las láminas dentro."""
    return assemble(ruta.read_text(encoding="utf-8"))

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "i18n" / "fuentes"


def etiquetas(texto: str) -> list[str]:
    """Las etiquetas de un segmento, en orden, sin atributos volátiles."""
    return [t.lower() for t in re.findall(r"<\s*(/?[a-zA-Z][\w:-]*)", texto)]


def main() -> None:
    inventario = i18n.inventario(
        [documento(r) for r in sorted((RAIZ / 'src').glob('*.html'))])
    por_texto = {re.sub(r"\s+", " ", v).strip(): k
                 for k, v in inventario.items()}

    # Segunda vía de emparejamiento: la misma cadena con los espacios entre
    # etiquetas colapsados. Al copiar un original desde el fuente es fácil
    # dejar un salto de línea donde no lo había, y ese detalle invisible no
    # debe costar una ronda de correcciones. La CLAVE se calcula siempre
    # desde el original real del documento, nunca desde lo que se tecleó.
    def pegado(t: str) -> str:
        return re.sub(r">\s+<", "><", re.sub(r"\s+", " ", t)).strip()

    por_pegado = {}
    for k, v in inventario.items():
        por_pegado.setdefault(pegado(v), (k, v))

    catalogo, errores, entradas = {}, [], 0
    for modulo in sorted(FUENTES.glob("*.py")):
        spec = importlib.util.spec_from_file_location(modulo.stem, modulo)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for original, versiones in getattr(mod, "T", {}).items():
            plano = re.sub(r"\s+", " ", original).strip()
            entradas += 1
            real = original
            if plano in por_texto:
                clave_seg = por_texto[plano]
            elif pegado(original) in por_pegado:
                clave_seg, real = por_pegado[pegado(original)]
            else:
                errores.append(f"{modulo.name}: original inexistente en los "
                               f"planes → «{plano[:70]}»")
                continue
            for idioma, destino in versiones.items():
                if idioma not in i18n.IDIOMAS:
                    errores.append(f"{modulo.name}: idioma «{idioma}» no "
                                   "soportado")
                    continue
                if etiquetas(destino) != etiquetas(plano):
                    errores.append(
                        f"{modulo.name} [{idioma}]: el marcado no coincide → "
                        f"«{plano[:50]}»")
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
        hechos = sum(1 for k in inventario if catalogo.get(k, {}).get(cod))
        print(f"    {nombre:<10} {hechos:>4}/{len(inventario)}  "
              f"{100 * hechos / max(len(inventario), 1):5.1f} %")

    # Cobertura por documento: es la que decide si un PDF se puede publicar.
    print("\n  Cobertura por documento")
    for ruta in sorted((RAIZ / "src").glob("*.html")):
        inv = i18n.inventario([documento(ruta)])
        linea = f"    {ruta.stem[:40]:<42}"
        for cod in i18n.IDIOMAS:
            if cod == "es":
                continue
            n = sum(1 for k in inv if catalogo.get(k, {}).get(cod))
            marca = "OK " if n == len(inv) else "   "
            linea += f"  {cod} {n:>3}/{len(inv):<3}{marca}"
        print(linea)


if __name__ == "__main__":
    main()
