# Biblioteca VILLUMINATIONS — libros recuperados

Recuperación tipográfica de tres obras esotéricas a partir de sus digitalizaciones
originales, compuestas en formato de libro A5 con la identidad de
[villuminations.com](https://villuminations.com).

## Resultado

| Libro | Autor | Original | Ahora |
|-------|-------|----------|-------|
| Curso Zodiacal | Samael Aun Weor | 82 pág. A4 | **142 pág. A5** · 16 capítulos |
| Las Conjuraciones y la Invocación del Sabio Salomón | Recopilación gnóstica | 29 pág. A4 | **52 pág. A5** · 6 capítulos |
| Conocimiento de Sí Mismo (Fase B) | Conferencias gnósticas | 61 pág. A4 | **105 pág. A5** · 26 capítulos |

El número de páginas sube porque cambia el formato: de A4 a A5, que es el tamaño
clásico de libro y el que mejor se lee en pantalla y en papel.

## Qué se ha arreglado

Las digitalizaciones de origen tenían tres problemas que hacían el texto
incómodo de leer y prácticamente imposible de reutilizar:

- **Encabezados repetidos mezclados con el texto.** Cada página traía incrustado
  «Curso Zodiacal — Samael Aun Weor / Instituto Cultural Quetzalcóatl — Página No. 14»
  o «Conocimiento de Sí Mismo — -4-», que aparecían en medio de las frases al
  copiar o buscar.
- **Párrafos partidos.** El texto guardaba los saltos de línea de la maquetación
  original, no los párrafos, así que cada renglón era una línea suelta.
- **Titulares duplicados.** El texto en negrita estaba dibujado dos y hasta tres
  veces, y al extraerlo salía «LAS CONJURACIONES LAS CONJURACIONES» o
  «LA CONJURACION DE LOS SIETE LA CONJURACION DE LOS SIETE URACION DE LOS SIETE».

Sobre eso, la edición añade:

- **Índice navegable** con el número de página real de cada capítulo, calculado
  midiendo el PDF ya compuesto.
- **Marcadores de PDF**, para saltar de capítulo desde el panel del lector.
- **Numeración de páginas** y titulillo con el nombre del libro en cada pie.
- **Capitulares** al inicio de cada capítulo y separadores decorativos.
- **Bloques rituales destacados**: las conjuraciones e invocaciones se componen
  centradas y en color de acento, separadas del cuerpo del texto.
- **Notas al pie recuperadas**: las que la digitalización había dejado caídas en
  mitad del cuerpo se componen ahora en cuerpo menor y separadas por un filete.
- **Acentos perdidos en el escaneo** corregidos en una lista cerrada de casos
  inequívocos (Íntimo, Espíritu, Práctica, Mística…). No se ha tocado nada que
  pudiera alterar el sentido.

## Decisiones de diseño

**Cubierta a sangre en neón, interior en papel hueso.** Las cubiertas llevan la
identidad de la tienda al completo: fondo oscuro, símbolo neón y titular en
Orbitron, cada libro con su color. El interior es claro por dos razones: leer
cien páginas en negativo cansa mucho la vista, y Chromium no pinta los márgenes
de página, de modo que un interior oscuro saldría flotando dentro de un marco
blanco. La cubierta se renderiza como documento aparte, sin márgenes, y después
se une al interior.

**Tipografía.** Orbitron para los titulares —es la fuente de la marca— y
**EB Garamond** para el cuerpo: una serif clásica, muy legible en lecturas
largas y adecuada al carácter de estas obras.

**Color de acento por libro:** Curso Zodiacal en cian, Conjuraciones en magenta,
Conocimiento de Sí Mismo en verde. Son los mismos neones de la tienda,
oscurecidos en el interior para que contrasten sobre papel claro.

## Estructura

```
libros/
├── assets/
│   ├── libro.css      Sistema de diseño (cubierta, índice, capítulos, rituales)
│   ├── fonts.css      Orbitron, EB Garamond y Rajdhani
│   └── fonts/         Los .ttf (instancias estáticas)
├── partials/
│   └── simbolos.svg   Rueda zodiacal, pentagrama, ojo y filigrana
├── src/               El texto ya limpio y estructurado, en JSON
├── dist/              Los tres libros en PDF
├── tools/
│   ├── extraer.py           PDF original → JSON limpio
│   ├── preparar-fuentes.py  Descarga e instancia las fuentes
│   └── render.mjs           Renderizador (Playwright)
└── build.py           Generador
```

## Cómo regenerar

```bash
cd libros
python3 tools/preparar-fuentes.py   # solo la primera vez
python3 tools/extraer.py            # relee los PDF originales
python3 build.py                    # los tres libros
python3 build.py curso              # filtrando por nombre
```

Requisitos: Python 3 con `pypdfium2`, `pypdf` y `fonttools`; Node con Playwright.

Se usa Playwright y no Chromium a secas porque los libros necesitan numeración
de página real en el pie, que solo se controla con `footerTemplate`.

## Cómo corregir el texto

El texto vive en `src/*.json`, ya limpio y separado en capítulos y bloques. Para
corregir una errata basta editar ahí y volver a ejecutar `build.py` — no hace
falta repetir la extracción.

Cada bloque tiene un tipo: `p` (párrafo), `h2` (epígrafe), `ritual` (conjuración
o invocación), `fechas` (rango del signo zodiacal) y `sep` (filigrana).

Si vuelves a ejecutar `extraer.py` se sobrescriben los JSON y se pierden las
correcciones manuales. Conviene hacer una copia antes.

## Sobre los derechos

**Estas tres obras no son originales de VILLUMINATIONS.** Pertenecen a sus
autores y a las instituciones que las difunden (Instituto Cultural Quetzalcóatl y
otras entidades gnósticas). El trabajo hecho aquí es exclusivamente de
recuperación tipográfica: no se ha alterado el contenido ni se reclama autoría
sobre él, y cada libro lo dice de forma expresa en su página de créditos y en el
cierre.

Antes de distribuir o vender estas ediciones conviene **verificar las condiciones
de reutilización de cada obra**. Muchos textos gnósticos se difunden de forma
libre y gratuita, y algunas de esas licencias permiten la copia pero **prohíben
el uso comercial**. Es una comprobación que debe hacerse caso por caso y que
excede lo que se puede resolver desde el diseño.
