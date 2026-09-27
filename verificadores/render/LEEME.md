# Renderizado real del Liquid

Los 28 verificadores de `check.mjs` **leen** el codigo. Este lo **ejecuta**, con
un motor de Liquid de verdad (liquidjs) y datos que imitan la tienda: cinco
idiomas publicados, un producto con valoraciones, una coleccion, un articulo.

Es la diferencia entre "el archivo parece correcto" y "Google recibe un JSON
que puede parsear". Una coma de mas en una rama que solo se pinta en las fichas
de blog no la ve ningun analisis estatico, y rompe el bloque entero para el
rastreador.

## Uso

    node verificadores/render/jsonld.mjs

Entra en la compuerta (`node empaquetar.mjs`), asi que normalmente no hay que
correrlo a mano. Durante meses NO entraba: se corria a mano o no se corria, y
no por falta de dependencias -- liquidjs ya estaba fijada en package.json. Fue
un olvido. Se noto al unificar el nombre de la marca, porque tres de los campos
que se tocaron son justo los que leen Google y los sistemas de IA.

Recorre nueve tipos de pagina (index, product, collection, article, blog, page,
search, 404, cart) en tres escenarios: precio unico, precio variable
(AggregateOffer) y **la configuracion que de verdad se envia**, con el correo y
el telefono de contacto vacios. Ese tercero faltaba: las dos pasadas anteriores
renderizaban el contacto relleno, asi que la forma en que el tema sale de
fabrica no se probaba nunca.

De cada bloque hace JSON.parse y ademas mira lo que dice dentro:

  - `name`, `url`, `@type` y `@id` no pueden ir en null ni vacios. Es el fallo
    que `{{ marca | json }}` deja a un descuido de distancia: con la variable
    vacia escribe `null`, que es JSON impecable y le dice a Google que la
    marca no se llama de ninguna manera.
  - El correo de la administracion no puede aparecer en ningun campo. Hoy no
    hay via para que llegue -- el bloque de contacto solo se pinta si el
    comerciante rellena el ajuste a mano, y va vacio de fabrica -- pero es la
    clase de respaldo "util" que alguien anade con la mejor intencion.

Sale con codigo 1 si algun bloque no es JSON valido o si le falta contenido.

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
