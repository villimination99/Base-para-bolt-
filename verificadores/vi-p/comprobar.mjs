/* VI.P dentro de un tema, como lo sirve Shopify.
   ------------------------------------------------------------------
   Monta la seccion igual que la tienda: resuelve asset_url contra un
   /assets/ de verdad, la mete en una pagina con cabecera, <h1> y pie
   ajenos, y la abre en un navegador real con WebGL por software.

   Lo que cambio en la version 4.46.0 y por que importa: antes esta bateria
   llevaba un apano -- borraba la cadena "https://cdn.jsdelivr.net" de la
   seccion y del modulo -- porque el contenedor no tiene salida a jsdelivr y
   sin ese recorte no cargaba nada. Un apano asi es peligroso: la bateria
   probaba una version del hub que no era la que iba a la tienda. Ahora
   three.js y Chart.js viajan dentro de assets/, no hay nada que recortar, y
   en su lugar se comprueba lo contrario: que la pagina NO pide ni un solo
   archivo a un tercero. Si alguien vuelve a meter un CDN, esto se pone rojo.
*/
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const TMP = fs.mkdtempSync('/tmp/vi-p-');
const TIPO = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

/* ---- la seccion, renderizada a mano como lo haria Shopify ---- */
let sec = fs.readFileSync(path.join(T, 'sections/vi-p.liquid'), 'utf8')
  .replace(/\{%-?\s*comment\s*-?%\}[\s\S]*?\{%-?\s*endcomment\s*-?%\}/g, '')
  .replace(/\{%\s*schema\s*%\}[\s\S]*?\{%\s*endschema\s*%\}/g, '')
  .replace(/\{\{\s*'([^']+)'\s*\|\s*asset_url\s*\|\s*stylesheet_tag\s*\}\}/g, '<link rel="stylesheet" href="/assets/$1">')
  .replace(/\{\{\s*'([^']+)'\s*\|\s*asset_url\s*\}\}/g, '/assets/$1');

const quedaLiquid = sec.match(/\{[%{]/);
if (quedaLiquid) { console.error('  queda Liquid sin resolver cerca de: ' + sec.slice(Math.max(0, sec.indexOf(quedaLiquid[0]) - 60), sec.indexOf(quedaLiquid[0]) + 60)); process.exit(1); }

fs.mkdirSync(path.join(TMP, 'assets'), { recursive: true });
for (const a of fs.readdirSync(path.join(T, 'assets'))) fs.copyFileSync(path.join(T, 'assets', a), path.join(TMP, 'assets', a));

fs.writeFileSync(path.join(TMP, 'pagina.html'), `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:0;font-family:system-ui;background:#fff;color:#111}
header.tema{background:#fff;border-bottom:1px solid #e5e5e5;padding:14px 18px;font-weight:800}
h1.titulo-pagina{font-size:2rem;margin:24px 18px}
footer{background:#f6f6f6;color:#333;border-top:1px solid #e5e5e5;padding:28px 18px;text-align:left}
.carrito-flotante{position:fixed;right:16px;bottom:16px;width:56px;height:56px;border-radius:50%;background:#111;color:#fff;display:flex;align-items:center;justify-content:center;z-index:990}</style>
</head><body>
<header class="tema">MI TIENDA</header>
<main><h1 class="titulo-pagina">VI.P</h1>
${sec}
</main>
<footer id="pie-tema">Pie del tema</footer><div class="carrito-flotante">🛒</div>
</body></html>`);

/* ---- servidor estatico: solo sirve lo que hay, nada de mapeos ---- */
const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  const f = path.join(TMP, u === '/' ? 'pagina.html' : u.replace(/^\//, ''));
  fs.readFile(f, (e, d) => {
    if (e) { res.writeHead(404); res.end('no: ' + u); return; }
    res.writeHead(200, { 'content-type': TIPO[path.extname(f)] || 'application/octet-stream' });
    res.end(d);
  });
});
const url = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
const p = await ctx.newPage();
const errs = [], fallos = [], externas = [];
p.on('pageerror', e => errs.push(e.message));
p.on('requestfailed', r => fallos.push(r.url()));
p.on('request', r => { if (!r.url().startsWith(url) && !r.url().startsWith('data:') && !r.url().startsWith('blob:')) externas.push(r.url()); });
const pedidas = [];
p.on('request', r => pedidas.push(r.url()));
await p.goto(url, { waitUntil: 'load' });

/* --- Primero: lo pesado NO se ha bajado --- */
const pedido = n => pedidas.some(u => u.endsWith('/assets/' + n));
const antes = await p.evaluate(() => ({ mapa: !!window.__mm3dReady, chart: typeof window.Chart }));
const perezoso = !pedido('vi-p-3d.js') && !pedido('vi-p-chart.js') && !antes.mapa && antes.chart === 'undefined';

/* --- Y ahora, al acercarse, si --- */
await p.evaluate(() => document.getElementById('muscle-canvas').scrollIntoView());
await p.waitForFunction(() => window.__mm3dReady === true, { timeout: 90000 }).catch(() => {});
await p.evaluate(() => (document.getElementById('nutrition') || document.getElementById('macro-chart')).scrollIntoView());
await p.waitForFunction(() => typeof window.Chart === 'function', { timeout: 30000 }).catch(() => {});
await p.evaluate(() => window.scrollTo(0, 0));

/* --- Las animaciones de las secciones: que se REPARTAN y que ENTREN --- */
const anim = await p.evaluate(async () => {
  const raiz = document.getElementById('vill-hub');
  const marcados = raiz.querySelectorAll('.vp-ent').length;
  /* Se recorre la pagina entera despacio para que el observador dispare */
  for (let y = 0; y < document.body.scrollHeight; y += 500) {
    window.scrollTo(0, y);
    await new Promise(r => setTimeout(r, 45));
  }
  window.scrollTo(0, 0);
  /* Se espera a que las transiciones TERMINEN antes de contar los opacos.
     La primera version miraba a los 400 ms y daba 47 de 59: los doce que
     faltaban estaban a mitad de su propia transicion, que dura 620 ms mas
     hasta 320 de retardo escalonado. Medir una animacion antes de que acabe
     y llamarlo fallo es culpar al producto del cronometro. */
  const vistos = raiz.querySelectorAll('.vp-ent.vp-visto').length;
  const cuentaOpacos = () => {
    let k = 0;
    raiz.querySelectorAll('.vp-ent.vp-visto').forEach(e => {
      if (parseFloat(getComputedStyle(e).opacity) > 0.9) k++;
    });
    return k;
  };
  let opacos = 0;
  for (let intento = 0; intento < 24; intento++) {
    opacos = cuentaOpacos();
    if (opacos >= vistos) break;
    await new Promise(r => setTimeout(r, 150));
  }
  const cifras = [...raiz.querySelectorAll('.hero-stat strong')].map(e => e.textContent.trim());
  return { marcados, vistos, opacos, cifras };
});

const r = await p.evaluate(() => ({
  mapa3d: !!window.__mm3dReady,
  hubListo: !!window.__villReady,
  grafica: typeof window.Chart === 'function',
  hub: !!document.getElementById('vill-hub'),
  hubTerminaAntesDelPie: !document.getElementById('vill-hub').contains(document.getElementById('pie-tema')),
  h1: document.querySelectorAll('h1').length,
  footers: document.querySelectorAll('footer').length,
  pieFondo: getComputedStyle(document.getElementById('pie-tema')).backgroundColor,
  respaldoOculto: getComputedStyle(document.getElementById('mm-fallback')).display === 'none',
  ejercicios: document.querySelectorAll('#ex-grid .ex-card').length,
  frecuencias: document.querySelectorAll('#freq-grid .freq-card').length,
  dias21: document.querySelectorAll('#mp-grid .mp-day').length,
  botanica: document.querySelectorAll('#bot-grid .bot-card').length,
  desborde: document.documentElement.scrollWidth - document.documentElement.clientWidth
}));

const esp = {
  mapa3d: true, hubListo: true, grafica: true, hub: true,
  hubTerminaAntesDelPie: true, h1: 1, footers: 1,
  pieFondo: 'rgb(246, 246, 246)', respaldoOculto: true, desborde: 0
};
let mal = 0;
console.log('  comprobacion                   esperado             obtenido');
for (const k of Object.keys(esp)) {
  const ok = String(r[k]) === String(esp[k]); if (!ok) mal++;
  console.log('  ' + (ok ? 'OK   ' : 'FALLA') + ' ' + k.padEnd(25) + String(esp[k]).padEnd(21) + String(r[k]));
}
const decir = (ok, txt) => { if (!ok) mal++; console.log('  ' + (ok ? 'OK   ' : 'FALLA') + ' ' + txt); };
decir(anim.marcados >= 30, `las secciones reparten la entrada (${anim.marcados} elementos marcados)`);

/* SIN JAVASCRIPT EL CONTENIDO SIGUE AHI. Se abre la misma pagina con el
   script desactivado y se comprueba que nada queda en opacidad cero. Es la
   comprobacion que evita el peor fallo posible de una entrada al hacer
   scroll: que un bloqueador, un error o una red que corta dejen media pagina
   invisible para siempre. El estado escondido cuelga de la clase vp-anim,
   que solo pone el propio script. */
{
  const ctxSinJs = await b.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
  const pj = await ctxSinJs.newPage();
  await pj.goto(url, { waitUntil: 'load' });
  const invisibles = await pj.evaluate === undefined ? -1 : await pj.$$eval('#vill-hub section > *', els =>
    els.filter(e => parseFloat(getComputedStyle(e).opacity) < 0.5).length);
  decir(invisibles === 0, `sin JavaScript no se esconde nada (${invisibles} elementos en opacidad baja)`);
  await ctxSinJs.close();
}
decir(anim.vistos === anim.marcados, `todos entran al acercarse (${anim.vistos} de ${anim.marcados})`);
decir(anim.opacos === anim.vistos, `y quedan visibles de verdad, no solo con la clase (${anim.opacos})`);
decir(anim.cifras.every(c => /^\d+$/.test(c)), `las cifras del hero terminan en su numero: ${anim.cifras.join(', ')}`);
decir(perezoso, `al abrir la pagina NO se bajan el mapa 3D ni las graficas (684 KB, 190 KB por la red) -- llegan al acercarse`);
decir(pedido('vi-p-3d.js'), 'el mapa 3D se pide al acercarse a el');
decir(pedido('vi-p-chart.js'), 'las graficas se piden al acercarse a nutricion');
decir(await p.evaluate(() => { const c = document.getElementById('macro-chart'); return !!(c && c.getContext('2d').getImageData(0, 0, c.width, c.height).data.some(v => v !== 0)); }), 'el anillo de macros esta dibujado, no en blanco');
decir(externas.length === 0, `ni una peticion a un tercero (${externas.length})`);
externas.slice(0, 5).forEach(u => console.log('    ✗ ' + u.slice(0, 110)));
decir(errs.length === 0, `sin errores de JavaScript (${errs.length})`);
errs.slice(0, 4).forEach(e => console.log('    ✗ ' + e.slice(0, 120)));
decir(fallos.length === 0, `sin peticiones fallidas (${fallos.length})`);
fallos.slice(0, 4).forEach(e => console.log('    ✗ ' + e.slice(0, 110)));
decir(r.ejercicios >= 25 && r.dias21 >= 21 && r.botanica >= 50,
  `contenido: ${r.ejercicios} ejercicios · ${r.dias21} dias de mindfulness · ${r.botanica} alimentos`);

/* Las frecuencias van en pestanas, asi que en el DOM solo esta la activa.
   La primera version de esta bateria esperaba las 19 de golpe y daba rojo con
   11 -- que era la respuesta correcta. Ahora se pulsan las tres pestanas y se
   cuenta cada una, que ademas ejercita el cambio de pestana. El total tiene
   que cuadrar con el "19" que anuncia el hero: si alguien anade una frecuencia
   y se olvida del contador, esto lo dice. */
const solfeggio = r.frecuencias;
await p.click('.freq-tab[data-tab="binaural"]');
const binaural = await p.$$eval('#freq-grid .freq-card', n => n.length);
await p.click('.freq-tab[data-tab="dual"]');
const dual = await p.$$eval('#freq-grid .dual-panel', n => n.length);
await p.click('.freq-tab[data-tab="solfeggio"]');
const anunciadas = await p.$$eval('.hero-stat strong', n => n.map(e => e.textContent.trim()));
decir(solfeggio === 11 && binaural === 8 && dual === 1,
  `frecuencias por pestana: ${solfeggio} solfeggio + ${binaural} binaurales + ${dual} panel dual`);
decir(anunciadas.includes(String(solfeggio + binaural)),
  `el hero anuncia ${solfeggio + binaural} frecuencias y hay ${solfeggio + binaural} (cifras del hero: ${anunciadas.join(', ')})`);

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(mal ? `\n  ${mal} comprobaciones mal` : '\nVI.P funciona dentro del tema, sin salir a internet y sin tocar lo que hay alrededor.');
process.exit(mal ? 1 : 0);
