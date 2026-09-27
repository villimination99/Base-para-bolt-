// Saca los tres textos definitivos del artefacto y los deja como .txt en esta
// carpeta, para que queden en el repositorio y no solo en una pagina publicada.
import fs from 'node:fs';
import path from 'node:path';
const AQUI = path.dirname(new URL(import.meta.url).pathname);
const html = fs.readFileSync(process.argv[2], 'utf8');
const NOMBRES = {
  'p-contacto': 'informacion-de-contacto.txt',
  'p-aviso': 'aviso-legal.txt',
  'p-condiciones': 'condiciones-del-servicio.txt',
};
for (const [id, archivo] of Object.entries(NOMBRES)) {
  const m = html.match(new RegExp('<pre id="' + id + '">([\\s\\S]*?)</pre>'));
  if (!m) throw new Error('falta ' + id + ' en ' + process.argv[2]);
  const texto = m[1].replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
  fs.writeFileSync(path.join(AQUI, archivo), texto + '\n');
  console.log('  ' + archivo.padEnd(30) + String(texto.length).padStart(6) + ' bytes');
}
