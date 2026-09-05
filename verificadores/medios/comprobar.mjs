/* Comprueba que ninguna tarjeta de video se queda en NEGRO cuando su miniatura
   no carga.
   ------------------------------------------------------------------
   Nacio de un fallo reportado desde la tienda: tarjetas y videos que se veian
   en negro. La causa no era el tema en si, sino de donde vienen las
   miniaturas: i.ytimg.com NO es el CDN de Shopify, y falla mucho mas de lo que
   parece. Lo bloquean casi todos los bloqueadores de anuncios, y algun video
   no tiene el tamano de miniatura que se le pide. Cuando eso pasaba, la
   tarjeta se quedaba en negro puro (.video-card lleva fondo #0a0a1a y
   .video-card-thumb #000) con el icono de imagen rota asomando por detras del
   boton de reproducir.

   COMO SE MIDE, Y POR QUE ASI. La pagina de prueba lleva dentro una tarjeta
   ROTA A PROPOSITO -- el marcado tal y como estaba antes del arreglo -- junto a
   la buena. La prueba no compara contra un numero escrito a mano, compara la
   buena CONTRA la rota, en la misma pasada y el mismo navegador. Asi lleva su
   linea de base pegada: si alguien quitara el respaldo, la tarjeta buena caeria
   hasta el valor de la rota y esto se pondria rojo solo, sin recalibrar nada.
   En esta sesion ya se perdio una ronda por calibrar con umbrales escritos a
   mano que resultaron no distinguir nada.

   El bloqueo del dominio se hace de verdad, con enrutado del navegador: es
   exactamente lo que hace un bloqueador de anuncios en el movil del cliente.

   Uso:  node verificadores/medios/comprobar.mjs                            */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const PAGINA = 'file://' + path.join(AQUI, 'tarjetas.html');

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

/* La pagina de prueba copia el marcado de la seccion. Si la seccion cambiara de
   estructura, esta prueba se quedaria describiendo un tema que ya no existe, asi
   que se comprueba que las piezas siguen ahi. */
const SECCION = fs.readFileSync(path.join(RAIZ, 'theme/sections/video-grid.liquid'), 'utf8');
const BASE = fs.readFileSync(path.join(RAIZ, 'theme/assets/base.js'), 'utf8');

console.log('\n--- La seccion sigue teniendo el respaldo que esta prueba mide ---');
for (const pieza of ['video-card-fondo', 'data-v-thumb', 'data-alt1', 'video-card-fondo--aviso', 'fallback_image'])
  decir(SECCION.includes(pieza), `video-grid.liquid declara "${pieza}"`);
decir(BASE.includes("$all('[data-v-thumb]')"), 'base.js encadena los respaldos de la miniatura');
decir(!/onerror\s*=/.test(SECCION),
  'el respaldo NO va en un atributo onerror (la politica de seguridad de contenido de algunas tiendas lo bloquea)');

const navegador = await chromium.launch({ executablePath: CHROME });

/* Cuanta luz tiene de verdad una caja. Un rectangulo negro da casi cero; una
   tarjeta con degradado de marca, icono y titulo da bastante mas. */
async function medir(p, sel) {
  // Se captura el ELEMENTO, no un recorte de la pantalla: con tres tarjetas en
  // fila y un viewport de movil, la segunda y la tercera caen fuera de la
  // pantalla y un recorte por coordenadas fallaba. La captura de elemento lo
  // desplaza hasta verlo, que ademas es lo que hace el visitante al deslizar.
  const el = await p.$(sel);
  if (!el) throw new Error('no existe ' + sel);
  const foto = await el.screenshot();
  return p.evaluate(async b64 => {
    const img = new Image();
    img.src = 'data:image/png;base64,' + b64;
    await img.decode();
    const L = 100;
    const c = document.createElement('canvas');
    c.width = c.height = L;
    const x = c.getContext('2d');
    x.drawImage(img, 0, 0, L, L);
    const d = x.getImageData(0, 0, L, L).data;
    let vivos = 0, min = 999, max = -1, suma = 0, croma = 0, n = 0;
    for (let i = 0; i < d.length; i += 4) {
      const r = d[i], g = d[i + 1], b = d[i + 2];
      const l = 0.2126 * r + 0.7152 * g + 0.0722 * b;
      if (l > 46) vivos++;
      if (l < min) min = l;
      if (l > max) max = l;
      suma += l;
      croma += Math.max(r, g, b) - Math.min(r, g, b);
      n++;
    }
    return { luz: vivos / (L * L), rango: max - min, media: suma / n, croma: croma / n };
  }, foto.toString('base64'));
}

for (const [nombre, ancho, alto] of [['movil', 390, 800], ['escritorio', 1280, 800]]) {
  console.log(`\n--- ${nombre}: con el dominio de las miniaturas BLOQUEADO ---`);
  const ctx = await navegador.newContext({ viewport: { width: ancho, height: alto }, deviceScaleFactor: 2 });
  // Esto es literalmente lo que hace un bloqueador de anuncios.
  await ctx.route('**i.ytimg.com/**', r => r.abort());
  const p = await ctx.newPage();
  const errores = [];
  p.on('pageerror', e => errores.push(e.message));
  await p.goto(PAGINA);
  await p.waitForTimeout(900);

  const roto = await medir(p, '[data-control-roto] .video-card');
  const real = await medir(p, '[data-tarjeta-real] .video-card');
  const vacia = await medir(p, '[data-tarjeta-vacia] .video-card');
  const f = (m) => `media ${m.media.toFixed(1)}  croma ${m.croma.toFixed(1)}`;
  console.log(`        control roto : ${f(roto)}`);
  console.log(`        real         : ${f(real)}`);
  console.log(`        sin video    : ${f(vacia)}`);

  /* LO PRINCIPAL ES ESTRUCTURAL, no estadistico. Lo que se prometio es que
     debajo de la miniatura hay SIEMPRE una capa de marca que cubre la tarjeta.
     Eso se puede comprobar exacto, y no depende de si un degradado oscuro sube
     o baja la media de brillo unas decimas. */
  const capa = await p.evaluate(() => {
    const salida = {};
    for (const [clave, sel] of [['real', '[data-tarjeta-real]'], ['vacia', '[data-tarjeta-vacia]'], ['roto', '[data-control-roto]']]) {
      const card = document.querySelector(sel + ' .video-card');
      const fondo = card.querySelector('.video-card-fondo');
      if (!fondo) { salida[clave] = { hay: false }; continue; }
      const rc = card.getBoundingClientRect(), rf = fondo.getBoundingClientRect();
      const cs = getComputedStyle(fondo);
      salida[clave] = {
        hay: true,
        cobertura: (rf.width * rf.height) / Math.max(rc.width * rc.height, 1),
        pintado: cs.backgroundImage !== 'none' || cs.backgroundColor !== 'rgba(0, 0, 0, 0)',
        visible: cs.display !== 'none' && +cs.opacity > 0.5,
      };
    }
    return salida;
  });

  decir(!capa.roto.hay,
    'el control roto NO tiene capa de respaldo: es el marcado de antes del arreglo, y por eso sirve de linea de base');
  for (const [clave, etiqueta] of [['real', 'la tarjeta con video'], ['vacia', 'la tarjeta sin video']]) {
    const c = capa[clave];
    decir(c.hay && c.visible, `${etiqueta} tiene capa de respaldo visible`);
    decir(c.hay && c.cobertura > 0.9,
      `${etiqueta} tiene el respaldo cubriendo la tarjeta entera (${(c.cobertura * 100).toFixed(0)} %)`);
    decir(c.hay && c.pintado, `${etiqueta} tiene el respaldo REALMENTE pintado, no transparente`);
  }

  /* Y un refuerzo en pixeles, con el umbral sacado de medir, no inventado.
     Se usa el CROMA (cuanto color hay) y no el brillo: medido en las dos
     pantallas, la rota da 15,3-16,3 y las buenas 21,9-22,2. El brillo no
     valia -- salia MAS ALTO en la rota, porque el circulo blanco de reproducir
     es lo unico luminoso que le queda -- y el rango de luminancia tampoco,
     porque ese mismo circulo lo satura a 250 en las dos. */
  decir(real.croma > 19 && vacia.croma > 19,
    `las tarjetas buenas tienen color de marca (croma ${real.croma.toFixed(1)} y ${vacia.croma.toFixed(1)}; la rota se queda en ${roto.croma.toFixed(1)})`);
  decir(roto.croma < 19,
    'el control roto sigue por debajo del umbral: la medida distingue de verdad');

  // El icono de imagen rota no puede quedarse asomando por detras del boton.
  const oculta = await p.$eval('[data-tarjeta-real] [data-v-thumb]',
    el => el.classList.contains('esta-rota') || getComputedStyle(el).display === 'none');
  decir(oculta, 'la miniatura fallida se retira, asi que no queda el icono de imagen rota');

  decir(errores.length === 0, `sin errores de JavaScript (${errores.length})`);
  await ctx.close();
}

console.log('\n--- Sin bloqueo, la miniatura manda ---');
{
  const ctx = await navegador.newContext({ viewport: { width: 390, height: 800 }, deviceScaleFactor: 2 });
  // Se responde con una imagen real para comprobar que, cuando la miniatura SI
  // carga, se pinta encima del respaldo y no se queda escondida detras.
  const png = Buffer.from(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==',
    'base64');
  await ctx.route('**i.ytimg.com/**', r => r.fulfill({ status: 200, contentType: 'image/png', body: png }));
  const p = await ctx.newPage();
  await p.goto(PAGINA);
  await p.waitForTimeout(700);
  const r = await p.$eval('[data-tarjeta-real] [data-v-thumb]', el => ({
    rota: el.classList.contains('esta-rota'),
    z: +getComputedStyle(el).zIndex || 0,
    ancho: el.getBoundingClientRect().width,
  }));
  decir(!r.rota, 'una miniatura que carga bien NO se marca como rota');
  decir(r.z >= 1, `la miniatura se pinta por encima del respaldo (z-index ${r.z})`);
  decir(r.ancho > 0, 'la miniatura ocupa la tarjeta');
  await ctx.close();
}

await navegador.close();
console.log(fallos === 0
  ? '\nNinguna tarjeta de video se queda en negro, ni con el dominio de las miniaturas bloqueado.\n'
  : `\n${fallos} comprobacion(es) en rojo.\n`);
process.exit(fallos ? 1 : 0);
