# Auditoria de la tienda — 27 de septiembre de 2026

Lo que se reviso esta vez no es el tema, es **la tienda**: el catalogo, los
idiomas, los envios y el correo. El tema ya tiene su compuerta de 26 baterias;
esto de aqui no lo ve ninguna bateria porque no vive en el repositorio.

Abajo hay dos listas. La primera esta **hecha y comprobada**. La segunda solo
la puedes hacer tu, porque o toca el DNS del dominio o es una decision de
negocio que no me corresponde tomar.

---

## YA ESTA HECHO

### 1. El tema 4.74.0, subido y sin publicar

`villuminations-3d-4-74-0-PUBLICAR-ESTE`, 116 archivos, **cada md5 identico al
del zip**. El import se comio `templates/robots.txt.liquid` por decimosexta vez
y se reescribio aparte: md5 `a9af17ec030eb6a33306e2e03c6e7845`.

Compuerta: 26 baterias y 48 comprobaciones de fuente, todo en verde.

### 2. Se acaba la reparacion manual de cada publicacion

Los cuatro textos de marca (eslogan, eslogan de la intro, frases, titulo de la
venta cruzada) vivian en `settings_data.json`, y sus traducciones iban **por
tema**: cada publicacion perdia dieciseis. Ahora viven en los archivos de
idioma, que viajan dentro del zip.

Comprobado contra la tienda: esas cuatro claves **ya no existen** como contenido
traducible del tema. El detalle esta en `LEEME-publicar.md`.

### 3. Un suplemento se vendia sin limite

**Preentreno Nitric Shock · Ponche de frutas** estaba activo, es fisico (pide
envio) y tenia el inventario **sin seguimiento** con la politica en `CONTINUE`.
Los otros nueve suplementos estaban en `DENY`. Con cincuenta pedidos se habrian
vendido cincuenta unidades habiendo once.

Ahora: seguimiento activado, politica `DENY`, **11 unidades** en Supliful
Fulfillment. Ya no puede sobrevenderse.

### 4. El menu de la cuenta de cliente estaba en frances para todo el mundo

Sus dos entradas tenian el frances como **idioma base** —"Commandes" y
"Profil"— asi que un espanol, un ingles, un aleman y un japones leian frances.
Ahora el base es "Pedidos" y "Perfil", con sus cuatro traducciones.

### 5. El titulo y la descripcion SEO de la tienda solo existian en castellano

Es lo que ensena Google. Traducidos a los cuatro idiomas.

### 6. Las fichas de producto ensenaban datos crudos del proveedor

Es la pagina donde aterriza cualquier anuncio, y decia cosas asi:

| Antes | Ahora |
| --- | --- |
| `actual_color` (una clave interna, a la vista) | Color |
| `Select Color` | Modelo |
| `Style` con el valor `12 Inch` | Altura · 30 cm (12 pulgadas) |
| `Size` | Talla |
| `Winered`, `Rosered`, `Lightpurple`, `Darkblue` | Burdeos, Fucsia, Lila, Azul marino |
| `D. Black 15Lbs` | Negro · 6,8 kg (15 lb) |
| `X-Large`, `10 Lb` | XL, 4,5 kg (10 lb) |
| `8Pcs` / `16Pcs` | 8 piezas / 16 piezas |
| `1Pair Bottom Bracket` (dentro de un desplegable de Color) | Par de soportes de base |
| `Black Set`, `Purple 2Pcs` | Juego negro, Morado · 2 piezas |

**20 etiquetas y 45 valores** pasados al castellano y registrados en los otros
cuatro idiomas. Las opciones que siguen llamandose `Title` son el valor por
defecto de Shopify para los productos de una sola variante, y el tema no las
pinta nunca.

### 7. Filtros y nombres de envio, traducidos

Los filtros de coleccion y los nombres de los metodos de envio, registrados en
los idiomas que se podian (ver el punto C de abajo para lo que falta).

---

## LO QUE SOLO PUEDES HACER TU

### A. El correo se va a ir a spam — esto es lo mas urgente

Lo comprobado hoy en el DNS de `villuminations.com`:

| Registro | Estado |
| --- | --- |
| SPF | **no existe** |
| DKIM | **no existe** (probados nueve selectores) |
| DMARC | existe, pero es `v=DMARC1; p=none` a secas |
| MX | **no existe** — el dominio no puede recibir correo |

Desde febrero de 2024, Gmail y Yahoo **exigen** SPF + DKIM + DMARC a quien
envia correo en volumen. Sin esto, los correos de pedido, el de bienvenida y el
de carrito abandonado van a la carpeta de spam. Con dinero de anuncios detras,
esto es tirar el trafico que ya pagaste.

**Los cuatro registros CNAME que hay que pegar los genera Shopify y son
distintos para cada tienda: no me los puedo inventar.** Estan aqui:

`Parametres` → `Notifications` → seccion del correo del remitente →
`Authentifier`. Shopify ensena cuatro CNAME.

Esos cuatro CNAME llevan **DKIM y SPF a la vez**. No hace falta anadir un TXT
de SPF aparte, y no hay que meter `include:shops.shopify.com` salvo que Shopify
lo pida por pantalla.

Donde se pegan: el dominio esta en **Google Cloud DNS**
(`ns-cloud-b1..b4.googledomains.com`), asi que no es ninguno de los tres
proveedores que Shopify configura solo (Cloudflare, GoDaddy, IONOS). Van a mano.

**El DMARC hay que cambiarlo tu.** El que hay no protege nada y no manda
informes. Sustituyelo por este, en `_dmarc.villuminations.com`, tipo TXT:

    v=DMARC1; p=none; rua=mailto:TU-CORREO; adkim=r; aspf=r; pct=100

Tres avisos sobre esa linea:

1. `TU-CORREO` tiene que ser un buzon que **exista y funcione**. Ojo: el
   dominio no tiene registros MX, asi que `algo@villuminations.com` **no
   recibe nada**. Pon el correo que usas de verdad.
2. Tiene que haber **un solo** registro DMARC. Dos hacen que la comprobacion
   falle entera.
3. `adkim=r` y `aspf=r` a proposito: en modo estricto (`s`) la autenticacion
   por Shopify no cuadra.

Cuando lleven dos o tres semanas llegando informes limpios, sube a
`p=quarantine`, y mas adelante a `p=reject`.

### B. La tienda regala el envio y el cliente no se entera

Tu regla es que el envio gratis se queda **apagado**. En el tema lo esta: el
umbral esta vacio y la barra de progreso no se pinta. **En la tienda no.**

| Perfil | Zona | Tarifa | Condicion |
| --- | --- | --- | --- |
| Profil general | Domestic (Canada) | `Standard` a **0,00 CAD** | total ≥ 75 CAD |
| Profil general | US Cross-border | `Standard International` a **0,00 CAD** | total ≥ 100 CAD |
| AutoDS Free Shipping | Rest of World | `Free Shipping` a **0,00 CAD** | ninguna |

Es lo peor de las dos opciones: pagas el envio y no ganas ni una conversion,
porque nada en la tienda dice que a partir de 75 $ sale gratis.

Hay dos salidas coherentes. **Elige una:**

- **Apagarlo de verdad.** `Parametres` → `Livraison` → borra esas tres tarifas
  a cero. Es tu regla escrita.
- **Aprovecharlo.** Dejalas y enciende la barra: editor del tema → `Carrito` →
  `Umbral de envio gratis` → `75`. Entonces el carrito dice cuanto falta, y eso
  sube el importe medio del pedido.

Y una cosa mas que conviene mirar: el perfil `Productos supliful` tiene **dos
grupos de ubicacion cubriendo los mismos paises** con precios distintos (14,99
frente a 15,99 CAD en internacional; 6,99 CAD frente a 5,99 USD en EE. UU. y
Mexico). Segun desde donde salga el pedido, el cliente paga una cosa u otra.

### C. Los nombres de envio estan en ingles siendo el castellano el idioma base

Shopify no deja traducir al idioma base: hay que **renombrarlos**. En
`Parametres` → `Livraison`, perfil general:

| Ahora | Ponle |
| --- | --- |
| Standard | Envio estandar |
| Express | Envio urgente |
| Standard International | Internacional estandar |
| Express International | Internacional urgente |

**Avisame cuando los renombres** y registro otra vez el frances, el aleman y el
japones: Shopify calcula su huella sobre el texto en castellano, asi que al
cambiarlo las traducciones de ahora se quedan colgadas.

Las de Printful (`US Flat Rate`, `EU Flat Rate`, `Worldwide Flat Rate`…) son de
la aplicacion. Se pueden renombrar, pero la proxima sincronizacion puede
deshacerlo.

### D. Los filtros de coleccion salen en frances

`Disponibilité` y `Prix`. No es un fallo del tema: Shopify guarda la etiqueta
del filtro en el idioma **del panel**, y tu panel esta en frances. Al no ser el
castellano, no se puede traducir con la API.

Arreglo: `Applications` → `Search & Discovery` → `Filtres` → renombra a
`Disponibilidad` y `Precio`. El ingles, el aleman y el japones ya estan puestos.

### E. El titulo SEO de la tienda dice «Illumina tu bienestar!»

En castellano es «Ilumina», con una sola L. Si es un juego a proposito con
VILLUMINATIONS, dejalo tal cual y no se toca. Si no lo es, se cambia en
`Parametres` → `Boutique` → SEO. No lo he tocado porque no me toca decidir
como se escribe tu marca.

### F. Pendientes de antes, por si los quieres cerrar ya

- Los codigos de verificacion de Bing, Yandex y Pinterest, si los quieres en
  `theme.liquid` junto al de Google (que sigue en su sitio).
- Shopify Email con la automatizacion de bienvenida y la de carrito abandonado.
  **Esto depende del punto A:** montarlas antes de autenticar el dominio es
  mandar correo directo a spam.

---

## Lo que se comprobo y estaba bien

- Las **seis politicas**: ni un marcador, ni una plantilla sin sustituir, la
  direccion completa, las 25 secciones de las condiciones en orden, y ni rastro
  de la plataforma europea de resolucion de litigios (cerrada el 20 de julio de
  2025). La compuerta `politicas/comprobar.mjs` en verde.
- El cupon `BIENVENIDO10`: **activo**, y coincide con el que reparte el pie.
- Los nueve suplementos restantes: `DENY` con existencias reales.
- Los dos jabones: `UNLISTED`, asi que no se pueden comprar sin existencias.
- Los libros y planes en PDF: sin seguimiento de inventario a proposito, que es
  lo correcto para un producto digital.
- Colecciones, paginas, blog y politicas: traducidos a los cinco idiomas.
- La pagina VI.P: el titulo es «VI.P» en los cinco idiomas porque es el nombre
  de la marca, no un texto por traducir. Correcto tal cual.
- Los enlaces del menu del pie: los once, traducidos.
