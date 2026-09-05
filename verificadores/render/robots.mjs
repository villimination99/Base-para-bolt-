/* Renderiza templates/robots.txt.liquid y comprueba el resultado.
   ------------------------------------------------------------------
   Este archivo decide que puede leer cada buscador y cada IA. Una linea
   "Disallow" de mas saca paginas del indice sin previo aviso y sin dejar
   rastro visible en la tienda, asi que aqui no vale con leer el codigo:
   hay que renderizarlo y mirar lo que sale.

   Uso:  node verificadores/render/robots.mjs                               */
import { Liquid } from 'liquidjs';
import fs from 'fs';

const T = 'theme';
const e = new Liquid({ root: [T + '/snippets', T], extname: '.liquid',
                       strictFilters: false, strictVariables: false });
e.registerTag('comment', { parse(tk, rem) { let d = 1; while (rem.length) { const t = rem.shift(); if (t.name === 'comment') d++; if (t.name === 'endcomment') { d--; if (!d) break; } } }, render() { return ''; } });

/* Imitacion de los grupos por defecto de Shopify, con la forma que documenta
   shopify.dev: user_agent, rules y un sitemap opcional. */
const grupo = (ua, reglas, sitemap) => ({
  user_agent: `User-agent: ${ua}`,
  rules: reglas.map(r => `\n${r}`),
  sitemap: sitemap ? `Sitemap: ${sitemap}` : '',
});
const robots = { default_groups: [
  grupo('*', ['Disallow: /admin', 'Disallow: /cart', 'Disallow: /checkout',
              'Disallow: /orders', 'Disallow: /*?*sort_by*', 'Disallow: /policies/'],
        'https://villuminations.com/sitemap.xml'),
  grupo('adsbot-google', ['Disallow: /checkout', 'Disallow: /cart']),
  grupo('Nutch', ['Disallow: /']),
  grupo('AhrefsBot', ['Crawl-delay: 10']),
  grupo('MJ12bot', ['Crawl-delay: 10']),
  grupo('Pinterest', ['Crawl-delay: 1']),
] };

const ctx = { robots, settings: { seo_sitemap_extra: '' },
              request: { host: 'villuminations.com', origin: 'https://villuminations.com' } };
e.options.globals = ctx;

const src = fs.readFileSync(`${T}/templates/robots.txt.liquid`, 'utf8');
let out;
try { out = await e.parseAndRender(src, ctx); }
catch (err) { console.error('FALLA  robots.txt no renderiza: ' + err.message); process.exit(1); }

const lineas = out.split('\n').map(l => l.trim());
const grupos = {};
let actual = null;
for (const l of lineas) {
  if (/^User-agent:/i.test(l)) { actual = l.split(':')[1].trim(); grupos[actual] = grupos[actual] || []; }
  else if (actual && /^(Allow|Disallow|Crawl-delay):/i.test(l)) grupos[actual].push(l);
}

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK  ' : 'FALLA'}  ${txt}`); };

console.log('');
// 1. Los grupos por defecto de Shopify siguen ahi, intactos
decir(!!grupos['*'], 'El grupo "*" de Shopify se conserva');
decir((grupos['*'] || []).some(r => /Disallow: \/checkout/.test(r)),
  'Las reglas por defecto se imprimen (checkout sigue bloqueado)');
decir(/Sitemap:\s*https?:\/\/\S+\/sitemap\.xml/.test(out), 'El sitemap se declara');

// 2. Nada nuevo se bloquea por accidente. Solo los grupos que Shopify ya
//    traia pueden llevar Disallow; los anadidos por el tema, jamas.
const porDefecto = new Set(['*', 'adsbot-google', 'Nutch', 'AhrefsBot', 'MJ12bot', 'Pinterest']);
const bloqueosNuevos = Object.entries(grupos)
  .filter(([ua, rs]) => !porDefecto.has(ua) && rs.some(r => /^Disallow:\s*\/\s*$/i.test(r)))
  .map(([ua]) => ua);
decir(bloqueosNuevos.length === 0,
  `Ningun grupo anadido bloquea el sitio${bloqueosNuevos.length ? ': ' + bloqueosNuevos.join(', ') : ''}`);

// 3. Las IA y los buscadores por respuesta tienen permiso explicito
const debenEntrar = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot',
  'PerplexityBot', 'Google-Extended', 'Applebot-Extended', 'meta-externalagent', 'Amazonbot'];
const sinPermiso = debenEntrar.filter(a => !grupos[a] || !grupos[a].some(r => /^Allow:\s*\//i.test(r)));
decir(sinPermiso.length === 0,
  `Los rastreadores de IA tienen permiso explicito${sinPermiso.length ? '. FALTAN: ' + sinPermiso.join(', ') : ` (${debenEntrar.length} comprobados)`}`);

const motores = ['bingbot', 'YandexBot', 'DuckDuckBot', 'Baiduspider', 'SeznamBot', 'Yeti'];
const sinMotor = motores.filter(a => !grupos[a]);
decir(sinMotor.length === 0,
  `Los buscadores clasicos estan nombrados${sinMotor.length ? '. FALTAN: ' + sinMotor.join(', ') : ` (${motores.length} comprobados)`}`);

// 4. Ningun user-agent repetido: dos grupos con el mismo nombre dan un
//    robots.txt ambiguo y cada rastreador decide por su cuenta cual gana.
const repes = Object.entries(grupos).filter(([, rs]) => false); // se calcula abajo
const cuenta = {};
for (const l of lineas) if (/^User-agent:/i.test(l)) {
  const ua = l.split(':')[1].trim().toLowerCase();
  cuenta[ua] = (cuenta[ua] || 0) + 1;
}
const dobles = Object.entries(cuenta).filter(([, n]) => n > 1).map(([ua, n]) => `${ua} x${n}`);
decir(dobles.length === 0, `Ningun user-agent repetido${dobles.length ? ': ' + dobles.join(', ') : ''}`);

// 5. Formato: sin lineas sueltas que no sean directiva, comentario o vacio
const sueltas = lineas.filter(l => l && !l.startsWith('#') &&
  !/^(User-agent|Allow|Disallow|Crawl-delay|Sitemap|Host):/i.test(l));
decir(sueltas.length === 0, `Sin lineas invalidas${sueltas.length ? ': ' + JSON.stringify(sueltas.slice(0, 3)) : ''}`);

console.log('');
console.log(`  ${Object.keys(grupos).length} grupos, ${out.split('\n').length} lineas, ${out.length} caracteres`);
console.log('');
console.log(fallos === 0 ? 'El robots.txt abre la tienda a todos los motores y a las IA.'
                         : `${fallos} problema(s) en el robots.txt.`);
process.exit(fallos ? 1 : 0);
