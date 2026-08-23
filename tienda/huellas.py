#!/usr/bin/env python3
"""
VILLUMINATIONS — Qué ha cambiado desde la última vez que se registró
====================================================================

    python3 tienda/huellas.py             # qué habría que volver a registrar
    python3 tienda/huellas.py --sellar    # dar por registrado lo de ahora
    python3 tienda/huellas.py --desde HEAD~1   # qué cambió en el último commit

El problema que resuelve
------------------------
Traducir un artículo **caduca la traducción ya registrada de los que lo
citan**: su cuerpo se compone distinto en cuanto el destino existe, porque
`_descolgar()` le devuelve el ancla. Lo mismo pasa al mover un enlace de
`lecturas.MAPA`: el bloque «Del Diario» de esa ficha cambia y lo que hay en
la tienda se queda con el texto viejo.

Hasta ahora eso se resolvía **acordándose**, y está escrito en CLAUDE.md con
esas palabras: «hay que acordarse». Acordarse no es una comprobación. Y como
salía más barato registrar los nueve de golpe que averiguar cuáles eran, se
registraban los nueve de golpe.

Este fichero guarda la huella de cada valor que se manda a la tienda y dice
exactamente cuáles han cambiado. No necesita credenciales ni hablar con
Shopify: compara el repositorio consigo mismo.

Por qué la huella es un SHA-256
-------------------------------
Porque **es el mismo número que devuelve la tienda**. El `digest` de
`translatableContent` es el SHA-256 del valor, tal cual — está comprobado con
el cuerpo de la FAQ—. Así que esta huella no solo sirve para comparar dos
estados del repositorio: sirve para cotejar contra la tienda sin descargar
nada. `cotejar.py` pide el digest; aquí se calcula.

Dos maneras de preguntarlo
--------------------------
Contra el **sello** —lo que consta subido— o contra un **commit**. La segunda
no necesita que nadie haya sellado nada y contesta la pregunta que se hace de
verdad al acabar de escribir: «de lo que acabo de tocar, ¿qué hay que volver a
registrar?». `--desde HEAD~1` lo dice, y ve las cadenas: al aparecer un
artículo nuevo salen también los cuerpos de los que lo citaban.

Lo que no hace
--------------
No registra nada ni lee la tienda. `--sellar` solo dice «esto ya está
subido», y hay que ejecutarlo **después** de que `traducir.py`,
`traducir_blog.py` o `blog.py` hayan terminado bien. Sellar antes de subir es
mentirle al fichero.
"""

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

SELLO = RAIZ / "huellas.json"


def _huella(valor: str) -> str:
    """El SHA-256 del valor, que es lo que la tienda llama digest."""
    return hashlib.sha256((valor or "").encode("utf-8")).hexdigest()


def valores() -> dict:
    """Todo lo que se manda a la tienda, por clave.

    La clave es `superficie|handle|lengua|clave-de-shopify`, con la clave tal
    y como la nombra la API (`title`, `body_html`, `meta_title`,
    `meta_description`, `summary_html`), para que el que lea esto y el que
    lea una mutación estén hablando de lo mismo.
    """
    v = {}

    def poner(superficie, handle, lengua, clave, valor):
        if valor:
            v[f"{superficie}|{handle}|{lengua}|{clave}"] = valor

    # --- los 29 de proveedor -------------------------------------------
    import catalogo
    for handle, (titulo, descripcion, _alt, _fam, _etq) in catalogo.FICHAS.items():
        poner("producto", handle, "es", "meta_title", titulo)
        poner("producto", handle, "es", "meta_description", descripcion)
    for handle, cuerpo in catalogo.CUERPOS.items():
        poner("producto", handle, "es", "body_html", cuerpo)
    for handle, lenguas in getattr(catalogo, "METAS", {}).items():
        for lengua, (titulo, descripcion) in lenguas.items():
            poner("producto", handle, lengua, "meta_title", titulo)
            poner("producto", handle, lengua, "meta_description", descripcion)

    import cuerpos_en_fr
    for lengua, mapa in (("en", cuerpos_en_fr.CUERPOS_EN),
                         ("fr", cuerpos_en_fr.CUERPOS_FR)):
        for handle, cuerpo in mapa.items():
            poner("producto", handle, lengua, "body_html", cuerpo)

    # --- los 11 propios -------------------------------------------------
    import seo
    for handle, lenguas in seo.META.items():
        for lengua, (titulo, descripcion) in lenguas.items():
            poner("producto propio", handle, lengua, "meta_title", titulo)
            poner("producto propio", handle, lengua, "meta_description",
                  descripcion)

    import descripciones
    import fichas_libros
    for f in list(descripciones.FICHAS) + list(fichas_libros.NUEVOS):
        for lengua in ("es", "en", "fr"):
            poner("producto propio", f["handle"], lengua, "body_html",
                  f.get(lengua))

    # --- el Diario ------------------------------------------------------
    import articulos
    for a in articulos.ARTICULOS:
        titulo, descripcion = a["meta"]
        poner("artículo", a["handle"], "es", "title", a["titulo"])
        poner("artículo", a["handle"], "es", "body_html", a["cuerpo"])
        poner("artículo", a["handle"], "es", "summary_html", a["resumen"])
        poner("artículo", a["handle"], "es", "meta_title", titulo)
        poner("artículo", a["handle"], "es", "meta_description", descripcion)

    import articulos_en_fr
    for handle, lenguas in articulos_en_fr.CUERPOS.items():
        for lengua, a in lenguas.items():
            titulo, descripcion = a["meta"]
            poner("artículo", handle, lengua, "title", a["titulo"])
            poner("artículo", handle, lengua, "body_html",
                  articulos_en_fr.cuerpo(handle, lengua))
            poner("artículo", handle, lengua, "summary_html", a["resumen"])
            poner("artículo", handle, lengua, "meta_title", titulo)
            poner("artículo", handle, lengua, "meta_description", descripcion)

    # --- la FAQ ---------------------------------------------------------
    import faq
    for lengua in faq.LENGUAS:
        titulo, descripcion = faq.META[lengua]
        poner("página", faq.MANGO, lengua, "title", faq.TITULO[lengua])
        poner("página", faq.MANGO, lengua, "body_html", faq.cuerpo(lengua))
        poner("página", faq.MANGO, lengua, "meta_title", titulo)
        poner("página", faq.MANGO, lengua, "meta_description", descripcion)

    return v


def huellas() -> dict:
    return {k: _huella(v) for k, v in valores().items()}


def sellado() -> dict:
    if not SELLO.exists():
        return {}
    return json.loads(SELLO.read_text(encoding="utf-8")).get("huellas", {})


def comparar() -> dict:
    """Qué hay que volver a registrar, y por qué.

    `cambiados` son los que existían y ya no dicen lo mismo: en la tienda hay
    texto viejo. `nuevos` no se han registrado nunca. `desaparecidos` están en
    la tienda y ya no en el repositorio — que no es lo mismo que sobrar: puede
    ser texto que solo vive en la tienda, y de eso hay.
    """
    return _diferencia(huellas(), sellado())


def sellar() -> int:
    h = huellas()
    SELLO.write_text(json.dumps(
        {
            "que_es": ("SHA-256 de cada valor que se manda a Shopify. Es el "
                       "mismo número que la tienda llama digest."),
            "cuando": ("se sella DESPUÉS de que traducir.py, traducir_blog.py "
                       "o blog.py hayan terminado bien, nunca antes."),
            "huellas": dict(sorted(h.items())),
        },
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\n  Sellados {len(h)} valores en {SELLO.name}.\n")
    return 0


def desde_commit(ref: str) -> dict:
    """Las huellas tal y como eran en ese commit.

    Se saca el repositorio entero a un directorio aparte y se ejecuta allí
    este mismo fichero, porque los módulos se importan unos a otros y leer
    solo los que cambiaron daría un estado que nunca existió. Si el commit es
    anterior a este fichero, se copia dentro: lo que se mide es el texto de
    entonces, no la herramienta.
    """
    with tempfile.TemporaryDirectory() as tmp:
        arbol = Path(tmp) / "arbol"
        arbol.mkdir()
        raiz = RAIZ.parent
        tar = subprocess.run(["git", "-C", str(raiz), "archive", ref],
                             capture_output=True)
        if tar.returncode:
            raise SystemExit(f"\n  No existe el commit «{ref}».\n")
        subprocess.run(["tar", "-x", "-C", str(arbol)], input=tar.stdout,
                       check=True)
        destino = arbol / "tienda" / "huellas.py"
        destino.write_bytes(Path(__file__).read_bytes())
        salida = subprocess.run(
            [sys.executable, str(destino), "--json"],
            capture_output=True, text=True, cwd=str(arbol))
        if salida.returncode:
            raise SystemExit(f"\n  No se pudo leer «{ref}»:\n{salida.stderr}\n")
        return json.loads(salida.stdout)


def _diferencia(ahora: dict, antes: dict) -> dict:
    return {
        "cambiados": sorted(k for k in ahora
                            if k in antes and antes[k] != ahora[k]),
        "nuevos": sorted(k for k in ahora if k not in antes),
        "desaparecidos": sorted(k for k in antes if k not in ahora),
        "iguales": sum(1 for k in ahora if antes.get(k) == ahora[k]),
        "total": len(ahora),
    }


def _por_superficie(claves) -> dict:
    salida = {}
    for k in claves:
        superficie, handle, lengua, clave = k.split("|")
        salida.setdefault((superficie, handle), []).append(f"{lengua}·{clave}")
    return salida


def _informe(d: dict, contra: str) -> int:
    print(f"\n  {d['iguales']} de {d['total']} valores siguen igual "
          f"que {contra}\n")

    for titulo, claves in (("HAY QUE VOLVER A REGISTRAR", d["cambiados"]),
                           ("NUNCA SE HAN REGISTRADO", d["nuevos"])):
        if not claves:
            continue
        print(f"  {titulo}  ({len(claves)})\n")
        for (superficie, handle), partes in sorted(
                _por_superficie(claves).items()):
            print(f"    {superficie:16} {handle}")
            print(f"        {', '.join(sorted(partes))}")
        print()

    if d["desaparecidos"]:
        print(f"  YA NO ESTÁN EN EL REPOSITORIO  ({len(d['desaparecidos'])})")
        print(f"    No quiere decir que sobren en la tienda: hay texto que "
              f"solo vive allí.\n")
        for (superficie, handle), partes in sorted(
                _por_superficie(d["desaparecidos"]).items()):
            print(f"    {superficie:16} {handle}  ({', '.join(sorted(partes))})")
        print()

    if not (d["cambiados"] or d["nuevos"]):
        print(f"  Nada que registrar de nuevo respecto de {contra}.\n")
    return 0


def main() -> int:
    if "--json" in sys.argv:
        json.dump(huellas(), sys.stdout)
        return 0

    if "--sellar" in sys.argv:
        return sellar()

    if "--desde" in sys.argv:
        i = sys.argv.index("--desde")
        if i + 1 >= len(sys.argv):
            raise SystemExit("\n  --desde necesita un commit: --desde HEAD~1\n")
        ref = sys.argv[i + 1]
        return _informe(_diferencia(huellas(), desde_commit(ref)), ref)

    if not SELLO.exists():
        print(f"\n  No hay sello todavía: {len(huellas())} valores sin que "
              f"conste que están subidos.")
        print(f"  Sella con --sellar cuando la tienda esté al día; mientras "
              f"tanto,")
        print(f"  --desde HEAD~1 dice qué cambió en el último commit.\n")
        return 0

    return _informe(comparar(), "el último sello")


if __name__ == "__main__":
    raise SystemExit(main())
