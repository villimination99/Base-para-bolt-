/* Accesibilidad medida, no supuesta.
   ------------------------------------------------------------------
   El tema ya tenia bateria de contraste y de teclado, pero nada que
   recorriera el arbol entero buscando lo que un lector de pantalla no puede
   nombrar: un boton que solo dice un emoji, un campo sin etiqueta, un id
   repetido, un salto de h2 a h4. Eso no lo ve nadie mirando la pagina --
   se ve exactamente igual de bien rota que entera -- y es justo lo que
   axe-core sabe encontrar.

   SE PASA POR LAS 49 SECCIONES, Y ANTES NO. Durante meses esta cabecera
   decia que miraba "la portada con sus secciones" y era mentira: la lista
   tenia dos entradas, VI.P y su banner. Cuarenta y siete secciones -- la
   ficha de producto incluida, que es donde se vende -- no habian pasado
   por axe ni una vez. El dia que se abrio la lista aparecieron tres
   infracciones graves a la primera, y ninguna estaba en VI.P.
   La leccion queda escrita aqui: una bateria que dice cubrir mas de lo que
   cubre es peor que no tenerla, porque el verde tranquiliza igual.

   Solo se miran las reglas serias (critical y serious). Las moderadas y
   menores de axe incluyen recomendaciones discutibles -- "region", por
   ejemplo, exige que todo cuelgue de un landmark, y aqui el hub vive
   dentro del <main> del tema, que la pagina de prueba si tiene pero que
   axe no siempre atribuye igual.

   Uso:  node verificadores/acceso/comprobar.mjs                          */
import { chromium } from 'playwright';
import http from 'http';
import path from 'path';
import fs from 'fs';
import { e, prepararFuente, contextoDeSeccion } from '../liquid.mjs';

const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const T = process.env.TEMA || path.join(RAIZ, 'theme');
const AXE = fs.readFileSync(path.join(RAIZ, 'node_modules/axe-core/axe.min.js'), 'utf8');
const TMP = fs.mkdtempSync('/tmp/acceso-');
const TIPO = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' };

/* Se renderiza con el MISMO motor que la bateria de secciones, no con
   sustituciones a mano. La primera version cambiaba asset_url con una
   expresion regular y se atraganto con vip-banner, que tiene bucles sobre
   bloques y condiciones de verdad: se quedo en "queda Liquid sin resolver".
   Y aunque hubiera pasado, habria medido una seccion con los ajustes
   vacios, que no es la que ve el cliente. */
async function renderizar(archivo) {
  const nombre = archivo.replace('.liquid', '');
  const src = fs.readFileSync(path.join(T, 'sections', archivo), 'utf8');
  const { ctx } = contextoDeSeccion(nombre, src);
  e.options.globals = ctx;
  let html = await e.parseAndRender(prepararFuente(src), ctx);
  /* asset_url lo devuelve el motor como //cdn/...: se reapunta al servidor
     local para que el CSS y el JavaScript de verdad se carguen. */
  html = html.replace(/\/\/cdn\/([\w.-]+)/g, '/assets/$1');
  if (/\{[%{]/.test(html)) { console.error(`  ${archivo}: queda Liquid sin resolver`); process.exit(1); }
  return html;
}

fs.mkdirSync(path.join(TMP, 'assets'), { recursive: true });
for (const a of fs.readdirSync(path.join(T, 'assets'))) fs.copyFileSync(path.join(T, 'assets', a), path.join(TMP, 'assets', a));

/* La seccion se mete en una pagina con la estructura minima de un tema:
   un <main>, un <h1> y un idioma. Sin eso, axe se queja de la pagina de
   prueba y no de la seccion, que es lo que se quiere medir. */
/* villumination.css SIEMPRE, aunque la seccion no la pida.

   Aqui hubo un falso hallazgo que conviene dejar escrito: la primera version
   no cargaba la hoja del tema, porque vip-banner.liquid no la incluye -- sus
   estilos viven en villumination.css, que carga el LAYOUT. Resultado: axe
   media un banner sin estilos, con el negro por defecto del navegador sobre
   fondo negro, y cantaba una infraccion en el boton que no describia nada
   real. Un verificador que mide una pagina que no existe es peor que no
   tenerlo: manda a arreglar lo que no esta roto.

   Y EL MISMO ERROR ESTABA REPETIDO CON EL JAVASCRIPT, dos parrafos mas
   abajo de donde se conto. base.js tambien lo carga el LAYOUT, y aqui no
   se cargaba: la bateria media el tema sin una linea de comportamiento.
   Todo lo que la accesibilidad le debe al guion -- la barra pegajosa que
   apaga su aria-hidden al aparecer, la pista de carrusel que se vuelve
   alcanzable con el teclado cuando desborda, el foco atrapado en los
   paneles -- quedaba fuera de la medida. Verde en la bateria y roto en la
   tienda, o al reves. Ahora va, con defer como en el layout, y se espera
   a que termine antes de medir. */
const envolver = (titulo, cuerpo) => `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>${titulo}</title>
<link rel="stylesheet" href="/assets/villumination.css">
<script src="/assets/base.js" defer></script>
<style>body{margin:0;font-family:system-ui;background:#0A0A0A;color:#eee}
h1.t{font-size:2rem;margin:24px 18px}</style></head><body>
<main><h1 class="t">${titulo}</h1>
${cuerpo}
</main></body></html>`;

/* La lista sale del directorio, no de la memoria de nadie: una seccion
   nueva entra en la bateria el dia que se crea, sin que haya que acordarse
   de anadirla. */
const PAGINAS = fs.readdirSync(path.join(T, 'sections'))
  .filter(f => f.endsWith('.liquid')).sort().map(f => [f.replace('.liquid', ''), f]);
for (const [titulo, arch] of PAGINAS) {
  fs.writeFileSync(path.join(TMP, arch.replace('.liquid', '.html')), envolver(titulo, await renderizar(arch)));
}

const srv = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  const f = path.join(TMP, u.replace(/^\//, ''));
  fs.readFile(f, (e, d) => {
    if (e) { res.writeHead(404); res.end('no ' + u); return; }
    res.writeHead(200, { 'content-type': TIPO[path.extname(f)] || 'application/octet-stream' });
    res.end(d);
  });
});
const base = await new Promise(r => srv.listen(0, '127.0.0.1', () => r('http://127.0.0.1:' + srv.address().port + '/')));

const CHROME = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));
const b = await chromium.launch({ executablePath: CHROME, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });

let fallos = 0;
const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
const p = await ctx.newPage();
for (const [titulo, arch] of PAGINAS) {
  await p.goto(base + arch.replace('.liquid', '.html'), { waitUntil: 'networkidle' });
  /* Se recorre la pagina entera para que arranque todo lo que carga al
     acercarse; si no, axe mediria media seccion. */
  /* Se recorre la pagina para que arranque todo lo que carga al acercarse, y
     DESPUES se espera a que las entradas terminen. axe mide el pixel: un
     elemento a mitad de su transicion de opacidad da contraste cero y sale
     como infraccion. La primera version media antes de tiempo y cantaba 928
     fallos que no existian -- eran 928 elementos todavia apareciendo. */
  await p.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    window.scrollTo(0, 0);
    const listo = () => {
      const faltan = [...document.querySelectorAll('.vp-ent')]
        .filter(e => parseFloat(getComputedStyle(e).opacity) < 0.95);
      return faltan.length === 0;
    };
    for (let i = 0; i < 40 && !listo(); i++) await new Promise(r => setTimeout(r, 150));
  });
  await p.addScriptTag({ content: AXE });
  const r = await p.evaluate(async () => await window.axe.run(document, {
    resultTypes: ['violations'],
    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] }
  }));
  const graves = r.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');

  /* REFLOW (WCAG 2.1 AA, criterio 1.4.10): a 320 px de ancho no puede
     perderse contenido por los lados. axe no lo mide -- no hay regla,
     porque depende del ancho real -- y en un movil pequeno es de lo que
     mas se nota.

     LA PRIMERA VERSION DE ESTA COMPROBACION NO SERVIA, y merece quedar
     escrito. Miraba documentElement.scrollWidth, que es lo que se mira
     normalmente... salvo que este tema lleva html,body{overflow-x:clip}
     para contener los halos y las bandas giradas de la decoracion. Con eso
     puesto, scrollWidth NUNCA supera el ancho: la pagina no se desplaza de
     lado porque lo que sobra se RECORTA. Lo probe metiendo un div de 600 px
     a la fuerza en un viewport de 320 y la comprobacion siguio en verde.
     Una comprobacion que no sabe fallar es peor que ninguna.

     Y el recorte no es mejor que el desplazamiento: es peor. Si algo se
     sale, con scroll al menos se alcanza; recortado se pierde, que es
     justo lo que 1.4.10 prohibe. Asi que no se mide la pagina, se miden
     los elementos: cuales sobresalen del viewport.

     Se descarta lo que sobresale con motivo:
       - La decoracion sin texto (halos, bordes girados, lienzos): esta ahi
         para salirse, y no se pierde nada al recortarla.
       - Lo que vive dentro de algo que SI se desplaza -- un carrusel --
         porque ahi se llega desplazando esa pista.
       - Lo que vive dentro de una marquesina: una cinta con animacion
         infinita esta hecha para ser mas ancha que la pantalla, y el texto
         no se pierde porque pasa por delante solo. flowing-menu y marquee
         daban 2116 y 31 px de "desborde" por esto. */
  await p.setViewportSize({ width: 320, height: 800 });
  await p.waitForTimeout(250);
  const reflow = await p.evaluate(() => {
    const w = document.documentElement.clientWidth;
    const enPistaDesplazable = (e) => {
      for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
        const cs = getComputedStyle(a);
        if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') return true;
        if (cs.animationName !== 'none' && cs.animationIterationCount === 'infinite') return true;
      }
      return false;
    };
    let peor = null;
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) continue;
      /* Solo cuenta lo que se puede perder: texto propio, o algo que se usa. */
      const texto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
      const util = texto || /^(a|button|input|select|textarea|img)$/.test(e.tagName.toLowerCase());
      if (!util) continue;
      if (enPistaDesplazable(e)) continue;
      const r = e.getBoundingClientRect();
      if (r.width < 1 || r.height < 1) continue;
      const sale = Math.round(Math.max(r.right - w, -r.left));
      if (sale > 1 && (!peor || sale > peor.sale)) {
        peor = { sale: sale, que: e.tagName.toLowerCase() +
          (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : ''),
          txt: (e.textContent || '').trim().slice(0, 40) };
      }
    }
    return peor;
  });
  await p.setViewportSize({ width: 390, height: 844 });

  console.log(`\n--- ${titulo} ---`);
  if (reflow) {
    fallos++;
    console.log(`  FALLA [serious] reflow: a 320 px de ancho hay contenido recortado por el borde (WCAG 1.4.10)`);
    console.log(`        se sale ${reflow.sale} px: ${reflow.que.slice(0, 110)}  «${reflow.txt}»`);
  }
  if (!graves.length && !reflow) console.log('  OK    sin infracciones graves de WCAG 2.1 AA, y no se desplaza de lado a 320 px');
  for (const v of graves) {
    fallos++;
    console.log(`  FALLA [${v.impact}] ${v.id}: ${v.help}  (${v.nodes.length} elemento(s))`);
    for (const n of v.nodes.slice(0, 3)) console.log('        ' + n.html.replace(/\s+/g, ' ').slice(0, 120));
  }
  const leves = r.violations.filter(v => v.impact !== 'critical' && v.impact !== 'serious');
  if (leves.length) console.log('  (' + leves.map(v => v.id + '×' + v.nodes.length).join(', ') + ' — impacto moderado o menor, no cuentan)');
}
await ctx.close();

await b.close(); srv.close(); fs.rmSync(TMP, { recursive: true, force: true });
console.log(fallos ? `\n  ${fallos} infraccion(es) grave(s)` : '\nNadie se queda fuera: ni un fallo grave de WCAG 2.1 AA.');
process.exit(fallos ? 1 : 0);
