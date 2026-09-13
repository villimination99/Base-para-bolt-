/* Renderiza el Liquid DE VERDAD con un motor real y comprueba que cada bloque
   de datos estructurados sale como JSON valido, en TODOS los tipos de pagina.

   Los otros verificadores leen el codigo; este lo ejecuta. Es la diferencia
   entre "el archivo parece correcto" y "Google recibe JSON que puede parsear".
   Una coma de mas en una rama que solo se pinta en las fichas de blog no la ve
   ningun analisis estatico, y rompe el bloque entero para el rastreador.

   Uso:
     npm install liquidjs --no-save
     node verificadores/render/jsonld.mjs

   Los datos de prueba imitan la tienda real: cinco idiomas publicados, un
   producto con valoraciones, una coleccion, un articulo. Si Shopify anade
   filtros nuevos hay que registrarlos abajo; con strictFilters en false, uno
   que falte devuelve el valor sin tocar en vez de romper la prueba. */
const T = process.env.TEMA || 'theme';
import { Liquid } from 'liquidjs';
import fs from 'fs';

const engine = new Liquid({ root: [T + '/snippets', T], extname: '.liquid', strictFilters: false, strictVariables: false });
// Filtros de Shopify que liquidjs no trae
const money = v => (Number(v||0)/100).toFixed(2).replace('.', ',') + ' $';
engine.registerFilter('money', money);
engine.registerFilter('money_without_currency', v => (Number(v||0)/100).toFixed(2));
engine.registerFilter('image_url', (v) => (typeof v === 'string' ? v : (v && v.src) || '//cdn.shopify.com/x.png'));
engine.registerFilter('asset_url', v => '//cdn.shopify.com/assets/' + v);
engine.registerFilter('handle', v => String(v||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''));
engine.registerFilter('handleize', v => String(v||'').toLowerCase().replace(/[^a-z0-9]+/g,'-'));
engine.registerFilter('t', v => String(v));
engine.registerFilter('json', v => JSON.stringify(v === undefined ? null : v));
engine.registerFilter('escape', v => String(v==null?'':v).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'));
engine.registerFilter('strip_html', v => String(v==null?'':v).replace(/<[^>]*>/g,''));
engine.registerFilter('date', v => '2026-08-22');
engine.registerFilter('default', (v,d) => (v===undefined||v===null||v==='' ? d : v));
engine.registerTag('style', { parse(t,r){this.tpls=[];const s=this;let tok;while((tok=r.shift())){if(tok.name==='endstyle')return;s.tpls.push(tok);}}, render(){ return ''; } });
engine.registerTag('schema', { parse(t,r){while(r.length){const k=r.shift();if(k.name==='endschema')return;}}, render(){return '';} });

const img = { src:'//cdn.shopify.com/logo.png', width:1600, height:400, alt:'VILLUMINATION', aspect_ratio:4 };
const ctx = {
  settings: {
    seo_google_verification:'ztSaLwg9MkIRvDsQj1HvTPsFg-kxZIdRXYlS-6lNFQE',
    logo: img, favicon: img, share_image: '',
    social_youtube:'https://www.youtube.com/@villumination99',
    social_instagram:'https://www.instagram.com/villumination99',
    social_tiktok:'', social_x:'',
    seo_contact_email:'hola@villuminations.com', seo_contact_phone:'+1 514 555 0134',
    seo_ship_country:'CA', seo_return_days:30, seo_return_free:true,
    cart_free_shipping_threshold:'', brand_display_name:'VILLUMINATION',
  },
  shop: { name:'VIllumination', url:'https://villuminations.com',
    description:'Villuminations te guía hacia un fitness sin límites.',
    money_format:'{{amount}} $', email:'villumination@outlook.com' },
  canonical_url:'https://villuminations.com/products/proteina',
  page_title:'Proteína aislada | VILLUMINATIONS', page_description:'Proteína de suero aislada.',
  request: { page_type:'product', path:'/products/proteina', locale:{iso_code:'es'}, origin:'https://villuminations.com' },
  localization: { available_languages:[{iso_code:'es',primary:true,root_url:'/'},{iso_code:'en',root_url:'/en'},{iso_code:'fr',root_url:'/fr'},{iso_code:'de',root_url:'/de'},{iso_code:'ja',root_url:'/ja'}] },
  routes: { root_url:'/', search_url:'/search', all_products_collection_url:'/collections/all' },
  product: { title:'Proteína de suero aislada', id:1, url:'/products/proteina', handle:'proteina',
    description:'Proteína de suero aislada sabor chocolate.', vendor:'VILLUMINATION', type:'Suplementos',
    featured_media:{preview_image:img}, media:[{preview_image:img}], images:[img], featured_image:img,
    price:12990, price_min:12990, price_max:15990, available:true, selected_or_first_available_variant:{id:9,sku:'VP-001',barcode:'1234567890123',price:12990,available:true,title:'2 kg'},
    variants:[{id:9,sku:'VP-001',barcode:'1234567890123',price:12990,available:true,title:'2 kg'}],
    // Se renderiza dos veces, con price_varies en false y en true: son dos
    // ramas distintas del JSON-LD (Offer y AggregateOffer) y la segunda no se
    // ejercitaba nunca, que es justo donde es mas facil colar una coma de mas.
    price_varies: false, type:'Suplemento',
    metafields:{reviews:{rating:{value:{rating:4.8,scale_max:5}},rating_count:{value:128}}},
    tags:[], collections:[{title:'Suplementos',url:'/collections/suplementos'}] },
  collection: { title:'Suplementos', url:'/collections/suplementos', description:'Proteína y creatina.', products:[], all_products_count:10, image:img },
  article: { title:'Qué suplementos tienen evidencia', url:'/blogs/diario/x', content:'<p>Texto</p>', excerpt:'Resumen',
    published_at:'2026-08-01', updated_at:'2026-08-02', author:'Villumination', image:img, tags:[], comments_count:0 },
  blog: { title:'Diario', url:'/blogs/diario', articles:[] },
  page: { title:'Contacto', url:'/pages/contact', content:'' },
  cart: { total_price:0, item_count:0, items:[] },
  template: { name:'product' },
};

// la ruta se resuelve contra root, asi que basta el nombre del snippet
const objetivo = process.argv[2] || 'structured-data.liquid';
const tipos = (process.argv[3] || 'index,product,collection,article,blog,page,search,404,cart').split(',');
let totalMalos = 0;
/* Cada tipo de pagina se renderiza dos veces: con un producto de precio unico
   y con uno de precio variable. Son dos ramas distintas del JSON-LD (Offer y
   AggregateOffer) y la segunda no se ejercitaba nunca, que es justo donde es
   mas facil colar una coma de mas y romper el bloque entero. */
for (const varia of [false, true]) {
 ctx.product.price_varies = varia;
 if (varia) console.log('\n  --- con precio variable (AggregateOffer) ---');
 for (const tipo of tipos) {
  ctx.request.page_type = tipo;
  ctx.template.name = tipo;
  const salida = await engine.renderFile(objetivo, ctx);
  const bloques = [...salida.matchAll(/<script[^>]*application\/ld\+json[^>]*>([\s\S]*?)<\/script>/g)];
  const resumen = [];
  let malos = 0;
  bloques.forEach(b => {
    try { const j = JSON.parse(b[1]);
      const t = JSON.stringify(j).match(/"@type":"[A-Za-z]+"/g) || [];
      resumen.push([...new Set(t.map(x=>x.split('"')[3]))].join('+'));
    } catch (e) { malos++; totalMalos++; resumen.push('INVALIDO: ' + e.message); }
  });
  console.log(`  ${tipo.padEnd(16)} ${String(salida.length).padStart(5)} car | ${bloques.length} bloques JSON-LD | ${resumen.join('  ·  ') || '(ninguno)'}`);
 }
}
console.log(totalMalos ? `\n${totalMalos} bloques INVALIDOS` : '\nTodos los bloques JSON-LD son JSON valido.');
process.exit(totalMalos ? 1 : 0);
