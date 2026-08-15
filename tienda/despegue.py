#!/usr/bin/env python3
"""
VILLUMINATIONS — Comprobación previa al despegue
-------------------------------------------------
Antes de gastar un dólar en anuncios conviene saber si la tienda puede cobrar,
entregar y enviar. Esto lo pregunta a la API en lugar de buscarlo a mano por el
panel.

    export SHOPIFY_TIENDA=villuminations.myshopify.com
    export SHOPIFY_TOKEN=shpat_...
    python3 tienda/despegue.py

**Solo lee.** No hay una sola mutación en este fichero: se puede lanzar en
cualquier momento sin miedo a cambiar nada.

Cada comprobación va por su cuenta. Si una falla —porque el token no tiene ese
permiso o porque el campo cambió de nombre— las demás siguen y el informe dice
cuál no se pudo hacer. Un comprobador que se cae entero al primer tropiezo no
sirve para lo que sirve este.

Lo que mira, y por qué cada cosa importa antes de anunciar:

· **Cobro.** Sin pasarela activa el botón de comprar no cobra. Es el único
  fallo que convierte cada clic pagado en pérdida limpia.
· **Envío.** Sin zonas de envío, el pago de un producto físico se cae o sale
  a cero. Los 29 de proveedor pesan y viajan.
· **Precio cero.** Un producto a 0,00 se vende gratis. Pasa más de lo que
  parece cuando se crean variantes por API.
· **Sin publicar.** Un producto que no está en el canal de la tienda no se ve,
  y un anuncio que apunta a él manda al cliente a una página que no existe.
· **Sin imagen.** En el catálogo y en el feed de compras, la ficha sin foto no
  se muestra.
· **Inventario.** Vender sin existencias es prometer lo que no se tiene.
"""

import json
import os
import sys
import urllib.error
import urllib.request

API = "2025-01"
TIENDA = os.environ.get("SHOPIFY_TIENDA", "")
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")


def pedir(consulta: str, variables: dict | None = None) -> dict:
    cuerpo = json.dumps({"query": consulta,
                         "variables": variables or {}}).encode()
    peticion = urllib.request.Request(
        f"https://{TIENDA}/admin/api/{API}/graphql.json",
        data=cuerpo,
        headers={"Content-Type": "application/json",
                 "X-Shopify-Access-Token": TOKEN},
    )
    with urllib.request.urlopen(peticion) as r:
        datos = json.loads(r.read())
    if "errors" in datos:
        raise RuntimeError("; ".join(e.get("message", "?")
                                     for e in datos["errors"]))
    return datos["data"]


# ---------------------------------------------------------------------------
# Cada comprobación devuelve (estado, frase). Estado: ok · aviso · alto · «?»
# ---------------------------------------------------------------------------
def cobro() -> tuple:
    d = pedir("{ shop { name currencyCode "
              "paymentSettings { supportedDigitalWallets } } }")["shop"]
    carteras = d["paymentSettings"]["supportedDigitalWallets"]
    if not carteras:
        return ("aviso", "No hay carteras digitales declaradas. Eso no prueba "
                         "que falte pasarela, pero sí que conviene abrir "
                         "Ajustes → Pagos y confirmarlo a ojo.")
    return ("ok", f"Pagos configurados · {d['currencyCode']} · "
                  f"{len(carteras)} carteras digitales")


def nombre_tienda() -> tuple:
    d = pedir("{ shop { name } }")["shop"]
    if d["name"] != "VILLUMINATIONS":
        return ("alto", f"La cuenta se llama «{d['name']}». Es el nombre que "
                        f"ve el cliente al pagar y en cada correo. "
                        f"Ajustes → Detalles de la tienda.")
    return ("ok", "El nombre de la cuenta es VILLUMINATIONS")


def envio() -> tuple:
    d = pedir("""{
      deliveryProfiles(first: 10) {
        nodes {
          name
          profileLocationGroups {
            locationGroupZones(first: 20) { nodes { zone { name } } }
          }
        }
      }
    }""")["deliveryProfiles"]["nodes"]
    zonas = sum(len(g["locationGroupZones"]["nodes"])
                for p in d for g in p["profileLocationGroups"])
    if zonas == 0:
        return ("alto", "No hay ni una zona de envío. El pago de cualquier "
                        "producto físico se cae aquí.")
    return ("ok", f"{zonas} zonas de envío en {len(d)} perfiles")


def impuestos() -> tuple:
    d = pedir("{ shop { taxesIncluded taxShipping } }")["shop"]
    return ("ok", f"Impuestos incluidos en el precio: "
                  f"{'sí' if d['taxesIncluded'] else 'no'} · "
                  f"al envío: {'sí' if d['taxShipping'] else 'no'}")


def catalogo() -> tuple:
    d = pedir("""{
      products(first: 250) {
        nodes {
          handle status totalInventory tracksInventory
          featuredMedia { id }
          publishedOnCurrentPublication
          variants(first: 50) { nodes { price } }
        }
      }
    }""")["products"]["nodes"]

    gratis, sin_foto, borradores, sin_publicar, sin_stock = [], [], [], [], []
    for p in d:
        if any(float(v["price"]) == 0 for v in p["variants"]["nodes"]):
            gratis.append(p["handle"])
        if not p["featuredMedia"]:
            sin_foto.append(p["handle"])
        if p["status"] != "ACTIVE":
            borradores.append(f"{p['handle']} ({p['status'].lower()})")
        elif not p["publishedOnCurrentPublication"]:
            sin_publicar.append(p["handle"])
        if p["tracksInventory"] and (p["totalInventory"] or 0) <= 0:
            sin_stock.append(p["handle"])

    lineas = [f"{len(d)} productos"]
    for etiqueta, lista in (("a precio cero", gratis),
                            ("sin imagen", sin_foto),
                            ("sin activar", borradores),
                            ("activos pero sin publicar", sin_publicar),
                            ("con inventario a cero", sin_stock)):
        if lista:
            muestra = ", ".join(x[:34] for x in lista[:4])
            resto = f" y {len(lista) - 4} más" if len(lista) > 4 else ""
            lineas.append(f"{len(lista)} {etiqueta}: {muestra}{resto}")

    estado = "alto" if (gratis or sin_publicar) else (
        "aviso" if (sin_foto or borradores or sin_stock) else "ok")
    return (estado, " · ".join(lineas))


def descargas() -> tuple:
    """Los once documentos no pueden pedir envío: no se envía un PDF."""
    d = pedir("""{
      products(first: 250, query: "product_type:Libro OR product_type:Plan") {
        nodes { handle variants(first: 5) { nodes { requiresShipping } } }
      }
    }""")["products"]["nodes"]
    if not d:
        return ("?", "No encuentro productos de tipo Libro ni Plan. "
                     "Comprueba el nombre del tipo en el panel.")
    malos = [p["handle"] for p in d
             if any(v["requiresShipping"] for v in p["variants"]["nodes"])]
    if malos:
        return ("alto", f"{len(malos)} documentos digitales piden envío: "
                        f"{', '.join(malos[:4])}")
    return ("ok", f"Los {len(d)} documentos digitales no piden envío")


COMPROBACIONES = (
    ("Cobro", cobro),
    ("Nombre de la cuenta", nombre_tienda),
    ("Envío", envio),
    ("Impuestos", impuestos),
    ("Catálogo", catalogo),
    ("Productos digitales", descargas),
)

SIMBOLO = {"ok": "ok  ", "aviso": "~~  ", "alto": "ALTO", "?": "??  "}


def main() -> int:
    if not (TIENDA and TOKEN):
        raise SystemExit("  Faltan SHOPIFY_TIENDA y SHOPIFY_TOKEN.")

    print(f"\n  Comprobación previa · {TIENDA}\n")
    altos = 0
    for nombre, funcion in COMPROBACIONES:
        try:
            estado, frase = funcion()
        except (urllib.error.URLError, RuntimeError, KeyError, TypeError) as e:
            estado, frase = "?", f"no se pudo comprobar: {e}"
        altos += estado == "alto"
        print(f"  {SIMBOLO[estado]} {nombre:22} {frase}")

    print("\n  Lo que esto NO puede ver, y hay que mirar en el panel:")
    for linea in (
        "la app de descargas digitales, que es lo que entrega los once "
        "documentos",
        "el píxel de Meta y la etiqueta de Google, sin los cuales un anuncio "
        "no sabe qué funcionó",
        "quién envía de verdad los 29 productos de proveedor",
        "las políticas de la tienda, que piden un permiso que esta app no "
        "tiene",
    ):
        print(f"       · {linea}")

    print(f"\n  {altos} paradas\n" if altos else
          "\n  Ninguna parada en lo que se puede comprobar por API.\n")
    return 1 if altos else 0


if __name__ == "__main__":
    raise SystemExit(main())
