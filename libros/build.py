#!/usr/bin/env python3
"""
VILLUMINATION 99 — Generador de libros
--------------------------------------
Toma el JSON limpio de src/, monta el HTML del libro y lo renderiza a PDF A5.

A diferencia de los planes, aquí el texto fluye y Chromium decide los saltos
de página. Eso obliga a renderizar dos veces: la primera para averiguar en qué
página cae cada capítulo, y la segunda ya con el índice numerado. Al final se
añaden los marcadores de navegación del PDF.

Uso:  python3 build.py                (edición pantalla)
      python3 build.py --papel        (edición para imprimir)
      python3 build.py --ambas
      python3 build.py --ambas curso  (filtrando por nombre)
"""

import html as _html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
ASSETS = ROOT / "assets"
PARTIALS = ROOT / "partials"

NODE = "/opt/node22/bin/node"

FOLIO = "#7c766c"


def esc(s: str) -> str:
    return _html.escape(s, quote=False)


def clave(s: str) -> str:
    """Normaliza para comparar: sin tildes, sin espacios y en mayúsculas.

    Se quitan los espacios porque los titulares llevan letter-spacing y el
    extractor de texto los devuelve con separaciones postizas
    («C A P Í T U L O   1»).
    """
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", "", s).upper()


# --------------------------------------------------------------------------
def bloque_html(b: dict) -> str:
    t = b["t"]
    if t == "p":
        texto = esc(b["x"])
        # Notas al pie que la digitalización dejó incrustadas en el cuerpo:
        # empiezan por el número de la llamada. Se componen en cuerpo menor.
        if re.match(r"^\d{1,2}\s+[A-ZÁÉÍÓÚÑ]", b["x"]) and len(b["x"]) > 40:
            return f'<p class="nota-pie">{texto}</p>' 
        # Las citas del original vienen entre comillas angulares en párrafo aparte
        if texto.startswith("«") and texto.rstrip().endswith("»") and len(texto) > 120:
            return f"<blockquote>{texto}</blockquote>"
        return f"<p>{texto}</p>"
    if t == "h2":
        return f"<h3>{esc(b['x'])}</h3>"
    if t == "ritual":
        lineas = "".join(f"<span>{esc(l)}</span>" for l in b["x"])
        return f'<div class="ritual">{lineas}</div>'
    if t == "sep":
        return '<svg class="sep"><use href="#filigrana"/></svg>'
    if t == "fechas":
        return ""      # se pinta en la cabecera del capítulo
    return ""


def capitulo_html(i: int, cap: dict) -> str:
    fechas = next((b["x"] for b in cap["bloques"] if b["t"] == "fechas"), "")
    titulo = cap["titulo"]
    clase = " largo" if len(titulo) > 34 else ""
    cuerpo = "".join(bloque_html(b) for b in cap["bloques"])
    return f"""
<section class="capitulo" id="cap-{i}">
  <header>
    <span class="orden">Capítulo {i}</span>
    <h2{f' class="{clase.strip()}"' if clase else ''}>{esc(titulo)}</h2>
    {f'<span class="fechas">{esc(fechas)}</span>' if fechas else ''}
  </header>
  <div class="cuerpo">{cuerpo}</div>
</section>"""


def indice_html(caps: list[dict], paginas: list[int] | None) -> str:
    filas = []
    for i, cap in enumerate(caps, 1):
        pg = f"{paginas[i - 1]}" if paginas else "&nbsp;"
        filas.append(
            f'<li><span class="n">{i:02d}</span>'
            f'<span class="t">{esc(cap["titulo"])}</span>'
            f'<span class="pg">{pg}</span></li>'
        )
    return f"""
<section class="indice">
  <h2>Índice</h2>
  <svg class="filigrana"><use href="#filigrana"/></svg>
  <ol>{''.join(filas)}</ol>
</section>"""


def cabecera(libro: dict, clase: str) -> str:
    return f"""<!-- VILLUMINATION 99 · {libro['titulo']} -->
<meta charset="utf-8">
<title>{esc(libro['titulo'])} | VILLUMINATION 99</title>
<link rel="stylesheet" href="{ASSETS.as_uri()}/fonts.css">
<link rel="stylesheet" href="{ASSETS.as_uri()}/libro.css">
<body class="{clase}">
{PARTIALS.joinpath('simbolos.svg').read_text()}"""


def cubierta(libro: dict) -> str:
    """La cubierta es un documento aparte para poder ir a sangre: Chromium
    no pinta los márgenes de página, así que con márgenes el neón quedaría
    flotando sobre un marco blanco."""
    largo = " largo" if len(libro["titulo"]) > 30 else ""
    # El @page del interior lleva márgenes; aquí hay que anularlos para que
    # el fondo llegue al borde.
    return cabecera(libro, f"cubierta-doc acento-{libro['acento']}") + """
<style>@page{ size:148mm 210mm; margin:0 }</style>""" + f"""
<div class="cubierta">
  <div class="sello">Villumination 99 · Biblioteca</div>
  <div>
    <svg class="simbolo"><use href="#{libro['mascota']}"/></svg>
    <h1 class="{largo.strip()}">{esc(libro['titulo'])}</h1>
    <p class="subtitulo">{esc(libro['subtitulo'])}</p>
    <div class="autor">{esc(libro['autor'])}</div>
  </div>
  <div class="pie">
    <b>Edición cuidada 2026</b><br>
    {esc(libro['fuente'])}<br>
    villuminations.com
  </div>
</div>
</body>"""


def documento(libro: dict, paginas: list[int] | None) -> str:
    caps = libro["capitulos"]
    capitulos = "".join(capitulo_html(i, c) for i, c in enumerate(caps, 1))

    return cabecera(libro, f"acento-{libro['acento']}") + f"""
<section class="creditos">
  <h2>Sobre esta edición</h2>
  <p>Este volumen reproduce el texto de <strong>{esc(libro['titulo'])}</strong>,
     de {esc(libro['autor'])}. La obra procede de {esc(libro['fuente'])}.</p>
  <p>Esta edición no altera el contenido: se ha respetado el texto original.
     El trabajo realizado ha sido de <strong>recuperación tipográfica</strong>
     — reconstruir los párrafos que la digitalización había partido, retirar
     los encabezados repetidos que se mezclaban con el texto, corregir acentos
     perdidos en el escaneo y componer el conjunto en un formato legible, con
     índice navegable y numeración de páginas.</p>
  <p>Los derechos del texto pertenecen a sus autores y a la institución que lo
     difunde. Esta edición se distribuye respetando esa autoría y sin
     atribuirse la obra.</p>
  <p><strong>Nota de lectura.</strong> Se trata de un texto de carácter
     filosófico y espiritual, escrito en su época y contexto. Su contenido no
     constituye consejo médico, psicológico ni sanitario, y no sustituye la
     atención de un profesional cualificado.</p>
</section>

{indice_html(caps, paginas)}
{capitulos}

<section class="cierre">
  <h2>Villumination 99</h2>
  <svg class="filigrana"><use href="#filigrana"/></svg>
  <div class="marca"><span class="v">VILLUMINATION</span><span class="n">99</span></div>
  <span class="url">villuminations.com</span>
  <div class="redes">YouTube <b>@villumination99</b> &nbsp;·&nbsp; Instagram <b>@villumination99</b></div>
  <div class="nota">
    <strong>Sobre los derechos.</strong> El texto de esta obra pertenece a sus
    autores y a la institución que originalmente lo difunde; esta edición se
    limita a su recuperación tipográfica y no reclama ninguna titularidad
    sobre el contenido. Si eres titular de derechos sobre esta obra y deseas
    que se retire o se modifique esta edición, escríbenos y se atenderá de
    inmediato.
  </div>
</section>
</body>"""


# --------------------------------------------------------------------------
def render(html_path: Path, pdf_path: Path, titulillo: str, sangre: bool = False) -> None:
    res = subprocess.run(
        [NODE, str(ROOT / "tools" / "render.mjs"), str(html_path), str(pdf_path),
         FOLIO, titulillo, "sangre" if sangre else ""],
        capture_output=True, text=True, timeout=300,
    )
    if not pdf_path.exists():
        raise SystemExit(f"Fallo al renderizar {html_path.name}:\n{res.stderr[-2000:]}")


def paginas_de_capitulos(pdf: Path, caps: list[dict]) -> list[int]:
    """Localiza en qué página del PDF empieza cada capítulo."""
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    textos = [clave(doc[i].get_textpage().get_text_range()) for i in range(len(doc))]

    paginas, desde = [], 0
    for i, cap in enumerate(caps, 1):
        marca = clave(f"Capítulo {i}")
        objetivo = clave(cap["titulo"])[:20]
        encontrada = 0
        for n in range(desde, len(textos)):
            if marca in textos[n] and objetivo[:12] in textos[n]:
                encontrada = n + 1
                desde = n
                break
        paginas.append(encontrada)
    return paginas


def marcadores(pdf: Path, caps: list[dict], paginas: list[int], titulo: str) -> None:
    from pypdf import PdfWriter

    w = PdfWriter(clone_from=str(pdf))
    for page in w.pages:
        page.compress_content_streams(level=9)
    raiz = w.add_outline_item(titulo, 0)
    for cap, pg in zip(caps, paginas):
        if pg:
            w.add_outline_item(cap["titulo"], pg - 1, parent=raiz)
    w.add_metadata({
        "/Title": titulo,
        "/Author": "VILLUMINATION 99 — villuminations.com",
        "/Subject": "Edición tipográfica cuidada",
        "/Creator": "VILLUMINATION 99",
    })
    tmp = pdf.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as fh:
        w.write(fh)
    tmp.replace(pdf)


def construir(libro: dict) -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    caps = libro["capitulos"]
    base = libro["id"]
    html_cub = BUILD / f"{base}-cubierta.html"
    html_int = BUILD / f"{base}-interior.html"
    pdf_cub = BUILD / f"{base}-cubierta.pdf"
    pdf_int = BUILD / f"{base}-interior.pdf"
    destino = DIST / f"{base}.pdf"

    # 1 · Cubierta a sangre, en documento propio
    html_cub.write_text(cubierta(libro))
    render(html_cub, pdf_cub, "", sangre=True)

    # 2 · Interior. Hacen falta dos pasadas: la primera para saber en qué
    #     página cae cada capítulo, la segunda ya con el índice numerado.
    html_int.write_text(documento(libro, None))
    render(html_int, pdf_int, libro["titulo"])
    folios = paginas_de_capitulos(pdf_int, caps)

    for _ in range(2):                       # el índice puede desplazar el texto
        html_int.write_text(documento(libro, folios))
        render(html_int, pdf_int, libro["titulo"])
        nuevos = paginas_de_capitulos(pdf_int, caps)
        if nuevos == folios:
            break
        folios = nuevos

    # 3 · Cubierta + interior en un solo PDF
    unir(pdf_cub, pdf_int, destino)

    # La cubierta va sin numerar, como en cualquier libro: el folio 1 es la
    # primera página del interior, que en el PDF es la segunda.
    marcadores(destino, caps, [f + 1 for f in folios], libro["titulo"])

    from pypdf import PdfReader
    n = len(PdfReader(str(destino)).pages)
    sin_localizar = sum(1 for f in folios if not f)
    aviso = f"  <-- {sin_localizar} capítulos sin localizar" if sin_localizar else ""
    print(f"  {destino.name:<32} {n:>3} pág  "
          f"{destino.stat().st_size/1024:>6.0f} KB  "
          f"{len(caps):>2} capítulos{aviso}")


def unir(cubierta_pdf: Path, interior_pdf: Path, destino: Path) -> None:
    from pypdf import PdfWriter

    w = PdfWriter()
    for origen in (cubierta_pdf, interior_pdf):
        w.append(str(origen))
    with open(destino, "wb") as fh:
        w.write(fh)


def main() -> None:
    flt = next((a for a in sys.argv[1:] if not a.startswith("--")), "")
    libros = [json.loads(p.read_text()) for p in sorted(SRC.glob("*.json"))
              if flt in p.name]
    if not libros:
        raise SystemExit(f"Sin libros que coincidan con '{flt}'.")
    for libro in libros:
        construir(libro)


if __name__ == "__main__":
    main()
