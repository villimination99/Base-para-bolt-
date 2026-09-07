/* TODAS LAS PAGINAS DE LA TIENDA, NO SOLO LA PORTADA.
   ------------------------------------------------------------------
   Hasta ahora se media la portada y nada mas. Pero una tienda no entra por la
   portada: entra por una ficha de producto que salio en Google, por una
   coleccion compartida en Instagram, por un articulo del diario. Esas paginas
   nunca se habian cronometrado, y son las que venden.

   Aqui se monta CADA plantilla como la sirve Shopify -- el layout con su
   cabecera, sus secciones y su pie -- y se mide, por una linea 4G lenta y con
   las fotos pesando lo que pesarian:

     LCP  cuando se pinta lo mas grande. Google: bueno < 2500 ms.
     CLS  cuanto salta la pagina mientras carga. Google: bueno < 0,1.
          Esto NO se habia medido nunca en este tema, y es uno de los tres
          numeros que Google usa para ordenar resultados.
     Errores de JavaScript, que en una ficha de producto significan un boton
          de comprar que no responde.
     Desbordes laterales, que en un movil son la diferencia entre una tienda
          y una tienda rota.

   Uso:  node verificadores/paginas/comprobar.mjs                           */
import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { crearBanco, frenar } from '../../herramientas/banco-de-fotos.mjs';
import { e, prepararFuente, ctxBase, contextoDeSeccion, T } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const TEMA = path.isAbsolute(T) ? T : path.join(RAIZ, T);
const TMP = fs.mkdtempSync('/tmp/paginas-');
const TIPO = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

fs.mkdirSync(path.join(TMP, 'assets'), { recursive: true });
for (const a of fs.readdirSync(path.join(TEMA, 'assets'))) fs.copyFileSync(path.join(TEMA, 'assets', a), path.join(TMP, 'assets', a));

const reapuntar = (h) => h
  .replace(/\/\/cdn\/foto\.png(\?[^"'\s>]*)?/g, (m, q) => '/foto' + (q || ''))
  .replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');

/* Una plantilla JSON es una lista ordenada de secciones con sus ajustes
   guardados. Se montan en ese orden, exactamente como lo hace la tienda: los
   ajustes de la plantilla mandan sobre los del esquema. */
async function montarPlantilla(archivo) {
  const j = JSON.parse(fs.readFileSync(path.join(TEMA, 'templates', archivo), 'utf8'));
  let html = '';
  const problemas = [];
  for (const id of j.order || Object.keys(j.sections || {})) {
    const tipo = j.sections[id].type;
    const ruta = path.join(TEMA, 'sections', tipo + '.liquid');
    if (!fs.existsSync(ruta)) { problemas.push(`la seccion ${tipo} no existe`); continue; }
    const src = fs.readFileSync(ruta, 'utf8');
    try {
      const { ctx } = contextoDeSeccion(tipo, src);
      Object.assign(ctx.section.settings, j.sections[id].settings || {});
      if (j.sections[id].blocks) {
        ctx.section.blocks = Object.entries(j.sections[id].blocks).map(([k, b]) => ({
          id: k, type: b.type, settings: b.settings || {}, shopify_attributes: '',
        }));
      }
      e.options.globals = ctx;
      html += await e.parseAndRender(prepararFuente(src), ctx);
    } catch (err) {
      problemas.push(`${tipo}: ${String(err.message).slice(0, 70)}`);
    }
  }
  return { html: reapuntar(html), problemas };
}

/* La cabecera y el pie van en TODAS las paginas, asi que tienen que estar en
   la medida: son parte de lo que retrasa el primer pintado y de lo que puede
   dar un salto. Se montan del grupo de secciones, como en la tienda. */
async function montarGrupo(nombre) {
  const ruta = path.join(TEMA, 'sections', nombre + '.json');
  if (!fs.existsSync(ruta)) return '';
  const j = JSON.parse(fs.readFileSync(ruta, 'utf8'));
  let html = '';
  for (const id of j.order || []) {
    const tipo = j.sections[id].type;
    const rutaS = path.join(TEMA, 'sections', tipo + '.liquid');
    if (!fs.existsSync(rutaS)) continue;
    const src = fs.readFileSync(rutaS, 'utf8');
    try {
      const { ctx } = contextoDeSeccion(tipo, src);
      Object.assign(ctx.section.settings, j.sections[id].settings || {});
      if (j.sections[id].blocks) {
        ctx.section.blocks = Object.entries(j.sections[id].blocks).map(([k, b]) => ({
          id: k, type: b.type, settings: b.settings || {}, shopify_attributes: '',
        }));
      }
      e.options.globals = ctx;
      html += await e.parseAndRender(prepararFuente(src), ctx);
    } catch (err) { /* el grupo no es lo que se juzga aqui */ }
  }
  return reapuntar(html);
}

const cabecera = await montarGrupo('header-group');
const pie = await montarGrupo('footer-group');

const PLANTILLAS = fs.readdirSync(path.join(TEMA, 'templates'))
  .filter(f => f.endsWith('.json')).sort();

const guardados = JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_data.json'), 'utf8')).current;

const montadas = [];
for (const f of PLANTILLAS) {
  const { html, problemas } = await montarPlantilla(f);
  const nombre = f.replace(/\.json$/, '');
  const doc = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>${nombre} · VILLUMINATION</title>
<link rel="stylesheet" href="/assets/villumination.css">
<style>body{margin:0;background:${guardados.color_bg || '#05060a'};color:#eee;font-family:system-ui}</style>
</head><body>
${cabecera}
<main id="MainContent">${html}</main>
${pie}
<script src="/assets/base.js" defer></script>
</body></html>`;
  fs.writeFileSync(path.join(TMP, nombre + '.html'), doc);
  montadas.push({ nombre, archivo: nombre + '.html', problemas, bytes: doc.length });
}

const banco = crearBanco(TMP, TIPO);
const base = await banco.escuchar();

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
banco.pincel = await b.newPage();

async function medir(archivo) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const errores = [];
  p.on('pageerror', x => errores.push(String(x.message)));
  p.on('console', m => { if (m.type() === 'error') errores.push(m.text()); });
  /* Que URL fallo, no solo que fallo algo. Sin esto, "1 error de JavaScript"
     manda a leer codigo cuando el problema era una direccion mal escrita. */
  const fallidas = [];
  p.on('requestfailed', q => fallidas.push(q.url().replace(base, '/')));
  p.on('response', q => { if (q.status() >= 400) fallidas.push(q.status() + ' ' + q.url().replace(base, '/')); });

  await p.addInitScript(() => {
    window.__lcp = 0; window.__que = '';
    new PerformanceObserver((l) => {
      for (const x of l.getEntries()) {
        window.__lcp = x.startTime;
        window.__que = (x.element && (x.element.tagName + '.' + String(x.element.className || '').slice(0, 34))) || x.url || '?';
      }
    }).observe({ type: 'largest-contentful-paint', buffered: true });

    /* CLS: se suman los saltos que NO vienen de una accion del visitante.
       Es la definicion de Google, no una aproximacion: hadRecentInput
       descarta lo que se movio porque alguien toco algo. */
    window.__cls = 0; window.__peorSalto = null;
    new PerformanceObserver((l) => {
      for (const x of l.getEntries()) {
        if (x.hadRecentInput) continue;
        window.__cls += x.value;
        if (!window.__peorSalto || x.value > window.__peorSalto.v) {
          const f = (x.sources || [])[0];
          window.__peorSalto = {
            v: x.value,
            quien: f && f.node ? (f.node.tagName + '.' + String(f.node.className || '').slice(0, 34)) : '?',
          };
        }
      }
    }).observe({ type: 'layout-shift', buffered: true });

    window.__lt = 0;
    try {
      new PerformanceObserver((l) => { for (const x of l.getEntries()) window.__lt += x.duration; })
        .observe({ type: 'longtask', buffered: true });
    } catch (e) { }
  });

  await frenar(ctx, p);
  banco.cuenta = [];
  await p.goto(base + archivo, { waitUntil: 'load' });
  await p.waitForTimeout(5500);

  /* El CLS de campo cuenta TODA la vida de la pagina, no solo la carga. Un
     desplazamiento hasta el pie despierta lo que entra al acercarse, que es
     justo donde suelen esconderse los saltos. */
  await p.evaluate(async () => {
    const duerme = ms => new Promise(r => setTimeout(r, ms));
    let anterior = -1;
    for (let i = 0; i < 60; i++) {
      window.scrollTo(0, window.scrollY + 600);
      await duerme(70);
      const fondo = document.documentElement.scrollHeight;
      if (window.scrollY + window.innerHeight >= fondo - 2 && window.scrollY === anterior) break;
      anterior = window.scrollY;
    }
  });
  await p.waitForTimeout(1200);

  const r = await p.evaluate(() => ({
    lcp: Math.round(window.__lcp), que: window.__que,
    cls: Math.round(window.__cls * 1000) / 1000,
    peor: window.__peorSalto,
    lt: Math.round(window.__lt),
    desborde: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    alto: document.documentElement.scrollHeight,
  }));
  /* Lo que no llega del CDN de Shopify o de YouTube no es un fallo del tema:
     es que este contenedor no tiene salida a esos dominios. Se aparta con el
     nombre del dominio, no con un "cualquier cosa que suene a red", que
     taparia justo los fallos que buscamos. Y se cuenta aparte, para que se
     vea que se aparto algo. */
  const deFuera = (t) => /cdn\.shopify\.com|i\.ytimg\.com|youtube\.com|jsdelivr/i.test(t);
  r.fallidas = [...new Set(fallidas)];
  r.deFuera = r.fallidas.filter(deFuera).length;
  r.errores = errores.filter(t => {
    if (!/Failed to load resource|net::ERR/i.test(t)) return true;
    /* Un mensaje de recurso caido no dice QUE recurso. Si todas las peticiones
       fallidas de esta pagina son de fuera, este mensaje es de una de ellas. */
    return !(r.fallidas.length > 0 && r.fallidas.every(deFuera));
  });
  r.red = banco.total();
  r.pesados = banco.pesados(2);
  await ctx.close();
  return r;
}

console.log('');
console.log('  plantilla          LCP      CLS   tareas   red     saltos / errores');
console.log('  ' + '-'.repeat(74));

const filas = [];
for (const m of montadas) {
  const r = await medir(m.archivo);
  filas.push({ ...m, ...r });
  const kb = (r.red / 1024).toFixed(0) + ' KB';
  const nota = [];
  if (r.peor && r.cls >= 0.01) nota.push('salta ' + r.peor.quien);
  if (r.errores.length) nota.push(r.errores.length + ' error(es) JS');
  if (r.desborde > 0) nota.push('desborde ' + r.desborde + ' px');
  if (m.problemas.length) nota.push(m.problemas.length + ' seccion(es) sin montar');
  console.log('  ' + m.nombre.padEnd(18) +
    (r.lcp + ' ms').padStart(7) + '  ' +
    String(r.cls).padStart(6) + '  ' +
    (r.lt + ' ms').padStart(7) + '  ' +
    kb.padStart(7) + '   ' + nota.join(' · '));
}

await b.close(); banco.srv.close(); fs.rmSync(TMP, { recursive: true, force: true });

console.log('');
let mal = 0;
const decir = (ok, txt) => { if (!ok) mal++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };

/* Los umbrales son los de Google, no inventados. LCP bueno por debajo de
   2500 ms; CLS bueno por debajo de 0,1. Se aplican a TODAS las plantillas,
   porque Google no puntua "la portada": puntua cada direccion. */
const lentas = filas.filter(f => f.lcp >= 2500);
const saltonas = filas.filter(f => f.cls >= 0.1);
const rotas = filas.filter(f => f.errores.length);
const anchas = filas.filter(f => f.desborde > 0);
const sinMontar = filas.filter(f => f.problemas.length);

decir(lentas.length === 0, lentas.length
  ? `${lentas.length} plantilla(s) tardan 2500 ms o mas: ${lentas.map(f => f.nombre + ' ' + f.lcp).join(', ')}`
  : `las ${filas.length} plantillas pintan lo mas grande por debajo de 2500 ms (la peor, ${Math.max(...filas.map(f => f.lcp))} ms)`);
decir(saltonas.length === 0, saltonas.length
  ? `${saltonas.length} plantilla(s) saltan 0,1 o mas: ${saltonas.map(f => f.nombre + ' ' + f.cls).join(', ')}`
  : `ninguna plantilla salta al cargar (la peor, ${Math.max(...filas.map(f => f.cls))})`);
decir(rotas.length === 0, rotas.length
  ? `JavaScript roto en: ${rotas.map(f => f.nombre).join(', ')}`
  : 'ninguna plantilla lanza errores de JavaScript');
decir(anchas.length === 0, anchas.length
  ? `se salen de lado: ${anchas.map(f => f.nombre + ' +' + f.desborde + 'px').join(', ')}`
  : 'ninguna plantilla se sale de lado en un movil de 390 px');
decir(sinMontar.length === 0, sinMontar.length
  ? `secciones que no montan: ${sinMontar.map(f => f.nombre + ' (' + f.problemas.join('; ') + ')').join(' | ')}`
  : 'todas las secciones de todas las plantillas montan');

for (const f of rotas) {
  for (const x of f.errores.slice(0, 3)) console.log(`        ${f.nombre}: ${x.slice(0, 120)}`);
  for (const u of f.fallidas.slice(0, 4)) console.log(`        ${f.nombre}: no llego ${u.slice(0, 110)}`);
}
for (const f of saltonas) console.log(`        ${f.nombre}: el peor salto lo da ${f.peor && f.peor.quien}`);

console.log(mal ? `\n  ${mal} en rojo.\n` : '\nTodas las paginas de la tienda cargan bien.\n');
process.exit(mal ? 1 : 0);
