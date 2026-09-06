/* Empaqueta el tema para subirlo a Shopify.
   ------------------------------------------------------------------
   El repositorio conserva el CSS comentado (esos comentarios son la memoria
   de por que cada regla esta como esta), pero el zip va sin ellos: medidos,
   cuestan 7 KB de los 36,8 KB que pesa el CSS comprimido, un 19 %.

   Los comentarios se quitan con un recorrido caracter a caracter, no con una
   expresion regular: un /* dentro de una cadena o de un url() no abre un
   comentario, y una regex ingenua se lo comeria y romperia la hoja.

   Uso:  node empaquetar.mjs [4.28.0]                                       */
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { createRequire } from 'module';

const RAIZ = path.dirname(new URL(import.meta.url).pathname);
const TEMA = path.join(RAIZ, 'theme');

const version = process.argv[2] ||
  JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_schema.json'), 'utf8'))[0].theme_version;
const SALIDA = path.join(RAIZ, `villumination-3d-theme-${version}.zip`);

/* Quita comentarios de CSS respetando cadenas y url(). */
function limpiarCss(css) {
  let out = '';
  let i = 0;
  let comilla = null;   // ' o " cuando estamos dentro de una cadena
  while (i < css.length) {
    const c = css[i], d = css[i + 1];
    if (comilla) {
      out += c;
      if (c === '\\') { out += css[i + 1] || ''; i += 2; continue; }
      if (c === comilla) comilla = null;
      i++;
      continue;
    }
    if (c === '"' || c === "'") { comilla = c; out += c; i++; continue; }
    if (c === '/' && d === '*') {
      const fin = css.indexOf('*/', i + 2);
      i = fin === -1 ? css.length : fin + 2;
      continue;
    }
    out += c;
    i++;
  }
  // Lineas en blanco y sangria que quedan tras quitar los comentarios
  return out.replace(/\n[ \t]+/g, '\n').replace(/\n{2,}/g, '\n').trim() + '\n';
}

/* Comprobacion de seguridad. La primera version comparaba el CSS limpio con
   el ORIGINAL y siempre fallaba, porque los comentarios contienen llaves y
   selectores de ejemplo: se comparaban peras con manzanas.
   Lo correcto es contrastar el recorrido caracter a caracter con un metodo
   INDEPENDIENTE (una regex ingenua). Si dos formas distintas de quitar
   comentarios dan exactamente los mismos selectores, la limpieza es fiable.
   Ademas se exige que las llaves cuadren en el resultado. */
function selectores(css) {
  return (css.match(/[^{}]+(?=\{)/g) || [])
    .map(x => x.replace(/\s+/g, ' ').trim())
    .filter(Boolean);
}

function comprobar(original, limpio) {
  const regexLimpio = original.replace(/\/\*[\s\S]*?\*\//g, '');
  const a = selectores(limpio), b = selectores(regexLimpio);
  return {
    llavesCuadran: limpio.split('{').length === limpio.split('}').length,
    mismosSelectores: a.length === b.length && a.every((x, i) => x === b[i]),
    cuantos: a.length,
  };
}

const TMP = path.join(RAIZ, '.paquete');
fs.rmSync(TMP, { recursive: true, force: true });
fs.cpSync(TEMA, TMP, { recursive: true });

const rutaCss = path.join(TMP, 'assets/villumination.css');
const original = fs.readFileSync(rutaCss, 'utf8');
const limpio = limpiarCss(original);
const chequeo = comprobar(original, limpio);

if (!chequeo.llavesCuadran || !chequeo.mismosSelectores) {
  console.error('  La limpieza del CSS cambiaria las reglas. Se aborta y se empaqueta sin limpiar.');
  console.error('  ' + JSON.stringify(chequeo));
} else {
  fs.writeFileSync(rutaCss, limpio);
  const antes = original.length, despues = limpio.length;
  console.log(`  CSS: ${antes} -> ${despues} B  (${(100 * (antes - despues) / antes).toFixed(1)} % menos)`);
  console.log(`  ${chequeo.cuantos} selectores intactos, llaves cuadradas`);
}

/* ---------------------------------------------------------------------
   JavaScript minificado, con la misma logica que el CSS: el repositorio se
   queda los comentarios -- son la memoria de por que cada cosa esta como
   esta -- y el zip va sin ellos.

   Medido sobre 4.46.0: los diez archivos pasan de 524 a 357 KB, y por la
   red (que es lo unico que nota el visitante, porque Shopify sirve
   comprimido) de 167 a 119 KB gzip, un 29 % menos. El que mas gana es
   intro.js: de 20 a 6 KB, y ese carga SIN defer porque la intro es lo
   primero que se ve, asi que sus catorce kilobytes menos salen del camino
   critico del primer pintado.

   Se salta los que ya vienen minificados de construir-3d.mjs.

   ES2017 y no mas moderno: es el suelo que exige la bateria de
   plataformas, y estos archivos se cargan como scripts clasicos, asi que
   cualquier motor los parsea enteros. La unica excepcion es vi-p-3d.js,
   que va con type="module" -- y por eso mismo se salta esta pasada.

   COMO SE COMPRUEBA. No sirve comparar el codigo antes y despues: un
   minificador reordena, une cadenas y convierte claves entrecomilladas en
   identificadores, asi que cualquier invariante sintactica da falsos
   rojos (lo probe: 'Accept' deja de ser una cadena y pasa a ser una clave,
   y la comparacion se pone roja por algo que no cambia nada). Lo que si
   sirve es medir el comportamiento, y por eso mas abajo se pasan las
   baterias de navegador SOBRE ESTA CARPETA ya minificada, antes de
   escribir el zip. Si el tema minificado no se comporta igual, no hay zip.
   --------------------------------------------------------------------- */
const req = createRequire(import.meta.url);
let esbuild = null;
try { esbuild = req('esbuild'); } catch { }

const YA_MINIFICADOS = ['vi-p-3d.js', 'vi-p-chart.js'];
if (!esbuild) {
  console.log('  (sin esbuild: el JavaScript va sin minificar. npm i --no-save esbuild@0.28.2)');
} else {
  let antes = 0, despues = 0, n = 0;
  for (const f of fs.readdirSync(path.join(TMP, 'assets')).filter(f => f.endsWith('.js'))) {
    if (YA_MINIFICADOS.includes(f)) continue;
    const ruta = path.join(TMP, 'assets', f);
    const src = fs.readFileSync(ruta, 'utf8');
    const r = esbuild.transformSync(src, { minify: true, target: 'es2017', legalComments: 'none' });
    /* Si la salida no parsea al suelo del tema, se deja el original: mas
       vale un archivo grande que un archivo que no arranca. */
    try { req('acorn').Parser.parse(r.code, { ecmaVersion: 2017, sourceType: 'script' }); }
    catch (e) { console.error(`  ${f}: el minificado no parsea a ES2017 (${e.message}); se deja el original`); continue; }
    fs.writeFileSync(ruta, r.code);
    antes += src.length; despues += r.code.length; n++;
  }
  console.log(`  JS: ${antes} -> ${despues} B en ${n} archivos  (${(100 * (antes - despues) / antes).toFixed(1)} % menos)`);
}

/* ---- las baterias, contra el tema minificado ----

   Solo las que miden COMPORTAMIENTO. La distincion no es cosmetica y la
   aprendio esta misma compuerta en su primer intento: check.mjs se puso
   roja en "Secuencia de marca" porque busca la llamada a pintar( en el
   codigo, y el minificador habia renombrado esa funcion a Y. El
   comportamiento estaba intacto -- la rama de movimiento reducido sigue
   pintando su fotograma y poniendo is-live, comprobado -- pero una
   comprobacion que busca un NOMBRE no puede opinar sobre un build donde
   los nombres son deliberadamente otros.

   check.mjs y las de render/ leen el codigo fuente y su intencion
   (comentarios, identificadores, esquemas): su sitio es el tema del
   repositorio, y ahi se pasan aparte. Aqui van las que abren un navegador
   y miran lo que ocurre, mas plataformas, que comprueba que el minificado
   sigue parseando al suelo de ES2017. */
const BATERIAS = [
  ['verificadores/vi-p/comprobar.mjs', 'VI.P entero en un navegador'],
  ['verificadores/teclado/comprobar.mjs', 'paneles con teclado'],
  ['verificadores/lienzos/comprobar.mjs', 'los lienzos animados pintan'],
  ['verificadores/plataformas/comprobar.mjs', 'sintaxis en motores viejos']
];
if (process.env.SIN_BATERIAS) {
  console.log('  (SIN_BATERIAS: no se comprueba el tema minificado)');
} else {
  for (const [script, que] of BATERIAS) {
    try {
      execSync(`node "${path.join(RAIZ, script)}"`, { cwd: RAIZ, env: { ...process.env, TEMA: TMP }, stdio: 'pipe' });
      console.log(`  OK   ${que}`);
    } catch (e) {
      console.error(`  FALLA ${que} sobre el tema minificado. NO se escribe el zip.`);
      console.error(String(e.stdout || '').split('\n').filter(l => /FALLA|rojo|mal|✗/.test(l)).slice(0, 8).join('\n'));
      process.exit(1);
    }
  }
}

fs.rmSync(SALIDA, { force: true });
execSync(`cd "${TMP}" && zip -rq "${SALIDA}" . -x '*.DS_Store' '__MACOSX/*'`);
fs.rmSync(TMP, { recursive: true, force: true });

const kb = fs.statSync(SALIDA).size / 1024;
console.log(`  Listo: ${path.basename(SALIDA)}  ${kb.toFixed(0)} KB`);
