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
    let vivos = 0, min = 999, max = -1, suma = 0, croma = 0, n = 0, cromaAlto = 0, nAlto = 0;
    for (let i = 0; i < d.length; i += 4) {
      const px = (i / 4) % L, py = Math.floor((i / 4) / L);
      const r = d[i], g = d[i + 1], b = d[i + 2];
      const l = 0.2126 * r + 0.7152 * g + 0.0722 * b;
      const c = Math.max(r, g, b) - Math.min(r, g, b);
      if (l > 46) vivos++;
      if (l < min) min = l;
      if (l > max) max = l;
      suma += l;
      croma += c;
      n++;
      // La mitad SUPERIOR, que es donde vive el degradado de marca sin que la
      // cortina inferior lo oscurezca.
      if (py < L * 0.5) { cromaAlto += c; nAlto++; }
    }
    return { luz: vivos / (L * L), rango: max - min, media: suma / n,
             croma: croma / n, cromaAlto: cromaAlto / Math.max(nAlto, 1) };
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
  const f = (m) => `media ${m.media.toFixed(1)}  croma ${m.croma.toFixed(1)}  croma arriba ${m.cromaAlto.toFixed(1)}`;
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
     Tres medidas descartadas antes de dar con la buena, y quedan escritas para
     que nadie repita el camino:
       - El BRILLO no vale: salia MAS ALTO en la rota, porque el circulo blanco
         de reproducir es lo unico luminoso que le queda.
       - El RANGO de luminancia tampoco: ese mismo circulo lo satura a 250 en
         las dos.
       - El CROMA DE TODA LA TARJETA valia hasta que se anadio la cortina
         inferior que tapa las marcas de agua: al oscurecer la parte baja, las
         buenas cayeron de 22,2 a 17,3 y la rota se quedaba en 16,3. Un 6 % de
         separacion no es un control, es un adorno.
     La que si vale es el croma de la MITAD SUPERIOR, donde vive el degradado
     de marca y la cortina no llega. Medido en las dos pantallas: la rota da
     15,3-16,4 y las buenas 21,5-21,9. El umbral va en 19, en medio. */
  decir(real.cromaAlto > 19 && vacia.cromaAlto > 19,
    `las tarjetas buenas tienen color de marca arriba (${real.cromaAlto.toFixed(1)} y ${vacia.cromaAlto.toFixed(1)}; la rota se queda en ${roto.cromaAlto.toFixed(1)})`);
  decir(roto.cromaAlto < 19,
    'el control roto sigue por debajo del umbral: la medida distingue de verdad');

  // El icono de imagen rota no puede quedarse asomando por detras del boton.
  const oculta = await p.$eval('[data-tarjeta-real] [data-v-thumb]',
    el => el.classList.contains('esta-rota') || getComputedStyle(el).display === 'none');
  decir(oculta, 'la miniatura fallida se retira, asi que no queda el icono de imagen rota');

  decir(errores.length === 0, `sin errores de JavaScript (${errores.length})`);
  await ctx.close();
}

console.log('\n--- La marca de agua de la imagen de respaldo queda tapada ---');
/* Los bancos de imagenes y los generadores estampan su marca en la esquina
   inferior derecha. El comerciante puede poner cualquier imagen de respaldo,
   asi que la tarjeta lleva una cortina OPACA en el 12 % inferior: tapa la
   esquina y de paso hace legible el titulo, que se apoya justo ahi.

   Se comprueba por DIFERENCIA, que es la unica forma honesta de medirlo: la
   misma tarjeta con una imagen que lleva un bloque blanco puro en esa esquina
   y con la misma imagen sin el. Si la cortina hace su trabajo, las dos zonas
   tienen que dar practicamente el mismo valor. Medir solo la version con marca
   no valia: en esa franja tambien cae el titulo de la tarjeta, que es claro a
   proposito, y contaminaba la medida.

   Las imagenes se generan aqui como SVG en una URL de datos, para no meter
   binarios en el repositorio. */
{
  const lienzo = (conMarca) =>
    'data:image/svg+xml,' + encodeURIComponent(
      "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 240 427'>" +
      "<rect width='240' height='427' fill='#5a5f6e'/>" +
      (conMarca ? "<rect x='130' y='396' width='110' height='31' fill='#ffffff'/>" : '') +
      '</svg>');

  const medida = {};
  for (const [nombre, conMarca] of [['con marca', true], ['sin marca', false]]) {
    const ctx = await navegador.newContext({ viewport: { width: 300, height: 480 }, deviceScaleFactor: 3 });
    await ctx.route('**i.ytimg.com/**', r => r.abort());
    const p = await ctx.newPage();
    await p.goto(PAGINA);
    // Se le mete la imagen de respaldo a la tarjeta real
    await p.evaluate(src => {
      const fondo = document.querySelector('[data-tarjeta-real] .video-card-fondo');
      const img = document.createElement('img');
      img.className = 'video-card-fondo-img';
      img.alt = '';
      img.src = src;
      fondo.insertBefore(img, fondo.firstChild);
    }, lienzo(conMarca));
    await p.waitForTimeout(500);
    const el = await p.$('[data-tarjeta-real] .video-card');
    const foto = (await el.screenshot()).toString('base64');
    medida[nombre] = await p.evaluate(async b64 => {
      const img = new Image();
      img.src = 'data:image/png;base64,' + b64;
      await img.decode();
      const c = document.createElement('canvas');
      c.width = img.width; c.height = img.height;
      const x = c.getContext('2d');
      x.drawImage(img, 0, 0);
      const y0 = Math.floor(img.height * 0.935), x0 = Math.floor(img.width * 0.58);
      const d = x.getImageData(x0, y0, img.width - x0, img.height - y0).data;
      let suma = 0, n = 0;
      for (let i = 0; i < d.length; i += 4) {
        suma += 0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2];
        n++;
      }
      return suma / n;
    }, foto);
    await ctx.close();
  }
  const dif = Math.abs(medida['con marca'] - medida['sin marca']);
  decir(dif < 1.5,
    `un bloque blanco puro en la esquina cambia el brillo en ${dif.toFixed(2)} sobre 255: la cortina lo tapa`);
  console.log(`        con marca ${medida['con marca'].toFixed(1)}  |  sin marca ${medida['sin marca'].toFixed(1)}`);
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
