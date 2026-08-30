# Secuencia de marca en video

Genera un video vertical 9:16 con la identidad de la tienda, listo para la
sección **Video 3D interactivo** y también para Reels, Shorts y TikTok.

```bash
node estudio/video/renderizar.mjs                 # 1080x1920 a 30 fps
node estudio/video/renderizar.mjs --ancho 720     # más ligero
```

Sale `estudio/video/villumination-marca.webm`: **16 s, 1080×1920, 2,4 MB**.
Esa es la resolución exacta de Reels, Shorts y TikTok, así que sirve igual
para la tienda que para redes. Tarda unos 90 segundos.

## Por qué WebM y no MP4

El único ffmpeg de este entorno es el que trae Playwright, compilado con
`--disable-everything`. Lleva el codificador `libvpx` (VP8) y el contenedor
`webm`, y nada más: **no hay H.264 ni contenedor MP4**. Se comprobó
ejecutándolo, no se supuso.

Shopify solo admite `.mp4` y `.mov` en el selector de video de la sección.
Hay dos caminos, los dos válidos:

**1. Convertir en el Mac** (recomendado, y el archivo pesa menos)

```bash
ffmpeg -i villumination-marca.webm -c:v libx264 -crf 20 -pix_fmt yuv420p \
       -movflags +faststart villumination-marca.mp4
```

Sin ffmpeg instalado: `brew install ffmpeg`. También sirve abrirlo con
QuickTime o VLC y exportar, pero la orden da mejor calidad por peso.
Después: Contenido → Archivos → Subir, y elegirlo en **Video subido a
Shopify** dentro de la sección.

**2. Subir el WebM tal cual**

Contenido → Archivos acepta el `.webm` como archivo suelto. Copia su URL y
pégala en el ajuste **"O la URL directa de un archivo de video"** de la
sección. Funciona en Chrome, Firefox, Edge y Safari 14.1 o más nuevo.
Como no todos los Safari antiguos leen VP8, para la portada conviene
rellenar también el campo de imagen.

## Cómo está hecho

`escena.html` es la escenografía y `guion.js` la animación. Todo depende de
una sola variable de tiempo (`window.__pintar(t)`) que **fija el
renderizador**, no el navegador: sin `requestAnimationFrame` ni `Date.now()`.
Por eso dos ejecuciones dan exactamente el mismo video, aunque la máquina vaya
más lenta. Un video grabado con el reloj del navegador saldría distinto cada
vez y con fotogramas saltados.

Abrir `escena.html` en el navegador reproduce la secuencia en bucle para
revisarla a ojo; en ese caso sí usa su propio reloj.

La tipografía Orbitron va incrustada en `fuente.b64` porque este entorno no
llega a Google Fonts y el video tiene que salir con la letra de la tienda, no
con una sustituta del sistema.

## Las cinco escenas (16 s)

| Desde | Hasta | Qué pasa |
|------:|------:|----------|
| 0,0 s | 2,9 s | El marco de neón se dibuja y **VILLUMINATION** cierra su interletrado |
| 3,0 s | 5,6 s | **NO TE CONFORMES** |
| 5,7 s | 9,2 s | Los tres pilares entran en cascada: fuerza, nutrición, constancia |
| 9,3 s | 11,6 s | La cifra sube hasta **37**, los productos que hay activos en la tienda |
| 11,7 s | 15,9 s | Cierre: el logo VI, el dominio y la llamada a la acción |

El cierre se lleva cuatro segundos largos a propósito: es el momento en que
alguien decide entrar, y con dos y medio no daba tiempo a leer el dominio.
Se desvanece **por completo** antes del segundo 16, para que al reiniciarse
el bucle enganche con el negro del primer fotograma en vez de dar un salto.

El fondo son los mismos haces y el mismo marco pulsante que el hero de la
tienda: quien vea el video en Instagram y luego entre en la web reconoce la
marca al instante.

## Cambiar el contenido

Los textos están en `guion.js`, arriba del todo: la lista `PILARES`, el
`lema` y el `37` de la cifra. Si cambia el catálogo, actualiza ese número —
una cifra que no cuadra con lo que hay en la tienda resta credibilidad en vez
de sumarla.
