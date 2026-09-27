/* Los textos que el comerciante escribe en el editor de Shopify.
   ------------------------------------------------------------------
   POR QUE EXISTE ESTA BATERIA. Las demas vigilan los ficheros de idioma del
   tema (locales/*.json). Pero lo que se teclea en el editor NO vive ahi: vive
   en config/settings_data.json, y sus traducciones viven en Shopify, fuera del
   repositorio. Ninguna bateria podia verlo.

   Ese agujero dejo salir a produccion el lema de la intro -- lo PRIMERO que
   lee quien llega -- en castellano para el visitante frances, aleman y
   japones. Cuatro idiomas, en la primera pantalla, con dinero de anuncios
   detras. No lo encontro ningun detector: lo vio el cliente en una captura.

   QUE COMPRUEBA.
     1. Que todo ajuste de texto con valor este declarado en
        marca/ajustes-de-texto.json. Si alguien escribe un lema nuevo en el
        editor y se olvida de traducirlo, la compuerta se pone roja.
     2. Que el castellano del manifiesto siga siendo el del tema. Si alguien
        cambia la frase y no toca el manifiesto, las traducciones se quedan
        hablando de otra cosa, que es peor que no tenerlas.
     3. Que lo declarado traducible traiga los cinco idiomas, sin huecos.
     4. Que lo declarado NO traducible diga POR QUE. Callarlo no vale: la
        proxima persona tiene que poder distinguir "es un nombre propio" de
        "se me olvido".

   QUE NO COMPRUEBA, Y HAY QUE DECIRLO. No mira si las traducciones estan
   REGISTRADAS en Shopify contra el tema que toque: eso vive fuera del
   repositorio y cambia con cada tema nuevo. Lo que garantiza es que el texto
   existe y esta traducido en el manifiesto, que es de donde salen los
   translationsRegister.

   Uso:  node verificadores/ajustes/comprobar.mjs                           */
import fs from 'fs';
import path from 'path';

const RAIZ = path.dirname(path.dirname(path.dirname(new URL(import.meta.url).pathname)));
const TEMA = path.join(RAIZ, 'theme');

const IDIOMAS = ['es', 'en', 'fr', 'de', 'ja'];

/* Los tipos de ajuste que llevan prosa. Un color, un numero o una casilla no
   se traducen; un "text" o un "textarea" con valor, casi siempre si. */
const PROSA = new Set(['text', 'textarea', 'richtext', 'html', 'inline_richtext']);

const esquema = JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_schema.json'), 'utf8'));
const datos = JSON.parse(fs.readFileSync(path.join(TEMA, 'config/settings_data.json'), 'utf8')).current;
const manifiesto = JSON.parse(fs.readFileSync(path.join(RAIZ, 'marca/ajustes-de-texto.json'), 'utf8'));

const tipoDe = {};
for (const grupo of esquema) for (const s of (grupo.settings || [])) if (s.id) tipoDe[s.id] = s.type;

const fallos = [];
const bien = [];

/* --- 1. todo ajuste de texto con valor tiene que estar declarado --------- */
const conValor = [];
for (const [id, valor] of Object.entries(datos)) {
  if (typeof valor !== 'string' || !valor.trim()) continue;
  if (!PROSA.has(tipoDe[id])) continue;
  conValor.push(id);
  if (!manifiesto['general.' + id]) {
    fallos.push('SIN DECLARAR  general.' + id + ' = ' + JSON.stringify(valor.slice(0, 70)) +
                '\n              Alguien escribio esto en el editor y no paso por ' +
                'marca/ajustes-de-texto.json.\n              O se traduce a los cinco idiomas, o se dice ahi por que no.');
  }
}

/* --- 2. el castellano del manifiesto es el del tema ---------------------- */
for (const [clave, ficha] of Object.entries(manifiesto)) {
  if (clave.startsWith('_')) continue;
  const id = clave.replace(/^general\./, '');
  const enTema = datos[id];
  if (enTema === undefined) {
    fallos.push('SOBRA        ' + clave + ' esta en el manifiesto pero ya no existe en los ajustes del tema.');
    continue;
  }
  if (ficha.es !== enTema) {
    fallos.push('NO CUADRA    ' + clave +
                '\n              manifiesto: ' + JSON.stringify(ficha.es) +
                '\n              tema:       ' + JSON.stringify(enTema) +
                '\n              Si la frase cambio, las traducciones de al lado hablan de otra cosa.');
    continue;
  }

  /* --- 3 y 4. traducible con los cinco, o no traducible con su motivo --- */
  if (ficha.traduce === true) {
    const faltan = IDIOMAS.filter((l) => !ficha[l] || !String(ficha[l]).trim());
    if (faltan.length) {
      fallos.push('SIN TRADUCIR ' + clave + ' no tiene ' + faltan.join(', ') +
                  '\n              ' + JSON.stringify(ficha.es));
    } else {
      const iguales = IDIOMAS.filter((l) => l !== 'es' && ficha[l] === ficha.es);
      if (iguales.length) {
        fallos.push('SIN TRADUCIR ' + clave + ': ' + iguales.join(', ') +
                    ' son identicos al castellano.\n              ' + JSON.stringify(ficha.es) +
                    '\n              Si de verdad se escribe igual, declaralo con traduce:false y di por que.');
      } else {
        bien.push(clave + '  (' + IDIOMAS.length + ' idiomas)');
      }
    }
  } else if (ficha.traduce === false) {
    if (!ficha.porque || !String(ficha.porque).trim()) {
      fallos.push('SIN MOTIVO   ' + clave + ' se declara no traducible pero no dice por que.' +
                  '\n              Callarlo no vale: hay que poder distinguir "es un nombre propio" de "se me olvido".');
    } else {
      bien.push(clave + '  (no se traduce: ' + ficha.porque.slice(0, 58) + (ficha.porque.length > 58 ? '...' : '') + ')');
    }
  } else {
    fallos.push('SIN DECIDIR  ' + clave + ' no dice si se traduce o no (falta "traduce": true/false).');
  }
}

console.log('\n--- los textos que se escriben en el editor de Shopify ---');
console.log('  ' + conValor.length + ' ajustes de texto con valor · ' +
            Object.keys(manifiesto).filter((k) => !k.startsWith('_')).length + ' declarados en el manifiesto\n');

for (const b of bien) console.log('  OK    ' + b);

if (fallos.length) {
  console.log('');
  for (const f of fallos) console.log('  FALLO ' + f);
  console.log('\n' + fallos.length + ' fallo(s). Se arreglan en marca/ajustes-de-texto.json.');
  process.exit(1);
}

console.log('\nTodo texto del editor esta declarado, cuadra con el tema, y o esta en los cinco idiomas o dice por que no.');
