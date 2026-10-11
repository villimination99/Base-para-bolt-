# La pagina de pago, y lo que falta antes de los anuncios

Escrito el 11 de octubre de 2026, a partir de la captura de la caja y de lo
comprobado contra la tienda. **No se ha tocado nada**: esto es el plan, y espera
tu senal.

---

## 1. Lo que se ve bien en la captura

No todo esta mal, y conviene decirlo antes de la lista de arreglos:

- **El pago express esta completo**: Shop Pay, PayPal, Apple Pay y Google Pay,
  los cuatro. En movil es la palanca de conversion mas grande que hay, y ya la
  tienes.
- **El francés es correcto.** Tu idioma base es el español, pero el francés esta
  publicado y tu telefono esta en francés, asi que la caja hace lo que debe. No
  es un fallo.
- **La casilla de marketing viene DESMARCADA.** Es lo correcto: marcarla por
  defecto es ilegal en la UE y te quemaria la lista.
- **No hay linea de envio** en un pedido de 19,99 $, porque es una descarga.
  Correcto.

## 2. El problema real: la caja no tiene NADA de tu marca

Comprobado por API sobre el perfil publicado («Configuration 2 de
Villuminations»):

    designSystem:   null
    customizations: null

Cero. El perfil no se ha editado desde el 23 de septiembre, el dia que se creo.
Por eso en la captura sale **«Villuminations» en texto negro del sistema** en vez
de tu logotipo, con el azul por defecto de Shopify y tipografia del sistema.

Tu tienda es negra con neon. Tu caja es blanca con azul. El comprador cruza de
un mundo a otro **justo en el momento en que escribe el numero de su tarjeta**.
Esa discontinuidad cuesta confianza, y la confianza en esa pantalla es dinero.

### Un limite que hay que saber antes de empezar

La **API** de personalizacion de la caja (`checkoutBranding`) **exige plan
Plus**. Estas en **Basic**. Lo he verificado en la documentacion, no es una
suposicion: por eso no puedo hacerlo yo por ti aunque me des la senal.

Lo que **si** esta en tu plan es el **editor de la caja**, a mano, en el panel.
Da logotipo, colores, tipografia y esquinas. Con eso se arregla el 90 % de lo
que se ve feo en la captura.

---

## 3. Paso a paso de la caja

Ruta: **Parametres → Paiement (Checkout) → Personnaliser**. Se abre un editor
parecido al del tema, con el panel de ajustes a la izquierda.

### Paso 1 — El logotipo

Tienes **dos versiones** subidas, y elegir mal aqui se nota:

| Archivo | Que es | Para que fondo |
| --- | --- | --- |
| `villuminations-logo-ancho.png` | 1600×400, transparente | **negro** — es el del tema |
| `villuminations-logo-ancho-fondo.png` | 1600×400, con fondo | **claro** — este es el de la caja |

El transparente esta dibujado para ir sobre negro. Sobre el blanco de la caja
puede salir ilegible o directamente invisible.

1. En el editor, seccion del encabezado → **Logo** → subir
   `villuminations-logo-ancho-fondo.png`.
2. Ancho: empieza en **160 px** y ajusta mirando la vista previa.
3. **Mira las dos** en la vista previa antes de decidir. Si la version con fondo
   te deja un rectangulo negro que no te gusta, la alternativa buena no es usar
   la transparente: es exportar una tercera version del logotipo en **tinta
   oscura sobre transparente**, pensada para fondo claro.

### Paso 2 — El color de accion

Aqui hay una respuesta correcta y no es la que parece. Estos son los contrastes
de tus colores de marca sobre el blanco de la caja (minimo WCAG: 4,5:1 para
texto, 3:1 para un boton):

| Color | Hex | Contraste | Sirve |
| --- | --- | --- | --- |
| Cian | `#00d4ff` | 1,77:1 | **no** |
| Verde | `#00e87b` | 1,64:1 | **no** |
| Naranja | `#ff7700` | 2,66:1 | **no** |
| Rosa | `#ff2ecb` | 3,23:1 | solo como forma, no con texto blanco encima |
| **Morado** | **`#7b2fff`** | **5,69:1** | **si** |

El cian es tu color principal en la tienda y **sobre blanco es ilegible**: un
boton cian con texto blanco da 1,77:1, cuando el minimo es 4,5:1. Ponerlo seria
cambiar una caja sosa por una caja rota.

**Usa el morado `#7b2fff`** como color de marca y de boton en la caja. Es el
unico de tu paleta que aguanta sobre blanco, y sigue siendo inequivocamente
tuyo.

- Color de marca / accent: `#7b2fff`
- Boton principal: fondo `#7b2fff`, texto blanco
- Enlaces: `#7b2fff`

### Paso 3 — Las esquinas

Tu tema usa **12 px** en los botones y **18 px** en las tarjetas. La caja por
defecto usa esquinas casi rectas. Igualarlo es barato y se nota:

- Esquinas de los botones: **12 px** (o el escalon mas cercano que ofrezca)
- Esquinas de los campos y las tarjetas: **12–18 px**

### Paso 4 — La tipografia

El tema usa **Assistant** para titulos y cuerpo. Si el editor te deja elegir una
fuente del catalogo de Shopify, pon **Assistant** en los dos sitios. Si no
aparece, deja la del sistema: una fuente mal elegida es peor que la neutra.

### Paso 5 — El fondo

**No pongas la caja en negro.** Es tentador y es un error:

- Los campos de tarjeta de los proveedores de pago se dibujan en claro y no
  siempre siguen tu tema. Acabas con campos blancos sobre negro, que es lo que
  de verdad parece roto.
- El comprador espera una caja clara. La familiaridad, en esa pantalla, vale
  mas que la coherencia estetica.

Lo que si funciona: fondo claro, **logotipo arriba**, morado como acento y las
esquinas iguales a las del tema. Si quieres mas marca, el editor permite una
**imagen de fondo lateral** en la columna del resumen — ahi si puede ir algo
oscuro y con neon, porque no hay campos encima.

### Paso 6 — Guardar y mirar en el movil

Guarda, y abre la caja **en tu telefono**, con un producto real en el carrito.
El editor ensena una simulacion; el telefono ensena la verdad.

---

## 4. Lo que hay que comprobar ANTES de gastar en anuncios

Por orden de cuanto dinero cuesta equivocarse.

### 4.1 Que los PDF se entregan de verdad — CRITICO

**No lo he podido comprobar**: el conector de productos digitales me responde
`Forbidden`. Y es el fallo mas caro posible, porque el cliente paga y no recibe
nada.

Como comprobarlo en diez minutos:

1. Crea un codigo de descuento del **100 %**, de un solo uso.
2. Compra tu propio **Pro · Definición + Volumen** con ese codigo, desde el
   movil y con un correo tuyo.
3. Mira que llegue el correo con el enlace de descarga, **abre el PDF** y
   comprueba que es el que debe ser.
4. Borra el codigo.

Hazlo con **uno de cada tipo**: un plan, un Códice y el Elite (que son once
documentos). Si uno falla, fallan todos los de su lote.

### 4.2 El pixel de Meta

**Tampoco lo puedo ver**: al conector le falta el permiso `read_pixels`. Sin
pixel no hay datos de conversion, la campana no aprende y el dinero se va sin
devolver nada. Comprueba en el panel que esta instalado y que dispara
`ViewContent`, `AddToCart` y `Purchase`.

### 4.3 La verificacion del dominio en Meta

El ajuste `seo_facebook_domain` del tema sigue **vacio**. Saca el codigo de Meta
Business Manager y pegalo ahi: la etiqueta sale sola, el tema ya esta cableado.

### 4.4 Los codigos de barras repetidos

Dos productos dan el **mismo** codigo a todas sus variantes: las bandas de
resistencia (`705353502002`, ocho variantes) y el entrenador respiratorio
(`313106953942`, dos). Los catalogos de Meta y Google marcan los GTIN repetidos
y pueden suprimir el producto entero.

### 4.5 El correo

Del 27 de septiembre: **sin SPF, sin DKIM**, DMARC en `p=none`, sin MX. Hoy no
lo puedo releer —este contenedor no tiene DNS de salida, falla hasta
google.com—, asi que si no lo has tocado, sigue igual y los correos de pedido y
de carrito abandonado van a spam.

### 4.6 El envio gratis

La tienda sigue regalando el envio a partir de 75 CAD en Canada y 100 CAD en
EE. UU., mientras la barra del tema esta apagada: pagas el envio y no ganas la
conversion. Sigue sin decidir.

---

## 5. Donde NO apuntar los anuncios

- **`/collections/cuidado-personal`**: cuenta dos productos y los dos estan
  ocultos. Al visitante le recibe una pagina vacia. El tema la saca del indice
  sola, pero un anuncio que apunte ahi es dinero tirado.
- Las fichas de **descarga digital** tienen **una sola imagen**. Para anuncios
  de catalogo funcionan, pero rinden mejor con tres o cuatro: portada, una
  pagina interior, una lamina.

---

## 6. Lo que no se ha hecho, y por que

- **Nada de lo de arriba**, porque pediste esperar tu senal.
- **El grafo de Mem0 no se ha actualizado**: el conector pide autorizacion y
  desde esta sesion no se puede dar. Se autoriza en los ajustes de conectores de
  claude.ai; hasta entonces, esa parte queda pendiente.
