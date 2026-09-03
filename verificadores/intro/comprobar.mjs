/* Comprueba la intro "Pulso" en un navegador real.
   ------------------------------------------------------------------
   Nacio de tres fallos que leer el codigo no habria encontrado nunca:

   1. El emblema pasa toda la secuencia congelado en el primer fotograma de
      logoAppear, que es scale(0.5). getBoundingClientRect devolvia por tanto
      LA MITAD del radio real, asi que las particulas formaban un anillo del
      tamano equivocado y la amplitud del latido se quedaba en un munon. Solo
      se ve midiendo geometria de verdad.
   2. Habia un hueco de casi medio segundo, entre que el trazo se apagaba y el
      emblema entraba, con la pantalla practicamente vacia. Solo se ve
      contando pixeles encendidos fotograma a fotograma.
   3. Los lienzos decorativos del fondo seguian corriendo DETRAS de la intro,
      que los tapa por completo: la pagina iba a 30 fps en vez de 60 justo en
      los dos segundos de los que depende la primera impresion. Solo se ve
      midiendo con el navegador estrangulado.

   Uso:  node verificadores/intro/comprobar.mjs                             */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

/* El marcado es el del snippet real, con las clases que el CSS del tema
   espera. Si el snippet cambia de estructura, esta prueba deja de reflejarlo,
   asi que se comprueba aparte que las piezas que se usan aqui siguen ahi. */
const SNIPPET = fs.readFileSync(path.join(RAIZ, 'theme/snippets/splash-intro.liquid'), 'utf8');
const PIEZAS = ['splash-canvas', 'splash-emblem', 'splash-enter-btn', 'data-splash-skip', 'intro.js'];

const PAGINA = `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="file://${ASSETS}/villumination.css">
<style>:root{--neon-cyan:#00d4ff;--neon-pink:#ff2ecb;--neon-green:#00e87b;--neon-purple:#7b2fff;
--color-bg:#000;--font-heading:system-ui;--font-body:system-ui}
body{margin:0;background:#000;color:#fff;font-family:system-ui}</style></head><body>
<div id="splash-intro" class="splash-intro" data-splash data-splash-3d role="dialog" aria-label="Villumination">
  <div class="splash-bg"></div>
  <canvas id="splash-canvas" class="splash-canvas" aria-hidden="true"></canvas>
  <button class="splash-skip" type="button" data-splash-skip>SALTAR</button>
  <div class="splash-content">
    <div class="splash-emblem">
      <span class="splash-halo splash-halo-1"></span><span class="splash-halo splash-halo-2"></span>
      <span class="splash-pulse"></span><span class="splash-pulse splash-pulse--2"></span>
      <span class="splash-ring"></span>
      <span class="splash-core"><span class="splash-mono">VI</span></span>
    </div>
    <h1 class="splash-title">VILLUMINATION</h1>
    <p class="splash-tagline">TRANSFORMA TU CUERPO.</p>
    <div class="splash-loader"><div class="splash-loader-bar"></div></div>
    <button id="splash-enter" class="splash-enter-btn" type="button"><span>ENTRAR</span></button>
  </div>
</div>
<script>window.theme={routes:{},settings:{splashOnce:false,splash3d:true},strings:{}};
window.__t0=performance.now();</script>
<script src="file://${ASSETS}/intro.js"></script>
<script src="file://${ASSETS}/base.js"></script>
<script src="file://${ASSETS}/effects.js"></script>
</body></html>`;

const TMP = path.join(AQUI, '.pagina-de-prueba.html');
fs.writeFileSync(TMP, PAGINA);
const URL_PRUEBA = 'file://' + TMP;

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
   segundo tarde, que en una secuencia de dos segundos es otra escena. */
const enElInstante = (p, ms) => p.evaluate(m => new Promise(r => {
  (function esperar() {
    if (performance.now() - window.__t0 >= m) r();
    else requestAnimationFrame(esperar);
  })();
}), ms);

async function abrir(nombre, extra) {
  const ctx = await navegador.newContext(Object.assign({}, APARATOS[nombre], extra || {}));
  const p = await ctx.newPage();
  const errores = [];
  p.on('pageerror', e => errores.push(e.message));
  await p.goto(URL_PRUEBA);
  return { ctx, p, errores };
}

console.log('\n--- El snippet sigue teniendo las piezas que esta prueba usa ---');
for (const pieza of PIEZAS) decir(SNIPPET.includes(pieza), `el snippet declara "${pieza}"`);

console.log('\n--- Composicion: el pico del latido cae bajo el anillo del emblema ---');
/* La punta del complejo QRS tiene que quedar justo DEBAJO del anillo, no
   atravesandolo por el medio: el estallido ocurre en la puerta del emblema y
   por eso las particulas casi no tienen que viajar para formarlo. */
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
  // Mismo calculo que intro.js, en px CSS
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

console.log('\n--- La secuencia nunca se queda en blanco ---');
/* El fallo que esto vigila: entre el trazo que se apagaba y el emblema que
   entraba habia casi medio segundo con el CENTRO de la pantalla vacio.

   SE MIDE LA ZONA DEL EMBLEMA, no la pantalla entera. Medir la pantalla
   entera parecia lo obvio y no servia: el fondo, la rejilla y el boton de
   saltar aportan luz constante, el estallido reparte particulas por todas
   partes y el resultado tapaba justo el agujero que se buscaba. Con la
   pantalla entera, la version ROTA daba 1,45 %, 1,56 % y 2,19 % en tres
   pasadas contra un umbral de 1,7 %: habria dado verde a un fallo real una de
   cada tres veces.

   CALIBRADO CONTRA LA VERSION ROTA Y SOBRE ESTA MISMA PAGINA. Las dos cosas
   importan: la primera calibracion se hizo con otro marcado de prueba y sus
   numeros no valian aqui, asi que el umbral quedo en el sitio equivocado y el
   sabotaje pasaba. Se mide un cuadro de 3,2 radios centrado en el emblema,
   remuestreado a 120x120, contando los pixeles cuya suma RGB pasa de 90. Dos
   pasadas de cada version en un iPhone 12:

       instante   rota          arreglada
         900 ms   3,2 / 2,8     11,5 / 11,0
        1000 ms   3,4 / 3,3     21,3 / 21,8
        1100 ms   8,0 / 7,3     23,0 / 23,2

   Y el peor valor de la ventana, tres pasadas seguidas de cada version, que
   es lo que decide de verdad:

       rota:       2,5 %   3,3 %   2,6 %      -> las tres en rojo
       arreglada:  9,6 %   9,4 %   9,3 %      -> las tres en verde

   Ahi esta el agujero: el nucleo que se carga en el lienzo entra a los 880 ms
   y el emblema a 1,05 s, asi que en la version buena el centro ya tiene luz;
   en la rota no llega nada hasta que aterrizan las particulas, pasados 1,2 s.
   El umbral va en el 6 %: por encima queda el peor caso medido de la buena
   (9,3 %) y por debajo el mejor de la rota (3,3 %), con margen de mas del
   50 % por los dos lados y sin solaparse en ninguna pasada.

   Fuera de esta ventana NO se exige nada, por razones medidas: a 700 ms las
   dos versiones dan lo mismo (13-15 %) porque manda el estallido, y a partir
   de 1200 ms tambien (16-24 %) porque las particulas ya han llegado y tapan
   el agujero. Solo entre 900 y 1100 ms la diferencia es de verdad. */
{
  const { ctx, p, errores } = await abrir('iPhone 12');
  const INSTANTES = [700, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2400];
  const VENTANA = [900, 1100];
  const MINIMO = 0.06;
  const medidas = [];
  for (const ms of INSTANTES) {
    const g = await p.evaluate(() => {
      const c = document.querySelector('[data-splash]');
      const e = c.querySelector('.splash-emblem');
      const r = e.getBoundingClientRect(), rc = c.getBoundingClientRect();
      return { cx: r.left - rc.left + r.width / 2, cy: r.top - rc.top + r.height / 2,
               R: (e.offsetWidth || r.width) / 2 };
    });
    await enElInstante(p, ms);
    const foto = await p.screenshot();
    // Se leen los pixeles de verdad con el propio navegador: el tamano del PNG
    // no dice nada sobre si hay algo en pantalla.
    const v = await p.evaluate(async ([b64, g]) => {
      const img = new Image();
      img.src = 'data:image/png;base64,' + b64;
      await img.decode();
      const esc = img.width / document.documentElement.clientWidth; // px de foto por px CSS
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
    medidas.push([ms, v]);
  }
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

console.log('\n--- La puerta de la tienda siempre aparece ---');
for (const [nombre, extra, espera] of [
  ['iPhone 12', {}, 3200],
  ['iPhone 12', { reducedMotion: 'reduce' }, 600],
  ['Escritorio', {}, 3200],
]) {
  const { ctx, p, errores } = await abrir(nombre, extra);
  await p.waitForTimeout(espera);
  const r = await p.evaluate(() => {
    const c = document.querySelector('[data-splash]');
    const e = document.querySelector('.splash-enter-btn');
    const s = document.querySelector('.splash-skip');
    return { listo: c.classList.contains('intro-lista'),
             op: +getComputedStyle(e).opacity,
             alto: Math.round(s.getBoundingClientRect().height),
             sop: +getComputedStyle(s).opacity };
  });
  const etiqueta = extra.reducedMotion ? `${nombre} (movimiento reducido)` : nombre;
  decir(r.listo && r.op > 0.9, `${etiqueta.padEnd(28)} el boton de entrar esta visible (opacidad ${r.op.toFixed(2)})`);
  decir(r.sop > 0.9 && r.alto >= 44, `${etiqueta.padEnd(28)} saltar es visible y tiene ${r.alto} px de area tactil`);
  decir(errores.length === 0, `${etiqueta.padEnd(28)} sin errores de JavaScript`);
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
  await p.waitForTimeout(3000);
  const f = (await p.evaluate(() => window.__f.slice(0))).filter(x => x > 0.5).sort((a, b) => a - b);
  const mediana = f[f.length >> 1];
  decir(mediana <= 34,
    `${nombre} con la CPU a 1/${cpu}: mediana ${mediana.toFixed(1)} ms (${(1000 / mediana).toFixed(0)} fps), peor ${f[f.length - 1].toFixed(0)} ms`);
  await ctx.close();
}

await navegador.close();
try { fs.unlinkSync(TMP); } catch (e) {}
console.log(fallos === 0
  ? '\nLa intro se ve, no se queda en blanco, se puede saltar y no roba fotogramas al fondo.\n'
  : `\n${fallos} comprobacion(es) en rojo.\n`);
process.exit(fallos ? 1 : 0);
