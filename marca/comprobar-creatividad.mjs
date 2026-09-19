/* Una creatividad de anuncio, contra los tres recortes de Meta.
   ------------------------------------------------------------------
   POR QUE EXISTE. Meta sirve el MISMO archivo en sitios que lo recortan
   distinto: 1:1 en el feed cuadrado, 4:5 en el feed vertical -- que es el que
   mas pantalla ocupa y el que mas rinde -- y 9:16 en Stories y Reels. Si se
   sube una sola pieza, tiene que sobrevivir a las tres.

   Y no hay atajo por el lado de la generacion: de los 38 modelos del catalogo
   de open-higgsfield, 34 hacen 1:1, 9:16 y 16:9, y NINGUNO hace 4:5. Asi que
   4:5 sale por recorte, si o si.

   ESTA ES LA LECCION QUE YA COSTO CARA. Las portadas del Diario se rindieron
   una vez con la marca al 7 % del borde, dentro de la zona que la tarjeta
   recorta, y en un movil se leia "ILLUMINATION" y el titulo sin su primera
   letra. Lo vio el cliente en una captura, no ningun detector. Despues paso
   lo mismo con las portadas de coleccion: el generador media UN recorte de
   los DOS que sufren, asi que las seis pasaban por estar centradas, no por
   estar comprobadas.

   Asi que aqui la caja segura no se estima: es la INTERSECCION de los tres
   recortes centrados, calculada, y se mide la tinta de verdad pixel a pixel.
   Sobre un lienzo 9:16 de 1080x1920 sale y 420..1500 -- el 56 % central. El
   recorte cuadrado es el que manda, porque es el mas alto de los tres.

   SE RECORTA POR DONDE SOBRA, NO SIEMPRE POR ARRIBA. La primera version de
   este mismo guion solo modelaba el recorte vertical, y con una pieza
   apaisada daba 100 % en los tres sitios: como la fuente ya era mas baja que
   cualquier recorte, no quitaba nada... por el eje equivocado. Meta la
   habria recortado POR LOS LADOS. O sea el mismo fallo de las portadas de
   coleccion -- medir uno de los dos recortes -- cometido otra vez, aqui, en
   la herramienta hecha para no cometerlo. Ahora se compara la proporcion de
   la fuente con la del destino y se recorta por el eje que sobra, y la caja
   segura es un RECTANGULO: la interseccion de los tres, en los dos ejes.

   NO COMPRUEBA SI HAY TEXTO, y hay que decirlo. Detectar letras sin OCR no es
   fiable, y una comprobacion que a veces acierta es peor que ninguna porque
   se confia en ella. La regla del texto se cumple en el prompt: las imagenes
   de esta tienda NO llevan texto, porque una imagen es UNA sola para los
   cinco idiomas y el texto no se traduce. El copy va en el anuncio, que Meta
   si sirve por idioma.

   Uso:  node marca/comprobar-creatividad.mjs <imagen> [--zona 0.55]         */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const ruta = process.argv[2];
if (!ruta || !fs.existsSync(ruta)) {
  console.error('Falta la imagen.  Uso: node marca/comprobar-creatividad.mjs <imagen>');
  process.exit(2);
}
/* Cuanta tinta tiene que haber dentro de la caja segura para darla por buena.
   Por defecto el 55 % de toda la del cuadro: si mas de un 45 % de lo que se
   ve vive fuera, algo importante se va a cortar. */
const i = process.argv.indexOf('--zona');
const MINIMO = i > 0 ? Number(process.argv[i + 1]) : 0.55;

const RECORTES = [['9:16', 9 / 16], ['4:5', 4 / 5], ['1:1', 1 / 1]];

const nav = await chromium.launch({ executablePath: CHROME });
const pg = await (await nav.newContext()).newPage();
await pg.setContent('<body style="margin:0">');

const b64 = fs.readFileSync(ruta).toString('base64');
const med = await pg.evaluate(async (b64) => {
  const im = new Image();
  im.src = 'data:image/png;base64,' + b64;
  await im.decode();
  const c = document.createElement('canvas');
  c.width = im.naturalWidth; c.height = im.naturalHeight;
  const x = c.getContext('2d');
  x.drawImage(im, 0, 0);
  const d = x.getImageData(0, 0, c.width, c.height).data;
  /* El fondo de esta marca es casi negro, asi que "tinta" es el pixel que
     brilla bastante mas que el fondo. Se guarda la posicion de cada uno
     para poder preguntarle a cualquier rectangulo cuanta cae dentro. */
  const px = [];
  for (let y = 0; y < c.height; y++) {
    for (let X = 0; X < c.width; X++) {
      const k = (y * c.width + X) * 4;
      if (d[k + 3] < 24) continue;
      if (d[k] + d[k + 1] + d[k + 2] > 200) px.push(X, y);
    }
  }
  return { w: c.width, h: c.height, px };
}, b64);
await nav.close();

const { w, h, px } = med;
const total = px.length / 2;
console.log('\n' + path.basename(ruta) + '   ' + w + 'x' + h + '   proporcion ' + (w / h).toFixed(3));

if (!total) { console.error('\nLa imagen no tiene tinta: esta en negro o el umbral no le sirve.'); process.exit(1); }

function dentro(x0, x1, y0, y1) {
  let n = 0;
  for (let i = 0; i < px.length; i += 2) {
    const X = px[i], Y = px[i + 1];
    if (X >= x0 && X < x1 && Y >= y0 && Y < y1) n++;
  }
  return n;
}

/* El recorte centrado de una proporcion: se quita por el eje que SOBRA. */
function recorte(r) {
  const fuente = w / h;
  if (fuente > r) {                       // la fuente es mas ancha: se cortan los lados
    const ancho = Math.round(h * r);
    const a = Math.round((w - ancho) / 2);
    return { x0: a, x1: a + ancho, y0: 0, y1: h, eje: 'por los lados' };
  }
  const alto = Math.round(w / r);         // la fuente es mas alta: se corta arriba y abajo
  const a = Math.round((h - alto) / 2);
  return { x0: 0, x1: w, y0: a, y1: a + alto, eje: 'arriba y abajo' };
}

let X0 = 0, X1 = w, Y0 = 0, Y1 = h;
console.log('');
for (const [nom, r] of RECORTES) {
  const c = recorte(r);
  X0 = Math.max(X0, c.x0); X1 = Math.min(X1, c.x1);
  Y0 = Math.max(Y0, c.y0); Y1 = Math.min(Y1, c.y1);
  const pc = (dentro(c.x0, c.x1, c.y0, c.y1) / total) * 100;
  console.log('  recorte ' + nom.padEnd(5) + ' ' + (c.x1 - c.x0) + 'x' + (c.y1 - c.y0) +
              '  (' + c.eje.padEnd(14) + ')  conserva el ' + pc.toFixed(1) + ' % de la tinta');
}

const enCaja = dentro(X0, X1, Y0, Y1);
const frac = enCaja / total;
console.log('\n  caja segura   x ' + X0 + '..' + X1 + '   y ' + Y0 + '..' + Y1 +
            '   (' + (X1 - X0) + 'x' + (Y1 - Y0) + ')');
console.log('  tinta dentro  ' + (frac * 100).toFixed(1) + ' %   (hace falta ' + (MINIMO * 100).toFixed(0) + ' %)');

/* Y donde esta el grueso del sujeto: el porcentaje global puede salvarse con
   fondo repartido y el sujeto cortarse igual. */
let sx = 0, sy = 0;
for (let i = 0; i < px.length; i += 2) { sx += px[i]; sy += px[i + 1]; }
const cx = Math.round(sx / total), cy = Math.round(sy / total);
const centroDentro = cx >= X0 && cx < X1 && cy >= Y0 && cy < Y1;
console.log('  centro de la tinta en (' + cx + ', ' + cy + ')  ->  ' +
            (centroDentro ? 'dentro' : '*** FUERA ***') + ' de la caja');

if (frac < MINIMO || !centroDentro) {
  console.error('\nNO SIRVE tal cual: en alguno de los tres sitios se va a cortar lo que importa.');
  console.error('Genera con el sujeto centrado, o recorta a mano dejando todo dentro de x ' +
                X0 + '..' + X1 + ', y ' + Y0 + '..' + Y1 + '.');
  process.exit(1);
}
console.log('\nSirve para los tres sitios de Meta: feed cuadrado, feed vertical y Stories.');
