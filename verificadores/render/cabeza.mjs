/* Renderiza el <head> COMPLETO del layout con todos los codigos de
   verificacion rellenos y comprueba que salen los once. Es la respuesta a
   "¿no falta el codigo de Google? ¿y el de Meta?" sin tener que fiarse de que
   alguien mire el archivo: se pinta y se cuenta lo que sale.

   Uso:
     npm install liquidjs --no-save
     node verificadores/render/cabeza.mjs

   CUIDADO con un detalle que ya me engano una vez: en liquidjs {% render %}
   aisla el ambito por completo, mientras que en Shopify settings, request,
   localization y product son objetos GLOBALES y si llegan dentro del snippet.
   Sin declararlos como globals, este script decia que faltaban seis etiquetas
   que en realidad estaban. Por eso va e.options.globals = ctx. */
/* Renderiza el <head> COMPLETO del layout con todos los codigos de
   verificacion rellenos, para comprobar que salen todos juntos y ninguno
   se pisa a otro. Es la respuesta a "¿no falta nada?". */
import { Liquid } from 'liquidjs';
const T = process.env.TEMA || 'theme';
const e = new Liquid({ root:[T+'/snippets',T], extname:'.liquid', strictFilters:false, strictVariables:false });
const F={escape:v=>String(v==null?'':v),json:v=>JSON.stringify(v===undefined?null:v),
 image_url:v=>(typeof v==='string'?v:(v&&v.src)||'//cdn.shopify.com/x.png'),asset_url:v=>'//cdn.shopify.com/'+v,
 stylesheet_tag:v=>`<link rel="stylesheet" href="${v}">`,preload_tag:v=>`<link rel="preload" href="${v}" as="font" type="font/woff2" crossorigin>`,
 strip_html:v=>String(v||'').replace(/<[^>]*>/g,''),truncate:(v,n)=>String(v||'').slice(0,n),
 date:()=>'2026-08-23',default:(v,d)=>(v===undefined||v===null||v===''?d:v),t:v=>String(v),
 money:v=>(Number(v||0)/100).toFixed(2),handle:v=>String(v||'').toLowerCase(),
 remove_first:(v,x)=>String(v||'').replace(x,''),append:(v,x)=>String(v||'')+String(x||''),
 divided_by:(v,n)=>Number(v||0)/n,times:(v,n)=>Number(v||0)*n,round:v=>Math.round(v),
 font_face:()=>'',font_url:()=>'',split:(v,s)=>String(v||'').split(s),first:v=>v&&v[0]};
for (const [k,f] of Object.entries(F)) e.registerFilter(k,f);
e.registerTag('style',{parse(tk,rem){while(rem.length){const t=rem.shift(); if(t.name==='endstyle')return;}},render(){return '';}});
e.registerTag('schema',{parse(tk,rem){while(rem.length){const t=rem.shift(); if(t.name==='endschema')return;}},render(){return '';}});
const img={src:'//cdn.shopify.com/logo.png',width:1600,height:400,aspect_ratio:4,alt:'VILLUMINATION'};
const ctxBase={ settings:{
   seo_google_verification:'ztSaLwg9MkIRvDsQj1HvTPsFg-kxZIdRXYlS-6lNFQE',
   seo_bing_verification:'BING-CODIGO', seo_yandex_verification:'YANDEX-CODIGO',
   seo_pinterest_verification:'PINTEREST-CODIGO', seo_facebook_domain:'META-CODIGO',
   seo_contact_email:'hola@villuminations.com', seo_contact_phone:'+1 514 555 0134',
   logo:img, favicon:img, share_image:'', use_display_font:true,
   social_youtube:'https://www.youtube.com/@villumination99', social_instagram:'https://www.instagram.com/villumination99',
   social_tiktok:'', social_x:'', drawer_width:400 },
 shop:{name:'VIllumination',url:'https://villuminations.com',description:'Fitness sin limites.',money_format:'{{amount}}'},
 canonical_url:'https://villuminations.com/products/proteina', page_title:'Proteína | VILLUMINATIONS',
 page_description:'Proteína de suero aislada.',
 localization:{available_languages:[{iso_code:'es',primary:true,root_url:'/'},{iso_code:'en',root_url:'/en'},
   {iso_code:'fr',root_url:'/fr'},{iso_code:'de',root_url:'/de'},{iso_code:'ja',root_url:'/ja'}]},
 product:{title:'Proteína',id:1,url:'/p',handle:'proteina',description:'d',vendor:'V',type:'T',price:12990,
   available:true,featured_media:{preview_image:img},media:[{preview_image:img}],images:[img],featured_image:img,
   selected_or_first_available_variant:{id:1,price:12990,available:true,sku:'X',barcode:'1'},
   variants:[{id:1,price:12990,available:true,sku:'X',barcode:'1'}],metafields:{},tags:[],collections:[]},
 /* Con la coleccion, la entrada y la pagina VACIAS, la segunda vuelta de este
    verificador no probaba nada: el tema no tenia de donde sacar una
    description propia y caia en la de la tienda, que es exactamente lo que
    esa vuelta busca impedir. Rojo del banco de pruebas, no del tema. Llevan
    contenido de verdad, con etiquetas y saltos de linea dentro, para que
    ademas se compruebe que el tema los limpia antes de meterlos en el
    atributo. */
 collection:{title:'Suplementos',handle:'suplementos',
   description:'<p>Proteina, creatina, preentreno y verdes.</p>\n<p>Cada ficha dice que lleva.</p>',
   products_count:10,image:img,all_products_count:10},
 article:{title:'Cuanta proteina hace falta al dia',handle:'cuanta-proteina',
   excerpt_or_content:'<p>0,8 g por kilo es el minimo oficial,\nno el objetivo de quien entrena.</p>',
   content:'<p>0,8 g por kilo es el minimo oficial.</p>',image:img,
   published_at:'2026-08-15',author:'Villumination',tags:[]},
 blog:{title:'Diario',handle:'diario',url:'/blogs/diario',articles:[]},
 page:{title:'Como se hace lo que vendemos',handle:'como-se-hace',
   content:'<p>De donde salen las cifras y por que el programa se niega\na publicar un libro incompleto.</p>'},
 cart:{items:[],item_count:0,total_price:0,currency:{iso_code:'CAD'}},
 routes:new Proxy({},{get:()=>'/'}), template:{name:'product'}, content_for_header:'<!-- shopify -->' };
const layout = (await import('fs')).readFileSync(T+'/layout/theme.liquid','utf8');
const head = layout.slice(0, layout.indexOf('</head>'));

const debe = {'google':'google-site-verification','bing':'msvalidate.01','yandex':'yandex-verification',
  'pinterest':'p:domain_verify','meta':'facebook-domain-verification','canonical':'rel="canonical"',
  'robots':'name="robots"','og:title':'og:title','og:image':'og:image','twitter':'twitter:card','hreflang':'hreflang',
  'og:image:width':'og:image:width','og:type':'og:type','og:url':'og:url','og:site_name':'og:site_name'};

/* Se recorren los NUEVE tipos de pagina, no solo la ficha de producto. Una
   etiqueta de verificacion que solo salga en algunas paginas puede hacer que
   Google o Bing den la propiedad por no verificada, segun por donde entre su
   rastreador. Y una etiqueta duplicada tambien da problemas, asi que se
   cuenta cuantas veces aparece cada una. */
const PAGINAS = [
  {tipo:'index',            ruta:'/'},
  {tipo:'product',          ruta:'/products/proteina'},
  {tipo:'collection',       ruta:'/collections/suplementos'},
  {tipo:'article',          ruta:'/blogs/diario/entrada'},
  {tipo:'blog',             ruta:'/blogs/diario'},
  {tipo:'page',             ruta:'/pages/como-se-hace'},
  {tipo:'search',           ruta:'/search'},
  {tipo:'404',              ruta:'/404'},
  {tipo:'cart',             ruta:'/cart'},
];

let fallos = 0;
console.log('');
for (const PAGINA of PAGINAS) {
  // Copia superficial, NO JSON.parse(JSON.stringify(...)): esa via se come
  // todo lo que no sea JSON puro (funciones, undefined) y dejaba el contexto
  // a medias, con lo que faltaban seis etiquetas en las nueve paginas. El
  // verificador acusaba al tema de un fallo que era mio.
  const ctxP = Object.assign({}, ctxBase, {
    request: { page_type: PAGINA.tipo, path: PAGINA.ruta,
               locale: { iso_code: 'es', root_url: '/' }, design_mode: false },
  });
  // En liquidjs, {% render %} aisla el ambito: el snippet NO ve el contexto
  // de quien lo llama, aunque en Shopify los objetos globales si llegan. Sin
  // esta linea el verificador dice que faltan seis etiquetas que si estan.
  // Lo advierte la cabecera de este archivo y aun asi la borre al reescribir
  // el final; el propio verificador lo caza.
  e.options.globals = ctxP;
  let out;
  try { out = await e.parseAndRender(head, ctxP); }
  catch (err) { console.log(`FALLA  ${PAGINA.tipo}: la cabeza no renderiza (${err.message})`); fallos++; continue; }
  const faltan = [], repes = [];
  for (const [nombre, aguja] of Object.entries(debe)) {
    const n = out.split(aguja).length - 1;
    if (n === 0) faltan.push(nombre);
    // hreflang y og aparecen varias veces a proposito; el resto, una sola
    else if (n > 1 && !['hreflang','og:title','og:image','twitter'].includes(nombre)) repes.push(`${nombre} x${n}`);
  }
  const ok = !faltan.length && !repes.length;
  if (!ok) fallos++;
  console.log(`${ok ? ' OK  ' : 'FALLA'}  ${PAGINA.tipo.padEnd(11)} ${Object.keys(debe).length - faltan.length}/${Object.keys(debe).length} etiquetas` +
    (faltan.length ? `  FALTAN: ${faltan.join(', ')}` : '') +
    (repes.length ? `  DUPLICADAS: ${repes.join(', ')}` : ''));
}

/* ---- SEGUNDA VUELTA: LA DESCRIPCION CUANDO NADIE LA HA ESCRITO ----
   La primera vuelta comprueba que las etiquetas ESTAN. Esta comprueba que la
   description dice algo util cuando el comerciante no ha rellenado la pestana
   de SEO, que es lo que pasa siempre con la prisa de subir un producto nuevo.

   Antes, sin description propia, TODAS las paginas repetian la descripcion de
   la tienda. Para Google eso no es "una tienda coherente": son treinta
   paginas con el mismo fragmento, y cuando dos resultados dicen lo mismo se
   queda con uno y descarta el resto. Ahora el respaldo baja en escalera y usa
   el contenido de la propia pagina. Aqui se exige justo eso: que con la
   description vacia, el producto hable del producto y la coleccion de la
   coleccion, y que no acaben todas diciendo lo mismo. */
console.log('\n--- Sin descripcion SEO escrita, cada pagina dice lo suyo ---');
const DELA_TIENDA = ctxBase.shop.description;
const CONTENIDO = { product: 1, collection: 1, article: 1, page: 1, blog: 1 };
const vistas = new Map();
for (const PAGINA of PAGINAS) {
  const ctxP = Object.assign({}, ctxBase, {
    page_description: '',
    request: { page_type: PAGINA.tipo, path: PAGINA.ruta,
               locale: { iso_code: 'es', root_url: '/' }, design_mode: false },
  });
  e.options.globals = ctxP;
  let out;
  try { out = await e.parseAndRender(head, ctxP); }
  catch (err) { console.log(`FALLA  ${PAGINA.tipo}: no renderiza (${err.message})`); fallos++; continue; }
  const m = out.match(/<meta name="description" content="([^"]*)"/);
  const texto = m ? m[1].trim() : '';
  const hay = texto.length > 0;
  if (!hay) fallos++;
  if (CONTENIDO[PAGINA.tipo]) {
    /* Que NO sea la de la tienda: eso significa que ha bajado a buscar el
       contenido de la pagina, que es lo que la distingue. */
    const propia = hay && texto !== DELA_TIENDA;
    if (!propia) fallos++;
    console.log(`${propia ? ' OK  ' : 'FALLA'}  ${PAGINA.tipo.padEnd(11)} usa su propio contenido: "${texto.slice(0, 46)}"`);
    /* Y que no haya palabras pegadas. Quitar las etiquetas de golpe une la
       ultima palabra de un parrafo con la primera del siguiente
       -- "verdes.Cada ficha" -- y eso es lo que se lee en el resultado de
       Google. Se busca un signo de puntuacion seguido de letra sin espacio. */
    if (/[\r\n]/.test(texto)) { fallos++; console.log(`FALLA  ${PAGINA.tipo}: la description lleva saltos de linea dentro del atributo`); }
    const pegadas = texto.match(/[.,;:!?][A-Za-zÁÉÍÓÚÑáéíóúñ]/);
    if (pegadas) { fallos++; console.log(`FALLA  ${PAGINA.tipo}: palabras pegadas al quitar las etiquetas ("${pegadas[0]}")`); }
    if (vistas.has(texto)) { fallos++; console.log(`FALLA  ${PAGINA.tipo}: repite la description de ${vistas.get(texto)}`); }
    vistas.set(texto, PAGINA.tipo);
  } else {
    /* En las paginas sin contenido propio -- carrito, buscador, 404 -- la de
       la tienda es lo correcto, y ademas van con noindex. Lo unico que no
       puede pasar es que se queden SIN description. */
    console.log(`${hay ? ' OK  ' : 'FALLA'}  ${PAGINA.tipo.padEnd(11)} recurre a la de la tienda, que es lo suyo`);
  }
}

console.log('');
console.log(fallos === 0
  ? `Las ${Object.keys(debe).length} etiquetas estan en los ${PAGINAS.length} tipos de pagina, sin duplicados, y ninguna pagina se queda sin description propia.`
  : `${fallos} problema(s) en las cabeceras.`);
process.exit(fallos ? 1 : 0);
