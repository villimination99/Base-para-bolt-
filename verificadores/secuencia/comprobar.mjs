/* LA SECUENCIA DE MARCA, FOTOGRAMA A FOTOGRAMA.
   ==================================================================
   Esta bateria no nacio de una idea: nacio de dos fallos que se colaron en
   la misma tarde, y cada comprobacion de aqui abajo es uno de ellos.

   1. EL ENLACE INVISIBLE QUE SE PODIA PULSAR.
      La escena del cierre lleva un enlace al catalogo. Las escenas apagadas
      estaban solo a `opacity: 0`, y un elemento transparente sigue
      recibiendo el dedo: durante el 80 % del ciclo habia un enlace invisible
      encima del centro de la seccion. Tocar ahi te sacaba de la portada sin
      haber visto ningun boton. Ninguna bateria lo veia porque nada se salia
      de su caja ni fallaba: simplemente estaba mal.

   2. LA ESCENA ENCENDIDA Y VACIA.
      La marca se compone letra a letra, y las letras heredaban un degradado
      recortado al texto. En cuanto cada letra recibio su propio transform,
      el recorte dejo de seguirlas: trece letras transparentes sobre un fondo
      que ya no estaba debajo. La escena decia `opacity: 1` y en la pantalla
      no habia NADA.

      De ahi sale la regla de esta bateria: NO SE MIDE OPACIDAD, SE MIDE
      TINTA. Se tapa el lienzo del fondo, se fotografia la capa de texto y se
      cuentan los pixeles encendidos de verdad. Un detector que se fia de lo
      que dice el estilo no habria visto ninguno de los dos.

   Y ademas se vigila lo que ya se sabia que importa:
     - que no haya un fotograma en negro entre escenas;
     - que dos escenas no se lean a la vez;
     - que el ciclo vuelva exactamente a su punto de partida;
     - que cada escena quepa en su caja en los cinco idiomas a 320 px;
     - que el motor no se quede pintando fuera de pantalla.

   Uso:  node verificadores/secuencia/comprobar.mjs                        */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const css = fs.readFileSync(path.join(T, 'assets/villumination.css'), 'utf8');
const js = fs.readFileSync(path.join(T, 'assets/secuencia.js'), 'utf8');
const SECCION = fs.readFileSync(path.join(RAIZ, 'theme/sections/secuencia.liquid'), 'utf8');

/* EL BANCO DE PRUEBAS TIENE QUE SER LA SECCION, NO UNA VERSION SUYA DE HACE
   TRES RONDAS. Aqui no hay motor de Liquid, asi que el marcado se escribe a
   mano -- y eso lo deja libre de separarse del original sin que nadie se
   entere. Debajo hay una comprobacion que exige que cada pieza que se usa
   aqui siga existiendo alli. Mientras eso este en verde, lo que se mide es
   lo que se envia. */
const PIEZAS = ['data-secuencia', 'data-sec-lienzo', 'data-sec-escena', 'data-sec-tipo',
                'data-sec-duracion', 'secuencia-marca', 'secuencia-lema-l1',
                'secuencia-lema-l2', 'secuencia-pilar', 'secuencia-cifra',
                'secuencia-cierre-tit', 'btn-neon', 'secuencia.js'];

/* Los cinco idiomas, con los textos mas largos de cada uno: es donde una caja
   se rompe. El aleman manda casi siempre. */
const IDIOMAS = {
  es: ['VILLUMINATION', 'NO TE', 'CONFÓRMATE', ['FUERZA', 'EQUIPO Y ACCESORIOS'], ['NUTRICIÓN', 'SUPLEMENTOS'], ['CONSTANCIA', 'PLANES Y CÓDICES'], 'PRODUCTOS · UNA SOLA META', 'VER CATÁLOGO'],
  en: ['VILLUMINATION', "DON'T", 'SETTLE', ['STRENGTH', 'EQUIPMENT AND ACCESSORIES'], ['NUTRITION', 'SUPPLEMENTS'], ['CONSISTENCY', 'PLANS AND CODICES'], 'PRODUCTS · ONE GOAL', 'VIEW CATALOGUE'],
  fr: ['VILLUMINATION', 'NE TE', 'CONTENTE PAS', ['FORCE', 'ÉQUIPEMENT ET ACCESSOIRES'], ['NUTRITION', 'COMPLÉMENTS'], ['CONSTANCE', 'PLANS ET CODEX'], 'PRODUITS · UN SEUL OBJECTIF', 'VOIR LE CATALOGUE'],
  de: ['VILLUMINATION', 'GIB DICH', 'NICHT ZUFRIEDEN', ['KRAFT', 'AUSRÜSTUNG UND ZUBEHÖR'], ['ERNÄHRUNG', 'NAHRUNGSERGÄNZUNG'], ['BESTÄNDIGKEIT', 'PLÄNE UND KODIZES'], 'PRODUKTE · EIN ZIEL', 'KATALOG ANSEHEN'],
  ja: ['VILLUMINATION', '妥協', 'しない', ['筋力', '器具とアクセサリー'], ['栄養', 'サプリメント'], ['継続', 'プランと書'], '商品 · ひとつの目標', 'カタログを見る'],
};

const ico = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="8"/></svg>';

function marcado(L) {
  const [marca, l1, l2, p1, p2, p3, pie, boton] = L;
  const pilar = (p, i) =>
    `<li class="secuencia-pilar" style="--i:${i}"><span class="secuencia-pilar-ico" aria-hidden="true">${ico}</span>` +
    `<span class="secuencia-pilar-txt"><strong>${p[0]}</strong><span>${p[1]}</span></span></li>`;
  return `
<div class="secuencia-escena secuencia-escena--marca" data-sec-escena data-sec-tipo="marca">
  <p class="secuencia-marca">${marca}</p></div>
<div class="secuencia-escena secuencia-escena--lema" data-sec-escena data-sec-tipo="lema">
  <p class="secuencia-lema"><span class="secuencia-lema-l1">${l1}</span><em class="secuencia-lema-l2">${l2}</em></p></div>
<div class="secuencia-escena secuencia-escena--pilares" data-sec-escena data-sec-tipo="pilares">
  <ul class="secuencia-pilares" role="list">${pilar(p1, 0)}${pilar(p2, 1)}${pilar(p3, 2)}</ul></div>
<div class="secuencia-escena secuencia-escena--cifra" data-sec-escena data-sec-tipo="cifra">
  <p class="secuencia-cifra">40</p><p class="secuencia-cifra-pie">${pie}</p></div>
<div class="secuencia-escena secuencia-escena--cierre" data-sec-escena data-sec-tipo="cierre">
  <p class="secuencia-cierre-tit">VILLUMINATIONS.COM</p>
  <a class="btn-neon secuencia-cta" href="/collections/all" data-cta><span>${boton}</span>${ico}</a></div>`;
}

function pagina(L, alto, dur) {
  return `<style>${css}
 html,body{margin:0;background:#05060a}
 .container{max-width:1180px;margin:0 auto;padding:0 20px}
 :root{--font-heading:system-ui,sans-serif;--font-body:system-ui,sans-serif;
   --neon-cyan:#00d4ff;--neon-purple:#7b2fff;--neon-pink:#ff2ecb}
 body{font-family:var(--font-body)}
</style>
<section class="secuencia-sec" style="--sec-acento:#00f0ff;--sec-fondo:#05060a;--sec-alto:${alto}px;--sec-alto-movil:${Math.round(alto * 0.78)}px;">
 <div class="container"><div class="secuencia" data-secuencia data-sec-duracion="${dur}" data-sec-fondo="#05060a">
  <canvas class="secuencia-lienzo" data-sec-lienzo aria-hidden="true"></canvas>
  <div class="secuencia-escenas">${marcado(L)}</div>
 </div></div></section>
<script>${js}<\/script>`;
}

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

/* ---- 0. El banco de pruebas sigue pegado a la seccion ---- */
for (const p of PIEZAS) {
  decir(SECCION.indexOf(p) >= 0, `la seccion sigue teniendo "${p}"`);
}

const nav = await chromium.launch({ executablePath: CHROME });

/* ==================================================================
   1. TINTA, NO OPACIDAD
   Se tapa el lienzo, se fotografia la capa de texto contra un fondo plano
   y se cuentan los pixeles que NO son ese fondo. Es la unica forma de
   saber si una escena encendida esta pintando algo de verdad.
   ================================================================== */
{
  const p = await nav.newPage({ viewport: { width: 1280, height: 900 } });
  await p.setContent(pagina(IDIOMAS.fr, 640, 12), { waitUntil: 'load' });
  await p.addStyleTag({ content: '.secuencia-lienzo{display:none!important}' +
                                 '.secuencia{background:#000!important}' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));

  const nombres = ['marca', 'lema', 'pilares', 'cifra', 'cierre'];
  for (let i = 0; i < 5; i++) {
    await p.waitForFunction((k) => {
      const e = document.querySelectorAll('[data-sec-escena]')[k];
      return e && parseFloat(e.style.opacity || 0) > 0.92 &&
             parseFloat(e.style.getPropertyValue('--p') || 0) > 0.66;
    }, i, { timeout: 40000, polling: 50 });

    const caja = await p.locator('.secuencia').boundingBox();
    const foto = await p.screenshot({ clip: caja });
    const tinta = await p.evaluate(async (b64) => {
      const img = new Image();
      await new Promise((r) => { img.onload = r; img.src = 'data:image/png;base64,' + b64; });
      const c = document.createElement('canvas');
      c.width = img.width; c.height = img.height;
      const g = c.getContext('2d');
      g.drawImage(img, 0, 0);
      const d = g.getImageData(0, 0, c.width, c.height).data;
      let n = 0;
      for (let k = 0; k < d.length; k += 4) if (d[k] + d[k + 1] + d[k + 2] > 90) n++;
      return { encendidos: n, total: d.length / 4 };
    }, foto.toString('base64'));

    const porcien = (tinta.encendidos / tinta.total) * 100;
    decir(porcien > 0.35,
      `la escena "${nombres[i]}" pinta tinta de verdad (${porcien.toFixed(2)} % del cuadro)`);
  }
  await p.close();
}

/* ==================================================================
   2. EL ENLACE DEL CIERRE NO SE PUEDE PULSAR CUANDO NO SE VE
   Se pregunta al navegador quien hay en el punto donde esta el boton,
   en muchos instantes del ciclo. Cuando la escena esta apagada, ahi no
   puede haber un enlace.
   ================================================================== */
{
  const p = await nav.newPage({ viewport: { width: 1280, height: 900 } });
  await p.setContent(pagina(IDIOMAS.fr, 640, 8), { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));

  let colados = 0, muestras = 0, vistoVivo = false;
  for (let k = 0; k < 90; k++) {
    const r = await p.evaluate(() => {
      const a = document.querySelector('[data-cta]');
      const esc = a.closest('[data-sec-escena]');
      const o = parseFloat(esc.style.opacity || 0);
      const c = a.getBoundingClientRect();
      const quien = document.elementFromPoint(c.left + c.width / 2, c.top + c.height / 2);
      return { o: o, alcanzable: !!(quien && quien.closest('[data-cta]')) };
    });
    muestras++;
    if (r.o < 0.25 && r.alcanzable) colados++;
    if (r.o > 0.9 && r.alcanzable) vistoVivo = true;
    await p.waitForTimeout(90);
  }
  decir(colados === 0,
    `el boton del cierre NO se puede pulsar mientras esta invisible (${colados} de ${muestras} muestras)`);
  decir(vistoVivo, 'y SI se puede pulsar cuando esta a la vista');
  await p.close();
}

/* ==================================================================
   3. NI UN FOTOGRAMA EN NEGRO, NI DOS ESCENAS LEYENDOSE A LA VEZ
   ================================================================== */
{
  const p = await nav.newPage({ viewport: { width: 1280, height: 900 } });
  await p.setContent(pagina(IDIOMAS.fr, 640, 8), { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));

  const muestras = await p.evaluate(() => new Promise((res) => {
    const out = [];
    const t = setInterval(() => {
      const o = [].map.call(document.querySelectorAll('[data-sec-escena]'),
        (e) => parseFloat(e.style.opacity || 0));
      out.push(o);
      if (out.length >= 170) { clearInterval(t); res(out); }
    }, 55);
  }));

  let vacios = 0, dobles = 0;
  for (const o of muestras) {
    if (Math.max.apply(null, o) < 0.30) vacios++;
    if (o.filter((x) => x > 0.62).length > 1) dobles++;
  }
  decir(vacios === 0, `nunca hay un fotograma sin escena (${vacios} de ${muestras.length})`);
  decir(dobles === 0, `nunca se leen dos escenas a la vez (${dobles} de ${muestras.length})`);
  await p.close();
}

/* ==================================================================
   4. CADA ESCENA CABE EN SU CAJA, EN LOS CINCO IDIOMAS, A 320 px
   320 es el ancho del movil mas estrecho que sigue vivo. Si algo se sale
   aqui, se sale en la tienda.
   ================================================================== */
for (const [lang, L] of Object.entries(IDIOMAS)) {
  const p = await nav.newPage({ viewport: { width: 320, height: 720 } });
  await p.setContent(pagina(L, 420, 60), { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));
  await p.waitForTimeout(120);

  const salidos = await p.evaluate(() => {
    const caja = document.querySelector('.secuencia').getBoundingClientRect();
    const malos = [];
    document.querySelectorAll('[data-sec-escena]').forEach((e) => {
      const tipo = e.getAttribute('data-sec-tipo');
      /* Se mide con la escena FORZADA a visible y sin transform: lo que se
         comprueba es si el TEXTO cabe, no donde esta a mitad de su gesto. */
      const antes = e.style.cssText;
      e.style.opacity = '1';
      e.style.setProperty('--p', '1');
      const r = e.getBoundingClientRect();
      /* CON EL NUMERO. Un detector que solo dice "se sale" obliga a quien lo
         lea a reconstruir el fallo a mano; con los pixeles encima, la causa
         suele verse sin abrir el navegador. */
      if (r.width > caja.width + 1)
        malos.push(tipo + ': ' + Math.round(r.width) + ' px de ancho en una caja de ' + Math.round(caja.width));
      if (r.height > caja.height + 1)
        malos.push(tipo + ': ' + Math.round(r.height) + ' px de alto en una caja de ' + Math.round(caja.height));
      e.querySelectorAll('*').forEach((h) => {
        const q = h.getBoundingClientRect();
        if (q.width === 0 && q.height === 0) return;
        const fuera = Math.max(caja.left - q.left, q.right - caja.right);
        if (fuera > 1)
          malos.push(tipo + ': "' + (h.textContent || '').trim().slice(0, 14) + '" se sale ' +
                     Math.round(fuera) + ' px (' + (h.className || h.tagName) + ')');
      });
      e.style.cssText = antes;
    });
    return malos;
  });
  decir(salidos.length === 0,
    `${lang}: todo cabe en la caja a 320 px${salidos.length ? ' -> ' + salidos.slice(0, 3).join(' | ') : ''}`);
  await p.close();
}

/* ==================================================================
   5. EL CICLO VUELVE A SU PUNTO DE PARTIDA
   Un bucle que no cierra se nota: al dar la vuelta hay un salto. Se
   comparan las opacidades en t y en t + DUR.
   ================================================================== */
{
  const DUR = 6;
  const p = await nav.newPage({ viewport: { width: 1280, height: 900 } });
  await p.setContent(pagina(IDIOMAS.fr, 640, DUR), { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));
  const leer = () => p.evaluate(() => [].map.call(
    document.querySelectorAll('[data-sec-escena]'), (e) => parseFloat(e.style.opacity || 0)));
  await p.waitForTimeout(1500);
  const a = await leer();
  await p.waitForTimeout(DUR * 1000);
  const b = await leer();
  let peor = 0;
  for (let i = 0; i < a.length; i++) peor = Math.max(peor, Math.abs(a[i] - b[i]));
  decir(peor < 0.12, `el ciclo cierra donde empezo (mayor diferencia ${peor.toFixed(3)})`);
  await p.close();
}

/* ==================================================================
   6. FUERA DE PANTALLA SE PARA
   Si sigue pintando debajo del pliegue, se lleva fotogramas de todo lo
   demas justo cuando el visitante esta comprando.
   ================================================================== */
{
  const p = await nav.newPage({ viewport: { width: 1280, height: 700 } });
  await p.setContent(pagina(IDIOMAS.fr, 640, 12) + '<div style="height:4000px"></div>',
    { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));
  await p.waitForTimeout(400);
  await p.evaluate(() => window.scrollTo(0, 3000));
  await p.waitForTimeout(700);
  const a = await p.evaluate(() => {
    const e = document.querySelectorAll('[data-sec-escena]')[0];
    return e.style.getPropertyValue('--p');
  });
  await p.waitForTimeout(900);
  const b = await p.evaluate(() => {
    const e = document.querySelectorAll('[data-sec-escena]')[0];
    return e.style.getPropertyValue('--p');
  });
  decir(a === b, `fuera de pantalla el motor se para (${a} -> ${b})`);
  await p.close();
}

/* ==================================================================
   7. SIN MOVIMIENTO SE VE EL BOTON
   Quien pide menos movimiento tambien tiene derecho a comprar.
   ================================================================== */
{
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: 'reduce' });
  const p = await ctx.newPage();
  await p.setContent(pagina(IDIOMAS.fr, 640, 12), { waitUntil: 'load' });
  await p.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));
  await p.waitForTimeout(350);
  const r = await p.evaluate(() => {
    const a = document.querySelector('[data-cta]');
    const esc = a.closest('[data-sec-escena]');
    const c = a.getBoundingClientRect();
    const quien = document.elementFromPoint(c.left + c.width / 2, c.top + c.height / 2);
    return {
      o: parseFloat(esc.style.opacity || 0),
      alcanzable: !!(quien && quien.closest('[data-cta]')),
      ancho: Math.round(c.width),
    };
  });
  decir(r.o > 0.9 && r.alcanzable && r.ancho > 80,
    `sin movimiento se ve el boton y se puede pulsar (opacidad ${r.o}, ${r.ancho} px)`);

  /* Y QUE LA LUZ ESTE PINTADA, no solo el texto.
     -------------------------------------------------------------------
     Lo de arriba comprueba el boton. Pero con movimiento reducido el motor
     no anima: pinta UN fotograma y se para. Si esa unica llamada se
     rompiera, el boton seguiria visible y esta prueba seguiria en verde
     mientras el visitante ve el texto flotando sobre un vacio negro.

     Asi que se tapa la capa de texto y se mide la tinta DEL LIENZO. Es la
     misma leccion que la bateria numero 1: se mide lo que se pinta, no lo
     que el codigo dice que pinta. */
  const p2 = await ctx.newPage();
  await p2.setContent(pagina(IDIOMAS.fr, 640, 12), { waitUntil: 'load' });
  await p2.addStyleTag({ content: '.secuencia-escenas{display:none!important}' +
                                  '.secuencia::before,.secuencia::after{display:none!important}' +
                                  '.secuencia{background:#000!important}' });
  await p2.waitForFunction(() => !!document.querySelector('[data-secuencia][data-sec-listo]'));
  await p2.waitForTimeout(350);
  const caja2 = await p2.locator('.secuencia').boundingBox();
  const foto2 = await p2.screenshot({ clip: caja2 });
  const luz = await p2.evaluate(async (b64) => {
    const img = new Image();
    await new Promise((r) => { img.onload = r; img.src = 'data:image/png;base64,' + b64; });
    const c = document.createElement('canvas');
    c.width = img.width; c.height = img.height;
    const g = c.getContext('2d');
    g.drawImage(img, 0, 0);
    const d = g.getImageData(0, 0, c.width, c.height).data;
    let n = 0;
    for (let k = 0; k < d.length; k += 4) if (d[k] + d[k + 1] + d[k + 2] > 90) n++;
    return { encendidos: n, total: d.length / 4 };
  }, foto2.toString('base64'));
  const pc = (luz.encendidos / luz.total) * 100;
  decir(pc > 1, `sin movimiento el lienzo tambien pinta su fotograma (${pc.toFixed(2)} % del cuadro)`);
  await p2.close();
  await ctx.close();
}

await nav.close();

console.log('');
if (fallos) {
  console.error(`  ${fallos} comprobacion${fallos > 1 ? 'es' : ''} en rojo en la secuencia.`);
  process.exit(1);
}
console.log('  La secuencia pinta lo que dice que pinta, no deja enlaces sueltos y cierra el ciclo.');
