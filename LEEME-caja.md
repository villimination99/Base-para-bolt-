# La caja y la pantalla de acceso, en oscuro

Guia viva: https://claude.ai/code/artifact/d8110dcf-267b-4fdb-81bd-e082cc122332

Escrito el 11 de octubre de 2026. Una version anterior de este archivo
recomendaba dejar la caja en claro con el morado de acento. **Era peor
consejo**, y los numeros lo dicen: en oscuro la paleta de la tienda funciona
entera y en blanco no funciona casi nada. Lo que sigue es la version buena.

---

## Un editor, dos pantallas

Shopify unifico la caja y las cuentas de cliente en una sola configuracion, con
una seccion de acceso que es exactamente `account.villuminations.com`. Lo que se
configura una vez sale en las dos.

Comprobado por API sobre el perfil publicado («Configuration 2 de
Villuminations»): `designSystem` y `customizations` estan los dos a **null**.
Cero personalizacion, sin editar desde el 23 de septiembre. Por eso la caja
ensena «Villuminations» en texto negro del sistema en vez del logotipo, con el
azul por defecto.

## Por que no se puede hacer por API

Las dos razones estan comprobadas en la documentacion, no supuestas:

- El API antiguo (`checkoutBranding`) **exige plan Plus** y la tienda esta en
  Basic. Ademas esta marcado como obsoleto.
- El API nuevo (`checkoutAndAccountsConfigurations`) **no exige Plus**, solo
  permisos, pero el conector esta fijado a la version `2026-01` del Admin API,
  donde ese campo todavia no existe.

Se hace a mano en el editor, que si entra en el plan Basic.

## El dato que decide: contraste

Contraste de la paleta de la tienda sobre la superficie de marca `#0b0b1e`,
comparado con el blanco que hay ahora. El minimo para texto es 4,5:1.

| Color | Sobre oscuro | Sobre blanco |
| --- | --- | --- |
| Cian `#00d4ff` | **10,97:1** | 1,77:1 |
| Verde `#00e87b` | **11,87:1** | 1,64:1 |
| Naranja `#ff7700` | **7,30:1** | 2,66:1 |
| Rosa `#ff2ecb` | **6,02:1** | 3,23:1 |
| Morado `#7b2fff` | 3,42:1 | 5,69:1 |
| Texto `#d8f6ff` | **17,16:1** | — |

En blanco solo aguantaba el morado. En oscuro aguanta todo **menos** el morado,
incluido el cian, que es el color principal de la marca. El morado pasa a servir
para bordes y detalles, no para texto.

Boton solido cian con texto negro: **11,86:1**. Es el mismo lenguaje de boton
que ya usa la tienda.

## Los valores

| Donde | Valor |
| --- | --- |
| Fondo de la pagina | `#0b0b1e` |
| Fondo de bloques y campos | `#121228` |
| Texto | `#d8f6ff` |
| Bordes y separadores | `#23234a` |
| Boton principal | fondo `#00d4ff`, texto `#000000` |
| Enlaces y acentos | `#00d4ff` |
| Esquinas de botones | 12 px |
| Esquinas de campos y tarjetas | 12–18 px |
| Tipografia | Assistant |

### No usar negro puro

Los campos de la tarjeta los dibujan los proveedores de pago y no siempre siguen
el tema. Sobre negro puro, un campo que no obedezca canta como un recuadro
blanco. Con `#0b0b1e` el salto es mucho menor, y ademas es el color de
superficie que ya usa la tienda. Hay que comprobarlo en el movil antes de darlo
por bueno.

### El logotipo cambia con el fondo

| Archivo | Para la caja oscura |
| --- | --- |
| `villuminations-logo-ancho.png` | **Este.** Transparente, dibujado para fondo negro. |
| `villuminations-logo-ancho-fondo.png` | No. Lleva fondo claro incorporado. |

## Los pasos

Ruta: `Configuracion` → `Pago` → `Personalizar`. En el panel, que esta en
frances: `Paramètres` → `Paiement` → `Personnaliser`.

1. **Duplica la configuracion publicada** y trabaja sobre la copia. Asi se
   prueba sin que nadie vea un estado a medias.
2. **Fondos**: pagina `#0b0b1e`, bloques y campos `#121228`, bordes `#23234a`.
3. **Texto**: `#d8f6ff`.
4. **Boton y enlaces**: boton con fondo `#00d4ff` y texto `#000000`; enlaces en
   `#00d4ff`.
5. **Logotipo**: `villuminations-logo-ancho.png`, ancho inicial 160 px.
6. **Esquinas y tipografia**: 12 px en botones, 12–18 px en campos, Assistant si
   aparece en el catalogo del editor.
7. **Imagen de fondo lateral** en la columna del resumen, si se quiere mas
   marca. Sin texto dentro de la imagen.
8. **Pruebalo en el movil** con un producto real, hasta la pantalla de la
   tarjeta. Si los campos del numero salen en blanco, sube el fondo de toda la
   pagina a `#121228` y vuelve a mirar.
9. **Publica** y entra en `account.villuminations.com`: tiene que haber cambiado
   sola.

---

## Antes de encender los anuncios

Por orden de cuanto cuesta equivocarse. Los tres primeros no se alcanzan desde
esta sesion.

1. **Que los PDF se entregan.** El conector de productos digitales responde
   `Forbidden`, asi que no se ha podido comprobar, y es el fallo mas caro
   posible: el cliente paga y no recibe nada. Crea un descuento del 100 %,
   comprate un plan, un Codice y el Elite, y abre los archivos que lleguen.
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
