/* Escribe la rama "inicio" de los cinco locales a partir de una sola fuente.
   ------------------------------------------------------------------
   POR QUE EXISTE ESTO. La copia de la portada vivia en templates/index.json,
   que para Shopify es contenido del comerciante: se traduce con registros
   POR TEMA, y esos registros no sobreviven a subir un tema nuevo. Se
   comprobo contra la tienda: translations:[] en 4-61-1, en 4-61-0 y en
   4-60-0. Un visitante en frances veia la interfaz en frances y la portada
   entera en espanol.

   Los locales SI son archivos del tema: viajan dentro del zip, estan en git
   y no hay nada que volver a registrar despues de cada subida.

   La fuente es marca/copia-portada.json, con los cinco idiomas juntos: asi
   se ve de un vistazo si a una frase le falta un idioma, en vez de tener
   que abrir cinco archivos y compararlos a mano.

   Uso:  node marca/generar-copia.mjs                                      */
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const FUENTE = path.join(RAIZ, 'marca/copia-portada.json');
const LOCALES = { es: 'es.json', en: 'en.default.json', fr: 'fr.json', de: 'de.json', ja: 'ja.json' };

const copia = JSON.parse(fs.readFileSync(FUENTE, 'utf8'));
const idiomas = Object.keys(LOCALES);

/* Primero se comprueba que no falte ningun idioma en ninguna frase. Un
   hueco aqui saldria en la tienda como texto en espanol en medio de una
   pagina en aleman, que es exactamente lo que se viene a arreglar. */
const huecos = [];
for (const grupo of Object.keys(copia)) {
  if (grupo.startsWith('_')) continue;
  for (const bloque of Object.keys(copia[grupo])) {
    for (const ajuste of Object.keys(copia[grupo][bloque])) {
      const v = copia[grupo][bloque][ajuste];
      for (const i of idiomas) {
        if (typeof v[i] !== 'string' || !v[i].trim()) huecos.push(`${grupo}.${bloque}.${ajuste} → ${i}`);
      }
    }
  }
}
if (huecos.length) {
  console.error('  Faltan traducciones:');
  for (const h of huecos) console.error('   ' + h);
  process.exit(1);
}

let claves = 0;
for (const [idioma, archivo] of Object.entries(LOCALES)) {
  const ruta = path.join(RAIZ, 'theme/locales', archivo);
  const loc = JSON.parse(fs.readFileSync(ruta, 'utf8'));
  const rama = {};
  for (const grupo of Object.keys(copia)) {
    if (grupo.startsWith('_')) continue;
    rama[grupo] = {};
    for (const bloque of Object.keys(copia[grupo])) {
      rama[grupo][bloque] = {};
      for (const ajuste of Object.keys(copia[grupo][bloque])) {
        rama[grupo][bloque][ajuste] = copia[grupo][bloque][ajuste][idioma];
        if (idioma === 'es') claves++;
      }
    }
  }
  loc.inicio = rama;
  fs.writeFileSync(ruta, JSON.stringify(loc, null, 2) + '\n');
}
console.log(`  ${claves} claves escritas en los ${idiomas.length} locales (${claves * idiomas.length} traducciones)`);
