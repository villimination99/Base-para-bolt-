#!/usr/bin/env python3
"""
Extrae y limpia el texto de los PDF originales, y lo deja estructurado en JSON.

Los PDF de origen son digitalizaciones antiguas y traen tres problemas:

1. Encabezado y pie repetidos en cada página, mezclados con el texto.
2. Texto en negrita dibujado dos veces, que al extraerlo sale duplicado
   («LAS CONJURACIONES LAS CONJURACIONES»).
3. Saltos de línea a mitad de frase, porque se guardó la maquetación y no
   los párrafos.

Se extrae con PDFium (mucho más fiel que pypdf: no parte las palabras),
se limpia y se reconstruyen los párrafos.

Uso:  python3 tools/extraer.py
"""

import json
import re
import statistics
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGINALES = Path("/root/.claude/uploads/124bf538-a5ca-5693-8309-e256bae586e1")
SRC = ROOT / "src"

# --------------------------------------------------------------------------
# Correcciones de texto. Solo casos inequívocos: acentos que la digitalización
# perdió y erratas repetidas. Nada que pueda cambiar el sentido.
# --------------------------------------------------------------------------
CORRECCIONES = [
    (r"\bIntimo\b", "Íntimo"),
    (r"\bintimo\b", "íntimo"),
    (r"\bIntima\b", "Íntima"),
    (r"\bintima\b", "íntima"),
    (r"\bSi Mismo\b", "Sí Mismo"),
    (r"\bMistica\b", "Mística"),
    (r"\bmistico\b", "místico"),
    (r"\bPractica\b", "Práctica"),
    (r"\bPRACTICA\b", "PRÁCTICA"),
    (r"\bCONJURACION\b", "CONJURACIÓN"),
    (r"\bMAGIA PRACTICA\b", "MAGIA PRÁCTICA"),
    (r"\bTeurgia\b", "Teúrgia") if False else (r"\bxxxx\b", "xxxx"),
    (r"\bespiritu\b", "espíritu"),
    (r"\bEspiritu\b", "Espíritu"),
    (r"\bmagico\b", "mágico"),
    (r"\bMagico\b", "Mágico"),
    (r"\bmagica\b", "mágica"),
    (r"\bMagica\b", "Mágica"),
    (r"\bAstrologia\b", "Astrología"),
    (r"\bAlquimia\b", "Alquimia"),
    (r"\bCabala\b", "Cábala"),
    (r"\besoterico\b", "esotérico"),
    (r"\bEsoterico\b", "Esotérico"),
    (r"\besoterica\b", "esotérica"),
    (r"\bEsoterica\b", "Esotérica"),
    # Comillas y guiones tipográficos
    (r'"([^"]{2,80})"', r"«\1»"),
    (r"(?<=\w)--(?=\w)", "—"),
]

# --------------------------------------------------------------------------
LIBROS = [
    {
        "id": "curso-zodiacal",
        "pdf": "d354625a-curso_zodiacal.pdf",
        "titulo": "Curso Zodiacal",
        "subtitulo": "El hombre se halla crucificado en el sexo",
        "autor": "Samael Aun Weor",
        "fuente": "Instituto Cultural Quetzalcóatl · Segunda edición, Colombia 1952",
        "mascota": "r-zodiaco",
        "acento": "cyan",
        "saltar": [0, 1],  # portada e índice originales: los rehacemos
        "encabezados": [
            r"^Curso Zodiacal\s+Samael Aun Weor$",
            r"^Instituto Cultural Quetzalcoatl\s+Página No\.\s*\d+$",
        ],
        "capitulos": [
            "DEDICATORIA", "OBJETO DEL CURSO ZODIACAL", "ARIES", "TAURUS",
            "GÉMINIS", "CÁNCER", "LEO", "VIRGO", "LIBRA", "ESCORPIO",
            "SAGITARIO", "CAPRICORNIO", "ACUARIO", "PISCIS",
            "RESUMEN ANALÍTICO DEL PRESENTE CURSO",
            "PARA GRANDES COSAS, GRANDES HOMBRES",
        ],
    },
    {
        "id": "conjuraciones",
        "pdf": "d0e0ef58-conjuracion_de_los_4.pdf",
        "titulo": "Las Conjuraciones y la Invocación del Sabio Salomón",
        "subtitulo": "Junto a otras fórmulas de defensa ante los tenebrosos",
        "autor": "Recopilación gnóstica",
        "fuente": "Segunda versión · 4 de febrero de 2004",
        "mascota": "r-pentagrama",
        "acento": "magenta",
        "saltar": [0, 1],
        "encabezados": [r"^-\s*\d+\s*-$"],
        "capitulos": [
            "Conceptos previos. Teurgia y Goecia",
            "LAS CONJURACIONES Y LA INVOCACIÓN DEL SABIO SALOMÓN",
            "LA CONJURACIÓN DE LOS CUATRO",
            "LA CONJURACIÓN DE LOS SIETE",
            "LA INVOCACIÓN DEL SABIO SALOMÓN",
            "EL ÁRBOL DE LA VIDA",
        ],
    },
    {
        "id": "conocimiento-de-si-mismo",
        "pdf": "347fdcad-Face_B.pdf",
        "titulo": "Conocimiento de Sí Mismo",
        "subtitulo": "Veinticinco lecciones prácticas · Fase B",
        "autor": "Libro de conferencias gnósticas",
        "fuente": "Ciclo de conferencias continuas, gratuitas y de entrada libre",
        "mascota": "r-ojo",
        "acento": "verde",
        "saltar": [0, 1, 2],
        "encabezados": [
            r"^Conocimiento de S[ií] Mismo$",
            r"^-\s*\d+\s*-$",
        ],
        "capitulos": "conferencias",  # se detectan por patrón
    },
]

CONFERENCIA = re.compile(r'^Conferencia\s+Nro\.\s*(\d+)\s*[-–]\s*Fase\s*[“"]?B[”"]?', re.I)

# Rango de fechas al empezar cada signo del zodiaco: «21 de Marzo a 20 de Abril»
FECHAS = re.compile(r'^\d{1,2}\s+de\s+\w+\s+a\s+\d{1,2}\s+de\s+\w+\.?$', re.I)

# En español solo va en mayúscula la primera palabra y los nombres propios.
MINUSCULAS = {
    "de", "del", "la", "las", "el", "los", "y", "e", "o", "u", "en", "a",
    "ante", "con", "por", "para", "sin", "sobre", "tras", "un", "una",
    "al", "que", "se", "su", "sus", "lo", "es", "como",
}


def titulo_es(texto: str) -> str:
    """Capitaliza como se hace en español, no como en inglés."""
    palabras = texto.strip().lower().split()
    salida = []
    for i, w in enumerate(palabras):
        if i > 0 and w in MINUSCULAS:
            salida.append(w)
        elif "-" in w:
            salida.append("-".join(p.capitalize() for p in w.split("-")))
        else:
            salida.append(w[:1].upper() + w[1:])
    return " ".join(salida)


# --------------------------------------------------------------------------
def desdoblar(linea: str) -> str:
    """Deshace el texto en negrita que el PDF dibuja dos veces."""
    s = linea.strip()
    if len(s) < 6:
        return s
    # «X X» con las dos mitades idénticas
    mitad = len(s) // 2
    for corte in (mitad, mitad + 1):
        a, b = s[:corte].strip(), s[corte:].strip()
        if a and a == b:
            return a
    # palabras repetidas de forma consecutiva a lo largo de toda la línea
    tk = s.split()
    if len(tk) >= 4 and len(tk) % 2 == 0:
        if all(tk[i] == tk[i + 1] for i in range(0, len(tk), 2)):
            return " ".join(tk[::2])
    # Titular dibujado tres veces, con la última copia recortada:
    # «LA CONJURACION DE LOS SIETE LA CONJURACION DE LOS SIETE URACION DE...»
    # Buscamos el bloque más corto que se repita al menos dos veces seguidas.
    # El mínimo de 14 caracteres evita destrozar letanías legítimas como
    # «¡ALELUYAH, ALELUYAH, ALELUYAH!».
    for k in range(14, len(s) // 2 + 1):
        if s[:k] == s[k:2 * k] and " " in s[:k]:
            return s[:k].strip()
    return s


def corregir(texto: str) -> str:
    for patron, reemplazo in CORRECCIONES:
        texto = re.sub(patron, reemplazo, texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    texto = texto.replace(" ,", ",").replace(" .", ".").replace(" ;", ";")
    return texto


def normaliza(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^A-Za-z0-9 ]", "", s).upper().strip()


def es_mayusculas(s: str) -> bool:
    letras = [c for c in s if c.isalpha()]
    return bool(letras) and sum(c.isupper() for c in letras) / len(letras) > 0.85


def extraer_lineas(pdf: Path, cfg: dict) -> list[str]:
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    patrones = [re.compile(p) for p in cfg["encabezados"]]
    lineas: list[str] = []
    for i in range(len(doc)):
        if i in cfg["saltar"]:
            continue
        texto = doc[i].get_textpage().get_text_range()
        for bruta in texto.splitlines():
            s = desdoblar(bruta)
            if not s:
                lineas.append("")
                continue
            if any(p.match(s) for p in patrones):
                continue
            if re.fullmatch(r"[-–—\s\d]+", s):        # folios sueltos
                continue
            lineas.append(s)
    return lineas


def agrupar(lineas: list[str], cfg: dict) -> list[dict]:
    """Convierte las líneas sueltas en bloques con tipo."""
    largos = [len(x) for x in lineas if len(x) > 20]
    ancho = statistics.median(largos) if largos else 80

    titulos = {} if cfg["capitulos"] == "conferencias" else {
        normaliza(t): t for t in cfg["capitulos"]
    }

    bloques: list[dict] = []
    buffer: list[str] = []
    caps_buffer: list[str] = []

    def cerrar_parrafo():
        nonlocal buffer
        if buffer:
            bloques.append({"t": "p", "x": corregir(" ".join(buffer))})
            buffer = []

    def cerrar_ritual():
        nonlocal caps_buffer
        if caps_buffer:
            bloques.append({"t": "ritual", "x": [corregir(l) for l in caps_buffer]})
            caps_buffer = []

    i = 0
    while i < len(lineas):
        s = lineas[i]
        i += 1
        if not s:
            cerrar_parrafo()
            cerrar_ritual()
            continue

        # ¿título de capítulo declarado? Puede venir partido en dos líneas.
        clave = normaliza(s)
        if clave not in titulos and i < len(lineas) and lineas[i]:
            unido = normaliza(s + " " + lineas[i])
            if unido in titulos:
                clave, _ = unido, i
                i += 1
        if clave in titulos:
            cerrar_parrafo(); cerrar_ritual()
            bloques.append({"t": "cap", "x": corregir(titulos.pop(clave))})
            # rango de fechas del signo, si lo hay
            if i < len(lineas) and FECHAS.match(lineas[i]):
                bloques.append({"t": "fechas", "x": lineas[i].rstrip(".")})
                i += 1
            continue

        # ¿conferencia numerada?
        m = CONFERENCIA.match(s)
        if m:
            cerrar_parrafo(); cerrar_ritual()
            # el título va en la línea siguiente, en mayúsculas
            titulo = ""
            if i < len(lineas) and es_mayusculas(lineas[i]):
                titulo = titulo_es(lineas[i])
                i += 1
            bloques.append({"t": "cap", "x": corregir(titulo) or f"Conferencia {m.group(1)}",
                            "n": int(m.group(1))})
            continue

        # ¿pregunta que hace de subtítulo?  ¿Qué es la Relajación?
        if s.startswith("¿") and s.endswith("?") and len(s) < 70:
            cerrar_parrafo(); cerrar_ritual()
            bloques.append({"t": "h2", "x": corregir(s)})
            continue

        # ¿bloque en mayúsculas? Puede ser subtítulo corto o texto ritual
        if es_mayusculas(s):
            siguiente_caps = i < len(lineas) and es_mayusculas(lineas[i])
            if len(s) < 55 and not siguiente_caps and not caps_buffer:
                cerrar_parrafo()
                bloques.append({"t": "h2", "x": corregir(s)})
            else:
                cerrar_parrafo()
                caps_buffer.append(s)
            continue

        cerrar_ritual()

        # separador decorativo
        if re.fullmatch(r"[*\s]+", s):
            cerrar_parrafo()
            bloques.append({"t": "sep"})
            continue

        buffer.append(s)
        # fin de párrafo: línea claramente más corta que la caja y con
        # puntuación de cierre
        if len(s) < ancho * 0.86 and re.search(r'[.:;!?»"]$', s):
            cerrar_parrafo()

    cerrar_parrafo()
    cerrar_ritual()
    return bloques


def a_capitulos(bloques: list[dict], cfg: dict) -> list[dict]:
    capitulos: list[dict] = []
    actual = {"titulo": "Presentación", "bloques": []}
    for b in bloques:
        if b["t"] == "cap":
            if actual["bloques"]:
                capitulos.append(actual)
            actual = {"titulo": b["x"], "bloques": []}
            if "n" in b:
                actual["numero"] = b["n"]
        else:
            actual["bloques"].append(b)
    if actual["bloques"]:
        capitulos.append(actual)
    return capitulos


def main() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    for cfg in LIBROS:
        pdf = ORIGINALES / cfg["pdf"]
        if not pdf.exists():
            print(f"  falta {pdf.name}, se omite")
            continue
        lineas = extraer_lineas(pdf, cfg)
        bloques = agrupar(lineas, cfg)
        capitulos = a_capitulos(bloques, cfg)

        datos = {k: cfg[k] for k in
                 ("id", "titulo", "subtitulo", "autor", "fuente", "mascota", "acento")}
        datos["capitulos"] = capitulos

        destino = SRC / f"{cfg['id']}.json"
        destino.write_text(json.dumps(datos, ensure_ascii=False, indent=1))

        palabras = sum(len(b.get("x", "")) if isinstance(b.get("x"), str) else 0
                       for c in capitulos for b in c["bloques"])
        print(f"  {cfg['id']:<26} {len(capitulos):>2} capítulos · "
              f"{sum(len(c['bloques']) for c in capitulos):>4} bloques · "
              f"{palabras//5:>6} palabras aprox.")
        for c in capitulos:
            tipos = {}
            for b in c["bloques"]:
                tipos[b["t"]] = tipos.get(b["t"], 0) + 1
            print(f"      · {c['titulo'][:44]:<46} {tipos}")


if __name__ == "__main__":
    sys.exit(main())
