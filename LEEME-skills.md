# Las skills del contenedor

El contenedor donde se trabaja es efimero: cada sesion clona el repositorio de
cero. Las skills instaladas viven en `.agents/skills/`, que son 111 MB de
repositorios ajenos y **no entran en git**. Sin este archivo y sin
`skills-lock.json`, cada sesion nueva empezaria sin ninguna y sin saber cuales
habia.

## Volver a instalarlas en un contenedor nuevo

    npx skills install

Lee `skills-lock.json` y baja las cinco. Si hiciera falta una suelta:

    npx skills add https://github.com/<fuente> --skill <nombre>

## Que hay instalado y para que

| Skill | Fuente | Para que |
| --- | --- | --- |
| `design` | nextlevelbuilder/ui-ux-pro-max-skill | identidad de marca, logotipos, banners |
| `impeccable` | pbakaus/impeccable | revision de interfaz: jerarquia, accesibilidad, estados |
| `memanto-companion` | moorcheh-ai/memanto | memoria de ingenieria entre sesiones |
| `ruflo` | ruvnet/ruflo | orquestacion de varios agentes |
| `shopify-admin` | shopify/shopify-ai-toolkit | escribir GraphQL del Admin de Shopify |

`ruflo` esta instalada pero **sin inicializar** a proposito: `npx ruflo init`
reescribe `.claude/` y mete hooks que corren en cada llamada de herramienta.

## La telemetria de Shopify, apagada

`shopify-admin` trae instrumentacion que manda un evento a
`https://shopify.dev/mcp/usage` cada vez que se activa. No es solo un contador:
su propio `scripts/track-telemetry.sh` documenta que en Claude Code captura
`user_prompt` — el mensaje del usuario **literal** — y lo adjunta cuando la
skill se activa. Y su `SKILL.md` pide llamar a `validate.mjs` en cada respuesta
con `--user-prompt-base64`, «verbatim — do not summarize, translate, or
paraphrase».

Los mensajes de esta tienda hablan de estrategia, margenes y datos del negocio.
Eso no sale de aqui. En `.claude/settings.json` quedan puestas las dos salidas
que el propio script comprueba antes que nada, en su funcion `is_opted_out`:

    DO_NOT_TRACK=1
    OPT_OUT_INSTRUMENTATION=true

Cualquiera de las dos basta; estan las dos por si una version futura deja de
mirar una. Si alguna vez se quiere volver a activar, se borra ese bloque `env`.

## Por que el GraphQL de Shopify no se escribe con esta skill

El trabajo real con la tienda se hace con el **servidor MCP oficial de Shopify**,
que ya esta conectado a la sesion: `graphql_schema` para no inventar campos,
`validate_graphql_codeblocks` para validar antes de ejecutar, y
`graphql_query` / `graphql_mutation` para correrlo contra la tienda de verdad.
Asi se crearon el cupon, los 19 segmentos y el arreglo de la sobreventa.

La skill sirve para **redactar** GraphQL que se ejecuta en otro sitio, y consulta
un indice generico. El MCP consulta el esquema de **esta** tienda. Se queda
instalada por si hace falta escribir una operacion sin tocar la tienda, pero no
es el camino por defecto.
