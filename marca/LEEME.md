# Archivos de marca — VILLUMINATION

Generados a partir del propio distintivo del tema (`snippets/logo-mark.liquid`),
con tus colores exactos: cian `#00d4ff`, violeta `#7b2fff`, rosa `#ff2ecb`,
fondo `#05050f`. La "VI" va en cian porque es el color con el que se reconoce
la marca en el resto de la tienda; el aro recorre el espectro completo.

## Dónde va cada archivo

| Archivo | Dónde | Por qué |
|---|---|---|
| `villumination-logo-ancho.png` (1600×400, fondo transparente) | Parámetros del tema → **Logo y marca → Logo** | Es el que sale en la cabecera. Transparente para que funcione sobre la barra oscura. |
| `villumination-favicon-512.png` (512×512) | Parámetros del tema → **Logo y marca → Favicon** | Google **ignora los favicons menores de 48×48**. A 512 tienes margen para todos los tamaños que el tema genera (48, 96, 192 y 180 para iOS). |
| `villumination-logo-512.png` (512×512) | Shopify → Configuración → **Datos de la tienda → Logo** | De aquí sale el logo de marca en los resultados de Google (propiedad `logo` del JSON-LD). |
| `villumination-logo-ancho-fondo.png` (1600×400, fondo oscuro) | Redes sociales, cabeceras de correo | Para sitios que no admiten transparencia. |
| `villumination-logo.svg` / `villumination-logo-ancho.svg` | Archivo maestro | Vectorial: escala a cualquier tamaño sin perder nitidez. Úsalo si algún día necesitas otra medida. |

## Imagen para compartir

El ajuste **Logo y marca → Imagen para compartir** es nuevo en la 4.13.0 y va
aparte: es la tarjeta que sale al pegar el enlace de la tienda en WhatsApp,
Facebook o X. Necesita **1200×630 px** (formato apaisado) y conviene que sea
una foto real de producto o de la marca, no el logo: un cuadrado recortado a
1200×630 se ve mal. Si la dejas vacía, el tema usa el logo como respaldo.

## Nota sobre los tamaños

El tema recorta el favicon con `crop: 'center'`, así que la marca queda
centrada en todos los tamaños. El logo de cabecera se sirve con `width: 240`
y la altura la controlas con **Altura del logo** (44 px por defecto).
