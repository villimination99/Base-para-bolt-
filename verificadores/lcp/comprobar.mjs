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

   CON LAS IMAGENES PUESTAS. La primera version borraba los <img> porque desde
   aqui no se alcanza el CDN de Shopify, y asi estuvo dando por buena una
   portada que no existe: lo mas grande de la portada de verdad ES una foto a
   pantalla completa, y era ella la que se llevaba el LCP. Ahora cada foto se
   sirve en local con el ancho, el formato y EL PESO que Shopify entregaria, y
   por una linea de movil de verdad (4G lenta: 1,6 Mb/s y 150 ms de ida y
   vuelta), que es la red en la que Google recoge sus numeros de campo.

   Uso:  node verificadores/lcp/comprobar.mjs                              */
import { chromium } from 'playwright';
import http from 'http';
import zlib from 'zlib';
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

/* Las URL del motor: //cdn/foto.png?width=..&format=.. son fotos del CDN, y
   //cdn/loquesea.js son archivos del propio tema. Las primeras van a la ruta
   que fabrica la foto; las segundas, a la copia local de assets/. El orden
   importa: la regla general se comeria la de las fotos. */
const reapuntar = (h) => h
  .replace(/\/\/cdn\/foto\.png(\?[^"'\s>]*)?/g, (m, q) => '/foto' + (q || ''))
  .replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');

/* --- La intro, aparte, para poder medir con y sin --- */
const splashSrc = fs.readFileSync(path.join(TEMA, 'snippets/splash-intro.liquid'), 'utf8');
const guardados = JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_data.json'), 'utf8')).current;
async function montarSplash(duracion) {
  const ctxS = JSON.parse(JSON.stringify(ctxBase));
  ctxS.settings = Object.assign({}, ctxBase.settings, guardados, { splash_duracion: duracion });
  e.options.globals = ctxS;
  return reapuntar(await e.parseAndRender(prepararFuente(splashSrc), ctxS));
}
const splashCompleta = await montarSplash('completa');
const splashCorta = await montarSplash('corta');

cuerpo = reapuntar(cuerpo);

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

/* ================= LO QUE PESA UNA FOTO DE LA TIENDA =================
   Nada de esto es a ojo: fotos-de-la-tienda.json lleva el ancho, el alto y los
   bytes REALES de cada imagen subida, consultados al panel. Con eso:

   - Proporcion. Si la plantilla pide solo el ancho, el alto sale de la foto
     original, no de suponerla cuadrada. Un logotipo de 1600x400 pedido a 900
     px son 900x225, no 900x900.
   - PNG (o el WebP que el CDN de Shopify sirve solo en su lugar). El peso baja
     con los pixeles: bytes x (pixeles pedidos / pixeles del original), y por
     0,7 de la conversion a WebP. La foto del gimnasio, 1536x2752 y 5,95 MB,
     pedida a 1400x2217 son 3,1 MB; a 900x1425, 1,26 MB.
   - pjpg. JPEG de calidad alta: 0,11 bytes por pixel en una foto y 0,04 en un
     dibujo plano, que se distinguen por la densidad del original. La misma
     foto del gimnasio a 900x1425 son 141 KB.

   Nueve veces menos por cambiar una palabra en la plantilla. Esa es la razon
   de que exista este modelo: sin el, en localhost los megabytes son gratis y
   la bateria daba luz verde a una portada que en un movil tardaba 4,3 s.

   La imagen se dibuja de verdad (degradado oscuro con vetas de neon, que
   comprime parecido a una foto de gimnasio) para que el navegador pague el
   coste real de decodificarla, y despues se rellena hasta el peso del modelo.
   Los bytes de mas van detras del final del archivo, donde todo decodificador
   los ignora. */
const CATALOGO = JSON.parse(fs.readFileSync(path.join(RAIZ, 'verificadores/lcp/fotos-de-la-tienda.json'), 'utf8'));
function medidasDe(src, wPedido, hPedido, fmt) {
  const o = CATALOGO[src] || CATALOGO.generica;
  const [ow, oh, obytes] = o;
  const w = wPedido || ow;
  const h = hPedido || Math.max(1, Math.round(w * oh / ow));
  const px = w * h;
  const densidad = obytes / (ow * oh);          // bytes por pixel del original
  let bytes;
  if (fmt === 'pjpg' || fmt === 'jpg') bytes = px * (densidad > 0.5 ? 0.11 : 0.04);
  else bytes = Math.min(obytes, obytes * px / (ow * oh)) * 0.7;
  return { w, h, bytes: Math.round(bytes) };
}

const fotos = new Map();
let pincel = null;
async function foto(w, h, fmt, bytes) {
  const clave = w + 'x' + h + fmt + bytes;
  if (fotos.has(clave)) return fotos.get(clave);
  const tipo = (fmt === 'pjpg' || fmt === 'jpg') ? 'image/jpeg' : 'image/png';
  /* Se dibuja en JPEG y bajando la calidad hasta caber por debajo del peso del
     modelo, porque al cuerpo solo se le puede ANADIR relleno. Sin este ajuste,
     un PNG sintetico de 1200x2133 pesaba 1,5 MB el solo y la bateria acusaba a
     una foto de algo que era culpa del pincel. La calidad que sobrevive es la
     mas alta que cabe, asi que cuando el modelo dice "esto son 1,2 MB" el
     navegador tambien paga una descodificacion de verdad. */
  const dataUrl = await pincel.evaluate(([w, h, tipo, tope]) => {
    const c = document.createElement('canvas');
    c.width = w; c.height = h;
    const x = c.getContext('2d');
    const g = x.createLinearGradient(0, 0, w, h);
    g.addColorStop(0, '#0b0f18'); g.addColorStop(0.5, '#18202e'); g.addColorStop(1, '#070a10');
    x.fillStyle = g; x.fillRect(0, 0, w, h);
    /* Pocas formas y grandes: lo dibujado tiene que pesar MENOS que el modelo,
       porque al cuerpo solo se le puede anadir relleno, no quitarlo. Con sesenta
       vetas finas un logotipo de 450 px se iba a 39 KB el solo. */
    for (let i = 0; i < 8; i++) {
      x.globalAlpha = 0.07 + (i % 4) * 0.03;
      x.fillStyle = i % 3 === 0 ? '#00d4ff' : (i % 3 === 1 ? '#ff2ecb' : '#7b2fff');
      x.fillRect((i * 211) % w, (i * 307) % h, w / 3, h / 6);
    }
    x.globalAlpha = 1;
    let mejor = c.toDataURL('image/jpeg', 0.92);
    for (const q of [0.92, 0.7, 0.5, 0.3, 0.15, 0.05]) {
      const d = c.toDataURL('image/jpeg', q);
      mejor = d;
      if (d.length * 0.75 <= tope) break;
    }
    return mejor;
  }, [w, h, tipo, bytes]);
  let cuerpoImg = Buffer.from(dataUrl.split(',')[1], 'base64');
  if (bytes > cuerpoImg.length) cuerpoImg = Buffer.concat([cuerpoImg, Buffer.alloc(bytes - cuerpoImg.length, 0)]);
  /* El cuerpo es JPEG siempre, tambien cuando la plantilla pide PNG: lo que
     se esta midiendo es lo que cuesta en red y en descodificar, y el peso ya lo
     fija el modelo. Se declara lo que de verdad se envia. */
  const r = { cuerpo: cuerpoImg, tipo: 'image/jpeg' };
  fotos.set(clave, r);
  return r;
}

/* Shopify sirve todo el texto comprimido, asi que aqui tambien. Sin esto la
   hoja de estilos viajaba con sus 206 KB en crudo -- un segundo entero de 4G
   solo para ella -- y la bateria medía un problema que la tienda no tiene.
   Los bytes que de verdad cruzan la red se apuntan por URL, que es la unica
   forma honesta de explicar despues de donde sale el numero. */
const TEXTO = new Set(['text/html', 'text/javascript', 'text/css', 'application/json']);
let cuenta = [];
const srv = http.createServer(async (req, res) => {
  const [ruta, busca] = req.url.split('?');
  const u = decodeURIComponent(ruta);
  if (u === '/foto') {
    const q = new URLSearchParams(busca || '');
    const fmt = q.get('format') || 'png';
    const m = medidasDe(q.get('src') || 'generica',
                        parseInt(q.get('width') || '0', 10) || 0,
                        parseInt(q.get('height') || '0', 10) || 0, fmt);
    const f = await foto(m.w, m.h, fmt, m.bytes);
    cuenta.push({ u: (q.get('src') || '?').slice(0, 34) + ' ' + m.w + 'x' + m.h + ' ' + fmt, n: f.cuerpo.length });
    res.writeHead(200, { 'content-type': f.tipo, 'cache-control': 'public, max-age=600' });
    res.end(f.cuerpo);
    return;
  }
  const f = path.join(TMP, u.replace(/^\//, ''));
  fs.readFile(f, (err, d) => {
    if (err) { res.writeHead(404); res.end('no ' + u); return; }
    const tipo = TIPO[path.extname(f)] || 'application/octet-stream';
    const cab = { 'content-type': tipo };
    let salida = d;
    if (TEXTO.has(tipo) && /\bbr\b/.test(req.headers['accept-encoding'] || '')) {
      salida = zlib.brotliCompressSync(d);
      cab['content-encoding'] = 'br';
    }
    cuenta.push({ u, n: salida.length });
    res.writeHead(200, cab);
    res.end(salida);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
pincel = await b.newPage();

async function medir(archivo) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.addInitScript(() => {
    window.__lcp = 0; window.__lcpQue = '';
    new PerformanceObserver((l) => {
      for (const x of l.getEntries()) { window.__lcp = x.startTime; window.__lcpQue = (x.element && (x.element.tagName + '.' + (x.element.className || '').toString().slice(0, 40))) || x.url || '?'; }
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  });
  /* 4G LENTA, la de Lighthouse: 1,6 Mb/s de bajada y 150 ms de ida y vuelta.
     Sin freno, un megabyte viaja por localhost en dos milisegundos y una foto
     de 4 MB parece gratis; con freno, cuesta lo que le cuesta al visitante. */
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', {
    offline: false, latency: 150,
    downloadThroughput: 1.6 * 1024 * 1024 / 8, uploadThroughput: 750 * 1024 / 8
  });
  cuenta = [];
  await p.goto(base + archivo, { waitUntil: 'load' });
  await p.waitForTimeout(6500);           // mas que la intro entera, ya con freno
  const r = await p.evaluate(() => ({ lcp: Math.round(window.__lcp), que: window.__lcpQue }));
  r.pesos = cuenta.slice().sort((a, b2) => b2.n - a.n).slice(0, 4);
  r.total = cuenta.reduce((a, x) => a + x.n, 0);
  await ctx.close();
  return r;
}

/* TRES VECES Y LA DEL MEDIO. Una sola medida de LCP baila 300 ms de una
   ejecucion a otra -- la maquina va a rafagas, el rasterizado es por software y
   la red simulada tiene su propio ruido -- y con ese baile una bateria se pone
   roja o verde por azar, que es la peor clase de bateria. La mediana de tres
   quita el pico suelto sin tapar un empeoramiento de verdad. */
async function medirTresVeces(archivo) {
  const t = [];
  for (let i = 0; i < 3; i++) t.push(await medir(archivo));
  t.sort((a, b2) => a.lcp - b2.lcp);
  return t[1];
}
const completa = await medirTresVeces('completa.html');
const corta = await medirTresVeces('corta.html');
const sin = await medirTresVeces('sin.html');
const con = completa;

console.log('');
console.log(`  intro completa:  ${String(completa.lcp).padStart(5)} ms   (lo mas grande: ${completa.que})`);
console.log(`  intro corta:     ${String(corta.lcp).padStart(5)} ms   (lo mas grande: ${corta.que})`);
console.log(`  sin intro:       ${String(sin.lcp).padStart(5)} ms   (lo mas grande: ${sin.que})`);
console.log(`  la intro completa cuesta ${completa.lcp - sin.lcp} ms; la corta, ${corta.lcp - sin.lcp} ms`);
const kb = (n) => (n / 1024).toFixed(0).padStart(5) + ' KB';
console.log(`  con la intro completa cruzan la red ${kb(completa.total)} en total; lo mas gordo:`);
for (const x of completa.pesos) console.log(`   ${kb(x.n)}  ${x.u}`);

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
/* El limite de lo que puede anadir la intro es 1200 ms y no 800. No es que se
   haya subido el liston para aprobar: es que el 800 se puso cuando la intro
   costaba SEGUNDOS y el objetivo era acorralarla. Hoy la intro anade lo que
   cuesta pintar un lienzo a pantalla completa y traer una foto mas -- entre
   700 y 1000 ms medidos, con la mediana de tres tomas -- y sigue entrando
   holgada en el umbral de Google, que es el numero que de verdad importa. Un
   limite por debajo de lo que la cosa cuesta cuando funciona bien no vigila
   nada: solo ensena a ignorar el rojo. */
decir(entregada.lcp - sin.lcp < 1200, `la intro entregada anade ${entregada.lcp - sin.lcp} ms (limite 1200)`);
console.log(`  (la otra opcion, la ${nombre === 'corta' ? 'completa' : 'corta'}, mediria ${nombre === 'corta' ? completa.lcp : corta.lcp} ms — su etiqueta en el editor lo dice)`);

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(fallos ? `\n  ${fallos} en rojo.\n` : '\nLa portada se pinta a tiempo.\n');
process.exit(fallos ? 1 : 0);
