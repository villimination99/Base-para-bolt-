#!/usr/bin/env python3
"""
VILLUMINATIONS — El punto de captura de correo
===============================================
El eslabón que falta. `correos.py` tiene cinco secuencias escritas en tres
lenguas y **ninguna tiene a quién escribir**: no hay un solo sitio en la tienda
donde alguien deje su correo. Sin esto, la mitad del CRM es un fichero de texto.

    python3 tienda/captura.py           # comprueba medidas y consentimiento
    python3 tienda/captura.py --liquid  # el bloque para pegar en el tema

**Esto no se publica por API.** El formulario es una sección del tema, así que
el `--liquid` sale para pegar. Lo que aporta este fichero es el texto medido,
en tres lenguas, y —sobre todo— que el consentimiento esté bien pedido.

Por qué el consentimiento no es un detalle de diseño
----------------------------------------------------
La tienda vende desde Canadá, así que a los correos comerciales les aplica la
**CASL**, que es de las normas más severas que hay. Lo que exige, en corto:

· **Consentimiento expreso**, y expreso significa que la persona marca una
  casilla que estaba vacía. Una casilla premarcada no es consentimiento, y
  «al suscribirte aceptas» tampoco.
· **Decir quién pide el consentimiento y para qué**, con una dirección de
  contacto. No vale un «suscríbete» a secas.
· **Un mecanismo de baja en cada envío**, que funcione durante al menos
  sesenta días y se atienda en diez días hábiles.

En Quebec se suma la **Ley 25** sobre datos personales, que pide que la
finalidad se diga en términos claros y sencillos en el momento de recoger el
dato. Las dos cosas se resuelven con la misma frase bien escrita, que es la
que está abajo en `CONSENTIMIENTO`.

Esto no es asesoramiento legal y no pretende serlo: es el texto redactado para
cumplir lo que las dos normas piden de forma explícita. Antes de publicarlo
conviene que lo lea alguien que responda de ello.

Lo que aquí NO se hace
----------------------
**No se promete un descuento ni un regalo.** Un imán de captación —un capítulo
suelto, una lámina, un porcentaje— convierte bastante más que «apúntate al
boletín», y probablemente convenga tenerlo. Pero decidir qué se regala es del
dueño, no de este fichero, y anunciar aquí algo que luego no se entrega es
exactamente el fallo que el resto del repositorio evita.

Lo que sí se ofrece es lo que ya existe y se entrega solo: el Diario.
"""

import re
import sys

TOPE_TITULO = 60
TOPE_SUB = 120
TOPE_BOTON = 22

LENGUAS = ("es", "en", "fr")

MARCA = "VILLUMINATIONS"
CORREO = "villumination@outlook.com"

# La casilla. Sale SIN marcar: marcarla de antemano no es consentimiento
# expreso, y con la CASL delante eso no es una sutileza.
CONSENTIMIENTO = {
    "es": ("Quiero recibir de <strong>VILLUMINATIONS</strong> el Diario y el "
           "aviso de cuándo se publica un documento nuevo. Entiendo que puedo "
           "darme de baja en cualquier momento desde el enlace de cada correo "
           "o escribiendo a " + CORREO + "."),
    "en": ("I want to receive the Journal from <strong>VILLUMINATIONS</strong> "
           "and notice of when a new document is published. I understand I can "
           "unsubscribe at any time from the link in every email or by writing "
           "to " + CORREO + "."),
    "fr": ("Je souhaite recevoir de <strong>VILLUMINATIONS</strong> le Journal "
           "et l'avis de publication d'un nouveau document. Je comprends que je "
           "peux me désabonner à tout moment depuis le lien de chaque courriel "
           "ou en écrivant à " + CORREO + "."),
}

# Qué se ofrece. Nada que no se entregue solo.
CAPTURA = {
    "es": {
        "titulo": "El Diario, en tu correo",
        "sub": ("Cada artículo dice de dónde sale cada cifra. Sin promesas de "
                "salud y sin nada que no se pueda comprobar."),
        "marcador": "tu@correo.com",
        "boton": "Suscribirme",
        "exito": ("Hecho. Te llega un correo para confirmar; hasta que lo "
                  "confirmes no te escribimos."),
        "error": "Ese correo no parece válido. Míralo y vuelve a probar.",
    },
    "en": {
        "titulo": "The Journal, in your inbox",
        "sub": ("Every article says where each figure comes from. No health "
                "promises and nothing that cannot be checked."),
        "marcador": "you@email.com",
        "boton": "Subscribe",
        "exito": ("Done. You will get an email to confirm; we write nothing "
                  "until you do."),
        "error": "That email does not look valid. Check it and try again.",
    },
    "fr": {
        "titulo": "Le Journal, dans votre boîte",
        "sub": ("Chaque article dit d'où vient chaque chiffre. Sans promesses "
                "de santé et sans rien qui ne puisse être vérifié."),
        "marcador": "vous@courriel.com",
        "boton": "M'abonner",
        "exito": ("C'est fait. Vous recevrez un courriel de confirmation ; "
                  "nous n'écrivons rien avant."),
        "error": "Ce courriel ne semble pas valide. Vérifiez et réessayez.",
    },
}

# Dónde va. Un solo sitio no basta y cinco cansan.
SITIOS = (
    ("pie de página", "en las tres lenguas, visible en cada página"),
    ("final de cada artículo del Diario",
     "quien ha leído 800 palabras es quien más probable es que se apunte"),
    ("página del Diario", "arriba, antes de la lista de artículos"),
)

# Frases que no pueden aparecer: son las mismas del resto de la tienda.
PROHIBIDAS = ("cura", "mejora tu salud", "quema grasa", "garantizado",
              "milagro", "adelgaza", "burns fat", "guaranteed", "miracle",
              "brûle les graisses", "garanti", "miracle")

LIQUID = """{%- comment -%}
  VILLUMINATIONS · captura de correo
  Pegar como sección o fragmento del tema. Usa el formulario nativo de
  Shopify, así que el contacto entra en Clientes con su consentimiento
  registrado y las automatizaciones de Marketing pueden dispararse solas.

  La casilla NO va marcada de antemano: con la CASL delante, el
  consentimiento tiene que ser un acto de la persona.
{%- endcomment -%}

<div class="vi-captura">
  <h2 class="vi-captura__titulo">{{ 'vi.captura.titulo' | t }}</h2>
  <p class="vi-captura__sub">{{ 'vi.captura.sub' | t }}</p>

  {%- form 'customer', class: 'vi-captura__form' -%}
    <input type="hidden" name="contact[tags]" value="boletin,diario">
    <input type="hidden" name="contact[accepts_marketing]" value="true">

    <label class="visually-hidden" for="vi-correo">
      {{ 'vi.captura.marcador' | t }}
    </label>
    <input id="vi-correo" type="email" name="contact[email]" required
           autocomplete="email"
           placeholder="{{ 'vi.captura.marcador' | t }}">

    <label class="vi-captura__consent">
      <input type="checkbox" name="contact[note][consentimiento]"
             value="expreso" required>
      <span>{{ 'vi.captura.consentimiento' | t }}</span>
    </label>

    <button type="submit">{{ 'vi.captura.boton' | t }}</button>

    {%- if form.posted_successfully? -%}
      <p class="vi-captura__ok" role="status">{{ 'vi.captura.exito' | t }}</p>
    {%- elsif form.errors -%}
      <p class="vi-captura__mal" role="alert">{{ 'vi.captura.error' | t }}</p>
    {%- endif -%}
  {%- endform -%}
</div>
"""


def locales() -> dict:
    """Las cadenas para los ficheros de idioma del tema (locales/*.json).

    El texto va ahí y no incrustado en el Liquid: así el tema lo traduce solo
    según la lengua del visitante, que es justo lo que se quiere en una tienda
    con tres idiomas publicados.
    """
    return {
        lengua: {"vi": {"captura": dict(CAPTURA[lengua],
                                        consentimiento=CONSENTIMIENTO[lengua])}}
        for lengua in LENGUAS
    }


def comprobar() -> list:
    malos = []
    for lengua in LENGUAS:
        c = CAPTURA[lengua]
        for clave, tope in (("titulo", TOPE_TITULO), ("sub", TOPE_SUB),
                            ("boton", TOPE_BOTON)):
            if len(c[clave]) > tope:
                malos.append(f"{lengua} · {clave} {len(c[clave])}/{tope}")

        texto = " ".join(c.values()) + " " + CONSENTIMIENTO[lengua]
        for frase in PROHIBIDAS:
            if re.search(rf"\b{re.escape(frase)}\b", texto, re.I):
                malos.append(f"{lengua} · promesa prohibida: «{frase}»")
        if "VIllumination" in texto or "Villumination " in texto:
            malos.append(f"{lengua} · la marca mal escrita")

        # Lo que la CASL pide que esté a la vista al pedir el consentimiento.
        falta = []
        if MARCA not in CONSENTIMIENTO[lengua]:
            falta.append("quién lo pide")
        if CORREO not in CONSENTIMIENTO[lengua]:
            falta.append("una dirección de contacto")
        bajas = ("baja", "unsubscribe", "désabonner")
        if not any(b in CONSENTIMIENTO[lengua].lower() for b in bajas):
            falta.append("cómo darse de baja")
        if falta:
            malos.append(f"{lengua} · el consentimiento no dice "
                         f"{', ni '.join(falta)}")

    # La casilla no puede salir marcada, y el formulario tiene que exigirla.
    if "checked" in LIQUID:
        malos.append("la casilla sale marcada: eso no es consentimiento "
                     "expreso")
    if 'name="contact[email]"' not in LIQUID or "required" not in LIQUID:
        malos.append("el formulario no exige correo o consentimiento")
    return malos


def main() -> int:
    if "--liquid" in sys.argv:
        print(LIQUID)
        print("\n// locales/*.json\n")
        import json
        for lengua in LENGUAS:
            print(f"--- {lengua}.json ---")
            print(json.dumps(locales()[lengua], ensure_ascii=False, indent=2))
        return 0

    malos = comprobar()
    print(f"\n  Captura de correo · {len(LENGUAS)} lenguas · "
          f"{len(malos)} problemas\n")
    for lengua in LENGUAS:
        c = CAPTURA[lengua]
        print(f"    {lengua}  «{c['titulo']}»  ·  botón «{c['boton']}»")
    for m in malos:
        print(f"    {m}")
    print("\n  Dónde va:")
    for donde, porque in SITIOS:
        print(f"    · {donde}: {porque}")
    print("\n  --liquid saca el bloque y las cadenas para el tema.\n")
    return 1 if malos else 0


if __name__ == "__main__":
    raise SystemExit(main())
