# Prueba para saber por qué "Parámetros del tema" sale vacío

Llevo dos intentos sin acertar. Esta prueba da una respuesta **definitiva** en
dos minutos y me dice exactamente por dónde seguir.

## Qué hacer

1. En Shopify: **Tienda online → Temas → ⋯ (junto a tu tema) → Editar código**.
2. En la lista de la izquierda, abre la carpeta **config** y pincha en
   **settings_schema.json**.
3. **Selecciona todo el contenido y bórralo.**
4. Pega dentro el contenido de `settings_schema-MINIMO.json` (el otro archivo
   de esta carpeta).
5. **Guardar**.
6. Abre el editor del tema y entra en **Parámetros del tema**.

## Qué significa cada resultado

### Ves un apartado "Prueba" con una casilla
El esquema **sí carga**. Entonces el problema está en el contenido del archivo
grande y puedo encontrarlo dividiéndolo por mitades. **Dímelo y sigo por ahí.**

### Sigue completamente vacío
El problema **no es el archivo**. Con un esquema de cuatro líneas que es
imposible que falle, si sigue en blanco entonces es una de estas:

- El tema instalado no es el que crees. Comprueba en **Tienda online → Temas**
  qué versión aparece bajo el nombre.
- La subida del tema quedó a medias y `config/` no llegó completo. Se arregla
  subiendo el zip otra vez y activándolo.
- El editor móvil de Shopify no está pintando la lista. **Pruébalo desde un
  ordenador** antes de nada: es lo más rápido de descartar.

**Dímelo también, con lo que veas.**

## Cuando terminemos

Vuelve a poner el `settings_schema.json` completo (está dentro del zip, en
`config/`), o simplemente sube el tema otra vez.
