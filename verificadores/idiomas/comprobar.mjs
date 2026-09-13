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

const leerJson = (ruta) => JSON.parse(fs.readFileSync(ruta, 'utf8').replace(/^\/\*[\s\S]*?\*\//, ''));

/* LA PORTADA NO ES TODO LO QUE VE EL VISITANTE. El pie y la cabecera no
   viven en templates/index.json sino en sections/*-group.json, y por eso se
   quedaron fuera cuando la copia se mudo a los idiomas: la bateria daba
   verde y el pie seguia diciendo "Tienda fitness para atletas que no se
   conforman con lo ordinario" en una pagina en frances. Lo vio el cliente.
   Ahora entran los tres: portada, cabecera y pie. */
const tpl = leerJson(`${T}/templates/index.json`);
const porTipo = {};
for (const s of Object.values(tpl.sections)) porTipo[s.type] = s;
for (const grupo of ['header-group', 'footer-group']) {
  const g = leerJson(`${T}/sections/${grupo}.json`);
  for (const s of Object.values(g.sections)) porTipo[s.type] = s;
}

/* COPIA QUE ESTA PRUEBA NO PUEDE VER, Y POR QUE.
   Cada exencion lleva su motivo escrito: una lista de exenciones sin motivo
   acaba siendo el sitio donde se esconden los fallos de verdad. */
const CONDICIONALES = {
  'diario.cab': 'la seccion entera se pinta solo si el blog elegido existe y tiene articulos, y aqui no hay blog',
  'sec.newsletter.success_text': 'se pinta solo despues de enviar el formulario con exito (form.posted_successfully?)',
  'sec.header.collections_trigger': 'no es texto que se pinte: es la lista de nombres con la que la cabecera reconoce el menu de colecciones',
  'sec.announcement-bar.countdown_prefix': 'se pinta solo si la barra tiene una cuenta atras configurada, y aqui esta vacia',
  'sec.announcement-bar.countdown_expired': 'se pinta solo cuando esa cuenta atras ha terminado'
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
    /* LAS LISTAS QUE VIAJAN EN UN <script> TAMBIEN CUENTAN. El pie pinta
       una sola frase y mete las demas en un JSON que el guion va rotando:
       estan entregadas y traducidas, pero no en el DOM a la vez. Tirar
       todos los <script> daba por perdidas cuatro de las cinco. Se rescata
       el contenido de los que llevan datos y se descarta el resto. */
    const datos = [...html.matchAll(/<script[^>]*type="application\/json"[^>]*>([\s\S]*?)<\/script>/g)]
      .map(m => m[1]).join(' ');
    todo += ' ' + datos.replace(/\\u([\da-f]{4})/gi, (_, c) => String.fromCharCode(parseInt(c, 16)));
    todo += ' ' + html.replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<style[\s\S]*?<\/style>/g, ' ')
                      .replace(/<[^>]*>/g, ' ');
  }
  todo = todo.replace(/\s+/g, ' ');
  textoPorIdioma[idioma] = todo;

  if (todo.includes('Translation missing')) { console.log(`  FALLA ${idioma}: sale "Translation missing" en pantalla`); fallos++; }

  /* ETIQUETAS ESCAPADAS A LA VISTA. Shopify escapa las traducciones por
     defecto -- solo se libra una clave terminada en _html -- asi que un
     texto traducido con HTML dentro sale por pantalla como "<p>Tous
     incluent une garantie satisfaction.</p>", tal cual, con las etiquetas
     leyendose. Paso en el FAQ y lo vio el cliente, no esta bateria: mi
     filtro t no escapaba y por eso daba verde. Ahora escapa igual que
     Shopify, y esto vigila el resultado. */
  const escapadas = todo.match(/&lt;\/?(p|br|strong|em|ul|li|span|a)\b[^&]{0,20}&gt;/g);
  if (escapadas) {
    fallos++;
    console.log(`  FALLA ${idioma}: se leen etiquetas HTML en pantalla (${[...new Set(escapadas)].slice(0, 3).join(' ')}) -- a esa clave le falta el sufijo _html`);
  }

  /* Cada frase del idioma tiene que aparecer de verdad. */
  const faltan = [];
  for (const g of Object.keys(COPIA)) {
    if (g.startsWith('_')) continue;
    for (const b of Object.keys(COPIA[g])) {
      for (const a of Object.keys(COPIA[g][b])) {
        if (exento(g, b, a)) continue;
        /* SE COMPARA POR TROZOS, no de una pieza. Dos casos lo obligan:
             - Las claves _html llevan una lista, y cada <li> sale en su
               elemento: quitar las etiquetas de golpe pega las palabras.
             - Las frases del pie van separadas por saltos de linea y el
               tema las reparte en elementos distintos.
           Comparar el bloque entero daba cinco falsos rojos sobre texto que
           SI se pinta. Se parte por lineas y por etiquetas, se normalizan
           los espacios en los dos lados, y se exige cada trozo. */
        const bruto = String(COPIA[g][b][a][idioma] || '');
        const trozos = bruto.split(/\n|<\/?[a-z][^>]*>/i)
          .map(x => x.replace(/\s+/g, ' ').trim())
          .filter(x => x.length >= 3);
        if (!trozos.length) continue;
        const perdidos = trozos.filter(x => !todo.includes(x));
        if (perdidos.length) faltan.push(`${g}.${b}.${a} = "${perdidos[0].slice(0, 46)}"`);
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
