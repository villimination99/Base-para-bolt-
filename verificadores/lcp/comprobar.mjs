/* CUANTO TARDA EN PINTARSE LO MAS GRANDE DE LA PORTADA (LCP).
   ------------------------------------------------------------------
   Nace de un dato de campo, no de una sospecha: el panel de Shopify daba
   LCP P75 = 4329 ms, "mediocre", subiendo un 316 %. Google considera bueno
   por debajo de 2500 ms y malo por encima de 4000.

   Aqui se monta la portada como la sirve la tienda -- el layout con sus
   secciones -- y se mide el LCP con la misma API que usa el navegador para
   informar a Google (PerformanceObserver sobre 'largest-contentful-paint').
   Se mide DOS veces: con la intro y sin ella, para saber cuanto de la espera
   es suya. Un numero sin su comparacion no dice que hacer.

   Uso:  node verificadores/lcp/comprobar.mjs                              */
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';
import { e, prepararFuente, ctxBase, contextoDeSeccion, T } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const TEMA = path.isAbsolute(T) ? T : path.join(RAIZ, T);
const TMP = fs.mkdtempSync('/tmp/lcp-');
const TIPO = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

fs.mkdirSync(path.join(TMP, 'assets'), { recursive: true });
for (const a of fs.readdirSync(path.join(TEMA, 'assets'))) fs.copyFileSync(path.join(TEMA, 'assets', a), path.join(TMP, 'assets', a));

/* --- Las secciones de la portada, en su orden real --- */
const index = JSON.parse(fs.readFileSync(path.join(TEMA, 'templates/index.json'), 'utf8'));
let cuerpo = '';
for (const id of index.order) {
  const tipo = index.sections[id].type;
  const ruta = path.join(TEMA, 'sections', tipo + '.liquid');
  if (!fs.existsSync(ruta)) continue;
  const src = fs.readFileSync(ruta, 'utf8');
  try {
    const { ctx } = contextoDeSeccion(tipo, src);
    /* Los ajustes guardados en la plantilla mandan sobre los del esquema, que
       es lo que hace Shopify. Sin esto se mediria una portada que no existe. */
    Object.assign(ctx.section.settings, index.sections[id].settings || {});
    if (index.sections[id].blocks) {
      ctx.section.blocks = Object.entries(index.sections[id].blocks).map(([k, b]) => ({
        id: k, type: b.type, settings: b.settings || {}, shopify_attributes: ''
      }));
    }
    e.options.globals = ctx;
    cuerpo += await e.parseAndRender(prepararFuente(src), ctx);
  } catch (err) {
    console.log(`  (la seccion ${tipo} no se pudo montar: ${String(err.message).slice(0, 60)})`);
  }
}

/* --- La intro, aparte, para poder medir con y sin --- */
const splashSrc = fs.readFileSync(path.join(TEMA, 'snippets/splash-intro.liquid'), 'utf8');
const guardados = JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_data.json'), 'utf8')).current;
async function montarSplash(duracion) {
  const ctxS = JSON.parse(JSON.stringify(ctxBase));
  ctxS.settings = Object.assign({}, ctxBase.settings, guardados, { splash_duracion: duracion });
  e.options.globals = ctxS;
  return (await e.parseAndRender(prepararFuente(splashSrc), ctxS))
    .replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1')
    .replace(/<img[^>]*>/g, '');   // la foto de fondo vive en el CDN, aqui no se alcanza
}
const splashCompleta = await montarSplash('completa');
const splashCorta = await montarSplash('corta');

cuerpo = cuerpo.replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');

const css = '<link rel="stylesheet" href="/assets/villumination.css">';
const pagina = (intro) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>VILLUMINATION</title>${css}
<style>body{margin:0;background:#0A0A0A;color:#eee;font-family:system-ui}</style></head><body>
${intro}
<main>${cuerpo}</main>
<script src="/assets/base.js" defer></script>
</body></html>`;

fs.writeFileSync(path.join(TMP, 'completa.html'), pagina(splashCompleta));
fs.writeFileSync(path.join(TMP, 'corta.html'), pagina(splashCorta));
fs.writeFileSync(path.join(TMP, 'sin.html'), pagina(''));

const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  const f = path.join(TMP, u.replace(/^\//, ''));
  fs.readFile(f, (err, d) => {
    if (err) { res.writeHead(404); res.end('no ' + u); return; }
    res.writeHead(200, { 'content-type': TIPO[path.extname(f)] || 'application/octet-stream' });
    res.end(d);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });

async function medir(archivo) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.addInitScript(() => {
    window.__lcp = 0; window.__lcpQue = '';
    new PerformanceObserver((l) => {
      for (const x of l.getEntries()) { window.__lcp = x.startTime; window.__lcpQue = (x.element && (x.element.tagName + '.' + (x.element.className || '').toString().slice(0, 40))) || x.url || '?'; }
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  });
  await p.goto(base + archivo, { waitUntil: 'load' });
  await p.waitForTimeout(7000);           // mas que la intro entera
  const r = await p.evaluate(() => ({ lcp: Math.round(window.__lcp), que: window.__lcpQue }));
  await ctx.close();
  return r;
}

const completa = await medir('completa.html');
const corta = await medir('corta.html');
const sin = await medir('sin.html');
const con = completa;

console.log('');
console.log(`  intro completa:  ${String(completa.lcp).padStart(5)} ms   (lo mas grande: ${completa.que})`);
console.log(`  intro corta:     ${String(corta.lcp).padStart(5)} ms   (lo mas grande: ${corta.que})`);
console.log(`  sin intro:       ${String(sin.lcp).padStart(5)} ms   (lo mas grande: ${sin.que})`);
console.log(`  la intro completa cuesta ${completa.lcp - sin.lcp} ms; la corta, ${corta.lcp - sin.lcp} ms`);

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };

/* SE JUZGA LO QUE EL TEMA ENTREGA, no una variante cualquiera.

   La primera version media las tres y suspendia por la completa aunque el
   tema ya no la enviara: un verificador que se pone rojo por una opcion que
   nadie tiene puesta ensena a ignorarlo. Asi que el umbral se aplica a la
   duracion guardada en settings_data.json -- lo que de verdad ve el visitante
   -- y de la otra se informa, porque es una decision de negocio con su precio
   escrito, no un fallo de codigo.

   Los umbrales son los de Google, no inventados: por debajo de 2500 ms es
   "bueno" y por encima de 4000 es "malo". */
const entregada = guardados.splash_duracion === 'corta' ? corta : completa;
const nombre = guardados.splash_duracion === 'corta' ? 'corta' : 'completa';
console.log(`  el tema entrega la intro ${nombre}`);
decir(entregada.lcp < 2500, `con lo que se entrega, lo mas grande se pinta en ${entregada.lcp} ms (bueno por debajo de 2500)`);
decir(sin.lcp < 2500, `y la portada sola, en ${sin.lcp} ms`);
decir(entregada.lcp - sin.lcp < 800, `la intro entregada anade ${entregada.lcp - sin.lcp} ms (limite 800)`);
console.log(`  (la otra opcion, la ${nombre === 'corta' ? 'completa' : 'corta'}, mediria ${nombre === 'corta' ? completa.lcp : corta.lcp} ms — su etiqueta en el editor lo dice)`);

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(fallos ? `\n  ${fallos} en rojo.\n` : '\nLa portada se pinta a tiempo.\n');
process.exit(fallos ? 1 : 0);
