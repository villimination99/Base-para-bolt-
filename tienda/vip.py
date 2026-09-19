#!/usr/bin/env python3
"""
VILLUMINATIONS — La página VI.P
--------------------------------
Mide y limpia el cuerpo de la página VI.P, que es la más pesada de la tienda y
está enlazada en el menú principal: si algún día se paga tráfico, aterriza ahí.

    python3 tienda/vip.py fichero.html          # informe sobre una copia
    python3 tienda/vip.py                       # (con credenciales) la pide
    python3 tienda/vip.py --limpiar             # deja la versión corregida
    python3 tienda/vip.py --limpiar --publicar  # y la escribe en la tienda

**Qué hace y qué no.** La limpieza quita lo que no pinta nada dentro del cuerpo
de una página de Shopify y no toca ni una línea de la aplicación. El Hub lo
escribió el dueño y funciona; aquí no se reescribe, se le quitan de encima
cuatro etiquetas que sobran y una que hace daño.

La que hace daño es esta:

    <meta name="viewport" content="… maximum-scale=1.0">

`maximum-scale=1.0` **impide ampliar con los dedos**. Es un fallo de
accesibilidad —quien no ve bien no puede acercar el texto—, lo penalizan las
auditorías, y encima está duplicando la etiqueta que el tema ya emite. Dentro
del cuerpo de una página, `<body>`, `<title>` y `<meta charset>` tampoco hacen
nada: el documento ya los tiene, y repetirlos es HTML inválido.

Lo que **no** hace este fichero, y conviene decirlo: no aligera los 313 KB de
JavaScript ni evita que Three.js y Chart.js se bajen de un CDN externo. Eso se
arregla moviendo el código a los recursos del tema, donde el navegador puede
guardarlo en caché entre visitas en vez de volver a bajarlo dentro del HTML
cada vez. Es una mudanza, no una limpieza, y pide probarla en la tienda.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")
PAGINA = "gid://shopify/Page/94564122673"          # se corrige abajo si hace falta
PAGINA_VIP = "gid://shopify/Page/94354800689"

# Etiquetas que el documento ya tiene y que dentro del cuerpo son inválidas.
SOBRAN = (
    (r'</?body[^>]*>', "<body>"),
    (r'</?html[^>]*>', "<html>"),
    (r'</?head[^>]*>', "<head>"),
    (r'<title[^>]*>.*?</title>', "<title>"),
    (r'<meta\s+charset[^>]*>', "<meta charset>"),
    (r'<meta\s+name=["\']viewport["\'][^>]*>', "<meta viewport>"),
    (r'<!doctype[^>]*>', "<!doctype>"),
)


def pedir(consulta: str, variables: dict) -> dict:
    cuerpo = json.dumps({"query": consulta, "variables": variables}).encode()
    peticion = urllib.request.Request(
        f"https://{TIENDA}/admin/api/{API}/graphql.json",
        data=cuerpo,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": TOKEN})
    with urllib.request.urlopen(peticion) as r:
        datos = json.loads(r.read())
    if "errors" in datos:
        raise SystemExit(f"  GraphQL: {datos['errors']}")
    return datos["data"]


def informe(html: str) -> list:
    """Lo que pesa y lo que está mal, con cifras."""
    lineas = [f"tamaño del cuerpo: {len(html) / 1024:.0f} KB"]

    est = re.findall(r'<style[^>]*>(.*?)</style>', html, re.S | re.I)
    scr = re.findall(r'<script[^>]*>(.*?)</script>', html, re.S | re.I)
    lineas.append(f"CSS en línea: {sum(map(len, est)) / 1024:.0f} KB "
                  f"en {len(est)} bloques")
    lineas.append(f"JS en línea: {sum(map(len, scr)) / 1024:.0f} KB "
                  f"en {len(scr)} bloques")

    externos = sorted({m for m in re.findall(r'https://[^\s"\')]+', html)
                       if "cdn.shopify.com" not in m})
    if externos:
        lineas.append(f"se baja de fuera: {len(externos)} recursos")
        for u in externos[:6]:
            lineas.append(f"    {u[:96]}")

    for patron, nombre in SOBRAN:
        n = len(re.findall(patron, html, re.S | re.I))
        if n:
            aviso = ""
            if nombre == "<meta viewport>" and "maximum-scale" in html:
                aviso = "  ← impide ampliar con los dedos"
            lineas.append(f"sobra {nombre} × {n}{aviso}")

    gifs = len(re.findall(r'\.gif\?', html))
    if gifs:
        lineas.append(f"{gifs} GIF animados: pesan más que un vídeo corto y "
                      f"no se pueden pausar")
    return lineas


def limpiar(html: str) -> tuple:
    """Quita lo que sobra. Devuelve (html, qué se quitó)."""
    quitado = []
    for patron, nombre in SOBRAN:
        html, n = re.subn(patron, "", html, flags=re.S | re.I)
        if n:
            quitado.append(f"{nombre} × {n}")
    # dos saltos seguidos donde estaban las etiquetas
    html = re.sub(r'\n{3,}', "\n\n", html).strip()
    return html, quitado


ESCRIBIR = """
mutation($id: ID!, $p: PageUpdateInput!) {
  pageUpdate(id: $id, page: $p) { page { handle } userErrors { field message } }
}"""

LEER = """
query($id: ID!) { page(id: $id) { handle title body } }"""


def main() -> int:
    ficheros = [a for a in sys.argv[1:] if not a.startswith("--")]
    if ficheros:
        html = Path(ficheros[0]).read_text(encoding="utf-8")
        origen = ficheros[0]
    elif TIENDA and TOKEN:
        html = pedir(LEER, {"id": PAGINA_VIP})["page"]["body"]
        origen = "la tienda"
    else:
        raise SystemExit("  Dame un fichero, o pon SHOPIFY_TIENDA y "
                         "SHOPIFY_TOKEN para pedirla a la tienda.")

    print(f"\n  VI.P · desde {origen}\n")
    for l in informe(html):
        print(f"    {l}")

    if "--limpiar" not in sys.argv:
        print("\n  --limpiar deja la versión corregida en /tmp.\n")
        return 0

    nuevo, quitado = limpiar(html)
    print(f"\n  quitado: {', '.join(quitado) or 'nada'}")
    print(f"  {len(html) / 1024:.0f} KB → {len(nuevo) / 1024:.0f} KB")

    destino = Path("/tmp/vip-limpia.html")
    destino.write_text(nuevo, encoding="utf-8")
    print(f"  escrito {destino}")

    if "--publicar" in sys.argv:
        if not (TIENDA and TOKEN):
            raise SystemExit("  Para publicar hacen falta las credenciales.")
        pedir(ESCRIBIR, {"id": PAGINA_VIP, "p": {"body": nuevo}})
        print("  publicada")
    else:
        print("  --publicar la escribe en la tienda.")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
