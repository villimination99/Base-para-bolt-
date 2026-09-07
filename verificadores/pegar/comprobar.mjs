/* EL CODIGO PARA PEGAR, ADELGAZADO, HACE LO MISMO QUE EL GORDO.
   ------------------------------------------------------------------
   El fragmento que se pega en una pagina de Shopify va minificado, y no por
   presumir: la copia que estuvo publicada y se guardaba pesaba 443 KB, la
   version con todo lo anadido despues llego a 521 y dejo de guardarse. Con
   el estilo sin comentarios y los guiones minificados son 407 KB, y cabe.

   Pero minificar es tocar el codigo, y tocar el codigo puede romperlo. Un
   minificador renombra variables, une cadenas, reordena y borra lo que cree
   muerto -- y "lo que cree muerto" es donde estan los sustos.

   COMO SE COMPRUEBA. No comparando el texto: eso da rojos falsos por
   definicion, porque el minificador reescribe. Lo que se compara es el
   COMPORTAMIENTO. Se abre el hub dos veces en el mismo navegador -- una con
   el codigo gordo y otra con el adelgazado -- se hacen las mismas cosas en
   los dos, y se exige que devuelvan exactamente los mismos numeros. Si el
   adelgazado se dejo algo por el camino, alguna cuenta se mueve.

   El mapa 3D y las graficas piden three.js y Chart.js a un CDN que este
   contenedor no alcanza; eso vale igual para las dos versiones, asi que los
   errores de red se descuentan en las dos y la comparacion sigue siendo
   justa. Lo que NO se descuenta es cualquier otro error de JavaScript.

   Uso:  node verificadores/pegar/comprobar.mjs                             */
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';
import { adelgazarFragmento, hayEsbuild } from '../../herramientas/adelgazar.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const TMP = fs.mkdtempSync('/tmp/pegar-');

if (!hayEsbuild()) { console.error('  falta esbuild: npm i --no-save esbuild@0.28.2'); process.exit(1); }

/* El fragmento gordo se arma del maestro igual que lo hace empaquetar-hub,
   y el adelgazado sale de pasarlo por la misma funcion que usa el zip. Asi
   se comparan las dos formas del MISMO codigo de hoy, no un archivo viejo. */
const h = fs.readFileSync(path.join(RAIZ, 'hub/vi-p-completo.html'), 'utf8');
const iS = h.indexOf('  <style>'), fS = h.indexOf('</style>') + 8;
const iB = h.indexOf('<body>') + 6, fB = h.lastIndexOf('</body>');
if (iS < 0 || iB < 6 || fB < 0) { console.error('  el maestro no tiene la forma esperada'); process.exit(1); }
const gordo = h.slice(iS, fS) + '\n' + h.slice(iB, fB).trim();
const flaco = adelgazarFragmento(gordo);

const pagina = (frag) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{margin:0;background:#0A0A0A}</style></head><body>
${frag}
</body></html>`;
fs.writeFileSync(path.join(TMP, 'gordo.html'), pagina(gordo));
fs.writeFileSync(path.join(TMP, 'flaco.html'), pagina(flaco));

const srv = http.createServer((req, res) => {
  fs.readFile(path.join(TMP, decodeURIComponent(req.url.split('?')[0]).replace(/^\//, '')), (err, d) => {
    if (err) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'content-type': 'text/html' });
    res.end(d);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });

/* Los errores que vienen de no alcanzar el CDN son de red, no del codigo, y
   le pasan igual a las dos versiones. Se reconocen por el nombre del modulo
   que no llego, no por "cualquier cosa que suene a red": una lista laxa
   taparia justo el fallo que buscamos. */
const esDeRed = (t) => /jsdelivr|Failed to load resource|Failed to fetch dynamically imported module|Importing a module script failed|Failed to resolve module specifier|Chart is not defined|net::ERR/i.test(t);

async function medir(archivo) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const errores = [];
  p.on('pageerror', e => errores.push(String(e.message)));
  p.on('console', m => { if (m.type() === 'error') errores.push(m.text()); });
  const pedidasMal = [];
  p.on('requestfailed', q => pedidasMal.push(q.url()));
  p.on('response', q => { if (q.status() >= 400) pedidasMal.push(q.status() + ' ' + q.url()); });
  await p.goto(base + archivo, { waitUntil: 'load' });
  await p.waitForTimeout(1200);

  /* Se recorre la pagina hasta tocar fondo de verdad, y se sigue mientras el
     fondo se mueva: el hub crece mientras se monta. Es la misma cautela que
     hizo falta en la bateria del tema, donde medir antes de tiempo daba 59,
     58 y 50 sin que nadie tocara nada. */
  await p.evaluate(async () => {
    const duerme = ms => new Promise(r => setTimeout(r, ms));
    let anterior = -1;
    for (let paso = 0; paso < 300; paso++) {
      window.scrollTo(0, window.scrollY + 400);
      await duerme(55);
      const fondo = document.documentElement.scrollHeight;
      if (window.scrollY + window.innerHeight >= fondo - 2 && window.scrollY === anterior) break;
      anterior = window.scrollY;
    }
    window.scrollTo(0, 0);
  });
  /* Las cifras del hero se cuentan hacia arriba. Leerlas a un tiempo fijo es
     leer una animacion a medias: salian 2|2|1|1 en una carga y 23|16|8|5 en
     la otra, y la bateria acusaba al minificador de algo que era del reloj.
     Se espera a que se QUEDEN QUIETAS -- seis lecturas iguales seguidas, 1,2
     segundos -- que es lo unico comparable entre dos cargas.

     Aqui NO se exige que lleguen a su data-cuenta, y merece explicacion: dos
     de las cuatro se recalculan a partir de contenido que llega del CDN, y
     este contenedor no alcanza el CDN. En el tema, donde three.js y Chart.js
     viajan dentro, la bateria de vi-p las ve terminar en 27, 19, 9 y 6. Lo
     que importa aqui es otra cosa: que el gordo y el adelgazado digan lo
     mismo. */
  await p.evaluate(async () => {
    const leer = () => [...document.querySelectorAll('#vill-hub .hero-stat strong')]
      .map(e => e.textContent.trim()).join('|');
    let anterior = leer(), quietas = 0;
    for (let i = 0; i < 60 && quietas < 6; i++) {
      await new Promise(r => setTimeout(r, 200));
      const ahora = leer();
      quietas = (ahora === anterior) ? quietas + 1 : 0;
      anterior = ahora;
    }
  });

  const r = await p.evaluate(() => {
    const raiz = document.getElementById('vill-hub');
    const q = (s) => raiz.querySelectorAll(s).length;
    return {
      hub: !!raiz,
      nodos: raiz ? raiz.querySelectorAll('*').length : 0,
      marcados: q('.vp-ent'),
      vistos: q('.vp-ent.vp-visto'),
      musculos: q('[data-muscle], .mm-item, .muscle-btn'),
      secciones: q('section'),
      botones: q('button'),
      enlaces: q('a[href]'),
      cifras: [...raiz.querySelectorAll('.hero-stat strong')].map(e => e.textContent.trim()).join('|'),
      cifrasDestino: [...raiz.querySelectorAll('.hero-stat strong')].map(e => (e.dataset.cuenta || '?').trim()).join('|'),
      titulos: [...raiz.querySelectorAll('h2')].map(e => e.textContent.trim()).join('|').length,
      desborde: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      alto: document.documentElement.scrollHeight,
    };
  });
  r.pedidasMal = pedidasMal;
  r.errores = errores.filter(t => !esDeRed(t));
  r.erroresDeRed = errores.length - r.errores.length;
  await ctx.close();
  return r;
}

const A = await medir('gordo.html');
const B = await medir('flaco.html');
await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });

let mal = 0;
const decir = (ok, txt) => { if (!ok) mal++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };

console.log('');
console.log(`  gordo ${(gordo.length / 1024).toFixed(0)} KB · adelgazado ${(flaco.length / 1024).toFixed(0)} KB` +
            `  (${(100 * (gordo.length - flaco.length) / gordo.length).toFixed(0)} % menos)`);
console.log(`  (errores de red descontados: ${A.erroresDeRed} y ${B.erroresDeRed}; son el CDN, que aqui no se alcanza)`);
console.log('');

decir(B.hub, 'el hub se monta con el codigo adelgazado');
decir(A.errores.length === 0, `el codigo gordo no lanza errores (${A.errores.length})`);
decir(B.errores.length === 0, `el adelgazado tampoco (${B.errores.length})`);
for (const e of [...A.errores, ...B.errores].slice(0, 4)) console.log('        ' + e.slice(0, 130));
for (const u of [...new Set([...A.pedidasMal, ...B.pedidasMal])].slice(0, 6)) console.log('        peticion fallida: ' + u.slice(0, 120));

/* Se comparan HECHOS del documento, no animaciones en vuelo.

   Las cifras del hero se quedaron fuera de esta lista despues de intentarlo
   de tres maneras. El contador va con requestAnimationFrame, y en este
   contenedor el dibujado es por software: los fotogramas llegan cuando
   llegan. El archivo gordo tarda mas en analizarse que el adelgazado, asi
   que a la misma hora de reloj van por distinto punto de la cuenta -- 2|2|1|1
   contra 20|14|7|4 -- y eso no dice nada del minificador, dice que uno pesa
   100 KB mas. Comparar una animacion a medias entre dos paquetes de distinto
   tamano es medir la maquina, no el codigo.

   Lo que si es comparable es a donde APUNTAN esas cifras, que esta escrito en
   el marcado (data-cuenta) y no depende de ningun reloj. Y que terminen en su
   numero se comprueba donde se puede comprobar de verdad: en la bateria del
   tema, que no depende de ningun CDN y las ve acabar en 27, 19, 9 y 6. */
const iguales = ['nodos', 'marcados', 'vistos', 'musculos', 'secciones', 'botones', 'enlaces', 'cifrasDestino', 'titulos'];
for (const k of iguales) decir(String(A[k]) === String(B[k]),
  String(A[k]) === String(B[k]) ? `${k}: ${A[k]} en los dos` : `${k}: gordo ${A[k]} · adelgazado ${B[k]}`);

decir(B.marcados > 0 && B.vistos === B.marcados, `todo entra al bajar (${B.vistos} de ${B.marcados})`);
decir(B.desborde === 0, `nada se sale de lado (${B.desborde} px)`);
/* El alto puede bailar unos pixeles entre dos cargas por las fuentes y las
   imagenes; lo que no puede es cambiar de escala. */
decir(Math.abs(A.alto - B.alto) < A.alto * 0.02, `la pagina mide lo mismo (${A.alto} vs ${B.alto} px)`);

console.log(mal
  ? `\n  ${mal} en rojo: el codigo para pegar NO se comporta igual.\n`
  : '\nEl codigo adelgazado hace exactamente lo mismo que el gordo.\n');
process.exit(mal ? 1 : 0);
