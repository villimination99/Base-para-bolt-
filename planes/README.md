# Planes VILLUMINATION 99 — PDFs optimizados

Rediseño y ampliación de los 11 planes descargables de [villuminations.com](https://villuminations.com),
con la identidad neón de la tienda aplicada de forma consistente.

## Resultado

| # | Documento | Tier | Antes | Ahora |
|---|-----------|------|-------|-------|
| 01 | Guía Rápida — Volumen Limpio | Básico | 2 pág. | **7 pág.** |
| 02 | Ciclado de Carbohidratos | Pro | 3 pág. | **8 pág.** |
| 03 | Guía de Suplementación | Pro | 4 pág. | **8 pág.** |
| 04 | Plan Definición + Volumen | Pro | 3 pág. | **8 pág.** |
| 05 | Registro de Progreso Semanal | Pro | 5 pág. | **8 pág.** |
| 06 | Dieta Mediterránea 4 Semanas | Elite | 5 pág. | **10 pág.** |
| 07 | 10 Rutinas HIIT | Elite | 5 pág. | **9 pág.** |
| 08 | Plan de Entrenamiento 8 Semanas | Elite | 5 pág. | **10 pág.** |
| 09 | Meditación y Mindfulness | Elite | 4 pág. | **8 pág.** |
| 10 | Protocolo de Sueño | Elite | 3 pág. | **8 pág.** |
| 11 | Coaching Semanal | Elite | 9 pág. | **10 pág.** |
| | **Total** | | 48 pág. | **94 pág.** |

## Qué se ha corregido

**Errores de los PDFs originales**

- **Acentos ausentes en todo el texto.** Los originales decían «Definicion», «Nutricion»,
  «Sueno», «Proteina». Reescrito con ortografía correcta.
- **Glifos rotos.** Los iconos y casillas se imprimían como `&¡`, `%¡` y `'`. Sustituidos por
  elementos vectoriales.
- **Ilustraciones que nunca se generaron.** Los originales contenían literalmente
  `[Robot levantando pesas]`, `[Robot cocinando]`, `[Robot meditando]`. Se han creado seis
  ilustraciones SVG del robot mascota en estilo neón.
- **Contenido prometido en portada pero ausente dentro:**
  - «20 recetas» → solo había 10. Añadidas las recetas 11–20.
  - «4 semanas» de dieta mediterránea → solo estaba la semana 1. Añadidas las semanas 2, 3 y 4.
  - «10 rutinas HIIT» → solo 3 estaban desarrolladas. Las 10 tienen ahora tabla completa.
  - «4 fases» de entrenamiento → las fases 3 y 4 no existían. Desarrolladas.
  - Ciclado de carbohidratos → faltaba el menú del día MEDIO. Añadido.
- **Coaching semanal:** eran cuatro formularios idénticos repetidos. Cada semana tiene ahora un
  foco propio (diagnóstico, ajuste, intensificación, consolidación).

**Mejoras de contenido**

- **Personalización por peso corporal.** Los originales daban calorías fijas (útiles solo para
  quien pesara exactamente lo mismo que el atleta de referencia). Ahora todos los planes
  nutricionales incluyen coeficientes en g/kg, tabla de equivalencias y hueco para calcular
  los propios números.
- **Cifras internamente consistentes.** Los totales de macros y calorías cuadran con el desglose.
- **Aviso legal y sanitario** en todos los documentos, con contraindicaciones específicas por
  tema (embarazo, menores, patologías, TCA, antidopaje). Necesario al vender planes dietarios.
- **Secciones nuevas de valor:** calculadora de macros, tabla de intercambios de alimentos,
  errores frecuentes, resolución de problemas, batch cooking, banco de 30 preguntas para
  coaching, suplementos sin evidencia, escalado por nivel.
- **Índice, cabeceras, pies numerados** y página de cierre con CTA y venta cruzada entre tiers.
- **Metadatos PDF** (título, autor, asunto, palabras clave) para catalogación y SEO.

## Identidad visual

Tomada del propio tema Shopify (`config/settings_data.json` y `assets/villumination.css`):

| Elemento | Valor |
|----------|-------|
| Cian neón | `#00f0ff` |
| Magenta neón | `#ff00e5` |
| Verde neón | `#00ff88` |
| Naranja neón | `#ff6600` |
| Amarillo neón | `#ffdd00` |
| Púrpura | `#7b2fff` |
| Turquesa | `#00ffcc` |
| Fondo | `#050510` |
| Titulares | Orbitron 900 |
| Texto | Rajdhani |
| Logotipo | «VI» en degradado turquesa → púrpura → rosa + «99» en naranja |

Cada tier tiene un color de acento propio para que se distingan de un vistazo:

- **BÁSICO** → cian `#00f0ff`
- **PRO** → magenta `#ff00e5`
- **ELITE** → verde `#00ff88`

## Estructura

```
planes/
├── assets/
│   ├── brand.css      Sistema de diseño de impresión (A4, neón, componentes)
│   ├── fonts.css      Orbitron y Rajdhani (instancias estáticas)
│   ├── fonts/         Los .ttf de marca
│   └── impresion.css  Reescritura para la edición en papel
├── partials/
│   └── sprite.svg     6 poses del robot mascota
├── src/               Los 11 documentos en HTML (aquí se edita el contenido)
├── dist/              Edición pantalla (neón)
│   └── impresion/     Edición papel
├── tools/             Preparación de fuentes
└── build.py           Generador
```

## Dos ediciones

| Edición | Carpeta | Peso total | Para qué |
|---------|---------|-----------|----------|
| Pantalla (neón) | `dist/` | 25,6 MB | Lectura en móvil, tablet y ordenador. Es la que vende. |
| Impresión (papel) | `dist/impresion/` | 4,8 MB | Fondo blanco, sin resplandores. Ahorra tinta y pesa 6 veces menos. |

Mismo contenido y misma paginación en las dos. Lo ideal es entregar ambas en la descarga:
quien lee en pantalla se queda con la neón y quien imprime, con la de papel.

## Cómo regenerar los PDFs

```bash
cd planes
python3 build.py                  # edición pantalla
python3 build.py --impresion      # edición papel
python3 build.py --ambas          # las dos
python3 build.py --ambas 06-elite # filtrando por nombre
python3 tools/preparar-fuentes.py # solo si cambian las fuentes de marca
```

Requisitos: Python 3 y Chromium. `pypdf` es opcional (añade metadatos, recomprime y verifica
la paginación). `tools/preparar-fuentes.py` necesita además `fonttools` y `brotli`.

## Sobre el peso de los archivos

La edición de pantalla pesa unos 2,4 MB por documento y no puede bajar mucho más sin
renunciar al neón: Chromium convierte cada resplandor y cada capa translúcida en un mapa de
bits con su máscara de transparencia. Es el precio del estilo. La edición de impresión no
tiene esos efectos y por eso pesa 6 veces menos.

Sí se corrigió un problema real de origen: Orbitron es una **fuente variable**, y Chromium no
sabe incrustarlas en PDF — convertía cada titular en dibujos Type3, con texto no seleccionable
ni buscable. `tools/preparar-fuentes.py` genera instancias estáticas y ahora los titulares se
incrustan como fuente de verdad: más nítidos, seleccionables y buscables.

El generador comprueba que cada `<section class="page">` ocupe exactamente una página del PDF
y avisa si algo se descuadra.

## Cómo editar el contenido

Edita el HTML de `src/` y vuelve a ejecutar `build.py`. Cada página es un bloque
`<section class="page">` con esta estructura:

```html
<section class="page">
  <header class="pg-head">…logotipo, sección, dominio…</header>
  <main>…contenido…</main>
  <footer class="pg-foot">…copyright y número de página…</footer>
</section>
```

Clases disponibles: `card`, `callout` (`.info`, `.warn`), `metric`, `tag` (`.hi`, `.mid`,
`.lo`, `.ok`, `.no`), `ol.neon`, `ul.dots`, `ul.check`, `fill` (campo rellenable), `box`
(casilla), `cta`, `upsell`, `legal`.

El tier se fija con la clase del `<body>`: `t-basico`, `t-pro` o `t-elite`.

> Al añadir contenido, comprueba que `build.py` sigue diciendo «Paginación correcta»: las
> páginas tienen altura fija y el contenido sobrante se recortaría.

## Nota sobre el aviso legal

Los textos legales incluidos son una base razonable para venta de contenidos de nutrición y
entrenamiento, pero **no son asesoramiento jurídico**. Conviene que un profesional los revise
según el país donde vendas y la normativa de consumo y protección de datos que te aplique.
