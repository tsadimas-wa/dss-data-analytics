import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

fig, ax = plt.subplots(figsize=(13, 5.5))
ax.set_xlim(0, 13)
ax.set_ylim(0, 5.5)
ax.axis('off')

# ── colours ───────────────────────────────────────────────────────────────────
C_CHANCE   = '#1565C0'   # ellipse  — chance node
C_DECISION = '#2E7D32'   # rect     — decision node
C_UTILITY  = '#F57F17'   # diamond  — utility node

# ── helpers ───────────────────────────────────────────────────────────────────
def chance_node(ax, cx, cy, title, sub='', r=0.85):
    """Ellipse — chance / random variable."""
    ell = mpatches.Ellipse((cx, cy), 2*r, 1.4,
                            facecolor=C_CHANCE, edgecolor='white',
                            linewidth=2.5, zorder=3)
    ax.add_patch(ell)
    ax.text(cx, cy + 0.15, title, ha='center', va='center',
            fontsize=10.5, color='white', fontweight='bold', zorder=4)
    if sub:
        ax.text(cx, cy - 0.28, sub, ha='center', va='center',
                fontsize=8.5, color='#BBDEFB', zorder=4)

def decision_node(ax, cx, cy, title, sub='', w=2.1, h=1.1):
    """Rectangle — decision node."""
    rect = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='square,pad=0.05',
        facecolor=C_DECISION, edgecolor='white',
        linewidth=2.5, zorder=3)
    ax.add_patch(rect)
    ax.text(cx, cy + 0.14, title, ha='center', va='center',
            fontsize=10.5, color='white', fontweight='bold', zorder=4)
    if sub:
        ax.text(cx, cy - 0.25, sub, ha='center', va='center',
                fontsize=8.5, color='#C8E6C9', zorder=4)

def utility_node(ax, cx, cy, title, sub='', size=0.72):
    """Diamond — utility node."""
    diamond = plt.Polygon(
        [(cx, cy + size), (cx + size*1.5, cy),
         (cx, cy - size), (cx - size*1.5, cy)],
        closed=True,
        facecolor=C_UTILITY, edgecolor='white',
        linewidth=2.5, zorder=3)
    ax.add_patch(diamond)
    ax.text(cx, cy + 0.12, title, ha='center', va='center',
            fontsize=10.5, color='white', fontweight='bold', zorder=4)
    if sub:
        ax.text(cx, cy - 0.22, sub, ha='center', va='center',
                fontsize=8.5, color='#FFF9C4', zorder=4)

def arrow(ax, x1, y1, x2, y2, off1=0.0, off2=0.0, color='#37474F', lw=2.2, dashed=False):
    dx, dy = x2-x1, y2-y1
    L = np.hypot(dx, dy)
    ux, uy = dx/L, dy/L
    ls = (0, (5, 4)) if dashed else 'solid'
    ax.annotate('', xy=(x2 - ux*off2, y2 - uy*off2),
                    xytext=(x1 + ux*off1, y1 + uy*off1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                linestyle=ls, mutation_scale=20), zorder=2)

# ══════════════════════════════════════════════════════════════════════════════
# Nodes (medical treatment influence diagram)
# ══════════════════════════════════════════════════════════════════════════════
#   (Disease) ──→ [Test Result] ──→ □Treatment ──→ ◆Utility
#        │                               ↑
#        └───────────────────────────────┘  (direct influence)

nodes = {
    'disease':   (2.0,  3.5),
    'test':      (5.2,  3.5),
    'treat':     (8.4,  3.5),
    'utility':   (11.5, 3.5),
}

chance_node  (ax, *nodes['disease'], 'Disease',          'P(D) = 0.30')
chance_node  (ax, *nodes['test'],    'Test\nResult',     'P(T|D)')
decision_node(ax, *nodes['treat'],   'Treatment;',       'Yes / No / Surgery')
utility_node (ax, *nodes['utility'], 'Utility',          'EU = Σ P·U')

# ── main causal arrows ────────────────────────────────────────────────────────
arrow(ax, 2.85, 3.5, 4.35, 3.5, off2=0.0)   # disease → test
arrow(ax, 6.05, 3.5, 7.35, 3.5)             # test → treat
arrow(ax, 9.45, 3.5, 10.42, 3.5)            # treat → utility

# ── direct influence arc: disease → utility (dashed, below) ──────────────────
arrow(ax, 2.0, 2.8, 11.5, 2.8, off1=0.0, off2=0.0, color='#78909C', lw=1.8, dashed=True)
ax.annotate('', xy=(11.5, 2.8), xytext=(11.5, 2.82),
            arrowprops=dict(arrowstyle='->', color='#78909C', lw=1.8,
                            mutation_scale=18), zorder=2)
# curved connection line disease ↓ and utility ↓
ax.annotate("", xy=(2.0, 2.80), xytext=(2.0, 3.50 - 0.70),
            arrowprops=dict(arrowstyle='-', color='#78909C', lw=1.8), zorder=2)
ax.annotate("", xy=(11.5, 2.80), xytext=(11.5, 3.50 - 0.70),
            arrowprops=dict(arrowstyle='-', color='#78909C', lw=1.8), zorder=2)
ax.text(6.75, 2.55, 'direct influence of disease on utility',
        ha='center', fontsize=8.5, color='#78909C', style='italic')

# ── information arc: disease → treat (dashed, above) ─────────────────────────
# arc over the top: disease → treat
ax.annotate("", xy=(8.4, 4.10), xytext=(2.0, 4.10),
            arrowprops=dict(arrowstyle='->', color='#B0BEC5', lw=1.5,
                            linestyle=(0,(4,3)), mutation_scale=16), zorder=2)
ax.annotate("", xy=(2.0, 4.10), xytext=(2.0, 3.5+0.70),
            arrowprops=dict(arrowstyle='-', color='#B0BEC5', lw=1.5), zorder=2)
ax.annotate("", xy=(8.4, 4.10), xytext=(8.4, 3.5+0.55),
            arrowprops=dict(arrowstyle='-', color='#B0BEC5', lw=1.5), zorder=2)
ax.text(5.2, 4.35, 'information available at decision time',
        ha='center', fontsize=8.5, color='#78909C', style='italic')

# ══════════════════════════════════════════════════════════════════════════════
# EU table (bottom right)
# ══════════════════════════════════════════════════════════════════════════════
tbl_x, tbl_y = 6.8, 2.2
ax.text(tbl_x, tbl_y, 'Expected Utility (EU) per option:',
        ha='center', fontsize=9.5, fontweight='bold', color='#37474F')

rows = [
    ('Treatment A',    'EU = 0.30×80 + 0.70×(-10) = +17'),
    ('Treatment B',    'EU = 0.30×60 + 0.70×(+5)  = +21.5  ✓'),
    ('No treatment',   'EU = 0.30×(-50)+ 0.70×10  = −8'),
]
row_colors = ['#E8F5E9', '#C8E6C9', '#FFEBEE']
for i, (opt, eu) in enumerate(rows):
    ry = tbl_y - 0.38 * (i + 1)
    bg = row_colors[i]
    rect = mpatches.FancyBboxPatch((3.5, ry - 0.16), 6.6, 0.32,
                                    boxstyle='round,pad=0.04',
                                    facecolor=bg, edgecolor='#ccc',
                                    linewidth=0.8, zorder=3)
    ax.add_patch(rect)
    ax.text(3.7,  ry, opt, ha='left',   va='center', fontsize=9,   color='#212121', zorder=4)
    ax.text(10.0, ry, eu,  ha='right',  va='center', fontsize=9,   color='#1B5E20' if '✓' in eu else '#37474F',
            fontweight='bold' if '✓' in eu else 'normal', zorder=4)

# ══════════════════════════════════════════════════════════════════════════════
# Legend
# ══════════════════════════════════════════════════════════════════════════════
legend_items = [
    mpatches.Patch(color=C_CHANCE,   label='Chance node — random variable (ellipse)'),
    mpatches.Patch(color=C_DECISION, label='Decision node (rectangle)'),
    mpatches.Patch(color=C_UTILITY,  label='Utility node (diamond)'),
]
ax.legend(handles=legend_items, loc='upper left', fontsize=9,
          framealpha=0.9, edgecolor='#ccc', ncol=3,
          bbox_to_anchor=(0.0, 1.0))

ax.set_title('Influence Diagram — Medical Treatment Decision',
             fontsize=13, fontweight='bold', pad=28)

fig.tight_layout()
out = 'lectures_material/influence_diagram_en.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'Saved: {out}')
