/* Las superficies que el navegador pinta por su cuenta.
   ------------------------------------------------------------------
   Hay tres estados de la tienda que nadie mira nunca y en los que un
   tema oscuro con titulos recortados sobre degradados se rompe de
   formas que no se ven en el navegador de todos los dias:

     1. Windows en alto contraste. El sistema borra fondos y sombras.
        Un titulo con -webkit-text-fill-color:transparent recortado
        sobre un degradado se queda transparente sobre nada: invisible.
     2. La impresion. El mismo titulo sale en blanco sobre blanco, y el
        resto de la pagina intenta imprimir un fondo negro entero.
     3. Las superficies del propio navegador -- la seleccion de texto,
        el cursor de escritura, las casillas, el relleno automatico --
        que vienen con los azules de fabrica y desentonan.

   Esto no se puede comprobar leyendo el CSS: hay que pedirle al motor
   que emule cada modo y leer el color calculado que sale.

   Uso:  node verificadores/superficies/comprobar.mjs                  */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = process.env.TEMA ? path.join(process.env.TEMA, 'assets') : path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const CSS = fs.readFileSync(path.join(ASSETS, 'villumination.css'), 'utf8');

/* Los titulos que van recortados sobre un degradado. Son los que
   desaparecen si nadie les devuelve tinta. */
const TITULOS = [
  ['h1', 'splash-mono', 'VILLUMINATION'],
  ['h1', 'splash-title', 'Villumination 3D'],
  ['h2', 'section-title', 'Los ocho Codices'],
  ['h1', 'product-title', 'Creatina con electrolitos'],
  ['h1', 'vip-title', 'VI.P'],
  ['div', 'error-404-code', '404'],
  ['span', 'nav-brand-grad', 'VILLUMINATION'],
  ['h2', 'haces-titulo', 'Haces de luz'],
];

const HTML = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>${CSS}</style></head>
<body class="grid-bg">
  <nav class="navbar"><div class="navbar-inner"><span class="nav-brand"><span class="nav-brand-grad">VILLUMINATION</span></span></div></nav>
  <main class="container">
    ${TITULOS.map(([t, c, txt]) => `<${t} class="${c}" id="t-${c}">${txt}</${t}>`).join('\n    ')}
    <div class="rte"><p>Un parrafo del texto rico con <a href="https://villuminations.com/blogs/diario/creatina">un enlace</a> dentro.</p>
      <ul><li>Una viñeta</li><li>Otra viñeta</li></ul></div>
    <form><input type="text" id="campo" placeholder="Tu correo"><input type="checkbox" id="casilla">
      <input type="search" id="buscar" placeholder="Buscar"></form>
    <article class="product-card" id="tarjeta"><h3>Producto</h3></article>
  </main>
</body></html>`;

const tmp = path.join(AQUI, '.superficies.html');
fs.writeFileSync(tmp, HTML);

const navegador = await chromium.launch({ executablePath: CHROME });
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

/* rgb(a) -> [r,g,b,a]. "transparent" llega como rgba(0,0,0,0). */
function rgb(v) {
  const m = String(v).match(/-?[\d.]+/g);
  if (!m) return null;
  return [+m[0], +m[1], +m[2], m.length > 3 ? +m[3] : 1];
}
const opaco = v => { const c = rgb(v); return !!c && c[3] > 0.05; };
const luz = v => { const c = rgb(v); return c ? (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255 : null; };

/* El color con el que el texto se pinta de verdad: si hay
   -webkit-text-fill-color, ese gana sobre color. */
const LEER = `(sel) => {
  const e = document.querySelector(sel);
  if (!e) return null;
  const s = getComputedStyle(e);
  return { fill: s.webkitTextFillColor || s.color, color: s.color,
           bg: s.backgroundImage, bgc: s.backgroundColor };
}`;

console.log('');

/* ---------- 1. Windows en alto contraste ---------- */
{
  const ctx = await navegador.newContext({ forcedColors: 'active', colorScheme: 'light' });
  const p = await ctx.newPage();
  await p.goto('file://' + tmp);
  console.log('--- Windows en alto contraste ---');
  for (const [, clase, txt] of TITULOS) {
    const r = await p.evaluate(eval(LEER), '#t-' + clase);
    decir(r && opaco(r.fill), `${clase.padEnd(16)} sigue teniendo tinta ("${txt}")`);
  }
  const foco = await p.evaluate(() => {
    const b = document.createElement('button'); b.textContent = 'x'; document.body.appendChild(b); b.focus();
    return getComputedStyle(b, null).outlineStyle;
  });
  decir(foco !== 'none', `el anillo de foco no desaparece (outline-style: ${foco})`);
  await ctx.close();
}

/* ---------- 2. La impresion ---------- */
{
  const ctx = await navegador.newContext();
  const p = await ctx.newPage();
  await p.goto('file://' + tmp);
  await p.emulateMedia({ media: 'print' });
  console.log('');
  console.log('--- Al imprimir ---');
  const fondo = await p.evaluate(() => getComputedStyle(document.body).backgroundColor);
  decir(luz(fondo) > 0.8, `el papel sale blanco y no negro (${fondo})`);
  for (const [, clase, txt] of TITULOS) {
    const r = await p.evaluate(eval(LEER), '#t-' + clase);
    const claro = r && luz(r.fill) !== null && luz(r.fill) < 0.45;
    decir(r && opaco(r.fill) && claro, `${clase.padEnd(16)} se imprime en tinta oscura ("${txt}")`);
  }
  const oculto = await p.evaluate(() => getComputedStyle(document.querySelector('.navbar')).display);
  decir(oculto === 'none', 'la barra de navegacion no gasta papel');
  const url = await p.evaluate(() => getComputedStyle(document.querySelector('.rte a'), '::after').content);
  decir(url.includes('villuminations.com'), 'los enlaces llevan su direccion al lado, que en papel es lo unico que queda');
  await ctx.close();
}

/* ---------- 3. Las superficies del navegador ---------- */
{
  const ctx = await navegador.newContext();
  const p = await ctx.newPage();
  await p.goto('file://' + tmp);
  console.log('');
  console.log('--- Lo que pinta el navegador ---');
  const r = await p.evaluate(() => {
    const raiz = getComputedStyle(document.documentElement);
    const campo = getComputedStyle(document.getElementById('campo'));
    const sel = getComputedStyle(document.body, '::selection');
    const viñeta = getComputedStyle(document.querySelector('.rte li'), '::marker');
    const enlace = getComputedStyle(document.querySelector('.rte a'));
    return {
      esquema: raiz.colorScheme,
      acento: raiz.accentColor,
      toque: raiz.webkitTapHighlightColor,
      ajuste: raiz.webkitTextSizeAdjust || raiz.textSizeAdjust,
      caret: campo.caretColor,
      selBg: sel.backgroundColor,
      marca: viñeta.color,
      subrayado: enlace.textUnderlineOffset,
      ancla: getComputedStyle(document.getElementById('t-vip-title')).scrollMarginTop,
    };
  });
  decir(r.esquema.includes('dark'), `el navegador sabe que pinta algo oscuro (color-scheme: ${r.esquema})`);
  decir(opaco(r.acento) && luz(r.acento) > 0.3, `las casillas y radios usan el cian de la casa (${r.acento})`);
  decir(opaco(r.toque), `al tocar en el movil el destello es de la marca (${r.toque})`);
  decir(r.ajuste === '100%', `Safari no agranda el texto al girar el telefono (${r.ajuste})`);
  decir(opaco(r.caret) && luz(r.caret) > 0.3, `el cursor de escritura se ve sobre fondo oscuro (${r.caret})`);
  decir(opaco(r.selBg), `la seleccion de texto no es el azul de fabrica (${r.selBg})`);
  decir(opaco(r.marca), `las viñetas del texto rico llevan color (${r.marca})`);
  decir(parseFloat(r.subrayado) > 0, `los subrayados no cruzan las colas de las letras (${r.subrayado})`);
  await ctx.close();
}

/* ---------- 4. El texto guia de los campos, contra su caja real ---------- */
{
  const ctx = await navegador.newContext();
  const p = await ctx.newPage();
  await p.goto('file://' + tmp);
  console.log('');
  console.log('--- El texto guia de los campos ---');
  /* Los campos de esta tienda se apoyan en tres tonos distintos. El texto
     guia tiene que llegar a 4.5:1 sobre el mas claro de los tres, que es el
     caso peor. Antes se quedaba en 4.12:1 sobre --dark-700 y nadie lo vio
     porque la bateria de contraste no mide placeholders. */
  const color = await p.evaluate(() => getComputedStyle(document.getElementById('campo'), '::placeholder').color);
  const FONDOS = [['--dark-950', '#060612'], ['--dark-900', '#0b0b1e'], ['--dark-800', '#101030'], ['--dark-700', '#1c1c40'], ['--dark-600', '#282858']];
  const lin = c => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
  const Lhex = h => { const n = parseInt(h.slice(1), 16); return 0.2126 * lin(n >> 16 & 255) + 0.7152 * lin(n >> 8 & 255) + 0.0722 * lin(n & 255); };
  const Lrgb = v => { const c = rgb(v); return 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]); };
  for (const [nombre, hex] of FONDOS) {
    const a = Lrgb(color), b = Lhex(hex);
    const r2 = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    decir(r2 >= 4.5, `${nombre.padEnd(11)} ${r2.toFixed(2)}:1  (minimo AA 4.5:1)`);
  }
  await ctx.close();
}

fs.unlinkSync(tmp);
await navegador.close();
console.log('');
console.log(fallos === 0
  ? 'La tienda se sostiene tambien en alto contraste, en papel y en las superficies que pinta el navegador.'
  : `${fallos} problema(s) en las superficies.`);
process.exit(fallos ? 1 : 0);
