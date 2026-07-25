#!/usr/bin/env python3
"""
VILLUMINATION 99 — Generador de PDFs premium
--------------------------------------------
Toma los HTML de src/, inyecta el sistema de diseño y las ilustraciones,
produce HTML autocontenido en build/ y PDFs A4 en dist/.

Uso:  python3 build.py            (todos)
      python3 build.py basico     (solo los que coincidan con el filtro)
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


def assemble(html: str) -> str:
    """Inyecta CSS y sprite para que el HTML sea autocontenido."""
    head = (
        "<style>\n"
        + (ASSETS / "fonts.css").read_text()
        + "\n"
        + (ASSETS / "brand.css").read_text()
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
    reader = PdfReader(str(pdf))
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
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


def main() -> None:
    chrome = find_chrome()
    BUILD.mkdir(exist_ok=True)
    DIST.mkdir(exist_ok=True)
    flt = sys.argv[1] if len(sys.argv) > 1 else ""

    sources = sorted(p for p in SRC.glob("*.html") if flt in p.name)
    if not sources:
        raise SystemExit(f"Sin documentos que coincidan con '{flt}'.")

    problems = []
    for src in sources:
        raw = src.read_text()
        html = assemble(raw)
        built = BUILD / src.name
        built.write_text(html)

        out = DIST / (src.stem + ".pdf")
        render(chrome, built, out)

        title_match = re.search(r"<title>(.*?)</title>", raw, re.S)
        title = title_match.group(1).strip() if title_match else src.stem
        stamp_metadata(out, title)

        # Cada <section class="page"> debe ocupar exactamente una pagina del PDF.
        declared = len(re.findall(r'class="page[ "]', raw))
        actual = page_count(out)
        flag = "" if declared == actual else f"  <-- REVISAR (declaradas {declared})"
        if flag:
            problems.append(f"{src.name}: {actual} paginas, {declared} declaradas")
        size = out.stat().st_size / 1024
        print(f"  {out.name:<46} {actual:>2} pag  {size:>6.0f} KB{flag}")

    if problems:
        print("\nDesajustes de paginacion:")
        for p in problems:
            print("  - " + p)
    else:
        print("\nPaginacion correcta en todos los documentos.")


if __name__ == "__main__":
    main()
