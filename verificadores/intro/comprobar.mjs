/* Comprueba la intro "Pulso / Malla" en un navegador real.
   ------------------------------------------------------------------
   Nacio de fallos que leer el codigo no habria encontrado nunca:

   1. El emblema pasa toda la secuencia congelado en el primer fotograma de
      logoAppear, que es scale(0.5). getBoundingClientRect devolvia por tanto
      LA MITAD del radio real, asi que las particulas formaban un anillo del
      tamano equivocado y la amplitud del latido se quedaba en un munon. Solo
      se ve midiendo geometria de verdad.
   2. Habia un hueco con la pantalla practicamente vacia entre actos. Solo se
      ve contando pixeles encendidos fotograma a fotograma.
   3. Los lienzos decorativos del fondo seguian corriendo DETRAS de la intro,
      que los tapa por completo: la pagina iba a 30 fps en vez de 60 justo en
      los segundos de los que depende la primera impresion. Solo se ve
      midiendo con el navegador estrangulado.
   4. La secuencia tiene dos duraciones y dos puertas. Si la puerta de la
      tienda se retrasara hasta el final, cada primera visita pagaria el peaje
      entero. Aqui se vigila con un presupuesto en segundos.

   Uso:  node verificadores/intro/comprobar.mjs                             */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

/* El marcado es el del snippet real. Si el snippet cambia de estructura, esta
   prueba deja de reflejarlo, asi que se comprueba aparte que las piezas que
   se usan aqui siguen estando alli. */
const SNIPPET = fs.readFileSync(path.join(RAIZ, 'theme/snippets/splash-intro.liquid'), 'utf8');
const PIEZAS = ['splash-canvas', 'splash-emblem', 'splash-enter-btn', 'data-splash-skip',
                'data-splash-frases', 'splash-logotipo', 'data-duracion', 'intro.js'];

const AJUSTES = JSON.parse(fs.readFileSync(path.join(RAIZ, 'theme/config/settings_schema.json'), 'utf8'));
const DATOS = JSON.parse(fs.readFileSync(path.join(RAIZ, 'theme/config/settings_data.json'), 'utf8')).current;

const FRASES = String(DATOS.splash_frases || '').split('\n').map(s => s.trim()).filter(Boolean);

/* Una foto sintetica para la sala. No hace falta que sea la de la tienda: lo
   que esta prueba mide de ella es su COSTE y su sitio en la pila de capas --
   una imagen a pantalla completa, con su animacion de camara y su vineta
   encima -- y eso no depende de lo que se vea en ella. Va como data URI para
   que la bateria siga funcionando sin red y sin ficheros sueltos. */
const FOTO_SALA = 'data:image/svg+xml,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1425">' +
  '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">' +
  '<stop offset="0" stop-color="#12303f"/><stop offset="1" stop-color="#05070d"/>' +
  '</linearGradient></defs><rect width="900" height="1425" fill="url(#g)"/>' +
  '<g stroke="#2b6d86" stroke-width="6" opacity=".5">' +
  '<path d="M60 1425V620h140v805M700 1425V620h140v805M0 900h900M0 1120h900"/></g></svg>');

/* Y un logotipo apaisado con las proporciones del de verdad. */
const LOGO = 'data:image/svg+xml,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="200">' +
  '<rect width="900" height="200" fill="none"/>' +
  '<text x="450" y="140" font-family="sans-serif" font-size="120" font-weight="700"' +
  ' text-anchor="middle" fill="#eaf6ff">VILLUMINATION</text></svg>');

/* EL BANCO DE PRUEBAS TIENE QUE SER EL SNIPPET, NO UNA VERSION SUYA DE HACE
   TRES RONDAS. Esta pagina se escribe a mano porque aqui no hay motor de
   Liquid, y eso la deja libre de separarse del snippet sin que nadie se
   entere: durante un tiempo esta bateria midio una intro con dos halos y dos
   anillos que ya no existian, y SIN la sala, sin las particulas de fondo y
   sin el logotipo, que si existen. Se median los fotogramas de una escena
   distinta de la que ve el cliente.

   Debajo hay una comprobacion que compara las clases de los dos y falla si
   aparece una que solo esta en uno de los dos lados. Mientras eso este en
   verde, lo que se mide aqui es lo que se envia. */
function pagina(duracion) {
  const trozos = FRASES.slice(0, 3)
    .map((f, i) => `<p class="splash-frase" data-i="${i}">${f}</p>`).join('\n');
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="file://${ASSETS}/villumination.css">
<style>:root{--neon-cyan:#00d4ff;--neon-pink:#ff2ecb;--neon-green:#00e87b;--neon-purple:#7b2fff;
--color-bg:#000;--font-heading:system-ui;--font-body:system-ui}
body{margin:0;background:#000;color:#fff;font-family:system-ui}</style></head><body>
<div id="splash-intro" class="splash-intro" data-splash data-duracion="${duracion}" data-splash-3d role="dialog" aria-label="Villumination">
  <div class="splash-bg"></div>
  <div class="splash-escena" aria-hidden="true">
    <img class="splash-escena-img" data-splash-escena src="${FOTO_SALA}"
         width="900" height="1425" alt="" loading="eager" decoding="async">
  </div>
  <canvas id="splash-canvas" class="splash-canvas" aria-hidden="true"></canvas>
  <div class="splash-particles" aria-hidden="true">
    <div class="splash-particle"></div><div class="splash-particle"></div><div class="splash-particle"></div>
    <div class="splash-particle"></div><div class="splash-particle"></div><div class="splash-particle"></div>
  </div>
  <span class="splash-grano" aria-hidden="true"></span>
  <span class="splash-corte" aria-hidden="true"></span>
  <button class="splash-skip" type="button" data-splash-skip>SALTAR</button>
  <div class="splash-content">
    <div class="splash-emblem">
      <span class="splash-halo splash-halo-1" aria-hidden="true"></span>
      <span class="splash-ring" aria-hidden="true">
        <svg viewBox="0 0 200 200" fill="none">
          <defs><linearGradient id="splash-rg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#00d4ff"/><stop offset="33%" stop-color="#7b2fff"/><stop offset="66%" stop-color="#ff2ecb"/><stop offset="100%" stop-color="#00d4ff"/></linearGradient></defs>
          <circle cx="100" cy="100" r="96" stroke="url(#splash-rg)" stroke-width="2" stroke-dasharray="8 6" stroke-linecap="round" opacity="0.75"/>
        </svg>
      </span>
      <span class="splash-core"><span class="splash-mono">VI</span></span>
    </div>
    <h1 class="splash-title splash-title--logo">
      <img class="splash-logotipo" src="${LOGO}" width="900" height="200"
           alt="Villumination" loading="eager" decoding="async" fetchpriority="high">
    </h1>
    <p class="splash-tagline">TRANSFORMA TU CUERPO.</p>
    <div class="splash-frases" data-splash-frases aria-hidden="true">
${trozos}
    </div>
    <button id="splash-enter" class="splash-enter-btn" type="button"><span>ENTRAR</span></button>
  </div>
</div>
<script>window.theme={routes:{},settings:{splashOnce:false,splash3d:true},strings:{}};
window.__t0=performance.now();</script>
<script src="file://${ASSETS}/intro.js"></script>
<script src="file://${ASSETS}/base.js"></script>
<script src="file://${ASSETS}/effects.js"></script>
</body></html>`;
}

const TMP = path.join(AQUI, '.pagina-de-prueba.html');
const TMP_CORTA = path.join(AQUI, '.pagina-de-prueba-corta.html');
fs.writeFileSync(TMP, pagina('completa'));
fs.writeFileSync(TMP_CORTA, pagina('corta'));
const URL_PRUEBA = 'file://' + TMP;
const URL_CORTA = 'file://' + TMP_CORTA;

const APARATOS = {
  'iPhone 12':  { viewport: { width: 390, height: 844 },  isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
  'iPhone SE':  { viewport: { width: 375, height: 667 },  isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
  'iPad':       { viewport: { width: 820, height: 1180 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 },
  'Escritorio': { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 },
  'Panoramica': { viewport: { width: 2560, height: 700 }, deviceScaleFactor: 1 },
};

const navegador = await chromium.launch({ executablePath: CHROME });
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

/* Espera al instante EXACTO de la secuencia. Con waitForTimeout el coste de
   cada captura (300 ms largos) se acumulaba y las medidas salian medio
   segundo tarde, que en una secuencia de tres segundos es otra escena. */
const enElInstante = (p, ms) => p.evaluate(m => new Promise(r => {
  (function esperar() {
    if (performance.now() - window.__t0 >= m) r();
    else requestAnimationFrame(esperar);
  })();
}), ms);

async function abrir(nombre, extra, url) {
  const ctx = await navegador.newContext(Object.assign({}, APARATOS[nombre], extra || {}));
  const p = await ctx.newPage();
  const errores = [];
  p.on('pageerror', e => errores.push(e.message));
  await p.goto(url || URL_PRUEBA);
  return { ctx, p, errores };
}

/* Zona del emblema: un cuadro de 3,2 radios centrado en el, remuestreado a
   120x120, contando los pixeles cuya suma RGB pasa de 90. */
async function encendido(p, ms) {
  const g = await p.evaluate(() => {
    const c = document.querySelector('[data-splash]');
    const e = c.querySelector('.splash-emblem');
    const r = e.getBoundingClientRect(), rc = c.getBoundingClientRect();
    return { cx: r.left - rc.left + r.width / 2, cy: r.top - rc.top + r.height / 2,
             R: (e.offsetWidth || r.width) / 2 };
  });
  await enElInstante(p, ms);
  const foto = await p.screenshot();
  return p.evaluate(async ([b64, g]) => {
    const img = new Image();
    img.src = 'data:image/png;base64,' + b64;
    await img.decode();
    const esc = img.width / document.documentElement.clientWidth;
    const lado = g.R * 3.2 * esc;
    const c = document.createElement('canvas');
    c.width = c.height = 120;
    const x = c.getContext('2d');
    x.drawImage(img, (g.cx - g.R * 1.6) * esc, (g.cy - g.R * 1.6) * esc, lado, lado, 0, 0, 120, 120);
    const d = x.getImageData(0, 0, 120, 120).data;
    let n = 0;
    for (let i = 0; i < d.length; i += 4) if (d[i] + d[i + 1] + d[i + 2] > 90) n++;
    return n / (120 * 120);
  }, [foto.toString('base64'), g]);
}

console.log('\n--- El banco de pruebas es la intro que se envia ---');
/* Compara las clases splash-* del snippet real con las de la pagina que mide
   esta bateria. Si alguien anade una capa al snippet, o quita una de aqui, el
   resto de la bateria pasaria a medir una escena que no existe -- y eso ya
   paso: se estuvo midiendo con dos halos y dos anillos de sobra y sin la
   sala, las particulas ni el logotipo. Con esto no puede volver a pasar en
   silencio. */
{
  const clases = (txt) => {
    const fuera = new Set();
    const re = /class="([^"]+)"/g;
    let m;
    while ((m = re.exec(txt))) {
      for (const c of m[1].split(/\s+/)) if (c.indexOf('splash-') === 0) fuera.add(c);
    }
    return fuera;
  };
  const sinComentarios = SNIPPET.replace(/\{%-?\s*comment[\s\S]*?endcomment\s*-?%\}/g, '');
  const enSnippet = clases(sinComentarios);
  const enBanco = clases(pagina('completa'));
  const soloSnippet = [...enSnippet].filter((c) => !enBanco.has(c));
  const soloBanco = [...enBanco].filter((c) => !enSnippet.has(c));
  decir(soloSnippet.length === 0,
    soloSnippet.length ? `el snippet trae capas que esta bateria NO mide: ${soloSnippet.join(', ')}`
                       : `las ${enSnippet.size} capas del snippet estan todas en el banco de pruebas`);
  decir(soloBanco.length === 0,
    soloBanco.length ? `esta bateria mide capas que el snippet YA NO trae: ${soloBanco.join(', ')}`
                     : 'el banco no mide ninguna capa que ya no exista');
}

console.log('\n--- El snippet y los ajustes tienen las piezas que esto usa ---');
for (const pieza of PIEZAS) decir(SNIPPET.includes(pieza), `el snippet declara "${pieza}"`);
const ids = AJUSTES.flatMap(g => (g.settings || []).map(s => s.id));
for (const id of ['splash_duracion', 'splash_frases'])
  decir(ids.includes(id), `el editor de Shopify ofrece el ajuste "${id}"`);
decir(FRASES.length >= 1 && FRASES.length <= 3,
  `hay ${FRASES.length} frase(s) de motivacion configurada(s), y el marcado pinta como mucho 3`);
decir(FRASES.every(f => f.length > 0 && f.length <= 60),
  'ninguna frase esta vacia ni pasa de 60 caracteres (mas no cabe en un movil)');

console.log('\n--- Composicion: el pico del latido cae bajo el anillo del emblema ---');
for (const nombre of Object.keys(APARATOS)) {
  const { ctx, p } = await abrir(nombre);
  const g = await p.evaluate(() => {
    const caja = document.querySelector('[data-splash]');
    const em = caja.querySelector('.splash-emblem');
    const r = em.getBoundingClientRect(), rc = caja.getBoundingClientRect();
    return { H: caja.clientHeight, W: caja.clientWidth,
             cy: r.top - rc.top + r.height / 2,
             radio: (em.offsetWidth || r.width) / 2,
             escalado: Math.abs(r.width - em.offsetWidth) > 2 };
  });
  let alto = Math.min(g.H * 0.15, g.radio * 1.45, g.W * 0.30);
  let yBase = g.cy + g.radio * 1.10 + alto;
  if (yBase > g.H * 0.90) yBase = g.H * 0.90;
  if (yBase - alto < g.cy + g.radio * 0.55) alto = yBase - g.cy - g.radio * 0.55;
  const margen = (yBase - alto) - (g.cy + g.radio);
  decir(margen > 0 && margen < g.radio * 0.45,
    `${nombre.padEnd(11)} la punta del pico queda ${margen.toFixed(0)} px bajo el anillo (radio ${g.radio.toFixed(0)}, amplitud ${alto.toFixed(0)})`);
  if (nombre === 'iPhone 12') {
    decir(g.escalado, 'el emblema esta escalado durante la secuencia (por eso el radio NO puede salir de getBoundingClientRect)');
  }
  await ctx.close();
}

/* ---- COMPROBACION RETIRADA: "la malla tiene perspectiva de verdad" ----
   Se intento dos veces y las dos salieron mal. Queda escrito para que nadie
   vuelva a intentarlo por el mismo camino.

   INTENTO 1. Interceptar ctx.arc y mirar el rango de radios de los nodos.
   Daba verde con un abanico de x56, pero ese 56 no era un nodo: era el
   degradado radial del nucleo, que tambien se dibuja con arc. Habria pasado
   igual con la perspectiva rota. Y filtrando por tamano tampoco vale: el
   radio de cada nodo ya varia de por si, asi que un rango ancho no demuestra
   nada.

   INTENTO 2. Medir la silueta: en una esfera proyectada las aristas se
   amontonan en el borde y se separan en el centro, asi que la densidad de
   pixeles encendidos en el anillo 0,80-1,00 del radio deberia superar
   claramente a la del disco central. Se calibro apagando la perspectiva
   (k = 1 para todos los nodos), tres pasadas de cada version:

       con perspectiva:  1,28   1,36   1,39
       sin perspectiva:  1,29   1,35   1,35

   Los dos grupos se solapan ENTEROS. La medida no distingue nada, asi que
   cualquier umbral habria sido decorativo. Se retira: un control que no puede
   fallar sobre la version rota es peor que no tener control, porque da
   confianza falsa.

   Lo que si queda cubierto, y con calibracion de verdad, es que la malla
   ESTE: la comprobacion de "el centro nunca se apaga" de aqui abajo esta
   calibrada precisamente contra la version con la malla apagada (11,5 %
   contra 5,1 %). Si la malla desapareciera, eso se pone rojo. */

console.log('\n--- La secuencia nunca se queda en blanco ---');
/* CALIBRADO CONTRA LA VERSION ROTA Y SOBRE ESTA MISMA PAGINA. Las dos cosas
   importan: una calibracion hecha con otro marcado de prueba da numeros que
   aqui no valen, y ya paso una vez -- el sabotaje pasaba el control. La
   version rota es la misma secuencia con la malla apagada, que es la
   regresion que de verdad importa: en ese tramo la malla es lo UNICO que hay
   en el centro. Dos pasadas de cada version, en un iPhone 12:

       instante   rota    buena
        1300 ms   5,2     13,7
        1600 ms   5,2     13,0
        1900 ms   5,1     13,4

   El peor de la buena es 13,0 % y el mejor de la rota 5,2 %: el umbral va en
   el 8 %, a mitad de camino y con un 60 % de margen por los dos lados. Vuelto a
   medir despues de meter el gimnasio y la foto de la sala, que tambien aportan
   luz a esa zona: la separacion aguanta porque el suelo y la foto iluminan
   IGUAL a las dos versiones, y lo que de verdad se echa en falta cuando la
   malla no esta sigue siendo la malla.

   La ventana se corta en 1900 ms y no mas tarde por un dato medido: a 2200 ms
   la version rota dio 3,4 % en una pasada y 7,9 % en otra, porque ahi las
   particulas ya empiezan a llegar al anillo y tapan el agujero. Con 2200
   dentro, el margen se quedaba en un 20 % y el control se volvia inestable.
   Y antes de 1300 ms tampoco: alli manda el estallido y las dos versiones dan
   lo mismo (10-11 %). */
{
  const { ctx, p, errores } = await abrir('iPhone 12');
  const INSTANTES = [900, 1100, 1300, 1600, 1900, 2200, 2500, 2800, 3100, 3400];
  const VENTANA = [1300, 1900];
  const MINIMO = 0.08;
  const medidas = [];
  for (const ms of INSTANTES) medidas.push([ms, await encendido(p, ms)]);
  const dentro = medidas.filter(m => m[0] >= VENTANA[0] && m[0] <= VENTANA[1]);
  const flojos = dentro.filter(m => m[1] < MINIMO);
  const peor = dentro.reduce((a, b) => b[1] < a[1] ? b : a);
  decir(flojos.length === 0,
    `el centro nunca se apaga entre ${VENTANA[0]} y ${VENTANA[1]} ms (el mas flojo: ${(peor[1] * 100).toFixed(1)} % a ${peor[0]} ms, minimo exigido ${(MINIMO * 100).toFixed(0)} %)`);
  console.log('        zona del emblema encendida: ' +
    medidas.map(m => `${m[0]}:${(m[1] * 100).toFixed(1)}%`).join('  '));
  if (flojos.length) {
    console.log('        por debajo del minimo: ' +
      flojos.map(m => `${m[0]}ms=${(m[1] * 100).toFixed(1)}%`).join(', '));
  }
  decir(errores.length === 0, `sin errores de JavaScript durante la secuencia (${errores.length})`);
  await ctx.close();
}

console.log('\n--- Alrededor del logotipo no hay ruido ---');
/* Se retiraron cinco piezas que no cumplian ninguna funcion y competian con la
   marca justo cuando aparece: la barra de progreso (fingia una carga que no
   existe), el segundo halo, los dos anillos que latian, los enlaces entre
   particulas vecinas y el barrido tipo radar. Esto vigila que no vuelvan por
   inercia en una ronda futura. */
for (const [pieza, donde] of [
  ['splash-loader', 'la barra de progreso que no cargaba nada'],
  ['splash-halo-2', 'el segundo halo'],
  ['splash-pulse', 'los anillos que latian'],
]) decir(!SNIPPET.includes(pieza), `el snippet ya no trae ${donde}`);
{
  const motor = fs.readFileSync(path.join(ASSETS, 'intro.js'), 'utf8');
  decir(!/ctx\.arc\(cx, cy, radio \* 1\.07/.test(motor), 'el motor ya no pinta el barrido tipo radar');
}

console.log('\n--- Presupuesto de espera: las dos puertas ---');
/* La de arriba abre la TIENDA y la de abajo cierra la secuencia. Si alguien
   alarga la secuencia sin mover la primera, cada primera visita paga el peaje
   entero, y eso son ventas perdidas. Por eso hay un techo en segundos. */
for (const [modo, url, techoPuerta, techoFin] of [
  ['completa', URL_PRUEBA, 2.6, 4.6],
  ['corta', URL_CORTA, 2.6, 3.0],
]) {
  const { ctx, p, errores } = await abrir('iPhone 12', {}, url);
  const r = await p.evaluate(() => new Promise(res => {
    const c = document.querySelector('[data-splash]');
    const t0 = window.__t0;
    let tp = 0, tl = 0;
    (function mirar() {
      const t = (performance.now() - t0) / 1000;
      if (!tp && c.classList.contains('intro-puerta')) tp = t;
      if (!tl && c.classList.contains('intro-lista')) tl = t;
      if ((tp && tl) || t > 6) res({ tp, tl });
      else requestAnimationFrame(mirar);
    })();
  }));
  decir(r.tp > 0 && r.tp <= techoPuerta,
    `${modo.padEnd(9)} el boton de entrar se habilita a los ${r.tp.toFixed(2)} s (techo ${techoPuerta} s)`);
  decir(r.tl > 0 && r.tl <= techoFin,
    `${modo.padEnd(9)} la secuencia termina a los ${r.tl.toFixed(2)} s (techo ${techoFin} s)`);
  decir(r.tp <= r.tl, `${modo.padEnd(9)} la puerta de la tienda no llega despues del final`);
  decir(errores.length === 0, `${modo.padEnd(9)} sin errores de JavaScript`);
  await ctx.close();
}

console.log('\n--- Las frases se ven y se leen ---');
{
  const { ctx, p, errores } = await abrir('iPhone 12');
  /* Se muestrea a 2,5 s y no a 1,9 s por una razon medida: la frase entra a
     los 1,45 s y su desplazamiento dura 0,8 s, asi que a 1,9 s TODAVIA esta
     entrando. La comprobacion tenia razon y el que estaba mal era el instante
     elegido. Aqui ya lleva un cuarto de segundo colocada. */
  await enElInstante(p, 2500);
  const r = await p.evaluate(() => {
    const vis = Array.prototype.filter.call(
      document.querySelectorAll('.splash-frase'),
      e => +getComputedStyle(e).opacity > 0.5);
    if (!vis.length) return { n: 0 };
    const e = vis[0], b = e.getBoundingClientRect();
    const cs = getComputedStyle(e);
    // El bloque tiene que haber terminado de entrar: ni desplazado ni borroso.
    // Antes esto miraba las palabras una a una; ahora el revelado es de bloque,
    // que en un fotograma congelado nunca parece texto roto.
    const m = new DOMMatrixReadOnly(cs.transform);
    return { n: vis.length, texto: e.textContent.trim(), color: cs.color,
             abajo: Math.round(b.bottom), alto: Math.round(b.height),
             ancho: Math.round(b.width),
             desplazada: Math.abs(m.f) > 1 || /blur\((?!0px)/.test(cs.filter || ''),
             vp: document.documentElement.clientWidth };
  });
  decir(r.n === 1, `a 2,5 s hay exactamente una frase visible (hay ${r.n})`);
  if (r.n) {
    decir(!r.desplazada, `la frase ha terminado de entrar, sin desplazamiento ni desenfoque: "${r.texto}"`);
    decir(r.ancho <= r.vp, `la frase cabe de ancho (${r.ancho} px de ${r.vp} disponibles)`);
    // La frase va sobre el fondo oscuro de la intro: se comprueba el contraste
    // real del color de texto contra ese fondo, no contra un blanco supuesto.
    const cont = await p.evaluate(col => {
      const lum = c => {
        const v = c.match(/\d+(\.\d+)?/g).slice(0, 3).map(Number).map(n => {
          n /= 255; return n <= 0.03928 ? n / 12.92 : Math.pow((n + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
      };
      const a = lum(col), b = lum('rgb(5, 6, 12)');
      return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    }, r.color);
    decir(cont >= 4.5, `contraste de la frase sobre el fondo de la intro: ${cont.toFixed(1)}:1 (AA pide 4,5)`);
  }
  // No pueden solaparse con el boton de entrar
  await enElInstante(p, 2500);
  const solape = await p.evaluate(() => {
    const f = document.querySelector('.splash-frase[data-i]');
    const b = document.querySelector('.splash-enter-btn');
    const rf = f.getBoundingClientRect(), rb = b.getBoundingClientRect();
    return rf.bottom > rb.top ? Math.round(rf.bottom - rb.top) : 0;
  });
  decir(solape === 0, `las frases no se montan sobre el boton de entrar${solape ? ` (se solapan ${solape} px)` : ''}`);
  decir(errores.length === 0, `sin errores de JavaScript (${errores.length})`);
  await ctx.close();
}

console.log('\n--- La puerta de la tienda siempre aparece ---');
for (const [nombre, extra, espera] of [
  ['iPhone 12', {}, 4400],
  ['iPhone 12', { reducedMotion: 'reduce' }, 600],
  ['Escritorio', {}, 4400],
]) {
  const { ctx, p, errores } = await abrir(nombre, extra);
  await p.waitForTimeout(espera);
  const r = await p.evaluate(() => {
    const c = document.querySelector('[data-splash]');
    const e = document.querySelector('.splash-enter-btn');
    const s = document.querySelector('.splash-skip');
    const f = document.querySelector('.splash-frases');
    return { lista: c.classList.contains('intro-lista'),
             op: +getComputedStyle(e).opacity,
             alto: Math.round(s.getBoundingClientRect().height),
             sop: +getComputedStyle(s).opacity,
             frasesVisibles: f ? getComputedStyle(f).display !== 'none' &&
               Array.prototype.some.call(f.children, x => +getComputedStyle(x).opacity > 0.5) : false };
  });
  const etiqueta = extra.reducedMotion ? `${nombre} (mov. reducido)` : nombre;
  decir(r.lista && r.op > 0.9, `${etiqueta.padEnd(26)} el boton de entrar esta visible (opacidad ${r.op.toFixed(2)})`);
  decir(r.sop > 0.9 && r.alto >= 44, `${etiqueta.padEnd(26)} saltar es visible y tiene ${r.alto} px de area tactil`);
  // En el fotograma FINAL las frases ya se han ido y manda el logotipo:
  // mostrarlas ahi seria inventar un estado que la secuencia nunca tiene.
  decir(!r.frasesVisibles, `${etiqueta.padEnd(26)} en el fotograma final no queda ninguna frase`);
  decir(errores.length === 0, `${etiqueta.padEnd(26)} sin errores de JavaScript`);
  await ctx.close();
}

console.log('\n--- Nunca hay dos frases en pantalla a la vez ---');
/* Salio en una captura del cliente: "CADA REPETICION" encima de "EL LIMITE LO
   PONES TU". Las ventanas estaban escritas a mano con 0,10 s de hueco y el
   fundido dura 0,45 s, asi que se superponian 0,22 s. Ahora se calculan, y
   esto lo vigila muestreando la secuencia entera cada 100 ms en vez de mirar
   dos instantes sueltos: un solape de dos decimas se cuela entre dos muestras
   espaciadas, no entre cuarenta. */
{
  const { ctx, p, errores } = await abrir('iPhone 12');
  const solapes = await p.evaluate(() => new Promise(res => {
    const malos = [];
    const t0 = window.__t0;
    (function mirar() {
      const t = (performance.now() - t0) / 1000;
      const vis = Array.prototype.filter.call(
        document.querySelectorAll('.splash-frase'),
        e => +getComputedStyle(e).opacity > 0.08).length;
      if (vis > 1) malos.push(+t.toFixed(2));
      if (t > 4.6) res(malos);
      else setTimeout(mirar, 100);
    })();
  }));
  decir(solapes.length === 0,
    `en ningun instante hay mas de una frase visible${solapes.length ? ' (se solapan en ' + solapes.slice(0, 6).join(', ') + ' s)' : ''}`);
  decir(errores.length === 0, `sin errores de JavaScript (${errores.length})`);
  await ctx.close();
}

console.log('\n--- La esfera nunca toca el borde ---');
/* Reportado con captura: la malla salia cortada por la izquierda. El radio
   proyectado maximo no es R sino 1,083 R, porque con perspectiva los nodos
   inclinados hacia el visitante se separan mas del centro que la silueta.
   Sumando el desvio de la camara, el latido y la anticipacion del colapso,
   el tope de ancho tuvo que bajar de W*0.40 a W*0.319. Aqui se mide el pixel
   encendido mas a la izquierda y mas a la derecha en el peor momento. */
for (const nombre of Object.keys(APARATOS)) {
  const { ctx, p } = await abrir(nombre);
  let peor = 1e9, cuando = 0;
  for (const ms of [1500, 1900, 2300, 2700, 3100, 3300]) {
    await enElInstante(p, ms);
    const foto = await p.screenshot();
    const m = await p.evaluate(async b64 => {
      const img = new Image();
      img.src = 'data:image/png;base64,' + b64;
      await img.decode();
      const c = document.createElement('canvas');
      c.width = img.width; c.height = img.height;
      const x = c.getContext('2d');
      x.drawImage(img, 0, 0);
      const d = x.getImageData(0, 0, img.width, img.height).data;
      let izq = img.width, der = -1;
      // Solo la banda donde vive la malla, para no medir el suelo ni el boton.
      const y0 = Math.floor(img.height * 0.14), y1 = Math.floor(img.height * 0.60);
      for (let y = y0; y < y1; y += 2) {
        for (let px = 0; px < img.width; px++) {
          const k = (y * img.width + px) * 4;
          if (d[k] + d[k + 1] + d[k + 2] > 200) {
            if (px < izq) izq = px;
            if (px > der) der = px;
          }
        }
      }
      const esc = img.width / document.documentElement.clientWidth;
      return { izq: izq / esc, der: (img.width - der) / esc, ancho: document.documentElement.clientWidth };
    }, foto.toString('base64'));
    const margen = Math.min(m.izq, m.der);
    if (margen < peor) { peor = margen; cuando = ms; }
  }
  decir(peor >= 8,
    `${nombre.padEnd(11)} margen minimo al borde: ${peor.toFixed(0)} px (a ${cuando} ms)`);
  await ctx.close();
}

console.log('\n--- Los simbolos de los lados no han vuelto ---');
{
  const motor = fs.readFileSync(path.join(ASSETS, 'intro.js'), 'utf8')
    .replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '');
  decir(!/function\s+rack\s*\(/.test(motor) && !/\brack\s*\(\s*-?1/.test(motor),
    'el motor no dibuja siluetas laterales: eso es lo que el cliente veia como simbolos sueltos');
}

console.log('\n--- El cierre es un corte, no un desvanecido ---');
{
  const { ctx, p, errores } = await abrir('iPhone 12');
  await enElInstante(p, 2600);
  const t = await p.evaluate(() => new Promise(res => {
    const c = document.querySelector('[data-splash]');
    const t0 = performance.now();
    document.querySelector('[data-splash-skip]').click();
    (function mirar() {
      const cs = getComputedStyle(c);
      if (+cs.opacity < 0.02 || cs.display === 'none') res((performance.now() - t0) / 1000);
      else if (performance.now() - t0 > 2000) res(99);
      else requestAnimationFrame(mirar);
    })();
  }));
  decir(t <= 0.45, `del dedo a la tienda pasan ${t.toFixed(2)} s (techo 0,45 s)`);
  decir(errores.length === 0, `sin errores de JavaScript (${errores.length})`);
  await ctx.close();
}

console.log('\n--- Se puede saltar desde el primer fotograma ---');
{
  const { ctx, p } = await abrir('iPhone 12');
  await enElInstante(p, 120);
  await p.click('[data-splash-skip]');
  await p.waitForTimeout(300);
  const cerrada = await p.evaluate(() => document.querySelector('[data-splash]').classList.contains('dismissed'));
  decir(cerrada, 'pulsar saltar a los 120 ms cierra la intro sin esperar a la secuencia');
  await ctx.close();
}

console.log('\n--- Compuerta: el fondo no trabaja detras de la intro ---');
/* Los observadores de interseccion ven los lienzos del fondo dentro del
   viewport, porque la intro esta ENCIMA, no delante en el flujo. Si no se les
   para, se paga el doble de trabajo por algo que nadie ve. Se mira el lienzo
   ambiental de effects.js: parado no cambia entre dos muestras; corriendo, si.
   Contar peticiones de fotograma no vale: la propia intro pide las suyas y
   enmascaran el resultado. */
{
  const { ctx, p, errores } = await abrir('Escritorio');
  const firma = () => p.evaluate(() => {
    const c = document.querySelector('.fx-ambient-canvas');
    return c ? c.toDataURL().slice(-160) : 'sin-lienzo';
  });
  await p.waitForTimeout(700);
  const a1 = await firma(); await p.waitForTimeout(500); const a2 = await firma();
  decir(a1 !== 'sin-lienzo', 'el lienzo ambiental del fondo existe');
  decir(a1 === a2, 'con la intro puesta, el fondo esta parado');
  await p.click('[data-splash-skip]');
  await p.waitForTimeout(700);
  const d1 = await firma(); await p.waitForTimeout(500); const d2 = await firma();
  decir(d1 !== d2, 'al cerrarse la intro, el fondo vuelve a animarse');
  decir(errores.length === 0, 'sin errores de JavaScript');
  await ctx.close();
}

console.log('\n--- Fluidez con la CPU estrangulada ---');
/* Una sonda propia que se reencola a si misma. La primera version envolvia
   requestAnimationFrame y medía el hueco entre CALLBACKS: como effects.js
   tambien pide fotogramas, dos callbacks del mismo fotograma daban un hueco
   de 0 ms y la mediana salia 0. */
for (const [nombre, cpu] of [['iPhone 12', 4], ['iPhone 12', 6], ['Escritorio', 1]]) {
  const ctx = await navegador.newContext(APARATOS[nombre]);
  const p = await ctx.newPage();
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: cpu });
  await p.addInitScript(() => {
    window.__f = []; let prev = 0;
    (function sonda(t) { if (prev) window.__f.push(t - prev); prev = t; requestAnimationFrame(sonda); })(performance.now());
  });
  await p.goto(URL_PRUEBA);
  await p.waitForTimeout(4200);
  const f = (await p.evaluate(() => window.__f.slice(0))).filter(x => x > 0.5).sort((a, b) => a - b);
  const mediana = f[f.length >> 1];
  decir(mediana <= 34,
    `${nombre} con la CPU a 1/${cpu}: mediana ${mediana.toFixed(1)} ms (${(1000 / mediana).toFixed(0)} fps), peor ${f[f.length - 1].toFixed(0)} ms`);
  await ctx.close();
}

await navegador.close();
for (const f of [TMP, TMP_CORTA]) { try { fs.unlinkSync(f); } catch (e) {} }
console.log(fallos === 0
  ? '\nLa intro se ve, no se queda en blanco, se puede saltar, abre la tienda a tiempo y no roba fotogramas al fondo.\n'
  : `\n${fallos} comprobacion(es) en rojo.\n`);
process.exit(fallos ? 1 : 0);
