/* Del hub completo a los dos archivos que se pegan / se abren.  node empaquetar-hub.mjs

   Genera:
     hub/villuminations-vi-p.html          el fragmento para pegar DENTRO de
                                           una pagina de Shopify: sin doctype,
                                           sin <html>, sin <head> y sin <body>,
                                           porque la tienda ya los pone y
                                           repetirlos rompe la pagina.
     hub/villuminations-vi-p-autonomo.html el mismo contenido con su documento
                                           alrededor, para abrirlo en el
                                           navegador o guardarlo.

   Esta via NO es la recomendada para la tienda: el cuerpo de una pagina de
   Shopify no se cachea, asi que estos 474 KB se vuelven a bajar en cada
   visita. Subiendo el tema, las mismas piezas van a assets/ y viajan por el
   CDN de Shopify con cache. Se mantiene porque es la unica forma de tener el
   hub sin tocar el tema, y porque el cliente decidio tenerla a mano.
*/
import fs from 'fs';

const h = fs.readFileSync('hub/vi-p-completo.html', 'utf8');
const iS = h.indexOf('  <style>'), fS = h.indexOf('</style>') + 8;
const estilo = h.slice(iS, fS);
const iB = h.indexOf('<body>') + 6;
const fB = h.lastIndexOf('</body>');
if (iS < 0 || iB < 6 || fB < 0) throw new Error('el maestro no tiene la forma esperada');
const cuerpo = h.slice(iB, fB).trim();

const frag = `<!-- ===================================================================
     VILLUMINATIONS · VI.P
     Pensado para pegarse DENTRO de una pagina de Shopify (Contenido ->
     Paginas -> "<>" Mostrar HTML). Empieza directamente por el estilo y el
     marcado: NO trae las etiquetas de documento (doctype, la raiz, la
     cabecera ni el cuerpo), porque la tienda ya las pone y repetirlas rompe
     la pagina.
     Todo el CSS cuelga de #vill-hub para no tocar el tema.
     =================================================================== -->
${estilo}
${cuerpo}
`;

/* Lo que no puede pasar nunca, porque se ve igual de bien roto que entero */
const fallos = [];
if (frag.length < 400000) fallos.push(`son ${frag.length} car: falta medio hub`);
if (/<!DOCTYPE|<html[ >]|<\/body>/i.test(frag)) fallos.push('lleva etiquetas de documento, que rompen la pagina de Shopify');
if (!frag.includes('id="vill-hub"')) fallos.push('falta el contenedor #vill-hub');
if (!frag.includes('muscle-canvas')) fallos.push('falta el lienzo del mapa 3D');
if ((frag.match(/<h1/gi) || []).length > 1) fallos.push('mas de un <h1>: parte la senal de SEO de la pagina');
if (fallos.length) { console.error('  NO se escribe nada:'); fallos.forEach(f => console.error('   - ' + f)); process.exit(1); }

fs.writeFileSync('hub/villuminations-vi-p.html', frag);
console.log('  hub/villuminations-vi-p.html          ' + (frag.length / 1024).toFixed(0) + ' KB   (para pegar en la pagina)');

const suelta = `<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VILLUMINATIONS – VI.P</title>
</head><body style="margin:0;background:#0A0A0A">
${frag}
</body></html>`;
fs.writeFileSync('hub/villuminations-vi-p-autonomo.html', suelta);
console.log('  hub/villuminations-vi-p-autonomo.html ' + (suelta.length / 1024).toFixed(0) + ' KB   (se abre en el navegador)');
