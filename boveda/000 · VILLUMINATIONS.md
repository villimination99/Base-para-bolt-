---
tags:
  - memoria
  - indice
actualizado: 2026-09-19
---

# VILLUMINATIONS — estado del proyecto

Nota escrita a mano, no generada. Las otras 1280 notas de esta bóveda salen del
grafo de `graphify` y se regeneran solas; esta no. Es la memoria: lo que hay que
saber antes de tocar nada, y lo que quedó a medias.

## Qué es esto

Una tienda Shopify —**villuminations.com**, CAD, plan Basic, Canadá— que vende
material propio en PDF y mercancía de proveedor. Cuarenta productos: once
propios y veintinueve de reventa.

Lo propio son **once documentos** que viven en este repositorio y se generan,
no se editan a mano:

- **Ocho libros** (`libros/`): Mesa, Carga, Descanso, Voluntad, Arcanos, Sí
  Mismo, Zodiacal e Invocaciones. Cada uno en español, inglés y francés. 24 PDF.
- **Tres niveles de planes** (`planes/`): Básico (1 documento), Pro (5) y Elite
  (11), también en tres lenguas. 66 PDF.

## Reglas que no se negocian

Están aquí porque se han roto antes y cuesta caro repararlas.

**La marca se escribe `VILLUMINATIONS`.** Ni «VILLUMINATIONS 99», ni
«VIllumination», ni «Ma boutique», que es lo que Shopify pone por defecto en
francés. Los tres aparecieron en la tienda a la vez y un comprador veía tres
vendedores distintos según qué ficha mirase.

**Todo el contenido es obra original y sin dueño ajeno.** Dos bases legales
distintas, y no se pueden mezclar:

- Los datos de nutrición y entrenamiento salen de organismos del Gobierno de
  los Estados Unidos y **no están sujetos a derechos de autor conforme al
  17 U.S.C. § 105**. Eso cubre las cifras, no la redacción.
- Los libros esotéricos se apoyan en la **tradición común y el dominio
  público**: la secuencia de los arcanos, las correspondencias clásicas, los
  ejercicios de examen de conciencia. Esa es otra cosa y hay que decirla como
  tal. Confundir las dos es un error jurídico, no de estilo.

No se le quita la firma a nadie.

**Cada producto se explica solo.** Una ficha no nombra ni describe lo que
contienen las demás: el catálogo se descubre comprando, no leyendo. La única
excepción es que cada nivel enumera sus propios documentos, y Elite dice que es
acumulativo porque lo es por definición.

**Rama de trabajo: `claude/shopify-diet-plans-9k0wti`.** No se empuja a otra sin
permiso. PR abierto: el #2.

## Cómo está montado

La localización tiene una regla que gobierna todo lo demás: **el marcado vive
una vez y las traducciones son datos**. Cada segmento se indexa por el SHA1 de
su original castellano normalizado. Por debajo del 100 % de cobertura el PDF no
se escribe: sale `Incompleto` y no hay libro. Eso es deliberado — es preferible
un libro que no existe a uno que aparece medio traducido.

Hay guardas que abortan la construcción, y conviene no desactivarlas:

- **Ancho de lámina** (`cargar-traducciones.py`): una etiqueta traducida que no
  cabe en su hueco rompe el dibujo, así que se rechaza antes.
- **Cuenta de láminas** (`comprobar_laminas` en `build.py`): si la prosa promete
  «siete láminas» y solo hay seis dibujadas, el libro no se publica. Se añadió
  porque tres libros mentían en tres idiomas a la vez.
- **Etiquetas cortas**: las fases lunares no pasan de 9 caracteres, la
  melotesia de columnas de 124 unidades.

Números duros: **5027 segmentos** traducidos al inglés y al francés, **90 PDF**
en 5 paquetes, 0 problemas de auditoría.

**La ropa se añadió después y sigue la misma regla que los libros: se genera,
no se dibuja a mano.** Hay **119 láminas propias** —vectoriales y de propiedad
entera— y tres generadores: `generar.py` para los doce signos del calendario de
lanzamientos, `dibujar-espinas.py` para la serie de filigrana orgánica y
`dibujar-marca.py` para el monograma. En la serie de espina la **V y la I de
VILLUMINATIONS son el esqueleto de la lámina**, no un sello encima, y lo que la
hace legible a tres metros es el contraste de ritmo: armazón recto y macizo
contra filigrana curva y fina.

`exportar-pod.py` traduce esas láminas a ficheros de impresión y hace cumplir
cinco reglas que son físicas y no de gusto: 300 ppp al tamaño real, fondo
transparente, ninguna opacidad parcial, ningún trazo por debajo de 1 mm impreso
y encaje dentro del área de **su** posición —que no es la misma en la espalda
que en el pecho, la manga o la pernera—. Al exportar la primera lámina saltaron
dos a la vez: el halo iba al 0,92 y las marcas de decanato medían 0,31 mm, o
sea que se habrían caído enteras de la plancha. `verificar()` abre después el
PNG escrito y le decodifica los píxeles, porque un metadato no prueba nada
sobre el alfa.

## Lo que falta

Por orden de urgencia real. **Cuatro cosas de la lista de agosto ya están
hechas** y se dejan dichas para que nadie las vuelva a abrir: el Diario está
entero en tres lenguas —once artículos, veinticuatro versiones—, los 29
productos de proveedor están traducidos, los jabones tienen colección y SEO, y
el blog está publicado.

1. **No hay app de descargas digitales.** Los once productos digitales cobran y
   el comprador no recibe nada. Es lo único que separa esto de una tienda que
   funciona. Se instala desde el panel; no se puede por API.
2. **El nombre de la tienda sigue siendo «VIllumination»**, y sale en la
   pestaña, en el checkout y en cada correo. Ajustes → Detalles de la tienda.
3. **Las políticas están mal**: la marca escrita con otro nombre, redactadas en
   inglés bajo títulos franceses, con literales sin rellenar a la vista
   (`[INSERT TRADING NAME]`), y una política de reembolso que niega remedio
   incluso para producto defectuoso. En Quebec es dudoso que se sostenga.
   `shopPolicyUpdate` pide un permiso que la app no tiene: es de panel.
4. **La ropa espera la hoja del proveedor de estampación.** Los dieciséis
   ficheros de impresión están hechos y verificados; lo que no se puede
   inventar es la composición, el gramaje, las tallas y los colores de la
   prenda blanca. `tienda/ropa.py` aborta sin ellos.
5. **Falta pedir muestra impresa y cotejar el color.** El fichero compensa la
   base blanca de la DTG con un acento más hondo, pero compensar no es
   acertar, y eso solo lo dice una muestra en la mano.
6. **`de` y `ja` publicados sin una sola traducción.** Shopify emite hreflang
   a `/de/…` y `/ja/…` y sirve castellano: para el buscador son copias del
   mismo contenido. O se traducen o se despublican.
7. **El CRM está escrito y sin enchufar.** Las cinco secuencias, el formulario
   de captura con el consentimiento de la CASL y la Ley 25, y con qué
   plantilla se monta cada una. Falta pegarlo en el tema y crear las cuatro
   automatizaciones activables. Sin píxel de Meta ni etiqueta de Google,
   correr anuncios hoy sería pagar sin poder medir.
8. **Precio provisional de 9,99 CAD** en los seis libros nuevos. Los planes sí
   están decididos —9,99 / 19,99 / 34,99 al mes— y así lo dicen las 66
   láminas; falta comprobar que Shopify cobre eso y que haya app de
   suscripciones.

## Fiabilidad de esta bóveda

El grafo tiene ahora **6672 nodos, 8678 aristas y 966 comunidades**, y su
diagnóstico da **cero aristas que apunten a nodos inexistentes**. Las 116 que
avisaba la versión de agosto venían de la extracción semántica, que inventaba
identificadores que no casaban con los del análisis del código; esta
construcción es solo AST y no los produce. A cambio pierde los enlaces
conceptuales que la semántica sí veía: se gana en que ningún enlace miente, se
pierde en alcance.

**`graphify-out/` no viaja en el repositorio** —está en `.gitignore`— así que en
cada máquina nueva hay que rehacerlo, y mientras no se haga las herramientas de
consulta no existen:

```
uv tool install graphifyy && graphify install --platform claude
graphify update .          # reconstruye el grafo, sin coste de LLM
graphify hook install      # post-commit: lo mantiene al día solo
```

El gancho es lo que evita que esto vuelva a quedarse viejo: rehace el grafo en
cada confirmación, sin que nadie tenga que acordarse.
