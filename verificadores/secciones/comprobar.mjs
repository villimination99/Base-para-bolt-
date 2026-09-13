/* Renderiza TODAS las secciones del tema con sus ajustes por defecto.
   ------------------------------------------------------------------
   Nace de una trampa que he pisado varias veces: pasarle a una seccion un
   section.settings vacio en vez de los "default" de su esquema. Shopify SI
   aplica esos valores por defecto a todo ajuste que la plantilla no guarda,
   asi que probar con {} deja partes enteras sin ejercitar. En la ficha de
   producto se quedaban fuera la barra pegajosa y los botones de compartir:
   unas cien lineas que parecian probadas y no lo estaban. Con los valores
   correctos el renderizado paso de 3.533 a 6.453 caracteres.

   Comprueba, por cada seccion:
     - que renderiza sin reventar,
     - que las etiquetas de apertura y cierre cuadran,
     - que no quedan restos de Liquid sin procesar en la salida.

   No sustituye a los verificadores especificos: es la red de seguridad ancha
   que atrapa el fallo tonto en una seccion que nadie estaba mirando.

   Uso:  node verificadores/secciones/comprobar.mjs                         */
import fs from 'fs';
import { e, T, prepararFuente, contextoDeSeccion } from '../liquid.mjs';

const secciones = fs.readdirSync(`${T}/sections`).filter(f => f.endsWith('.liquid')).sort();
let fallos = 0;
console.log('');

for (const archivo of secciones) {
  const nombre = archivo.replace('.liquid', '');
  const src = fs.readFileSync(`${T}/sections/${archivo}`, 'utf8');
  const m = src.match(/\{%\s*schema\s*%\}([\s\S]*?)\{%\s*endschema\s*%\}/);

  /* Los ajustes y bloques salen del esquema, que es lo que da sentido a esta
     prueba. Lo hace el modulo compartido. */
  let esquema, ctx, ajustes, bloques;
  try { ({ esquema, ctx, ajustes, bloques } = contextoDeSeccion(nombre, src)); }
  catch (err) { console.log(`FALLA  ${nombre.padEnd(24)} el esquema no es JSON valido: ${err.message}`); fallos++; continue; }
  e.options.globals = ctx;

  let html;
  try { html = await e.parseAndRender(prepararFuente(src), ctx); }
  catch (err) { console.log(`FALLA  ${nombre.padEnd(24)} revienta: ${String(err.message).split('\n')[0].slice(0, 80)}`); fallos++; continue; }

  const par = /<(div|form|button|ul|ol|li|span|p|a|section|label|select|option|aside|nav|footer|header|h1|h2|h3|h4|table|tr|td|th|figure|picture|video|details|summary)\b/g;
  const cierre = /<\/(div|form|button|ul|ol|li|span|p|a|section|label|select|option|aside|nav|footer|header|h1|h2|h3|h4|table|tr|td|th|figure|picture|video|details|summary)>/g;
  /* Los comentarios HTML NO cuentan. Un comentario puede describir marcado
     -- "esto era un <h1> y ahora es un <p>, y aqui esta el porque" -- y eso es
     documentacion, no etiquetas. Contarlo daba un falso positivo: la seccion
     del hub salia con "h1 +3 sin cerrar" por tres menciones dentro de un
     comentario, cuando el marcado real no tiene ni un h1. Un verificador que
     avisa de lo que no pasa entrena a que se le ignore. */
  html = html.replace(/<!--[\s\S]*?-->/g, '');
  const ab = (html.match(par) || []).length, ci = (html.match(cierre) || []).length;
  const resto = html.match(/\{\{|\{%/);

  const problemas = [];

  /* Con la seccion ya renderizada se puede mirar lo que de verdad llega al
     navegador, no lo que parece en el codigo. Un alt que sale de una variable
     vacia, un boton cuyo unico contenido es un icono, un aria-labelledby que
     apunta a un id que solo existe en otra rama del if: nada de eso se ve
     leyendo el Liquid. */
  for (const im of html.matchAll(/<img\b[^>]*>/g)) {
    if (!/\salt=/.test(im[0]))
      problemas.push('una imagen sin alt');
  }
  // Botones y enlaces sin nombre accesible: ni texto, ni aria-label, ni title,
  // ni una imagen con alt dentro.
  for (const ctrl of html.matchAll(/<(button|a)\b([^>]*)>([\s\S]*?)<\/\1>/g)) {
    const [, et, attrs, dentro] = ctrl;
    if (et === 'a' && !/\shref=/.test(attrs)) continue;
    if (/aria-hidden="true"/.test(attrs)) continue;
    const texto = dentro.replace(/<[^>]*>/g, '').trim();
    const etiqueta = /aria-label=|title=|aria-labelledby=/.test(attrs);
    const imgConAlt = /<img[^>]*\salt="[^"]+"/.test(dentro);
    if (!texto && !etiqueta && !imgConAlt)
      problemas.push(`un <${et}> sin nombre accesible: ${ctrl[0].replace(/\s+/g,' ').slice(0,110)}`);
  }
  // Referencias aria y for que apuntan a un id que no existe en la seccion
  const ids = new Set([...html.matchAll(/\sid="([^"]+)"/g)].map(x => x[1]));
  for (const ref of html.matchAll(/\s(for|aria-labelledby|aria-describedby|aria-controls)="([^"]+)"/g)) {
    for (const id of ref[2].split(/\s+/)) {
      if (id && !ids.has(id)) problemas.push(`${ref[1]}="${id}" apunta a un id que no existe`);
    }
  }
  // Ids repetidos dentro de la misma seccion
  const vistos = {}, repes = [];
  for (const x of html.matchAll(/\sid="([^"]+)"/g)) {
    vistos[x[1]] = (vistos[x[1]] || 0) + 1;
    if (vistos[x[1]] === 2) repes.push(x[1]);
  }
  for (const r of repes) problemas.push(`id repetido: ${r}`);

  if (ab !== ci) {
    // Decir CUAL descuadra, no solo que algo descuadra: sin esto hay que
    // volcar el HTML entero a mano para averiguarlo.
    const cuenta = {};
    for (const m2 of html.matchAll(/<(\/?)([a-z][a-z0-9]*)\b/g)) {
      const [, cierra, et] = m2;
      if (!/^(div|form|button|ul|ol|li|span|p|a|section|label|select|option|aside|nav|footer|header|h1|h2|h3|h4|table|tr|td|th|figure|picture|video|details|summary)$/.test(et)) continue;
      cuenta[et] = (cuenta[et] || 0) + (cierra ? -1 : 1);
    }
    const desc = Object.entries(cuenta).filter(([, v]) => v !== 0)
      .map(([k, v]) => `${k}${v > 0 ? ' +' + v + ' sin cerrar' : ' ' + v + ' de mas'}`);
    problemas.push(`etiquetas ${ab}/${ci}: ${desc.join(', ')}`);
  }
  if (resto) problemas.push('queda Liquid sin procesar');
  const resumen = [...new Set(problemas)].map(x => {
    const n = problemas.filter(y => y === x).length;
    return n > 1 ? `${x} (x${n})` : x;
  });
  if (resumen.length) fallos++;
  console.log(`${resumen.length ? 'FALLA ' : ' OK   '} ${nombre.padEnd(24)} ${String(html.length).padStart(6)} car · ${bloques.length} bloque(s) · ${Object.keys(ajustes).length} ajuste(s)${resumen.length ? '  ' + resumen.join(' | ') : ''}`);
}

console.log('');
console.log(fallos === 0
  ? `Las ${secciones.length} secciones renderizan con sus valores por defecto.`
  : `${fallos} de ${secciones.length} secciones con problemas.`);
process.exit(fallos ? 1 : 0);
