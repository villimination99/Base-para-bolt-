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
python3 tienda/correos.py    # los cinco correos automáticos y cómo se montan
python3 tienda/captura.py    # el formulario de captura y su consentimiento
python3 tienda/menus.py      # la navegación, con sus traducciones
python3 tienda/ropa.py       # láminas propias disponibles para estampar
python3 tienda/calendario.py # los doce lanzamientos y sus fechas
python3 ropa/tools/generar.py # rehace las doce láminas de espalda
python3 tienda/hero.py       # el vídeo de 5 s de la cabecera y su póster
python3 tienda/visibilidad.py # superficie indexable, datos estructurados y CRM
python3 libros/tools/faltan.py
python3 tablero.py           # rehace tablero/index.html con el estado del sistema
python3 auditar.py           # lo que solo se ve mirando todas las superficies juntas
python3 tienda/huellas.py --desde HEAD~1   # de lo tocado, qué hay que volver a registrar
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
python3 tienda/cotejar.py             # ¿dice la tienda lo que dice el repositorio?
```

`cotejar.py` es el que faltaba: `auditar.py` cruza ficheros del repositorio y
ninguno cruzaba el repositorio con la tienda. Compara byte a byte las noventa
traducciones del Diario y las de la FAQ, exige el prefijo de idioma en cada
enlace de las cuatro superficies, mira `outdated` y avisa de lo que está
traducido a una lengua y no a la otra. **Solo lee.**

`despegue.py` **solo lee**: no tiene una sola mutación. Contesta de una vez las
preguntas que no se deducen del repositorio —si hay pasarela, si hay zonas de
envío, qué productos están a precio cero o sin publicar— y dice al final lo que
ni siquiera él puede ver.

Los cinco correos automáticos viven en `tienda/correos.py`, en tres lenguas y
con las mismas prohibiciones que las fichas. **No se publican por API**: las
automatizaciones se montan en Marketing → Automatizaciones y el texto se pega
allí. `--texto` los saca en claro.

**Antes de dar de alta ropa estampada**, `tienda/ropa.py`. Un diseño no se
publica si no señala su lámina dentro del repositorio: hay **110 láminas
propias** en `libros/partials/`, `planes/partials/` y `ropa/partials/`,
vectoriales y de propiedad entera, y no hace falta buscar dibujos fuera.
Faltan por rellenar la hoja del proveedor de estampación y qué lámina va en qué
prenda; ninguna de las dos se puede inventar.

**El calendario no va por meses, va por la rueda.** `tienda/calendario.py`
tiene doce lanzamientos y cada uno abre el día que abre su temporada: Aries el
21 de marzo porque ese día empieza Aries. Doce colores repartidos por los meses
los monta cualquiera; esto no, porque pide tener los doce signos dibujados, un
libro sobre ellos y un artículo sobre los decanos. Las láminas las genera
`ropa/tools/generar.py` y **no se editan a mano**, como los libros y los planes.

El elemento no cambia solo el color: cambia el dibujo —fuego veintiuna
costillas, tierra doce, aire veintitrés, agua dieciséis—. Y las cifras del
texto **las comprueba `calendario.comprobar()` contra lo que el generador
dibuja**, que es la guarda de `comprobar_laminas()` traída aquí: allí la prosa
prometió siete láminas y había seis, en tres idiomas. Mordió a la primera. Las
otras tres guardas: cada lanzamiento señala una lámina que existe, las doce
temporadas embaldosan el año sin huecos ni solapes, y tres signos por elemento
o los tonos de acento se repetirían.

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

El precio de esa comodidad es que **traducir un artículo caduca la traducción
ya registrada de los que lo citan**: su cuerpo se compone distinto en cuanto el
destino existe. Los dos que estaban publicados desde antes tenían guardada la
cita sin ancla, y desde la tienda no se nota —el texto se lee bien—, así que
durante un tiempo esto se resolvió acordándose. Acordarse no es una
comprobación.

**`tienda/huellas.py` lo dice sin acordarse de nada.** Guarda el SHA-256 de
cada valor que se manda a la tienda —que es exactamente el `digest` que
devuelve `translatableContent`, no un número parecido— y contesta de dos
maneras: contra el sello de lo que consta subido (`--sellar` lo pone, y se
pone **después** de que la mutación haya terminado bien) o contra un commit
(`--desde HEAD~1`), que no necesita que nadie haya sellado nada. Ve las
cadenas: al aparecer un artículo nuevo salen también los cuerpos de las fichas
que lo citaban.

**Un enlace de un texto traducido lleva su prefijo de idioma.** Shopify no
reescribe lo que va dentro de un cuerpo: `href="/pages/contact"` sale tal cual,
así que desde una página inglesa manda al comprador a la castellana. La guarda
existía en `articulos_en_fr.py`, pero enumeraba tres prefijos conocidos
—`/products/`, `/blogs/`, `/collections/`— en vez de comprobar la regla, y por
eso no veía `/pages/`. Estuvieron publicados así ocho enlaces: los dos de la
FAQ, cuatro de «cómo se hace» y dos de la colección de suplementos. Ahora las
dos guardas —`faq.comprobar()` y `articulos_en_fr.comprobar()`— valen para
cualquier ruta, y las dos muerden también al revés: un `/en/` dentro del
castellano. **Enumerar los casos conocidos no es comprobar la regla.**

**Hay texto que solo vive en la tienda.** Los cuerpos traducidos de las seis
colecciones y de las páginas «cómo se hace», VI.P y «tus opciones de
privacidad» se escribieron directamente en el panel: no hay fuente aquí que los
regenere ni comprobación que los mida, y por eso el fallo de los enlaces vivió
en ellos sin que nadie lo viera. `cotejar.py` los enumera al final para que
conste de qué no responde el repositorio.

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
  (`/en/collections/supplements`). Está hecho en las seis, y ya consta cuál es
  cada uno —preguntado a la tienda, no deducido—:

  | castellano | en | fr |
  |---|---|---|
  | `suplementos` | `supplements` | `complements` |
  | `ropa` | `apparel` | `vetements` |
  | `equipo` | `equipment` | `equipement` |
  | `conocimiento` | `knowledge` | `connaissance` |
  | `planes` | `training-plans` | `plans-d-entrainement` |
  | `cuidado-personal` | `personal-care` | `soins-du-corps` |

  `articulos_en_fr.COLECCION` sigue con `None`: rellenarlo cambia los enlaces
  que salen en los cuerpos, y eso obliga a registrar de nuevo los nueve
  artículos. Es una decisión, no un descuido.
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
- **El `digest` de `translatableContent` es el SHA-256 del valor**, tal cual.
  Comprobado con el cuerpo de la FAQ: `sha256(fichero)` da exactamente el
  digest que devuelve la tienda. Sirve para cotejar un original contra el
  repositorio **sin descargarlo**, que es la comprobación barata que faltaba.
  Las traducciones no llevan digest; esas hay que pedirlas.
- **Pero Shopify reescribe el HTML que recibe**, así que el digest no cuadra
  nunca con el `body_html` del repositorio: `<li><strong>` vuelve como
  `<li>\n<strong>` y un salto de línea dentro de una etiqueta vuelve
  colapsado. Sirve para títulos, resúmenes y metaetiquetas; para cuerpos no.
  No se arregla enumerando las reglas del normalizador — enumerar los casos
  conocidos no es comprobar la regla.
- **Y para lo que sirve, coge lo que hay que coger.** Al crear los dos
  artículos de agosto encontró en el acto dos derivas de transcripción: un
  resumen y una metadescripción retecleados dentro de la mutación en vez de
  mandados desde el repositorio. El fallo del «veintivún», otra vez. Por eso
  el payload se genera con un script y se cotejan los digests **después** de
  registrar.
- **`Translation.outdated` dice si el original cambió después de la
  traducción.** Es un booleano por clave y por lengua, así que se piden las
  cien de una vez y se ve de un vistazo si algún digest iba caducado. Es lo
  más barato que hay para saber que un registro entró contra el texto vivo.
- El `handle` de una **página** sí se traduce y crea su URL localizada
  (`/en/pages/faq`, `/fr/pages/questions`). Es lo contrario que en los
  artículos del Diario, donde traducirlo rompería los cuarenta enlaces de
  `lecturas.py`. Que sean recursos parecidos no quiere decir que se traten
  igual.

## Lo que sigue pendiente

1. **No hay app de descargas digitales.** Once productos cobran y no entregan
   nada. Se instala desde el panel; por API no se puede.
2. **El nombre de la tienda sigue siendo «VIllumination».** Sale en la pestaña
   del navegador, en el checkout y en cada correo. No se puede cambiar por API:
   es Ajustes → Detalles de la tienda.
3. **El Diario está entero en tres lenguas**, en el repositorio y en la
   tienda: los nueve artículos quedaron registrados en inglés y en francés
   —cuerpo, título, resumen y las dos metaetiquetas, 9 de 9—. Los 29 de
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
8. **El CRM está escrito y falta enchufarlo.** Ya está todo el texto: las
   cinco secuencias de `correos.py`, con qué plantilla de Shopify se monta
   cada una (`AUTOMATIZACION`), y el formulario de captura de `captura.py` en
   tres lenguas con el consentimiento que piden la CASL y la Ley 25 de Quebec
   —casilla sin marcar, quién lo pide, para qué y cómo darse de baja—.

   Lo que falta es de panel y de tema: pegar el bloque de
   `tienda/tema/captura-correo.liquid.txt` en el tema y crear las cuatro
   automatizaciones activables. La quinta, `entrega`, **no se activa** hasta
   que haya app de descargas: manda un enlace que hoy no lleva a nada, y
   `SIN_ACTIVAR` lo dice.

   Sigue sin haber píxel de Meta ni etiqueta de Google, así que correr
   anuncios hoy sería pagar sin poder medir cuál vende.
9. **Las tres superficies a medio traducir, una resuelta y dos por decidir.**

   `creatina` **ya está traducido entero** a inglés y francés en
   `articulos_en_fr.py`, y falta registrarlo. Su castellano vive solo en la
   tienda —lo escribió el dueño ahí—, así que entra por `SIN_FUENTE`: se
   compone sin pie de fuentes ni remate de libro porque su original tampoco
   los lleva. Sus tres traducciones inglesas estaban además **caducadas**
   (`outdated: true`), o sea que el castellano cambió después de
   registrarlas; al volver a registrar se arregla eso también.

   `app` **está sin publicar y vacío**: sin resumen y sin cuerpo. Es el
   borrador que Shopify deja por defecto. No es indexable, pero arrastra una
   traducción de título huérfana. Lo limpio es borrarlo; no se ha hecho
   porque borrar no se deshace.

   La página **VI.P** sigue con cuerpo y título en inglés y nada en francés.
   No tiene fuente aquí y son 437 KB, así que es trabajo de panel.
10. **El blog «suplementos» está vacío.** Cero artículos, ninguna entrada de menú
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
