/* Prueba de estres del hero WebGL.
   ------------------------------------------------------------------
   El usuario ya vio caerse la pagina al mover el hero deprisa en el editor.
   La causa era que un contexto WebGL perdido no se recuperaba nunca, porque
   sin preventDefault() en webglcontextlost el navegador no vuelve a emitir
   webglcontextrestored. Esta prueba reproduce las tres formas de tumbarlo:

     1. Desplazamiento violento: 60 saltos seguidos.
     2. Perdida y recuperacion forzadas del contexto (WEBGL_lose_context).
     3. Vaiven del editor: cargar y descargar la seccion 25 veces, que es lo
        que pasa al arrastrar los ajustes.

   En los tres casos el hero tiene que seguir dibujando al final.

   Uso:  node verificadores/lienzos/estres.mjs                              */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const TMP = path.join(AQUI, '.estres.html');
fs.writeFileSync(TMP, `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>html,body{margin:0;background:#000}
.hero-shader{position:relative;height:100svh;overflow:hidden}
.hero-shader canvas{position:absolute;inset:0;width:100%;height:100%}
.relleno{height:300vh}</style></head><body>
<section class="hero-shader"><canvas data-hero-shader data-scale="1.25" data-thickness="0.30" data-grain="0.20"></canvas></section>
<div class="relleno"></div></body></html>`);

const navegador = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=swiftshader'] });
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

const ctx = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
const p = await ctx.newPage();
const errs = [];
p.on('pageerror', e => errs.push(e.message));
p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });

// Cuenta dibujos reales, no clases CSS
await p.addInitScript(() => {
  window.__gl = 0;
  const dp = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (t, o) {
    const c = dp.call(this, t, o);
    if (c && (t === 'webgl' || t === 'webgl2' || t === 'experimental-webgl')) {
      const f = c.drawArrays.bind(c);
      c.drawArrays = function () { window.__gl++; return f.apply(null, arguments); };
      window.__ctx = c;
    }
    return c;
  };
});
await p.goto('file://' + TMP);
await p.addScriptTag({ path: path.join(ASSETS, 'hero-shader.js') });
await p.waitForTimeout(1500);

const dibuja = async (ms = 1200) => {
  await p.evaluate(() => { window.__gl = 0; });
  await p.waitForTimeout(ms);
  return p.evaluate(() => window.__gl);
};

console.log('');
decir(await dibuja() > 0, 'Dibuja al arrancar');

/* 1 — Desplazamiento violento */
for (let i = 0; i < 60; i++) {
  await p.evaluate(k => window.scrollTo(0, (k % 2) ? 0 : 1400 + k * 7), i);
}
await p.evaluate(() => window.scrollTo(0, 0));
await p.waitForTimeout(700);
decir(await dibuja() > 0, 'Sigue dibujando tras 60 saltos de desplazamiento');

/* 2 — Perdida y recuperacion forzadas del contexto */
const perdido = await p.evaluate(() => {
  const c = document.querySelector('[data-hero-shader]');
  const gl = window.__ctx;
  if (!gl) return 'sin contexto';
  const ext = gl.getExtension('WEBGL_lose_context');
  if (!ext) return 'sin extension';
  ext.loseContext();
  setTimeout(() => ext.restoreContext(), 300);
  return 'ok';
});
if (perdido !== 'ok') {
  decir(false, `No se pudo forzar la perdida de contexto (${perdido})`);
} else {
  await p.waitForTimeout(1800);
  decir(await dibuja() > 0, 'Se recupera tras perder y restaurar el contexto WebGL');
}

/* 3 — Vaiven del editor */
/* El HTML se captura SIN la marca de inicializado. init() pone
   data-vinit-shader en el lienzo para no arrancar dos veces sobre el mismo
   nodo, y al clonar el HTML ya marcado cada copia nueva llegaba marcada y se
   saltaba: la prueba acusaba al tema de un fallo que era de la prueba.
   Shopify vuelve a renderizar la seccion desde Liquid, asi que el marcado que
   llega al editor NO tiene esa marca; esto lo reproduce fielmente. */
const html = (await p.evaluate(() => document.querySelector('.hero-shader').outerHTML))
  .replace(/\s*data-vinit-shader="1"/g, '');
const traiaMarca = (await p.evaluate(() => document.querySelector('[data-hero-shader]').hasAttribute('data-vinit-shader')));
decir(traiaMarca, 'init marca el lienzo para no arrancar dos veces sobre el mismo nodo');
for (let i = 0; i < 25; i++) {
  await p.evaluate(h => {
    const vieja = document.querySelector('.hero-shader');
    const ev = new CustomEvent('shopify:section:unload');
    Object.defineProperty(ev, 'target', { value: vieja });
    document.dispatchEvent(ev);
    vieja.remove();
    const d = document.createElement('div');
    d.innerHTML = h;
    const nueva = d.firstElementChild;
    document.body.insertBefore(nueva, document.body.firstChild);
    const ev2 = new CustomEvent('shopify:section:load');
    Object.defineProperty(ev2, 'target', { value: nueva });
    document.dispatchEvent(ev2);
  }, html);
}
await p.waitForTimeout(1500);
const n = await p.evaluate(() => document.querySelectorAll('.hero-shader').length);
decir(n === 1, `Tras 25 recargas de seccion queda una sola (hay ${n})`);
decir(await dibuja(1500) > 0, 'Sigue dibujando tras 25 recargas de seccion');

decir(errs.length === 0, `Sin errores de JavaScript en toda la prueba${errs.length ? ': ' + errs.slice(0, 2).join(' | ') : ''}`);

fs.unlinkSync(TMP);
await navegador.close();
console.log('');
console.log(fallos === 0 ? 'El hero aguanta el movimiento, la perdida de contexto y el editor.'
                         : `${fallos} problema(s) de estabilidad.`);
process.exit(fallos ? 1 : 0);
