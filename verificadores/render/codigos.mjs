/* Comprueba que los codigos de verificacion salen bien pegues lo que pegues.
   ------------------------------------------------------------------
   Cada buscador ensena el codigo dentro de una etiqueta <meta> entera, y lo
   natural es copiar la linea completa. Pegada tal cual en un ajuste que
   espera solo el codigo, el tema imprimia una etiqueta rota y la
   verificacion fallaba sin decir por que. Aqui se prueban las formas reales
   en que cada uno lo presenta.

   Uso:  node verificadores/render/codigos.mjs                              */
import { Liquid } from 'liquidjs';
import fs from 'fs';

const T = 'theme';
const e = new Liquid({ root: [T + '/snippets', T], extname: '.liquid',
                       strictFilters: false, strictVariables: false });
e.registerFilter('escape', v => String(v).replace(/&/g, '&amp;').replace(/</g, '&lt;')
  .replace(/>/g, '&gt;').replace(/"/g, '&quot;'));
e.registerTag('comment', { parse(tk, rem) { let d = 1; while (rem.length) { const t = rem.shift(); if (t.name === 'comment') d++; if (t.name === 'endcomment') { d--; if (!d) break; } } }, render() { return ''; } });

const CODIGO = 'A1b2C3d4-E5f6G7h8_I9j0';

/* Las formas en que cada buscador ensena el codigo, tal cual salen de sus
   paneles. La ultima no es de ningun panel: es un pegado descuidado. */
const FORMAS = [
  ['el codigo suelto', CODIGO],
  ['la etiqueta entera de Google', `<meta name="google-site-verification" content="${CODIGO}" />`],
  ['la de Bing, sin cierre', `<meta name="msvalidate.01" content="${CODIGO}">`],
  ['la de Yandex', `<meta name="yandex-verification" content="${CODIGO}" />`],
  ['la de Pinterest', `<meta name="p:domain_verify" content="${CODIGO}"/>`],
  ['la de Meta', `<meta name="facebook-domain-verification" content="${CODIGO}" />`],
  ['con comillas simples', `<meta name='msvalidate.01' content='${CODIGO}'>`],
  ['con espacios y salto', `\n  <meta name="msvalidate.01" content="${CODIGO}">  \n`],
  ['sin comillas', `<meta name=msvalidate.01 content=${CODIGO}>`],
  ['vacio', ''],
  ['solo espacios', '   '],
];

let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };
console.log('');

for (const [nombre, valor] of FORMAS) {
  const salida = (await e.renderFile('codigo-verificacion', { valor })).trim();
  const esperado = valor.trim() === '' ? '' : CODIGO;
  decir(salida === esperado,
    `${nombre.padEnd(30)} -> ${salida === '' ? '(vacio)' : salida}${salida === esperado ? '' : `   ESPERADO: ${esperado || '(vacio)'}`}`);
}

/* Y la comprobacion que de verdad importa: que la etiqueta que sale a la
   pagina sea valida, con el codigo dentro y sin nada roto. */
const robots = fs.readFileSync(`${T}/snippets/seo-robots.liquid`, 'utf8');
const ctx = { settings: {
  seo_bing_verification: `<meta name="msvalidate.01" content="${CODIGO}">`,
  seo_yandex_verification: CODIGO,
  seo_pinterest_verification: `<meta name='p:domain_verify' content='${CODIGO}'/>`,
  seo_facebook_domain: `  <meta name="facebook-domain-verification" content="${CODIGO}" />  `,
}, request: { page_type: 'index' } };
e.options.globals = ctx;
const html = await e.parseAndRender(robots, ctx);

for (const [nombre, aguja] of [['Bing', 'msvalidate.01'], ['Yandex', 'yandex-verification'],
                               ['Pinterest', 'p:domain_verify'], ['Meta', 'facebook-domain-verification']]) {
  // Sin expresion regular: el nombre de Bing lleva un punto y escaparlo
  // dentro de una plantilla anidada salio mal (barras de mas), y la prueba
  // acusaba al tema de no emitir una etiqueta que si estaba.
  const marca = `<meta name="${aguja}" content="`;
  const i = html.indexOf(marca);
  const valor = i < 0 ? null : html.slice(i + marca.length).split('"')[0];
  decir(valor === CODIGO,
    `La etiqueta de ${nombre.padEnd(10)} sale con el codigo limpio${valor !== null ? ` (content="${valor}")` : ' — NO SALE'}`);
}
decir(!/&lt;meta/.test(html), 'Ninguna etiqueta lleva otra etiqueta escapada dentro');

console.log('');
console.log(fallos === 0 ? 'Los codigos de verificacion funcionan pegues lo que pegues.'
                         : `${fallos} problema(s) con los codigos.`);
process.exit(fallos ? 1 : 0);
