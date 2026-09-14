/* El marcado del hub vive en DOS sitios. Que no se separen.
   ------------------------------------------------------------------
   hub/vi-p-completo.html es el original de una sola pieza -- de ahi sale la
   version que se pega en una pagina de Shopify -- y theme/sections/vi-p.liquid
   es la misma cosa como seccion del tema. El estilo y el JavaScript SI salen
   automaticamente del maestro (partir.mjs), pero el MARCADO se mantiene a
   mano en los dos.

   Eso se paga tarde y mal: un titular cambiado en uno y no en el otro, y la
   tienda acaba diciendo dos cosas distintas segun por donde entres, sin que
   nadie se entere hasta que un cliente lo ve. Ya paso al renombrar el hub a
   VI.P y al reescribir el subtitulo del hero.

   Esto compara las frases visibles de los dos y canta las que no cuadran.
   No compara el marcado entero a proposito: la seccion lleva ademas su
   cabecera de Liquid, sus etiquetas asset_url y su schema, y exigir igualdad
   literal seria un verificador que ladra siempre.

   Uso:  node verificadores/render/deriva-hub.mjs                          */
import fs from 'fs';
import path from 'path';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');

/* Del maestro se quitan los <script> y el <style> antes de comparar: lleva
   el motor entero dentro, y ahi hay plantillas de JavaScript que producen
   marcado en tiempo de ejecucion. Sin este recorte, la comparacion cantaba
   una frase que no existe en ninguna pagina -- era un trozo de codigo
   ("' + TX(f.name) + '") pescado por el buscador de clases. */
const maestro = fs.readFileSync(path.join(RAIZ, 'hub/vi-p-completo.html'), 'utf8')
  .replace(/<script[\s\S]*?<\/script>/g, '')
  .replace(/<style[\s\S]*?<\/style>/g, '');
const seccion = fs.readFileSync(path.join(T, 'sections/vi-p.liquid'), 'utf8')
  .replace(/<script[\s\S]*?<\/script>/g, '');

/* Se comparan los textos con peso: los que un cliente lee y los que venden.
   Cada uno se busca por su clase, que es estable, en vez de por su posicion. */
const CLASES = ['hero-tag', 'hero-sub', 'hero-motto', 'section-title', 'section-sub',
                'hc-name', 'hc-desc', 'mm-hint', 'freq-name'];

function textos(fuente, quien) {
  const fuera = new Map();
  for (const cls of CLASES) {
    const re = new RegExp('class="[^"]*\\b' + cls + '\\b[^"]*"[^>]*>([^<]{3,})<', 'g');
    let m;
    while ((m = re.exec(fuente))) {
      const t = m[1].replace(/\s+/g, ' ').trim();
      if (!t || t.includes('{{') || t.includes('{%')) continue;
      const clave = cls + ' :: ' + t;
      fuera.set(clave, (fuera.get(clave) || 0) + 1);
    }
  }
  return fuera;
}

const a = textos(maestro, 'maestro');
const b = textos(seccion, 'seccion');

const soloMaestro = [...a.keys()].filter(k => !b.has(k));
const soloSeccion = [...b.keys()].filter(k => !a.has(k));

let fallos = 0;
console.log('');
console.log(`  frases comparadas: ${a.size} en el maestro, ${b.size} en la seccion`);
if (a.size < 20) { console.error('  se han leido demasiado pocas frases: la comparacion no significa nada'); process.exit(1); }

for (const k of soloMaestro.slice(0, 8)) { fallos++; console.log('  FALLA solo en el MAESTRO:  ' + k.slice(0, 110)); }
for (const k of soloSeccion.slice(0, 8)) { fallos++; console.log('  FALLA solo en la SECCION:  ' + k.slice(0, 110)); }
if (soloMaestro.length > 8 || soloSeccion.length > 8) console.log(`  ... y ${soloMaestro.length + soloSeccion.length - 16} mas`);

/* ================= Y LOS GANCHOS, NO SOLO LAS FRASES =================
   Comparar frases visibles atrapa que un texto se quede viejo en un lado, pero
   no atrapa lo que de verdad rompe el hub: que a la seccion del tema le falte
   un TROZO. Paso: se anadio al maestro el formulario que crea la cuenta en la
   tienda, la seccion se quedo sin el, y esta bateria dijo que decian
   exactamente lo mismo. La pagina VI.P de la tienda no habria tenido registro
   y nadie se habria enterado hasta que alguien fuera a buscarlo.

   Asi que ademas se comparan los GANCHOS: los id= y los atributos data- de los
   que cuelga el JavaScript. Si el maestro tiene un gancho que la seccion no
   tiene, hay codigo que en la tienda no encuentra a que agarrarse.

   Se comparan los ganchos del MARCADO, no los del guion: el maestro es un
   archivo unico que lleva el JavaScript dentro, y ahi hay nombres de ganchos
   que el guion crea al vuelo y que no estan escritos en ningun marcado. Si no
   se quitan los <script> antes de mirar, el maestro parece tener cientos de
   ganchos que la seccion "no tiene" y la comparacion no vale nada.

   El primer intento fue al reves -- perdonar todo gancho que apareciera en
   vi-p.js -- y no valia: el guion tambien nombra los ganchos que CONSULTA, asi
   que perdonaba justo los que hay que vigilar. Probado a mano quitandole uno a
   la seccion: seguia en verde. Quitando los <script> se pone rojo, que es lo
   que tiene que pasar. */
function ganchos(texto) {
  const soloMarcado = texto.replace(/<script[\s\S]*?<\/script>/gi, ' ');
  const g = new Set();
  for (const m of soloMarcado.matchAll(/\bid="([\w-]+)"/g)) g.add('#' + m[1]);
  for (const m of soloMarcado.matchAll(/\b(data-[a-z0-9-]+)[=\s>]/g)) g.add('[' + m[1] + ']');
  return g;
}
const gm = ganchos(maestro), gs = ganchos(seccion);
const faltan = [...gm].filter(k => !gs.has(k));
for (const k of faltan.slice(0, 10)) { fallos++; console.log('  FALLA gancho solo en el MAESTRO: ' + k); }
if (faltan.length) console.log(`  (${faltan.length} gancho(s) que la seccion del tema no tiene: ahi hay codigo sin nada a que agarrarse)`);
else console.log(`  ganchos comparados: ${gm.size} en el maestro, todos presentes en la seccion`);

console.log(fallos
  ? `\n  ${fallos} diferencia(s): el hub no es el mismo segun por donde entres.\n`
  : '\nEl maestro y la seccion del tema dicen exactamente lo mismo.\n');
process.exit(fallos ? 1 : 0);
