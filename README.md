# Villumination 3D — Tema Shopify

Tema **Online Store 2.0** con estética neón sobre fondo negro, tipografía
legible (modo alta accesibilidad), intro splash 3D interactivo, visor
**3D + Realidad Aumentada** nativo de Shopify, y efectos visuales ligeros
con carga diferida.

## Instalación

1. Comprime el **contenido** de esta carpeta `theme/` en un `.zip`
   (que en la raíz del zip queden `assets/`, `config/`, `layout/`,
   `locales/`, `sections/`, `snippets/`, `templates/`).
2. En Shopify: **Tienda online → Temas → Agregar tema → Subir archivo zip**.
3. Personalízalo desde **Personalizar** (todo es editable, ver abajo).

## Qué es editable (sin tocar código)

- **Colores** (fondo + 5 neones), **tipografía** y **modo alta legibilidad**
  para personas con problemas de visión → *Configuración del tema*.
- **Intro splash 3D**: activar/desactivar, versión 3D interactiva o CSS,
  título y subtítulo.
- **Efectos visuales**: efecto estacional (nieve / confeti / corazones /
  chispas), densidad, parallax, animación al hacer scroll, inclinación 3D
  de tarjetas.
- **Producto**: activar visor 3D + AR, zoom, formulario fijo.
- **Encabezado / Pie**: menús, logo, redes sociales, boletín.
- **Página de inicio**: hero, productos destacados, rejilla de videos y
  planes de suscripción — todas secciones con bloques.

## 3D + Realidad Aumentada

Sube modelos `.glb` / `.usdz` a un producto en el admin de Shopify (en la
sección de medios). El tema los muestra automáticamente con rotar/zoom y el
botón "Ver en tu espacio" (AR) en móviles compatibles. Nativo de Shopify,
sin apps de pago.

## Rendimiento

- CSS/JS propios, sin frameworks. `base.js` y `effects.js` cargan con `defer`.
- Todos los efectos respetan `prefers-reduced-motion` y se pausan con la
  pestaña oculta.
- Fuente de marca (Orbitron) cargada de forma no bloqueante.
- Verificar con Google PageSpeed Insights tras subir contenido real.

Validado con `@shopify/theme-check` — **0 errores**.
