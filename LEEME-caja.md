# La caja y la pantalla de acceso

Guia viva: https://claude.ai/code/artifact/d8110dcf-267b-4fdb-81bd-e082cc122332

Escrito el 11 de octubre de 2026. Este archivo se ha corregido tres veces y las
correcciones estan marcadas, porque dos de ellas eran errores mios y conviene
que se vean:

- Una version recomendaba la caja **en claro con acento morado**. Era peor
  consejo: en oscuro la paleta de la tienda funciona entera.
- Otra version decia que `villuminations-logo-ancho-fondo.png` **lleva fondo
  claro**. Es falso: el generador le pinta un fondo **casi negro**.
- Otra version daba `#23234a` para los bordes. No vale: contra el campo
  `#121228` da **1,23:1** y el minimo para un borde es 3:1.

---

## Un editor, dos pantallas

Shopify unifico la caja y las cuentas de cliente en una sola configuracion, con
una seccion de acceso que es exactamente `account.villuminations.com`. Lo que se
configura una vez sale en las dos. No hay que tocar la pantalla de acceso por
separado.

Perfiles de la tienda, comprobados por API:

| Perfil | ID | Estado el 11-oct 22:33 |
| --- | --- | --- |
| Configuration 2 de Villuminations | `2696020017` | borrador, listo para publicar |
| Configuration  de Ma boutique | `2065530929` | **publicado** |

Los dos perfiles llevan ya lo mismo, asi que publicar cualquiera de los dos no
rompe nada. El estado de publicacion se invirtio ese dia a las 22:33:25Z: antes
la publicada era «Configuration 2» y ahora es «Configuration de Ma boutique»,
con «Configuration 2» en borrador para prepararla antes de publicarla.

---

## Lo que ya esta aplicado, sin tocar nada a mano

Esto ya esta **en la caja de verdad**, hecho por API el 11 de octubre, en los dos
perfiles:

| Campo | Valor puesto |
| --- | --- |
| Logotipo de la cabecera | `villuminations-logo-ancho-fondo.png` |
| Ancho del logotipo | 200 px |
| `colors.global.accent` | `#7b2fff` |
| `colors.global.brand` | `#7b2fff` |

Antes de esto el perfil publicado tenia `designSystem` y `customizations` los dos
a **null**: cero personalizacion desde el 23 de septiembre. Por eso la caja
ensenaba «Villuminations» en texto negro del sistema y botones en el azul por
defecto de Shopify.

> **Publicar «Configuration 2» tal como esta no se va a notar.** Lleva lo mismo
> que la publicada, porque lo que falta —los fondos y los textos— es justo la
> parte que la API no deja escribir en Basic. La caja seguiria siendo blanca.
> Para que el cambio se vea hay que hacer los colores a mano en el editor
> **antes** de publicarla. Son los pasos de mas abajo.

**Por que el morado y no el cian.** Mientras la pagina siga siendo blanca, el
cian es ilegible: 1,77:1 contra 4,5:1 de minimo. El morado es el unico color de
la marca que aguanta sobre blanco, con 5,69:1. Es decir: el morado no es la
eleccion bonita, es la unica correcta **mientras la caja sea blanca**.

**Por que el logotipo con fondo y no el transparente.** La tinta del logotipo es
un degradado que arranca en cian (`#7df3ff`, `#00d4ff`). Sobre blanco esa mitad
desaparece. El archivo `-fondo` trae su propio panel `#05050f`, asi que el
degradado se lee entero. Queda como una placa oscura de marca sobre la pagina
blanca, que es un recurso normal de diseno y desde luego mejor que texto negro
del sistema.

> **Cuando pases la caja a oscuro hay que cambiar estas dos cosas.** Con fondo
> oscuro el morado baja a 3,42:1 y se queda corto, y la placa negra del logotipo
> se ve como un recuadro sobre el fondo. En oscuro van: acento **`#00d4ff`** y
> logotipo **`villuminations-logo-ancho.png`** (el transparente). Esta en el
> paso 3 y el paso 2 de la guia de abajo.

---

## Lo que no se puede hacer por API, comprobado campo por campo

No es una suposicion de la documentacion: se ha probado cada campo contra el
perfil borrador. El que falla devuelve siempre el mismo error:

> One or more fields cannot be modified with public access to the Checkout
> Branding API.

| Campo | Resultado |
| --- | --- |
| `customizations.header.logo` (imagen, ancho) | **se escribe** |
| `customizations.header.alignment` / `position` | **se escribe** |
| `designSystem.colors.global.accent` / `brand` | **se escribe** |
| `designSystem.colors.schemes.*` (fondos y textos) | bloqueado |
| `designSystem.colors.global` critical/success/warning/decorative | bloqueado |
| `designSystem.cornerRadius` | bloqueado |
| `designSystem.typography` | bloqueado |
| `customizations.favicon` | bloqueado |
| `customizations.primaryButton.*` | bloqueado |
| `customizations.header.banner` / `divided` / `colorScheme` | bloqueado |
| `customizations.main.colorScheme` / `orderSummary.colorScheme` | bloqueado |

Dos cosas sobre el porque:

- **Es el plan, y antes escribi aqui lo contrario.** La documentacion de Shopify
  lo dice sin rodeos: «Checkout styling customizations are available only to
  Shopify Plus merchants», y el objeto entero «requires [...] the shop must be
  on a Plus plan or a Development store plan». La tienda devuelve
  `planName: "Basic"` y `shopifyPlus: false`. Una version anterior de este
  archivo decia que no era cuestion de plan; lo deduje de que dos campos si
  escribian, y esos dos resultan ser el subconjunto que Shopify deja por debajo
  de Plus. El plan es la puerta.
- **Plus no se toca por esto.** Cuesta del orden de 2.300 USD al mes frente a
  los 39 del Basic. Pagar eso para cambiar unos colores que el editor manual
  deja cambiar gratis no tiene ningun sentido.
- `checkoutBrandingUpsert` esta marcada como obsoleta y la propia API dice que
  se use `checkoutAndAccountsConfigurationUpdate`. Esa mutacion **no existe en
  la version 2026-01**, que es a la que esta fijado el conector. Comprobado:
  la busqueda de `checkoutAndAccounts` en el esquema de mutaciones no devuelve
  nada.

Resumen: los fondos, los textos, los botones, la tipografia y las esquinas
**solo se cambian a mano en el editor**, que si entra en el plan Basic.

---

## El dato que decide: contraste

Contraste de la paleta de la tienda sobre la superficie de marca `#0b0b1e`,
comparado con el blanco que hay ahora. El minimo para texto es 4,5:1.

| Color | Sobre oscuro | Sobre blanco |
| --- | --- | --- |
| Cian `#00d4ff` | **10,97:1** | 1,77:1 |
| Verde `#00e87b` | **11,87:1** | 1,64:1 |
| Naranja `#ff7700` | **7,30:1** | 2,66:1 |
| Rosa `#ff2ecb` | **6,02:1** | 3,23:1 |
| Morado `#7b2fff` | 3,42:1 | **5,69:1** |
| Texto `#d8f6ff` | **17,16:1** | — |

En blanco solo aguanta el morado. En oscuro aguanta todo **menos** el morado,
incluido el cian, que es el color principal de la marca. En oscuro el morado
pasa a servir para bordes y detalles, no para texto.

Boton solido cian con texto negro: **11,86:1**. Es el mismo lenguaje de boton
que ya usa la tienda.

---

## Los valores de la caja oscura

| Donde | Valor | Comprobacion |
| --- | --- | --- |
| Fondo de la pagina | `#0b0b1e` | — |
| Fondo de bloques y campos | `#121228` | — |
| Texto | `#d8f6ff` | 17,16:1 sobre el fondo |
| Bordes y separadores | `#6b6fae` | 3,95:1 sobre el campo |
| Boton principal | fondo `#00d4ff`, texto `#000000` | 11,86:1 |
| Enlaces y acentos | `#00d4ff` | 10,97:1 |
| Esquinas de botones | 12 px | igual que la tienda |
| Esquinas de campos y tarjetas | 12–18 px | igual que la tienda |
| Tipografia | Assistant | la del tema |

### El borde es el valor que mas se falla

Un borde no es texto, pero tampoco vale cualquier cosa: WCAG pide **3:1** para
el contorno de un control. Dos valores que parecen razonables y no lo son:

| Borde | Sobre `#121228` | Vale |
| --- | --- | --- |
| `#23234a` | 1,23:1 | no |
| `#2e2f5c` | 1,47:1 | no |
| `#6b6fae` | **3,95:1** | si |

Si el borde no se ve, el cliente no distingue donde termina un campo y empieza
el siguiente, y en la pantalla de la tarjeta eso se paga en ventas perdidas.

### No usar negro puro

Los campos de la tarjeta los dibujan los proveedores de pago y no siempre siguen
el tema. Sobre negro puro, un campo que no obedezca canta como un recuadro
blanco. Con `#0b0b1e` el salto es mucho menor, y ademas es el color de
superficie que ya usa la tienda. Hay que comprobarlo en el movil antes de darlo
por bueno.

### El logotipo cambia con el fondo

El generador (`marca/generar-logotipos.mjs`, linea 75) pinta el fondo del
archivo `-fondo` en `#05050f`. De ahi sale la regla:

| Archivo | Fondo del archivo | Donde va |
| --- | --- | --- |
| `villuminations-logo-ancho.png` | transparente | caja **oscura** |
| `villuminations-logo-ancho-fondo.png` | `#05050f` casi negro | caja **clara** (lo que hay hoy) |

---

## Paso a paso para la caja oscura

Esto es lo que no puedo hacer yo. Son unos quince minutos.

El panel esta en frances, asi que va el nombre frances y, entre parentesis, de
que se trata. Los rotulos exactos del editor cambian de vez en cuando; cuando no
coincidan, busca por lo que hace, que es lo que describo.

### Antes de empezar

No hace falta duplicar nada: **«Configuration 2 de Villuminations» ya es el
borrador** y ya lleva el logotipo y el acento puestos por API. Se trabaja
directamente sobre ella y se publica al final.

`Paramètres` → `Paiement` (Configuracion → Pago). Ahi arriba esta el bloque de
la configuracion del pago con el boton `Personnaliser` (Personalizar).

### 1. Entrar, y mirar una cosa antes de nada

Abre `Personnaliser` sobre **Configuration 2**. Se abre un editor con la caja a
la derecha y los ajustes a la izquierda. Arriba a la derecha hay un selector de
escritorio/movil: lo vas a usar.

**Lo primero: busca los ajustes de color y mira si se dejan tocar.** La API
exige plan Plus, eso esta comprobado; lo que no he podido comprobar desde fuera
es si el editor manual los deja cambiar en Basic. Historicamente si, y es la
razon de que esta guia exista, pero el que lo sabe de verdad eres tu en cuanto
abres la pantalla.

- Si los colores se pueden cambiar: sigue con el paso 2.
- Si salen en gris o con un cartel de Plus: para aqui. **No contrates Plus por
  esto** — son del orden de 2.300 USD al mes contra los 39 del Basic. La caja se
  queda blanca con el logotipo y el morado que ya tiene, que es correcto y
  accesible, y ese dinero rinde mucho mas en los seis puntos del final de este
  archivo.

### 2. El logotipo

En los ajustes, el apartado del logotipo (`Logo`).

1. Cambia la imagen a **`villuminations-logo-ancho.png`** — el transparente. El
   que hay puesto ahora (`-fondo`) trae panel negro y en oscuro se veria como un
   recuadro.
2. Ancho: **200 px** en escritorio.
3. Posicion: a la izquierda.

### 3. Los colores

Es el paso largo y el que de verdad cambia la pantalla. Shopify no te deja
pintar cada cosa por separado: trabaja con **esquemas de color** (`Schéma 1`,
`Schéma 2`). Un esquema es un juego de fondo + texto + boton, y luego dices que
zona usa cada esquema. Normalmente el cuerpo de la caja usa el esquema 1 y la
columna del resumen del pedido usa el esquema 2.

Rellena **los dos esquemas** con estos valores. Si solo haces el 1, el resumen
del pedido se queda blanco al lado de una caja oscura, que es peor que no tocar
nada.

**Esquema 1 — el cuerpo de la caja**

| Ajuste | Valor |
| --- | --- |
| Fondo | `#0b0b1e` |
| Texto | `#d8f6ff` |
| Fondo de los campos y bloques | `#121228` |
| Borde | `#6b6fae` |
| Boton principal, fondo | `#00d4ff` |
| Boton principal, texto | `#000000` |
| Enlaces / acento | `#00d4ff` |

**Esquema 2 — la columna del resumen**

Los mismos valores, con una sola diferencia: el fondo va en **`#121228`** en vez
de `#0b0b1e`, para que la columna se separe del cuerpo sin necesidad de linea.

**Y el acento global.** Donde este el color de acento general, cambialo de
`#7b2fff` a **`#00d4ff`**. El morado era para la pagina blanca; en oscuro se
queda en 3,42:1.

### 4. La tipografia

Apartado de tipografia (`Typographie`). Elige **Assistant** en los dos sitios,
titulos y cuerpo. Es la fuente del tema, asi que la caja deja de parecer otra
web. Si no sale en el catalogo, deja la que mas se parezca de palo seco y no
pierdas tiempo: importa mucho menos que los colores.

### 5. Las esquinas

Apartado de esquinas o formas (`Coins`, `Formes`). Botones **12 px**, campos y
tarjetas entre **12 y 18 px**. Son los mismos radios que `button_radius` y
`card_radius` del tema, por eso coinciden.

### 6. Imagen de fondo, solo si quieres

Se le puede poner una imagen a la columna del resumen. Dos condiciones: que sea
oscura, para que el texto siga leyendose, y **sin una sola letra dentro**. El
texto en una imagen no se traduce, y la tienda vende en varios idiomas.

### 7. Probarlo, que es el paso que nadie hace

En el selector de arriba pasa a **movil** y repasa la caja entera.

Luego, y esto es lo importante, **pruebalo de verdad**: crea un descuento del
100 %, metete un producto en el carrito y llega hasta la pantalla de la tarjeta.

Lo que hay que mirar ahi:

- **Los campos de la tarjeta.** Los pinta el proveedor de pago, no Shopify. Si
  salen como recuadros blancos sobre el fondo oscuro, sube el fondo de la pagina
  de `#0b0b1e` a `#121228` y vuelve a mirar: el salto se nota mucho menos.
- **Que se ve donde acaba cada campo.** Si no, el borde se quedo demasiado
  oscuro: ponlo en `#6b6fae`.
- **El boton de pagar.** Cian con texto negro, no cian con texto blanco: el
  blanco sobre cian da 1,6:1 y no se lee.

### 8. Publicar

Cuando la copia este bien, publicala desde la lista de configuraciones. La
publicada pasa a ser esta.

### 9. Comprobar la otra pantalla

Entra en `account.villuminations.com`. Tiene que haber cambiado **sola**, sin
tocar nada: es la misma configuracion. Si sigue en blanco, es que publicaste la
copia equivocada.

---

## Antes de encender los anuncios

Por orden de cuanto cuesta equivocarse. Los tres primeros no se alcanzan desde
esta sesion.

1. **Que los PDF se entregan.** El conector de productos digitales responde
   `Forbidden`, asi que no se ha podido comprobar, y es el fallo mas caro
   posible: el cliente paga y no recibe nada. Crea un descuento del 100 %,
   comprate un plan, un Codice y el Elite, y abre los archivos que lleguen.
   Este descuento te sirve tambien para el paso 7 de arriba.
2. **El pixel de Meta.** Al conector le falta el permiso `read_pixels`.
   Comprueba que esta instalado y que dispara `ViewContent`, `AddToCart` y
   `Purchase`.
3. **La verificacion del dominio en Meta.** El ajuste `seo_facebook_domain`
   sigue vacio; el tema emite la etiqueta en cuanto se pegue el codigo.
4. **SPF, DKIM y DMARC.** El 27 de septiembre no existia ninguno. Hoy no se
   puede releer: este contenedor no tiene DNS de salida.
5. **El envio gratis.** La tienda lo regala a partir de 75 CAD en Canada y 100
   CAD en EE. UU. con la barra del tema apagada.
6. **No apuntar anuncios a `/collections/cuidado-personal`**: cuenta dos
   productos y los dos estan ocultos, asi que esta vacia para el visitante.

## Dos cosas ya corregidas en la tienda

- **23 precios tachados valian 0,00** en once productos. No se veia en la
  tienda, pero viajaba al catalogo de Meta y de Google. Todos a nulo.
- **Diez codigos de barras repetidos**: las bandas de resistencia repartian
  `705353502002` entre ocho variantes y el entrenador respiratorio
  `313106953942` entre dos. Un GTIN identifica una unidad vendible, asi que no
  eran GTIN sino el codigo interno del proveedor. Los diez a nulo; el catalogo
  pasa a identificarlos por marca + SKU.
