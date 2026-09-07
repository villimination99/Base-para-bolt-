/* Fotos del mapa 3D para verlo con los ojos y no solo con numeros.
   node mirar-mapa.mjs [salida]   -> /tmp/mapa-*.png */
import { chromium } from 'playwright';
import http from 'http'; import path from 'path'; import fs from 'fs';
import { e, prepararFuente, contextoDeSeccion } from './verificadores/liquid.mjs';
const T = process.env.TEMA || 'theme';
const SAL = process.argv[2] || '/tmp';
const TMP = fs.mkdtempSync('/tmp/mirar-');
fs.mkdirSync(TMP + '/assets', { recursive: true });
for (const a of fs.readdirSync(T + '/assets')) fs.copyFileSync(T + '/assets/' + a, TMP + '/assets/' + a);
const src = fs.readFileSync(T + '/sections/vi-p.liquid', 'utf8');
const { ctx } = contextoDeSeccion('vi-p', src); e.options.globals = ctx;
const html = (await e.parseAndRender(prepararFuente(src), ctx)).replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');
fs.writeFileSync(TMP + '/p.html', `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>x</title><link rel="stylesheet" href="/assets/villumination.css"></head><body style="margin:0;background:#0A0A0A"><main><h1 style="color:#fff">VI.P</h1>${html}</main></body></html>`);
const srv = http.createServer((q, s) => { const u = decodeURIComponent(q.url.split('?')[0]);
  fs.readFile(path.join(TMP, u === '/' ? 'p.html' : u.slice(1)), (er, d) => { if (er) { s.writeHead(404); s.end(); return; }
    s.writeHead(200, { 'content-type': u.endsWith('.css') ? 'text/css' : u.endsWith('.js') ? 'text/javascript' : 'text/html' }); s.end(d); }); });
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const p = await b.newPage({ viewport: { width: 900, height: 1000 }, deviceScaleFactor: 2 });
const errs = []; p.on('pageerror', x => errs.push(x.message));
await p.goto(base, { waitUntil: 'load' });
await p.evaluate(() => document.getElementById('muscle-canvas').scrollIntoView());
await p.waitForFunction(() => window.__mm3dReady === true, { timeout: 90000 }).catch(() => {});
await p.waitForTimeout(3000);
await p.evaluate(() => { window.__mmPararGiro && window.__mmPararGiro(); });
await p.locator('#muscle-canvas').screenshot({ path: SAL + '/mapa-libre.png' });
for (const m of (process.env.MUSCULOS || 'Pecho,Espalda,Cuadriceps').split(',')) {
  await p.evaluate(n => window.selectMuscle3D && window.selectMuscle3D(n, false), m);
  await p.waitForTimeout(2200);
  await p.locator('#muscle-canvas').screenshot({ path: SAL + '/mapa-' + m + '.png' });
}
console.log('  errores de JS: ' + errs.length); errs.slice(0, 3).forEach(x => console.log('   ✗ ' + x.slice(0, 120)));
await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
