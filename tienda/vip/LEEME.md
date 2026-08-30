# VI.P — el cuerpo limpio, para pegar en el panel

`VI-P-limpia.html` es el cuerpo de la página **VI.P** tal como está en la
tienda, menos cinco etiquetas que dentro del cuerpo de una página de Shopify
son inválidas o dañinas. Nada más: **no se ha tocado una sola línea de la
aplicación** —los cinco bloques de script y el de estilo siguen intactos.

Qué se quitó, y por qué:

| Etiqueta | Veces | Por qué sobra |
|---|---|---|
| `<body>` | 2 | el documento ya tiene uno; repetirlo es HTML inválido |
| `<title>` | 1 | el título lo pone Shopify, y este lo pisaba |
| `<meta charset>` | 1 | ya declarado en la cabecera del tema |
| `<meta name="viewport">` | 1 | **lleva `maximum-scale=1.0`** |

La del viewport es la que hace daño: `maximum-scale=1.0` **impide ampliar con
los dedos**. Quien no ve bien no puede acercar el texto, las auditorías de
accesibilidad lo penalizan, y encima duplicaba la etiqueta que el tema ya
emite.

## Por qué está aquí en vez de publicado

`pageUpdate` exige mandar el cuerpo entero y son **437 KB**: no caben en una
llamada del conector. Se pega desde Contenido → Páginas → VI.P, en el editor
de código (`<>`), reemplazando todo.

`python3 tienda/vip.py fichero.html` vuelve a medirlo cuando haga falta, y
`--limpiar` regenera esto.

## Lo que este fichero NO arregla

- **337 KB de JavaScript en línea** y 53 de CSS. Eso no se aligera limpiando:
  se mueve a los recursos del tema, donde el navegador lo guarda en caché
  entre visitas en vez de volver a bajarlo dentro del HTML cada vez.
- **Cinco recursos de un CDN externo** (TensorFlow, Three.js, Chart.js).
- **32 GIF animados**, que pesan más que un vídeo corto y no se pueden pausar.

Las tres cosas son mudanzas de tema, no limpieza de cuerpo, y piden probarse
en la tienda. Es trabajo para la sesión del tema.
