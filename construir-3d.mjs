/* Empaqueta el mapa muscular 3D en un solo archivo para assets/.
   ------------------------------------------------------------------
   Por que existe este paso, que es el unico del tema:

   El mapa 3D usa three.js. Hasta la version 4.45.0 three.js venia de
   jsdelivr y se resolvia con un <script type="importmap">. Dos problemas
   medidos, no teoricos:

   1. Los importmap solo existen desde Safari 16.4 (marzo de 2023). Un
      iPhone con iOS 15 o con iOS 16.0-16.3 no resuelve el especificador
      'three', el modulo revienta al cargar y el visitante ve el lienzo
      vacio. No es que se vea peor: no hay mapa.
   2. Si jsdelivr esta bloqueado -- red de empresa, filtro de pais -- pasa
      lo mismo, y ademas cada visita le entrega su IP a un tercero.

   El argumento que habia a favor del CDN ("muchas visitas ya lo traen en
   cache de otras webs") dejo de ser cierto: Chrome particiona la cache por
   sitio desde la 86 (2020), Safari desde 2013 y Firefox desde 2021. Un
   three.js cacheado en otra web NO se reutiliza aqui. El beneficio no
   existe; los dos problemas si.

   Asi que three.js viaja dentro del asset. La fuente, con sus imports, se
   queda en fuente/vi-p-3d.js -- que es la que se edita -- y esto produce
   theme/assets/vi-p-3d.js, que es la que se sube. Sigue siendo un modulo
   ES (type="module"), soportado desde Safari 10.1, pero ya no necesita
   resolver ningun especificador externo.

   Para reconstruirlo:  node construir-3d.mjs
*/
import fs from 'fs';
import { createRequire } from 'module';

/* Las tres piezas que hacen falta para construir. No estan declaradas en
   ningun package.json porque el repositorio no versiona uno (ver .gitignore:
   esto es un tema de Shopify, no un proyecto de node), asi que si faltan hay
   que decirlo con la orden exacta en vez de dejar caer un MODULE_NOT_FOUND. */
const req = createRequire(import.meta.url);
for (const [mod, quien] of [['esbuild', 'para empaquetar'], ['three', 'el motor 3D'], ['chart.js', 'las graficas'], ['acorn', 'para comprobar la salida']]) {
  try { req.resolve(mod); } catch {
    console.error(`  falta ${mod} (${quien}).`);
    console.error('  npm i --no-save esbuild@0.28.2 three@0.160.0 chart.js@4.4.0 acorn');
    process.exit(1);
  }
}
const esbuild = req('esbuild');
const { Parser } = req('acorn');

/* Cuenta los import que quedan SIN resolver en la salida. Se parsea de
   verdad en vez de buscar la palabra con una expresion regular: la primera
   version de esta comprobacion daba rojo porque Chart.js lleva un aviso en
   ingles que dice "Please import and register the Filler plugin", y la
   palabra "import" dentro de una cadena de texto no es un import. */
function importsPendientes(js) {
  const arbol = Parser.parse(js, { ecmaVersion: 2020, sourceType: 'module' });
  return arbol.body.filter(n => n.type === 'ImportDeclaration').map(n => n.source.value);
}

const ENTRADA = 'fuente/vi-p-3d.js';
const SALIDA  = 'theme/assets/vi-p-3d.js';

const r = await esbuild.build({
  entryPoints: [ENTRADA],
  bundle: true,
  format: 'esm',
  /* es2020 y no mas abajo a proposito. El renderizador de three r160 pide
     WebGL2, que en iPhone llega con iOS 15, asi que bajar la sintaxis por
     debajo de ahi no gana ni un dispositivo: solo engorda el archivo. Y si
     alguien llega con un motor mas viejo, el modulo no se ejecuta y salta el
     respaldo que ya tiene la seccion, que es lo mismo que pasaria si fallara
     el WebGL. */
  target: ['es2020'],
  minify: true,
  legalComments: 'eof',   // el aviso MIT de three.js viaja con el codigo
  write: false,
  banner: { js: '/* Villumination 3D - mapa muscular. Generado por construir-3d.mjs a partir de fuente/vi-p-3d.js.\n   Incluye three.js 0.160.0 (MIT, (c) 2010-2024 three.js authors) y sus complementos.\n   No editar aqui: se sobreescribe. */' }
});

const js = r.outputFiles[0].text;

/* Comprobaciones que tienen que pasar SIEMPRE, porque un paquete a medias
   se ve exactamente igual que uno bueno hasta que alguien abre la pagina. */
const fallos = [];
if (js.length < 400000) fallos.push(`el paquete son ${js.length} B y three.js solo ya pasa de 400 KB: no ha entrado`);
const sueltos = importsPendientes(js);
if (sueltos.length) fallos.push('quedan imports sin resolver: ' + sueltos.join(', '));
if (!/MarchingCubes|marchingcubes/i.test(js)) fallos.push('falta MarchingCubes, que es con lo que se construye el cuerpo');
if (!js.includes('__mmFocus')) fallos.push('falta __mmFocus, el enganche que usa el hub para encuadrar un musculo');
if (!js.includes('muscle-canvas')) fallos.push('falta el lienzo muscle-canvas');
if (fallos.length) { console.error('  NO se escribe nada:'); fallos.forEach(f => console.error('   - ' + f)); process.exit(1); }

fs.writeFileSync(SALIDA, js);
console.log(`  ${ENTRADA} (${(fs.statSync(ENTRADA).size/1024).toFixed(0)} KB de fuente)`);
console.log(`  -> ${SALIDA}  ${(js.length/1024).toFixed(0)} KB `);
console.log('  three.js y sus complementos van dentro: ya no hace falta importmap ni CDN.');

/* ---- Y la grafica, por lo mismo: venia de jsdelivr y ahora viaja dentro ----
   Aqui ademas se aprovecha para recortar: de las treinta y tantas graficas
   que trae Chart.js, el hub dibuja dos. Ver fuente/vi-p-chart.js. */
const rc = await esbuild.build({
  entryPoints: ['fuente/vi-p-chart.js'],
  bundle: true, format: 'iife',
  /* ES2017 aqui, y no es un capricho: esto se carga como script CLASICO, sin
     type="module", asi que TODOS los motores lo parsean -- tambien los viejos.
     Una sola pieza de sintaxis moderna (un ?? , un ?.) es un error de sintaxis
     que tumba el archivo entero, y el hub se queda sin graficas en vez de sin
     una linea. El modulo 3D puede permitirse es2020 justo por lo contrario:
     va con type="module" y el motor que no lo entiende lo ignora entero.

     Lo encontro la bateria verificadores/plataformas, y solo pudo encontrarlo
     porque el archivo ya no vive en un CDN: mientras Chart.js venia de
     jsdelivr, su sintaxis no la miraba nadie. Cuesta 1 KB mas. */
  target: ['es2017'],
  minify: true, write: false,
  /* legalComments 'eof': three.js y Chart.js son MIT y su aviso de copyright
     tiene que viajar con el codigo distribuido. Con 'none' se borraba. Se
     agrupan al final del archivo para no estorbar al principio. */
  legalComments: 'eof',
  banner: { js: '/* Villumination 3D - graficas. Generado por construir-3d.mjs a partir de fuente/vi-p-chart.js.\n   Incluye Chart.js 4.4.0 (MIT, (c) 2014-2024 Chart.js Contributors), recortado a doughnut y bar.\n   No editar aqui: se sobreescribe. */' }
});
const cjs = rc.outputFiles[0].text;
const fc = [];
if (cjs.length < 60000) fc.push(`son ${cjs.length} B: Chart.js no ha entrado`);
const cSueltos = importsPendientes(cjs);
if (cSueltos.length) fc.push('quedan imports sin resolver: ' + cSueltos.join(', '));
if (!cjs.includes('window.Chart')) fc.push('no se expone window.Chart, que es como lo llama vi-p.js');
if (fc.length) { console.error('  NO se escribe la grafica:'); fc.forEach(f => console.error('   - ' + f)); process.exit(1); }
fs.writeFileSync('theme/assets/vi-p-chart.js', cjs);
console.log(`  -> theme/assets/vi-p-chart.js  ${(cjs.length/1024).toFixed(0)} KB  (el Chart.js entero que servia el CDN, minificado, son 200 KB)`);
