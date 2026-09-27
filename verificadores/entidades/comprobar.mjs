/* NINGUNA ENTIDAD HTML PUEDE LEERSE POR PANTALLA, EN NINGUN IDIOMA.
   ------------------------------------------------------------------
   De donde sale esta bateria. Un cliente mando una captura del pie en
   frances donde se leia, literalmente:

       Le corps accomplit ce que l&#39;esprit croit.

   Dos verdades que por separado estan bien y juntas rompen la pagina:

     1. Shopify ESCAPA toda traduccion. El filtro t convierte "l'esprit" en
        "l&#39;esprit". Es su comportamiento documentado y no se puede apagar
        salvo con el sufijo _html en la clave.
     2. textContent NO interpreta HTML. Lo que le des, se ve tal cual.

   Mientras el texto lo pinta Liquid dentro del HTML no pasa nada: el
   navegador deshace la entidad al analizar el documento. El fallo aparece
   cuando el texto CRUZA a JavaScript -- en window.theme.strings, en un
   data-* o en un <script type="application/json"> -- y se pinta con
   textContent. Por eso en la captura la primera frase salia bien (esa la
   pinta Liquid) y las que rotan salian rotas.

   POR QUE NO BASTABA CON MIRAR EL HTML. La frase mala no esta en la pagina
   al cargar: aparece a los cinco segundos, cuando el temporizador cambia de
   frase. Una bateria que mire el marcado inicial da verde. Asi que aqui se
   captura setInterval ANTES de que cargue el guion, y despues se disparan
   sus callbacks a mano: lo que tardaria minutos en verse ocurre al
   instante, y sin esperas que hagan la prueba lenta o caprichosa.

   Se prueba en frances e ingles porque son las dos lenguas con apostrofo en
   la copia. El castellano casi no tiene y daria verde por suerte, no por
   estar bien.

   Uso:  node verificadores/entidades/comprobar.mjs                        */
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';
import { e, prepararFuente, contextoDeSeccion } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const TMP = fs.mkdtempSync(path.join(RAIZ, '.entidades-'));
const TIPO = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
               '.json': 'application/json', '.png': 'image/png', '.svg': 'image/svg+xml',
               '.woff2': 'font/woff2' };

const LOC = { fr: 'fr.json', en: 'en.default.json' };
const leerJson = (r) => JSON.parse(fs.readFileSync(r, 'utf8').replace(/^\/\*[\s\S]*?\*\//, ''));

/* Las secciones que de verdad cruzan texto a JavaScript. No se mira el tema
   entero: se mira donde esta el riesgo, y cada una con su motivo escrito.
     footer          -> las frases rotativas, que es donde lo vio el cliente
     main-product    -> el aviso de stock bajo viaja en data-stock-tpl, y ahi
                        llega DOBLEMENTE escapado (t escapa, y encima | escape)
     hero            -> las palabras que rotan viajan en data-typed
     announcement-bar-> el texto de cuenta atras terminada, en data-expired */
const SECCIONES = ['footer', 'main-product', 'hero', 'announcement-bar'];

/* Entidades que el cliente leeria por pantalla. Se busca el patron crudo:
   si el navegador las hubiera interpretado, ya no estarian aqui. */
const ENTIDAD = /&(?:#\d{2,5}|#x[0-9a-fA-F]{2,4}|amp|lt|gt|quot|apos|nbsp);/;

fs.copyFileSync(path.join(T, 'assets/base.js'), path.join(TMP, 'base.js'));
fs.copyFileSync(path.join(T, 'assets/effects.js'), path.join(TMP, 'effects.js'));

/* Se captura setInterval y setTimeout ANTES del guion del tema, para poder
   adelantar el reloj a mano. Tambien se fija el idioma en window.theme. */
const arnes = (strings) => `
<script>
  window.__intervalos = []; window.__esperas = [];
  var _si = window.setInterval, _st = window.setTimeout;
  window.setInterval = function (f, ms) { window.__intervalos.push(f); return _si(function(){}, 1e9); };
  window.setTimeout  = function (f, ms) { if (ms >= 200) { window.__esperas.push(f); return _st(function(){}, 1e9); } return _st(f, ms); };
  window.theme = { routes: {}, settings: { moneyFormat: '\${{amount}}' }, strings: ${strings} };
</script>`;

const envolver = (titulo, cuerpo, strings) => `<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>${titulo}</title>
<link rel="stylesheet" href="/villumination.css">
${arnes(strings)}
<script src="/base.js" defer></script>
<script src="/effects.js" defer></script>
</head><body><main>${cuerpo}</main></body></html>`;

fs.copyFileSync(path.join(T, 'assets/villumination.css'), path.join(TMP, 'villumination.css'));

let fallos = 0;
const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  fs.readFile(path.join(TMP, u.replace(/^\//, '')), (err, d) => {
    if (err) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'content-type': TIPO[path.extname(u)] || 'application/octet-stream' });
    res.end(d);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));
const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME });
const pag = await (await b.newContext({ viewport: { width: 390, height: 844 } })).newPage();

/* Como escapa Shopify, literalmente: las traducciones salen escapadas salvo
   que la clave termine en _html. Si esta prueba no escapara, no probaria
   nada -- seria la novena vez que este banco de pruebas difiere de la tienda. */
const escapar = (v) => String(v)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

for (const [idioma, archivo] of Object.entries(LOC)) {
  const loc = leerJson(path.join(T, 'locales', archivo));
  const busca = (k) => String(k).split('.').reduce((o, p) => (o && typeof o === 'object' && p in o) ? o[p] : undefined, loc);
  e.registerFilter('t', (v) => {
    const r = busca(v);
    if (r === undefined || (r !== null && typeof r === 'object')) return `Translation missing: ${idioma}.${v}`;
    return /_html$/.test(String(v)) ? r : escapar(r);
  });

  /* Las cadenas que el layout mete en window.theme.strings, escapadas igual
     que las manda Shopify. */
  const claves = {
    addToCart: 'products.product.add_to_cart', soldOut: 'products.product.sold_out',
    unavailable: 'products.product.unavailable', copied: 'general.copied',
    searchError: 'general.search.error', noResults: 'general.search.no_results_short',
  };
  const strings = {};
  for (const [k, clave] of Object.entries(claves)) {
    const v = busca(clave);
    if (typeof v === 'string') strings[k] = escapar(v);
  }

  for (const tipo of SECCIONES) {
    const ruta = path.join(T, 'sections', tipo + '.liquid');
    if (!fs.existsSync(ruta)) continue;
    const src = fs.readFileSync(ruta, 'utf8');
    const { ctx } = contextoDeSeccion(tipo, src);
    e.options.globals = ctx;
    let html;
    try { html = await e.parseAndRender(prepararFuente(src), ctx); }
    catch (err) { console.log(`  FALLA ${idioma}/${tipo}: no se pudo pintar -- ${err.message}`); fallos++; continue; }

    const arch = `${idioma}-${tipo}.html`;
    fs.writeFileSync(path.join(TMP, arch), envolver(tipo, html, JSON.stringify(strings)));
    await pag.goto(base + arch, { waitUntil: 'load' });
    await pag.waitForTimeout(150);

    /* Se adelanta el reloj: se disparan los temporizadores capturados varias
       vueltas, que es lo que el visitante ve a los cinco, diez y quince
       segundos. Y se pintan ademas todas las frases de la lista, para que no
       se escape la unica que llevaba apostrofo. */
    const visto = await pag.evaluate(async () => {
      const salida = [];
      const mirar = () => {
        const t = document.body.innerText || '';
        const m = t.match(/[^\n]*&(?:#\d{2,5}|#x[0-9a-fA-F]{2,4}|amp|lt|gt|quot|apos|nbsp);[^\n]*/g);
        if (m) salida.push(...m);
      };
      mirar();
      for (let vuelta = 0; vuelta < 4; vuelta++) {
        for (const f of (window.__intervalos || [])) { try { f(); } catch (e) {} }
        for (const f of (window.__esperas || [])) { try { f(); } catch (e) {} }
        await new Promise(r => setTimeout(r, 30));
        mirar();
      }
      /* NO se pinta la lista a mano aqui. La primera version de esta prueba
         hacia destino.textContent = q con el JSON crudo, y eso no prueba el
         tema: prueba el arnes. Lo que tiene que pintar las frases es el guion
         del tema, disparado por los temporizadores de arriba. Si alguien
         quita el desescapador, esas vueltas lo cantan solas -- comprobado con
         trampa. */
      return [...new Set(salida)];
    });

    if (visto.length) {
      fallos += visto.length;
      console.log(`  FALLA ${idioma}/${tipo}: se lee una entidad HTML por pantalla`);
      for (const v of visto.slice(0, 3)) console.log(`        «${v.trim().slice(0, 72)}»`);
    } else {
      console.log(`  OK    ${idioma}/${tipo}`);
    }
  }
}

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(fallos ? `\n  ${fallos} entidad(es) HTML a la vista del cliente`
                   : '\nNo se lee ni una entidad HTML por pantalla, ni en frances ni en ingles.');
process.exit(fallos ? 1 : 0);
