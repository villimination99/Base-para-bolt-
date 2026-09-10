/* Mide en un navegador real si algo se sale de su caja o se recorta.
   Recorre las paginas de prueba a varios anchos de telefono y falla si
   encuentra un elemento fuera del ancho util o un texto cortado. */
import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const PAGINAS = ['componentes.html', 'vip.html', 'secciones.html'];
/* 900 y 1200 son FRONTERAS de la hoja de estilos, y las fronteras es donde se
   rompen las cosas: justo en 900 empieza la fila de cifras del banner y justo
   en 1200 vuelven a ser cinco. 1024 es el iPad apaisado, que no es ninguna de
   las dos y es de los tamanos que mas visitan una tienda. */
const ANCHOS = [320, 375, 390, 768, 900, 1024, 1200, 1440];

const navegador = await chromium.launch({
  executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
});

let fallos = 0;
for (const pagina of PAGINAS) {
  for (const ancho of ANCHOS) {
    const p = await navegador.newPage({ viewport: { width: ancho, height: 900 }, isMobile: ancho < 500 });
    await p.goto('file://' + path.join(AQUI, pagina));
    await p.waitForTimeout(200);
    const malos = await p.evaluate(() => {
      const vw = document.documentElement.clientWidth;
      const out = [];
      // Los fondos decorativos se salen a proposito y un ancestro los recorta:
      // el borde giratorio del banner VIP mide -60% de inset porque tiene que
      // desbordar. Lo que NO puede salirse es algo que lleva texto, porque
      // entonces se pierden palabras. El criterio es ese, y no "tiene un
      // ancestro que recorta": con ese, el verificador se tragaba el propio
      // fallo de la tira de cifras, que estaba dentro de un contenedor con
      // overflow:hidden y aun asi perdia texto por los lados.
      const decorativo = e => {
        if (e.getAttribute('aria-hidden') === 'true') return true;
        if ((e.textContent || '').trim() !== '') return false;
        return true; // sin texto: nada que perder
      };
      /* UN CARRIL NO ES UN DESBORDE. La tira de cifras del banner VIP es, en
         movil, un carril que se desliza con el dedo: overflow-x:auto,
         scroll-snap y sin barra visible. Sus celdas se salen de la ventana a
         proposito y se alcanzan deslizando, igual que en cualquier carrusel.
         Marcarlas era acusar al diseno de un fallo que no tiene.

         Lo que NO se perdona sigue siendo overflow:hidden, que es recortar de
         verdad: ahi el texto que se sale no lo alcanza nadie. Esa distincion
         es justo la que faltaba, y no la de antes ("tiene un ancestro que
         recorta"), que se tragaba el fallo de verdad de esta misma tira. */
      const enUnCarril = e => {
        for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
          const o = getComputedStyle(a);
          const desliza = /auto|scroll/.test(o.overflowX) || /auto|scroll/.test(o.overflowY);
          if (desliza && a.scrollWidth > a.clientWidth + 1) return true;
        }
        return false;
      };
      for (const e of document.querySelectorAll('body *')) {
        const r = e.getBoundingClientRect();
        if (!r.width) continue;
        const nombre = (typeof e.className === 'string' && e.className.split(' ')[0]) || e.tagName;
        if ((r.right > vw + 1 || r.left < -1) && !decorativo(e) && !enUnCarril(e)) out.push(`${nombre} se sale ${Math.round(Math.max(r.right - vw, -r.left))}px`);
        else if (!e.children.length && e.scrollWidth > e.clientWidth + 1
                 && getComputedStyle(e).textOverflow !== 'ellipsis') out.push(`${nombre} texto recortado`);
      }
      if (document.documentElement.scrollWidth > vw + 1) out.push('la pagina tiene scroll lateral');
      return [...new Set(out)];
    });
    if (malos.length) { fallos += malos.length; console.log(`FALLA  ${pagina} @${ancho}px`); malos.slice(0, 5).forEach(m => console.log('        ' + m)); }
    else console.log(` OK    ${pagina} @${ancho}px`);
    await p.close();
  }
}
await navegador.close();
console.log(fallos ? `\n${fallos} problemas de desbordamiento.` : '\nNada se sale de su caja.');
process.exit(fallos ? 1 : 0);
