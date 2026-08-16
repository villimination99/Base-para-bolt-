# VILLUMINATIONS

Tienda Shopify (**villuminations.com**, CAD, Canadá) más el generador de todo lo
que vende de cosecha propia. La memoria larga del proyecto está en
[`boveda/000 · VILLUMINATIONS.md`](boveda/000%20·%20VILLUMINATIONS.md); esto es
solo lo que hay que tener delante antes de escribir una línea.

## Reglas que no se negocian

**La marca se escribe `VILLUMINATIONS`.** Nunca «VILLUMINATIONS 99», ni
«VIllumination», ni «Ma boutique». Las tres han estado a la vez en la tienda.

**Dos bases legales distintas, y no se mezclan.** Los datos de nutrición y
entrenamiento vienen de organismos del Gobierno de EE. UU. y **no están sujetos
a derechos de autor conforme al 17 U.S.C. § 105** — eso cubre las cifras, no la
redacción. Los libros esotéricos se apoyan en la **tradición común y el dominio
público**, que es otra cosa y se dice como tal. Y a nadie se le quita la firma.

**Cada producto se explica solo.** Una ficha no nombra ni describe el contenido
de las demás: el catálogo se descubre comprando. Única excepción: cada nivel
enumera sus propios documentos, y Elite dice que es acumulativo porque lo es.

**Nada de promesas de salud** en las fichas de suplementos, y **ninguna cifra
que no esté en la ficha del proveedor** (véase `tienda/catalogo.py`).

**Rama de trabajo: `claude/shopify-diet-plans-9k0wti`.** No se empuja a otra.

## Cómo funciona esto

El texto de los libros y los planes **no se edita a mano**: vive en
`libros/src/*.json` y `planes/src/*.html`, y los `build.py` lo componen. Editar
un PDF o un HTML de `dist/` es trabajo que se pierde en la siguiente pasada.

Las traducciones son **datos, no marcado**: cada segmento se indexa por el SHA1
de su original castellano normalizado, así que la maqueta existe una sola vez.

### Guardas que abortan la construcción a propósito

No se desactivan para «salir del paso» — cada una está por un fallo real:

| Guarda | Qué impide |
|---|---|
| Cobertura < 100 % | Un libro medio traducido. Sale `Incompleto` y no se escribe el PDF. |
| Ancho de lámina (`cargar-traducciones.py`) | Una etiqueta traducida que no cabe y rompe el dibujo. |
| `comprobar_laminas()` (`libros/build.py`) | Que la prosa prometa siete láminas y haya seis. Pasó, en tres idiomas. |
| `datos_oficiales.comprobar()` | Que una tabla no cuadre con su fuente. |

Comprobaciones rápidas antes de dar nada por bueno:

```
python3 tienda/seo.py        # medidas de título y descripción de los 11 propios
python3 tienda/catalogo.py   # ídem de los 29 de proveedor
python3 tienda/articulos.py  # ídem de los artículos del Diario
python3 tienda/cuerpos_en_fr.py   # cuerpos traducidos: medidas y promesas de salud
python3 tienda/articulos_en_fr.py # el Diario en inglés y francés: cobertura y medidas
python3 tienda/lecturas.py   # qué ficha ofrece qué artículo del Diario
python3 tienda/correos.py    # los cinco correos automáticos
python3 tienda/menus.py      # la navegación, con sus traducciones
python3 tienda/ropa.py       # láminas propias disponibles para estampar
python3 tienda/hero.py       # el vídeo de 5 s de la cabecera y su póster
python3 tienda/visibilidad.py # superficie indexable, datos estructurados y CRM
python3 libros/tools/faltan.py
python3 tablero.py           # rehace tablero/index.html con el estado del sistema
python3 auditar.py           # lo que solo se ve mirando todas las superficies juntas
```

`auditar.py` es el único que cruza ficheros. Cada módulo se mide a sí mismo y
ninguno puede ver un título repetido entre dos superficies, una descripción que
desperdicia el fragmento del buscador o un artículo al que no apunta nadie. Las
tres cosas estaban ahí y ninguna comprobación existente las veía.

Para llevarlo a la tienda hacen falta `SHOPIFY_TIENDA` y `SHOPIFY_TOKEN`:

```
python3 tienda/traducir.py --ensayo   # qué traducciones se registrarían
python3 tienda/traducir.py            # las registra
python3 tienda/blog.py --ensayo       # ídem con los artículos
python3 tienda/traducir_blog.py --ensayo   # el Diario en inglés y francés
python3 tienda/despegue.py            # ¿puede cobrar, enviar y entregar?
```

`despegue.py` **solo lee**: no tiene una sola mutación. Contesta de una vez las
preguntas que no se deducen del repositorio —si hay pasarela, si hay zonas de
envío, qué productos están a precio cero o sin publicar— y dice al final lo que
ni siquiera él puede ver.

Los cinco correos automáticos viven en `tienda/correos.py`, en tres lenguas y
con las mismas prohibiciones que las fichas. **No se publican por API**: las
automatizaciones se montan en Marketing → Automatizaciones y el texto se pega
allí. `--texto` los saca en claro.

**Antes de dar de alta ropa estampada**, `tienda/ropa.py`. Un diseño no se
publica si no señala su lámina dentro del repositorio: hay **95 láminas
propias** en `libros/partials/` y `planes/partials/`, vectoriales y de
propiedad entera, y no hace falta buscar dibujos fuera. Faltan por rellenar la
hoja del proveedor de estampación y qué lámina va en qué prenda; ninguna de las
dos se puede inventar.

**Las traducciones no se copian a mano dentro de una mutación.** Se hizo así
una vez y se coló un «veintivún» que no estaba en el original; encontrarlo
costó cotejar ocho artículos carácter a carácter. `traducir.py` pide los
digests y manda el texto sin que pase por ningún teclado.

**El precio vive en dos sitios y uno de ellos no se puede corregir a
posteriori.** Las once láminas de planes llevan impresa la escalera de los tres
niveles: eso son 66 PDF, en tres lenguas y dos ediciones, y los que ya se han
descargado siguen diciendo lo que decían. Si el precio cambia en Shopify, hay
que reconstruirlos. `auditar.py` imprime la tabla de lo que dicen las láminas
para poder cotejarla con la tienda de un vistazo, y aborta si dos láminas no
coinciden. Está decidido y escrito: **suscripción mensual, en dólares
canadienses**, con la moneda en la insignia («9,99 $ CAD/mes»), la
periodicidad en cada escalón y una línea bajo la escalera que lo dice entero.

**Un precio también es un segmento traducible.** `traducible()` de
`planes/tools/i18n.py` exigía dos letras, así que «9,99 $» nunca entró en el
catálogo y salía con coma española dentro de la edición inglesa, tres líneas
por debajo de la insignia que sí estaba traducida. La cobertura al 100 % no lo
veía: no había un hueco, había un segmento que no existía. Ahora un precio
entra aunque no lleve ni una letra.

**El Elite no incluye sesiones de coaching.** La lámina 11 es el cuaderno con
el que se prepara una sesión —cuatro focos, banco de preguntas, plan de
acción—, no la sesión. El título decía «Todo Incluido + Coaching» y la escalera
«+ coaching 1 a 1»: las dos cosas prometían un servicio que no se entrega y las
dos están corregidas. El **handle no se tocó** (`elite-todo-incluido-coaching`)
porque la URL está indexada. Si algún día se dan sesiones de verdad, lo que
hace falta antes es lo operativo: cuántas, de cuánto, por qué canal y cómo se
reservan.

**Las dos bases legales tampoco se mezclan en el blog.** `_fuentes()` de
`tienda/articulos.py` pide `base="federal"` o `base="tradicion"` y no tiene
valor por defecto que sirva para las dos: antes firmaba siempre con el
17 U.S.C. § 105 y el artículo del decanato salió publicado invocando una ley
que no le tocaba. `articulos_en_fr.py` repite la misma exigencia en inglés y en
francés, con las dos entradas y sin valor por defecto.

**El handle de un artículo del Diario no se traduce.** Shopify deja hacerlo y
crea la URL localizada, como en las colecciones; aquí no, porque `lecturas.py`
escribe los enlaces de las cuarenta fichas como
`/en/blogs/diario/<handle-castellano>` y traducirlo los convertiría todos en un
404 de golpe. Está en `PROHIBIDAS` de `traducir_blog.py`. Si algún día se
decide traducirlos, se cambian las dos cosas a la vez.

**No se enlaza a lo que no está traducido.** El Diario está en castellano y se
va traduciendo artículo a artículo. Dos guardas lo sostienen solo:
`lecturas.disponibles()` no ofrece desde una ficha inglesa un artículo que no
existe en inglés, y `_descolgar()` de `articulos_en_fr.py` le quita el ancla a
las citas entre artículos cuyo destino aún no está. Ninguna de las dos hay que
acordarse de mantener: el enlace aparece solo el día que el destino existe.

## La API de Shopify, en corto

Lo que costó descubrir y no está en ningún sitio evidente:

- `productCreate` pide **`ProductCreateInput`** y `productUpdate` pide
  **`ProductUpdateInput`**. No comparten tipo; `ProductInput` ya no vale.
- Un producto en **borrador no admite canales de venta**: `publishablePublish`
  devuelve éxito y no hace nada. Hay que ponerlo en `ACTIVE` primero.
- `translationsRegister` necesita el **digest recién pedido**, después de
  escribir el original. Si cambias el texto, el digest anterior ya no sirve.
- El idioma primario de la tienda es el **castellano**; en/fr/de/ja están
  publicados, y de/ja caen al castellano porque no tienen traducción.
- `menuUpdate` pide **`MenuItemUpdateInput`** y `menuCreate` **`MenuItemCreateInput`**,
  igual que los productos. Los enlaces del menú se traducen aparte, como
  recursos de tipo `LINK`, uno por entrada.
- **`shopPolicyUpdate` está fuera de alcance**: pide `write_legal_policies`, un
  permiso que esta app no tiene. Las políticas solo se tocan desde el panel.
- Traducir el `handle` de una colección crea su URL localizada
  (`/en/collections/supplements`). Está hecho en las seis, pero **cuál es el
  handle traducido de cada una no consta en el repositorio**: hay que
  preguntárselo a la tienda antes de escribir un enlace a una colección desde
  un texto traducido. `articulos_en_fr.COLECCION` los tiene a `None` por eso.
- **`blogByHandle` ya no existe** en el QueryRoot de 2025-01: devuelve «Field
  'blogByHandle' doesn't exist». Se busca con `blogs(first: 1, query:
  "handle:diario")`. Estaba escrito en `traducir_blog.py` y habría fallado en
  la primera pasada real.
- **Reescribir un menú vuelve a crear sus enlaces con identificadores nuevos**,
  y las traducciones se quedan colgando de los viejos. Hay que volver a pedir
  los `LINK` y registrarlas después de cada `menuUpdate`. Se comprobó: tras
  añadir la FAQ al pie, los once enlaces del pie salían con
  `translations: []`.
- **El cuerpo de una página no se puede actualizar por el conector si es
  grande.** `pageUpdate` exige mandar el cuerpo entero, y el de VI.P son
  437 KB: no caben en una llamada. Se arregla desde el panel o con acceso
  directo a la API.
- Las claves traducibles de un artículo (`title`, `body_html`, `summary_html`,
  `meta_title`, `meta_description`) **las dice la tienda** en
  `translatableContent`. `traducir_blog.py` pide la lista y solo manda las que
  existen, en vez de escribirlas de memoria: `blog.py` se hizo a ciegas con la
  referencia delante y hubo que corregirlo.

## Lo que sigue pendiente

1. **No hay app de descargas digitales.** Once productos cobran y no entregan
   nada. Se instala desde el panel; por API no se puede.
2. **El nombre de la tienda sigue siendo «VIllumination».** Sale en la pestaña
   del navegador, en el checkout y en cada correo. No se puede cambiar por API:
   es Ajustes → Detalles de la tienda.
3. **El Diario ya está entero en tres lenguas** en el repositorio: los nueve
   artículos, con sus metaetiquetas y sus cuerpos. Lo que falta es registrarlo
   en la tienda —van 2 de 9 publicados— con `traducir_blog.py`. Los 29 de
   proveedor y los 11 propios ya estaban. Al traducir, **no se copia el texto
   del proveedor como versión inglesa**: viene lleno de declaraciones de salud
   y las devolvería por la puerta de atrás. Se traduce lo que hay escrito aquí.

   Tres cosas que `articulos_en_fr.py` admite porque los artículos no son
   todos iguales: `cierre` en vez de `libro` cuando el remate son párrafos
   propios; `firma` propia para los dos esotéricos, que advierten de que el
   tarot y la astrología no son ciencia predictiva en vez de hablar de
   atención sanitaria; y `base="tradicion"` para esos mismos, que es la mezcla
   que una vez se publicó mal.
4. **Las políticas de la tienda están mal y no se arreglan por API.** Escriben
   la marca como «VIllumination», están redactadas en inglés bajo títulos
   franceses, y las condiciones del servicio llevan a la vista literales sin
   rellenar: `[INSERT TRADING NAME]`, `[INSERT BUSINESS ADDRESS]`, `[LINK]`.
   Aparte de eso, la política de reembolso niega remedio incluso para producto
   defectuoso o no entregado, lo que en Quebec es dudoso que se sostenga y
   además invita a la contracargo. Es cosa de mirarlo con calma en el panel.
5. Precio provisional de 9,99 CAD en los seis libros nuevos. Los **planes**
   sí están decididos: 9,99 / 19,99 / 34,99 CAD **al mes**, y así lo dicen las
   66 láminas. Falta comprobar que Shopify cobre exactamente eso y que haya app
   de suscripciones; un cobro único de lo que el documento anuncia como
   mensualidad es una discrepancia de precio, y en Quebec invita a la
   contracargo.
6. **Los dos jabones siguen en UNLISTED.** Ya tienen colección, SEO y variantes
   corregidas; solo falta decidir si se venden. Piden envío y no llevan control
   de existencias, así que activarlos significa poder vender sin stock.
7. **Dos locales publicados sin una sola traducción: `de` y `ja`.** Shopify
   emite hreflang apuntando a `/de/…` y `/ja/…` y sirve castellano, así que
   para el buscador son copias del mismo contenido bajo URL distintas. O se
   traducen o se despublican; dejarlos así reparte la fuerza entre cinco
   direcciones que dicen lo mismo. Lo cuenta `tienda/visibilidad.py`.
8. **El CRM está escrito y sin enchufar.** Las cinco secuencias de
   `correos.py` no tienen a quién escribir: no hay punto de captura de correo
   en la tienda. Tampoco hay píxel de Meta ni etiqueta de Google, así que
   correr anuncios hoy sería pagar sin poder medir cuál vende.
9. **El blog «suplementos» está vacío.** Cero artículos, ninguna entrada de menú
   apunta a él, y aun así `/blogs/suplementos` es una página indexable sin
   contenido. O se llena o se borra desde el panel; no se ha tocado porque
   borrar no se deshace.

## Si acabas de clonar esto

Dos cosas no viajan en el repositorio y hay que rehacerlas a mano en cada
máquina nueva:

```
uv tool install graphifyy && graphify install --platform claude
graphify hook install     # post-commit: rehace el grafo al confirmar
```

Los hooks de git viven en `.git/hooks/`, que git no versiona por diseño. El
`.claude/settings.json` sí viaja, y está escrito para no romperse si graphify
no está instalado: comprueba antes de llamar.

La bóveda de `boveda/` se abre como *vault* en Obsidian. Empieza por
`000 · VILLUMINATIONS.md`, que es la única nota escrita a mano.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
