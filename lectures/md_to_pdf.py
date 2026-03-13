#!/usr/bin/env python3
"""
Convert a Marp Markdown file to a slide-based PDF presentation.

Strategy:
  1. Run the full md_to_html pipeline to produce a correct self-contained HTML
     (pre-rendered Mermaid, embedded logo, auto-scale JS, proper font-size)
  2. Inject @media print CSS so each Marp SVG slide becomes its own PDF page
  3. Print to PDF with Chromium headless (same engine, same rendering as the HTML)

This guarantees the PDF matches the HTML exactly, including auto-scaled text.

Usage:
  python3 md_to_pdf.py <input.md> [output.pdf]
"""
import subprocess
import sys
from pathlib import Path

from md_to_html import md_to_html


# When Chromium prints headlessly, only slide 1 is ever "active", so the
# interactive auto-scale JS (which waits for bespoke-marp-active) doesn't
# run on any other slide.  This script scales ALL slides up-front at load.
_FIT_ALL_JS = """
<script>
(function () {
  var MIN_FS = 13;
  function fitSection(section) {
    var fs = parseFloat(getComputedStyle(section).fontSize);
    while (section.scrollHeight > section.clientHeight + 2 && fs > MIN_FS) {
      fs -= 0.5;
      section.style.fontSize = fs + 'px';
    }
  }
  function fitAll() {
    document.querySelectorAll('svg.bespoke-marp-slide section').forEach(fitSection);
  }
  document.fonts.ready.then(function () { setTimeout(fitAll, 150); });
  window.addEventListener('beforeprint', fitAll);
})();
</script>
"""


def md_to_pdf(md_path: str, pdf_path: str | None = None) -> None:
    src = Path(md_path)
    if not src.exists():
        sys.exit(f"Error: file not found: {md_path}")

    pdf_out = Path(pdf_path) if pdf_path else src.with_suffix(".pdf")

    # 1. Generate self-contained HTML into a temp file
    tmp_html = src.with_name(f"_tmp_{src.stem}.html")
    try:
        print("Building HTML…")
        md_to_html(str(src), str(tmp_html))

        # 2. Inject the fit-all script (scales every slide at load, not just active)
        html = tmp_html.read_text(encoding="utf-8")
        html = html.replace("</body>", _FIT_ALL_JS + "\n</body>", 1)
        tmp_html.write_text(html, encoding="utf-8")

        # 3. Print to PDF with Chromium
        # --virtual-time-budget lets bespoke.js + auto-scale JS run before print
        print(f"Printing to PDF → {pdf_out} …")
        res = subprocess.run(
            [
                "chromium",
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                # Allow JS (bespoke.js + auto-scale) to run before printing
                "--virtual-time-budget=5000",
                f"--print-to-pdf={pdf_out.resolve()}",
                "--print-to-pdf-no-header",
                f"file://{tmp_html.resolve()}",
            ],
            capture_output=True, text=True,
        )
        if res.returncode == 0:
            print(f"✅ PDF saved: {pdf_out.resolve()}")
        else:
            print("❌ Chromium error:")
            print(res.stderr or res.stdout)
    finally:
        tmp_html.unlink(missing_ok=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)
    md_to_pdf(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
