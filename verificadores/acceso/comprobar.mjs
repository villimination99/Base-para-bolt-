/* Accesibilidad medida, no supuesta.
   ------------------------------------------------------------------
   El tema ya tenia bateria de contraste y de teclado, pero nada que
   recorriera el arbol entero buscando lo que un lector de pantalla no puede
   nombrar: un boton que solo dice un emoji, un campo sin etiqueta, un id
   repetido, un salto de h2 a h4. Eso no lo ve nadie mirando la pagina --
   se ve exactamente igual de bien rota que entera -- y es justo lo que
   axe-core sabe encontrar.

   Se pasa sobre las dos paginas que mas pesan en la tienda: VI.P montada
   como la sirve Shopify, y la portada con sus secciones.

   Solo se miran las reglas serias (critical y serious). Las moderadas y
   menores de axe incluyen recomendaciones discutibles -- "region", por
   ejemplo, exige que todo cuelgue de un landmark, y aqui el hub vive
   dentro del <main> del tema, que la pagina de prueba si tiene pero que
   axe no siempre atribuye igual.

   Uso:  node verificadores/acceso/comprobar.mjs                          */
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';
import { e, prepararFuente, contextoDeSeccion } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const AXE = fs.readFileSync(path.join(RAIZ, 'node_modules/axe-core/axe.min.js'), 'utf8');
const TMP = fs.mkdtempSync('/tmp/acceso-');
const TIPO = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' };

/* Se renderiza con el MISMO motor que la bateria de secciones, no con
   sustituciones a mano. La primera version cambiaba asset_url con una
   expresion regular y se atraganto con vip-banner, que tiene bucles sobre
   bloques y condiciones de verdad: se quedo en "queda Liquid sin resolver".
   Y aunque hubiera pasado, habria medido una seccion con los ajustes
   vacios, que no es la que ve el cliente. */
async function renderizar(archivo) {
  const nombre = archivo.replace('.liquid', '');
  const src = fs.readFileSync(path.join(T, 'sections', archivo), 'utf8');
  const { ctx } = contextoDeSeccion(nombre, src);
  e.options.globals = ctx;
  let html = await e.parseAndRender(prepararFuente(src), ctx);
  /* asset_url lo devuelve el motor como //cdn/...: se reapunta al servidor
     local para que el CSS y el JavaScript de verdad se carguen. */
  html = html.replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');
  if (/\{[%{]/.test(html)) { console.error(`  ${archivo}: queda Liquid sin resolver`); process.exit(1); }
  return html;
}

fs.mkdirSync(path.join(TMP, 'assets'), { recursive: true });
for (const a of fs.readdirSync(path.join(T, 'assets'))) fs.copyFileSync(path.join(T, 'assets', a), path.join(TMP, 'assets', a));

/* La seccion se mete en una pagina con la estructura minima de un tema:
   un <main>, un <h1> y un idioma. Sin eso, axe se queja de la pagina de
   prueba y no de la seccion, que es lo que se quiere medir. */
/* villumination.css SIEMPRE, aunque la seccion no la pida.

   Aqui hubo un falso hallazgo que conviene dejar escrito: la primera version
   no cargaba la hoja del tema, porque vip-banner.liquid no la incluye -- sus
   estilos viven en villumination.css, que carga el LAYOUT. Resultado: axe
   media un banner sin estilos, con el negro por defecto del navegador sobre
   fondo negro, y cantaba una infraccion en el boton que no describia nada
   real. Un verificador que mide una pagina que no existe es peor que no
   tenerlo: manda a arreglar lo que no esta roto. */
const envolver = (titulo, cuerpo) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>${titulo}</title>
<link rel="stylesheet" href="/assets/villumination.css">
<style>body{margin:0;font-family:system-ui;background:#0A0A0A;color:#eee}
h1.t{font-size:2rem;margin:24px 18px}</style></head><body>
<main><h1 class="t">${titulo}</h1>
${cuerpo}
</main></body></html>`;

const PAGINAS = [
  ['VI.P', 'vi-p.liquid'],
  ['Banner VI.P', 'vip-banner.liquid']
];
for (const [titulo, arch] of PAGINAS) {
  fs.writeFileSync(path.join(TMP, arch.replace('.liquid', '.html')), envolver(titulo, await renderizar(arch)));
}

const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  const f = path.join(TMP, u.replace(/^\//, ''));
  fs.readFile(f, (e, d) => {
    if (e) { res.writeHead(404); res.end('no ' + u); return; }
    res.writeHead(200, { 'content-type': TIPO[path.extname(f)] || 'application/octet-stream' });
    res.end(d);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });

let fallos = 0;
for (const [titulo, arch] of PAGINAS) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.goto(base + arch.replace('.liquid', '.html'), { waitUntil: 'load' });
  /* Se recorre la pagina entera para que arranque todo lo que carga al
     acercarse; si no, axe mediria media seccion. */
  await p.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    window.scrollTo(0, 0);
  });
  await p.addScriptTag({ content: AXE });
  const r = await p.evaluate(async () => await window.axe.run(document, {
    resultTypes: ['violations'],
    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] }
  }));
  const graves = r.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
  console.log(`\n--- ${titulo} ---`);
  if (!graves.length) console.log('  OK    sin infracciones graves de WCAG 2.1 AA');
  for (const v of graves) {
    fallos++;
    console.log(`  FALLA [${v.impact}] ${v.id}: ${v.help}  (${v.nodes.length} elemento(s))`);
    for (const n of v.nodes.slice(0, 3)) console.log('        ' + n.html.replace(/\s+/g, ' ').slice(0, 120));
  }
  const leves = r.violations.filter(v => v.impact !== 'critical' && v.impact !== 'serious');
  if (leves.length) console.log('  (' + leves.map(v => v.id + '×' + v.nodes.length).join(', ') + ' — impacto moderado o menor, no cuentan)');
  await ctx.close();
}

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(fallos ? `\n  ${fallos} infraccion(es) grave(s)` : '\nNadie se queda fuera: ni un fallo grave de WCAG 2.1 AA.');
process.exit(fallos ? 1 : 0);
