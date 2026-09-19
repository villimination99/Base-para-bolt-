# Bóveda de conocimiento

Abre esta carpeta como *vault* en Obsidian.

Dentro hay 1278 notas y un lienzo (`graph.canvas`). Todas menos una las genera
`graphify` a partir del repositorio: una nota por cada entidad que encuentra
—función, clase, concepto, lámina, capítulo— con sus enlaces `[[así]]` hacia
las demás. La excepción es **`000 · VILLUMINATIONS.md`**, que está escrita a
mano y es la que hay que leer primero: dice qué es el proyecto, qué reglas no
se tocan y qué quedó pendiente.

## Regenerarla

```
/graphify .                 # reconstruye el grafo en graphify-out/
graphify export obsidian    # vuelca las notas
cp -r graphify-out/obsidian/* boveda/
```

`graphify-out/` está en el `.gitignore` porque son megas de JSON regenerable.
Esta carpeta sí se versiona, y por una razón concreta: la máquina donde se
generó es efímera y se recicla sola. Lo que no está en el repositorio, se pierde.

Al regenerar, `000 · VILLUMINATIONS.md` y este mismo archivo no se sobrescriben
—`graphify` no los conoce—, pero sí quedan desactualizados. Merece la pena
repasarlos cuando el proyecto cambie de sitio.

## Aviso sobre los enlaces

El diagnóstico del grafo cuenta 116 aristas cuyo destino no existe: nombres que
la extracción semántica dedujo y que no coinciden con los que sacó el análisis
del código. Se traducen en enlaces rotos dentro de algunas notas. El contenido
de cada nota es bueno; un enlace suelto puede no llevar a ninguna parte.
