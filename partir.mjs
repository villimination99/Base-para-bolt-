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

   NO TOCA EL MODULO 3D, y esto conviene leerlo entero. Lo escribia, y el dia
   que el mapa paso a editarse en fuente/vi-p-3d.js -- paleta permanente,
   zonas con union suave, encuadre en metros -- una pasada de partir.mjs lo
   sobreescribio con la copia vieja del maestro y se llevo el trabajo por
   delante. Sin ruido: el archivo seguia ahi, seguia compilando, las baterias
   seguian verdes, y el cuerpo simplemente volvia a salir blanco. Peor aun,
   el commit quedo incoherente -- el asset construido llevaba la paleta y su
   fuente no.

   El modulo 3D tiene ahora UN dueno: fuente/vi-p-3d.js. De ahi salen las dos
   vias -- construir-3d.mjs lo empaqueta con three.js para el tema, y
   empaquetar-hub.mjs lo inyecta en el maestro para la version pegable. Este
   script se limita a mirar si el maestro se ha quedado atras y decirlo.

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
/* El modulo 3D NO se escribe: se compara. Su dueno es fuente/vi-p-3d.js.
   Si el maestro se ha quedado atras, se avisa -- y lo pone al dia
   empaquetar-hub.mjs, que es quien lo inyecta en la version pegable. */
const fuente3d = fs.readFileSync('fuente/vi-p-3d.js', 'utf8').trim();
const alDia = mod3d.cuerpo.trim() === fuente3d;

const K = n => (n / 1024).toFixed(0).padStart(4) + ' KB';
console.log('  ' + T + '/assets/vi-p.css   ' + K(css.length));
console.log('  ' + T + '/assets/vi-p.js    ' + K(js.length) + '   (' + (otros.length + 1) + ' scripts en linea unidos)');
console.log('  fuente/vi-p-3d.js        ' + K(fuente3d.length) + '   (no se toca: su dueno es fuente/)');
console.log(alDia
  ? '  el maestro lleva el mismo modulo 3D'
  : '  el maestro lleva un modulo 3D DISTINTO: lo pone al dia empaquetar-hub.mjs');
