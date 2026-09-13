# Verificador de desbordamientos

Los 28 verificadores de `check.mjs` leen el codigo. Ninguno puede ver que un
texto se salga de su caja: eso solo se sabe midiendo en un navegador de
verdad. De ahi salieron dos fallos que llegaron hasta la tienda:

- La tira de cifras del banner VIP se salia 34 px del marco en un iPhone.
- El titulo de la tarjeta de producto se quedaba en una linea y se cortaba.

## Como se usa

Necesita Playwright y el Chromium del entorno (no van en el repositorio):

    npm install playwright --no-save
    node verificadores/desbordes/comprobar.mjs

Las paginas `componentes.html` y `vip.html` llevan el CSS del tema y el
contenido REAL de la tienda, con los nombres largos de verdad. No sirve
probar con "Lorem ipsum": el fallo aparece justo con las palabras largas.
