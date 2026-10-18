# El equipo creativo

Un equipo de agentes que convierte clips en bruto en videos verticales cortos
para anuncios y redes. Una orden, y cada clip de `inbox/` sale cortado,
rotulado y con portada.

Nada de esta carpeta viaja a Shopify. El zip del tema solo lleva `theme/`.

## De donde sale

Adaptado de **https://github.com/bekhruztbx/ai-creative-team** (MIT,
(c) 2026 Bekhruz AI), que es una plantilla publica salida del video «I Built an
AI Agent Team From Scratch». El original esta bien hecho: permisos estrictos de
verdad, nada se sube a ninguna parte y las herramientas son ffmpeg y Whisper
reales, no humo.

Lo que **no** servia tal cual, y por que:

| Lo del original | El problema aqui |
| --- | --- |
| Voz a texto fijada a ingles (`small.en`, `language="en"`) | La tienda vende en **cinco idiomas**. En espanol transcribia ruido. |
| Muletillas inglesas (`um`, `uh`, `erm`) | En espanol son `eh`, `este`, `pues`, `o sea`; en frances `euh`, `ben`. |
| `cut.py` depende del habla | Con un clip **mudo** devuelve cero trozos y le pasa a ffmpeg `concat=n=0`, que revienta. Y el catalogo es casi todo producto sin voz. |
| Solo subtitulos de voz | Sin voz no hay nada que transcribir: el mensaje hay que **escribirlo**. |
| Tipografia Geist, color amarillo `#FFD400` | No son los de la marca. |
| Todo dirigido a «Bekhruz» | Las reglas de marca eran las suyas. |

## Lo que hay ahora

Dos caminos, porque hay dos tipos de material y no se editan igual:

- **Con voz**: el ritmo lo marcan las frases. Se quitan pausas y muletillas y se
  transcribe palabra por palabra.
- **Sin voz**: el ritmo lo marcan los **cambios de plano** y el mensaje va en
  **rotulos escritos**.

Y una pieza nueva que decide cual toca mirando el clip, no a ojo.

| Pieza | Archivo | Que hace |
| --- | --- | --- |
| Carta del equipo | `CLAUDE.md` | Quien es quien, las carpetas, las reglas |
| Clasificador | `herramientas/clasificar.py` | Dice de cada clip si va por voz o por producto |
| Editor de voz | `.claude/agents/editor-voz.md` | Un clip hablado entra, una edicion sale |
| Editor de producto | `.claude/agents/editor-producto.md` | Lo mismo para clips mudos |
| Revisor | `.claude/agents/revisor-marca.md` | Repasa contra las reglas. Solo mira, no edita |
| La orden | `.claude/commands/editar-clips.md` | `/editar-clips` |
| Permisos | `.claude/settings.json` | Que puede hacer solo, que pregunta, que no puede |
| Cerebro | `.mcp.json` + `cerebro/reglas.jsonl` | Las reglas de marca |

## Preparacion, una sola vez

Hace falta [Claude Code](https://claude.com/claude-code), ffmpeg, Python 3.10+ y
Node.js 18+.

```bash
cd creativo
bash herramientas/preparar.sh
```

### La tipografia

**Baja Assistant de https://fonts.google.com/specimen/Assistant y deja el `.ttf`
en `herramientas/fuentes/`.** Es la fuente del tema, y con ella las portadas y
los rotulos salen con la letra de la tienda. Sin ella todo funciona igual, pero
con la mejor fuente que haya en el sistema; cada herramienta dice en su informe
con cual ha escrito, y el revisor lo senala.

No va versionada en git a proposito: es un binario de fuente y el repositorio no
es su sitio.

## Usarlo

1. Deja los clips (mp4, mov, m4v) en `inbox/`.
2. Arranca Claude Code **dentro de `creativo/`**: `cd creativo && claude`
3. Escribe `/editar-clips`

Cada clip acaba en `salida/<nombre>/`: `edicion.mp4` (vertical, con subtitulos o
rotulos), `portada.jpg`, `fotogramas.jpg`, `notas.md`, y `subtitulos.srt` si
llevaba voz.

> **Arranca Claude Code dentro de `creativo/`, no en la raiz del repositorio.**
> Asi el equipo de video y el trabajo del tema no se mezclan nunca: los agentes,
> la orden, los permisos y el cerebro son de esta carpeta y solo se cargan aqui.

## Ensenarle tu estilo

Diselo y ya: *«a partir de ahora los rotulos en verde, no en cian»*. La regla se
guarda en `cerebro/reglas.jsonl` y todos los agentes la siguen desde la
siguiente vez. Tambien puedes editar ese archivo a mano.

## Las herramientas, por si las quieres sueltas

```bash
python3 herramientas/clasificar.py inbox

python3 herramientas/cortar-voz.py inbox/x.mp4 salida/x/corte.mp4 --max 45 --idioma es
python3 herramientas/subtitulos.py salida/x/corte.mp4 salida/x/edicion.mp4 --idioma es --color cian

python3 herramientas/cortar-producto.py inbox/y.mp4 salida/y/corte.mp4 --max 20
python3 herramientas/rotulos.py salida/y/corte.mp4 salida/y/edicion.mp4 --reparte "LUZ QUE RESPIRA|HECHA A MANO"

python3 herramientas/portada.py salida/y/corte.mp4 salida/y/portada.jpg --texto "LUZ QUE RESPIRA"
python3 herramientas/fotogramas.py salida/y/edicion.mp4 salida/y/fotogramas.jpg
```

Los colores se dicen por nombre — `cian`, `verde`, `naranja`, `rosa`, `morado` —
o en hex. Un nombre que no existe no pasa en silencio: la herramienta para y te
dice cuales hay.

## Seguridad

- El equipo solo puede correr las siete herramientas de `herramientas/`, mover
  clips de `inbox/` a `hechos/` y escribir en `salida/`.
- Borrar archivos y las ordenes de red (`curl`, `wget`) estan **bloqueados**.
  `git push` y `git commit` **preguntan**.
- `../theme/` y `../verificadores/` estan bloqueados: el equipo de video no toca
  el tema de la tienda.
- El servidor de memoria va **pinneado** a `@1.0.0` en vez de a la ultima, para
  que no cambie bajo los pies.
- Nada se sube ni se publica. Tu miras `salida/` y publicas tu.

## Lo que esta probado y lo que no

Probado aqui de verdad, con clips sinteticos, no solo leido:

- El corte de producto encuentra los cambios de plano (3,0 / 6,0 / 9,0 s en un
  clip de cuatro planos), saca 1080x1920 y le pone pista de audio muda.
- El corte de voz quita el silencio (4,1 s de 12) y deja 1080x1920.
- Un clip mudo mandado al corte de voz **avisa y para**, que es justo lo que el
  original no hacia.
- El clasificador acierta los tres casos: sin pista de audio, con pista pero en
  silencio, y con voz.
- Rotulos, portada y hoja de contactos salen y se ven bien. Mirandolos se
  encontraron y arreglaron dos fallos de contraste: la hora de la hoja de
  contactos desaparecia sobre planos cian o verdes, y el degradado de la portada
  se apagaba antes de llegar a la ultima palabra, que es la que va en cian.

**No** probado aqui: la transcripcion de voz de verdad. `faster-whisper` se baja
su modelo de internet y este contenedor no llega. Los clips de prueba llevaban
tonos, no habla. La primera vez que edites un clip hablado, **lee la
transcripcion** que imprime la herramienta antes de fiarte.
