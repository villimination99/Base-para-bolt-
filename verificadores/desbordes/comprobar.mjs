/* Mide en un navegador real si algo se sale de su caja o se recorta.
   Recorre las paginas de prueba a varios anchos de telefono y falla si
   encuentra un elemento fuera del ancho util o un texto cortado. */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const PAGINAS = ['componentes.html', 'vip.html', 'secciones.html'];
/* 900 y 1200 son FRONTERAS de la hoja de estilos, y las fronteras es donde se
   rompen las cosas: justo en 900 empieza la fila de cifras del banner y justo
   en 1200 vuelven a ser cinco. 1024 es el iPad apaisado, que no es ninguna de
   las dos y es de los tamanos que mas visitan una tienda. */
const ANCHOS = [320, 375, 390, 768, 900, 1024, 1200, 1440];

let fallos = 0;

/* ---- EL BANCO DE PRUEBAS TIENE QUE SER EL TEMA ----
   Estas paginas se escriben a mano, y eso las deja libres de separarse del
   tema sin que nadie se entere. Paso: el pie llevaba los enlaces sueltos
   cuando el tema los pone dentro de <ul><li>, el testimonio usaba clases de
   hace rondas (testimonial-author en vez de testi-author) y el indice de
   colecciones inventaba col-index-name. Medir eso no es medir la tienda.

   Aqui se comprueba que CADA clase que usan estas paginas existe de verdad en
   el tema -- en su marcado o en su hoja de estilos. Una clase que no esta en
   ningun sitio no la ha visto nunca un cliente. */
{
  const T = process.env.TEMA || path.join(AQUI, '../../theme');
  const propias = new Set(['probe']);   // andamiaje de estas paginas
  const delTema = new Set();
  const recorrer = (d) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const f = path.join(d, e.name);
      if (e.isDirectory()) { recorrer(f); continue; }
      if (!/\.(liquid|css|js|json)$/.test(e.name)) continue;
      const txt = fs.readFileSync(f, 'utf8');
      /* De la hoja de estilos, los selectores de clase. Del marcado, lo que
         hay dentro de los atributos class -- que es donde estan de verdad.
         Nada de buscar la palabra suelta por el archivo: asi "author" en un
         comentario daria por buena una clase que no existe. */
      if (f.endsWith('.css')) {
        for (const m of txt.matchAll(/\.(-?[A-Za-z_][\w-]*)/g)) delTema.add(m[1]);
      } else {
        for (const m of txt.matchAll(/class\s*=\s*(['"])([\s\S]*?)\1/g))
          for (const c of m[2].split(/\s+/)) if (/^[A-Za-z][\w-]*$/.test(c)) delTema.add(c);
        /* Y las que el JavaScript del tema anade o quita a mano. */
        for (const m of txt.matchAll(/classList\.(?:add|remove|toggle|contains)\(\s*['"]([\w-]+)/g)) delTema.add(m[1]);
      }
    }
  };
  recorrer(T);
  const huerfanas = new Set();
  for (const pagina of PAGINAS) {
    const html = fs.readFileSync(path.join(AQUI, pagina), 'utf8');
    for (const m of html.matchAll(/class="([^"]+)"/g))
      for (const c of m[1].split(/\s+/))
        if (c && !propias.has(c) && !delTema.has(c)) huerfanas.add(`${pagina}: .${c}`);
  }
  const ok = huerfanas.size === 0;
  if (!ok) fallos += huerfanas.size;
  console.log(`${ok ? ' OK   ' : 'FALLA '} el banco usa ${ok ? 'solo' : ''} clases que existen en el tema` +
    (ok ? '' : `: ${[...huerfanas].slice(0, 6).join(' · ')}`));
}

const navegador = await chromium.launch({
  executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
});

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

      /* ---- DOS TEXTOS NO PUEDEN OCUPAR EL MISMO SITIO ----
         Esto nace de una captura del cliente: en la intro, el nombre de la
         tienda, la esfera y la frase de motivacion pintados unos encima de
         otros. Alli se arreglo y se le puso bateria propia; aqui se extiende
         el mismo ojo a TODAS las secciones, porque el fallo no era de la
         intro: era de que nadie miraba si dos cosas caen en el mismo sitio.

         Se comparan solo HOJAS CON TEXTO -- elementos sin hijos y con letras
         dentro -- porque un contenedor solapa a sus hijos por definicion y
         los adornos no pierden nada al taparse. Se descartan ademas:
           - lo que esta oculto o transparente,
           - lo que es decorativo (aria-hidden),
           - lo que vive dentro de un carril que se desliza o de un carrusel,
             donde las tarjetas se apilan a proposito,
           - y los pares padre/hijo, por si algun nodo se cuela.
         El umbral es de 4 px en los dos ejes: por debajo de eso son bordes
         que se rozan, no texto perdido. */
      const texto = [];
      for (const e of document.querySelectorAll('body *')) {
        if (e.children.length) continue;
        if (!(e.textContent || '').trim()) continue;
        if (e.closest('[aria-hidden="true"]')) continue;
        if (e.closest('[data-carousel], .carousel, .carousel-track, [data-splash]')) continue;
        const c = getComputedStyle(e);
        if (c.visibility === 'hidden' || c.display === 'none' || parseFloat(c.opacity) < 0.1) continue;
        const r = e.getBoundingClientRect();
        if (r.width < 4 || r.height < 4) continue;
        /* Un carril que se desliza apila a proposito lo que no cabe. */
        let enCarril = false;
        for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
          const o = getComputedStyle(a);
          if (/auto|scroll/.test(o.overflowX) && a.scrollWidth > a.clientWidth + 1) { enCarril = true; break; }
        }
        if (enCarril) continue;
        /* LOS RECTANGULOS, UNO POR LINEA, Y NO LA CAJA QUE LOS ENVUELVE.
           Un enlace que ocupa dos lineas devuelve en getBoundingClientRect
           una caja que cubre las dos y todo el hueco del final de la primera
           -- hueco donde cabe perfectamente el texto siguiente sin tocar una
           sola letra. Con la caja envolvente, esta comprobacion acusaba a la
           fila del carrito de un solape que no existe. getClientRects da una
           caja POR LINEA, que es lo que de verdad pinta el navegador. */
        const cajas = [...e.getClientRects()].filter(c => c.width > 3 && c.height > 3);
        texto.push({ e, cajas: cajas.length ? cajas : [r],
                     n: (typeof e.className === 'string' && e.className.split(' ')[0]) || e.tagName });
      }
      for (let i = 0; i < texto.length; i++) {
        for (let j = i + 1; j < texto.length; j++) {
          const A = texto[i], B = texto[j];
          if (A.e.contains(B.e) || B.e.contains(A.e)) continue;
          let peor = null;
          for (const ca of A.cajas) for (const cb of B.cajas) {
            const dx = Math.min(ca.right, cb.right) - Math.max(ca.left, cb.left);
            const dy = Math.min(ca.bottom, cb.bottom) - Math.max(ca.top, cb.top);
            if (dx > 4 && dy > 4 && (!peor || dx * dy > peor.dx * peor.dy)) peor = { dx, dy };
          }
          if (peor) out.push(`${A.n} y ${B.n} se pisan ${Math.round(peor.dx)}x${Math.round(peor.dy)}px`);
        }
      }
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
