/* EL NOMBRE DE LA COLECCION NO SE PINTA ENCIMA DEL QUE YA TRAE LA FOTO.
   ------------------------------------------------------------------
   Esto nace de la tienda de verdad: las imagenes de las colecciones llevan el
   nombre rotulado DENTRO de la foto, y el tema le pintaba encima su propio
   titulo. Dos textos, dos tipografias, el mismo sitio. Ninguna bateria lo veia
   porque, tecnicamente, nada se salia de su caja ni fallaba: simplemente se
   leia mal.

   Hay tres modos, y cada uno tiene que hacer EXACTAMENTE lo suyo:

     encima      el titulo va sobre la foto  -> se solapan A PROPOSITO
     debajo      la foto limpia, titulo bajo -> no se solapan, y se VE
     en_la_foto  lo pone la imagen           -> no se solapan, y NO se ve,
                                                pero sigue en el HTML

   Ese ultimo matiz es el que mas importa y el mas facil de romper: si algun
   dia alguien "limpia" el modo en_la_foto con display:none, el nombre de la
   coleccion desaparece del codigo y con el una de las senales que Google lee
   primero. Aqui se exige que el elemento siga existiendo y con su texto.

   Uso:  node verificadores/rotulos/comprobar.mjs                          */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const CSS = path.join(T, 'assets/villumination.css');
const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome']
  .find(p => fs.existsSync(p));

let mal = 0;
const decir = (ok, txt) => { if (!ok) mal++; console.log(`  ${ok ? 'OK   ' : 'FALLA'} ${txt}`); };

/* El banco de pruebas se escribe a mano porque aqui no hay motor de Liquid, y
   eso lo deja libre de separarse de las secciones sin que nadie se entere. La
   comprobacion de abajo lo ata: si una seccion deja de usar una de estas
   clases, o le cambia el nombre, esto se pone rojo antes que la tienda. */
const PIEZAS = {
  'sections/collection-list.liquid':     ['collection-tile-media', 'collection-tile-overlay', 'collection-tile-title'],
  'sections/category-mosaic.liquid':     ['catmosaic-tile', 'catmosaic-shade', 'catmosaic-body', 'catmosaic-title'],
  'sections/main-list-collections.liquid': ['col-index-media', 'col-index-overlay', 'col-index-body', 'col-index-title'],
  'sections/main-collection.liquid':     ['collection-hero-bg', 'collection-hero-overlay', 'collection-hero-inner', 'collection-hero-title'],
};
console.log('\n--- El banco de pruebas usa las clases que las secciones traen ---');
for (const [arch, clases] of Object.entries(PIEZAS)) {
  const txt = fs.readFileSync(path.join(T, arch), 'utf8');
  const faltan = clases.filter(c => !txt.includes(c));
  decir(faltan.length === 0, faltan.length
    ? `${arch}: ya no trae ${faltan.join(', ')}`
    : `${arch}: sus ${clases.length} piezas siguen ahi`);
}
/* Y que el ajuste exista en el editor, porque sin ajuste no hay modo. */
const ESQ = JSON.parse(fs.readFileSync(path.join(T, 'config/settings_schema.json'), 'utf8'));
const ajuste = ESQ.flatMap(g => g.settings || []).find(s => s.id === 'coleccion_rotulo');
decir(!!ajuste, 'el editor de Shopify ofrece el ajuste "coleccion_rotulo"');
decir(!!ajuste && ajuste.options.map(o => o.value).join(',') === 'encima,debajo,en_la_foto',
  'el ajuste ofrece los tres modos');
const CUERPO = fs.readFileSync(path.join(T, 'layout/theme.liquid'), 'utf8');
decir(/rotulo-\{\{\s*settings\.coleccion_rotulo/.test(CUERPO),
  'el <body> lleva la clase del modo elegido');

/* Una foto CON TEXTO DENTRO, que es justo el caso del que salio todo esto. */
const FOTO = 'data:image/svg+xml,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="500">' +
  '<rect width="700" height="500" fill="#123"/><text x="350" y="270" font-family="sans-serif"' +
  ' font-size="64" font-weight="800" text-anchor="middle" fill="#0ff">SUPLEMENTOS</text></svg>');

const MARCADO = `
<div class="collection-list-grid">
  <a href="#" class="collection-tile"><div class="collection-tile-media"><img src="${FOTO}" width="700" height="500"><div class="collection-tile-overlay"></div></div><h3 class="collection-tile-title">Suplementos</h3></a>
</div>
<div class="catmosaic">
  <a href="#" class="catmosaic-tile is-hero"><img src="${FOTO}" width="900" height="700"><span class="catmosaic-shade"></span><span class="catmosaic-body"><span class="catmosaic-title">Suplementos</span></span></a>
</div>
<div class="col-index-grid" style="--cols:2">
  <a href="#" class="col-index-tile"><div class="col-index-media"><img src="${FOTO}" width="800" height="600"><span class="col-index-grain"></span><span class="col-index-overlay"></span></div><div class="col-index-body"><span class="col-index-count">10 productos</span><h2 class="col-index-title">Suplementos</h2></div></a>
</div>
<div class="collection-hero has-img"><img class="collection-hero-bg" src="${FOTO}" width="1600" height="500"><span class="collection-hero-overlay"></span><div class="collection-hero-inner"><h1 class="collection-hero-title">Suplementos</h1></div></div>`;

const PARES = [
  ['la lista de colecciones', '.collection-tile-title', '.collection-tile-media img'],
  ['el mosaico',              '.catmosaic-title',       '.catmosaic-tile img'],
  ['todas las colecciones',   '.col-index-title',       '.col-index-media img'],
  ['la portada de coleccion', '.collection-hero-title', '.collection-hero-bg'],
];

const b = await chromium.launch({ executablePath: CHROME });
const pagina = (modo) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="file://${CSS}"><style>body{margin:0;background:#05050f;padding:18px}</style>
</head><body class="grid-bg rotulo-${modo}"><div class="container">${MARCADO}</div></body></html>`;

for (const modo of ['encima', 'debajo', 'en_la_foto']) {
  console.log(`\n--- Modo "${modo}" ---`);
  const tmp = path.join(AQUI, `.pagina-${modo}.html`);
  fs.writeFileSync(tmp, pagina(modo));
  /* Dos anchos: en movil el mosaico y las tarjetas cambian de rejilla, y una
     regla que arregla el escritorio puede dejar el movil como estaba. */
  for (const ancho of [390, 1280]) {
    const p = await b.newPage({ viewport: { width: ancho, height: 1400 }, isMobile: ancho < 500 });
    await p.goto('file://' + tmp);
    await p.waitForTimeout(250);
    const r = await p.evaluate((pares) => {
      const out = {};
      for (const [nombre, selTexto, selFoto] of pares) {
        const a = document.querySelector(selTexto), c = document.querySelector(selFoto);
        if (!a || !c) { out[nombre] = { falta: true }; continue; }
        const x = a.getBoundingClientRect(), y = c.getBoundingClientRect();
        const dx = Math.min(x.right, y.right) - Math.max(x.left, y.left);
        const dy = Math.min(x.bottom, y.bottom) - Math.max(x.top, y.top);
        const cs = getComputedStyle(a);
        out[nombre] = {
          solape: (dx > 1 && dy > 1) ? `${Math.round(dx)}x${Math.round(dy)} px` : null,
          seVe: cs.display !== 'none' && cs.visibility !== 'hidden' && x.width > 2 && x.height > 2,
          enElCodigo: (a.textContent || '').trim().length > 0 && cs.display !== 'none',
        };
      }
      return out;
    }, PARES);

    for (const [nombre, v] of Object.entries(r)) {
      if (v.falta) { decir(false, `${ancho}px · ${nombre}: falta una pieza en el banco`); continue; }
      if (modo === 'encima') {
        decir(!!v.solape && v.seVe, `${ancho}px · ${nombre}: el titulo va sobre la foto, como debe (${v.solape})`);
      } else {
        decir(!v.solape, v.solape
          ? `${ancho}px · ${nombre}: el titulo SIGUE encima de la foto (${v.solape})`
          : `${ancho}px · ${nombre}: nada del tema se pinta sobre la foto`);
        if (modo === 'debajo') decir(v.seVe, `${ancho}px · ${nombre}: y el titulo se sigue viendo`);
        else decir(!v.seVe && v.enElCodigo,
          `${ancho}px · ${nombre}: el titulo no se ve, pero sigue en el HTML para Google`);
      }
    }
    await p.close();
  }
  fs.unlinkSync(tmp);
}
await b.close();

console.log(mal
  ? `\n  ${mal} en rojo: el rotulo de las colecciones no se comporta.\n`
  : '\nLas colecciones nunca pintan dos textos en el mismo sitio, y el nombre nunca se pierde para los buscadores.\n');
process.exit(mal ? 1 : 0);
