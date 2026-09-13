/* LA PORTADA, ENTERA, EN LOS CINCO IDIOMAS.
   ------------------------------------------------------------------
   De donde sale esta bateria: la tienda tenia cinco idiomas publicados y la
   portada salia en espanol para los cinco. La copia vivia en
   templates/index.json, que para Shopify es contenido del comerciante y se
   traduce con registros POR TEMA -- y esos registros no sobreviven a subir
   un tema nuevo. Comprobado contra la tienda: translations:[] en los tres
   temas de septiembre. Un visitante en frances veia la interfaz en frances
   y la portada entera en castellano.

   La copia se mudo a los locales del tema, que si viajan dentro del zip. Y
   con ella aparecio una trampa que esta bateria existe para vigilar: media
   portada se pinta dentro de condiciones del tipo "si el ajuste no esta
   vacio". Al vaciar los ajustes -- que es lo que deja mandar al idioma --
   esas guardas escondian el texto. Eran CUARENTA Y NUEVE. Ninguna otra
   comprobacion lo habria visto: el Liquid es valido, el JSON es valido y la
   pagina se pinta sin un error; simplemente le faltan la mitad de las
   frases.

   Asi que aqui se pinta cada seccion de la portada CON los ajustes reales de
   index.json, en los cinco idiomas, y se exige:
     1. Que aparezca cada frase que el idioma tiene escrita.
     2. Que no salga nunca un "Translation missing" por pantalla.
     3. Que ningun idioma pinte menos texto que el espanol, que es la senal
        de que una guarda se ha quedado mirando el ajuste crudo.

   Uso:  node verificadores/idiomas/comprobar.mjs                          */
import fs from 'fs';
import path from 'path';
import { e, prepararFuente, contextoDeSeccion } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const COPIA = JSON.parse(fs.readFileSync(path.join(RAIZ, 'marca/copia-portada.json'), 'utf8'));
const LOC = { es: 'es.json', en: 'en.default.json', fr: 'fr.json', de: 'de.json', ja: 'ja.json' };

const tpl = JSON.parse(fs.readFileSync(`${T}/templates/index.json`, 'utf8').replace(/^\/\*[\s\S]*?\*\//, ''));
const porTipo = {};
for (const s of Object.values(tpl.sections)) porTipo[s.type] = s;

/* COPIA QUE ESTA PRUEBA NO PUEDE VER, Y POR QUE.
   Cada exencion lleva su motivo escrito: una lista de exenciones sin motivo
   acaba siendo el sitio donde se esconden los fallos de verdad. */
const CONDICIONALES = {
  'diario.cab': 'la seccion entera se pinta solo si el blog elegido existe y tiene articulos, y aqui no hay blog',
  'sec.newsletter.success_text': 'se pinta solo despues de enviar el formulario con exito (form.posted_successfully?)'
};
const exento = (g, b, a) => CONDICIONALES[`${g}.${b}.${a}`] || CONDICIONALES[`${g}.${b}`];

let fallos = 0;
const textoPorIdioma = {};

for (const [idioma, archivo] of Object.entries(LOC)) {
  const loc = JSON.parse(fs.readFileSync(`${T}/locales/${archivo}`, 'utf8'));
  const busca = (k) => String(k).split('.').reduce((o, p) => (o && typeof o === 'object' && p in o) ? o[p] : undefined, loc);
  e.registerFilter('t', (v) => { const r = busca(v); return r === undefined ? String(v) : r; });

  let todo = '';
  for (const tipo of Object.keys(porTipo)) {
    const ruta = `${T}/sections/${tipo}.liquid`;
    if (!fs.existsSync(ruta)) continue;
    const src = fs.readFileSync(ruta, 'utf8');
    const { ctx } = contextoDeSeccion(tipo, src);
    ctx.section.settings = { ...ctx.section.settings, ...porTipo[tipo].settings };
    if (porTipo[tipo].blocks) {
      ctx.section.blocks = Object.entries(porTipo[tipo].blocks)
        .map(([id, b]) => ({ id, type: b.type, settings: b.settings, shopify_attributes: '' }));
    }
    e.options.globals = ctx;
    let html;
    try { html = await e.parseAndRender(prepararFuente(src), ctx); }
    catch (err) { console.log(`  FALLA ${idioma}/${tipo}: ${err.message}`); fallos++; continue; }
    todo += ' ' + html.replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<style[\s\S]*?<\/style>/g, ' ')
                      .replace(/<[^>]*>/g, ' ');
  }
  todo = todo.replace(/\s+/g, ' ');
  textoPorIdioma[idioma] = todo;

  if (todo.includes('Translation missing')) { console.log(`  FALLA ${idioma}: sale "Translation missing" en pantalla`); fallos++; }

  /* Cada frase del idioma tiene que aparecer de verdad. */
  const faltan = [];
  for (const g of Object.keys(COPIA)) {
    if (g.startsWith('_')) continue;
    for (const b of Object.keys(COPIA[g])) {
      for (const a of Object.keys(COPIA[g][b])) {
        const frase = String(COPIA[g][b][a][idioma] || '').replace(/<[^>]*>/g, '').trim();
        if (!frase || frase.length < 3) continue;
        if (exento(g, b, a)) continue;
        if (!todo.includes(frase)) faltan.push(`${g}.${b}.${a} = "${frase.slice(0, 46)}"`);
      }
    }
  }
  if (faltan.length) {
    fallos += faltan.length;
    console.log(`  FALLA ${idioma}: ${faltan.length} frase(s) no se pintan`);
    for (const f of faltan.slice(0, 8)) console.log('        ' + f);
  } else {
    console.log(`  OK    ${idioma}: la portada entera, sin huecos`);
  }
}

/* Ningun idioma puede pintar mucho menos texto que el espanol. */
const base = textoPorIdioma.es.length;
for (const [idioma, t] of Object.entries(textoPorIdioma)) {
  if (idioma === 'ja') continue;                 // el japones ocupa la mitad por naturaleza
  if (t.length < base * 0.72) {
    console.log(`  FALLA ${idioma}: pinta ${t.length} caracteres contra ${base} del espanol -- falta texto`);
    fallos++;
  }
}

for (const [k, motivo] of Object.entries(CONDICIONALES)) console.log(`  --    ${k}: sin comprobar, ${motivo}`);

console.log(fallos ? `\n  ${fallos} fallo(s) de idioma en la portada`
                   : '\nLa portada se pinta entera en los cinco idiomas, sin un hueco.');
process.exit(fallos ? 1 : 0);
