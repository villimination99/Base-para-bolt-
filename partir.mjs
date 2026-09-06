/* Parte el hub completo en las piezas que sube el tema.  node partir.mjs

   COMO ENCAJA ESTO
   ----------------
   hub/vi-p-completo.html es el ORIGINAL: una pagina entera, con su estilo,
   su marcado y sus scripts en un solo archivo. Es lo que se edita cuando se
   toca el hub, y es tambien lo que se pega tal cual en una pagina de Shopify
   (de ahi sale hub/villuminations-vi-p.html, via empaquetar-hub.mjs).

   Este script lo abre y escribe:
     theme/assets/vi-p.css   el estilo
     theme/assets/vi-p.js    los scripts en linea, unidos
     fuente/vi-p-3d.js       el modulo del mapa muscular

   Ojo con el ultimo: escribe en fuente/, NO en theme/assets/. El asset que
   sube el tema lo produce despues construir-3d.mjs, que le mete three.js
   dentro. Si esto escribiera directamente en assets/ se cargaria el paquete
   y el mapa dejaria de funcionar en cuanto alguien volviera a partir.

   Vivio un tiempo fuera del repositorio, en un directorio temporal, y eso
   significaba que cualquier arreglo hecho a mano en theme/assets/vi-p.js
   se perdia en silencio la siguiente vez que alguien partia el hub. Por eso
   esta aqui.
*/
import fs from 'fs';

const MAESTRO = 'hub/vi-p-completo.html';
const T = 'theme';

const h = fs.readFileSync(MAESTRO, 'utf8');

const css = h.slice(h.indexOf('  <style>') + 9, h.indexOf('</style>')).trim();

const trozos = [];
const re = /<script([^>]*)>([\s\S]*?)<\/script>/g;
let m;
while ((m = re.exec(h))) trozos.push({ attr: m[1].trim(), cuerpo: m[2] });

/* Se identifican POR CONTENIDO, no por el orden en que aparecen.
   Antes se cogian por indice -- enLinea[0], enLinea[1] -- y al anadir un
   script nuevo al banner los indices se corrieron: el archivo principal
   salio de 2 KB en vez de 319, o sea el hub entero sin su motor. Un fallo
   que no da error en ningun sitio: simplemente la pagina no hace nada. */
const enLinea = trozos.filter(t => !t.attr);
const mod3d = trozos.find(t => /type="module"/.test(t.attr));
const principal = enLinea.slice().sort((a, b) => b.cuerpo.length - a.cuerpo.length)[0];
const otros = enLinea.filter(t => t !== principal);

if (!principal || principal.cuerpo.length < 200000) throw new Error('el script principal no parece el correcto: ' + (principal ? principal.cuerpo.length : 0) + ' car');
if (!mod3d) throw new Error('no se encuentra el modulo 3D');
if (css.length < 40000) throw new Error('el estilo son ' + css.length + ' car: no puede ser');

const js = otros.map(t => t.cuerpo.trim()).join('\n\n') + '\n\n' + principal.cuerpo.trim() + '\n';
fs.writeFileSync(T + '/assets/vi-p.css', css + '\n');
fs.writeFileSync(T + '/assets/vi-p.js', js);
fs.writeFileSync('fuente/vi-p-3d.js', mod3d.cuerpo.trim() + '\n');

const K = n => (n / 1024).toFixed(0).padStart(4) + ' KB';
console.log('  ' + T + '/assets/vi-p.css   ' + K(css.length));
console.log('  ' + T + '/assets/vi-p.js    ' + K(js.length) + '   (' + (otros.length + 1) + ' scripts en linea unidos)');
console.log('  fuente/vi-p-3d.js        ' + K(mod3d.cuerpo.length) + '   <- ahora toca: node construir-3d.mjs');
