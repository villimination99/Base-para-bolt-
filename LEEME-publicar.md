# Publicar un tema: las dos cosas que Shopify rompe

Cada vez que se publica una copia nueva del tema hay que reparar dos cosas a
mano. No son fallos del tema: son como funciona Shopify.

## 1. El zip se come `templates/robots.txt.liquid`

Confirmado **15 veces**. El import de un zip descarta ese archivo en silencio:
no hay aviso, no hay error, el tema queda con 120 archivos en vez de 121 y la
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

## 2. Las traducciones de los ajustes NO se heredan

Las traducciones en Shopify van **por tema**. Al publicar una copia nueva, los
textos que el comerciante escribio en el editor vuelven al idioma base
—espanol— para todos los demas idiomas, aunque el tema nuevo sea identico.

Los textos de los archivos `locales/*.json` viajan dentro del zip y no se
pierden. Lo que se pierde son los valores de `config/settings_data.json` que
Shopify expone como contenido traducible. En este tema son **cuatro**:

| Clave | Valor en espanol |
| --- | --- |
| `general.brand_tagline` | Transforma tu cuerpo. Domina tu mente. |
| `general.splash_tagline` | TRANSFORMA TU CUERPO. DOMINA TU MENTE. |
| `general.splash_frases` | EL LIMITE LO PONES TU |
| `general.cart_cross_sell_title` | Completa tu compra |

Cuatro claves por cuatro idiomas: **16 traducciones** que hay que volver a
registrar en cada publicacion. Sin esto, un visitante frances ve la pantalla de
entrada en espanol.

### Como repararlo

1. Leer las traducciones del tema **anterior** (sigue en la biblioteca):
   `translatableResource(resourceId: "gid://shopify/OnlineStoreTheme/<viejo>")`
   con `translations(locale: "fr")`, y lo mismo para en, de y ja.
2. Leer los **digests** del tema nuevo: `translatableContent { key digest }`.
   El digest se calcula sobre el valor en espanol, asi que cambia con el tema.
3. Registrarlas con `translationsRegister` sobre el tema nuevo.
4. Comprobar que los cuatro idiomas tienen el mismo numero de claves que el
   tema anterior.

Las respuestas de estas consultas pesan 1-2 MB, asi que conviene pedir solo
`{ key }` para contar y filtrar con jq en vez de leerlas enteras.

## Lo que NO se pierde

- Las politicas de la tienda y sus traducciones: son de la tienda, no del tema.
- `config/settings_data.json`: viaja en el zip. El codigo de Google
  (`seo_google_verification`), el logotipo, el favicon y la imagen de compartir
  sobreviven.
- Los archivos `locales/*.json` con las 353 claves de cada idioma.

## Comprobacion final, despues de publicar

- [ ] `templates/robots.txt.liquid` presente, md5 `a9af17ec030eb6a33306e2e03c6e7845`
- [ ] 121 archivos en total
- [ ] `config/settings_data.json` con el codigo de Google dentro
- [ ] Las 16 traducciones de ajustes, registradas
- [ ] Los cuatro idiomas con el mismo recuento de claves que el tema anterior
