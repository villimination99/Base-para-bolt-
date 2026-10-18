#!/usr/bin/env bash
# Preparacion, una sola vez: comprueba ffmpeg y Node, instala lo de Python y
# crea las carpetas. Derivado de tools/setup.sh de
# https://github.com/bekhruztbx/ai-creative-team (MIT, (c) 2026 Bekhruz AI).
#
# Cambios: el modelo de voz a texto que se instala es MULTILINGUE, porque la
# tienda vende en cinco idiomas y el del original era solo ingles. Y avisa de
# la tipografia, que es lo que hace que las portadas salgan con la letra de la
# marca y no con la que haya.
set -e
cd "$(dirname "$0")/.."

command -v ffmpeg >/dev/null || { echo "Instala ffmpeg primero (macOS: brew install ffmpeg)"; exit 1; }
command -v ffprobe >/dev/null || { echo "Falta ffprobe, que viene con ffmpeg. Reinstala ffmpeg."; exit 1; }
command -v npx >/dev/null || { echo "Instala Node.js 18+ primero (hace correr el cerebro compartido)"; exit 1; }

python3 -m pip install --quiet numpy pillow

if python3 -m pip install --quiet faster-whisper; then
  echo "voz a texto: faster-whisper (se baja el modelo la primera vez que corre)"
  echo "             el modelo por defecto es 'small', que entiende espanol, frances, ingles, aleman y japones."
  echo "             para ir mas rapido con menos acierto: export WHISPER_MODEL=base"
else
  echo "AVISO: faster-whisper no se ha instalado."
  echo "       Los clips de producto siguen funcionando enteros, porque no necesitan voz."
  echo "       Los clips con voz NO: el respaldo del proyecto original solo trae modelo ingles."
fi

mkdir -p inbox salida hechos cerebro herramientas/fuentes

if ! ls herramientas/fuentes/*.ttf herramientas/fuentes/*.otf >/dev/null 2>&1; then
  echo
  echo "TIPOGRAFIA: no hay ninguna en herramientas/fuentes/."
  echo "  Las portadas y los rotulos saldran con la mejor fuente del sistema, no con la de la marca."
  echo "  Para que salgan con la de verdad, baja Assistant de https://fonts.google.com/specimen/Assistant"
  echo "  y deja el .ttf ahi dentro. Las herramientas la encuentran solas."
fi

echo
echo "Listo. Deja los clips en inbox/, arranca Claude Code AQUI (en creativo/) con: claude"
echo "y escribe: /editar-clips"
