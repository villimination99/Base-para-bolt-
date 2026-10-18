# Bitácora

Dónde estamos, qué está abierto y **qué ya se probó y no funciona**.

La cronología completa no está aquí: está en `git log`, que son 188 commits con
mensajes que explican el porqué. Duplicarla sería reescribir por gusto y además
se pudriría. Lo que el log no da bien es el estado de ahora y los callejones sin
salida — eso es lo que recoge este archivo.

```bash
git log --date=short --format='%ad %h %s'    # la historia, de verdad
```

**Última actualización: 18 de octubre de 2026.** Quien cierre una sesión con
algo decidido, probado o descartado, lo añade aquí.

---

## Estado actual

El tema está en 4.75.0, con las 48 comprobaciones, la batería de accesibilidad
y la de VI.P en verde. La tienda vende en cinco idiomas y está en plan **Basic**.

La caja de pago tiene puesto por API lo único que Basic deja escribir: el
logotipo y los colores de acento. Sigue siendo **blanca**; pasarla a oscuro es
trabajo manual y está sin hacer.

Hay un equipo de agentes para vídeo en `creativo/`, montado el 18 de octubre y
probado contra clips sintéticos. Nunca ha editado un clip real.

---

## Hilos abiertos

Por orden de lo que cuesta equivocarse.

| Qué | Por qué importa | Quién puede |
| --- | --- | --- |
| **Comprobar que los PDF se entregan** | El cliente paga y no recibe nada. Es el fallo más caro que existe. | **Tú.** El conector de productos digitales responde `Forbidden`. |
| **El píxel de Meta** | Sin él no hay datos para optimizar anuncios. | **Tú.** Al conector le falta el permiso `read_pixels`. |
| **Verificar el dominio en Meta** | `seo_facebook_domain` existe en el esquema (línea 916) y **no tiene valor**. El tema emite la etiqueta en cuanto se pegue el código. | Tú pegas el código; yo lo pongo en el ajuste. |
| **SPF, DKIM y DMARC** | El 27 de septiembre no existía ninguno: el correo de la tienda se va a spam. | **Tú.** Este contenedor no tiene DNS de salida, no puedo ni mirarlo. |
| **La barra de envío gratis** | `cart_free_shipping_threshold` existe (línea 833) y **no tiene valor**, mientras la tienda regala envío a 75 CAD en Canadá y 100 en EE. UU. Lo regala sin decirlo. | Yo, en cuanto confirmes los umbrales. |
| **`/collections/cuidado-personal` está vacía** | Dos productos y los dos ocultos. Ningún anuncio debe apuntar ahí. | Tú decides si se publican o se quita la colección. |
| **La caja en oscuro** | Es manual. El primer paso es abrir el editor y ver si deja cambiar colores en Basic — eso no lo he podido comprobar desde fuera. | **Tú**, con `LEEME-caja.md` al lado. |
| **La tipografía Assistant para `creativo/`** | Sin ella las portadas salen con Inter del sistema, no con la letra de la marca. | **Tú.** El proxy da 403 en los dominios de fuentes. |

---

## Callejones sin salida

Comprobado, no supuesto. **No volver a intentarlo** sin que haya cambiado algo.

### La API de personalización de la caja

En plan Basic **sólo** se dejan escribir tres cosas: el logotipo de la cabecera,
su alineación y posición, y `colors.global.accent` / `brand`. Todo lo demás
—esquemas de color, tipografía, radio de esquinas, botón principal, favicon,
imagen y separador de cabecera, y el esquema del cuerpo y del resumen— devuelve:

> One or more fields cannot be modified with public access to the Checkout
> Branding API.

Está probado campo por campo contra el perfil borrador. La documentación pide
**Plus**, y la tienda está en Basic.

`checkoutAndAccountsConfigurationUpdate`, que es la mutación que la propia API
recomienda, **no existe en la versión 2026-01** del Admin API, que es a la que
está fijado el conector.

**Plus está descartado**: del orden de 2.300 USD al mes contra los 39 del Basic,
para unos colores que el editor manual cambia gratis.

### La red de este contenedor

| Destino | Qué pasa |
| --- | --- |
| `cdn.shopify.com` | 403. No puedo mirar las imágenes de la tienda. |
| Fuentes de Google y `raw` de GitHub | 403. No puedo bajar tipografías. |
| DNS de salida | No hay. No puedo comprobar SPF, DKIM ni DMARC. |
| Modelos de `faster-whisper` | No se bajan. La transcripción de voz de `creativo/` no está probada. |

### Conectores

- Productos digitales: `Forbidden`.
- Píxel de Meta: le falta `read_pixels`.
- **Mem0** (memoria entre sesiones) y **Supabase** aparecen sin autorizar. Mem0
  es, literalmente, un almacén de memoria: si lo autorizas en los conectores de
  claude.ai, habría recuerdo real entre sesiones además de este archivo. Yo no
  puedo autorizarlo.

---

## Decisiones cerradas

No hace falta volver a discutirlas. Si cambian, se cambian aquí y se dice por qué.

- **La caja va en oscuro**, no en claro con acento morado. Se propuso en claro y
  se rechazó: la tienda es oscura y tiene que parecerse a sí misma.
- **Al zip sólo viaja `theme/`.**
- **`hub/vi-p-completo.html` es el dueño** de `theme/assets/vi-p.js` y `vi-p.css`.
- **`package.json` se versiona** desde 4.48.0.
- **`creativo/` es autocontenido** y Claude Code se arranca *dentro* de esa
  carpeta, para que el equipo de vídeo no se mezcle con el trabajo del tema.
- **El servidor MCP de memoria va pinneado** a `@1.0.0`, no a la última.
- **El logotipo depende del fondo**: `villuminations-logo-ancho.png`
  (transparente) sobre oscuro, `-fondo.png` (panel `#05050f`) sobre claro.

---

## Errores que ya se cometieron

Están corregidos. Se dejan escritos porque un documento arreglado en silencio
vuelve a engañar al siguiente.

- `LEEME-caja.md` decía que el logotipo `-fondo` lleva fondo **claro**. Lleva
  `#05050f`, casi negro.
- Daba `#23234a` para los bordes de la caja: **1,23:1**, cuando el mínimo es 3:1.
- Afirmaba que la API de la caja **no** estaba limitada por plan. Sí lo está.
- Los assets `vi-p.js` y `vi-p.css` se editaron a mano una vez, con el maestro
  sin enterarse. Habría muerto en la siguiente pasada de `partir.mjs`. De ahí
  salió la comprobación 48.
- En `creativo/`, la hora de la hoja de contactos iba en cian y desaparecía
  sobre planos cian y verdes; y el degradado de la portada se apagaba antes de
  la última palabra, justo la que va en cian. Los dos salieron de **mirar las
  imágenes**: sus informes decían «ok».
