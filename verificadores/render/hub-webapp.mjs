/* La pagina del hub se declara como APLICACION WEB GRATUITA, y solo ella.
   ------------------------------------------------------------------
   VI.P no es un texto: es una herramienta que se usa dentro del navegador --
   mapa muscular 3D, planificador, calculadoras, camara, audio. Declararla
   como WebApplication con precio 0 es decir la verdad, y es lo que permite
   que un buscador la presente como herramienta gratuita en vez de como una
   pagina mas.

   Aqui se comprueban las dos mitades del asunto, porque fallar cualquiera de
   las dos hace dano: que el bloque SALGA en la pagina del hub, y que NO
   salga en las demas -- una tienda que declara cada pagina como aplicacion
   es una tienda que pierde la credibilidad de sus datos estructurados.

   Uso:  node verificadores/render/hub-webapp.mjs                          */
import { e, prepararFuente, ctxBase, T } from '../liquid.mjs';
import fs from 'fs';

const src = fs.readFileSync(T + '/snippets/structured-data.liquid', 'utf8');
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

async function tipos(handle) {
  const ctx = JSON.parse(JSON.stringify(ctxBase));
  ctx.request = Object.assign({}, ctxBase.request, { page_type: 'page' });
  ctx.page = { title: 'Una pagina', handle, url: '/pages/' + handle, content: '<p>Texto</p>' };
  ctx.settings = Object.assign({}, ctxBase.settings, {
    hub_page_handle: 'vi-p',
    hub_page_summary: 'Mapa muscular 3D interactivo y rutinas, gratis.'
  });
  ctx.template = { name: 'page', suffix: null };
  e.options.globals = ctx;
  const html = await e.parseAndRender(prepararFuente(src), ctx);
  const bloques = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  for (const b of bloques) {
    try { JSON.parse(b[1]); }
    catch (err) { decir(false, `${handle}: un bloque JSON-LD no es JSON valido (${String(err.message).slice(0, 60)})`); }
  }
  return [...html.matchAll(/"@type":\s*"([A-Za-z]+)"/g)].map(m => m[1]);
}

console.log('');
const hub = await tipos('vi-p');
decir(hub.includes('WebApplication'), `la pagina del hub se declara WebApplication (${hub.join(', ')})`);
decir(hub.includes('Offer'), 'y dice que es gratis, que es el motivo por el que alguien pincharia');
decir(!hub.includes('WebPage'), 'sin declararse ademas como WebPage: un tipo por pagina, no dos');

for (const otra of ['preguntas', 'como-se-hace', 'contact']) {
  const t = await tipos(otra);
  decir(!t.includes('WebApplication'), `${otra} NO se declara aplicacion (${t.join(', ')})`);
}

console.log(fallos ? `\n  ${fallos} comprobacion(es) en rojo.\n` : '\nSolo el hub se declara aplicacion, y se declara gratis.\n');
process.exit(fallos ? 1 : 0);
