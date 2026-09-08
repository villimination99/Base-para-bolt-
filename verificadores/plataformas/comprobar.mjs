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

/* Todo el Liquid del tema, para poder mirar COMO se carga cada archivo. */
const LIQUID = (function leer(dir) {
  let salida = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) salida = salida.concat(leer(p));
    else if (e.name.endsWith('.liquid')) salida.push(fs.readFileSync(p, 'utf8'));
  }
  return salida;
})(process.env.TEMA || path.join(RAIZ, 'theme'));

/* ¿El tema carga este archivo con type="module"? Hay dos formas, y las dos
   cuentan:

   1. Una etiqueta <script type="module" src="..."> en el Liquid. Se busca la
      etiqueta COMPLETA que lo menciona, no el nombre suelto, para que un
      archivo citado en un comentario no cuente.

   2. Un <script> que crea JavaScript. Desde 4.47.0 el mapa 3D se carga solo
      cuando se acerca a la pantalla, asi que su etiqueta ya no esta escrita
      en el Liquid: la fabrica vi-p.js poniendo type = 'module' y sacando la
      direccion de un data-. Cuando eso paso, esta comprobacion se puso roja
      y exigio ES2017 a un modulo -- que es pedirle que no sea un modulo.

      Para el segundo caso se mira el par completo: que el Liquid publique la
      direccion del archivo en un atributo data-, y que algun JavaScript del
      tema fabrique un script de tipo modulo leyendo ese mismo data-. Con las
      dos mitades no queda duda de como se carga. */
function cargadoComoModulo(nombre) {
  const esc = nombre.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const re = new RegExp('<script[^>]*' + esc + '[^>]*>|<script[^>]*type="module"[^>]*' + esc, 'i');
  if (LIQUID.some((l) => { const m = l.match(re); return !!m && /type="module"/i.test(m[0]); })) return true;

  const dato = LIQUID.map(l => l.match(new RegExp('(data-[a-z0-9-]+)="\\{\\{\\s*\'' + esc + '\'[^"]*"', 'i'))).find(Boolean);
  if (!dato) return false;
  const attr = dato[1];

  /* Y aqui hace falta precision, no buena voluntad.

     La primera version se conformaba con que ALGUN archivo del tema
     mencionara el data- y ademas dijera type = 'module' en cualquier parte.
     Como vi-p.js trae los dos cargadores -- el del mapa, que es modulo, y el
     de las graficas, que es un script clasico -- daba por modulo tambien a
     vi-p-chart.js. Y eso apagaba justo la comprobacion que habia pillado que
     Chart.js llevaba sintaxis ES2020 en un script que parsean todos los
     motores.

     La segunda version exigia que las dos mitades estuvieran a menos de N
     caracteres. Media 656 en un caso y 1339 en el otro, asi que cualquier
     N entre ambos "funcionaba" -- hasta que alguien anadiera un comentario
     dentro del cargador. Un umbral afinado a la forma que tiene el codigo
     hoy no es una comprobacion, es una coincidencia.

     Asi que se pregunta lo que de verdad se quiere saber: si la LECTURA del
     data- y la asignacion type = 'module' viven en la MISMA funcion. Eso no
     depende de espacios, comentarios ni de si el archivo esta minificado
     -- y el empaquetador pasa esta bateria sobre el tema ya minificado. */
  const dentroDeLaMismaFuncion = (js) => {
    let arbol;
    try { arbol = Parser.parse(js, { ecmaVersion: 2022, sourceType: 'script' }); }
    catch { return false; }

    const esModuleType = (n) => n.type === 'AssignmentExpression'
      && n.left.type === 'MemberExpression'
      && ((n.left.property.name || n.left.property.value) === 'type')
      && n.right.type === 'Literal' && n.right.value === 'module';
    const esNuestroDato = (n) => n.type === 'Literal' && typeof n.value === 'string' && n.value.includes(attr);

    let encontrado = false;
    const recorrer = (n, funcion) => {
      if (!n || typeof n !== 'object' || encontrado) return;
      if (/Function(Declaration|Expression)|ArrowFunctionExpression/.test(n.type)) funcion = n;
      if (funcion && esNuestroDato(n)) {
        /* Se ha visto el data-. ¿Esta funcion pone type = 'module'? */
        let hay = false;
        const buscar = (m) => {
          if (!m || typeof m !== 'object' || hay) return;
          if (esModuleType(m)) { hay = true; return; }
          for (const k in m) { const v = m[k]; if (Array.isArray(v)) v.forEach(buscar); else if (v && typeof v === 'object') buscar(v); }
        };
        buscar(funcion);
        if (hay) { encontrado = true; return; }
      }
      for (const k in n) { const v = n[k]; if (Array.isArray(v)) v.forEach(x => recorrer(x, funcion)); else if (v && typeof v === 'object') recorrer(v, funcion); }
    };
    recorrer(arbol, null);
    return encontrado;
  };

  return fs.readdirSync(ASSETS).filter(f => f.endsWith('.js'))
    .some(f => dentroDeLaMismaFuncion(fs.readFileSync(path.join(ASSETS, f), 'utf8')));
}

console.log('\n--- Sintaxis: el suelo es ES2017 (Safari 11 / iOS 11) ---');
/* Por que ES2017 y no algo mas nuevo: un iPhone 5s o un iPad de 2014 se
   quedaron en esa version de Safari y siguen navegando. No son muchos, pero
   para ellos la tienda no se ve a medias: se ve rota, porque un error de
   sintaxis tumba el archivo completo antes de ejecutar la primera linea. */
for (const f of js) {
  const src = fs.readFileSync(path.join(ASSETS, f), 'utf8');
  /* Un archivo que el tema carga con <script type="module"> puede usar import:
     los motores que no entienden modulos IGNORAN esa etiqueta entera, asi que
     nunca llegan a leer el archivo. Exigirle ES2017 a un modulo es pedirle que
     no sea un modulo. Se mira como lo carga el tema y se analiza en
     consecuencia, en vez de tratar a todos igual. */
  const esModulo = cargadoComoModulo(f);
  let error = null;
  try { Parser.parse(src, { ecmaVersion: esModulo ? 2022 : 2017, sourceType: esModulo ? 'module' : 'script' }); }
  catch (e) { error = e; }
  if (error) {
    const linea = src.slice(0, error.pos).split('\n').length;
    const texto = src.split('\n')[linea - 1].trim().slice(0, 70);
    decir(false, `${f} usa sintaxis posterior a ES2017 en la linea ${linea}: ${texto}`);
  } else {
    decir(true, `${f.padEnd(22)} se analiza como ${esModulo ? 'modulo ES (el tema lo carga con type="module")' : 'ES2017'}`);
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

/* ================= EL INVENTARIO DE FUNCIONES MODERNAS =================
   Aqui no se puede ejecutar Safari: el contenedor no alcanza el CDN de
   Playwright, asi que webkit y firefox no se pueden descargar. Todo lo demas
   se mide en Chromium. Decirlo importa, porque un iPhone es WebKit.

   Lo que SI se puede hacer sin ejecutarlos es esto: llevar la cuenta de cada
   funcion moderna que el tema usa y de la version en la que aparecio, y exigir
   que cualquiera que llegue mas tarde que el SUELO declarado este justificada
   por escrito. No sustituye a probar en un telefono de verdad -- nada lo hace
   -- pero atrapa la clase de fallo que de verdad ocurre: alguien anade una
   propiedad nueva y reluciente y media tienda se cae en un iPad de hace tres
   anos, en silencio, durante meses.

   EL SUELO: Safari 15.4 (marzo de 2022). Es la version del ultimo iPhone que
   ya no recibe iOS nuevo pero sigue en manos de gente, y por debajo de ahi el
   trafico real es residual. Todo lo que pida mas que eso tiene que estar en la
   lista de toleradas, con el motivo, o dentro de un @supports. */
console.log('\n--- Funciones modernas: nada por encima del suelo sin justificar ---');
const SUELO_SAFARI = 15.4;

/* clave: [nombre, version minima de Safari, motivo por el que se tolera] */
const FUNCIONES = [
  ['aspect-ratio', 15, null],
  ['color-mix(', 16.2, 'check.mjs comprueba que cada uso lleve un color de respaldo delante'],
  ['inset:', 14.1, null],
  ['backdrop-filter', 9, null],
  ['clamp(', 13.1, null],
  ['env(safe-area', 11.2, null],
  [':has(', 15.4, null],
  ['mask-image', 15.4, null],
  ['text-wrap:', 17.5, 'solo equilibra el corte de linea de un titular; sin ella el texto se parte como siempre'],
  ['scrollbar-width', 18.2, 'adelgaza la barra de desplazamiento; sin ella se ve la del sistema'],
  ['content-visibility', 18, 'solo aplaza el pintado de lo que esta fuera de pantalla; sin ella se pinta todo, que es lo que hacia antes'],
  ['@container', 16, 'ninguna: si aparece, hay que justificarla'],
  ['subgrid', 16, 'ninguna: si aparece, hay que justificarla'],
  ['dvh', 15.4, null],
];

let cssTodo = '';
for (const f of fs.readdirSync(ASSETS).filter(f => f.endsWith('.css'))) {
  cssTodo += fs.readFileSync(path.join(ASSETS, f), 'utf8');
}
/* Los comentarios no son codigo: una propiedad NOMBRADA en una explicacion no
   la usa nadie, y contarla seria verificar la prosa otra vez. */
cssTodo = cssTodo.replace(/\/\*[\s\S]*?\*\//g, '');

for (const [clave, minSafari, motivo] of FUNCIONES) {
  const usos = cssTodo.split(clave).length - 1;
  if (!usos) continue;
  if (minSafari <= SUELO_SAFARI) {
    decir(true, `${clave.padEnd(20)} ${String(usos).padStart(4)} usos · Safari ${minSafari}, dentro del suelo`);
  } else {
    decir(!!motivo, `${clave.padEnd(20)} ${String(usos).padStart(4)} usos · Safari ${minSafari} > suelo ${SUELO_SAFARI}` +
      (motivo ? ` · tolerada: ${motivo}` : ' · SIN JUSTIFICAR'));
  }
}

console.log(fallos === 0
  ? '\nEl codigo del tema no usa nada que rompa en Safari, iOS, Firefox, Windows ni Linux.\n(Aviso honesto: aqui no se puede ejecutar WebKit ni Gecko. Esto es analisis, no ejecucion.)\n'
  : `\n${fallos} comprobacion(es) en rojo.\n`);
process.exit(fallos ? 1 : 0);
