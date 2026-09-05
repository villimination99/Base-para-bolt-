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

fs.rmSync(SALIDA, { force: true });
execSync(`cd "${TMP}" && zip -rq "${SALIDA}" . -x '*.DS_Store' '__MACOSX/*'`);
fs.rmSync(TMP, { recursive: true, force: true });

const kb = fs.statSync(SALIDA).size / 1024;
console.log(`  Listo: ${path.basename(SALIDA)}  ${kb.toFixed(0)} KB`);
