---
description: Clasifica los clips de inbox/, los edita en paralelo por el camino que toque, los revisa y te informa
---
Edita los clips nuevos de `inbox/`.

1. **Clasifica primero**, que es lo que decide el resto:
   `python3 herramientas/clasificar.py inbox`
   Devuelve una ficha por clip con `camino`: `voz` o `producto`. Si alguno sale
   `ilegible`, dilo al final y no lo edites.

2. **Lanza un sub-agente por clip**, el que diga su ficha:
   - `camino: voz` → **editor-voz**
   - `camino: producto` → **editor-producto**

   **Todos en el mismo mensaje**, para que trabajen en paralelo. A cada uno
   dile su archivo, su camino y, si es de voz, el idioma (`es` si nadie dice
   otra cosa).

3. Cuando acaben todos, pasa el **revisor-marca** sobre `salida/`.

4. Lo que el revisor tumbe, vuelve al editor que toque con el arreglo exacto, y
   se revisa otra vez. No des por bueno un clip que el revisor no haya aprobado.

5. Mueve cada clip ya editado: `mv inbox/<archivo> hechos/`
   Solo despues de que su edicion este terminada y aprobada.

6. **Informa** con una tabla corta: clip, camino, duracion, titulo, texto de
   portada, y la ruta de su carpeta. Si alguna edicion salio sin la tipografia
   Assistant, dilo en una linea aparte.
   Termina siempre con: "No se ha publicado nada. Contesta OK para aprobar."

$ARGUMENTS
