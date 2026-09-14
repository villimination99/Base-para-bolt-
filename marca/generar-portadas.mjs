/* Portadas de los articulos del Diario, 1200x630.
   ------------------------------------------------------------------
   POR QUE EXISTEN. Los trece articulos del blog no tenian imagen: ninguno.
   En la tienda se veia -- el tema dibuja de respaldo una letra de neon sobre
   una rejilla, que aguanta pero no dice nada -- y fuera de la tienda se veia
   PEOR: sin imagen no hay og:image, asi que cada vez que alguien comparte un
   articulo en WhatsApp, en X o en LinkedIn sale una tarjeta sin nada. Y las
   vistas generales de los buscadores y los sistemas de IA que citan fuentes
   tiran de esa misma imagen.

   NO LLEVAN TEXTO, Y ESA ES LA REGLA. La primera version horneaba el titulo
   del articulo, la palabra de la familia ("NUTRICION") y "EL DIARIO" dentro
   del PNG. Una imagen de articulo en Shopify es UNA sola para las cinco
   lenguas: no hay version francesa del archivo. Asi que un visitante en
   frances veia la interfaz en frances, el articulo en frances y encima una
   portada que decia "Cuanta proteina hace falta al dia". Lo vio el cliente
   en una captura y tiene toda la razon: lo que no se puede traducir no se
   escribe en una imagen.

   Lo unico escrito que queda es el dominio -- villuminations.com -- que es
   un nombre propio y se lee igual en los cinco idiomas.

   Lo que distingue una portada de otra ya no son palabras sino el color de
   la familia, su simbolo geometrico y una constelacion sembrada con el
   handle del articulo: doce portadas distintas, ninguna traducible.

   1200x630 es la proporcion que piden Open Graph y Twitter. Se rinden con el
   Chromium que ya trae el contenedor, sin dependencias nuevas.

   LA CAJA SEGURA, QUE ES LA LECCION DE LA PRIMERA VERSION. La tarjeta del
   blog NO ensena la portada entera: la recorta DOS veces seguidas. Primero
   el Liquid le pide a Shopify 700x450 con recorte centrado, que ya deja
   fuera el 18 % del ancho; despues el CSS hace object-fit:cover sobre un
   hueco de ancho_tarjeta x 210 px y vuelve a recortar. Con la rejilla
   minmax(280px,1fr), el peor caso deja a la vista el 70 % del ancho y el
   68 % del alto.

   La primera version ponia la marca al 7 % del borde -- dentro de la zona
   que se corta -- y en un movil se veia "ILLUMINATION" y el titulo sin su
   primera letra. Lo vio el cliente en una captura, no yo.

   Asi que todo lo que hay que leer vive dentro de 840x428 px centrados.
   Fuera de esa caja solo va decoracion: rejilla, halos y el filo de color,
   que se pueden cortar sin que se pierda nada. El archivo sigue siendo
   1200x630 completo, asi que al compartirlo en redes se ve entero.

   Uso:  node marca/generar-portadas.mjs                                    */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const SALIDA = path.join(RAIZ, 'marca/portadas');
const FUENTE = path.join(RAIZ, 'theme/assets/orbitron-variable.woff2');

/* Un simbolo por familia, dibujado en SVG: dice lo mismo que la palabra
   pero no hay que traducirlo. Todos caben en un lienzo de 100x100. */
const FAMILIAS = {
  suplementos: { color: '#00d4ff', glifo: '<circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="12"/><path d="M50 8v12M50 80v12M8 50h12M80 50h12"/>' },
  nutricion:   { color: '#00e87b', glifo: '<path d="M50 88C50 60 30 44 16 40c-2 26 12 46 34 48Z"/><path d="M50 88c0-30 20-46 34-50 2 26-12 46-34 50Z"/><path d="M50 88V46"/>' },
  entreno:     { color: '#ff2ecb', glifo: '<path d="M14 50h72"/><rect x="22" y="34" width="14" height="32" rx="3"/><rect x="64" y="34" width="14" height="32" rx="3"/><rect x="8" y="42" width="10" height="16" rx="3"/><rect x="82" y="42" width="10" height="16" rx="3"/>' },
  descanso:    { color: '#0077ff', glifo: '<path d="M66 14a38 38 0 1 0 22 50A30 30 0 0 1 66 14Z"/><circle cx="26" cy="26" r="3"/><circle cx="40" cy="16" r="2"/>' },
  equipo:      { color: '#ff7700', glifo: '<rect x="16" y="16" width="68" height="68" rx="10"/><path d="M16 50h68M50 16v68"/><circle cx="50" cy="50" r="9"/>' },
  codices:     { color: '#ffd000', glifo: '<path d="M50 8 88 30v40L50 92 12 70V30Z"/><path d="M50 8v84M12 30l76 40M88 30 12 70"/>' },
};

export const ARTICULOS = [
  ['creatina', 'Creatina: cuánta, cuándo y por qué el monohidrato', 'suplementos'],
  ['que-suplementos-tienen-evidencia', 'Qué suplementos tienen evidencia y cuáles no', 'suplementos'],
  ['como-elegir-una-proteina-en-polvo', 'Cómo elegir una proteína en polvo', 'suplementos'],
  ['que-lleva-un-preentreno', 'Qué lleva un preentreno, y qué hace cada cosa', 'suplementos'],
  ['como-se-lee-una-etiqueta-nutricional', 'Cómo se lee una etiqueta nutricional', 'nutricion'],
  ['cuanta-proteina-hace-falta-al-dia', 'Cuánta proteína hace falta al día', 'nutricion'],
  ['superalimentos-en-polvo-sustituyen-verdura', 'Un superalimento en polvo no sustituye a la verdura', 'nutricion'],
  ['cuanta-actividad-fisica-hace-falta', 'Cuánta actividad física hace falta de verdad', 'entreno'],
  ['cuantas-horas-hay-que-dormir', 'Cuántas horas hay que dormir, y qué pasa si no', 'descanso'],
  ['gimnasio-en-casa-que-comprar-primero', 'Gimnasio en casa: qué comprar primero', 'equipo'],
  ['que-es-un-decanato', 'Qué es un decanato, y por qué tu signo no te describe', 'codices'],
  ['que-es-un-arcano-mayor', 'Qué es un arcano mayor', 'codices'],
];

const fuenteB64 = fs.readFileSync(FUENTE).toString('base64');

/* La constelacion: puntos sembrados con el handle, para que dos articulos
   de la misma familia no salgan identicos. Determinista a proposito --
   correr el generador dos veces da el mismo PNG, byte a byte. */
function semilla(txt) {
  let h = 2166136261;
  for (let i = 0; i < txt.length; i++) { h ^= txt.charCodeAt(i); h = Math.imul(h, 16777619); }
  return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 10000) / 10000; };
}

function constelacion(handle) {
  const r = semilla(handle);
  const pts = [];
  for (let i = 0; i < 34; i++) pts.push([Math.round(r() * 1200), Math.round(r() * 630), (r() * 2.4 + 0.8).toFixed(1)]);
  let svg = '';
  for (const [x, y, rad] of pts) svg += `<circle cx="${x}" cy="${y}" r="${rad}"/>`;
  /* Lineas solo entre puntos cercanos: una telarana, no un ovillo. */
  for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) {
    const dx = pts[i][0] - pts[j][0], dy = pts[i][1] - pts[j][1];
    if (dx * dx + dy * dy < 27000) svg += `<line x1="${pts[i][0]}" y1="${pts[i][1]}" x2="${pts[j][0]}" y2="${pts[j][1]}"/>`;
  }
  return svg;
}

const pagina = (handle, fam) => `<!doctype html><html lang="en"><head><meta charset="utf-8">
<style>
  @font-face{font-family:'Orbitron';src:url(data:font/woff2;base64,${fuenteB64}) format('woff2');font-weight:400 900;font-display:block}
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:630px;overflow:hidden;background:#060612;
       font-family:'Orbitron',system-ui,sans-serif;color:#fff;position:relative}
  .rejilla{position:absolute;inset:0;
    background-image:linear-gradient(${fam.color}1f 1px,transparent 1px),
                     linear-gradient(90deg,${fam.color}1f 1px,transparent 1px);
    background-size:48px 48px}
  .estrellas{position:absolute;inset:0}
  .estrellas circle{fill:${fam.color};opacity:.38}
  .estrellas line{stroke:${fam.color};stroke-width:.7;opacity:.16}
  .halo{position:absolute;width:900px;height:900px;border-radius:50%;
    left:-260px;top:-380px;
    background:radial-gradient(circle,${fam.color}38 0%,${fam.color}12 38%,transparent 68%)}
  .halo2{position:absolute;width:620px;height:620px;border-radius:50%;
    right:-200px;bottom:-300px;
    background:radial-gradient(circle,${fam.color}22 0%,transparent 66%)}
  .borde{position:absolute;inset:0;border:2px solid ${fam.color}40}
  .filo{position:absolute;left:0;right:0;top:0;height:6px;
    background:linear-gradient(90deg,${fam.color},#ff2ecb 55%,#7b2fff)}
  /* LA CAJA SEGURA SIGUE MANDANDO: 840x428 centrados. Aqui dentro va el
     simbolo, la marca y el dominio; fuera solo decoracion que se puede
     cortar sin perder nada. */
  .cuerpo{position:absolute;inset:0;padding:101px 180px;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start}
  .marca{font-weight:900;font-size:19px;letter-spacing:.24em;color:#fff;white-space:nowrap}
  .marca span{color:${fam.color}}
  .centro{align-self:center;display:flex;align-items:center;gap:26px}
  .glifo{width:190px;height:190px;filter:drop-shadow(0 0 30px ${fam.color}88)}
  .glifo svg{width:100%;height:100%;fill:none;stroke:${fam.color};stroke-width:3.4;
             stroke-linecap:round;stroke-linejoin:round}
  .anillo{width:190px;height:190px;position:absolute;border-radius:50%;
    border:1.5px solid ${fam.color}3a}
  .abajo{width:100%;display:flex;align-items:center;justify-content:space-between;gap:20px}
  .pie{font-weight:600;font-size:15px;white-space:nowrap;letter-spacing:.16em;color:#a9b6cc}
  .raya{height:4px;width:150px;flex:0 0 auto;border-radius:2px;
    background:linear-gradient(90deg,${fam.color},transparent)}
</style></head><body>
  <div class="rejilla"></div>
  <svg class="estrellas" viewBox="0 0 1200 630">${constelacion(handle)}</svg>
  <div class="halo"></div><div class="halo2"></div>
  <div class="borde"></div><div class="filo"></div>
  <div class="cuerpo">
    <div class="marca">VI<span>LLUMINATION</span></div>
    <div class="centro"><div class="glifo"><svg viewBox="0 0 100 100">${fam.glifo}</svg></div></div>
    <div class="abajo"><div class="pie">VILLUMINATIONS.COM</div><div class="raya"></div></div>
  </div>
</body></html>`;

fs.mkdirSync(SALIDA, { recursive: true });
const salidas = [];
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const [handle, titulo, familia] of ARTICULOS) {
  await p.setContent(pagina(handle, FAMILIAS[familia]), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  /* SE MIDE, NO SE SUPONE. Cada cosa legible tiene que caber en la caja
     segura; si una sola se sale, no se escribe ninguna portada. */
  const fuera = await p.evaluate(([mx, my]) => {
    const malos = [];
    for (const el of document.querySelectorAll('.marca,.glifo,.pie')) {
      const r = el.getBoundingClientRect();
      if (r.left < mx - 0.5 || r.right > 1200 - mx + 0.5 || r.top < my - 0.5 || r.bottom > 630 - my + 0.5) {
        malos.push(`${el.className || el.tagName} [${Math.round(r.left)},${Math.round(r.top)} → ${Math.round(r.right)},${Math.round(r.bottom)}]`);
      }
    }
    return malos;
  }, [180, 101]);
  if (fuera.length) { salidas.push(`${handle}: ${fuera.join(' | ')}`); }
  await p.screenshot({ path: path.join(SALIDA, handle + '.png') });
  const kb = Math.round(fs.statSync(path.join(SALIDA, handle + '.png')).size / 1024);
  console.log(`  ${handle.padEnd(44)} ${String(kb).padStart(4)} KB  ${familia.padEnd(12)}${fuera.length ? '   <<<< SE SALE' : ''}`);
}
await b.close();
if (salidas.length) {
  console.error('\n  Estas portadas se salen de la caja segura de 840x428:');
  for (const s of salidas) console.error('   ' + s);
  process.exit(1);
}
console.log(`\n  ${ARTICULOS.length} portadas en marca/portadas/`);
