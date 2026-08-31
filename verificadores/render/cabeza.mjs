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
const T='theme';
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
 collection:{}, article:{}, blog:{}, cart:{items:[],item_count:0,total_price:0,currency:{iso_code:'CAD'}},
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
console.log('');
console.log(fallos === 0
  ? `Las ${Object.keys(debe).length} etiquetas estan en los ${PAGINAS.length} tipos de pagina, sin duplicados.`
  : `${fallos} tipo(s) de pagina con problemas.`);
process.exit(fallos ? 1 : 0);
