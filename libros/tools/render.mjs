/**
 * Renderizador de libros. Se usa Playwright en vez de Chromium a secas porque
 * los libros necesitan numeración de página real en el pie, y eso solo se
 * puede controlar con footerTemplate.
 *
 * Uso:  node tools/render.mjs <html> <pdf> <color-del-folio> [titulillo]
 */
import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;

const [html, pdf, color = '#7c766c', titulillo = '', modo = ''] = process.argv.slice(2);
const sangre = modo === 'sangre';

const navegador = await chromium.launch();
const pagina = await navegador.newPage();
await pagina.goto('file://' + html, { waitUntil: 'networkidle' });
await pagina.evaluate(() => document.fonts.ready);

const pie = `
  <div style="width:100%;padding:0 17mm;font-family:'Helvetica',sans-serif;
              font-size:7pt;color:${color};display:flex;
              justify-content:space-between;align-items:center;">
    <span style="letter-spacing:.08em;opacity:.75">${titulillo}</span>
    <span style="font-weight:700"><span class="pageNumber"></span></span>
  </div>`;

await pagina.pdf(sangre
  ? {   // cubierta: sin márgenes, el fondo llega al borde del papel
      path: pdf, width: '148mm', height: '210mm',
      printBackground: true, pageRanges: '1',
      margin: { top: '0', bottom: '0', left: '0', right: '0' },
    }
  : {   // interior: márgenes de lectura y folio en el pie
      path: pdf, format: 'A5', printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: pie,
      margin: { top: '20mm', bottom: '18mm', left: '17mm', right: '17mm' },
    });

await navegador.close();
