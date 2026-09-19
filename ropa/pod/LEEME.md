# VILLUMINATIONS · ficheros de impresión bajo demanda

## Qué subir a Printful

Los **16 PNG** `villuminations-*.png` de esta carpeta. Cada uno tiene al lado
su `.md` con prenda, posición, colocación, tamaño impreso, área disponible y
las dos tintas.

| pieza | prenda y posición | tamaño impreso | fichero |
|---|---|---|---|
| dorsal | camiseta · espalda | 28,0 × 32,2 cm | 3307 × 3803 px |
| pecho | camiseta · pecho izquierdo | 9,0 × 9,5 cm | 1063 × 1119 px |
| manga | sudadera · manga | 8,0 × 22,2 cm | 945 × 2617 px |
| pierna | chándal · pernera | 10,0 × 26,2 cm | 1181 × 3093 px |

Cuatro acentos cada una: **cian, púrpura, magenta, hielo**.

Todos a **300 ppp**, PNG con canal alfa, fondo transparente verificado píxel a
píxel, opacidad plena y ningún trazo por debajo de 1 mm impreso.

## Las fotos

Las de `ropa/maquetas/` son **composición de marca**: para anuncios,
publicaciones y cabecera de colección.

Para la **ficha de producto** usa las que genera Printful al subir el fichero:
salen de la prenda real, son fotográficas y son gratis. Estas no las
sustituyen.

## Antes de la primera tirada

**Pide una muestra y coteja el color.** La DTG sobre prenda oscura imprime una
base blanca y esa base levanta y desatura, así que el fichero ya lleva un cian
más hondo que el de la marca (`#00C4D6` en vez de `#00f0ff`) para compensar.
Compensar no es acertar.

**Coteja el área con el producto concreto.** Las de la tabla son las estándar
del catálogo y varían entre modelos. Si el tuyo admite más, subir el tamaño es
un parámetro en `ropa/tools/exportar-pod.py`, no rehacer el dibujo.

## Cómo se rehace todo esto

```
python3 ropa/tools/dibujar-espinas.py --hoja   # las láminas y su hoja de contacto
python3 ropa/tools/exportar-pod.py --todas     # los 16 ficheros de impresión
python3 ropa/tools/maqueta.py                  # las maquetas de marca
```
