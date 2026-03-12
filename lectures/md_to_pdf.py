#!/usr/bin/env python3
"""
Convert Markdown (with Mermaid diagrams) to PDF.
Strategy: pre-render each Mermaid block to SVG via mermaid.ink API,
embed SVGs directly in the HTML so Chromium needs zero JS wait time.
Usage: python3 md_to_pdf.py <input.md> [output.pdf]
"""
import base64
import re
import subprocess
import sys
import tempfile
import urllib.request
import urllib.error
from pathlib import Path


# ── Mermaid pre-rendering ────────────────────────────────────────────────────

def _fetch_svg(code: str) -> str | None:
    """Render mermaid code to SVG. Primary: kroki.io POST. Fallback: mermaid.ink."""
    b64 = base64.urlsafe_b64encode(code.encode("utf-8")).decode()
    attempts = [
        # kroki.io: reliable POST, no encoding issues with Unicode
        ("POST", "https://kroki.io/mermaid/svg",
         code.encode("utf-8"), "text/plain; charset=utf-8"),
        # mermaid.ink: GET with URL-safe base64
        ("GET", f"https://mermaid.ink/svg/{b64}", None, ""),
    ]
    for method, url, data, ctype in attempts:
        try:
            headers = {"User-Agent": "md-to-pdf/2.0"}
            if ctype:
                headers["Content-Type"] = ctype
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=20) as resp:
                svg = resp.read().decode("utf-8")
                if "<svg" in svg:
                    return svg
        except urllib.error.HTTPError as e:
            print(f"    ⚠ HTTP {e.code} from {url[:40]}...")
        except Exception as e:
            print(f"    ⚠ {url[:40]}...: {e}")
    return None


def prerender_mermaid(md: str) -> str:
    """Replace ```mermaid...``` blocks with inline SVG (or error box)."""
    pattern = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
    blocks = pattern.findall(md)
    if not blocks:
        return md

    print(f"Pre-rendering {len(blocks)} Mermaid diagram(s)...")
    counter = [0]

    def replace(match: re.Match) -> str:
        code = match.group(1).strip()
        counter[0] += 1
        short = code[:60].replace("\n", " ")
        print(f"  [{counter[0]}/{len(blocks)}] {short}...")
        svg = _fetch_svg(code)
        if svg:
            return f'\n<div class="mermaid-svg">{svg}</div>\n'
        escaped = (code.replace("&", "&amp;")
                       .replace("<", "&lt;")
                       .replace(">", "&gt;"))
        return (f'\n<div class="mermaid-error">'
                f'<p>⚠ Diagram could not be rendered</p>'
                f'<pre>{escaped}</pre></div>\n')

    return pattern.sub(replace, md)


# ── HTML generation ──────────────────────────────────────────────────────────

_CSS = """
body {
  font-family: "Segoe UI", Arial, sans-serif;
  font-size: 14px; line-height: 1.6;
  max-width: 960px; margin: 0 auto; padding: 2em; color: #222;
}
h1 { font-size: 1.8em; border-bottom: 2px solid #4472C4;
     padding-bottom: .3em; margin-top: 2em; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 1.4em; color: #4472C4; margin-top: 1.5em; }
h3 { font-size: 1.1em; color: #5B9BD5; }
hr { border: none; border-top: 1px dashed #ccc; margin: 2em 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th { background: #4472C4; color: #fff; padding: .5em .8em; text-align: left; }
td { border: 1px solid #ddd; padding: .4em .8em; }
tr:nth-child(even) td { background: #f5f8ff; }
pre { background: #f4f4f4; padding: 1em; border-radius: 4px;
      overflow-x: auto; font-size: .85em; }
code { background: #f4f4f4; padding: .1em .3em; border-radius: 3px; }
blockquote { border-left: 4px solid #4472C4; margin: 1em 0;
             padding: .5em 1em; background: #f0f4ff; }
.mermaid-svg { text-align: center; margin: 1.5em 0; }
.mermaid-svg svg { max-width: 100%; height: auto; }
.mermaid-error { border: 1px solid #f66; padding: 1em;
                 background: #fff0f0; border-radius: 4px; }
@media print {
  h1 { page-break-before: always; }
  h1:first-of-type { page-break-before: avoid; }
  .mermaid-svg { page-break-inside: avoid; }
}
"""


def build_html(title: str, md_with_svgs: str) -> str:
    # Escape for JS template literal: \, `, $
    safe = (md_with_svgs
            .replace("\\", "\\\\")
            .replace("`", "\\`")
            .replace("$", "\\$"))
    return f"""<!DOCTYPE html>
<html lang="el">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>{_CSS}</style>
</head>
<body>
  <div id="content"></div>
  <script>
    marked.setOptions({{ mangle: false, headerIds: false }});
    // marked passes raw HTML blocks through untouched — our SVGs are safe
    document.getElementById('content').innerHTML = marked.parse(`{safe}`);
  </script>
</body>
</html>"""


# ── Main ─────────────────────────────────────────────────────────────────────

def md_to_pdf(md_path: str, pdf_path: str | None = None):
    src = Path(md_path)
    if not src.exists():
        sys.exit(f"Error: file not found: {md_path}")

    pdf_out = Path(pdf_path) if pdf_path else src.with_suffix(".pdf")
    raw = src.read_text(encoding="utf-8")

    # Strip Marp / YAML frontmatter (--- ... ---)
    raw = re.sub(r"^\s*---\n.*?\n---\n", "", raw, flags=re.DOTALL)

    # Pre-render Mermaid diagrams to inline SVG
    raw = prerender_mermaid(raw)

    html = build_html(src.stem, raw)

    with tempfile.NamedTemporaryFile(
        suffix=".html", mode="w", encoding="utf-8", delete=False
    ) as f:
        f.write(html)
        tmp = f.name

    print(f"Generating PDF → {pdf_out} ...")
    res = subprocess.run(
        [
            "chromium",
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            f"--print-to-pdf={pdf_out.resolve()}",
            f"file://{tmp}",
        ],
        capture_output=True,
        text=True,
    )

    Path(tmp).unlink(missing_ok=True)

    if res.returncode == 0:
        print(f"✅ PDF saved: {pdf_out.resolve()}")
    else:
        print("❌ Chromium error:")
        print(res.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)
    md_to_pdf(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
