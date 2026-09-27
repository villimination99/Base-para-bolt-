/* LA TIENDA ENTERA, EN LOS CINCO IDIOMAS.
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
import { e, prepararFuente, contextoDeSeccion, ctxBase } from '../liquid.mjs';

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
   Ahora entran los tres: portada, cabecera y pie.

   Y ENTRA LA FICHA DE PRODUCTO, que es la pagina que de verdad importa: es
   donde aterriza cualquier anuncio. Estaba entera en castellano y nadie lo
   miraba -- los siete textos (los tres sellos de confianza, el desplegable
   de envios con su contenido, "Como se usa" y la etiqueta de recomendados)
   vivian escritos a mano dentro de templates/product.json, que es contenido
   del comerciante y no se traduce. Un frances veia la ficha en frances con
   "Envio rapido 3-7 dias" debajo del boton de comprar. */
const tpl = leerJson(`${T}/templates/index.json`);
const porTipo = {};
for (const s of Object.values(tpl.sections)) porTipo[s.type] = s;
/* TODAS LAS PLANTILLAS, no una muestra. Cada una que se queda fuera es una
   pagina entera que nadie mira en cinco idiomas -- la ficha de producto
   estuvo asi, sin traducir y en verde, hasta septiembre. */
for (const plantilla of ['product', 'collection', 'list-collections', 'blog', 'article',
                         'page', 'page.contact', 'cart', 'search', '404']) {
  const t = leerJson(`${T}/templates/${plantilla}.json`);
  for (const s of Object.values(t.sections)) porTipo[s.type] = s;
}
for (const grupo of ['header-group', 'footer-group']) {
  const g = leerJson(`${T}/sections/${grupo}.json`);
  for (const s of Object.values(g.sections)) porTipo[s.type] = s;
}

/* COPIA QUE ESTA PRUEBA NO PUEDE VER, Y POR QUE.
   Cada exencion lleva su motivo escrito: una lista de exenciones sin motivo
   acaba siendo el sitio donde se esconden los fallos de verdad. */
/* TRES SUPERFICIES QUE NO SON SECCIONES, Y QUE NADIE MIRABA.
   Esta bateria recorre las secciones de las plantillas, y por ahi no pasan ni
   la intro, ni la pagina de contraseña, ni el cajon del carrito: son un
   fragmento y una plantilla suelta. Cuando el eslogan, las frases de la intro
   y el titulo de la venta cruzada se mudaron a los idiomas, sus cuatro claves
   quedaron sin nadie que las viera -- y exentarlas habria sido justo eso,
   dejar de mirarlas. Asi que se pintan aqui, con el contexto que hace falta
   para que cada una entre en su rama:
     - la intro y la contraseña se pintan solas;
     - el cajon necesita un carrito CON articulos, y ademas que el primero
       pertenezca a una coleccion con hermanos, que es la unica puerta por la
       que se pinta el titulo de la venta cruzada. */
const SUELTAS = [
  { ruta: 'snippets/splash-intro.liquid', ctx: () => ctxBase },
  { ruta: 'templates/password.liquid', ctx: () => ctxBase },
  { ruta: 'snippets/cart-drawer-items.liquid', ctx: () => {
      const p = ctxBase.product;
      const linea = { key: 'k1', quantity: 1, title: p.title, url: p.url, image: null,
        variant: { title: 'Único' }, properties: {}, product: p,
        line_level_discount_allocations: [], original_line_price: p.price, final_line_price: p.price };
      return Object.assign({}, ctxBase, {
        cart: { item_count: 1, items: [linea], total_price: p.price,
                original_total_price: p.price, cart_level_discount_applications: [],
                currency: ctxBase.cart.currency, note: '' } });
    } },
];

const CONDICIONALES = {
  'diario.cab': 'la seccion entera se pinta solo si el blog elegido existe y tiene articulos, y aqui no hay blog',
  'sec.newsletter.success_text': 'se pinta solo despues de enviar el formulario con exito (form.posted_successfully?)',
  'sec.header.collections_trigger': 'no es texto que se pinte: es la lista de nombres con la que la cabecera reconoce el menu de colecciones',
  'sec.announcement-bar.countdown_prefix': 'se pinta solo si la barra tiene una cuenta atras configurada, y aqui esta vacia',
  'sec.announcement-bar.countdown_expired': 'se pinta solo cuando esa cuenta atras ha terminado',
  'producto.c2': 'el desplegable "Como se usa" viene apagado (visible:false) y sin contenido: un desplegable vacio es peor que no tenerlo'
};
const exento = (g, b, a) => CONDICIONALES[`${g}.${b}.${a}`] || CONDICIONALES[`${g}.${b}`];

/* CASTELLANO QUE SE CUELA EN UNA PAGINA EN OTRO IDIOMA.
   La bateria sabia exigir que apareciera cada frase traducida, pero no sabia
   ver la frase EN CASTELLANO al lado. Y se cuela por una puerta concreta:
   Shopify aplica el "default" del esquema a todo ajuste que la plantilla no
   guarda, asi que un default escrito en castellano sale tal cual en las
   cinco lenguas. La barra de anuncios estuvo prometiendo "Envio gratis en
   pedidos +$50" -- con el envio gratis apagado -- en frances, aleman y
   japones, y ninguna comprobacion chistaba.
   Se recogen todos los defaults de texto de los esquemas que se pintan y se
   exige que ninguno asome fuera del castellano. */
const DEFAULTS_ES = new Map();
for (const tipo of Object.keys(porTipo)) {
  const ruta = `${T}/sections/${tipo}.liquid`;
  if (!fs.existsSync(ruta)) continue;
  const m = fs.readFileSync(ruta, 'utf8').match(/\{%\s*schema\s*%\}([\s\S]*?)\{%\s*endschema\s*%\}/);
  if (!m) continue;
  let esquema; try { esquema = JSON.parse(m[1]); } catch { continue; }
  const anda = (o) => {
    if (Array.isArray(o)) return o.forEach(anda);
    if (o && typeof o === 'object') {
      if (typeof o.default === 'string') {
        const t = o.default.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
        /* Solo frases: una palabra suelta puede ser una marca, un color o un
           nombre propio que se escribe igual en los cinco idiomas. */
        if (t.length >= 10 && t.includes(' ') && /[a-záéíóúñ]/i.test(t)) DEFAULTS_ES.set(t, tipo);
      }
      Object.values(o).forEach(anda);
    }
  };
  anda(esquema);
}

let fallos = 0;
const textoPorIdioma = {};

for (const [idioma, archivo] of Object.entries(LOC)) {
  const loc = JSON.parse(fs.readFileSync(`${T}/locales/${archivo}`, 'utf8'));
  const busca = (k) => String(k).split('.').reduce((o, p) => (o && typeof o === 'object' && p in o) ? o[p] : undefined, loc);
  /* OCTAVA DIVERGENCIA: Shopify no devuelve la clave cuando falla, devuelve
     "Translation missing: <idioma>.<clave>". Esta bateria devolvia la clave,
     asi que su propia comprobacion de "Translation missing" no podia saltar
     nunca -- ni siquiera con {{ x | default: y | t }} delante, que le mete al
     filtro el texto del comerciante ya resuelto. El cliente lo vio en una
     captura en frances: "Translation missing: fr.Vetements". */
  e.registerFilter('t', (v) => {
    const r = busca(v);
    if (r === undefined) return `Translation missing: ${idioma}.${v}`;
    if (r !== null && typeof r === 'object') return `Translation missing: ${idioma}.${v}`;
    return /_html$/.test(String(v)) ? r : String(r)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  });

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
  for (const suelta of SUELTAS) {
    const ruta = `${T}/${suelta.ruta}`;
    if (!fs.existsSync(ruta)) { console.log(`  FALLA ${idioma}: falta ${suelta.ruta}`); fallos++; continue; }
    const ctx = suelta.ctx();
    e.options.globals = ctx;
    let html;
    try { html = await e.parseAndRender(prepararFuente(fs.readFileSync(ruta, 'utf8')), ctx); }
    catch (err) { console.log(`  FALLA ${idioma}/${suelta.ruta}: ${err.message}`); fallos++; continue; }
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
  /* AL COMPARAR se deshacen las cinco entidades: el filtro t escapa igual
     que Shopify, asi que un apostrofo frances sale "&#39;" y la frase del
     diccionario nunca coincidiria. El guardian de etiquetas visibles de
     abajo sigue mirando el texto SIN deshacer, que es lo que ve el cliente. */
  const todoLlano = todo
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'").replace(/&amp;/g, '&');

  if (idioma !== 'es') {
    const colados = [...DEFAULTS_ES].filter(([frase]) => todoLlano.includes(frase));
    if (colados.length) {
      fallos += colados.length;
      console.log(`  FALLA ${idioma}: se lee castellano en una pagina en ${idioma}`);
      for (const [frase, tipo] of colados) {
        console.log(`        ${tipo}: "${frase.slice(0, 58)}" -- es un "default" del esquema, y Shopify lo aplica en los cinco idiomas`);
      }
    }
  }

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
        /* [n] ES UN COMODIN, no texto. El aviso de stock bajo se guarda como
           "Solo quedan [n]" y se pinta con el numero puesto, asi que pedir la
           frase literal da un rojo sobre texto que SI se ve. Se compara por
           los lados del comodin en vez de exentar la frase: exentarla seria
           dejar de mirarla. */
        const perdidos = trozos.filter(x =>
          x.includes('[n]') ? !x.split('[n]').every(t => t.trim().length < 3 || todoLlano.includes(t.trim()))
                            : !todoLlano.includes(x));
        if (perdidos.length) faltan.push(`${g}.${b}.${a} = "${perdidos[0].slice(0, 46)}"`);
      }
    }
  }
  if (faltan.length) {
    fallos += faltan.length;
    console.log(`  FALLA ${idioma}: ${faltan.length} frase(s) no se pintan`);
    for (const f of faltan.slice(0, 8)) console.log('        ' + f);
  } else {
    console.log(`  OK    ${idioma}: las once plantillas, sin huecos`);
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

console.log(fallos ? `\n  ${fallos} fallo(s) de idioma en la tienda`
                   : '\nLas once plantillas se pintan enteras en los cinco idiomas, sin un hueco.');
process.exit(fallos ? 1 : 0);
