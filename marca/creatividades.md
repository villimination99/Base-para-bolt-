# Creatividades para anuncios — VILLUMINATIONS

Qué se puede generar, con qué medidas, y qué tiene que cumplir una pieza antes
de subirla a Meta. Los datos de modelos salen del catálogo de
[open-higgsfield](https://github.com/wide-trace/open-higgsfield) (commit
`b16a0ef`), extraído y verificado, no copiado a ojo.

## Las tres reglas

**1. Ninguna imagen lleva texto.** Una imagen de Shopify o de un anuncio es
**una sola para los cinco idiomas**, y el texto no se traduce. Es la lección
que ya obligó a rehacer las portadas del Diario, las de colección y la tarjeta
para compartir. El copy va en el anuncio, que Meta sí sirve por idioma; la
imagen lleva luz, producto y marca, que se leen igual en los cinco.

Si alguna pieza necesita texto quemado, se generan **cinco versiones** y cinco
conjuntos de anuncios. No hay atajo.

**2. Una pieza tiene que sobrevivir a los tres recortes.** Meta sirve el mismo
archivo en sitios que lo recortan distinto:

| Sitio | Proporción |
|---|---|
| Feed cuadrado | 1:1 |
| Feed vertical (el que más pantalla ocupa, y el que más rinde) | 4:5 |
| Stories y Reels | 9:16 |

**3. Se comprueba, no se supone.** `node marca/comprobar-creatividad.mjs <imagen>`
mide la tinta píxel a píxel dentro de la intersección de los tres recortes y
sale con error si el sujeto se corta. Ver abajo por qué hizo falta.

## 4:5 no lo genera ningún modelo

De los 38 modelos del catálogo, **34 hacen 1:1, 9:16 y 16:9. Ninguno hace 4:5.**
Las proporciones que existen en todo el catálogo son: `1:1 2:3 3:2 3:4 4:3 9:16
16:9 21:9 auto`.

Así que 4:5 sale **por recorte, sí o sí**. Lo práctico es generar en 9:16
(1080×1920, la más alta) y recortar hacia abajo: 4:5 conserva `y 285..1635`,
1:1 conserva `y 420..1500`. La intersección —y por tanto la caja segura— es
**y 420..1500: el 56 % central de la altura**. Fuera de ahí solo va fondo.

El recorte cuadrado es el que manda, porque es el más alto de los tres.

## Los modelos que sirven

### Imagen (8)

| Modelo | id | Proporciones | Resolución | Entradas |
|---|---|---|---|---|
| Soul 2 | `soul-2` | 9:16 16:9 4:3 3:4 1:1 2:3 3:2 | 720p / 1080p | solo texto |
| Soul Cinema | `soul-cinema` | 9:16 16:9 4:3 3:4 1:1 2:3 3:2 | 720p / 1080p | solo texto |
| Flux 2 | `flux-2` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |
| Grok Imagine 2.0 | `grok-imagine-2` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |
| Ideogram 4.0 | `ideogram-4` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |
| Recraft 4.1 | `recraft-4.1` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |
| Qwen Image 3 | `qwen-image-3` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |
| Z-Image Turbo | `z-image-turbo` | auto 1:1 4:3 3:4 16:9 9:16 | 1k / 2k / 4k | hasta 8 referencias |

Los seis que aceptan **referencias** son los que sirven para producto: se les
pasa la foto real del bote o de la camiseta y generan la escena alrededor, en
vez de inventarse el producto. Para anuncios de catálogo es la diferencia entre
una imagen bonita y una que enseña lo que vendes.

### Vídeo con imagen de inicio (los útiles para producto)

Todos aceptan una imagen de arranque, así que se puede partir de una foto real.

| Familia | Proporciones | Duración | Notas |
|---|---|---|---|
| Seedance 2.5 / 2.0 | 16:9 4:3 1:1 3:4 9:16 21:9 | 4–30 s (2.5) · 4–15 s (2.0) | inicio + fin, hasta 30 referencias, audio. 2.0 llega a 4k |
| Kling 3.0 (Turbo/Std/Pro/4K) | 16:9 9:16 1:1 | 3–15 s | Pro y 4K aceptan fin |
| Wan 3.0 / 3.0 Prime / 2.7 / 2.6 | 16:9 9:16 1:1 | 4–10 s | 720p / 1080p |
| Kling 2.6 / 2.5 / O1 / O3 | 16:9 9:16 1:1 | 4–10 s | O1 y O3 aceptan fin |
| LTX 2.5 Fast / Pro | 16:9 9:16 1:1 | 4–10 s | |
| MiniMax H3 / Hailuo 2.3 | 16:9 9:16 1:1 | 4–10 s | |
| PixVerse 6, Flux 3, DoP, Happy Horse 1/1.1 | 16:9 9:16 1:1 | 4–10 s | |
| Kling 3.0 Motion Control | — | — | copia el movimiento de un vídeo de referencia |

Para Stories y Reels, **9:16 y 6–10 s**. Lo primero que se ve tiene que estar en
el primer segundo: en Reels la mayoría se va antes del segundo tres.

## Por qué existe el comprobador

`marca/comprobar-creatividad.mjs` mide la tinta dentro de la intersección de los
tres recortes, en **los dos ejes**, y falla si el sujeto se sale.

Hizo falta dos veces. Las portadas del Diario se rindieron con la marca al 7 %
del borde, dentro de la zona que la tarjeta recorta, y en un móvil se leía
«ILLUMINATION» y el título sin su primera letra: lo vio el cliente en una
captura, no ningún detector. Después las portadas de colección volvieron a
fallar igual, porque el generador medía **uno** de los **dos** recortes que
sufren: las seis pasaban por estar centradas, no por estar comprobadas.

Y una tercera, aquí mismo: la primera versión de este guion solo modelaba el
recorte vertical, y con una pieza apaisada daba 100 % en los tres sitios —
porque no quitaba nada **por el eje equivocado**. Meta la habría recortado por
los lados. El mismo fallo, en la herramienta hecha para evitarlo.

Medido sobre lo que ya existe:

| Pieza | Sobrevive a 9:16 | Veredicto |
|---|---|---|
| Distintivo cuadrado 512×512 | 69,7 % | sirve |
| Tarjeta para compartir 1200×630 | 34,4 % | no sirve de anuncio |
| Logotipo ancho 1600×400 | 12,1 % | no sirve de anuncio |

**Lo que NO comprueba:** si hay texto. Detectar letras sin OCR no es fiable, y
una comprobación que a veces acierta es peor que ninguna, porque se confía en
ella. La regla del texto se cumple en el prompt.
