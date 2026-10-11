// Compuerta de las politicas. Ningun texto sale de aqui con un hueco sin
// rellenar. Esta bateria existe porque una vez se entregaron dos marcadores
// mios —‹NEQ...› y ‹TPS/TVQ...›— dentro del texto listo para pegar, y se
// publicaron tal cual en la tienda. No puede volver a pasar sin que salte.
import fs from 'node:fs';
import path from 'node:path';

const AQUI = path.dirname(new URL(import.meta.url).pathname);

const TRAMPAS = [
  [/[‹›]/, 'un marcador entre guillemets simples'],
  [/\[(INSERT|LINK|NOTE|TODO)\b/i, 'un corchete de plantilla'],
  [/DIRECCION_COMPLETA|NUMERO_EMPRESA|NUMERO_TVA|NOMBRE_COMERCIAL/, 'una variable sin sustituir'],
  [/\bXX+\b|\bTBD\b|\bLOREM\b/i, 'un relleno provisional'],
  [/\bno aplica\b/i, 'el marcador "no aplica"'],
  [/&[a-z]+;|&#\d+;/, 'una entidad HTML sin decodificar'],
  [/[ \t]+$/m, 'un espacio al final de una linea'],
  [/\n{3,}/, 'tres saltos de linea seguidos'],
];

// Lo que tiene que aparecer, y en que archivo.
const OBLIGATORIO = {
  'informacion-de-contacto.txt': [
    [/^VILLUMINATIONS$/m, 'el nombre de la marca'],
    [/183 Rue Édouard-Rousseau\nGranby \(Quebec\) J2H 0A6\nCanadá/, 'la direccion completa'],
    [/villumination@outlook\.com/, 'el correo'],
    [/\+1 450 558-7463/, 'el telefono'],
  ],
  'aviso-legal.txt': [
    [/183 Rue Édouard-Rousseau, Granby \(Quebec\) J2H 0A6, Canadá/, 'la direccion completa en el punto 1'],
    [/ECC-Net/, 'la via de reclamacion que si existe'],
    [/dos años desde la entrega/, 'la garantia legal de la UE'],
  ],
  'condiciones-del-servicio.txt': [
    [/183 Rue Édouard-Rousseau\nGranby \(Quebec\) J2H 0A6\nCanadá/, 'la direccion completa en la seccion 25'],
    [/\/policies\/privacy-policy/, 'el enlace a la privacidad'],
    [/\/policies\/refund-policy/, 'el enlace al reembolso'],
    [/\/policies\/shipping-policy/, 'el enlace al envio'],
  ],
};

// Lo que NO puede aparecer nunca mas.
const PROHIBIDO = [
  [/plataforma europea de resoluci/i, 'la plataforma europea de litigios, apagada el 20 de julio de 2025'],
  [/All sales are final/i, 'la frase inglesa que contradecia la politica de reembolso'],
  [/VIllumination\b/, 'el nombre viejo de la tienda'],
];

let fallos = 0;
const aviso = (m) => { console.log('  FALLA  ' + m); fallos++; };

for (const archivo of Object.keys(OBLIGATORIO)) {
  const ruta = path.join(AQUI, archivo);
  if (!fs.existsSync(ruta)) { aviso(archivo + ': no existe'); continue; }
  const t = fs.readFileSync(ruta, 'utf8');

  for (const [re, que] of TRAMPAS) {
    const m = t.match(re);
    if (m) aviso(archivo + ': queda ' + que + ' -> ' + JSON.stringify(m[0]));
  }
  for (const [re, que] of PROHIBIDO) {
    if (re.test(t)) aviso(archivo + ': sigue ' + que);
  }
  for (const [re, que] of OBLIGATORIO[archivo]) {
    if (!re.test(t)) aviso(archivo + ': falta ' + que);
  }
  console.log('  ' + archivo.padEnd(30) + String(t.length).padStart(6) + ' bytes');
}

// Las condiciones tienen que traer sus 25 secciones, enteras y en orden.
const ts = fs.readFileSync(path.join(AQUI, 'condiciones-del-servicio.txt'), 'utf8');
const secs = [...ts.matchAll(/^SECCIÓN (\d+) —/gm)].map((m) => Number(m[1]));
const esperado = Array.from({ length: 25 }, (_, i) => i + 1);
if (secs.join(',') !== esperado.join(',')) {
  aviso('condiciones-del-servicio.txt: las secciones son ' + secs.join(',') + ', no 1..25');
} else {
  console.log('  las 25 secciones, enteras y en orden');
}

console.log(fallos ? '\n  ' + fallos + ' problemas' : '\n  OK   las politicas, sin un solo hueco');
process.exit(fallos ? 1 : 0);
