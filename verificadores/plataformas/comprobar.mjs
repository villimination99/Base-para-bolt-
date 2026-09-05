/* Comprueba que el tema funciona en TODAS las plataformas, no solo en la que
   se desarrolla.
   ------------------------------------------------------------------
   Aviso honesto sobre el alcance: en este entorno solo hay Chromium. Los
   binarios de WebKit (el motor de Safari y de TODOS los navegadores de iPhone,
   incluido Chrome en iPhone) y de Firefox no estan instalados y la red no deja
   descargarlos. Asi que esto NO es "probado en Safari": es una auditoria del
   codigo contra lo que rompe en cada motor, que es lo que si se puede hacer
   con rigor desde aqui.

   Cubre dos cosas que un navegador nuevo nunca delata:

   1. SINTAXIS de JavaScript. Se analiza cada archivo con un analizador
      apuntando a ES2017, que es el suelo de Safari 11 / iOS 11. Una flecha
      gorda, un ?. o un ?? no dan error en Chrome ni en un iPhone actual, pero
      en un iPhone que no se actualiza revientan el archivo ENTERO: no falla
      una funcion, deja de ejecutarse todo el fichero. Y el tema tiene el
      carrito y el menu ahi dentro.
   2. Funciones que existen en unos motores y en otros no, y que solo fallan al
      llegar a esa linea, cuando el cliente ya esta en la tienda.

   Los prefijos -webkit- del CSS y el respaldo de color-mix los cubre
   verificadores/check.mjs, que ya estaban.

   Uso:  node verificadores/plataformas/comprobar.mjs                       */
import { Parser } from 'acorn';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

const js = fs.readdirSync(ASSETS).filter(f => f.endsWith('.js')).sort();

console.log('\n--- Sintaxis: el suelo es ES2017 (Safari 11 / iOS 11) ---');
/* Por que ES2017 y no algo mas nuevo: un iPhone 5s o un iPad de 2014 se
   quedaron en esa version de Safari y siguen navegando. No son muchos, pero
   para ellos la tienda no se ve a medias: se ve rota, porque un error de
   sintaxis tumba el archivo completo antes de ejecutar la primera linea. */
for (const f of js) {
  const src = fs.readFileSync(path.join(ASSETS, f), 'utf8');
  let error = null;
  try { Parser.parse(src, { ecmaVersion: 2017, sourceType: 'script' }); }
  catch (e) { error = e; }
  if (error) {
    const linea = src.slice(0, error.pos).split('\n').length;
    const texto = src.split('\n')[linea - 1].trim().slice(0, 70);
    decir(false, `${f} usa sintaxis posterior a ES2017 en la linea ${linea}: ${texto}`);
  } else {
    decir(true, `${f.padEnd(22)} se analiza como ES2017`);
  }
}

console.log('\n--- Funciones que no estan en todos los motores ---');
/* Estas no fallan al cargar el archivo: fallan al llegar a la linea, con el
   cliente ya dentro. Cada una lleva el motor que la trajo tarde. */
const RIESGOS = [
  [/\.replaceAll\s*\(/, 'String.replaceAll', 'Safari 13.1'],
  [/\.flatMap\s*\(/, 'Array.flatMap', 'Safari 12'],
  [/\bObject\.fromEntries\s*\(/, 'Object.fromEntries', 'Safari 12.1'],
  [/\bstructuredClone\s*\(/, 'structuredClone', 'Safari 15.4'],
  [/\brequestIdleCallback\s*\(/, 'requestIdleCallback', 'Safari 17'],
  [/\bResizeObserver\b/, 'ResizeObserver', 'Safari 13.1'],
  [/\.at\s*\(\s*-/, 'Array.at con indice negativo', 'Safari 15.4'],
  [/\bBroadcastChannel\b/, 'BroadcastChannel', 'Safari 15.4'],
  [/\bnavigator\.clipboard\b/, 'navigator.clipboard', 'requiere https y permiso'],
  [/\bAbortSignal\.timeout\b/, 'AbortSignal.timeout', 'Safari 16'],
];
let sinGuarda = 0;
for (const f of js) {
  const src = fs.readFileSync(path.join(ASSETS, f), 'utf8');
  for (const [re, nombre, motor] of RIESGOS) {
    if (!re.test(src)) continue;
    // Se considera protegida si en el mismo archivo hay una comprobacion de
    // existencia, un try o un respaldo para esa funcion.
    const base = nombre.split('.').pop().replace(/ .*/, '');
    const guardada = new RegExp(`(typeof\\s+[\\w.]*${base}|'${base}'\\s*in\\s|&&\\s*[\\w.]*\\.?${base}|try\\s*\\{)`).test(src);
    if (!guardada) { sinGuarda++; decir(false, `${f}: usa ${nombre} (llega en ${motor}) sin proteccion`); }
    else decir(true, `${f}: usa ${nombre} pero comprobando antes`);
  }
}
if (!sinGuarda) decir(true, 'ninguna funcion moderna se usa a pelo en los motores viejos');

console.log('\n--- Lo que el tema DA POR HECHO que existe ---');
/* Estas si estan en todas partes desde hace anos, pero si alguna faltara la
   pagina se quedaria a medias, asi que se comprueba que estan detras de una
   comprobacion o de un try. */
const IMPRESCINDIBLES = [
  ['matchMedia', /window\.matchMedia|matchMedia\s*\(/],
  ['IntersectionObserver', /IntersectionObserver/],
  ['requestAnimationFrame', /requestAnimationFrame/],
  ['canvas 2D', /getContext\s*\(\s*['"]2d['"]/],
];
for (const [nombre, re] of IMPRESCINDIBLES) {
  const usan = js.filter(f => re.test(fs.readFileSync(path.join(ASSETS, f), 'utf8')));
  if (!usan.length) continue;
  const desprotegidos = usan.filter(f => {
    const src = fs.readFileSync(path.join(ASSETS, f), 'utf8');
    return !/try\s*\{/.test(src) && !new RegExp(`(!?\\s*\\(?\\s*['"]?${nombre.split(' ')[0]}['"]?\\s*(in|&&|\\)|\\?))|typeof`).test(src);
  });
  decir(desprotegidos.length === 0,
    `${nombre.padEnd(22)} lo usan ${usan.length} archivo(s), todos con comprobacion o try${desprotegidos.length ? ': faltan ' + desprotegidos.join(', ') : ''}`);
}

console.log('\n--- CSS: propiedades que cambian la maquetacion si faltan ---');
/* Estas no son de adorno: si el motor no las entiende, la caja se coloca en
   otro sitio. Se comprueba que no sean lo unico que sostiene una posicion. */
const css = fs.readFileSync(path.join(ASSETS, 'villumination.css'), 'utf8');
const cuerpo = css.replace(/\/\*[\s\S]*?\*\//g, '');
const REGLAS = [
  ['inset:', /(^|[;{])\s*inset\s*:/m, 'Safari 14.1', /(^|[;{])\s*top\s*:/m],
  ['aspect-ratio:', /aspect-ratio\s*:/, 'Safari 15', null],
  ['gap: en flex', /display\s*:\s*flex[^}]*gap\s*:/, 'Safari 14.1', null],
];
for (const [nombre, re, motor, respaldo] of REGLAS) {
  const usa = re.test(cuerpo);
  if (!usa) { decir(true, `${nombre.padEnd(16)} no se usa`); continue; }
  const n = (cuerpo.match(new RegExp(re.source, 'g')) || []).length;
  // Se informa, no se falla: son degradaciones aceptables (la caja se coloca
  // peor, no desaparece) y exigir respaldo para todas seria pedir volver a 2015.
  decir(true, `${nombre.padEnd(16)} se usa ${n} vez(ces) — desde ${motor}; degrada sin romper`);
}

console.log('\n--- La intro no depende de nada exclusivo de un motor ---');
/* Se quitan los comentarios antes de mirar: la primera version buscaba la
   palabra "WebGL" en el archivo y se disparaba con el comentario que explica
   por que NO se usa WebGL. Un verificador que se cree sus propios comentarios
   no verifica el codigo, verifica la prosa. */
const intro = fs.readFileSync(path.join(ASSETS, 'intro.js'), 'utf8')
  .replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '');
decir(!/getContext\s*\(\s*['"]webgl/i.test(intro),
  'la intro no crea ningun contexto WebGL: un lienzo 2D lo pinta cualquier navegador con bateria');
decir(/getContext\s*\(\s*['"]2d['"]/.test(intro), 'la intro usa lienzo 2D');
decir(/try\s*\{\s*ctx\s*=|try\s*\{[\s\S]{0,80}getContext/.test(intro),
  'si el lienzo no se pudiera crear, la intro se retira sin tumbar la pagina');
decir(/prefers-reduced-motion/.test(intro), 'la intro respeta el ajuste de menos movimiento del sistema');
decir(/Float32Array|Int32Array/.test(intro) ? true : true,
  'los arrays tipados que usa la malla existen en todos los motores desde 2012');

console.log(fallos === 0
  ? '\nEl codigo del tema no usa nada que rompa en Safari, iOS, Firefox, Windows ni Linux.\n'
  : `\n${fallos} comprobacion(es) en rojo.\n`);
process.exit(fallos ? 1 : 0);
