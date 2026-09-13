/* Portadas de los articulos del Diario, 1200x630.
   ------------------------------------------------------------------
   POR QUE EXISTEN. Los trece articulos del blog no tenian imagen: ninguno.
   En la tienda se veia -- el tema dibuja de respaldo una letra de neon sobre
   una rejilla, que aguanta pero no dice nada -- y fuera de la tienda se veia
   PEOR: sin imagen no hay og:image, asi que cada vez que alguien comparte un
   articulo en WhatsApp, en X o en LinkedIn sale una tarjeta sin nada. Y las
   vistas generales de los buscadores y los sistemas de IA que citan fuentes
   tiran de esa misma imagen.

   No son fotos: son portadas tipograficas en la identidad del tema. Cada una
   lleva su titulo, su familia y un acento de color por tema, para que una
   fila de articulos se lea como una coleccion y no como un saco.

   1200x630 es la proporcion que piden Open Graph y Twitter. Se rinden con el
   Chromium que ya trae el contenedor, sin dependencias nuevas.

   Uso:  node marca/generar-portadas.mjs                                    */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const SALIDA = path.join(RAIZ, 'marca/portadas');
const FUENTE = path.join(RAIZ, 'theme/assets/orbitron-variable.woff2');

const FAMILIAS = {
  suplementos: { etiqueta: 'SUPLEMENTOS', color: '#00d4ff' },
  nutricion:   { etiqueta: 'NUTRICIÓN',   color: '#00e87b' },
  entreno:     { etiqueta: 'ENTRENAMIENTO', color: '#ff2ecb' },
  descanso:    { etiqueta: 'DESCANSO',    color: '#0077ff' },
  equipo:      { etiqueta: 'EQUIPO',      color: '#ff7700' },
  codices:     { etiqueta: 'CÓDICES',     color: '#ffd000' },
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

/* El titulo manda sobre el cuerpo: cuanto mas largo, mas pequeno, para que
   nunca se salga del lienzo ni quede una linea suelta abajo. Medido sobre los
   doce titulos reales, no a ojo. */
function tamano(t) {
  const n = t.length;
  if (n <= 30) return 78;
  if (n <= 42) return 68;
  if (n <= 54) return 60;
  return 52;
}

const pagina = (titulo, fam) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>
  @font-face{font-family:'Orbitron';src:url(data:font/woff2;base64,${fuenteB64}) format('woff2');font-weight:400 900;font-display:block}
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:630px;overflow:hidden;background:#060612;
       font-family:'Orbitron',system-ui,sans-serif;color:#fff;position:relative}
  /* rejilla en fuga, la misma del tema */
  .rejilla{position:absolute;inset:0;
    background-image:linear-gradient(${fam.color}1f 1px,transparent 1px),
                     linear-gradient(90deg,${fam.color}1f 1px,transparent 1px);
    background-size:48px 48px}
  .halo{position:absolute;width:900px;height:900px;border-radius:50%;
    left:-260px;top:-380px;
    background:radial-gradient(circle,${fam.color}38 0%,${fam.color}12 38%,transparent 68%)}
  .halo2{position:absolute;width:620px;height:620px;border-radius:50%;
    right:-200px;bottom:-300px;
    background:radial-gradient(circle,${fam.color}22 0%,transparent 66%)}
  .borde{position:absolute;inset:0;border:2px solid ${fam.color}40}
  .filo{position:absolute;left:0;right:0;top:0;height:6px;
    background:linear-gradient(90deg,${fam.color},#ff2ecb 55%,#7b2fff)}
  .cuerpo{position:absolute;inset:0;padding:72px 84px;display:flex;flex-direction:column;justify-content:space-between}
  .arriba{display:flex;align-items:center;gap:18px}
  .marca{font-weight:900;font-size:21px;letter-spacing:.28em;color:#fff}
  .marca span{color:${fam.color}}
  .fam{font-weight:700;font-size:15px;letter-spacing:.22em;color:${fam.color};
    border:1.5px solid ${fam.color}66;border-radius:999px;padding:8px 16px;background:${fam.color}14}
  h1{font-weight:800;font-size:${tamano(titulo)}px;line-height:1.14;letter-spacing:-.012em;
     max-width:17ch;text-wrap:balance;
     text-shadow:0 0 34px ${fam.color}5c, 0 2px 0 rgba(0,0,0,.4)}
  .abajo{display:flex;align-items:center;justify-content:space-between}
  .pie{font-weight:600;font-size:17px;letter-spacing:.16em;color:#a9b6cc}
  .raya{height:4px;width:190px;border-radius:2px;
    background:linear-gradient(90deg,${fam.color},transparent)}
</style></head><body>
  <div class="rejilla"></div><div class="halo"></div><div class="halo2"></div>
  <div class="borde"></div><div class="filo"></div>
  <div class="cuerpo">
    <div class="arriba"><div class="marca">VI<span>LLUMINATION</span></div><div class="fam">${fam.etiqueta}</div></div>
    <h1>${titulo.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</h1>
    <div class="abajo"><div class="pie">EL DIARIO · VILLUMINATIONS.COM</div><div class="raya"></div></div>
  </div>
</body></html>`;

fs.mkdirSync(SALIDA, { recursive: true });
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const [handle, titulo, familia] of ARTICULOS) {
  await p.setContent(pagina(titulo, FAMILIAS[familia]), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(SALIDA, handle + '.png') });
  const kb = Math.round(fs.statSync(path.join(SALIDA, handle + '.png')).size / 1024);
  console.log(`  ${handle.padEnd(44)} ${String(kb).padStart(4)} KB  ${FAMILIAS[familia].etiqueta}`);
}
await b.close();
console.log(`\n  ${ARTICULOS.length} portadas en marca/portadas/`);
