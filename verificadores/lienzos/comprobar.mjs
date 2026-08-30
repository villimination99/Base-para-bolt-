/* Comprueba en un navegador real los tres lienzos animados del tema.
   Nacio de un fallo que la lectura del codigo no vio: al poner un limite de
   fotogramas a los haces, el limitador se aplicaba tambien al PRIMER dibujo.
   Con movimiento reducido no hay nadie que reprograme, asi que el lienzo se
   quedaba vacio para siempre. Solo se ve midiendo pixeles de verdad.

   Uso:  node verificadores/lienzos/comprobar.mjs                            */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const CABEZA = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:0;background:#000;color:#fff;font-family:system-ui}
.hero-shader{position:relative;height:100svh;overflow:hidden}
.hero-shader canvas{position:absolute;inset:0;width:100%;height:100%}
.haces{min-height:100svh;position:relative;overflow:hidden}
.haces canvas,.haces-lienzo{position:absolute;inset:0;width:100%;height:100%;filter:blur(4px)}
.relleno{height:120vh}</style></head><body>`;

const PAGINA = CABEZA + `
<section class="hero-shader"><canvas data-hero-shader data-scale="125" data-thickness="30" data-grain="40"></canvas></section>
<div class="relleno"></div>
<section class="haces"><canvas data-haces class="haces-lienzo"></canvas></section>
<div class="relleno"></div>
</body></html>`;

// La pagina se escribe en disco: addInitScript solo se aplica al navegar a
// una URL, no con setContent, y la sonda de dibujos la necesita.
const TMP = path.join(AQUI, '.pagina-de-prueba.html');
fs.writeFileSync(TMP, PAGINA);
const URL_PRUEBA = 'file://' + TMP;

const navegador = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=swiftshader'] });
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

/* Cuenta pixeles encendidos de verdad, no clases CSS: "is-live" solo dice que
   el modulo arranco, no que haya pintado algo. */
const pintado = async (p, sel) => p.evaluate(s => {
  const c = document.querySelector(s);
  if (!c || !c.width) return { existe: false };
  const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;
  let n = 0;
  for (let i = 0; i < d.length; i += 4) if (d[i] + d[i + 1] + d[i + 2] > 0) n++;
  return { existe: true, encendidos: n, total: c.width * c.height, w: c.width, h: c.height };
}, sel);

async function abrir(opts) {
  const ctx = await navegador.newContext(opts);
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(URL_PRUEBA);
  for (const f of ['hero-shader.js', 'haces.js'])
    await p.addScriptTag({ path: path.join(ASSETS, f) });
  await p.waitForTimeout(1400);
  return { ctx, p, errs };
}

/* 1 — Los haces pintan en movimiento normal Y en movimiento reducido. */
for (const reducido of [false, true]) {
  const { ctx, p, errs } = await abrir({
    viewport: { width: 1280, height: 800 },
    reducedMotion: reducido ? 'reduce' : 'no-preference',
  });
  await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.5));
  await p.waitForTimeout(900);
  const r = await pintado(p, '[data-haces]');
  const etq = reducido ? 'movimiento reducido' : 'movimiento normal';
  decir(r.existe && r.encendidos > r.total * 0.05,
    `Los haces pintan con ${etq} (${r.existe ? Math.round(100 * r.encendidos / r.total) : 0} % del lienzo encendido)`);
  decir(errs.length === 0, `Sin errores de JavaScript con ${etq}${errs.length ? ': ' + errs[0] : ''}`);
  await ctx.close();
}

/* 2 — Cada lienzo se para al salir de pantalla y se reanuda al volver.
   Un bucle que sigue corriendo fuera de la vista es bateria robada. */
{
  const ctx = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.addInitScript(() => {
    window.__c = { gl: 0, d2: 0 };
    const dp = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (t, o) {
      const c = dp.call(this, t, o);
      if (!c) return c;
      if (t === 'webgl' || t === 'webgl2' || t === 'experimental-webgl') {
        const f = c.drawArrays.bind(c);
        c.drawArrays = function () { window.__c.gl++; return f.apply(null, arguments); };
      } else if (t === '2d' && this.hasAttribute('data-haces')) {
        // fill(), no fillRect(): los haces son poligonos con degradado.
        const f = c.fill.bind(c);
        c.fill = function () { window.__c.d2++; return f.apply(null, arguments); };
      }
      return c;
    };
  });
  await p.goto(URL_PRUEBA);
  for (const f of ['hero-shader.js', 'haces.js'])
    await p.addScriptTag({ path: path.join(ASSETS, f) });
  await p.waitForTimeout(1500);

  const ventana = async () => {
    await p.evaluate(() => { window.__c.gl = 0; window.__c.d2 = 0; });
    await p.waitForTimeout(1600);
    return p.evaluate(() => window.__c);
  };
  const arriba = await ventana();
  // A la seccion de haces, no al final del documento: detras hay relleno y
  // desde ahi los haces tampoco se ven (la primera version fallaba por esto).
  await p.evaluate(() => document.querySelector('.haces').scrollIntoView({ block: 'center' }));
  await p.waitForTimeout(1000);
  const abajo = await ventana();
  await p.evaluate(() => window.scrollTo(0, 0));
  await p.waitForTimeout(1000);
  const vuelta = await ventana();

  decir(arriba.gl > 0, `El hero dibuja cuando se ve (${arriba.gl} en 1,6 s)`);
  decir(abajo.gl === 0, `El hero se para al salir de pantalla (${abajo.gl} dibujos fuera de la vista)`);
  decir(vuelta.gl > 0, `El hero se reanuda al volver (${vuelta.gl})`);
  decir(arriba.d2 === 0, `Los haces se paran fuera de pantalla (${arriba.d2} dibujos)`);
  decir(abajo.d2 > 0, `Los haces dibujan cuando se ven (${abajo.d2} en 1,6 s)`);
  await ctx.close();
}

/* 3 — En un equipo flojo el lienzo de los haces se reduce; en uno capaz, no.
   Sin esto, un movil de gama baja se quedaba en 17 fps. */
{
  const medidas = {};
  for (const nucleos of [8, 4]) {
    const ctx = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 3 });
    const p = await ctx.newPage();
    const cdp = await ctx.newCDPSession(p);
    await cdp.send('Emulation.setHardwareConcurrencyOverride', { hardwareConcurrency: nucleos });
    await p.goto(URL_PRUEBA);
    await p.addScriptTag({ path: path.join(ASSETS, 'haces.js') });
    await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.5));
    await p.waitForTimeout(1200);
    medidas[nucleos] = await p.evaluate(() => {
      const c = document.querySelector('[data-haces]');
      return { w: c.width, h: c.height };
    });
    await ctx.close();
  }
  decir(medidas[8].w > medidas[4].w,
    `El lienzo se reduce en equipos flojos (8 nucleos: ${medidas[8].w}x${medidas[8].h} · 4 nucleos: ${medidas[4].w}x${medidas[4].h})`);
  decir(medidas[8].w <= 390 * 1.01,
    `En un equipo capaz no se pasa de 1x pese a un devicePixelRatio de 3 (${medidas[8].w} px)`);
}

await navegador.close();
fs.unlinkSync(TMP);
console.log('');
console.log(fallos === 0 ? 'Los lienzos animados pintan, se paran y se adaptan.' : `${fallos} problema(s) en los lienzos.`);
process.exit(fallos === 0 ? 0 : 1);
