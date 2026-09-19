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
python3 ropa/tools/dibujar-espinas.py --hoja  # la serie de filigrana orgánica
python3 ropa/tools/exportar-pod.py --todas    # los 24 PNG de impresión bajo demanda
python3 ropa/tools/maqueta.py                 # las maquetas de prenda para anuncios
python3 ropa/tools/paquete-pod.py             # el catálogo, el LEEME y el ZIP
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

**La serie espina** (`ropa/tools/dibujar-espinas.py`) es la que sigue el género
de filigrana orgánica que pidió el dueño. Cuatro cosas la sostienen, y las
cuatro salieron de comparar con la referencia y luego renderizar:

· **Cinta, no trazo.** Cada nervio es una banda rellena calculada desplazando
  una línea central; un `stroke` de grosor constante da dibujo de cable.
· **Perfil de hoja, punta en los dos extremos.** El primer perfil arrancaba a
  plena anchura y dejaba cortes romos: los troncos de manga y pantalón salían
  como barras cortadas a sierra. Ahora el ancho es un seno que vale cero en
  los dos extremos.
· **El acento va DEBAJO y más ancho**, no encima. Encima son dos tintas
  planas; debajo asoma por el canto y parece que algo brilla dentro. Con
  `stroke-width` 7 se comía el hueso y con 2,6 seguía borrando el afilado —un
  trazo fijo sobre una forma que se afila a cero acaba siendo toda la forma—.
  A 1,2 asoma y no manda. `comprobar()` aborta si el hueso se dibuja antes que
  el acento.
· **La separación tiene que superar al grueso.** Tres troncos de 21 a 22 de
  distancia se solapaban en una plancha de borde escalonado. No es un dibujo,
  es un fallo de composición, y solo se ve renderizando.

El símbolo **no fija el acento**: lo heredaba del contenedor y lo fijaba a la
vez, así que las tres columnas de la hoja salían cian. Los valores por defecto
viven en el `<svg>` de fuera.

**La marca va dentro del dibujo, y no como sello.** `armazon_vi()` dibuja la
**V** y la **I** de VILLUMINATIONS como esqueleto de la lámina dorsal: dos hojas
rectas bajan de los hombros y se juntan en un vértice, y del vértice cae la
columna. Todo lo demás crece colgado de ellas. Lo que la hace legible a tres
metros no es el tamaño sino el **contraste de ritmo** —armazón recto y macizo
contra filigrana curva y fina—, y por eso la V aparece de lejos y desaparece de
cerca, que es lo que se pidió.

Costó tres intentos y los tres fallos son la misma lección:

· Los brazos medían menos que la filigrana y la marca quedaba **enterrada
  dentro del bulto**. Tienen que ser lo más ancho de la lámina.
· Con el hueco entre los brazos lleno de costillas, la forma se lee como
  **ala, no como letra**. Una V solo es una V si su interior está limpio: las
  costillas nacen ahora **sobre el brazo** y crecen hacia afuera.
· Con el brazo liso la pieza perdía carácter, así que lleva púas finas en el
  canto interior: pesan poco y no vuelven a llenar el hueco.

**La prueba de bizco es la que decide.** Se mira la lámina a 110 px y con dos
píxeles de desenfoque: si la V no aparece ahí, no aparece a tres metros, y eso
no se juzga a tamaño completo. Está en la hoja de aprobación.
`comprobar()` exige además que el armazón sea `ARMAZON_MINIMO` veces la
costilla mayor; si algún día se engorda la filigrana sin mirar esto, la marca
se pierde y nadie se entera hasta ver la prenda impresa.

**Un fichero para Printful no es un SVG bonito.** `ropa/tools/exportar-pod.py`
traduce la lámina de pantalla al fichero de impresión, y las reglas que hace
cumplir son físicas, no de gusto: 300 ppp, fondo transparente, **ninguna
opacidad parcial** —la DTG no hace medias tintas—, **ningún rasgo por debajo de
1 mm impreso**, ningún hueco interior que se empaste y encaje en el área. Al
exportar la dorsal saltaron las dos primeras a la vez: el halo iba al 0,92 y el
arco y las marcas de decanato a 0,67 y **0,31 mm**, o sea que las marcas se
habrían caído enteras de la plancha. `endurecer()` lo arregla en el fichero de
impresión y deja el de pantalla como está: el destino impone sus mínimos, no el
dibujo.

La consecuencia visible es que **la lámina impresa lleva el arco más grueso que
la de pantalla**. No es un descuido: por debajo de 1 mm no hay lámina.

**EL LIENZO ES EL ÁREA DE ESTAMPACIÓN, NO EL DIBUJO.** Es la regla que manda
sobre las demás y la que costó una tirada mal escalada. La primera versión
sacaba el PNG **al tamaño del dibujo**: el pecho salía a 9 cm, 1063 píxeles. Al
subirlo, la aplicación lo encaja en su área —30,5 × 40,6 cm en el frente— y al
estirar 1063 píxeles a 30,5 cm quedan **88 ppp**, así que avisa de resolución
insuficiente y hay que encogerlo a mano hasta que calle. Eso no es un fichero,
es una negociación, y la segunda tirada sale a otro tamaño que la primera
porque nadie apuntó cuánto se encogió. Ahora el PNG mide **exactamente el área
a 300 ppp** y el dibujo va dentro con transparencia alrededor: encajar al área
—que es lo que la aplicación hace sola— deja el dibujo en su sitio y a 300 ppp
exactos. `verificar()` aborta si el lienzo no mide lo que mide el área.

**En DTG el pecho no es un área, es un sitio dentro del área frontal.**
Tratarlo como un área de 10 × 10 cm es justo lo que producía el aviso. Y va
**centrado a propósito**: «pecho izquierdo» se coloca en la industria unas
veces a la izquierda de lo que se ve y otras a la del que lleva la prenda, que
son lados contrarios; centrado no tiene lado que equivocar.

**El área no es la misma en toda la prenda.** `AREAS` la guarda por posición
—espalda y frente 30,5 × 40,6 cm, manga 10 × 40, pernera 24 × 30— y
`COLOCACION` dice a qué tamaño y en qué punto del área va cada pieza. Darle a
todas la de la espalda es la manera de mandar a producción una lámina que no
cabe. La pernera iba a 10 cm de ancho y 4 del borde: 26,2 + 4 son 30,2 en un
área de 30 y **se salía por dos milímetros**; lo cazó la guarda de encaje.
Son las estándar del catálogo: **hay que cotejarlas con el producto concreto**,
que varían entre modelos.

**Los `stroke-width` no dicen nada del dibujo.** La serie espina está hecha de
**cintas rellenas** —siluetas calculadas, no trazos—, así que la comprobación
por atributo no veía el 90 % de lo que se imprime: podía dar por bueno un
nervio de medio milímetro porque no era un `stroke`. `medir()` rasteriza y mide
**píxel a píxel**: para cada punto de tinta el grosor local es el menor de su
recorrido horizontal y su vertical, que estima la anchura de una forma sin
saber su geometría. El hueco se mide igual y solo cuenta el interior —un claro
con tinta a los dos lados—, porque un hueco de medio milímetro se cierra en la
plancha y dos nervios salen como mancha.

Se vigila la **fracción**, no el mínimo: el hueco más estrecho sale siempre en
torno a un píxel porque en algún cruce dos cintas se rozan, y eso es un empalme,
no un defecto. Medido sobre la serie: tinta fina del 0,98 % al 1,8 %, hueco fino
del 0,7 % al 1,2 %. Los umbrales están a dos veces y media el peor.

**La paleta de impresión se deriva, no se retecléa.** `_compensar()` baja el
valor un 16 % y deja tono y saturación donde estaban; por debajo de 0,85 de
valor la tinta ya es honda y se deja. La regla no es un invento: reproduce
—dentro de dos o tres pasos— los tres acentos que se habían ajustado a ojo
antes de que existiera, y por eso se puede confiar en ella para los que vengan.
Un acento nuevo se añade **una sola vez**, en `dibujar-espinas.ACENTOS`, y el
de impresión sale solo. Son seis a impresión: cian, **cardenal**, **oro**,
púrpura, magenta y hielo.

**El hueso es la excepción y va al revés.** No se compensa hacia abajo: se
empuja hacia arriba (`#ECEFF6`), porque la base blanca levantándolo es justo lo
que se quiere de él —es quien pone el contraste contra la prenda negra, mientras
el acento solo asoma por el canto—. Compensar los dos igual sería aplicar la
regla sin mirar para qué está cada tinta.

**`verificar()` abre el PNG escrito y lo comprueba.** No basta con haberlo
pedido: descomprime la primera fila de píxeles y deshace su filtro para mirar
el alfa de verdad, porque el fondo transparente es el fallo más caro de este
flujo y un metadato no prueba nada sobre los píxeles. Probada contra dos
ficheros rotos a propósito —uno sin `pHYs` y otro con la fila 0 opaca—: caza
los dos.

El PNG lleva su trozo `pHYs` escrito a mano —nueve bytes, `struct` y
`zlib.crc32`— porque sin él el fichero solo dice cuántos píxeles tiene y quien
lo abra decide el tamaño físico.

**El color de pantalla no es el color impreso.** La DTG sobre prenda oscura
imprime una base blanca y el color encima, y esa base levanta y desatura: el
cian de neón de la marca (`#00f0ff`) sale pálido. El fichero lleva `#00C4D6`,
más hondo, para compensar. Es compensación, no certeza: **hay que pedir muestra
y cotejarla antes de una tirada**. Lo que el fichero garantiza es lo
comprobable; el color lo dice la muestra.

**Las maquetas no son fotografías y no compiten con Printful.** Printful genera
maquetas fotográficas solas desde el fichero de impresión, con la prenda real y
gratis: **para la ficha de producto, esas**. `ropa/tools/maqueta.py` hace lo
otro, lo que Printful no da: la composición de marca para anuncio, publicación
y cabecera de colección. Tres cosas la sostienen:

· **La sombra va encima**, en una capa de pliegues por arriba de todo, para que
  oscurezca prenda y tinta a la vez y **atraviese** el estampado, que es lo que
  hace la tela de verdad. Pegarlo encima y ya se ve pegado: flota.
· **La tinta va en normal, no en `screen`.** Iba en `screen` por lo mismo —para
  que los pliegues la atravesaran—, pero eso ya lo hace la capa de arriba, así
  que `screen` solo sumaba: sumaba el tono de la tela al de la tinta y
  **aclaraba todos los acentos oscuros**. El rojo cardenal `#BC1733` salía en
  la maqueta como `#C63A57`, o sea frambuesa, y **la maqueta enseñaba un color
  que la plancha no imprime**. Se ve al añadir el primer acento oscuro; con
  cianes y magentas no se notaba.
· **Un negro fotografiado no es negro.** La tela va entre `#26262d` y `#3a3a44`
  sobre fondo claro. En la primera pasada iba a `#141419` sobre fondo casi
  negro y la prenda **desaparecía**: solo se veía el estampado flotando.
  Y los pliegues eran tres elipses enormes en `multiply` que salían como óvalos
  negros y se comían la silueta. Un pliegue es una línea de sombra, no media
  prenda.

Y la maqueta **coloca la lámina donde la coloca el fichero de impresión**, no
con sus propios números: si los dos sitios tuvieran su constante, llegaría el
día en que la maqueta enseña el estampado en un sitio y la prenda sale con él
en otro. Lo único que pone de su parte es `AREA_BAJO_CUELLO`, a qué altura de
la prenda empieza el área, que el fichero no sabe porque es cosa del producto.

**El paquete lo monta `ropa/tools/paquete-pod.py`, no una mano.** El anterior se
montó a mano y así tiene dos maneras de mentir y ninguna de avisar: manda
ficheros viejos —un PNG de la semana pasada se abre igual de bien— y su LEEME
lleva números retecleados que dejan de ser verdad. Ahora el LEEME **se genera**
de `exportar-pod.py` y `comprobar()` aborta si falta una lámina, sobra una, o
alguna es **más vieja que el generador**. Un ZIP que no se puede montar es
mejor que uno que miente.

**`ropa/VILLUMINATIONS-print-on-demand.zip`** es el paquete que se descarga: los
24 ficheros de impresión con su ficha y su vectorial, las maquetas, el catálogo
y el LEEME.

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

## Dos sesiones, una tienda: cómo no perderse información

Sobre villuminations.com trabajan **dos sesiones de Claude Code a la vez**:

| | rama | de qué responde |
|---|---|---|
| esta | `claude/shopify-diet-plans-9k0wti` | lo que la tienda **vende**: libros, planes, fichas, Diario, FAQ, CRM, ropa |
| la del tema | `claude/impulse-shopify-theme-a6mb8w` | el **tema**: plantillas, secuencia de portada, imágenes, i18n del tema |

Corren en contenedores distintos y **no comparten disco**: ni el grafo, ni la
bóveda, ni los ficheros. Lo único común es la tienda y **Mem0**.

**Antes de dar nada por pendiente, leer Mem0.** El 19/09 esta sesión tenía en
su lista «traducir o despublicar `de` y `ja`» cuando la otra los había
traducido **cinco días antes**, y mantenía un generador que deshacía una
corrección suya. Nada avisaba: los dos repositorios estaban en verde.

```
mcp__Mem0__list_entities                       # quién tiene memorias
mcp__Mem0__get_memories  filters={"AND":[{"user_id":"villumination"}]}
mcp__Mem0__search_memories  query="..."        # búsqueda semántica
```

**Escribir siempre con `user_id: "villumination"`, explícito.** Hay **cuatro
identidades** con memorias —`villumination`, `villimination99`, `mem0-mcp` y
`villimination`— todas con el mismo propietario, creadas por variantes de
escritura y por el identificador por defecto del servidor. La memoria está
repartida entre ellas y por eso no se encuentra. No se fusionan desde aquí
—borrar no se deshace—, pero **todo lo nuevo va a `villumination`**.

**Y escribir al terminar algo que la otra sesión pueda tropezar.** No el diario
de la sesión: lo que cambia sus decisiones. Un fichero que quedó obsoleto, una
trampa de la API, una regla que salió de un fallo real.

## Lo que sabe la otra sesión y aquí no se sabía

Este repositorio es **una de dos sesiones** sobre la misma tienda. La otra
trabaja el tema (rama `claude/impulse-shopify-theme-a6mb8w`) y guarda lo suyo
en **Mem0**. Sin leerlo, esta sesión daba por pendiente cosas ya hechas y
generaba ficheros que deshacían sus correcciones. Lo traído el 19/09:

**Una imagen es UNA para los cinco idiomas.** No existe versión francesa de un
PNG de colección. De ahí la regla: **lo que no se puede traducir no se escribe
dentro de una imagen**. Sustituyeron las seis portadas y la `og:image` por
versiones sin una sola letra. `tienda/portadas.py` quemaba el nombre dentro y
**está marcado como superado y aborta**: ejecutarlo desharía su arreglo.

**La marca ya está unificada en el tema**, a `VILLUMINATIONS` en plural, vía
`settings.brand_display_name` — de ahí salen el alt del logotipo, el
`aria-label`, el título de página, `og:site_name` y el nombre de los datos
estructurados. Lo que sigue en «VIllumination» es `shop.name` del panel, y eso
solo lo cambia el dueño porque Shopify lo usa en el checkout y en los correos.

**Printful ya está configurado** como uno de los tres perfiles de envío
(general, Supliful, Printful), con tarifas para Canadá, EE. UU., Francia,
Alemania y Japón. Los dieciséis ficheros de `ropa/pod/` tienen a dónde ir.

**Trampas de la API que descubrieron ellos** y que aquí habrían costado lo
mismo:

- `themeFilesUpsert` con `body {type: URL}` **acepta la llamada, devuelve
  `userErrors` vacío y no escribe nada**. Silencioso. Hay que usar
  `{type: BASE64}`, que devuelve `filename`, `size` y `checksumMd5`.
- La importación de un zip **se come `templates/robots.txt.liquid`**.
  Confirmado ocho veces; el zip demostrablemente lo contiene.
- **Las traducciones van pegadas a cada tema**: un tema nuevo hereda las que
  existían al arrastrarlo, pero no las registradas a mano después. Hay que
  volver a llamar a `translationsRegister` contra el gid nuevo. Los digests
  se reutilizan, porque el digest es del valor de origen y no del tema.
- `collectionUpdate` sobre una colección que **ya tiene imagen conserva el
  nombre de archivo viejo** y solo cambia el `?v=`. Para cambiarlo hacen falta
  dos pasos: `image: null` y luego la nueva.
- Shopify **antepone una cabecera de 363 bytes** a todo fichero `.json` de un
  tema. Hay que quitarla antes de comparar byte a byte; el campo `size` que
  devuelve la API sí es el tamaño original.
- `media(first: 12)` ocultó cinco imágenes de un producto que tenía 17.
  **Consultar siempre `mediaCount { count }`** antes de dar por barrido un
  catálogo.

**Bloqueos de publicidad que ellos encontraron** y que esta sesión no veía: la
política de reembolso dice «ALL SALES ARE FINAL», lo que choca con el derecho
de desistimiento de 14 días de la UE y con la ley de Quebec y **arriesga el
rechazo de Meta y de Google Merchant**; la dirección de contacto está
incompleta («quebec,Canada») y falta teléfono, que Meta exige para verificar; y
los canales de Facebook e Instagram **no están instalados**.

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
7. ~~Dos locales publicados sin una sola traducción: `de` y `ja`.~~
   **RESUELTO por la sesión del tema, no por esta.** Los doce artículos
   publicados están completos en inglés, francés, **alemán y japonés**, sin
   ninguna caducada. Comprobado contra la tienda el 19/09 sobre
   `gid://shopify/Article/558097170481`: las cinco claves en `de` y en `ja`
   con `outdated: false`.

   **`tienda/visibilidad.py` sigue diciendo lo contrario**: su constante
   `TRADUCIDOS = ("es","en","fr")` es de agosto y hay que subirla a cinco.
   Mientras no se haga, cuenta un problema que ya no existe.
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
graphify update .         # CONSTRUYE el grafo: sin esto no hay graphify-out/
graphify hook install     # post-commit: lo mantiene al día solo
```

Los tres, y en ese orden. `graphify-out/` está en `.gitignore`, así que en un
contenedor recién clonado **el grafo no existe** y las herramientas de consulta
tampoco: `update` es el que lo construye, y no cuesta llamadas a ningún modelo.
Faltaba decirlo aquí y se descubrió a la mala, con el grafo ausente.

**El gancho mantiene al día el grafo, no las notas.** Las de `boveda/` salen de
`graphify export obsidian --dir boveda` y hay que pedirlo. Llevaban desde
agosto sin rehacerse —solo 2 de 1280 mencionaban la capa entera de ropa— y por
eso la bóveda mintió un mes. El exportador respeta los ficheros que no ha
creado él, así que la nota escrita a mano sobrevive; aun así conviene copiarla
antes, porque es la única que no se puede rehacer.

**`.graphifyignore` excluye `boveda/`, y no es opcional.** Las notas salen del
grafo: si además entran en él se realimenta. Al regenerarlas el grafo pasó de
6672 nodos a **26 689, de los que 23 981 —el 90 %— eran las propias notas**.
Cada exportación lo multiplicaría por su reflejo y las consultas dejarían de
hablar del código para hablar de su documentación. Excluida la bóveda son 2676
nodos, todos de código. **El grafo es del código; la bóveda es cómo se lee.**

**El gancho revienta en confirmaciones enormes.** Mete la lista de ficheros
cambiados en una variable de entorno, y con los 6000 de la bóveda regenerada
falla con `Argument list too long` y no reconstruye nada. No avisa más que en
esa línea, así que tras un commit masivo hay que ejecutar `graphify update .`
a mano. Se descubrió confirmando la bóveda entera.

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
