/* Logotipos de la marca: el de cabecera (1600x400) y su variante con fondo.
   ------------------------------------------------------------------
   POR QUE EXISTE ESTE FICHERO. Los PNG del logotipo se habian rendido a mano
   una sola vez y nadie habia vuelto a tocarlos. Cuando el nombre paso de
   VILLUMINATION a VILLUMINATIONS -- una letra mas -- eso dejo de valer: el
   texto anterior estaba ajustado al milimetro y su tinta terminaba en el
   pixel 1540 de un lienzo de 1600. Una letra mas se salia del lienzo, y el
   logotipo de la cabecera sale en TODAS las paginas y en los cinco idiomas.

   Asi que el ajuste no se hace a ojo: se mide. El guion prueba tamanos de
   letra, rinde, cuenta la tinta de verdad pixel a pixel y se queda con el
   mayor que respeta el margen del diseno. Si ninguno cabe, no escribe nada
   y sale con error.

   EL MARGEN ES EL DEL DISENO ORIGINAL, NO UNO INVENTADO. El logotipo que ya
   estaba en la tienda tenia la tinta entre x=58 y x=1540, y entre y=50 y
   y=349: un marco de unos 58 px por los lados. Ese es el numero que se
   respeta aqui, para que el logotipo nuevo se plante en la cabecera igual
   que el viejo y no haya que tocar "Altura del logo".

   SE MIDE LA TINTA, NO LA CAJA DEL TEXTO. El texto lleva un resplandor
   (feGaussianBlur) que se sale de su caja. La caja diria que cabe y el
   resplandor estaria cortado igualmente. Por eso se cuenta el pixel
   encendido, que es lo que se ve.

   LA LETRA VA INCRUSTADA. La Orbitron del tema se mete en el SVG como
   data URI. Si se dejara al navegador buscarla por nombre, un contenedor
   sin esa fuente rendiria el logotipo en DejaVu sin avisar de nada.

   Uso:  node marca/generar-logotipos.mjs                                   */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const SALIDA = path.join(RAIZ, 'marca');
const FUENTE = path.join(RAIZ, 'theme/assets/orbitron-variable.woff2');
const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const NOMBRE = 'VILLUMINATIONS';

/* El marco que hay que respetar, medido sobre el logotipo anterior. */
const A = 1600, ALTO = 400;
const MARGEN_DCHO = 58;      // la tinta no puede pasar de 1600-58 = 1542
const HOLGURA = 26;          // ni quedarse mas corta que eso, o baila en el hueco
const TEXTO_X = 424;         // donde arranca el nombre, pegado al distintivo

/* La proporcion del diseno: el espaciado entre letras acompana al cuerpo. */
const RATIO_ESP = 10.40 / 112.0;

const fuente = fs.readFileSync(FUENTE).toString('base64');

function svg(cuerpo, conFondo) {
  const esp = (cuerpo * RATIO_ESP).toFixed(2);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${A}" height="${ALTO}" viewBox="0 0 ${A} ${ALTO}">
<defs>
  <style>@font-face{font-family:Orbitron;font-weight:400 900;src:url(data:font/woff2;base64,${fuente}) format('woff2')}</style>
  <!-- El aro recorre el espectro; la VI y el nombre van en cian a violeta,
       que es como se reconoce la marca en el resto de la tienda. -->
  <linearGradient id="ga" gradientUnits="userSpaceOnUse" x1="66.0" y1="58.0" x2="350.0" y2="342.0">
    <stop offset="0%" stop-color="#00d4ff"/><stop offset="45%" stop-color="#7b2fff"/><stop offset="100%" stop-color="#ff2ecb"/>
  </linearGradient>
  <linearGradient id="gvi" gradientUnits="userSpaceOnUse" x1="122.8" y1="58.0" x2="293.2" y2="342.0">
    <stop offset="0%" stop-color="#7df3ff"/><stop offset="50%" stop-color="#00d4ff"/><stop offset="100%" stop-color="#7b2fff"/>
  </linearGradient>
  <linearGradient id="gt" gradientUnits="userSpaceOnUse" x1="400" y1="0" x2="1568" y2="0">
    <stop offset="0%" stop-color="#7df3ff"/><stop offset="35%" stop-color="#00d4ff"/>
    <stop offset="78%" stop-color="#7b2fff"/><stop offset="100%" stop-color="#ff2ecb"/>
  </linearGradient>
  <filter id="glow" x="-20%" y="-80%" width="140%" height="260%">
    <feGaussianBlur stdDeviation="6.40" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
${conFondo ? `<rect width="${A}" height="${ALTO}" fill="#05050f"/>` : ''}
<circle cx="208.0" cy="200.0" r="142.0" fill="none" stroke="url(#ga)" stroke-width="15.20"
        stroke-dasharray="28.80 20.80" stroke-linecap="round" filter="url(#glow)"/>
<text x="208.0" y="208.0" fill="url(#gvi)" filter="url(#glow)" font-family="Orbitron, DejaVu Sans, Verdana, sans-serif"
      font-weight="900" font-size="144.0" text-anchor="middle" dominant-baseline="central">VI</text>
<text x="${TEXTO_X}" y="208.0" fill="url(#gt)" filter="url(#glow)" font-family="Orbitron, DejaVu Sans, Verdana, sans-serif"
      font-weight="900" font-size="${cuerpo.toFixed(1)}" letter-spacing="${esp}" dominant-baseline="central">${NOMBRE}</text>
</svg>`;
}

const nav = await chromium.launch({ executablePath: CHROME });
const ctx = await nav.newContext({ viewport: { width: A, height: ALTO }, deviceScaleFactor: 1 });
const pg = await ctx.newPage();

/* Rinde un SVG y devuelve el PNG y los limites reales de su tinta. */
async function rendir(fuenteSvg) {
  const b64 = Buffer.from(fuenteSvg, 'utf8').toString('base64');
  await pg.setContent(
    `<style>html,body{margin:0;padding:0;background:transparent}img{display:block}</style>` +
    `<img id="i" width="${A}" height="${ALTO}" src="data:image/svg+xml;base64,${b64}">`);
  await pg.locator('#i').evaluate((im) => im.complete || im.decode());
  const png = await pg.screenshot({ omitBackground: true, clip: { x: 0, y: 0, width: A, height: ALTO } });

  const caja = await pg.evaluate(async (b64) => {
    const im = new Image();
    im.src = 'data:image/svg+xml;base64,' + b64;
    await im.decode();
    const c = document.createElement('canvas');
    c.width = im.width || 1600; c.height = im.height || 400;
    const x = c.getContext('2d');
    x.drawImage(im, 0, 0, c.width, c.height);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    let x0 = 1e9, x1 = -1, y0 = 1e9, y1 = -1;
    for (let y = 0; y < c.height; y++) for (let X = 0; X < c.width; X++) {
      const k = (y * c.width + X) * 4;
      const a = d[k + 3]; if (a < 24) continue;
      const luz = (d[k] + d[k + 1] + d[k + 2]) * a / 255;
      if (luz < 70) continue;
      if (X < x0) x0 = X; if (X > x1) x1 = X;
      if (y < y0) y0 = y; if (y > y1) y1 = y;
    }
    return { x0, x1, y0, y1 };
  }, b64);

  return { png, caja };
}

/* Busca el cuerpo mas grande cuya tinta cabe en el marco. */
const TOPE = A - MARGEN_DCHO;          // 1542
let mejor = null;
const probados = [];
for (let cuerpo = 118; cuerpo >= 70; cuerpo -= 0.5) {
  const r = await rendir(svg(cuerpo, false));
  probados.push({ cuerpo, x1: r.caja.x1 });
  if (r.caja.x1 <= TOPE) { mejor = { cuerpo, caja: r.caja, png: r.png }; break; }
}

if (!mejor) {
  console.error('NADA CABE. "' + NOMBRE + '" no entra en ' + A + 'x' + ALTO + ' ni al cuerpo mas pequeno probado.');
  console.error(probados.slice(-3).map((p) => '  cuerpo ' + p.cuerpo + ' -> tinta hasta ' + p.x1).join('\n'));
  await nav.close();
  process.exit(1);
}

const { cuerpo, caja } = mejor;
const holgura = TOPE - caja.x1;
console.log('nombre        ' + NOMBRE + '  (' + NOMBRE.length + ' letras)');
console.log('cuerpo        ' + cuerpo.toFixed(1) + ' px   espaciado ' + (cuerpo * RATIO_ESP).toFixed(2) + ' px');
console.log('tinta         x ' + caja.x0 + '..' + caja.x1 + '   y ' + caja.y0 + '..' + caja.y1);
console.log('margen dcho   ' + (A - 1 - caja.x1) + ' px  (el diseno pide ' + MARGEN_DCHO + ')');

if (holgura > HOLGURA) {
  console.error('DEMASIADO PEQUENO: sobran ' + holgura + ' px a la derecha, el nombre baila en el hueco.');
  await nav.close();
  process.exit(1);
}
if (caja.y0 < 8 || caja.y1 > ALTO - 9) {
  console.error('SE SALE POR ARRIBA O POR ABAJO: y ' + caja.y0 + '..' + caja.y1);
  await nav.close();
  process.exit(1);
}

/* Solo ahora, con todo comprobado, se escribe. */
const maestro = svg(cuerpo, false);
const conFondo = (await rendir(svg(cuerpo, true))).png;
await nav.close();

const salida = [
  ['villuminations-logo-ancho.svg', Buffer.from(maestro, 'utf8')],
  ['villuminations-logo-ancho.png', mejor.png],
  ['villuminations-logo-ancho-fondo.png', conFondo],
];
for (const [nom, dato] of salida) fs.writeFileSync(path.join(SALIDA, nom), dato);
console.log('\nescritos:');
for (const [nom, dato] of salida) console.log('  marca/' + nom + '  ' + (dato.length / 1024).toFixed(0) + ' KB');

/* ---------------------------------------------------------------------------
   LA TARJETA PARA COMPARTIR (1200x630).
   ---------------------------------------------------------------------------
   La que habia decia, horneado dentro del PNG, "Equipo, ropa y suplementos
   para quienes entrenan en serio". En castellano. Y una imagen de Shopify es
   UNA sola para las cinco lenguas: no hay version francesa del archivo. Asi
   que cada vez que alguien pegaba el enlace de la tienda en WhatsApp desde
   Francia, Alemania o Japon, la tarjeta le hablaba en castellano. Es la misma
   leccion que ya obligo a rehacer las portadas del Diario y las de coleccion.

   Aqui no se escribe ni una frase traducible. Solo el distintivo, el nombre
   -- que es un nombre propio -- y el dominio, que se lee igual en los cinco
   idiomas. Lo que distingue la tarjeta es la luz, no las palabras.

   LA CAJA SEGURA. WhatsApp, X y Discord recortan la tarjeta por los bordes y
   cada uno de una manera. Todo lo que hay que leer vive dentro del 82 %
   central; fuera solo va el fondo y los halos, que se pueden cortar.        */

const TA = 1200, TALTO = 630;
const CAJA = { x0: Math.round(TA * 0.09), x1: Math.round(TA * 0.91),
               y0: Math.round(TALTO * 0.09), y1: Math.round(TALTO * 0.91) };

function tarjeta(cuerpo, dx) {
  const esp = (cuerpo * RATIO_ESP).toFixed(2);
  const corre = dx ? ` transform="translate(${dx.toFixed(1)},0)"` : '';
  const cy = 258;                    // el distintivo y el nombre, centrados
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${TA}" height="${TALTO}" viewBox="0 0 ${TA} ${TALTO}">
<defs>
  <style>@font-face{font-family:Orbitron;font-weight:400 900;src:url(data:font/woff2;base64,${fuente}) format('woff2')}</style>
  <radialGradient id="fondo" cx="50%" cy="42%" r="78%">
    <stop offset="0%" stop-color="#111233"/><stop offset="60%" stop-color="#08081a"/>
    <stop offset="100%" stop-color="#05050f"/>
  </radialGradient>
  <linearGradient id="ga" gradientUnits="userSpaceOnUse" x1="180" y1="180" x2="420" y2="420">
    <stop offset="0%" stop-color="#00d4ff"/><stop offset="45%" stop-color="#7b2fff"/><stop offset="100%" stop-color="#ff2ecb"/>
  </linearGradient>
  <linearGradient id="gvi" gradientUnits="userSpaceOnUse" x1="228" y1="180" x2="372" y2="420">
    <stop offset="0%" stop-color="#7df3ff"/><stop offset="50%" stop-color="#00d4ff"/><stop offset="100%" stop-color="#7b2fff"/>
  </linearGradient>
  <linearGradient id="gt" gradientUnits="userSpaceOnUse" x1="${CAJA.x0}" y1="0" x2="${CAJA.x1}" y2="0">
    <stop offset="0%" stop-color="#7df3ff"/><stop offset="35%" stop-color="#00d4ff"/>
    <stop offset="78%" stop-color="#7b2fff"/><stop offset="100%" stop-color="#ff2ecb"/>
  </linearGradient>
  <filter id="glow" x="-25%" y="-90%" width="150%" height="280%">
    <feGaussianBlur stdDeviation="7.0" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="rejilla" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M48 0H0V48" fill="none" stroke="#00b4ff" stroke-width="1" opacity="0.05"/>
  </pattern>
</defs>
<rect width="${TA}" height="${TALTO}" fill="url(#fondo)"/>
<rect width="${TA}" height="${TALTO}" fill="url(#rejilla)"/>
<g${corre}>
<circle cx="300" cy="${cy}" r="108" fill="none" stroke="url(#ga)" stroke-width="11.6"
        stroke-dasharray="22.0 15.9" stroke-linecap="round" filter="url(#glow)"/>
<text x="300" y="${cy + 6}" fill="url(#gvi)" filter="url(#glow)" font-family="Orbitron, sans-serif"
      font-weight="900" font-size="110" text-anchor="middle" dominant-baseline="central">VI</text>
<text x="452" y="${cy + 6}" fill="url(#gt)" filter="url(#glow)" font-family="Orbitron, sans-serif"
      font-weight="900" font-size="${cuerpo.toFixed(1)}" letter-spacing="${esp}" dominant-baseline="central">${NOMBRE}</text>
</g>
<text x="${TA / 2}" y="470" fill="#9aa0c4" font-family="Orbitron, sans-serif" font-weight="500"
      font-size="30" letter-spacing="5.4" text-anchor="middle" dominant-baseline="central">villuminations.com</text>
</svg>`;
}

const nav2 = await chromium.launch({ executablePath: CHROME });
const pg2 = await (await nav2.newContext({ viewport: { width: TA, height: TALTO }, deviceScaleFactor: 1 })).newPage();

async function rendirTarjeta(fuenteSvg) {
  const b64 = Buffer.from(fuenteSvg, 'utf8').toString('base64');
  await pg2.setContent(
    `<style>html,body{margin:0;padding:0}img{display:block}</style>` +
    `<img id="i" width="${TA}" height="${TALTO}" src="data:image/svg+xml;base64,${b64}">`);
  await pg2.locator('#i').evaluate((im) => im.complete || im.decode());
  const png = await pg2.screenshot({ clip: { x: 0, y: 0, width: TA, height: TALTO } });
  /* Aqui la tinta se mide contra el fondo oscuro: cuenta el pixel que brilla
     bastante mas que el fondo, no el que simplemente es opaco. */
  const caja = await pg2.evaluate(async (b64) => {
    const im = new Image(); im.src = 'data:image/svg+xml;base64,' + b64; await im.decode();
    const c = document.createElement('canvas'); c.width = 1200; c.height = 630;
    const x = c.getContext('2d'); x.drawImage(im, 0, 0, 1200, 630);
    const d = x.getImageData(0, 0, 1200, 630).data;
    let x0 = 1e9, x1 = -1, y0 = 1e9, y1 = -1;
    for (let y = 0; y < 630; y++) for (let X = 0; X < 1200; X++) {
      const k = (y * 1200 + X) * 4;
      if (d[k] + d[k + 1] + d[k + 2] < 200) continue;   // el fondo no llega ahi
      if (X < x0) x0 = X; if (X > x1) x1 = X; if (y < y0) y0 = y; if (y > y1) y1 = y;
    }
    return { x0, x1, y0, y1 };
  }, b64);
  return { png, caja };
}

let tj = null;
for (let cuerpo = 92; cuerpo >= 48; cuerpo -= 0.5) {
  const r = await rendirTarjeta(tarjeta(cuerpo, 0));
  if (r.caja.x1 <= CAJA.x1) { tj = { cuerpo, ...r }; break; }
}

/* CENTRAR ES UNA MEDIDA, NO UN NUMERO A OJO. El distintivo, el aro y el
   nombre no ocupan lo que dice el marcado: el resplandor se sale por los dos
   lados y no por igual. Asi que se mide la tinta de verdad, se calcula lo que
   sobra a cada lado y se corre el conjunto esa diferencia. La primera version
   dejaba 185 px a la izquierda y 108 a la derecha -- 77 px de desequilibrio
   que en una tarjeta de enlace se ven enseguida. */
if (tj) {
  const ancho = tj.caja.x1 - tj.caja.x0;
  const dx = Math.round((TA - ancho) / 2 - tj.caja.x0);
  if (dx !== 0) {
    const r = await rendirTarjeta(tarjeta(tj.cuerpo, dx));
    const izq = r.caja.x0, der = TA - 1 - r.caja.x1;
    if (Math.abs(izq - der) <= 4) tj = { cuerpo: tj.cuerpo, dx, ...r };
    else console.error('AVISO: el centrado no cuadro (izq ' + izq + ', dcha ' + der + '), se deja sin correr.');
  }
}
await nav2.close();

if (!tj) { console.error('TARJETA: el nombre no cabe en la caja segura.'); process.exit(1); }
if (tj.caja.x0 < CAJA.x0 || tj.caja.y0 < CAJA.y0 || tj.caja.y1 > CAJA.y1) {
  console.error('TARJETA: algo se sale de la caja segura. tinta x ' + tj.caja.x0 + '..' + tj.caja.x1 +
                '  y ' + tj.caja.y0 + '..' + tj.caja.y1 +
                '   caja x ' + CAJA.x0 + '..' + CAJA.x1 + '  y ' + CAJA.y0 + '..' + CAJA.y1);
  process.exit(1);
}

fs.writeFileSync(path.join(SALIDA, 'villuminations-compartir.png'), tj.png);
console.log('\ntarjeta para compartir  cuerpo ' + tj.cuerpo.toFixed(1) + '  corrida ' + (tj.dx || 0) + ' px' +
            '  margenes izq ' + tj.caja.x0 + ' / dcha ' + (TA - 1 - tj.caja.x1) +
            '  tinta x ' + tj.caja.x0 + '..' + tj.caja.x1 + '  y ' + tj.caja.y0 + '..' + tj.caja.y1 +
            '  (caja x ' + CAJA.x0 + '..' + CAJA.x1 + '  y ' + CAJA.y0 + '..' + CAJA.y1 + ')');
console.log('  marca/villuminations-compartir.png  ' + (tj.png.length / 1024).toFixed(0) + ' KB');
