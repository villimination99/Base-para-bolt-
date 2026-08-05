#!/usr/bin/env python3
"""
VILLUMINATIONS — Generador de libros
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

sys.path.insert(0, str(Path(__file__).resolve().parent / "tools"))
import i18n                                                     # noqa: E402

NODE = "/opt/node22/bin/node"

FOLIO = "#8a93ab"   # folio claro: el interior es oscuro


class Incompleto(Exception):
    """Un libro sin traducir del todo. No es un error del generador: es la
    puerta que impide publicar un producto medio en un idioma y medio en otro."""

    def __init__(self, libro, idioma, hechos, totales):
        self.libro, self.idioma = libro, idioma
        self.hechos, self.totales = hechos, totales
        super().__init__(f"{libro} [{idioma}]: {hechos}/{totales} segmentos")


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


_CARDINALES = {
    "una": 1, "un": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
}
_CUENTA_LAMINAS = re.compile(
    r"\b([a-záéíóúñ]+|\d+)\s+láminas\b", re.IGNORECASE)


def comprobar_laminas(libro: dict) -> None:
    """El texto no puede prometer más láminas de las que hay dibujadas.

    Los libros se refieren a su propio repertorio gráfico por su número —«las
    cinco láminas», «siete láminas dibujadas para este libro»— y ese número se
    escribió a mano cuando el libro tenía otras tantas. Después se añaden
    láminas y la frase se queda atrás, sin que nada chille: es una cifra en
    medio de una frase, no una tabla, y no hay quien la vea al releer.

    Aquí se cuenta lo que de verdad se compone —símbolos distintos, porque una
    misma lámina puede citarse dos veces— y se compara con lo que el texto
    afirma. Si no cuadra, no se compone el libro. Es la misma regla que rige
    las tablas de datos: o se calcula, o se comprueba.
    """
    laminas = {b["x"] for c in libro["capitulos"]
               for b in c["bloques"] if b.get("t") == "figura"}
    fallos = []
    for cap in libro["capitulos"]:
        for bloque in cap["bloques"]:
            for texto in _textos(bloque):
                for m in _CUENTA_LAMINAS.finditer(texto):
                    dicho = m.group(1).lower()
                    n = _CARDINALES.get(dicho)
                    if n is None and dicho.isdigit():
                        n = int(dicho)
                    if n is not None and n != len(laminas):
                        fallos.append((cap["titulo"], m.group(0), n))
    if fallos:
        detalle = "\n".join(
            f'    «{frase}» en «{titulo}» — dice {n}' for titulo, frase, n in fallos)
        raise SystemExit(
            f"\n  {libro['id']}: el libro tiene {len(laminas)} láminas y el "
            f"texto dice otra cosa:\n{detalle}\n"
            "  Corrige la frase o el repertorio; el libro no se compone así.\n")


def _textos(bloque: dict):
    """Todas las cadenas de prosa de un bloque, sea del tipo que sea."""
    for clave_ in ("x", "tit", "pie"):
        v = bloque.get(clave_)
        if isinstance(v, str):
            yield v
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, str):
                    yield i
                elif isinstance(i, (list, tuple)):
                    yield from (c for c in i if isinstance(c, str))


def inicial(s: str) -> str:
    """Primera letra de una entrada de vocabulario, sin tilde y en mayúscula.

    «Élément» va bajo la E y «Ámbar» bajo la A: en las tres lenguas la letra
    de la banda es la de la vocal desnuda, no la de la vocal acentuada.
    """
    for c in unicodedata.normalize("NFD", s):
        if c.isalpha() and unicodedata.category(c) != "Mn":
            return c.upper()
    return ""


def orden_alfabetico(s: str) -> str:
    """Clave de ordenación: sin tildes y en minúsculas, con los espacios.

    Los espacios se conservan —al revés que en clave()— porque aquí sí
    separan palabras: «Signo solar» va después de «Sextil» y antes de
    «Trígono», y quitarle el espacio no cambiaría nada, pero «Caldeo (orden)»
    y «Cardinal» sí dependen de leerse enteros.
    """
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


_BANDA = re.compile(r"^\s*([A-Z])\s*[–—-]\s*([A-Z])\s*$")


def reordenar_vocabulario(libro: dict, idioma: str, cat: dict) -> dict:
    """Devuelve el libro con los vocabularios ordenados en la lengua de salida.

    Los capítulos de vocabulario se reparten en bandas rotuladas «A – D»,
    «E – M», «N – Z», y el rótulo es una promesa: dice qué letras hay dentro.
    En castellano se cumple sola, porque las entradas se escribieron ya
    ordenadas. Al traducir deja de cumplirse —Cuadratura es Square y Eje es
    Axis— y el capítulo pasa a mentir sobre sí mismo en el peor sitio posible,
    que es el único al que el lector vuelve a buscar algo.

    Así que las bandas se rellenan de nuevo con las entradas traducidas: se
    juntan todas las filas del capítulo, se ordenan por el término en su
    lengua y cada una cae en la banda cuyo rango contiene su inicial. Los
    rótulos no se tocan: son rangos fijos del alfabeto y siguen valiendo. Lo
    que cambia es el reparto, y con él el número de filas por banda, que deja
    de estar equilibrado — un vocabulario reparte lo que hay, no lo que
    quedaría bonito.

    En castellano la operación es idéntica al original y no mueve una sola
    fila; eso es exactamente lo que debe pasar, y es la comprobación de que la
    ordenación no se ha inventado un criterio propio.

    Lo que se reordena son las filas EN CASTELLANO, aunque el criterio salga
    de su traducción. El HTML tiene que salir de aquí en el idioma original
    para que i18n.traducir() lo reconozca entero: si se colara ya traducido,
    el catálogo no encontraría las cadenas, las contaría como pendientes y la
    cobertura caería por debajo del 100 % — con lo que el libro no se
    publicaría. Se ordena por la traducción y se escribe el original.
    """
    salida = dict(libro)
    salida["capitulos"] = [dict(c) for c in libro["capitulos"]]

    for cap in salida["capitulos"]:
        bloques = cap["bloques"]
        bandas = [(i, _BANDA.match(b.get("tit") or ""))
                  for i, b in enumerate(bloques) if b.get("t") == "ficha"]
        bandas = [(i, m) for i, m in bandas if m]
        if len(bandas) < 2:
            continue

        # Cada fila viaja emparejada con el término tal como se leerá. Se
        # ordena y se reparte por ese término, y se escribe la fila castellana.
        filas = [(i18n.cadena(fila[0], idioma, cat), fila)
                 for i, _ in bandas for fila in bloques[i]["x"]]
        filas.sort(key=lambda par: orden_alfabetico(par[0]))

        # Cada banda se queda con las entradas cuya inicial cae en su rango.
        # La última recoge lo que sobre por arriba, para que ninguna entrada
        # se pierda si una traducción empieza por un signo inesperado.
        repartidas: list[list] = [[] for _ in bandas]
        for termino, fila in filas:
            letra = inicial(termino)
            destino = len(bandas) - 1
            for n, (_, m) in enumerate(bandas):
                if m.group(1) <= letra <= m.group(2):
                    destino = n
                    break
            repartidas[destino].append(fila)

        nuevos = list(bloques)
        for (i, _), filas_banda in zip(bandas, repartidas):
            nuevos[i] = dict(bloques[i], x=filas_banda)
        cap["bloques"] = nuevos

    return salida


# --------------------------------------------------------------------------
def bloque_html(b: dict) -> str:
    t = b["t"]
    if t == "p":
        texto = esc(b["x"])
        # Cita larga en párrafo aparte, marcada con comillas angulares.
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
    if t == "ficha":
        filas = "".join(
            f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in b["x"]
        )
        titulo = f'<caption>{esc(b["tit"])}</caption>' if b.get("tit") else ""
        return f'<table class="ficha">{titulo}<tbody>{filas}</tbody></table>'
    if t == "lista":
        items = "".join(f"<li>{esc(i)}</li>" for i in b["x"])
        return f'<ul class="puntos">{items}</ul>'
    if t == "pasos":
        items = "".join(f"<li>{esc(i)}</li>" for i in b["x"])
        return f'<ol class="pasos">{items}</ol>'
    if t == "nota":
        tit = f'<div class="nota-t">{esc(b["tit"])}</div>' if b.get("tit") else ""
        return f'<div class="nota">{tit}<p>{esc(b["x"])}</p></div>'
    if t == "figura":
        return figura_html(b)
    return ""


# Las láminas viven en partials/zodiaco.svg como <symbol>. Cada una trae su
# propio viewBox, y hay que repetirlo en el <svg> que la instancia para que
# conserve la proporción: se lee del propio fichero en vez de duplicarlo a
# mano en el texto, que es la clase de dato que siempre acaba desincronizado.
_VIEWBOX: dict[str, str] = {}


def viewbox(simbolo: str) -> str:
    if not _VIEWBOX:
        for svg in PARTIALS.glob("*.svg"):
            _VIEWBOX.update(
                dict(re.findall(r'<symbol id="([^"]+)" viewBox="([^"]+)"',
                                svg.read_text()))
            )
    if simbolo not in _VIEWBOX:
        raise SystemExit(f"Lámina desconocida: {simbolo}")
    return _VIEWBOX[simbolo]


def figura_html(b: dict) -> str:
    simbolo = b["x"]
    clase = " " + b["clase"] if b.get("clase") else ""
    svg = (f'<svg viewBox="{viewbox(simbolo)}" role="img">'
           f'<use href="#{simbolo}"/></svg>')
    if not b.get("tit") and not b.get("pie"):
        return f'<figure class="figura{clase}">{svg}</figure>'
    rot = f'<span class="fig-n">{esc(b["tit"])}</span> ' if b.get("tit") else ""
    pie = esc(b.get("pie", ""))
    return (f'<figure class="figura{clase}">{svg}'
            f"<figcaption>{rot}{pie}</figcaption></figure>")


def capitulo_html(i: int, cap: dict) -> str:
    fechas = next((b["x"] for b in cap["bloques"] if b["t"] == "fechas"), "")
    titulo = cap["titulo"]
    clase = " largo" if len(titulo) > 34 else ""
    cuerpo = "".join(bloque_html(b) for b in cap["bloques"])
    sello = ""
    if cap.get("medallon"):
        s = cap["medallon"]
        sello = (f'<svg class="medallon" viewBox="{viewbox(s)}" role="img">'
                 f'<use href="#{s}"/></svg>')
    return f"""
<section class="capitulo" id="cap-{i}">
  <header>
    <span class="orden">Capítulo {i}</span>
    <h2{f' class="{clase.strip()}"' if clase else ''}>{esc(titulo)}</h2>
    {f'<span class="fechas">{esc(fechas)}</span>' if fechas else ''}
    {sello}
  </header>
  <div class="cuerpo">{cuerpo}</div>
</section>"""


def indice_html(caps: list[dict], paginas: list[int] | None) -> str:
    filas = []
    for i, cap in enumerate(caps, 1):
        pg = f"{paginas[i - 1]}" if paginas else "&nbsp;"
        filas.append(
            # El folio va en un <div> y no en un <span> a propósito. El <li> es
            # flex, así que visualmente no cambia nada; pero para el segmentador
            # un hijo de bloque hace que la FILA deje de ser un segmento y lo sea
            # solo el título. Si no, cada renumeración del índice inventaría
            # dieciséis segmentos nuevos y tiraría abajo su traducción.
            f'<li><span class="n">{i:02d}</span>'
            f'<span class="t">{esc(cap["titulo"])}</span>'
            f'<div class="pg">{pg}</div></li>'
        )
    return f"""
<section class="indice">
  <h2>Índice</h2>
  <svg class="filigrana"><use href="#filigrana"/></svg>
  <ol>{''.join(filas)}</ol>
</section>"""


def cabecera(libro: dict, clase: str) -> str:
    return f"""<!-- VILLUMINATIONS · {libro['titulo']} -->
<meta charset="utf-8">
<title>{esc(libro['titulo'])} | VILLUMINATIONS</title>
<link rel="stylesheet" href="{ASSETS.as_uri()}/fonts.css">
<link rel="stylesheet" href="{ASSETS.as_uri()}/libro.css">
<body class="{clase}">
{PARTIALS.joinpath('simbolos.svg').read_text()}
{laminas_svg(libro)}"""


def laminas_svg(libro: dict) -> str:
    """Inyecta los sprites de láminas que declare el libro.

    Va en línea y no por <link>: los <symbol> de un SVG externo no se pueden
    referenciar con <use href="#id"> desde el documento, y necesitamos los ids
    disponibles en el propio árbol.
    """
    return "\n".join(
        PARTIALS.joinpath(nombre).read_text() for nombre in libro.get("laminas", [])
    )


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
  <div class="sello">Villuminations · Biblioteca</div>
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


CREDITOS_ORIGINAL = """
<section class="creditos">
  <h2>Sobre esta obra</h2>
  <p><strong>{titulo}</strong> es una obra original de {autor},
     escrita y compuesta íntegramente para <strong>villuminations.com</strong>.
     {fuente}.</p>
  <p>{base}</p>
  <p>No se reproduce texto de ningún autor moderno. Donde una idea proviene
     de una fuente concreta se dice en el propio capítulo.</p>
  <p>{lectura}</p>
  <p><strong>Uso permitido.</strong> Tu compra te da una licencia personal e
     intransferible para leer e imprimir este archivo. No se autoriza su
     reventa, redistribución ni publicación total o parcial.</p>
</section>"""

CIERRE_ORIGINAL = """
  <div class="nota">
    <strong>Sobre los derechos.</strong> Obra original.
    © 2026 Villuminations · villuminations.com. Todos los derechos
    reservados. Licencia de lectura personal: no se autoriza la reventa ni la
    redistribución del archivo. Si este libro te ha servido, la mejor forma de
    apoyarlo es recomendarlo por la vía legítima.
  </div>"""


def documento(libro: dict, paginas: list[int] | None) -> str:
    caps = libro["capitulos"]
    capitulos = "".join(capitulo_html(i, c) for i, c in enumerate(caps, 1))
    original = bool(libro.get("original"))

    if not original:
        raise SystemExit(
            f"{libro['id']}: el catálogo es de obra original. Un libro sin "
            '"original": true no tiene plantilla de créditos y no se compone.'
        )
    # La página de créditos es la que dice de qué es esta obra y sobre qué
    # material común se apoya. Si un libro no lo declara, no se compone: un
    # texto de créditos genérico acaba diciendo del libro algo que no es.
    faltan = [c for c in ("base", "lectura") if not libro.get(c)]
    if faltan:
        raise SystemExit(
            f"{libro['id']}: faltan {', '.join(faltan)} en el catálogo. Cada "
            "libro declara su propia base documental y su propia advertencia "
            "de lectura; no hay plantilla común que sirva para todos.")
    creditos = CREDITOS_ORIGINAL.format(
        titulo=esc(libro["titulo"]),
        autor=esc(libro["autor"]),
        fuente=esc(libro["fuente"]),
        base=libro["base"],
        lectura=libro["lectura"],
    )

    return cabecera(libro, f"acento-{libro['acento']}") + f"""
{creditos}

{indice_html(caps, paginas)}
{capitulos}

<section class="cierre">
  <h2>Villuminations</h2>
  <svg class="filigrana"><use href="#filigrana"/></svg>
  <div class="marca"><span class="v">VILLUMINATIONS</span></div>
  <span class="url">villuminations.com</span>
  <div class="redes">YouTube <b>@villuminations</b> &nbsp;·&nbsp; Instagram <b>@villuminations</b></div>
{CIERRE_ORIGINAL}
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


def paginas_de_capitulos(pdf: Path, caps: list[dict], idioma: str = "es",
                         cat: dict | None = None) -> list[int]:
    """Localiza en qué página del PDF empieza cada capítulo.

    Busca el texto TAL Y COMO aparece impreso, así que en la edición inglesa
    hay que buscar «Chapter 3», no «Capítulo 3». Se resuelve contra el mismo
    catálogo que compuso la página: si buscara el español, el índice de las
    ediciones traducidas saldría entero a cero sin avisar.
    """
    import pypdfium2 as pdfium

    cat = cat if cat is not None else {}
    doc = pdfium.PdfDocument(str(pdf))
    textos = [clave(doc[i].get_textpage().get_text_range()) for i in range(len(doc))]

    paginas, desde = [], 0
    for i, cap in enumerate(caps, 1):
        marca = clave(i18n.cadena(f"Capítulo {i}", idioma, cat))
        objetivo = clave(i18n.cadena(cap["titulo"], idioma, cat))[:20]
        encontrada = 0
        for n in range(desde, len(textos)):
            if marca in textos[n] and objetivo[:12] in textos[n]:
                encontrada = n + 1
                desde = n
                break
        paginas.append(encontrada)
    return paginas


def marcadores(pdf: Path, libro: dict, paginas: list[int], idioma: str = "es",
               cat: dict | None = None) -> None:
    from pypdf import PdfWriter

    cat = cat if cat is not None else {}
    caps = libro["capitulos"]
    titulo = i18n.cadena(libro["titulo"], idioma, cat)
    w = PdfWriter(clone_from=str(pdf))
    for page in w.pages:
        page.compress_content_streams(level=9)
    raiz = w.add_outline_item(titulo, 0)
    for cap, pg in zip(caps, paginas):
        if pg:
            w.add_outline_item(i18n.cadena(cap["titulo"], idioma, cat),
                               pg - 1, parent=raiz)
    original = bool(libro.get("original"))
    w.add_metadata({
        "/Title": titulo,
        "/Author": (f"{libro['autor']} — villuminations.com" if original
                    else "VILLUMINATIONS — villuminations.com"),
        "/Subject": i18n.cadena(libro["subtitulo"], idioma, cat),
        "/Creator": "VILLUMINATIONS",
        "/Keywords": ", ".join(libro.get("claves", [])) or "villuminations.com",
    })
    tmp = pdf.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as fh:
        w.write(fh)
    tmp.replace(pdf)


def construir(libro: dict, idioma: str = "es", cat: dict | None = None) -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    cat = cat if cat is not None else i18n.cargar()
    comprobar_laminas(libro)
    libro = reordenar_vocabulario(libro, idioma, cat)
    caps = libro["capitulos"]
    base = libro["id"]
    sufijo = "" if idioma == "es" else f"-{idioma}"
    carpeta_b = BUILD if idioma == "es" else BUILD / idioma
    carpeta_d = DIST if idioma == "es" else DIST / idioma
    carpeta_b.mkdir(parents=True, exist_ok=True)
    carpeta_d.mkdir(parents=True, exist_ok=True)

    html_cub = carpeta_b / f"{base}-cubierta.html"
    html_int = carpeta_b / f"{base}-interior.html"
    pdf_cub = carpeta_b / f"{base}-cubierta.pdf"
    pdf_int = carpeta_b / f"{base}-interior.pdf"
    destino = carpeta_d / f"{base}{sufijo}.pdf"

    def local(html: str) -> str:
        """Traduce, y solo publica con cobertura completa.

        Un libro a medio traducir no es un libro en inglés: es un libro en
        español con frases sueltas en inglés. Por eso, por debajo del 100 %,
        no se escribe nada.
        """
        if idioma == "es":
            return html
        salida, hechos, totales = i18n.traducir(html, idioma, cat)
        if hechos < totales:
            raise Incompleto(base, idioma, hechos, totales)
        return salida

    titulillo = i18n.cadena(libro["titulo"], idioma, cat)

    # 1 · Cubierta a sangre, en documento propio
    html_cub.write_text(local(cubierta(libro)))
    render(html_cub, pdf_cub, "", sangre=True)

    # 2 · Interior. Hacen falta dos pasadas: la primera para saber en qué
    #     página cae cada capítulo, la segunda ya con el índice numerado.
    html_int.write_text(local(documento(libro, None)))
    render(html_int, pdf_int, titulillo)
    folios = paginas_de_capitulos(pdf_int, caps, idioma, cat)

    for _ in range(2):                       # el índice puede desplazar el texto
        html_int.write_text(local(documento(libro, folios)))
        render(html_int, pdf_int, titulillo)
        nuevos = paginas_de_capitulos(pdf_int, caps, idioma, cat)
        if nuevos == folios:
            break
        folios = nuevos

    # 3 · Cubierta + interior en un solo PDF
    unir(pdf_cub, pdf_int, destino, acento=libro["acento"])

    # La cubierta va sin numerar, como en cualquier libro: el folio 1 es la
    # primera página del interior, que en el PDF es la segunda.
    marcadores(destino, libro, [f + 1 for f in folios], idioma, cat)

    from pypdf import PdfReader
    n = len(PdfReader(str(destino)).pages)
    sin_localizar = sum(1 for f in folios if not f)
    aviso = f"  <-- {sin_localizar} capítulos sin localizar" if sin_localizar else ""
    print(f"  {destino.name:<32} {n:>3} pág  "
          f"{destino.stat().st_size/1024:>6.0f} KB  "
          f"{len(caps):>2} capítulos{aviso}")


def fondo(acento: str) -> Path:
    """Genera (y cachea) la capa de fondo negro con textura de marca.

    Chromium no pinta los márgenes de página, así que el negro no puede venir
    del CSS del interior: se renderiza como página independiente a sangre y
    luego se compone DEBAJO de cada página del libro.
    """
    destino = BUILD / f"fondo-{acento}.pdf"
    if destino.exists():
        return destino
    html = (PARTIALS / "fondo.html.tpl").read_text()
    html = html.replace("__ASSETS__", ASSETS.as_uri()).replace("__ACENTO__", acento)
    ruta = BUILD / f"fondo-{acento}.html"
    ruta.write_text(html)
    render(ruta, destino, "", sangre=True)
    return destino


def unir(cubierta_pdf: Path, interior_pdf: Path, destino: Path,
         acento: str | None = None) -> None:
    from pypdf import PdfWriter

    from pypdf import PdfReader

    w = PdfWriter()
    w.append(str(cubierta_pdf))

    capa = PdfReader(str(fondo(acento))).pages[0] if acento else None
    for pagina in PdfReader(str(interior_pdf)).pages:
        if capa is None:
            w.add_page(pagina)
            continue
        # El fondo va primero y el texto encima: la página del interior se
        # renderiza con fondo transparente para que el negro se vea.
        base = w.add_blank_page(width=pagina.mediabox.width,
                                height=pagina.mediabox.height)
        base.merge_page(capa)
        base.merge_page(pagina)

    with open(destino, "wb") as fh:
        w.write(fh)


def main() -> None:
    args = sys.argv[1:]
    flt = next((a for a in args if not a.startswith("--")), "")
    libros = [json.loads(p.read_text()) for p in sorted(SRC.glob("*.json"))
              if flt in p.name]
    if not libros:
        raise SystemExit(f"Sin libros que coincidan con '{flt}'.")

    # --idioma en,fr   ·   --todos-los-idiomas
    idiomas = ["es"]
    for a in args:
        if a.startswith("--idioma="):
            idiomas = [c.strip() for c in a.split("=", 1)[1].split(",")]
    if "--todos-los-idiomas" in args:
        idiomas = list(i18n.IDIOMAS)
    desconocidos = [c for c in idiomas if c not in i18n.IDIOMAS]
    if desconocidos:
        raise SystemExit(f"Idioma no soportado: {', '.join(desconocidos)}. "
                         f"Disponibles: {', '.join(i18n.IDIOMAS)}")

    cat = i18n.cargar()
    pendientes = []
    for idioma in idiomas:
        print(f"\n  {i18n.IDIOMAS[idioma][0]}")
        for libro in libros:
            try:
                construir(libro, idioma, cat)
            except Incompleto as e:
                pendientes.append(e)
                print(f"  {e.libro + ('' if idioma == 'es' else '-' + idioma):<32} "
                      f"SIN TRADUCIR  {e.hechos}/{e.totales} segmentos")

    if pendientes:
        print(f"\n  {len(pendientes)} edición(es) no publicadas por cobertura "
              "incompleta. Se traduce lo que falta y se vuelve a lanzar.")


if __name__ == "__main__":
    main()
