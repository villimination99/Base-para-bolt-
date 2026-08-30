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
<section class="hero-shader"><canvas data-hero-shader data-scale="1.25" data-thickness="0.30" data-grain="0.40"></canvas></section>
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

/* 4 — El marco del hero se cierra en CUALQUIER formato de pantalla.
   La caja estaba fija en 0.82 x 0.47 sobre un espacio normalizado por el lado
   corto: en vertical el eje X solo llegaba a ±0.62, asi que los dos lados
   quedaban fuera de pantalla y el visitante veia una sola barra horizontal en
   vez de un marco. Pasaba en iPhone y en iPad. Se mide sobre la captura, no
   con readPixels: sin preserveDrawingBuffer el buffer se vacia al componer y
   readPixels devuelve ceros (primera version de esta prueba, que mintio). */
{
  const analizar = async (p) => {
    const b64 = (await p.locator('.hero-shader').screenshot()).toString('base64');
    return p.evaluate(async (s) => {
      const img = new Image(); img.src = 'data:image/png;base64,' + s; await img.decode();
      const c = document.createElement('canvas'); c.width = img.width; c.height = img.height;
      const g = c.getContext('2d'); g.drawImage(img, 0, 0);
      const d = g.getImageData(0, 0, img.width, img.height).data;
      const W = img.width, H = img.height;
      const br = (x, y) => { const i = (y * W + x) * 4; return d[i] + d[i + 1] + d[i + 2]; };
      // El hero lleva grano fuerte. Ni el maximo ni la media de una columna
      // sirven: con el maximo, un solo pixel de ruido ya pasaba la prueba
      // aunque el marco estuviera roto; con la media, la linea de 3 px se
      // pierde entre 844 px de ruido. Se promedia en bloques de 8x8, que
      // deja el ruido en una constante y conserva la linea.
      const B = 8, w = Math.floor(W / B), h = Math.floor(H / B);
      const mapa = new Float32Array(w * h);
      for (let by = 0; by < h; by++) for (let bx = 0; bx < w; bx++) {
        let s2 = 0;
        for (let y = 0; y < B; y++) for (let x = 0; x < B; x++) s2 += br(bx * B + x, by * B + y);
        mapa[by * w + bx] = s2 / (B * B);
      }
      const colMax = fx => { const bx = Math.round(w * fx); let m = 0;
        for (let by = 0; by < h; by++) m = Math.max(m, mapa[by * w + bx]); return m; };
      const filMax = fy => { const by = Math.round(h * fy); let m = 0;
        for (let bx = 0; bx < w; bx++) m = Math.max(m, mapa[by * w + bx]); return m; };
      // Control: el centro del cuadro, por dentro del marco, donde no hay linea
      let ctrl = 0, nc = 0;
      for (let by = Math.round(h * 0.42); by < Math.round(h * 0.58); by++)
        for (let bx = Math.round(w * 0.42); bx < Math.round(w * 0.58); bx++) { ctrl += mapa[by * w + bx]; nc++; }
      return { izq: colMax(0.10), der: colMax(0.90), arr: filMax(0.10), aba: filMax(0.90), ctrl: ctrl / nc };
    }, b64);
  };
  for (const [n, w, h] of [['movil vertical', 390, 844], ['tableta vertical', 820, 1180], ['escritorio', 1440, 800]]) {
    const ctx = await navegador.newContext({ viewport: { width: w, height: h }, isMobile: w < 500, hasTouch: w < 500 });
    const p = await ctx.newPage();
    await p.goto(URL_PRUEBA);
    await p.addScriptTag({ path: path.join(ASSETS, 'hero-shader.js') });
    await p.waitForTimeout(1600);
    const r = await analizar(p);
    // Un carril tenue siempre encendido: sin el, palette(0) devuelve el propio
    // color de fondo y el marco se lee como roto donde no pasa el pulso.
    // El criterio es RELATIVO: los cuatro lados tienen que brillar
    // claramente mas que el interior. Un umbral absoluto lo cumplia el grano.
    const ctrl = Math.max(r.ctrl, 1);
    const lados = [r.izq, r.der, r.arr, r.aba];
    const peor = Math.min.apply(null, lados) / ctrl;
    // Umbral calibrado midiendo el shader ANTIGUO, no elegido a ojo:
    // con la caja fija daba entre 1.25 y 1.45 (solo se veia una barra);
    // con la caja adaptada da entre 2.08 y 6.67. 1.70 separa los dos casos
    // con margen por los dos lados.
    const cerrado = peor > 1.70;
    const f = v => v.toFixed(0);
    decir(cerrado, `El marco del hero se cierra en ${n} (lados ${lados.map(f).join('/')} contra ${f(ctrl)} de control = x${peor.toFixed(2)})`);
    await ctx.close();
  }
}

await navegador.close();
fs.unlinkSync(TMP);
console.log('');
console.log(fallos === 0 ? 'Los lienzos animados pintan, se paran y se adaptan.' : `${fallos} problema(s) en los lienzos.`);
process.exit(fallos === 0 ? 0 : 1);
