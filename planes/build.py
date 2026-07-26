#!/usr/bin/env python3
"""
VILLUMINATION 99 — Generador de PDFs premium
--------------------------------------------
Toma los HTML de src/, inyecta el sistema de diseño y las ilustraciones,
produce HTML autocontenido en build/ y PDFs A4 en dist/.

Uso:  python3 build.py                     (edición pantalla, todos)
      python3 build.py basico              (solo los que coincidan)
      python3 build.py --impresion         (edición para papel → dist/impresion/)
      python3 build.py --ambas             (las dos ediciones)
"""

import base64
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
ASSETS = ROOT / "assets"
PARTIALS = ROOT / "partials"

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/google-chrome",
]

META = {
    "author": "VILLUMINATION 99",
    "subject": "Plan de nutricion y entrenamiento — villuminations.com",
    "keywords": "fitness, nutricion, dieta, entrenamiento, villumination99",
}


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    found = shutil.which("chromium") or shutil.which("google-chrome")
    if found:
        return found
    hits = list(Path("/opt/pw-browsers").rglob("chrome"))
    if hits:
        return str(hits[0])
    raise SystemExit("No se encontro Chromium para renderizar los PDF.")


def assemble(html: str, impresion: bool = False) -> str:
    """Inyecta el sistema de diseno y las ilustraciones en el HTML."""
    # Las fuentes se enlazan desde assets/ en vez de incrustarse en base64:
    # Chromium NO incrusta en el PDF las fuentes cargadas desde data: URI y
    # acaba rasterizando cada titular como imagen. Con url() relativa las
    # incrusta como fuente real (texto nitido, seleccionable y mucho mas ligero).
    head = (
        '<link rel="stylesheet" href="../assets/fonts.css">\n<style>\n'
        + (ASSETS / "brand.css").read_text()
        + ("\n" + (ASSETS / "impresion.css").read_text() if impresion else "")
        + "\n</style>"
    )
    html = html.replace("<!--@head-->", head)
    html = html.replace("<!--@sprite-->", (PARTIALS / "sprite.svg").read_text())
    return html


def render(chrome: str, src_html: Path, out_pdf: Path) -> None:
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--font-render-hinting=none",
        "--no-pdf-header-footer",
        "--virtual-time-budget=12000",
        f"--print-to-pdf={out_pdf}",
        src_html.as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not out_pdf.exists():
        raise SystemExit(f"Fallo al renderizar {src_html.name}:\n{res.stderr[-2000:]}")


def stamp_metadata(pdf: Path, title: str) -> None:
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        return
    writer = PdfWriter(clone_from=str(pdf))
    for page in writer.pages:
        page.compress_content_streams(level=9)
    try:
        writer.compress_identical_objects()
    except Exception:
        pass
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": META["author"],
            "/Subject": META["subject"],
            "/Keywords": META["keywords"],
            "/Creator": "VILLUMINATION 99 — villuminations.com",
        }
    )
    tmp = pdf.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(pdf)


def page_count(pdf: Path) -> int:
    try:
        from pypdf import PdfReader

        return len(PdfReader(str(pdf)).pages)
    except Exception:
        return -1


def run(chrome: str, sources, impresion: bool) -> None:
    """Genera una edicion completa (pantalla o impresion)."""
    out_dir = DIST / "impresion" if impresion else DIST
    build_dir = BUILD / "impresion" if impresion else BUILD
    out_dir.mkdir(parents=True, exist_ok=True)
    build_dir.mkdir(parents=True, exist_ok=True)
    print(f"\nEdicion {'IMPRESION (papel blanco)' if impresion else 'PANTALLA (neon)'}")

    problems = []
    total = 0
    for src in sources:
        raw = src.read_text()
        built = build_dir / src.name
        built.write_text(assemble(raw, impresion))

        out = out_dir / (src.stem + ".pdf")
        render(chrome, built, out)

        title_match = re.search(r"<title>(.*?)</title>", raw, re.S)
        title = title_match.group(1).strip() if title_match else src.stem
        stamp_metadata(out, title)

        declared = len(re.findall(r'class="page[ "]', raw))
        actual = page_count(out)
        flag = "" if declared == actual else f"  <-- REVISAR (declaradas {declared})"
        if flag:
            problems.append(f"{src.name}: {actual} paginas, {declared} declaradas")
        size = out.stat().st_size / 1024
        total += size
        print(f"  {out.name:<46} {actual:>2} pag  {size:>6.0f} KB{flag}")

    print(f"  {'TOTAL':<46}        {total/1024:>6.1f} MB")
    if problems:
        print("  Desajustes de paginacion:")
        for p in problems:
            print("   - " + p)


def main() -> None:
    chrome = find_chrome()
    BUILD.mkdir(exist_ok=True)
    DIST.mkdir(exist_ok=True)

    args = [a for a in sys.argv[1:]]
    impresion = "--impresion" in args
    ambas = "--ambas" in args
    flt = next((a for a in args if not a.startswith("--")), "")

    sources = sorted(p for p in SRC.glob("*.html") if flt in p.name)
    if not sources:
        raise SystemExit(f"Sin documentos que coincidan con '{flt}'.")

    if ambas:
        run(chrome, sources, impresion=False)
        run(chrome, sources, impresion=True)
    else:
        run(chrome, sources, impresion=impresion)


if __name__ == "__main__":
    main()
