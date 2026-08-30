/* Graba la secuencia de marca a un archivo de video.
   ------------------------------------------------------------------
   Cadena:  navegador -> fotogramas JPEG -> VP8/WebM

   Por que WebM y no MP4: el unico ffmpeg de este entorno es el que trae
   Playwright, compilado con --disable-everything. Solo lleva el codificador
   libvpx (VP8) y el contenedor webm; no hay H.264 ni muxer de mp4. Se
   comprobo antes de escribir esto, no se supone.

   Shopify solo admite .mp4 y .mov en su selector de video, asi que el .webm
   se convierte en el Mac con una orden (esta en el LEEME de esta carpeta) o
   se sube como archivo suelto y se pega su URL en la seccion.

   El tiempo lo pone este guion, no el navegador: asi el resultado no depende
   de lo rapido que vaya la maquina y dos ejecuciones dan el mismo video.

   Uso:  node estudio/video/renderizar.mjs [--fps 30] [--ancho 1080]        */
import { chromium } from 'playwright';
import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const FFMPEG = process.env.FFMPEG || '/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux';
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const arg = (n, d) => {
  const i = process.argv.indexOf('--' + n);
  return i > -1 && process.argv[i + 1] ? Number(process.argv[i + 1]) : d;
};
const FPS = arg('fps', 30);
const ANCHO = arg('ancho', 1080);
const ALTO = Math.round(ANCHO * 16 / 9);   // vertical 9:16
const DPR = 4;                              // 270x480 css * 4 = 1080x1920
const SALIDA = path.join(AQUI, 'villumination-marca.webm');

console.log(`  Renderizando ${ANCHO}x${ALTO} a ${FPS} fps`);

const navegador = await chromium.launch({ executablePath: CHROME });
const ctx = await navegador.newContext({
  viewport: { width: Math.round(ANCHO / DPR), height: Math.round(ALTO / DPR) },
  deviceScaleFactor: DPR,
});
const p = await ctx.newPage();
const errores = [];
p.on('pageerror', e => errores.push(e.message));

// Avisa al guion de que hay captura: asi no arranca su propio bucle y el
// tiempo lo manda este proceso.
await p.addInitScript(() => { window.__capturando = true; });
await p.goto('file://' + path.join(AQUI, 'escena.html'));

// La tipografia de la marca, incrustada (aqui no se llega a Google Fonts)
const fuente = fs.readFileSync(path.join(AQUI, 'fuente.b64'), 'utf8').trim();
await p.evaluate(async (b64) => {
  const cara = new FontFace('Orbitron', `url(data:font/woff2;base64,${b64}) format('woff2')`);
  await cara.load();
  document.fonts.add(cara);
  await document.fonts.ready;
}, fuente);

const duracion = await p.evaluate(() => window.__duracion);
const total = Math.round(duracion * FPS);
console.log(`  ${duracion} s = ${total} fotogramas`);

// Los fotogramas se acumulan en un archivo y ffmpeg lo lee DESPUES.
// La primera version se los pasaba por una tuberia y se bloqueaba: navegador,
// node y ffmpeg quedaban los tres al 0 % de CPU esperandose entre ellos. Un
// archivo intermedio de veinte megas es un precio ridiculo por no tener que
// razonar sobre contrapresion entre tres procesos.
//
// El build de ffmpeg solo trae el demuxer image2pipe y el decodificador
// mjpeg: no sabe leer PNG, por eso los fotogramas son JPEG.
const CRUDO = path.join(AQUI, '.fotogramas.jpg');
const flujo = fs.createWriteStream(CRUDO);
const escribir = (buf) => new Promise((res, rej) =>
  flujo.write(buf, err => err ? rej(err) : res()));

const t0 = Date.now();
for (let i = 0; i < total; i++) {
  await p.evaluate(t => window.__pintar(t), i / FPS);
  await escribir(await p.screenshot({ type: 'jpeg', quality: 92 }));
  if (i % 24 === 0 || i === total - 1)
    console.log(`  fotograma ${i + 1}/${total}  ${Math.round((i + 1) / total * 100)} %`);
}
await new Promise(res => flujo.end(res));
await navegador.close();

if (errores.length) {
  console.error('  errores de JavaScript en la escena: ' + errores.join(' | '));
  process.exit(1);
}

console.log(`  codificando ${(fs.statSync(CRUDO).size / 1048576).toFixed(1)} MB de fotogramas`);
const ff = spawn(FFMPEG, [
  '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', CRUDO,
  '-c:v', 'libvpx', '-b:v', '3000k', '-crf', '22',
  '-deadline', 'good', '-auto-alt-ref', '0', SALIDA,
], { stdio: ['ignore', 'ignore', 'pipe'] });
let ffErr = '';
ff.stderr.on('data', d => { ffErr += d.toString(); });
const codigo = await new Promise(res => ff.on('close', res));
try { fs.unlinkSync(CRUDO); } catch (e) {}

if (codigo !== 0) {
  console.error('  ffmpeg fallo:\n' + ffErr.split('\n').slice(-12).join('\n'));
  process.exit(1);
}
const mb = fs.statSync(SALIDA).size / 1048576;
console.log(`  Listo: ${path.relative(RAIZ, SALIDA)}  ${mb.toFixed(2)} MB  en ${((Date.now() - t0) / 1000).toFixed(0)} s`);
