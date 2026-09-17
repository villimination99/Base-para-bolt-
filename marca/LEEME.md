# Archivos de marca — VILLUMINATIONS

Generados a partir del propio distintivo del tema (`snippets/logo-mark.liquid`),
con tus colores exactos: cian `#00d4ff`, violeta `#7b2fff`, rosa `#ff2ecb`,
fondo `#05050f`. La "VI" va en cian porque es el color con el que se reconoce
la marca en el resto de la tienda; el aro recorre el espectro completo.

## Dónde va cada archivo

| Archivo | Dónde | Por qué |
|---|---|---|
| `villuminations-logo-ancho.png` (1600×400, fondo transparente) | Parámetros del tema → **Logo y marca → Logo** | Es el que sale en la cabecera. Transparente para que funcione sobre la barra oscura. |
| `villumination-favicon-512.png` (512×512) | Parámetros del tema → **Logo y marca → Favicon** | Google **ignora los favicons menores de 48×48**. A 512 tienes margen para todos los tamaños que el tema genera (48, 96, 192 y 180 para iOS). |
| `villumination-logo-512.png` (512×512) | Shopify → Configuración → **Datos de la tienda → Logo** | De aquí sale el logo de marca en los resultados de Google (propiedad `logo` del JSON-LD). |
| `villuminations-logo-ancho-fondo.png` (1600×400, fondo oscuro) | Redes sociales, cabeceras de correo | Para sitios que no admiten transparencia. |
| `villumination-logo.svg` / `villuminations-logo-ancho.svg` | Archivo maestro | Vectorial: escala a cualquier tamaño sin perder nitidez. Úsalo si algún día necesitas otra medida. |

## Imagen para compartir

`villuminations-compartir.png` (1200×630) va en **Logo y marca → Imagen para
compartir**: es la tarjeta que sale al pegar el enlace de la tienda en
WhatsApp, Facebook o X. Si la dejas vacía, el tema usa el logo de respaldo.

**La anterior tenía texto en castellano horneado dentro** —«Equipo, ropa y
suplementos para quienes entrenan en serio»— y una imagen de Shopify es UNA
sola para las cinco lenguas: no hay versión francesa del archivo. Así que
cada vez que alguien pegaba el enlace desde Francia, Alemania o Japón, la
tarjeta le hablaba en castellano. Es la misma lección que ya obligó a rehacer
las portadas del Diario y las de colección: **lo que no se puede traducir no
se escribe en una imagen.**

La nueva no lleva ni una frase traducible. Solo el distintivo, el nombre
—que es un nombre propio— y el dominio, que se lee igual en los cinco
idiomas. Lo que distingue la tarjeta es la luz, no las palabras.

## Cómo se regeneran

`node marca/generar-logotipos.mjs` rehace el logotipo ancho, su variante con
fondo y la tarjeta para compartir. **No se ajustan a ojo:** el guion prueba
tamaños de letra, rinde, cuenta la tinta píxel a píxel y se queda con el mayor
que respeta el margen del diseño; si nada cabe, no escribe nada y sale con
error. El centrado también se mide, porque el resplandor se sale por los dos
lados y no por igual.

Eso hizo falta el día que el nombre pasó de VILLUMINATION a VILLUMINATIONS:
el texto anterior estaba ajustado al milímetro y su tinta terminaba en el
píxel 1540 de un lienzo de 1600. Una letra más se salía del lienzo.

De paso salió otra cosa: **el logotipo que estaba en la tienda no se había
rendido nunca en Orbitron.** El SVG maestro la pedía, pero quien lo rindió no
tenía la fuente instalada y el navegador cayó en la de respaldo sin avisar.
Por eso ahora la Orbitron va incrustada dentro del SVG como data URI. El
logotipo nuevo sí está en la tipografía de la marca, la misma que usa el
resto de la tienda.

## Nota sobre los tamaños

El tema recorta el favicon con `crop: 'center'`, así que la marca queda
centrada en todos los tamaños. El logo de cabecera se sirve con `width: 240`
y la altura la controlas con **Altura del logo** (44 px por defecto).
