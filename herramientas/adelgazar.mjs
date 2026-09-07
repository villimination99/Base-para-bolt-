/* ADELGAZAR SIN CAMBIAR NADA: el CSS y su comprobacion de seguridad.
   ------------------------------------------------------------------
   Esto vivia dentro de empaquetar.mjs y solo lo usaba el zip. Ahora tambien
   lo necesita empaquetar-hub.mjs, porque el codigo que se pega en una pagina
   de Shopify TIENE que caber: el cuerpo de una pagina admite mucho, pero no
   todo, y los comentarios -- que en el repositorio valen su peso en oro --
   ahi solo ocupan sitio. Un solo dueno para la funcion evita que las dos
   herramientas adelgacen de maneras distintas.

   Los comentarios se quitan con un recorrido caracter a caracter, no con una
   expresion regular: un /* dentro de una cadena o de un url() no abre un
   comentario, y una regex ingenua se lo comeria y romperia la hoja.        */
import { createRequire } from 'module';
const req = createRequire(import.meta.url);
let esbuild = null;
try { esbuild = req('esbuild'); } catch { }
export const hayEsbuild = () => !!esbuild;

/* Quita comentarios de CSS respetando cadenas y url(). */
export function limpiarCss(css) {
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
export function selectores(css) {
  return (css.match(/[^{}]+(?=\{)/g) || [])
    .map(x => x.replace(/\s+/g, ' ').trim())
    .filter(Boolean);
}

export function comprobar(original, limpio) {
  const regexLimpio = original.replace(/\/\*[\s\S]*?\*\//g, '');
  const a = selectores(limpio), b = selectores(regexLimpio);
  return {
    llavesCuadran: limpio.split('{').length === limpio.split('}').length,
    mismosSelectores: a.length === b.length && a.every((x, i) => x === b[i]),
    cuantos: a.length,
  };
}

/* ================= ADELGAZAR PARA QUE QUEPA =================
   El estilo pierde los comentarios con el mismo recorrido caracter a caracter
   que usa el zip del tema (un /* dentro de una cadena o de un url() no abre
   un comentario, y una regex ingenua se lo comeria), y cada guion en linea
   pasa por esbuild.

   Tres detalles que costarian una tarde si no estuvieran escritos:

   - El mapa de importacion NO es JavaScript. Es JSON dentro de una etiqueta
     script, y pasarlo por un minificador de JS lo destroza. Se compacta con
     JSON.parse/stringify, que ademas valida de paso.
   - El modulo del mapa 3D va con type="module" y usa import: se minifica
     como modulo y a es2020. Los demas son guiones clasicos y van a es2017,
     que es el suelo que exige la bateria de plataformas.
   - Si algo no vuelve a parsear despues de adelgazar, se deja el original.
     Mas vale un archivo grande que un archivo que no arranca. */
export function adelgazarFragmento(html, cuenta = {}) {
  let out = html.replace(/<style([^>]*)>([\s\S]*?)<\/style>/g,
    (m, attrs, css) => {
      const limpio = limpiarCss(css);
      const chequeo = comprobar(css, limpio);
      if (!chequeo.llavesCuadran || !chequeo.mismosSelectores) {
        console.error('  el estilo no se adelgaza: la limpieza cambiaria las reglas');
        return m;
      }
      cuenta.css = [css.length, limpio.length, chequeo.cuantos];
      return `<style${attrs}>${limpio}</style>`;
    });

  out = out.replace(/<script([^>]*)>([\s\S]*?)<\/script>/g, (m, attrs, js) => {
    if (/\bsrc=/.test(attrs) || !js.trim()) return m;
    const tipo = (attrs.match(/type\s*=\s*["']([^"']+)["']/) || [])[1] || '';

    if (tipo === 'importmap' || tipo === 'application/ld+json') {
      try {
        const compacto = JSON.stringify(JSON.parse(js));
        cuenta.jsAntes = (cuenta.jsAntes || 0) + js.length; cuenta.jsDespues = (cuenta.jsDespues || 0) + compacto.length; cuenta.n = (cuenta.n || 0) + 1;
        return `<script${attrs}>${compacto}</script>`;
      } catch (e) {
        console.error(`  el bloque ${tipo} no es JSON valido: se deja tal cual`);
        return m;
      }
    }

    const esModulo = tipo === 'module';
    try {
      const r = esbuild.transformSync(js, {
        minify: true,
        target: esModulo ? 'es2020' : 'es2017',
        format: esModulo ? 'esm' : undefined,
        legalComments: 'inline',   // las licencias de terceros viajan con el codigo
      });
      req('acorn').Parser.parse(r.code, {
        ecmaVersion: esModulo ? 2020 : 2017,
        sourceType: esModulo ? 'module' : 'script',
      });
      cuenta.jsAntes = (cuenta.jsAntes || 0) + js.length; cuenta.jsDespues = (cuenta.jsDespues || 0) + r.code.length; cuenta.n = (cuenta.n || 0) + 1;
      return `<script${attrs}>${r.code}</script>`;
    } catch (e) {
      console.error(`  un guion no sobrevive al adelgazado (${String(e.message).slice(0, 70)}): se deja el original`);
      return m;
    }
  });
  /* Y el marcado. Se le quitan los comentarios de HTML -- que viajan al
     navegador de cada visitante sin que nadie los lea nunca -- y la sangria
     del principio de cada linea. Ni una cosa ni la otra cambian como se ve
     la pagina: HTML colapsa los espacios en blanco por definicion, y aqui no
     hay ni un <pre> ni un <textarea> ni una regla white-space:pre donde eso
     dejaria de ser cierto (comprobado antes de escribir esto). El estilo y
     los guiones ya son de una sola linea a estas alturas, asi que esta pasada
     solo toca el marcado. */
  out = out.replace(/<!--(?!\s*=========)[\s\S]*?-->/g, '')
           .replace(/\n[ \t]+/g, '\n')
           .replace(/\n{2,}/g, '\n');
  return out;
}
