/* Comprueba con teclado de verdad los paneles que tapan la pagina.
   ------------------------------------------------------------------
   Un panel superpuesto tiene que hacer tres cosas, y ni el menu movil ni el
   carrito hacian ninguna hasta que esta prueba lo midio:
     1. Llevar el foco dentro al abrirse.
     2. Atraparlo mientras esta abierto. Sin esto, a las cuatro tabulaciones
        el foco se escapaba al contenido de detras y el visitante recorria
        enlaces que no puede ver.
     3. Devolverlo a donde estaba al cerrarse.

   Se prueba pulsando Tab de verdad y leyendo document.activeElement, no
   inspeccionando el codigo: el foco depende de lo que este visible en ese
   momento, y eso solo lo sabe el navegador.

   Uso:  node verificadores/teclado/comprobar.mjs                           */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '../..');
const ASSETS = path.join(RAIZ, 'theme/assets');
const CHROME = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const CSS = fs.readFileSync(path.join(ASSETS, 'villumination.css'), 'utf8');

/* Dos paneles, cada uno con el marcado y las clases que usa el tema. */
const CASOS = [
  {
    nombre: 'menu movil',
    panel: '#mobile-menu',
    abrir: '.mobile-toggle',
    html: `
      <header><button class="mobile-toggle" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menu">M</button></header>
      <nav id="mobile-menu" aria-label="Menu principal">
        <button data-mobile-close aria-label="Cerrar">X</button>
        <a href="/a">Colecciones</a><a href="/b">Diario</a><a href="/c">VI.P</a>
      </nav>`,
    estilo: '#mobile-menu{position:fixed;inset:0;background:#0a0b12;transform:translateX(100%)}#mobile-menu.open{transform:none}',
  },
  {
    nombre: 'carrito lateral',
    panel: '#cart-drawer',
    abrir: '#cart-btn-open',
    // Marcado real de sections/cart-drawer.liquid y del enlace del
    // encabezado. El carrito solo se abre como panel si theme.settings
    // dice cartType 'drawer'; con 'page' navega a /cart y no hay panel.
    ajustes: { cartType: 'drawer' },
    html: `
      <header><a href="/cart" class="cart-btn" id="cart-btn-open" data-cart-drawer-open aria-label="Carrito">C</a></header>
      <div id="cart-drawer" class="cart-drawer" aria-hidden="true">
        <div class="cart-drawer-overlay" data-cart-drawer-close></div>
        <div class="cart-drawer-panel" role="dialog" aria-modal="true" aria-label="Carrito">
          <button class="cart-drawer-close" data-cart-drawer-close aria-label="Cerrar">X</button>
          <div data-cart-drawer-body>
            <a href="/products/proteina">Proteina</a>
            <button data-qty-up aria-label="Sumar uno">+</button>
          </div>
          <a href="/checkout" class="btn">Pagar</a>
        </div>
      </div>`,
    estilo: '#cart-drawer{position:fixed;inset:0;pointer-events:none}#cart-drawer.open{pointer-events:auto}.cart-drawer-panel{position:absolute;inset:0 0 0 auto;width:90%;background:#0a0b12;transform:translateX(100%)}#cart-drawer.open .cart-drawer-panel{transform:none}',
  },
];

const navegador = await chromium.launch({ executablePath: CHROME });
let fallos = 0;
const decir = (ok, txt) => { if (!ok) fallos++; console.log(`${ok ? ' OK   ' : 'FALLA '} ${txt}`); };

console.log('');
for (const caso of CASOS) {
  const ctx = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));

  const tmp = path.join(AQUI, '.panel.html');
  fs.writeFileSync(tmp, `<!doctype html><html lang="es"><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>body{margin:0;background:#05060a;color:#fff;font-family:system-ui}
    ${caso.estilo}</style><style>${CSS}</style></head><body>
    ${caso.html}
    <main><a href="/x">enlace de detras</a> <button>boton de detras</button>
      <input aria-label="campo de detras"></main>
    <script>window.theme={routes:{cart:'/cart'},settings:${JSON.stringify(caso.ajustes || {})},strings:{}};</script>
    </body></html>`);
  await p.goto('file://' + tmp);
  await p.addScriptTag({ path: path.join(ASSETS, 'base.js') });
  await p.waitForTimeout(400);

  const abrir = await p.locator(caso.abrir).count();
  if (!abrir) { decir(false, `${caso.nombre}: no se encuentra el boton que lo abre`); await ctx.close(); continue; }

  await p.locator(caso.abrir).focus();
  await p.locator(caso.abrir).click();
  await p.waitForTimeout(400);

  const abierto = await p.evaluate(s => {
    const e = document.querySelector(s);
    return !!e && e.classList.contains('open');
  }, caso.panel);
  decir(abierto, `${caso.nombre}: se abre al pulsar`);
  if (!abierto) { await ctx.close(); continue; }

  const dentroAlAbrir = await p.evaluate(s => document.querySelector(s).contains(document.activeElement), caso.panel);
  decir(dentroAlAbrir, `${caso.nombre}: el foco entra al abrirse`);

  // Ocho tabulaciones: mas que elementos hay dentro, para forzar la vuelta
  let escapo = false;
  for (let i = 0; i < 8; i++) {
    await p.keyboard.press('Tab');
    const dentro = await p.evaluate(s => document.querySelector(s).contains(document.activeElement), caso.panel);
    if (!dentro) { escapo = true; break; }
  }
  decir(!escapo, `${caso.nombre}: el foco no se escapa al contenido de detras (8 tabulaciones)`);

  // Y hacia atras
  let escapoAtras = false;
  for (let i = 0; i < 8; i++) {
    await p.keyboard.press('Shift+Tab');
    const dentro = await p.evaluate(s => document.querySelector(s).contains(document.activeElement), caso.panel);
    if (!dentro) { escapoAtras = true; break; }
  }
  decir(!escapoAtras, `${caso.nombre}: tampoco se escapa tabulando hacia atras`);

  await p.keyboard.press('Escape');
  await p.waitForTimeout(400);
  const cerrado = await p.evaluate(s => !document.querySelector(s).classList.contains('open'), caso.panel);
  decir(cerrado, `${caso.nombre}: Escape lo cierra`);

  const vuelve = await p.evaluate(s => document.activeElement === document.querySelector(s), caso.abrir);
  decir(vuelve, `${caso.nombre}: el foco vuelve al boton que lo abrio`);

  decir(errs.length === 0, `${caso.nombre}: sin errores de JavaScript${errs.length ? ': ' + errs[0] : ''}`);
  fs.unlinkSync(tmp);
  await ctx.close();
}

await navegador.close();
console.log('');
console.log(fallos === 0 ? 'Los paneles se manejan con teclado sin perder el foco.'
                         : `${fallos} problema(s) de teclado.`);
process.exit(fallos ? 1 : 0);
