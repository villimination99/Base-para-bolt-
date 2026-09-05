/* Extrae una portada del propio video, a partir del mismo guion.
   ------------------------------------------------------------------
   Sin portada propia, la seccion caia en la miniatura de YouTube: una imagen
   que ya no representa el video que se reproduce, y que ademas se le
   declaraba a Google como thumbnailUrl. Datos y pagina en desacuerdo.

   Se renderiza el instante que se pida del mismo guion, asi que la portada y
   el video son literalmente el mismo fotograma.

   Uso:  node estudio/video/portada.mjs [segundo]                           */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const T = Number(process.argv[2] || 20.6);
const SALIDA = path.join(AQUI, 'villumination-marca-portada.png');

const navegador = await chromium.launch({ executablePath: CHROME });
const ctx = await navegador.newContext({ viewport: { width: 270, height: 480 }, deviceScaleFactor: 4 });
const p = await ctx.newPage();
const errores = [];
p.on('pageerror', e => errores.push(e.message));
await p.addInitScript(() => { window.__capturando = true; });
await p.goto('file://' + path.join(AQUI, 'escena.html'));

const fuente = fs.readFileSync(path.join(AQUI, 'fuente.b64'), 'utf8').trim();
await p.evaluate(async (b64) => {
  const cara = new FontFace('Orbitron', `url(data:font/woff2;base64,${b64}) format('woff2')`);
  await cara.load(); document.fonts.add(cara); await document.fonts.ready;
}, fuente);

await p.evaluate(t => window.__pintar(t), T);
await p.waitForTimeout(300);
await p.screenshot({ path: SALIDA });
await navegador.close();

if (errores.length) { console.error('  errores: ' + errores.join(' | ')); process.exit(1); }
console.log(`  Listo: ${path.relative(RAIZ, SALIDA)}  1080x1920  segundo ${T}  ${(fs.statSync(SALIDA).size / 1024).toFixed(0)} KB`);
