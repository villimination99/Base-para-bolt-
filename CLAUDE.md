# VILLUMINATIONS

Tienda Shopify (**villuminations.com**, CAD, Canadá) más el generador de todo lo
que vende de cosecha propia. La memoria larga del proyecto está en
[`boveda/000 · VILLUMINATIONS.md`](boveda/000%20·%20VILLUMINATIONS.md); esto es
solo lo que hay que tener delante antes de escribir una línea.

## Reglas que no se negocian

**La marca se escribe `VILLUMINATIONS`.** Nunca «VILLUMINATIONS 99», ni
«VIllumination», ni «Ma boutique». Las tres han estado a la vez en la tienda.

**Dos bases legales distintas, y no se mezclan.** Los datos de nutrición y
entrenamiento vienen de organismos del Gobierno de EE. UU. y **no están sujetos
a derechos de autor conforme al 17 U.S.C. § 105** — eso cubre las cifras, no la
redacción. Los libros esotéricos se apoyan en la **tradición común y el dominio
público**, que es otra cosa y se dice como tal. Y a nadie se le quita la firma.

**Cada producto se explica solo.** Una ficha no nombra ni describe el contenido
de las demás: el catálogo se descubre comprando. Única excepción: cada nivel
enumera sus propios documentos, y Elite dice que es acumulativo porque lo es.

**Nada de promesas de salud** en las fichas de suplementos, y **ninguna cifra
que no esté en la ficha del proveedor** (véase `tienda/catalogo.py`).

**Rama de trabajo: `claude/shopify-diet-plans-9k0wti`.** No se empuja a otra.

## Cómo funciona esto

El texto de los libros y los planes **no se edita a mano**: vive en
`libros/src/*.json` y `planes/src/*.html`, y los `build.py` lo componen. Editar
un PDF o un HTML de `dist/` es trabajo que se pierde en la siguiente pasada.

Las traducciones son **datos, no marcado**: cada segmento se indexa por el SHA1
de su original castellano normalizado, así que la maqueta existe una sola vez.

### Guardas que abortan la construcción a propósito

No se desactivan para «salir del paso» — cada una está por un fallo real:

| Guarda | Qué impide |
|---|---|
| Cobertura < 100 % | Un libro medio traducido. Sale `Incompleto` y no se escribe el PDF. |
| Ancho de lámina (`cargar-traducciones.py`) | Una etiqueta traducida que no cabe y rompe el dibujo. |
| `comprobar_laminas()` (`libros/build.py`) | Que la prosa prometa siete láminas y haya seis. Pasó, en tres idiomas. |
| `datos_oficiales.comprobar()` | Que una tabla no cuadre con su fuente. |

Comprobaciones rápidas antes de dar nada por bueno:

```
python3 tienda/seo.py        # medidas de título y descripción de los 11 propios
python3 tienda/catalogo.py   # ídem de los 29 de proveedor
python3 tienda/articulos.py  # ídem de los artículos del Diario
python3 libros/tools/faltan.py
python3 tablero.py           # rehace tablero/index.html con el estado del sistema
```

**Las dos bases legales tampoco se mezclan en el blog.** `_fuentes()` de
`tienda/articulos.py` pide `base="federal"` o `base="tradicion"` y no tiene
valor por defecto que sirva para las dos: antes firmaba siempre con el
17 U.S.C. § 105 y el artículo del decanato salió publicado invocando una ley
que no le tocaba.

## La API de Shopify, en corto

Lo que costó descubrir y no está en ningún sitio evidente:

- `productCreate` pide **`ProductCreateInput`** y `productUpdate` pide
  **`ProductUpdateInput`**. No comparten tipo; `ProductInput` ya no vale.
- Un producto en **borrador no admite canales de venta**: `publishablePublish`
  devuelve éxito y no hace nada. Hay que ponerlo en `ACTIVE` primero.
- `translationsRegister` necesita el **digest recién pedido**, después de
  escribir el original. Si cambias el texto, el digest anterior ya no sirve.
- El idioma primario de la tienda es el **castellano**; en/fr/de/ja están
  publicados, y de/ja caen al castellano porque no tienen traducción.
- `menuUpdate` pide **`MenuItemUpdateInput`** y `menuCreate` **`MenuItemCreateInput`**,
  igual que los productos. Los enlaces del menú se traducen aparte, como
  recursos de tipo `LINK`, uno por entrada.
- **`shopPolicyUpdate` está fuera de alcance**: pide `write_legal_policies`, un
  permiso que esta app no tiene. Las políticas solo se tocan desde el panel.
- Traducir el `handle` de una colección crea su URL localizada
  (`/en/collections/supplements`). Está hecho en las seis.

## Lo que sigue pendiente

1. **No hay app de descargas digitales.** Once productos cobran y no entregan
   nada. Se instala desde el panel; por API no se puede.
2. **El nombre de la tienda sigue siendo «VIllumination».** Sale en la pestaña
   del navegador, en el checkout y en cada correo. No se puede cambiar por API:
   es Ajustes → Detalles de la tienda.
3. **De los 29 ya van en tres lenguas el título y las metaetiquetas; los
   cuerpos no.** Los cuerpos en castellano de `tienda/catalogo.py` (`CUERPOS`)
   y los artículos del Diario están solo en español. Al traducirlos, **no se
   copia el texto del proveedor como versión inglesa**: viene lleno de
   declaraciones de salud y las devolvería por la puerta de atrás. Se traduce
   lo que hay escrito aquí.
4. **Las políticas de la tienda están mal y no se arreglan por API.** Escriben
   la marca como «VIllumination», están redactadas en inglés bajo títulos
   franceses, y las condiciones del servicio llevan a la vista literales sin
   rellenar: `[INSERT TRADING NAME]`, `[INSERT BUSINESS ADDRESS]`, `[LINK]`.
   Aparte de eso, la política de reembolso niega remedio incluso para producto
   defectuoso o no entregado, lo que en Quebec es dudoso que se sostenga y
   además invita a la contracargo. Es cosa de mirarlo con calma en el panel.
5. Precio provisional de 9,99 CAD en los seis libros nuevos.
6. **Los dos jabones siguen en UNLISTED.** Ya tienen colección, SEO y variantes
   corregidas; solo falta decidir si se venden. Piden envío y no llevan control
   de existencias, así que activarlos significa poder vender sin stock.
7. **El blog «suplementos» está vacío.** Cero artículos, ninguna entrada de menú
   apunta a él, y aun así `/blogs/suplementos` es una página indexable sin
   contenido. O se llena o se borra desde el panel; no se ha tocado porque
   borrar no se deshace.

## Si acabas de clonar esto

Dos cosas no viajan en el repositorio y hay que rehacerlas a mano en cada
máquina nueva:

```
uv tool install graphifyy && graphify install --platform claude
graphify hook install     # post-commit: rehace el grafo al confirmar
```

Los hooks de git viven en `.git/hooks/`, que git no versiona por diseño. El
`.claude/settings.json` sí viaja, y está escrito para no romperse si graphify
no está instalado: comprueba antes de llamar.

La bóveda de `boveda/` se abre como *vault* en Obsidian. Empieza por
`000 · VILLUMINATIONS.md`, que es la única nota escrita a mano.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
