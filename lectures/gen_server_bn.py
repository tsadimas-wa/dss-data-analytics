import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── colours ───────────────────────────────────────────────────────────────────
C_ROOT  = '#1565C0'
C_INTER = '#6A1B9A'
C_OBS   = '#2E7D32'
C_POST  = '#B71C1C'

def draw_node(ax, cx, cy, title, subtitle, color, w=2.6, h=0.90):
    box = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='round,pad=0.1',
        facecolor=color, edgecolor='white', linewidth=2.5,
        alpha=0.93, zorder=3)
    ax.add_patch(box)
    ax.text(cx, cy + 0.14, title,    ha='center', va='center',
            fontsize=12, color='white', fontweight='bold', zorder=4)
    ax.text(cx, cy - 0.22, subtitle, ha='center', va='center',
            fontsize=9.5, color='#E3F2FD', zorder=4)

def arrow(ax, x1, y1, x2, y2, off=0.47):
    dx, dy = x2-x1, y2-y1
    L = np.hypot(dx, dy)
    ux, uy = dx/L, dy/L
    ax.annotate('', xy=(x2 - ux*off, y2 - uy*off),
                    xytext=(x1 + ux*off, y1 + uy*off),
                arrowprops=dict(arrowstyle='->', color='#455A64',
                                lw=2.5, mutation_scale=22), zorder=2)

# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 1 — Network graph
# ══════════════════════════════════════════════════════════════════════════════
fig1, ax = plt.subplots(figsize=(9, 7))
ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.axis('off')

pos = {'D': (2.0, 6.5), 'H': (6.0, 6.5), 'A': (4.0, 4.5), 'P': (4.0, 2.3)}

draw_node(ax, *pos['D'], 'D — Επίθεση DDoS',      'prior: P(D=T) = 0.02', C_ROOT)
draw_node(ax, *pos['H'], 'H — Αστοχία Hardware',   'prior: P(H=T) = 0.05', C_ROOT)
draw_node(ax, *pos['A'], 'A — Αργή Απόκριση',      'P(A | D, H)  ← CPT 2', C_INTER)
draw_node(ax, *pos['P'], 'P — Παράπονα Χρηστών',
          '✦  observed evidence: P = T\nP(P | A)  ← CPT 3', C_OBS)

arrow(ax, *pos['D'], *pos['A'])
arrow(ax, *pos['H'], *pos['A'])
arrow(ax, *pos['A'], *pos['P'])

# Posterior result boxes
ax.text(4.0, 1.15, 'Posterior — δεδομένου P = T', ha='center',
        fontsize=11, fontweight='bold', color=C_POST)
for xi, lbl, col in [
    (2.0, 'P(D=T | P=T)\n≈ 15.6%', '#E53935'),
    (6.0, 'P(H=T | P=T)\n≈ 33.2%', '#1565C0'),
]:
    rb = mpatches.FancyBboxPatch((xi-1.4, 0.2), 2.8, 0.75,
                                  boxstyle='round,pad=0.08',
                                  facecolor='#FFF3E0', edgecolor=col,
                                  linewidth=2, zorder=3)
    ax.add_patch(rb)
    ax.text(xi, 0.575, lbl, ha='center', va='center',
            fontsize=10.5, color=col, fontweight='bold', zorder=4)

legend = [
    mpatches.Patch(color=C_ROOT,  label='Root — prior γνωστό'),
    mpatches.Patch(color=C_INTER, label='Ενδιάμεση — CPT 2'),
    mpatches.Patch(color=C_OBS,   label='Observed evidence — CPT 3'),
]
ax.legend(handles=legend, loc='lower left', fontsize=9.5,
          framealpha=0.9, edgecolor='#ccc')

ax.set_title('Δίκτυο Bayes — Διάγνωση Server', fontsize=14,
             fontweight='bold', pad=10)

fig1.tight_layout()
fig1.savefig('lectures_material/server_bn_graph.png', dpi=150, bbox_inches='tight')
print('Saved: server_bn_graph.png')

# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 2 — CPT tables
# ══════════════════════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(10, 5.5))
ax2.axis('off')

H_HDR = '#37474F'   # header bg
COLS   = {'root': ['#E3F2FD', '#E8EAF6'],
          'A':    ['#F3E5F5', '#EDE7F6', '#F3E5F5', '#EDE7F6'],
          'P':    ['#E8F5E9', '#C8E6C9']}

def cell(ax, x, y, w, h, text, bg, fg='#212121', bold=False, fs=10):
    r = mpatches.FancyBboxPatch((x, y), w, h,
                                 boxstyle='square,pad=0',
                                 facecolor=bg, edgecolor='white',
                                 linewidth=1.0, transform=ax.transAxes, zorder=3)
    ax.add_patch(r)
    ax.text(x + w/2, y + h/2, text, transform=ax.transAxes,
            ha='center', va='center', fontsize=fs,
            color=fg, fontweight='bold' if bold else 'normal', zorder=4)

def table(ax, title, headers, rows, row_colors, x0, y0, col_widths, rh=0.085):
    ax.text(x0, y0 + 0.015, title, transform=ax.transAxes,
            fontsize=11, fontweight='bold', color='#1A237E', va='bottom')
    y0 -= 0.005
    # header
    cx = x0
    for h, cw in zip(headers, col_widths):
        cell(ax, cx, y0 - rh, cw, rh, h, H_HDR, fg='white', bold=True, fs=9.5)
        cx += cw
    # rows
    for ri, (row, rc) in enumerate(zip(rows, row_colors)):
        ry = y0 - rh * (ri + 2)
        cx = x0
        for val, cw in zip(row, col_widths):
            cell(ax, cx, ry, cw, rh, val, rc, fs=10)
            cx += cw
    return y0 - rh * (len(rows) + 2) - 0.05

# ── CPT 1 ─────────────────────────────────────────────────────────────────────
y = 0.92
y = table(ax2, 'CPT 1 — Priors (ανεξάρτητες μεταβλητές)',
          ['Μεταβλητή', 'P( = T)', 'P( = F)'],
          [['D — Επίθεση DDoS',     '0.02', '0.98'],
           ['H — Αστοχία Hardware', '0.05', '0.95']],
          COLS['root'],
          x0=0.04, y0=y, col_widths=[0.50, 0.23, 0.23])

# ── CPT 2 ─────────────────────────────────────────────────────────────────────
y = table(ax2, 'CPT 2 — P(A = T | D, H)',
          ['D', 'H', 'P(A = T)', 'P(A = F)'],
          [['F', 'F', '0.01', '0.99'],
           ['F', 'T', '0.80', '0.20'],
           ['T', 'F', '0.90', '0.10'],
           ['T', 'T', '0.95', '0.05']],
          COLS['A'],
          x0=0.04, y0=y, col_widths=[0.18, 0.18, 0.27, 0.27])

# ── CPT 3 ─────────────────────────────────────────────────────────────────────
table(ax2, 'CPT 3 — P(P = T | A)',
      ['A', 'P(P = T)', 'P(P = F)'],
      [['F', '0.05', '0.95'],
       ['T', '0.85', '0.15']],
      COLS['P'],
      x0=0.04, y0=y, col_widths=[0.18, 0.27, 0.27])

ax2.set_title('Πίνακες Δεσμευμένων Πιθανοτήτων (CPT)', fontsize=13,
              fontweight='bold', pad=10)

fig2.tight_layout()
fig2.savefig('lectures_material/server_bn_cpts.png', dpi=150, bbox_inches='tight')
print('Saved: server_bn_cpts.png')
