#!/usr/bin/env python3
"""
Convert a Marp Markdown file to a beautiful HTML slide presentation.

Strategy:
  1. Pre-render Mermaid blocks to SVG via kroki.io / mermaid.ink
  2. Embed SVGs as base64 <img> tags so Marp treats them as images
  3. Reduce the default font-size (35px → 28px) if no custom style is set,
     so content-heavy slides don't overflow
  4. Run: marp --html <temp.md> -o <output.html>   (Node 20 via nvm)

Usage:
  python3 md_to_html.py <input.md> [output.html]
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
    """Render mermaid code → SVG string.  Primary: kroki.io  Fallback: mermaid.ink"""
    b64 = base64.urlsafe_b64encode(code.encode("utf-8")).decode()
    attempts = [
        ("POST", "https://kroki.io/mermaid/svg",
         code.encode("utf-8"), "text/plain; charset=utf-8"),
        ("GET",  f"https://mermaid.ink/svg/{b64}", None, ""),
    ]
    for method, url, data, ctype in attempts:
        try:
            headers = {"User-Agent": "md-to-html/1.0"}
            if ctype:
                headers["Content-Type"] = ctype
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=20) as resp:
                svg = resp.read().decode("utf-8")
                if "<svg" in svg:
                    return svg
        except urllib.error.HTTPError as e:
            print(f"    ⚠ HTTP {e.code} from {url[:50]}...")
        except Exception as e:
            print(f"    ⚠ {url[:50]}...: {e}")
    return None


def prerender_mermaid(md: str, max_height: int = 380) -> str:
    """
    Replace ```mermaid … ``` blocks with:
      <img src="data:image/svg+xml;base64,…" style="max-width:100%;max-height:{max_height}px">
    Marp (with --html) passes raw <img> tags through to the SVG foreignObject,
    so the diagram appears as a proper image inside the slide.
    """
    pattern = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
    blocks = pattern.findall(md)
    if not blocks:
        return md

    print(f"Pre-rendering {len(blocks)} Mermaid diagram(s)…")
    counter = [0]

    def replace(match: re.Match) -> str:
        code = match.group(1).strip()
        counter[0] += 1
        print(f"  [{counter[0]}/{len(blocks)}] {code[:60].replace(chr(10),' ')}…")
        svg = _fetch_svg(code)
        if svg:
            data_uri = "data:image/svg+xml;base64," + base64.b64encode(
                svg.encode("utf-8")
            ).decode()
            return (
                f'\n<img src="{data_uri}" '
                f'style="display:block;margin:0 auto;max-width:95%;max-height:{max_height}px">\n'
            )
        # fallback: show raw code
        escaped = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'\n<pre><code>⚠ Mermaid render failed:\n{escaped}</code></pre>\n'

    return pattern.sub(replace, md)


# ── Frontmatter helpers ───────────────────────────────────────────────────────

_FM_RE = re.compile(r"^(---\n.*?\n---\n)", re.DOTALL)


def _inject_font_size(md: str, px: int = 28) -> str:
    """
    If the frontmatter has no 'style:' key, inject a small CSS override
    that reduces the section font-size so content-heavy slides don't overflow.
    """
    m = _FM_RE.match(md)
    if not m:
        return md
    fm = m.group(1)
    if "style:" in fm:
        return md  # user already has custom styles – don't touch
    # Insert before the closing ---
    new_fm = fm.rstrip("\n").rstrip("-").rstrip("\n") + f"""
style: |
  section {{
    font-size: {px}px;
  }}
---
"""
    return new_fm + md[m.end():]


# ── Auto-scale post-processing ───────────────────────────────────────────────

_AUTOSCALE_JS = """
<script>
(function () {
  /* Auto-scale slide content so it never overflows the 1280×720 canvas.
     Strategy: watch for each slide gaining 'bespoke-marp-active', then
     iteratively shrink its font-size until scrollHeight <= clientHeight. */
  var MIN_FS = 13;
  var done = new WeakSet();

  function fitSection(section) {
    var fs = parseFloat(getComputedStyle(section).fontSize);
    // Guard: only shrink, never grow; stop at minimum readable size
    while (section.scrollHeight > section.clientHeight + 2 && fs > MIN_FS) {
      fs -= 0.5;
      section.style.fontSize = fs + 'px';
    }
  }

  function fitActive() {
    document.querySelectorAll('svg.bespoke-marp-slide.bespoke-marp-active')
      .forEach(function (svg) {
        if (done.has(svg)) return;
        done.add(svg);
        var section = svg.querySelector('section');
        if (section) fitSection(section);
      });
  }

  // Watch for slides becoming active (class mutation)
  var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (m) {
      if (m.type === 'attributes' && m.target.classList &&
          m.target.classList.contains('bespoke-marp-active') &&
          !done.has(m.target)) {
        done.add(m.target);
        var section = m.target.querySelector('section');
        if (section) {
          // tiny delay so bespoke finishes its own transition
          setTimeout(function () { fitSection(section); }, 50);
        }
      }
    });
  });

  function init() {
    observer.observe(document.body, {
      attributes: true, attributeFilter: ['class'], subtree: true
    });
    // Fit the first (already active) slide after fonts settle
    document.fonts.ready.then(function () { setTimeout(fitActive, 100); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
"""


def _embed_local_images(html: str, base_dir: Path) -> str:
    """Replace <img src="local-file.ext"> with inline base64 data URIs."""
    import mimetypes

    def replacer(m: re.Match) -> str:
        src = m.group(1)
        # Skip already-embedded or remote URLs
        if src.startswith(("data:", "http://", "https://", "//")):
            return m.group(0)
        img_path = (base_dir / src).resolve()
        if not img_path.exists():
            return m.group(0)
        mime = mimetypes.guess_type(str(img_path))[0] or "image/png"
        data = base64.b64encode(img_path.read_bytes()).decode()
        return m.group(0).replace(f'src="{src}"', f'src="data:{mime};base64,{data}"')

    return re.sub(r'<img\b[^>]*\ssrc="([^"]+)"[^>]*>', replacer, html)


def post_process_html(html_path: Path) -> None:
    """Embed local images as base64 and inject the auto-scale JS."""
    html = html_path.read_text(encoding="utf-8")
    # 1. Embed local images so the HTML is fully self-contained
    html = _embed_local_images(html, html_path.parent)
    # 2. Inject auto-scale JS
    if _AUTOSCALE_JS.strip()[:20] not in html:
        html = html.replace("</body>", _AUTOSCALE_JS + "\n</body>", 1)
    html_path.write_text(html, encoding="utf-8")


# ── Main ─────────────────────────────────────────────────────────────────────

def md_to_html(md_path: str, html_path: str | None = None) -> None:
    src = Path(md_path)
    if not src.exists():
        sys.exit(f"Error: file not found: {md_path}")

    html_out = Path(html_path) if html_path else src.with_suffix(".html")
    raw = src.read_text(encoding="utf-8")

    # 1. Pre-render mermaid diagrams
    raw = prerender_mermaid(raw)

    # 2. Reduce font size if not already customised
    raw = _inject_font_size(raw, px=28)

    # 3. Write to a temp .md file next to the source (so relative paths work)
    tmp_md = src.with_name(f"_tmp_{src.name}")
    try:
        tmp_md.write_text(raw, encoding="utf-8")

        # 4. Run marp with Node 20 (avoids yargs ESM bug in Node 25)
        marp_cmd = (
            "source ~/.nvm/nvm.sh && nvm use 20 --silent && "
            f'marp --html --allow-local-files "{tmp_md.resolve()}" -o "{html_out.resolve()}"'
        )
        print(f"Running Marp → {html_out} …")
        res = subprocess.run(
            ["bash", "-c", marp_cmd],
            capture_output=True, text=True
        )
        if res.returncode == 0:
            post_process_html(html_out)
            print(f"✅ HTML saved: {html_out.resolve()}")
        else:
            print("❌ Marp error:")
            print(res.stderr or res.stdout)
    finally:
        tmp_md.unlink(missing_ok=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_html.py <input.md> [output.html]")
        sys.exit(1)
    md_to_html(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
