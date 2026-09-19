# VILLUMINATIONS · ficheros de impresión bajo demanda

24 PNG `villuminations-*.png`: 4 piezas en
6 acentos. Cada uno lleva al lado su `.md` con la prenda, el
área, el tamaño del dibujo, la colocación, las dos tintas y lo que mide su
ráster.

## Lo primero, porque es lo que se hace mal

**El lienzo de cada PNG ES el área de estampación completa**, y el dibujo va
dentro con transparencia alrededor. Al subirlo, dile a la aplicación que lo
**encaje al área**. No lo escales, no lo centres a mano, no lo recortes: cae
solo en su tamaño y en su sitio, y queda a 300 ppp exactos.

Antes no era así —el fichero medía lo que medía el dibujo— y pasaba esto: la
aplicación estiraba una pieza de pecho de 1063 píxeles hasta los 30 cm del área
frontal, salían 88 ppp, avisaba de resolución insuficiente y había que
encogerla a ojo hasta que callara. Eso no es un fichero, es una negociación, y
la segunda tirada sale a otro tamaño que la primera. Ya no pasa.

## Qué se sube

| pieza | prenda y posición | fichero | dibujo dentro | colocado |
|---|---|---|---|---|
| dorsal | camiseta negra · espalda · 12″ × 16″ | **3602 × 4795 px** | 28.0 × 32.2 cm | a 1.2 / 2.5 cm del borde |
| pecho | camiseta negra · frente · 12″ × 16″ | **3602 × 4795 px** | 9.0 × 9.5 cm | a 10.8 / 6.0 cm del borde |
| manga | sudadera negra · manga de sudadera | **1181 × 4724 px** | 8.0 × 22.2 cm | a 1.0 / 6.0 cm del borde |
| pierna | pantalón de chándal negro · pernera de pantalón de chándal | **2835 × 3543 px** | 9.2 × 24.1 cm | a 7.4 / 3.0 cm del borde |

Todos a **300 ppp**, PNG con canal alfa, fondo transparente comprobado
píxel a píxel, opacidad plena, ningún rasgo por debajo de 1.0 mm y
ningún hueco interior que se empaste.

## Los 6 acentos

| acento | pantalla | impresión |
|---|---|---|
| cian | `#00f0ff` | `#00CAD6` |
| cardenal | `#e01b3d` | `#BC1733` |
| oro | `#ffc21a` | `#D6A316` |
| purpura | `#7b2fff` | `#6727D6` |
| magenta | `#ff00e5` | `#D600C0` |
| hielo | `#8fa6c4` | `#8FA6C4` |

El hueso es `#ECEFF6` en todos.

**Por qué el fichero no lleva el color de la marca.** La DTG sobre prenda
oscura imprime primero una base blanca y el color encima, y esa base levanta y
desatura. El fichero lleva el acento más hondo para que lo impreso caiga cerca
de lo que la marca es en pantalla. **Compensar no es acertar: pide una muestra
y cotéjala antes de cualquier tirada**, y con el rojo y el oro más que con
ninguno, que son los dos que más se mueven.

## Las fotos

Las de `maquetas/` son **composición de marca**: anuncio, publicación y
cabecera de colección.

Para la **ficha de producto** usa las que genera Printful al subir el fichero:
salen de la prenda real, son fotográficas y son gratis. Estas no las
sustituyen.

## Y antes de la primera tirada

**Coteja el área con el producto concreto.** Las de la tabla son las estándar
del catálogo y varían entre modelos. Si el tuyo admite más, subirlo es cambiar
un número en `ropa/tools/exportar-pod.py`, no rehacer el dibujo.

## Cómo se rehace todo esto

```
python3 ropa/tools/dibujar-espinas.py --hoja   # las láminas y su hoja de contacto
python3 ropa/tools/exportar-pod.py --todas     # los 24 ficheros de impresión
python3 ropa/tools/maqueta.py                  # las maquetas de marca
python3 ropa/tools/paquete-pod.py              # esta hoja, el catálogo y el ZIP
```

Generado por `ropa/tools/paquete-pod.py`. No se edita a mano: la siguiente
pasada lo sobrescribe.
