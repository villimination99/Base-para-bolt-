"""Ayudas de ffmpeg que comparten las herramientas del equipo creativo.

Derivado de `tools/media.py` de https://github.com/bekhruztbx/ai-creative-team
(MIT, (c) 2026 Bekhruz AI). Lo que cambia respecto al original, y por que:

  - **El reconocimiento de voz ya no esta fijado a ingles.** El original usaba
    `small.en` y `language="en"` en los dos caminos. La tienda vende en cinco
    idiomas (de, en, es, fr, ja), asi que un modelo `.en` transcribiria el
    espanol como ruido. Aqui el modelo es multilingue y el idioma es un
    parametro.
  - **Las muletillas son por idioma.** `um`/`uh` no aparecen en espanol: alli
    son `eh`, `este`, `o sea`, `pues`; en frances `euh`, `ben`.
  - **La tipografia se resuelve por cadena de respaldo** en vez de apuntar a un
    archivo fijo. Si dejas la Assistant en `fuentes/`, sale la fuente real de la
    marca; si no, la mejor que haya en el sistema.
  - **La paleta de la tienda por nombre**, para no pegar hex a mano en cada
    orden y que no se cuele un color que no es de la marca.
  - **`probe()` usa ffprobe** en vez de leer el banner de ffmpeg con una
    expresion regular, y de paso dice si el clip trae pista de audio. Eso hace
    falta para los clips de producto, que a menudo vienen mudos.
  - **`escenas()`**: cambios de plano, que es el reemplazo del habla para marcar
    el ritmo de un montaje sin voz.
"""
import json, os, re, subprocess, sys

import numpy as np

FFMPEG = os.environ.get("FFMPEG", "ffmpeg")
FFPROBE = os.environ.get("FFPROBE", "ffprobe")
AQUI = os.path.dirname(os.path.abspath(__file__))
SR = 16000

# La paleta de la tienda. Los contrastes estan medidos sobre la superficie
# #0b0b1e y anotados en LEEME-caja.md. El cian es el color principal.
PALETA = {
    "cian": "#00d4ff",
    "verde": "#00e87b",
    "naranja": "#ff7700",
    "rosa": "#ff2ecb",
    "morado": "#7b2fff",
    "texto": "#d8f6ff",
    "fondo": "#0b0b1e",
    "fondo2": "#121228",
    "negro": "#05050f",
    "blanco": "#ffffff",
}


def rgb(valor):
    """(r, g, b) de un nombre de la paleta o de un hex. Falla claro si no es ni uno ni otro."""
    v = PALETA.get(str(valor).strip().lower(), str(valor).strip())
    v = v.lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", v):
        raise SystemExit(f"color desconocido: {valor!r}. Usa un hex #rrggbb o uno de: {', '.join(PALETA)}")
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def run(args, **kw):
    """Ejecuta ffmpeg en silencio; si falla, levanta con su propio stderr."""
    p = subprocess.run([FFMPEG, "-hide_banner", "-y"] + args, capture_output=True, text=True, **kw)
    if p.returncode != 0:
        raise RuntimeError(p.stderr[-2000:])
    return p


def probe(path):
    """Duracion, tamano, fps y si trae audio. Por ffprobe, que da datos y no texto que adivinar."""
    p = subprocess.run([FFPROBE, "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path],
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"no se puede leer {path}: {p.stderr.strip()[-500:]}")
    d = json.loads(p.stdout)
    vs = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    audio_ok = any(s["codec_type"] == "audio" for s in d["streams"])
    if vs is None:
        raise RuntimeError(f"{path} no tiene pista de video")
    dur = float(d["format"].get("duration") or vs.get("duration") or 0.0)
    fps = 30.0
    if vs.get("avg_frame_rate", "0/0") not in ("0/0", "0/1"):
        num, den = (float(x) for x in vs["avg_frame_rate"].split("/"))
        fps = num / den if den else 30.0
    return {"duration": dur, "width": int(vs["width"]), "height": int(vs["height"]), "fps": fps or 30.0, "audio": audio_ok}


def audio(path, sr=SR):
    """Muestras mono float32 del audio. Array vacio si el clip viene mudo."""
    if not probe(path)["audio"]:
        return np.zeros(0, np.float32)
    raw = subprocess.run([FFMPEG, "-hide_banner", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def segmentos_voz(path, ruido_db=-32, silencio_min=0.45):
    """[(inicio, fin)] de los trozos con sonido, de silencedetect. Vacio si el clip es mudo."""
    if not probe(path)["audio"]:
        return []
    err = run(["-i", path, "-vn", "-af", f"silencedetect=noise={ruido_db}dB:d={silencio_min}", "-f", "null", "-"]).stderr
    dur = probe(path)["duration"]
    inicios = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    finales = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    segs, t = [], 0.0
    for s, e in zip(inicios, finales + [dur] * (len(inicios) - len(finales))):
        if s > t + 0.05:
            segs.append((t, s))
        t = e
    if t < dur - 0.05:
        segs.append((t, dur))
    return segs


def escenas(path, umbral=0.30):
    """Segundos en los que cambia el plano. Es lo que marca el ritmo cuando no hay voz."""
    err = run(["-i", path, "-vf", f"select='gt(scene,{umbral})',showinfo", "-an", "-f", "null", "-"]).stderr
    return sorted(float(t) for t in re.findall(r"pts_time:([\d.]+)", err))


def report(**kw):
    """Una linea JSON en stdout, para que el agente lea el resultado."""
    print(json.dumps(kw, ensure_ascii=False))
    sys.stdout.flush()


# Muletillas por idioma. Las del original eran solo inglesas.
MULETILLAS = {
    "es": {"eh", "ehh", "este", "pues", "osea", "mmm", "mm", "em", "ehm", "aaa", "bueno"},
    "en": {"um", "uh", "erm", "er", "hmm", "ah", "uhm", "mm"},
    "fr": {"euh", "euhh", "ben", "bah", "hein", "mmm", "mm"},
    "de": {"ah", "aeh", "aehm", "oehm", "hm", "hmm", "tja"},
    "ja": {"ano", "eto", "maa", "ee"},
}

# Palabras cortas que NO son muletilla y hay que conservar, por idioma.
CONSERVAR = {
    "es": {"si", "no", "ya", "vale", "mira", "oye", "hola", "ojo", "toma", "venga", "guau"},
    "en": {"okay", "ok", "yes", "yeah", "no", "so", "right", "wow", "hi", "hey", "go", "now"},
    "fr": {"oui", "non", "ok", "voila", "salut", "tiens", "allez", "bon"},
    "de": {"ja", "nein", "ok", "so", "gut", "hallo", "jetzt"},
    "ja": {"hai", "iie", "ok", "dou", "sou"},
}


def solo_muletillas(texto, idioma="es", segundos=None):
    """True para "eh", "um", "euh"... Un sonido suelto de menos de 0,55 s que no sea
    una palabra corta de verdad cuenta tambien: los modelos pequenos escriben una
    muletilla como cualquier cosa."""
    mul = MULETILLAS.get(idioma, set()) | MULETILLAS["en"]
    keep = CONSERVAR.get(idioma, set()) | CONSERVAR["en"]
    pal = [re.sub(r"[^\wáéíóúñàèùçü]", "", w.lower(), flags=re.UNICODE) for w in texto.split()]
    pal = [w for w in pal if w]
    if segundos is not None and segundos < 0.55 and len(pal) <= 1 and not (pal and pal[0] in keep):
        return True
    return bool(pal) and all(w in mul for w in pal)


class STT:
    """Voz a texto, en local y multilingue.

    faster-whisper si esta instalado (es el que da tiempos por palabra). El
    respaldo sherpa-onnx del original solo trae el modelo `tiny.en`, asi que en
    espanol o frances no sirve: si solo hay ese, avisa en vez de devolver ruido.
    """

    def __init__(self, idioma="es"):
        self.idioma = idioma
        try:
            from faster_whisper import WhisperModel
            modelo = os.environ.get("WHISPER_MODEL", "small")
            if idioma == "en" and not modelo.endswith(".en"):
                modelo = os.environ.get("WHISPER_MODEL", "small.en")
            self.fw = WhisperModel(modelo, compute_type="int8")
            self.motor = f"faster-whisper {modelo}"
        except ImportError:
            import sherpa_onnx
            d = os.environ.get("WHISPER_ONNX_DIR", os.path.join(AQUI, "modelos", "sherpa-onnx-whisper-tiny.en"))
            if idioma != "en":
                raise SystemExit(
                    f"Solo esta el respaldo sherpa-onnx con el modelo ingles y pediste idioma {idioma!r}.\n"
                    "Instala faster-whisper (bash herramientas/preparar.sh) o pasa --idioma en."
                )
            pre = os.path.join(d, os.path.basename(d).replace("sherpa-onnx-whisper-", "") + "-")
            self.rec = sherpa_onnx.OfflineRecognizer.from_whisper(
                encoder=pre + "encoder.int8.onnx", decoder=pre + "decoder.int8.onnx", tokens=pre + "tokens.txt",
                language="en", task="transcribe", num_threads=2)
            self.fw = None
            self.motor = "sherpa-onnx whisper tiny.en"

    def texto(self, pcm, sr=SR):
        """Transcripcion de un trozo corto de audio."""
        if len(pcm) == 0:
            return ""
        if self.fw is not None:
            segs, _ = self.fw.transcribe(pcm, language=self.idioma)
            return " ".join(x.text.strip() for x in segs)
        st = self.rec.create_stream()
        st.accept_waveform(sr, pcm)
        self.rec.decode_stream(st)
        return st.result.text.strip()


def fuente(tamano, peso=800):
    """La tipografia de los rotulos, por orden de preferencia.

    1. `herramientas/fuentes/` de la marca: cualquier Assistant primero, que es
       la fuente del tema, y si no la que haya.
    2. Lo mejor del sistema (Inter, DejaVu).
    3. La de PIL, para que nunca reviente.

    Devuelve (fuente, nombre) para que la herramienta pueda decir con que ha
    escrito: si no es Assistant, conviene que se vea en el informe.
    """
    from PIL import ImageFont

    dir_marca = os.path.join(AQUI, "fuentes")
    candidatas = []
    if os.path.isdir(dir_marca):
        archivos = sorted(f for f in os.listdir(dir_marca) if f.lower().endswith((".ttf", ".otf")))
        candidatas += [os.path.join(dir_marca, f) for f in archivos if "assistant" in f.lower()]
        candidatas += [os.path.join(dir_marca, f) for f in archivos if "assistant" not in f.lower()]
    candidatas += [
        "/usr/share/fonts/opentype/inter/Inter-Black.otf",
        "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf",
        "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for ruta in candidatas:
        if not os.path.exists(ruta):
            continue
        try:
            f = ImageFont.truetype(ruta, tamano)
        except OSError:
            continue
        try:                                    # si es variable, al peso que toca
            f.set_variation_by_axes([peso])
        except Exception:
            pass
        return f, os.path.basename(ruta)
    return ImageFont.load_default(), "PIL por defecto"
