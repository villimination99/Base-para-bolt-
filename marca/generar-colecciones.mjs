/* Portadas de las colecciones, 1600x1200.
   ------------------------------------------------------------------
   POR QUE EXISTEN. Las que habia llevaban texto en castellano dentro de la
   imagen -- la de los planes lo confesaba en su propio texto alternativo:
   "con el nombre de la coleccion Planes de entrenamiento". Y una imagen de
   coleccion en Shopify es UNA sola para las cinco lenguas: no hay version
   francesa del archivo. Es el mismo fallo que tenian las portadas del
   Diario y que el cliente vio en una captura. Lo que no se puede traducir
   no se escribe en una imagen.

   Aqui no se escribe NADA. Ni siquiera el dominio: el tema ya pinta el
   nombre de la coleccion encima o debajo de la tarjeta, y ese si se
   traduce. Lo que distingue una portada de otra es el color de la familia
   -- el mismo acento que usa la seccion de categorias de la portada --, su
   simbolo geometrico y una constelacion sembrada con el handle.

   LA CAJA SEGURA, Y AQUI ES MAS DURA QUE EN EL DIARIO. El tema pide esta
   imagen en CUATRO proporciones distintas, todas con recorte centrado:
     collection-list        700x500  (1.40)
     main-list-collections  800x600  (1.33)
     category-mosaic        900x700  (1.29)
     header, el megamenu    160x160  (1.00)  <-- esta manda
   La del megamenu es cuadrada, asi que de un lienzo 4:3 solo sobrevive el
   CUADRADO CENTRAL: 1200x1200 de los 1600 de ancho, o sea el 75 %. Todo lo
   que haya que ver vive ahi dentro, con margen. Fuera solo va decoracion:
   rejilla, halos y constelacion, que se pueden cortar sin perder nada.

   Uso:  node marca/generar-colecciones.mjs                                */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const SALIDA = path.join(RAIZ, 'marca/colecciones');

const A = 1600, ALTO = 1200;
/* El cuadrado central que sobrevive al recorte del megamenu, menos un
   margen de respiro. */
const LADO = ALTO;                       // 1200
const CAJA_X = (A - LADO) / 2;           // 200
const MARGEN = 90;

/* Un simbolo por coleccion, dibujado en SVG sobre un lienzo de 100x100.
   El color es el mismo acento que la seccion de categorias de la portada,
   para que la tienda entera hable en un solo idioma de color. */
const COLECCIONES = [
  ['ropa', '#00d4ff',
   '<path d="M35 18 L50 26 L65 18 L84 30 L76 44 L68 40 V86 H32 V40 L24 44 L16 30Z"/>'],
  ['equipo', '#ff2ecb',
   '<path d="M14 50h72"/><rect x="22" y="33" width="15" height="34" rx="3"/><rect x="63" y="33" width="15" height="34" rx="3"/><rect x="7" y="41" width="10" height="18" rx="3"/><rect x="83" y="41" width="10" height="18" rx="3"/>'],
  ['suplementos', '#00e87b',
   '<rect x="18" y="32" width="64" height="36" rx="18"/><path d="M50 32v36"/><circle cx="34" cy="50" r="5"/>'],
  ['conocimiento', '#ff7700',
   '<path d="M50 30C42 22 28 20 16 22v54c12-2 26 0 34 8"/><path d="M50 30c8-8 22-10 34-8v54c-12-2-26 0-34 8"/><path d="M50 30v62"/>'],
  ['planes', '#7b2fff',
   '<rect x="16" y="22" width="68" height="66" rx="8"/><path d="M16 42h68M34 14v16M66 14v16"/><path d="M36 62l9 9 19-19"/>'],
  ['cuidado-personal', '#ffd000',
   '<path d="M50 14c14 18 22 29 22 40a22 22 0 1 1-44 0c0-11 8-22 22-40Z"/><path d="M40 58c0 8 5 13 12 14"/>'],
];

/* Constelacion determinista: sembrada con el handle, asi que correr el
   generador dos veces da el mismo PNG. */
function semilla(txt) {
  let h = 2166136261;
  for (let i = 0; i < txt.length; i++) { h ^= txt.charCodeAt(i); h = Math.imul(h, 16777619); }
  return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 10000) / 10000; };
}

function constelacion(handle) {
  const r = semilla(handle);
  const pts = [];
  for (let i = 0; i < 40; i++) pts.push([Math.round(r() * A), Math.round(r() * ALTO), (r() * 3 + 1).toFixed(1)]);
  let svg = '';
  for (const [x, y, rad] of pts) svg += `<circle cx="${x}" cy="${y}" r="${rad}"/>`;
  for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) {
    const dx = pts[i][0] - pts[j][0], dy = pts[i][1] - pts[j][1];
    if (dx * dx + dy * dy < 46000) svg += `<line x1="${pts[i][0]}" y1="${pts[i][1]}" x2="${pts[j][0]}" y2="${pts[j][1]}"/>`;
  }
  return svg;
}

const pagina = (handle, color, glifo) => `<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:${A}px;height:${ALTO}px;overflow:hidden;background:#060612;position:relative}
  .rejilla{position:absolute;inset:0;
    background-image:linear-gradient(${color}1c 1px,transparent 1px),
                     linear-gradient(90deg,${color}1c 1px,transparent 1px);
    background-size:64px 64px}
  .estrellas{position:absolute;inset:0}
  .estrellas circle{fill:${color};opacity:.36}
  .estrellas line{stroke:${color};stroke-width:.8;opacity:.15}
  .halo{position:absolute;width:1100px;height:1100px;border-radius:50%;
    left:50%;top:50%;transform:translate(-50%,-50%);
    background:radial-gradient(circle,${color}3a 0%,${color}14 36%,transparent 66%)}
  .borde{position:absolute;inset:0;border:3px solid ${color}3a}
  .filo{position:absolute;left:0;right:0;top:0;height:8px;
    background:linear-gradient(90deg,${color},#ff2ecb 55%,#7b2fff)}
  /* El simbolo, centrado y dentro del cuadrado que sobrevive al recorte
     cuadrado del megamenu. */
  .glifo{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
    width:440px;height:440px;filter:drop-shadow(0 0 46px ${color}88)}
  .glifo svg{width:100%;height:100%;fill:none;stroke:${color};stroke-width:3.2;
             stroke-linecap:round;stroke-linejoin:round}
  .anillo{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
    width:620px;height:620px;border-radius:50%;border:2px solid ${color}30}
</style></head><body>
  <div class="rejilla"></div>
  <svg class="estrellas" viewBox="0 0 ${A} ${ALTO}">${constelacion(handle)}</svg>
  <div class="halo"></div>
  <div class="anillo"></div>
  <div class="borde"></div><div class="filo"></div>
  <div class="glifo"><svg viewBox="0 0 100 100">${glifo}</svg></div>
</body></html>`;

fs.mkdirSync(SALIDA, { recursive: true });
const fuera = [];
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: A, height: ALTO }, deviceScaleFactor: 1 });

for (const [handle, color, glifo] of COLECCIONES) {
  await p.setContent(pagina(handle, color, glifo), { waitUntil: 'load' });
  /* SE MIDE, NO SE SUPONE. El simbolo tiene que caber en el cuadrado
     central con su margen; si uno solo se sale, no se escribe ninguna. */
  const mal = await p.evaluate(([x0, lado, margen]) => {
    const r = document.querySelector('.glifo').getBoundingClientRect();
    const izq = x0 + margen, der = x0 + lado - margen;
    const malos = [];
    if (r.left < izq - 0.5) malos.push('se sale por la izquierda');
    if (r.right > der + 0.5) malos.push('se sale por la derecha');
    if (r.top < margen - 0.5) malos.push('se sale por arriba');
    if (r.bottom > lado - margen + 0.5) malos.push('se sale por abajo');
    return malos;
  }, [CAJA_X, LADO, MARGEN]);
  if (mal.length) fuera.push(`${handle}: ${mal.join(', ')}`);
  await p.screenshot({ path: path.join(SALIDA, handle + '.png') });
  const kb = Math.round(fs.statSync(path.join(SALIDA, handle + '.png')).size / 1024);
  console.log(`  ${handle.padEnd(20)} ${String(kb).padStart(4)} KB  ${color}${mal.length ? '   <<<< SE SALE' : ''}`);
}
await b.close();

if (fuera.length) {
  console.error('\n  Estas se salen del cuadrado que sobrevive al recorte:');
  for (const f of fuera) console.error('   ' + f);
  process.exit(1);
}
console.log(`\n  ${COLECCIONES.length} portadas de coleccion en marca/colecciones/, sin una palabra dentro.`);
