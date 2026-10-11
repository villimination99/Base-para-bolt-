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
const ASSETS = process.env.TEMA ? path.join(process.env.TEMA, 'assets') : path.join(RAIZ, 'theme/assets');
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
  {
    /* El visor de zoom de la ficha de producto. Llevaba el foco al boton de
       cerrar y ahi se acababa: a la siguiente tabulacion el foco se iba a la
       tienda de detras, que no se ve pero sigue siendo tabulable. Ademas el
       dialogo no tenia nombre, asi que un lector de pantalla anunciaba
       "dialogo" y nada mas. Las dos cosas se miden aqui. */
    nombre: 'visor de zoom',
    panel: '.img-lightbox',
    claseAbierto: 'is-open',
    abrir: '[data-zoomable]',
    creaAlAbrir: true,
    exigeNombre: true,
    html: `
      <main>
        <img data-zoomable src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
             alt="Creatina con electrolitos" width="200" height="200">
      </main>`,
    estilo: '.img-lightbox{position:fixed;inset:0;background:#05060a;display:flex;opacity:0;pointer-events:none}.img-lightbox.is-open{opacity:1;pointer-events:auto}',
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

  const abierto = await p.evaluate(([s, cls]) => {
    const e = document.querySelector(s);
    return !!e && e.classList.contains(cls);
  }, [caso.panel, caso.claseAbierto || 'open']);
  decir(abierto, `${caso.nombre}: se abre al pulsar`);
  if (!abierto) { await ctx.close(); continue; }

  /* Un dialogo modal sin nombre accesible se anuncia como "dialogo" a secas:
     quien no ve la pantalla no sabe que se ha abierto. */
  if (caso.exigeNombre) {
    const nombre = await p.evaluate(s => {
      const e = document.querySelector(s);
      return e ? (e.getAttribute('aria-label') || e.getAttribute('aria-labelledby') || '') : '';
    }, caso.panel);
    decir(nombre.trim().length > 0, `${caso.nombre}: el dialogo tiene nombre accesible${nombre ? ' ("' + nombre + '")' : ''}`);
  }

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
  const cerrado = await p.evaluate(([s, cls]) => !document.querySelector(s).classList.contains(cls), [caso.panel, caso.claseAbierto || 'open']);
  decir(cerrado, `${caso.nombre}: Escape lo cierra`);

  const vuelve = await p.evaluate(s => document.activeElement === document.querySelector(s), caso.abrir);
  decir(vuelve, `${caso.nombre}: el foco vuelve al boton que lo abrio`);

  decir(errs.length === 0, `${caso.nombre}: sin errores de JavaScript${errs.length ? ': ' + errs[0] : ''}`);
  fs.unlinkSync(tmp);
  await ctx.close();
}

/* ------------------------------------------------------------------
   EL CERROJO DEL DESPLAZAMIENTO, CON DOS CAPAS ABIERTAS A LA VEZ
   Cada panel bloqueaba y desbloqueaba la pagina por su cuenta. Con el
   menu y el carrito abiertos, cerrar el primero soltaba el cerrojo del
   segundo y la tienda volvia a moverse debajo de un panel que seguia
   tapandola. Ahora se cuenta, y esto lo comprueba con los dos abiertos.
   ------------------------------------------------------------------ */
{
  const ctx = await navegador.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  const tmp = path.join(AQUI, '.cerrojo.html');
  fs.writeFileSync(tmp, `<!doctype html><html lang="es"><head><meta charset="utf-8">
    <style>body{margin:0;height:300vh;background:#05060a;color:#fff}
    #mobile-menu{position:fixed;inset:0;background:#0a0b12;transform:translateX(100%)}#mobile-menu.open{transform:none}
    #cart-drawer{position:fixed;inset:0;pointer-events:none}#cart-drawer.open{pointer-events:auto}
    .cart-drawer-panel{position:absolute;inset:0 0 0 auto;width:90%;background:#0a0b12;transform:translateX(100%)}
    #cart-drawer.open .cart-drawer-panel{transform:none}</style>
    <style>${CSS}</style></head><body>
    <header>
      <button class="mobile-toggle" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menu">M</button>
      <a href="/cart" class="cart-btn" id="cart-btn-open" data-cart-drawer-open aria-label="Carrito">C</a>
    </header>
    <nav id="mobile-menu" aria-label="Menu principal">
      <button data-mobile-close id="cerrar-menu" aria-label="Cerrar">X</button><a href="/a">Colecciones</a>
    </nav>
    <div id="cart-drawer" class="cart-drawer" aria-hidden="true">
      <div class="cart-drawer-panel" role="dialog" aria-modal="true" aria-label="Carrito">
        <button class="cart-drawer-close" id="cerrar-carro" data-cart-drawer-close aria-label="Cerrar">X</button>
        <a href="/checkout" class="btn">Pagar</a>
      </div>
    </div>
    <main><a href="/x">enlace de detras</a></main>
    <script>window.theme={routes:{cart:'/cart'},settings:{cartType:'drawer'},strings:{}};</script>
    </body></html>`);
  await p.goto('file://' + tmp);
  await p.addScriptTag({ path: path.join(ASSETS, 'base.js') });
  await p.waitForTimeout(400);

  const bloqueado = () => p.evaluate(() =>
    getComputedStyle(document.body).overflow === 'hidden' ||
    getComputedStyle(document.documentElement).overflow === 'hidden');

  decir(!(await bloqueado()), 'cerrojo: la pagina se mueve antes de abrir nada');

  await p.locator('.mobile-toggle').click();
  await p.waitForTimeout(250);
  decir(await bloqueado(), 'cerrojo: con el menu abierto la pagina de detras no se mueve');

  await p.evaluate(() => document.getElementById('cart-btn-open').click());
  await p.waitForTimeout(250);
  const dosAbiertos = await p.evaluate(() =>
    document.getElementById('mobile-menu').classList.contains('open') &&
    document.getElementById('cart-drawer').classList.contains('open'));
  decir(dosAbiertos, 'cerrojo: se pueden tener el menu y el carrito abiertos a la vez');

  await p.evaluate(() => document.getElementById('cerrar-menu').click());
  await p.waitForTimeout(250);
  decir(await bloqueado(), 'cerrojo: al cerrar el menu sigue bloqueada porque el carrito sigue abierto');

  await p.evaluate(() => document.getElementById('cerrar-carro').click());
  await p.waitForTimeout(250);
  decir(!(await bloqueado()), 'cerrojo: al cerrar el ultimo panel la pagina vuelve a moverse');

  /* Y el caso que rompia la cuenta: el carrito se vuelve a abrir cada vez
     que se añade algo. Si eso sumara otro cerrojo, cerrarlo una vez ya no
     bastaria y la tienda se quedaria clavada para siempre. */
  await p.evaluate(() => { const b = document.getElementById('cart-btn-open'); b.click(); b.click(); b.click(); });
  await p.waitForTimeout(250);
  await p.evaluate(() => document.getElementById('cerrar-carro').click());
  await p.waitForTimeout(250);
  decir(!(await bloqueado()), 'cerrojo: abrir el carrito tres veces seguidas no deja la pagina clavada');

  decir(errs.length === 0, `cerrojo: sin errores de JavaScript${errs.length ? ': ' + errs[0] : ''}`);
  fs.unlinkSync(tmp);
  await ctx.close();
}

await navegador.close();
console.log('');
console.log(fallos === 0 ? 'Los paneles se manejan con teclado sin perder el foco.'
                         : `${fallos} problema(s) de teclado.`);
process.exit(fallos ? 1 : 0);
