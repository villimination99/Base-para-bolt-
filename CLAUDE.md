# Cómo se trabaja en este repositorio

Este archivo **no sustituye a nada**. Los LEEME siguen mandando sobre su tema;
aquí sólo está lo que vale para todo y lo que ya costó caro aprender, para que
no haya que volver a tropezar.

## Lo primero, porque se rompe solo

**Al zip de Shopify sólo viaja `theme/`.** Todo lo demás —`verificadores/`,
`marca/`, `hub/`, `creativo/`, los `.mjs` de la raíz— son herramientas. Nada de
eso llega a la tienda.

**`hub/vi-p-completo.html` es el dueño de `theme/assets/vi-p.js` y
`theme/assets/vi-p.css`.** `partir.mjs` los escribe a partir de él. Editar esos
dos assets a mano *funciona*: las baterías pasan, el zip sale bien, todo parece
correcto — hasta que alguien vuelve a partir el hub y el trabajo desaparece sin
un aviso. Ya pasó una vez, con los chakras y la tira del tiempo. Por eso existe
la comprobación 48.

## Dónde está cada cosa

| Documento | De qué trata |
| --- | --- |
| `README.md` | Qué es el tema y qué se edita sin tocar código |
| `LEEME-tienda.md` | Auditoría de la tienda: lo que hay que arreglar y por qué |
| `LEEME-caja.md` | La caja y `account.villuminations.com` |
| `LEEME-publicar.md` | Publicar un tema sin que Shopify lo rompa |
| `LEEME-skills.md` | Las skills del contenedor y cómo se reconstruyen |
| `marca/LEEME.md` | Logotipos, favicon, imagen para compartir |
| `creativo/LEEME.md` | El equipo de vídeo. Tiene su propio `CLAUDE.md` |

Antes de responder sobre un tema, **lee su LEEME**. Suele estar ya contestado, y
con los números medidos.

## Las órdenes

```bash
npm run check         # las 48 comprobaciones. Ninguna entrega sin esto en verde
npm run acceso        # WCAG 2.1 AA y 320 px, sección por sección
npm run vi-p          # el hub VI.P dentro del tema
npm run theme-check   # el theme-check de Shopify
npm run construir     # construye el 3D
npm run partir        # parte el hub maestro hacia theme/assets/
npm run empaquetar    # saca el zip (sólo theme/)
```

## Las reglas

**1. Comprobar antes de afirmar.** Es la que más rinde, con diferencia. En la
ronda del 11 al 18 de octubre, **las cuatro veces** que se fue a comprobar algo
que ya estaba dado por bueno, apareció un fallo. Tres de esos cuatro eran
errores escritos con toda confianza en un documento de aquí:

- `LEEME-caja.md` decía que `villuminations-logo-ancho-fondo.png` lleva fondo
  claro. Lleva `#05050f`, casi negro. Lo dice `marca/generar-logotipos.mjs`
  línea 75.
- Daba `#23234a` para los bordes de la caja. Contra el campo `#121228` eso es
  **1,23:1**, y el mínimo para el contorno de un control es 3:1. El bueno es
  `#6b6fae`.
- Afirmaba que la API de personalización de la caja no estaba limitada por plan.
  Sí lo está: la documentación de Shopify pide Plus, y la tienda está en Basic.

**2. Mirar la salida, no el informe.** Un JSON que dice que todo fue bien no
prueba que se vea bien. Los dos fallos de contraste de `creativo/` salieron de
abrir las imágenes; sus informes decían «ok» las dos veces. Si algo se ve, hay
que verlo.

**3. Las baterías antes de cerrar.** `npm run check` siempre. `npm run acceso` y
`npm run vi-p` si se tocó el tema o el hub. No se anuncia nada como terminado
sin eso, y si algo falla se dice con su salida, no se suaviza.

**4. Corregir en voz alta.** Cuando algo que ya estaba escrito resulte estar
mal, se arregla **y se deja dicho que estaba mal**, en el archivo y en el
commit. Un documento corregido en silencio vuelve a engañar al siguiente.

**5. Sólo se mejora.** No se deshace lo que funciona ni se reescribe por gusto.
Lo que hay está ahí por una razón, muchas veces por una que costó dinero o una
sesión entera. Si algo parece sobrar, se pregunta antes de quitarlo. Añadir,
afinar, corregir: sí. Barrer y empezar de cero: no.

**6. Nada se publica sin que lo apruebes.** Ni temas, ni cambios en la tienda en
vivo, ni vídeos, ni nada hacia fuera. Se deja listo y se te enseña.

## Lo que muerde si no se sabe

- **Cinco idiomas**: `de`, `en.default`, `es`, `fr`, `ja`. Las cinco tienen que
  llevar las mismas claves, y la batería lo comprueba. Texto dentro de una
  imagen no se traduce.
- **El cian `#00d4ff` da 1,77:1 sobre blanco.** Es el color principal de la
  marca y no se lee sobre fondo claro. Sobre claro el único que aguanta es el
  morado `#7b2fff` (5,69:1), y es justo el que *no* aguanta sobre el fondo
  oscuro de la marca (3,42:1). Esto ha mordido ya tres veces: en la caja, en la
  hoja de contactos del vídeo y en la portada.
- **`package.json` se versiona** desde 4.48.0. Estuvo ignorado y cada
  `npm i --no-save` podaba las dependencias que no estaban escritas; se
  perseguían errores del árbol de módulos creyendo que eran del código.
- **La tienda está en Basic**, no en Plus. Lo que la API de la caja no deja
  escribir se hace a mano en el editor; está en `LEEME-caja.md`.

## El contenedor

Es efímero y se recicla. Lo que no esté **commiteado y empujado** se pierde.
La rama de trabajo es `claude/impulse-shopify-theme-a6mb8w`.

Las skills se reinstalan solas desde `skills-lock.json` y
`.claude/settings.json`: por eso esos dos sí entran en git aunque `.claude/*`
esté ignorado.
