#!/usr/bin/env python3
"""
VILLUMINATIONS — El paquete que se manda a la estampadora
=========================================================

    python3 ropa/tools/paquete-pod.py

Hace tres cosas y ninguna a mano: la hoja de contacto de las láminas, el LEEME
con la tabla de qué se sube dónde, y el ZIP.

Por qué existe este fichero
---------------------------
El paquete anterior se montó a mano, y un paquete montado a mano tiene dos
maneras de mentir y ninguna de avisar:

· **Manda ficheros viejos.** El dibujo cambia, se rehacen los PNG, y el ZIP se
  queda con los de la semana pasada porque nadie se acordó de rehacerlo. El
  destinatario no puede notarlo: un PNG viejo se abre igual de bien.
· **El LEEME dice números que ya no son.** Estaban escritos a mano —«los 16
  ficheros», «1063 × 1119 px»— y no había nada que los atara al código. Es
  exactamente el fallo de la prosa que prometía siete láminas cuando había
  seis, que aquí ya costó tres idiomas.

Así que el LEEME **se genera** de `exportar-pod.py`, y `comprobar()` aborta si
falta una lámina, sobra una, o alguna es más vieja que el dibujo del que
salió. Un ZIP que no se puede montar es mejor que uno que miente.
"""

import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
POD = RAIZ / "pod"
MAQUETAS = RAIZ / "maquetas"
ZIP = RAIZ / "VILLUMINATIONS-print-on-demand.zip"
S = Path("/tmp/claude-0/-home-user-Base-para-bolt-/"
         "124bf538-a5ca-5693-8309-e256bae586e1/scratchpad")
FUENTES = ("dibujar-espinas.py", "exportar-pod.py")


def _pod():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "pod", Path(__file__).resolve().parent / "exportar-pod.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def esperados(m) -> list:
    return [f"villuminations-{sid.replace('es-', '')}-{ac}"
            for sid in m.COLOCACION for ac in m.ACENTOS]


def comprobar(m) -> list:
    malos = []
    quiere = set(esperados(m))
    hay = {p.stem for p in POD.glob("villuminations-*.png")}
    for falta in sorted(quiere - hay):
        malos.append(f"falta la lámina {falta}.png")
    for sobra in sorted(hay - quiere):
        malos.append(f"sobra {sobra}.png: no sale de la serie de ahora, "
                     f"y en el ZIP nadie distinguiría una de otra")
    # Lo que más caro sale: mandar un PNG anterior al dibujo del que dice
    # venir. No se nota abriéndolo, solo comparando fechas.
    tope = max((Path(__file__).parent / f).stat().st_mtime for f in FUENTES)
    for nombre in sorted(quiere & hay):
        if (POD / f"{nombre}.png").stat().st_mtime < tope:
            malos.append(f"{nombre}.png es anterior al generador: hay que "
                         f"volver a pasar exportar-pod.py --todas")
        if not (POD / f"{nombre}.md").exists():
            malos.append(f"{nombre} no tiene ficha .md")
    if not list(MAQUETAS.glob("*.png")):
        malos.append("no hay maquetas: pasa maqueta.py")
    return malos


# ---------------------------------------------------------------------------
# La hoja de contacto
# ---------------------------------------------------------------------------
def catalogo(m) -> int:
    """Las láminas juntas, una columna por pieza y una fila por acento.

    Se dibuja desde los SVG que acompañan a cada PNG, no desde los PNG: a
    tamaño de hoja de contacto un PNG de 3600 píxeles se ve peor reducido por
    el navegador que el vector rasterizado a la medida que hace falta.
    """
    S.mkdir(parents=True, exist_ok=True)
    piezas = list(m.COLOCACION)
    filas = []
    for ac in m.ACENTOS:
        celdas = []
        for sid in piezas:
            base = f"villuminations-{sid.replace('es-', '')}-{ac}"
            area = m.AREAS[m.COLOCACION[sid][0]]
            svg = (POD / f"{base}.svg").read_text(encoding="utf-8")
            # la relación de aspecto del área, para que se vean a escala
            celdas.append(
                f'<figure style="flex:{area[0] / area[1]:.3f}">{svg}'
                f'<figcaption>{sid.replace("es-", "")}<span>'
                f'{area[0]} × {area[1]} cm</span></figcaption></figure>')
        filas.append(f'<section><h2>{ac}<em>'
                     f'{m.ACENTOS_POD[ac]}</em></h2>'
                     f'<div class=fila>{"".join(celdas)}</div></section>')
    html = f"""<!doctype html><meta charset=utf-8><style>
body{{margin:0;background:#0a0a0e;color:#eef2ff;font:13px/1.5 Georgia,serif;
 padding:26px}}
h1{{font-size:15px;letter-spacing:.24em;font-weight:400;margin:0 0 4px}}
h1+p{{margin:0 0 26px;opacity:.45;font-size:12px}}
section{{margin-bottom:26px}}
h2{{font-size:12px;letter-spacing:.2em;font-weight:400;margin:0 0 10px;
 text-transform:uppercase;border-bottom:1px solid #1b1b24;padding-bottom:6px}}
h2 em{{float:right;font-style:normal;opacity:.4;font-family:monospace}}
.fila{{display:flex;gap:16px;align-items:flex-start}}
figure{{margin:0;background:#121218;border:1px solid #1e1e28;padding:12px}}
svg{{width:100%;height:auto;display:block}}
figcaption{{margin-top:8px;font-size:11px;letter-spacing:.12em}}
figcaption span{{display:block;opacity:.38;letter-spacing:.02em}}
</style>
<h1>VILLUMINATIONS · SERIE ESPINA</h1>
<p>{len(piezas)} piezas × {len(m.ACENTOS)} acentos = {len(piezas) * len(m.ACENTOS)} ficheros de impresión.
El lienzo de cada uno es su área de estampación completa a {m.PPP} ppp.</p>
{"".join(filas)}"""
    (S / "cat.html").write_text(html, encoding="utf-8")
    (S / "cat.mjs").write_text(
        "import { chromium } from "
        "'/opt/node22/lib/node_modules/playwright/index.mjs';\n"
        "const b = await chromium.launch("
        "{executablePath:'/opt/pw-browsers/chromium'});\n"
        "const p = await b.newPage({viewport:{width:1500,height:1100},"
        "deviceScaleFactor:1.6});\n"
        f"await p.goto('file://{S}/cat.html');\n"
        f"await p.screenshot({{path:'{POD}/catalogo.png',fullPage:true}});\n"
        "await b.close();\n", encoding="utf-8")
    r = subprocess.run(["node", str(S / "cat.mjs")],
                       capture_output=True, text=True)
    if r.returncode:
        print(f"    no se pudo rasterizar la hoja:\n{r.stderr[:300]}")
        return 1
    return 0


# ---------------------------------------------------------------------------
# El LEEME, generado
# ---------------------------------------------------------------------------
def leeme(m) -> str:
    filas = []
    for sid, (area, ancho, xf, yc, prenda) in m.COLOCACION.items():
        aw, ah, an = m.AREAS[area]
        W, H, _c = m._piezas().PIEZAS[sid][0]()
        alto = ancho * H / W
        filas.append(
            f"| {sid.replace('es-', '')} | {prenda.lower()} · {an.lower()} | "
            f"**{m.px(aw)} × {m.px(ah)} px** | {ancho} × {alto:.1f} cm | "
            f"a {aw * xf - ancho / 2:.1f} / {yc} cm del borde |")
    tintas = "\n".join(
        f"| {ac} | `{m._piezas().ACENTOS[ac]}` | `{m.ACENTOS_POD[ac]}` |"
        for ac in m.ACENTOS)
    n = len(m.COLOCACION) * len(m.ACENTOS)
    return f"""# VILLUMINATIONS · ficheros de impresión bajo demanda

{n} PNG `villuminations-*.png`: {len(m.COLOCACION)} piezas en
{len(m.ACENTOS)} acentos. Cada uno lleva al lado su `.md` con la prenda, el
área, el tamaño del dibujo, la colocación, las dos tintas y lo que mide su
ráster.

## Lo primero, porque es lo que se hace mal

**El lienzo de cada PNG ES el área de estampación completa**, y el dibujo va
dentro con transparencia alrededor. Al subirlo, dile a la aplicación que lo
**encaje al área**. No lo escales, no lo centres a mano, no lo recortes: cae
solo en su tamaño y en su sitio, y queda a {m.PPP} ppp exactos.

Antes no era así —el fichero medía lo que medía el dibujo— y pasaba esto: la
aplicación estiraba una pieza de pecho de 1063 píxeles hasta los 30 cm del área
frontal, salían 88 ppp, avisaba de resolución insuficiente y había que
encogerla a ojo hasta que callara. Eso no es un fichero, es una negociación, y
la segunda tirada sale a otro tamaño que la primera. Ya no pasa.

## Qué se sube

| pieza | prenda y posición | fichero | dibujo dentro | colocado |
|---|---|---|---|---|
{chr(10).join(filas)}

Todos a **{m.PPP} ppp**, PNG con canal alfa, fondo transparente comprobado
píxel a píxel, opacidad plena, ningún rasgo por debajo de {m.MM_MINIMO} mm y
ningún hueco interior que se empaste.

## Los {len(m.ACENTOS)} acentos

| acento | pantalla | impresión |
|---|---|---|
{tintas}

El hueso es `{m.HUESO_POD}` en todos.

**Por qué el fichero no lleva el color de la marca.** La DTG sobre prenda
oscura imprime primero una base blanca y el color encima, y esa base levanta y
desatura. El fichero lleva el acento más hondo para que lo impreso caiga cerca
de lo que la marca es en pantalla. **Compensar no es acertar: pide una muestra
y cotéjala antes de cualquier tirada**, y con el rojo y el oro más que con
ninguno, que son los dos que más se mueven.

## Las fotos

Las de `maquetas/` son **composición de marca**: anuncio, publicación y
cabecera de colección.

Para la **ficha de producto** usa las que genera Printful al subir el fichero:
salen de la prenda real, son fotográficas y son gratis. Estas no las
sustituyen.

## Y antes de la primera tirada

**Coteja el área con el producto concreto.** Las de la tabla son las estándar
del catálogo y varían entre modelos. Si el tuyo admite más, subirlo es cambiar
un número en `ropa/tools/exportar-pod.py`, no rehacer el dibujo.

## Cómo se rehace todo esto

```
python3 ropa/tools/dibujar-espinas.py --hoja   # las láminas y su hoja de contacto
python3 ropa/tools/exportar-pod.py --todas     # los {n} ficheros de impresión
python3 ropa/tools/maqueta.py                  # las maquetas de marca
python3 ropa/tools/paquete-pod.py              # esta hoja, el catálogo y el ZIP
```

Generado por `ropa/tools/paquete-pod.py`. No se edita a mano: la siguiente
pasada lo sobrescribe.
"""


def main() -> int:
    m = _pod()
    malos = comprobar(m)
    print(f"\n  PAQUETE PARA LA ESTAMPADORA · {len(malos)} problemas\n")
    for x in malos:
        print(f"    {x}")
    if malos:
        return 1

    if catalogo(m):
        return 1
    (POD / "LEEME.md").write_text(leeme(m), encoding="utf-8")

    fecha = (2026, 9, 19, 0, 0, 0)          # fija: dos pasadas, un mismo ZIP
    # El SVG va también. Ninguna aplicación de estampación lo acepta —todas
    # piden PNG—, pero es el original del que se vuelve a sacar cualquier
    # tamaño el día que el producto concreto resulte tener otra área.
    dentro = ([(p, f"pod/{p.name}") for p in sorted(POD.iterdir())
               if p.suffix in (".png", ".md", ".svg")]
              + [(p, f"maquetas/{p.name}") for p in sorted(MAQUETAS.glob("*.png"))])
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for ruta, nombre in dentro:
            info = zipfile.ZipInfo(nombre, fecha)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, ruta.read_bytes())

    print(f"    {POD.relative_to(RAIZ.parent)}/catalogo.png")
    print(f"    {POD.relative_to(RAIZ.parent)}/LEEME.md")
    print(f"    {ZIP.relative_to(RAIZ.parent)}  ·  {len(dentro)} ficheros  ·  "
          f"{ZIP.stat().st_size // 1024 // 1024} MB\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
