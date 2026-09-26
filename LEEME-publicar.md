# Publicar un tema: la cosa que Shopify rompe

Cada vez que se publica una copia nueva del tema hay que reparar **una** cosa a
mano. No es un fallo del tema: es como funciona Shopify.

Hasta la version 4.73.0 eran dos. La segunda —las dieciseis traducciones de
ajustes que se perdian en cada publicacion— ya no existe: desde la 4.74.0 esos
textos viven en los archivos de idioma del tema, que viajan dentro del zip. El
apartado 2 queda abajo como historia, para saber por que ya no hay que hacerlo.

## 1. El zip se come `templates/robots.txt.liquid`

Confirmado **16 veces**, la ultima con el tema 4.74.0. El import de un zip
descarta ese archivo en silencio: no hay aviso, no hay error, el tema queda
con 115 archivos en vez de 116 y la
tienda pasa a servir el robots.txt por defecto de Shopify, sin los permisos
explicitos a los rastreadores de IA.

`themeCreate` desde una subida preparada (staged upload) **tampoco lo salva**:
es el mismo import por dentro.

La unica via que funciona:

1. Crear el tema (por zip o por `themeCreate`).
2. Esperar a que `processing` sea `false`.
3. Escribirlo aparte con `themeFilesUpsert` y `body: { type: BASE64, value: ... }`.
   Con `type: URL` la mutacion responde que todo fue bien y **no escribe nada**.
4. Comprobar el md5. El correcto es `a9af17ec030eb6a33306e2e03c6e7845`.

## 2. Las traducciones de los ajustes NO se heredan — RESUELTO en 4.74.0

**Este paso ya no hay que darlo.** Se deja escrito porque explica por que el
tema esta montado como esta, y para que nadie lo deshaga sin saberlo.

Las traducciones en Shopify van **por tema**. Al publicar una copia nueva, los
textos que el comerciante escribio en el editor volvian al idioma base
—espanol— para todos los demas idiomas, aunque el tema nuevo fuera identico.
Paso de verdad con el tema 4.72.0: se perdieron dieciseis traducciones y hubo
que recuperarlas una a una del tema viejo.

Los textos de los archivos `locales/*.json` viajan dentro del zip y no se
pierden. Lo que se perdia eran los valores de `config/settings_data.json` que
Shopify expone como contenido traducible. Eran **cuatro**:

| Ajuste | Donde vive ahora |
| --- | --- |
| `brand_tagline` | `inicio.marca.tienda.lema` |
| `splash_tagline` | `inicio.marca.intro.lema` |
| `splash_frases` | `inicio.marca.intro.frases` |
| `cart_cross_sell_title` | `inicio.marca.carrito.cruzada` |

Los cuatro ajustes **siguen existiendo en el editor, y vacios**. Los pinta
`snippets/copia.liquid`: si el comerciante escribe algo, manda lo suyo; si el
campo esta vacio —que es como viaja el tema— manda el idioma del visitante.
Asi que la copia viaja dentro del zip y no se pierde en ninguna publicacion.

Dos cosas que NO hay que hacer:

- **No poner un `default` a esos cuatro ajustes en `settings_schema.json`.**
  Shopify aplica el default a todo ajuste que el tema no guarda, y el default
  se escribe en un solo idioma: volveria a salir castellano en las cinco
  lenguas. Ademas, un `"default": ""` hace que Shopify **descarte el archivo
  entero** al importar el zip, sin avisar.
- **No volver a meterlos en `marca/ajustes-de-texto.json`.** Ese manifiesto es
  para lo que se teclea en el editor. La copia de marca se edita en
  `marca/copia-portada.json` y se regenera con `node marca/generar-copia.mjs`.

## Lo que NO se pierde

- Las politicas de la tienda y sus traducciones: son de la tienda, no del tema.
- `config/settings_data.json`: viaja en el zip. El codigo de Google
  (`seo_google_verification`), el logotipo, el favicon y la imagen de compartir
  sobreviven.
- Los archivos `locales/*.json` con las 353 claves de cada idioma.

## Comprobacion final, despues de publicar

- [ ] `templates/robots.txt.liquid` presente, md5 `a9af17ec030eb6a33306e2e03c6e7845`
- [ ] 116 archivos en total, y cada md5 igual al del zip
- [ ] `config/settings_data.json` con el codigo de Google dentro
- [ ] La portada, la intro y el pie en frances: ni una frase en castellano
- [ ] Los cuatro ajustes de marca **vacios** en el editor (ver apartado 2)

## Si la API de Shopify no responde

El 23 de septiembre de 2026 la API empezo a devolver:

    This shop is unavailable for API access.
    The merchant may need to resolve a billing issue or upgrade their plan.

Con ese error **no se puede subir ningun tema**: `stagedUploadsCreate`,
`themeCreate` y `themeFilesUpsert` pasan todos por la misma puerta. Tampoco se
puede leer nada de la tienda.

Se resuelve en el panel, mirando el aviso de facturacion. Mientras tanto, el
tema se sube **a mano**, y entonces hay un paso mas:

1. `Tienda online` → `Temas` → `Añadir tema` → `Subir archivo zip`.
2. Subir `villumination-3d-theme-<version>.zip`. **NO publicar todavia.**
3. En el tema recien subido: `⋯` → `Editar codigo`.
4. `templates` → `Añadir una plantilla nueva` → tipo `robots.txt`.
   Shopify la crea con su contenido por defecto.
5. Seleccionar todo lo que haya dentro y pegar encima el contenido de
   `theme/templates/robots.txt.liquid` de este repositorio. Guardar.
6. Ahora si: publicar.

Y ya esta. Antes habia un paso 7 —reparar a mano las dieciseis traducciones de
ajustes, idioma por idioma, en `Configuracion` → `Idiomas`— que desde la
4.74.0 **ya no hace falta**: esos textos viajan dentro del zip.

El paso 4 y 5 no son opcionales. Sin ellos la tienda sirve el robots.txt por
defecto de Shopify y se pierden los permisos explicitos a los rastreadores de
IA, que es justo lo que hace que la tienda aparezca en ChatGPT, Claude,
Perplexity y Gemini.
