# Renderizado real del Liquid

Los 28 verificadores de `check.mjs` **leen** el codigo. Este lo **ejecuta**, con
un motor de Liquid de verdad (liquidjs) y datos que imitan la tienda: cinco
idiomas publicados, un producto con valoraciones, una coleccion, un articulo.

Es la diferencia entre "el archivo parece correcto" y "Google recibe un JSON
que puede parsear". Una coma de mas en una rama que solo se pinta en las fichas
de blog no la ve ningun analisis estatico, y rompe el bloque entero para el
rastreador.

## Uso

    npm install liquidjs --no-save
    node verificadores/render/jsonld.mjs

Recorre nueve tipos de pagina (index, product, collection, article, blog, page,
search, 404, cart), renderiza los datos estructurados de cada uno y hace
JSON.parse de cada bloque. Sale con codigo 1 si alguno no es JSON valido.

## Comprobado que salta

Al meter una coma de mas antes del cierre de OnlineStore, el verificador la
caza en los nueve tipos y dice la posicion exacta. Al deshacerlo, vuelve a
verde. Un verificador que nunca falla no sirve de nada.

## Limite conocido

Los filtros de Shopify se registran a mano al principio del script. Con
`strictFilters: false`, uno que falte devuelve el valor sin tocar en vez de
romper la prueba: eso puede dar un valor raro (un precio a 0, por ejemplo) que
NO es un fallo del tema sino de los datos de prueba. Antes de dar por bueno un
valor extrano, hay que mirar el Liquid original.
