/**
 * Verifica que ninguna página se desborde.
 *
 * Las páginas tienen altura fija y overflow:hidden, así que el contenido que
 * sobra no se ve — o peor, empuja el pie y se solapa con él. Comprobar que el
 * pie «existe» en el PDF no basta: hay que medir en el navegador.
 *
 * Uso:  node tools/verificar.mjs build/*.html
 */
import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;

const archivos = process.argv.slice(2);
const navegador = await chromium.launch();
const pagina = await navegador.newPage();

let fallos = 0;
for (const archivo of archivos) {
  await pagina.goto('file://' + archivo, { waitUntil: 'networkidle' });
  await pagina.evaluate(() => document.fonts.ready);

  const problemas = await pagina.evaluate(() => {
    const salida = [];
    document.querySelectorAll('section.page').forEach((seccion, i) => {
      const main = seccion.querySelector('main');
      if (!main) return;
      const sobra = main.scrollHeight - main.clientHeight;
      if (sobra > 2) salida.push({ pagina: i + 1, sobra: Math.round(sobra) });
    });
    return salida;
  });

  // Con tres idiomas, el nombre del archivo ya no basta: 07-…-hiit.html existe
  // en build/, build/en/ y build/fr/, y saber en cuál desborda es medio arreglo.
  const partes = archivo.split('/');
  const carpeta = partes[partes.length - 2];
  const idioma = (carpeta === 'en' || carpeta === 'fr') ? carpeta : 'es';
  const nombre = `[${idioma}] ` + partes[partes.length - 1];
  if (problemas.length) {
    fallos += problemas.length;
    for (const p of problemas) {
      console.log(`  DESBORDA  ${nombre}  pág. ${p.pagina}  →  sobran ${p.sobra} px`);
    }
  }
}

await navegador.close();
console.log(fallos ? `\n${fallos} página(s) con desbordamiento.` : 'Sin desbordamientos.');
process.exit(fallos ? 1 : 0);
