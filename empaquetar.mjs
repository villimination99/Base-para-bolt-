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

import { limpiarCss, comprobar } from './herramientas/adelgazar.mjs';

const TMP = path.join(RAIZ, '.paquete');
fs.rmSync(TMP, { recursive: true, force: true });
fs.cpSync(TEMA, TMP, { recursive: true });

/* TODAS las hojas, no solo la principal. vi-p.css llevaba sus 55 comentarios
   al cliente porque esta linea nombraba un archivo suelto en vez de recorrer
   la carpeta: el dia que el hub estreno hoja propia, se quedo fuera sin que
   nadie lo notara. Recorrer el directorio no puede olvidarse de un archivo
   nuevo. */
let cssAntes = 0, cssDespues = 0, cssSelectores = 0, cssArchivos = 0;
for (const nombre of fs.readdirSync(path.join(TMP, 'assets')).filter(f => f.endsWith('.css')).sort()) {
  const ruta = path.join(TMP, 'assets', nombre);
  const original = fs.readFileSync(ruta, 'utf8');
  const limpio = limpiarCss(original);
  const chequeo = comprobar(original, limpio);
  if (!chequeo.llavesCuadran || !chequeo.mismosSelectores) {
    console.error(`  ${nombre}: la limpieza cambiaria las reglas. Se deja tal cual.`);
    console.error('  ' + JSON.stringify(chequeo));
    continue;
  }
  fs.writeFileSync(ruta, limpio);
  cssAntes += original.length; cssDespues += limpio.length;
  cssSelectores += chequeo.cuantos; cssArchivos++;
}
console.log(`  CSS: ${cssAntes} -> ${cssDespues} B en ${cssArchivos} hojas  (${(100 * (cssAntes - cssDespues) / cssAntes).toFixed(1)} % menos)`);
console.log(`  ${cssSelectores} selectores intactos, llaves cuadradas`);

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
    /* legalComments 'inline' y no 'none': el zip que se sube a Shopify es una
       COPIA DISTRIBUIDA, y three.js y Chart.js son MIT, mientras que el shader
       del hero es una adaptacion de Paper Shaders (Apache-2.0). Las tres
       licencias exigen que el aviso de copyright viaje con el codigo. Con
       'none' se borraba, y lo que se subia a la tienda no cumplia. Cuestan
       unos cientos de bytes. */
    const r = esbuild.transformSync(src, { minify: true, target: 'es2017', legalComments: 'inline' });
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
  /* El linter OFICIAL de Shopify, el primero de todos: si el tema tiene algo
     que Shopify considera roto, no hay que seguir midiendo fotogramas. Estuvo
     fuera de la compuerta sin que nadie se diera cuenta porque su lanzador no
     estaba versionado; la primera vez que entro encontro un error de verdad
     -- el guion de la intro detenia el analisis de la tienda entera. */
  ['verificadores/shopify/comprobar.mjs', 'el linter oficial de Shopify'],
  /* Y los limites publicados de Shopify -- secciones, bloques, peso del zip --
     que no avisan mientras vas holgado y avisan el dia que subes. */
  ['verificadores/limites/comprobar.mjs', 'las reglas y los limites de Shopify'],
  ['verificadores/vi-p/comprobar.mjs', 'VI.P entero en un navegador'],
  ['verificadores/teclado/comprobar.mjs', 'paneles con teclado'],
  ['verificadores/lienzos/comprobar.mjs', 'los lienzos animados pintan'],
  ['verificadores/plataformas/comprobar.mjs', 'sintaxis en motores viejos'],
  ['verificadores/acceso/comprobar.mjs', 'accesibilidad WCAG 2.1 AA'],
  ['verificadores/lcp/comprobar.mjs', 'la portada se pinta a tiempo (LCP)'],
  /* Y las DOCE plantillas, no solo la portada. Una tienda no se entra por la
     portada: se entra por la ficha de producto que salio en Google o por la
     coleccion que alguien compartio. Esta bateria las monta todas y mide en
     cada una el LCP, el CLS -- cuanto salta la pagina, que es de los tres
     numeros con los que Google ordena y que aqui no se medía en ningun sitio
     -- los errores de JavaScript y los desbordes laterales. */
  ['verificadores/paginas/comprobar.mjs', 'las doce plantillas cargan bien (LCP y CLS)'],
  /* La intro entro en la compuerta el dia que una captura del cliente mostro
     el nombre de la tienda, la esfera y la frase pintados unos encima de
     otros en un iPhone. Ninguna de las otras baterias lo vio, y no por
     descuido: todas miraban el lienzo, y la colision estaba en el HTML de
     encima. Ahora esta mira lo que mira un ojo -- rectangulos que se ven a la
     vez y no pueden ocupar el mismo sitio -- en nueve ventanas, incluida la
     del movil TUMBADO, donde el boton de entrar se salia de la pantalla.
     Tarda sus minutos. Los vale: es lo PRIMERO que ve cada visitante. */
  ['verificadores/intro/comprobar.mjs', 'la intro no amontona nada y siempre deja entrar'],
  /* Y el rotulo de las colecciones, que salio de que las fotos de la tienda
     llevan el nombre escrito dentro y el tema le pintaba el suyo encima. */
  ['verificadores/rotulos/comprobar.mjs', 'las colecciones no pintan dos textos en el mismo sitio'],
  /* Y los tres estados que nadie mira nunca: Windows en alto contraste, el
     papel y las superficies que pinta el propio navegador. La tienda entera
     se apoya en titulos recortados sobre un degradado, y en alto contraste
     el sistema borra ese degradado y el titulo se queda transparente sobre
     nada: invisible. En papel, lo mismo en blanco sobre blanco. Aqui se
     emula cada modo y se lee el color con el que el texto sale de verdad. */
  ['verificadores/superficies/comprobar.mjs', 'alto contraste, papel y superficies del navegador'],
  /* Y el hero, que es el unico sitio donde el texto va sobre un fondo que se
     MUEVE. Ninguna otra bateria puede: axe lee colores computados y sobre un
     lienzo WebGL no hay ninguno que leer, asi que daba el hero por bueno sin
     mirarlo. Un fondo animado no tiene un contraste, tiene un peor caso a lo
     largo del tiempo; esta fotografia diez fotogramas en dos anchos y se
     queda con el pixel mas claro de cada caja de texto.
     El dia que entro encontro que la flecha de bajar del marco pulsante,
     publicada desde siempre, estaba a 1,40:1 en un movil: cian sobre el neon
     cian del propio marco. */
  ['verificadores/hero/comprobar.mjs', 'el texto del hero sobre un fondo que se mueve']
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
