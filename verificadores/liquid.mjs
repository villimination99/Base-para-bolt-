/* El motor de Liquid compartido por las baterias.
   ------------------------------------------------------------------
   Vivia dentro de verificadores/secciones/comprobar.mjs: ciento cincuenta
   lineas de contexto de tienda, filtros de Shopify y etiquetas que liquidjs
   no trae. Cuando la bateria de accesibilidad necesito renderizar las
   mismas secciones, la alternativa era copiarlo -- y dos copias del mismo
   contexto se separan a la primera seccion que estrene un ajuste. Asi que
   sale aqui, entero y sin cambios, y las dos lo importan.

   Exporta:
     motor(T)              el Liquid ya configurado para ese tema
     ctxBase               una tienda de mentira completa
     prepararFuente(src)   form y paginate resueltos antes de parsear
     PAGINA                el tipo de pagina que le toca a cada seccion
     contextoDeSeccion()   los ajustes y bloques sacados del esquema        */
import { Liquid } from 'liquidjs';
import fs from 'fs';
import path from 'path';

export const T = process.env.TEMA || 'theme';

const img = { src: '//cdn/x.png', width: 1200, height: 1200, aspect_ratio: 1, alt: 'foto',
              preview_image: { aspect_ratio: 1, src: '//cdn/x.png' }, media_type: 'image', id: 1 };

const variante = { id: 1, sku: 'X', barcode: '', price: 1990, compare_at_price: null, available: true,
  title: 'Único', inventory_quantity: 10, inventory_management: 'shopify', inventory_policy: 'deny',
  requires_shipping: true, options: ['Único'], featured_media: img, selected: false, url: '/products/p' };

const producto = { id: 9, title: 'Proteína', handle: 'proteina', url: '/products/proteina',
  vendor: 'VILLUMINATIONS', type: 'Suplemento', description: '<p>Aislado de suero.</p>',
  price: 1990, price_min: 1990, price_max: 1990, price_varies: false, compare_at_price: null,
  available: true, sold_out: false, has_only_default_variant: true, featured_media: img,
  media: [img], images: [img], variants: [variante], selected_or_first_available_variant: variante,
  options_with_values: [{ name: 'Talla', values: [{ name: 'Único', selected: true }] }],
  collections: [], metafields: { reviews: {}, villumination: {} }, tags: [], created_at: '2024-01-01' };

const coleccion = { id: 2, title: 'Suplementos', handle: 'suplementos', url: '/collections/suplementos',
  description: 'Todo lo que se toma.', products: [producto], products_count: 1, all_products_count: 1,
  image: img, featured_image: img, all_tags: [], sort_by: 'manual', default_sort_by: 'manual',
  sort_options: [{ name: 'Manual', value: 'manual' }], filters: [] };

const articulo = { id: 3, title: 'Cómo entrenar', handle: 'como-entrenar', url: '/blogs/diario/como',
  content: '<p>Texto.</p>', excerpt: 'Resumen.', author: 'Villumination', image: img,
  published_at: '2024-05-01', tags: [], comments_count: 0, comments: [] };

export const ctxBase = {
  shop: { name: 'Villumination', url: 'https://villuminations.com', description: 'Tienda fitness.',
          enabled_payment_types: ['visa'], published_at: '2024-01-01', money_format: '${{amount}}' },
  routes: { cart_add_url: '/cart/add', cart_url: '/cart', root_url: '/', search_url: '/search',
            account_url: '/account', all_products_collection_url: '/collections/all' },
  request: { page_type: 'index', path: '/', locale: { iso_code: 'es', root_url: '/' }, design_mode: false,
             origin: 'https://villuminations.com' },
  cart: { item_count: 0, items: [], total_price: 0, currency: { iso_code: 'CAD', symbol: '$' }, note: '' },
  settings: { enable_scroll_reveal: true, enable_card_tilt: true, product_zoom: true,
              product_sticky_form: true, product_enable_3d: true, cart_type: 'drawer',
              price_show_compare: true, price_show_save: true, badge_low_stock: 5, badge_new_days: 30,
              variant_style: 'pill', card_show_vendor: false, card_text_align: 'left',
              color_cyan: '#00d4ff', color_pink: '#ff2ecb', color_purple: '#7b2fff', color_bg: '#000',
              logo: img, favicon: img, brand_display_name: 'VILLUMINATION', search_show_header: true,
              social_youtube: 'https://youtube.com/@x', cart_cross_sell: true },
  collections: { all: coleccion, suplementos: coleccion },
  product: producto, collection: coleccion, article: articulo,
  blog: { title: 'Diario', url: '/blogs/diario', articles: [articulo], all_tags: [] },
  page: { title: 'Cómo se hace', content: '<p>Texto.</p>', handle: 'como-se-hace', url: '/pages/x' },
  search: { performed: true, terms: 'proteina', results: [producto], results_count: 1, filters: [], sort_by: '' },
  linklists: { 'main-menu': { links: [{ title: 'Tienda', url: '/collections', links: [] }] },
               footer: { links: [{ title: 'Envíos', url: '/policies/shipping-policy', links: [] }] } },
  template: { name: 'index', suffix: null },
  current_tags: [], current_page: 1, canonical_url: 'https://villuminations.com/',
  page_title: 'Villumination', page_description: 'Tienda fitness.',
  recommendations: { products: [producto], performed: true },
  form: {}, customer: null, content_for_header: '', powered_by_link: '',
};

export const e = new Liquid({ root: [T + '/snippets', T], extname: '.liquid',
                       strictFilters: false, strictVariables: false });
const F = {
  image_url: () => '//cdn/x.png', money: v => '$' + (Number(v) / 100).toFixed(2),
  money_without_currency: v => (Number(v) / 100).toFixed(2), money_with_currency: v => '$' + v,
  t: v => String(v), json: v => JSON.stringify(v === undefined ? null : v),
  asset_url: v => '//cdn/' + v, asset_img_url: () => '//cdn/x.png', file_url: v => '//cdn/' + v,
  stylesheet_tag: v => `<link rel="stylesheet" href="${v}">`, script_tag: v => `<script src="${v}"></script>`,
  video_tag: () => '<video></video>', external_video_tag: () => '<iframe></iframe>',
  model_viewer_tag: () => '<model-viewer></model-viewer>', image_tag: () => '<img alt="">',
  payment_type_svg_tag: () => '<svg></svg>', payment_button: () => '<button>Comprar ahora</button>',   // el de Shopify si lleva texto
  payment_terms: () => '', link_to: (v, u) => `<a href="${u}">${v}</a>`,
  within: v => v, default_pagination: () => '', highlight: v => v, weight_with_unit: v => v + ' g',
  format_address: () => '', article_img_url: () => '//cdn/x.png', img_tag: () => '<img alt="">',
  handleize: v => String(v).toLowerCase().replace(/\s+/g, '-'), handle: v => String(v).toLowerCase(),
  camelize: v => v, url_for_type: v => '/types/' + v, url_for_vendor: v => '/vendors/' + v,
  sort_by: v => v, currency_selector: () => '', time_tag: v => `<time>${v}</time>`,
  inline_asset_content: () => '<svg></svg>', metafield_tag: v => String(v), metafield_text: v => String(v),
  brightness_difference: () => 100, color_difference: () => 500, color_brightness: () => 50,
  color_modify: v => v, color_mix: v => v, color_extract: () => 0, color_to_rgb: v => v,
  color_lighten: v => v, color_darken: v => v, color_saturate: v => v, color_desaturate: v => v,
  font_face: () => '', font_modify: v => v, font_url: () => '//cdn/f.woff2',
};
for (const [k, fn] of Object.entries(F)) e.registerFilter(k, fn);

/* Etiquetas que liquidjs no trae y que en Shopify SI emiten HTML.
   La primera version las trataba como contenedores con un bucle a mano sobre
   los tokens, y se comia todo lo que venia DESPUES de la etiqueta de cierre:
   cinco secciones aparecian con el </section> final sin cerrar y parecian
   rotas estandolo el arnes. Este es el patron documentado de liquidjs, que
   deja intacto el resto del flujo. */
/* form y paginate se resuelven ANTES de parsear, sustituyendo la etiqueta
   por el HTML que Shopify emite de verdad.
   Registrarlas como etiquetas de bloque con parseStream se probo y sale mal:
   liquidjs comparte estado entre invocaciones de la misma etiqueta y el
   resultado salia duplicado y descuadrado. Verificado con un caso minimo:
     <section><div>{% form "x" %}DENTRO{% endform %}</div></section>
   daba  <section><div>DENTRO<form><section><div>DENTRO</form></div></section>
   Una sustitucion de texto no tiene ese problema y es exactamente lo que
   hace Shopify: {% form %} imprime <form> y {% endform %} imprime </form>. */
export function prepararFuente(src) {
  return src
    .replace(/\{%-?\s*form\b[\s\S]*?-?%\}/g, '<form>')
    .replace(/\{%-?\s*endform\s*-?%\}/g, '</form>')
    .replace(/\{%-?\s*paginate\b[\s\S]*?-?%\}/g, '')
    .replace(/\{%-?\s*endpaginate\s*-?%\}/g, '');
}

function tragar(nombre) {
  return {
    parse(token, remainTokens) {
      const flujo = this.liquid.parser.parseStream(remainTokens)
        .on('template', () => {})
        .on(`tag:end${nombre}`, () => flujo.stop())
        .on('end', () => flujo.stop());
      flujo.start();
    },
    render() { return ''; },
  };
}
for (const n of ['comment', 'javascript', 'stylesheet', 'style', 'schema']) e.registerTag(n, tragar(n));
e.registerTag('section', { parse() {}, render() { return ''; } });
e.registerTag('sections', { parse() {}, render() { return ''; } });

/* {% render block %} es el bloque de aplicacion de Shopify: el argumento no
   es el nombre de un snippet sino un objeto, y liquidjs no sabe resolverlo.
   Se deja pasar como un hueco vacio, que es lo que hay en una tienda sin
   aplicaciones instaladas. Los {% render 'nombre' %} normales siguen
   funcionando de verdad, que es lo que interesa probar. */
const renderOriginal = e.tags.get ? e.tags.get('render') : null;
e.registerTag('render', {
  parse(token, remainTokens) {
    this.esLiteral = /^\s*['"]/.test(token.args || '');
    if (this.esLiteral && renderOriginal && renderOriginal.parse)
      return renderOriginal.parse.call(this, token, remainTokens);
    this.args = token.args;
  },
  *render(ctx, em) {
    if (this.esLiteral && renderOriginal && renderOriginal.render)
      return yield renderOriginal.render.call(this, ctx, em);
    return '';
  },
});

/* El tipo de pagina que le toca a cada seccion, para que las condiciones de
   dentro se cumplan como en la tienda. */
export const PAGINA = {
  'main-product': 'product', 'main-collection': 'collection', 'main-article': 'article',
  'main-blog': 'blog', 'main-page': 'page', 'main-search': 'search', 'main-cart': 'cart',
  'main-404': '404', 'main-list-collections': 'list-collections', 'main-contact': 'page',
};


/* Los ajustes y bloques de una seccion, sacados de SU esquema y no
   inventados: Shopify aplica los "default" a todo ajuste que la plantilla
   no guarda, asi que probar con {} deja partes enteras sin ejercitar. */
export function contextoDeSeccion(nombre, src) {
  const m = src.match(/\{%\s*schema\s*%\}([\s\S]*?)\{%\s*endschema\s*%\}/);
  const esquema = m ? JSON.parse(m[1]) : null;
  const ajustes = {};
  for (const x of (esquema?.settings || [])) if (x.id && 'default' in x) ajustes[x.id] = x.default;
  const bloques = (esquema?.blocks || []).map((b, i) => {
    const s = {};
    for (const x of (b.settings || [])) if (x.id && 'default' in x) s[x.id] = x.default;
    return { id: 'b' + i, type: b.type, settings: s, shopify_attributes: '' };
  });
  const ctx = Object.assign({}, ctxBase, {
    section: { id: nombre, settings: ajustes, blocks: bloques, location: 'template' },
  });
  ctx.request = Object.assign({}, ctxBase.request, { page_type: PAGINA[nombre] || 'index' });
  ctx.template = { name: PAGINA[nombre] || 'index', suffix: null };
  return { esquema, ctx, ajustes, bloques };
}
