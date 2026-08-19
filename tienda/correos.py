#!/usr/bin/env python3
"""
VILLUMINATIONS — Correos automáticos
-------------------------------------
Las cinco secuencias que deciden si el dinero de un anuncio termina en venta.
Sin esto, una campaña paga por una visita, la visita no compra —el 97 % no
compra la primera vez— y no queda forma de volver a hablar con ella.

    python3 tienda/correos.py           # comprueba medidas y prohibiciones
    python3 tienda/correos.py --texto   # los saca en claro para pegarlos

**Esto no se publica por API.** Las automatizaciones de Shopify se montan en
Marketing → Automatizaciones, y el texto se pega a mano ahí (o en Klaviyo, o en
el proveedor que uses). Lo que aporta este fichero es el texto en tres lenguas,
medido y con las mismas prohibiciones que el resto de la tienda.

Reglas que se comprueban abajo, no se confían:

· **Ninguna promesa de salud.** Un correo es publicidad y está sujeto a lo
  mismo que la ficha. «Recupérate mejor» es una promesa; «la creatina es el
  suplemento más estudiado» es una afirmación sobre la evidencia pública.

· **La marca se escribe VILLUMINATIONS.** En un correo se ve más que en
  ninguna otra parte, porque va en la firma de cada envío.

· **Asunto de 50 caracteres y preencabezado de 90.** Es lo que cabe en la
  bandeja de un móvil. Más largo no es más: es texto que nadie lee.

El correo de entrega (`entrega`) da por hecho que la app de descargas está
instalada y manda el enlace. Mientras no lo esté, ese correo no se puede
activar: prometería un archivo que no llega.
"""

TOPE_ASUNTO = 50
TOPE_PREENCABEZADO = 90

# La firma va al pie de los cinco, en la lengua que toque.
FIRMA = {
    "es": ("VILLUMINATIONS · villuminations.com<br>"
           "Escríbenos respondiendo a este correo: lo lee una persona."),
    "en": ("VILLUMINATIONS · villuminations.com<br>"
           "Reply to this email and a person will read it."),
    "fr": ("VILLUMINATIONS · villuminations.com<br>"
           "Répondez à ce courriel : une personne le lira."),
}

# (secuencia, cuándo se envía)
CUANDO = {
    "bienvenida": "al suscribirse al boletín",
    "carrito-1h": "1 hora después de abandonar el carrito",
    "carrito-24h": "24 horas después, si sigue sin comprar",
    "entrega": "inmediatamente después de la compra de un documento",
    "resena": "14 días después de la compra",
}

# Cómo se monta cada una en Marketing → Automatizaciones. Sin esto había que
# adivinar qué plantilla usar y con qué espera, y adivinar es como se acaba con
# dos correos de carrito que salen a la vez.
#
# secuencia -> (plantilla de Shopify, disparador, espera, se puede activar hoy)
AUTOMATIZACION = {
    "bienvenida": (
        "Suscriptor de correo electrónico",
        "el cliente se suscribe desde el formulario de captura.py",
        "inmediato",
        True),
    "carrito-1h": (
        "Carrito abandonado",
        "añade al carrito y no compra",
        "1 hora",
        True),
    "carrito-24h": (
        "Carrito abandonado",
        "el mismo, con una segunda espera y condición «sigue sin comprar»",
        "24 horas",
        True),
    "entrega": (
        "Pedido pagado",
        "compra de un documento",
        "inmediato",
        False),          # ← promete un archivo que hoy no llega
    "resena": (
        "Pedido cumplimentado",
        "14 días después de entregar",
        "14 días",
        True),
}

# Por qué `entrega` no se puede activar todavía: manda el enlace de descarga y
# no hay app de descargas instalada. Activarlo sería prometer por correo un
# archivo que no existe, que es peor que no escribir.
SIN_ACTIVAR = {
    "entrega": "no hay app de descargas: el enlace que manda no lleva a nada",
}

CORREOS = {

# ---------------------------------------------------------------------------
"bienvenida": {
 "es": {
  "asunto": "Lo que no vas a encontrar aquí",
  "preencabezado": "Ni promesas de salud ni cifras sin fuente. Empezamos por ahí.",
  "cuerpo": """
<p>Gracias por dejarnos tu correo.</p>

<p>Antes de enseñarte nada, lo que <em>no</em> hacemos, que es lo que nos
distingue: aquí no hay promesas de salud ni cifras sin fuente. Las tablas de
nutrición y entrenamiento salen de organismos públicos y se pueden comprobar una
por una. Si la documentación de un proveedor se contradice, el dato no se
publica.</p>

<p>Para que lo veas antes de comprar nada, el <a href="{diario}">Diario</a> está
abierto: cuánta proteína hace falta al día, cuántas horas hay que dormir, qué
suplementos tienen evidencia y cuáles no. Mismo criterio que los libros.</p>

<p>Si algo te cuadra, ahí estaremos.</p>
""",
  "llamada": ("Leer el Diario", "{diario}"),
 },
 "en": {
  "asunto": "What you will not find here",
  "preencabezado": "No health promises, no figures without a source. Start there.",
  "cuerpo": """
<p>Thanks for leaving us your email.</p>

<p>Before we show you anything, here is what we <em>don't</em> do, which is what
sets us apart: no health promises and no figures without a source. The nutrition
and training tables come from public bodies and can be checked one by one. If a
supplier's documentation contradicts itself, the figure is not published.</p>

<p>So you can see it before buying anything, the <a href="{diario}">Journal</a>
is open: how much protein a day, how many hours of sleep, which supplements have
evidence behind them and which do not. Same standard as the books.</p>

<p>If any of it rings true, we will be here.</p>
""",
  "llamada": ("Read the Journal", "{diario}"),
 },
 "fr": {
  "asunto": "Ce que vous ne trouverez pas ici",
  "preencabezado": "Ni promesses de santé ni chiffres sans source. On commence par là.",
  "cuerpo": """
<p>Merci de nous avoir laissé votre adresse.</p>

<p>Avant de vous montrer quoi que ce soit, voici ce que nous ne faisons
<em>pas</em>, et c'est ce qui nous distingue : aucune promesse de santé et aucun
chiffre sans source. Les tables de nutrition et d'entraînement viennent
d'organismes publics et se vérifient une par une. Si la documentation d'un
fournisseur se contredit, la donnée n'est pas publiée.</p>

<p>Pour que vous puissiez le constater avant d'acheter, le
<a href="{diario}">Journal</a> est ouvert : combien de protéines par jour,
combien d'heures de sommeil, quels compléments ont des preuves et lesquels n'en
ont pas. Le même critère que les livres.</p>

<p>Si cela vous parle, nous serons là.</p>
""",
  "llamada": ("Lire le Journal", "{diario}"),
 },
},

# ---------------------------------------------------------------------------
"carrito-1h": {
 "es": {
  "asunto": "Se te quedó algo en el carrito",
  "preencabezado": "Lo guardamos. Si tienes una duda, respóndenos y te contestamos.",
  "cuerpo": """
<p>Dejaste algo a medias. Lo hemos guardado, no hay prisa.</p>

<p>Si lo que te frenó fue una duda concreta —una medida que no encaja, si un
libro cubre lo que buscas, cuánto tarda un envío— responde a este correo y te
contestamos. No es un buzón automático.</p>

<p>Y si simplemente cambiaste de idea, también está bien. No te vamos a escribir
cinco veces por esto.</p>
""",
  "llamada": ("Volver al carrito", "{carrito}"),
 },
 "en": {
  "asunto": "You left something in your cart",
  "preencabezado": "We saved it. If something is unclear, reply and we will answer.",
  "cuerpo": """
<p>You left something halfway. We have saved it; there is no rush.</p>

<p>If what stopped you was a specific question — a measurement that does not add
up, whether a book covers what you are after, how long shipping takes — reply to
this email and we will answer. It is not an automated inbox.</p>

<p>And if you simply changed your mind, that is fine too. We are not going to
write to you five times about this.</p>
""",
  "llamada": ("Back to your cart", "{carrito}"),
 },
 "fr": {
  "asunto": "Vous avez laissé quelque chose",
  "preencabezado": "Nous l'avons gardé. Une question ? Répondez, nous vous répondrons.",
  "cuerpo": """
<p>Vous avez laissé quelque chose en chemin. Nous l'avons gardé, rien ne
presse.</p>

<p>Si c'est une question précise qui vous a arrêté — une dimension qui ne colle
pas, si un livre couvre ce que vous cherchez, le délai de livraison — répondez à
ce courriel et nous vous répondrons. Ce n'est pas une boîte automatique.</p>

<p>Et si vous avez simplement changé d'avis, c'est très bien aussi. Nous ne vous
écrirons pas cinq fois pour cela.</p>
""",
  "llamada": ("Revenir au panier", "{carrito}"),
 },
},

# ---------------------------------------------------------------------------
"carrito-24h": {
 "es": {
  "asunto": "Última vez que te escribimos por esto",
  "preencabezado": "Tu carrito sigue guardado. Después de este correo, lo dejamos.",
  "cuerpo": """
<p>Tu carrito sigue ahí. Este es el segundo y último correo que te mandamos por
él: si no lo quieres, no hace falta que hagas nada.</p>

<p>Por si ayuda a decidir, dos cosas que conviene saber antes de comprar:</p>

<ul>
  <li>Los documentos vienen con las <strong>tres ediciones en un solo
  archivo</strong> —español, inglés y francés—, no hay que elegir lengua.</li>
  <li>En las fichas de equipo publicamos solo las medidas y cargas que declara
  el fabricante. Cuando su documentación se contradice, omitimos el dato y lo
  decimos. Si necesitas una cifra concreta, pregúntanos y la confirmamos con el
  proveedor <em>antes</em> de que compres.</li>
</ul>
""",
  "llamada": ("Terminar la compra", "{carrito}"),
 },
 "en": {
  "asunto": "Last time we write about this",
  "preencabezado": "Your cart is still saved. After this email, we will leave it.",
  "cuerpo": """
<p>Your cart is still there. This is the second and last email we will send
about it: if you do not want it, you need do nothing.</p>

<p>In case it helps you decide, two things worth knowing before buying:</p>

<ul>
  <li>The documents come with <strong>all three editions in a single
  file</strong> — Spanish, English and French — so there is no language to
  choose.</li>
  <li>On the equipment listings we publish only the measurements and load
  ratings the manufacturer states. When their documentation contradicts itself
  we leave the figure out and say so. If you need a specific number, ask and we
  will confirm it with the supplier <em>before</em> you buy.</li>
</ul>
""",
  "llamada": ("Complete your order", "{carrito}"),
 },
 "fr": {
  "asunto": "Dernier courriel à ce sujet",
  "preencabezado": "Votre panier est toujours gardé. Après ce courriel, nous en restons là.",
  "cuerpo": """
<p>Votre panier est toujours là. C'est le deuxième et dernier courriel que nous
enverrons à ce sujet : si vous n'en voulez pas, vous n'avez rien à faire.</p>

<p>Au cas où cela aiderait à décider, deux choses à savoir avant d'acheter :</p>

<ul>
  <li>Les documents contiennent les <strong>trois éditions dans un seul
  fichier</strong> — espagnol, anglais et français — : aucune langue à
  choisir.</li>
  <li>Sur les fiches d'équipement, nous publions uniquement les dimensions et
  les charges déclarées par le fabricant. Quand sa documentation se contredit,
  nous omettons la donnée et nous le disons. S'il vous faut un chiffre précis,
  demandez-le et nous le confirmerons auprès du fournisseur <em>avant</em> votre
  achat.</li>
</ul>
""",
  "llamada": ("Finaliser la commande", "{carrito}"),
 },
},

# ---------------------------------------------------------------------------
"entrega": {
 "es": {
  "asunto": "Tu documento, listo para descargar",
  "preencabezado": "El enlace no caduca. Guárdalo o descárgalo ahora, como prefieras.",
  "cuerpo": """
<p>Ya está. Tu documento se descarga desde el enlace de abajo.</p>

<p>Tres cosas prácticas:</p>

<ul>
  <li>El archivo lleva las <strong>tres ediciones</strong> —español, inglés y
  francés— con marcadores de navegación. Ábrelo por el índice.</li>
  <li>Los planes traen versión de pantalla y versión preparada para imprimir.</li>
  <li>Si una página no abre o una cifra no cuadra con su fuente, responde a este
  correo. Se corrige en el original y se vuelve a componer, que es como se
  arreglan las cosas aquí.</li>
</ul>

<p>Gracias por comprarlo.</p>
""",
  "llamada": ("Descargar", "{descarga}"),
 },
 "en": {
  "asunto": "Your document is ready to download",
  "preencabezado": "The link does not expire. Save it or download now, as you prefer.",
  "cuerpo": """
<p>Done. Your document downloads from the link below.</p>

<p>Three practical things:</p>

<ul>
  <li>The file carries <strong>all three editions</strong> — Spanish, English
  and French — with navigation bookmarks. Open it from the table of
  contents.</li>
  <li>The plans come with a screen version and a version prepared for
  printing.</li>
  <li>If a page will not open or a figure does not match its source, reply to
  this email. It gets corrected at the original and typeset again, which is how
  things are fixed here.</li>
</ul>

<p>Thank you for buying it.</p>
""",
  "llamada": ("Download", "{descarga}"),
 },
 "fr": {
  "asunto": "Votre document est prêt",
  "preencabezado": "Le lien n'expire pas. Enregistrez-le ou téléchargez maintenant.",
  "cuerpo": """
<p>Voilà. Votre document se télécharge depuis le lien ci-dessous.</p>

<p>Trois choses pratiques :</p>

<ul>
  <li>Le fichier contient les <strong>trois éditions</strong> — espagnol,
  anglais et français — avec des signets de navigation. Ouvrez-le par la table
  des matières.</li>
  <li>Les programmes comportent une version écran et une version prête à
  imprimer.</li>
  <li>Si une page ne s'ouvre pas ou qu'un chiffre ne correspond pas à sa source,
  répondez à ce courriel. La correction se fait à l'original et l'on recompose,
  c'est ainsi que les choses se réparent ici.</li>
</ul>

<p>Merci de votre achat.</p>
""",
  "llamada": ("Télécharger", "{descarga}"),
 },
},

# ---------------------------------------------------------------------------
"resena": {
 "es": {
  "asunto": "¿Te ha servido?",
  "preencabezado": "Dos minutos de tu tiempo, y también valen las críticas.",
  "cuerpo": """
<p>Hace dos semanas compraste en VILLUMINATIONS. Si has tenido tiempo de usarlo,
nos interesa saber qué tal.</p>

<p>Y va en serio lo de que valen las críticas: si una tabla no se entiende, si
una lámina no se lee bien impresa, si esperabas otra cosa. Eso se corrige en la
fuente y se vuelve a componer para todo el mundo. Un elogio no cambia nada; un
fallo señalado, sí.</p>

<p>Responde a este correo o deja tu reseña en la ficha del producto.</p>
""",
  "llamada": ("Dejar una reseña", "{producto}"),
 },
 "en": {
  "asunto": "Has it been useful?",
  "preencabezado": "Two minutes of your time — and criticism counts just as much.",
  "cuerpo": """
<p>Two weeks ago you bought from VILLUMINATIONS. If you have had time to use it,
we would like to know how it went.</p>

<p>And we mean it about criticism: if a table does not read clearly, if a plate
does not print well, if you expected something else. That gets corrected at the
source and typeset again for everyone. Praise changes nothing; a fault pointed
out does.</p>

<p>Reply to this email or leave your review on the product page.</p>
""",
  "llamada": ("Leave a review", "{producto}"),
 },
 "fr": {
  "asunto": "Cela vous a-t-il servi ?",
  "preencabezado": "Deux minutes de votre temps — et les critiques comptent autant.",
  "cuerpo": """
<p>Il y a deux semaines, vous avez acheté chez VILLUMINATIONS. Si vous avez eu
le temps de vous en servir, nous aimerions savoir ce que cela a donné.</p>

<p>Et nous le pensons vraiment pour les critiques : si un tableau ne se comprend
pas, si une planche s'imprime mal, si vous attendiez autre chose. Cela se
corrige à la source et se recompose pour tout le monde. Un éloge ne change
rien ; un défaut signalé, si.</p>

<p>Répondez à ce courriel ou laissez votre avis sur la fiche du produit.</p>
""",
  "llamada": ("Laisser un avis", "{producto}"),
 },
},
}


# ---------------------------------------------------------------------------
# Lo que un correo de esta tienda no puede decir
# ---------------------------------------------------------------------------
# Un correo es publicidad y está sujeto a lo mismo que la ficha. Estas son las
# fórmulas que un redactor de correos escribe sin pensar y que aquí no valen.
PROHIBIDAS = {
    "es": ("mejora tu salud", "quema grasa", "aumenta tu energía", "refuerza",
           "desintoxica", "cura", "adelgaza", "rejuvenece", "milagro",
           "resultados garantizados", "clínicamente probado"),
    "en": ("boost", "burns fat", "burn fat", "detox", "improves your health",
           "anti-aging", "miracle", "guaranteed results", "clinically proven",
           "supports immunity"),
    "fr": ("stimule", "brûle les graisses", "détox", "améliore votre santé",
           "anti-âge", "miracle", "résultats garantis", "cliniquement prouvé",
           "renforce l'immunité"),
}

LENGUAS = ("es", "en", "fr")


def comprobar_montaje() -> list:
    """Que cada secuencia sepa cómo se monta, y que lo que no se puede activar
    lo diga en vez de quedarse a medias."""
    malos = []
    for nombre in CORREOS:
        if nombre not in AUTOMATIZACION:
            malos.append(f"{nombre} · no dice con qué plantilla se monta")
            continue
        _plantilla, _disparo, _espera, activable = AUTOMATIZACION[nombre]
        if not activable and nombre not in SIN_ACTIVAR:
            malos.append(f"{nombre} · no se puede activar y no dice por qué")
        if activable and nombre in SIN_ACTIVAR:
            malos.append(f"{nombre} · dice que no se activa y está marcado "
                         f"como activable")
    for nombre in AUTOMATIZACION:
        if nombre not in CORREOS:
            malos.append(f"AUTOMATIZACION · secuencia que no existe: {nombre}")
    return malos


def comprobar() -> list:
    """Medidas, lenguas que faltan, marca mal escrita y promesas de salud."""
    malos = []
    for nombre, versiones in CORREOS.items():
        if nombre not in CUANDO:
            malos.append(f"{nombre} · no dice cuándo se envía")
        for lengua in LENGUAS:
            if lengua not in versiones:
                malos.append(f"{nombre} · falta la versión en {lengua}")
                continue
            c = versiones[lengua]
            if len(c["asunto"]) > TOPE_ASUNTO:
                malos.append(f"{nombre}/{lengua} · asunto "
                             f"{len(c['asunto'])}/{TOPE_ASUNTO}")
            if len(c["preencabezado"]) > TOPE_PREENCABEZADO:
                malos.append(f"{nombre}/{lengua} · preencabezado "
                             f"{len(c['preencabezado'])}/{TOPE_PREENCABEZADO}")
            texto = (c["asunto"] + " " + c["preencabezado"] + " "
                     + c["cuerpo"]).lower()
            for frase in PROHIBIDAS[lengua]:
                if frase in texto:
                    malos.append(f"{nombre}/{lengua} · promesa de salud: "
                                 f"«{frase}»")
            entero = c["asunto"] + c["preencabezado"] + c["cuerpo"]
            for mal in ("VIllumination", "Villuminations", "VILLUMINATIONS 99"):
                if mal in entero:
                    malos.append(f"{nombre}/{lengua} · marca mal escrita: "
                                 f"«{mal}»")
    return malos


def en_claro() -> str:
    """Los correos listos para pegar en el panel."""
    trozos = []
    for nombre, versiones in CORREOS.items():
        trozos.append(f"\n{'=' * 72}\n{nombre.upper()} — {CUANDO[nombre]}\n"
                      f"{'=' * 72}")
        for lengua in LENGUAS:
            c = versiones[lengua]
            texto, enlace = c["llamada"]
            trozos.append(
                f"\n--- {lengua} ---\n"
                f"Asunto        : {c['asunto']}\n"
                f"Preencabezado : {c['preencabezado']}\n"
                f"{c['cuerpo'].strip()}\n"
                f"[Botón] {texto} → {enlace}\n"
                f"{FIRMA[lengua]}")
    return "\n".join(trozos)


if __name__ == "__main__":
    import sys
    malos = comprobar() + comprobar_montaje()
    print(f"\n  {len(CORREOS)} secuencias × {len(LENGUAS)} lenguas · "
          f"{len(malos)} problemas\n")
    for m in malos:
        print(f"    {m}")
    if "--texto" in sys.argv:
        print(en_claro())
    else:
        for nombre in CORREOS:
            print(f"    {nombre:14} {CUANDO[nombre]}")
        print("\n  --texto los saca en claro para pegarlos en el panel.\n")
