import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 10)
ax.set_ylim(-0.2, 6.8)
ax.axis('off')

# Node definitions: name, (x, y), color, prob label (shown below node)
nodes = {
    'history':  ('Ιστορικό\nΠληρωμών',     (1.8, 5.4), '#1565C0',
                 'P(Καλό)=0.70\nP(Κακό)=0.30'),
    'income':   ('Εισόδημα',                (8.2, 5.4), '#1565C0',
                 'P(Υψηλό)=0.45\nP(Χαμηλό)=0.55'),
    'credit':   ('Πιστοληπτική\nΙκανότητα', (3.0, 3.4), '#6A1B9A',
                 'P(Υψηλή|Καλό)=0.85\nP(Υψηλή|Κακό)=0.20'),
    'debt':     ('Αναλογία\nΧρέους',        (7.2, 3.4), '#6A1B9A',
                 'P(Χαμηλή|Υψηλό)=0.78\nP(Χαμηλή|Χαμηλό)=0.30'),
    'risk':     ('Ρίσκο\nΔανείου',          (5.1, 1.6), '#B71C1C',
                 'βλ. CPT →'),
    'approval': ('Απόφαση\nΈγκρισης',       (5.1, 0.3), '#2E7D32',
                 'P(Εγκρ.|Χαμηλό)=0.90\nP(Εγκρ.|Υψηλό)=0.05'),
}

# Draw nodes + probability labels
node_patches = {}
for key, (label, (x, y), color, prob) in nodes.items():
    box = mpatches.FancyBboxPatch(
        (x - 1.05, y - 0.42), 2.10, 0.84,
        boxstyle='round,pad=0.08',
        facecolor=color, edgecolor='white', linewidth=2,
        alpha=0.93, zorder=3
    )
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center',
            fontsize=16, color='white', fontweight='bold', zorder=4)
    # Probability label below node
    ax.text(x, y - 0.60, prob, ha='center', va='top',
            fontsize=10, color='#37474F',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F5F5F5',
                      edgecolor=color, linewidth=0.8, alpha=0.9),
            zorder=4)
    node_patches[key] = (x, y)

# Draw edges with arrows
edges = [
    ('history', 'credit'),
    ('income',  'debt'),
    ('credit',  'risk'),
    ('debt',    'risk'),
    ('risk',    'approval'),
]

def arrow(ax, x1, y1, x2, y2, dy_start=0.45, dy_end=0.45):
    # Adjust start/end to box edges
    dx = x2 - x1
    dy = y2 - y1
    length = np.sqrt(dx**2 + dy**2)
    ux, uy = dx/length, dy/length
    sx = x1 + ux * 1.05
    sy = y1 - uy * dy_start + uy * 0.05 if dy < 0 else y1 - uy * dy_start
    # simpler: just from bottom of source to top of target
    start = (x1, y1 - 0.46)
    end   = (x2, y2 + 0.46)
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color='#37474F',
                                lw=2.2, mutation_scale=18),
                zorder=2)

# Custom edge routing
arrow(ax, *node_patches['history'], *node_patches['credit'])
arrow(ax, *node_patches['income'],  *node_patches['debt'])
arrow(ax, *node_patches['credit'],  *node_patches['risk'])
arrow(ax, *node_patches['debt'],    *node_patches['risk'])
arrow(ax, *node_patches['risk'],    *node_patches['approval'])

# CPT mini-table next to Ρίσκο node
cpt_x, cpt_y = 8.5, 1.6
ax.text(cpt_x, cpt_y + 0.7, 'CPT — P(Ρίσκο = Υψηλό)', fontsize=12,
        ha='center', fontweight='bold', color='#B71C1C')
rows = [
    ('Πιστοληπτ.', 'Αναλογία', 'P'),
    ('Χαμηλή',     'Υψηλή',    '0.92'),
    ('Χαμηλή',     'Χαμηλή',   '0.65'),
    ('Υψηλή',      'Υψηλή',    '0.40'),
    ('Υψηλή',      'Χαμηλή',   '0.08'),
]
col_x = [cpt_x - 0.85, cpt_x + 0.05, cpt_x + 0.82]
for i, row in enumerate(rows):
    y_row = cpt_y + 0.35 - i * 0.22
    bold = i == 0
    bg = '#FFEBEE' if i % 2 == 0 and i > 0 else ('#FAFAFA' if i > 0 else '#FFCDD2')
    if i > 0:
        rect = mpatches.FancyBboxPatch((col_x[0]-0.3, y_row-0.10), 2.3, 0.20,
                                        boxstyle='square,pad=0', facecolor=bg,
                                        edgecolor='none', zorder=1)
        ax.add_patch(rect)
    for cx, val in zip(col_x, row):
        ax.text(cx, y_row, val, ha='center', va='center',
                fontsize=9, fontweight='bold' if bold else 'normal',
                color='#212121')

# Legend
legend_items = [
    mpatches.Patch(color='#1565C0', label='Παρατηρούμενη μεταβλητή (root)'),
    mpatches.Patch(color='#6A1B9A', label='Ενδιάμεση μεταβλητή'),
    mpatches.Patch(color='#B71C1C', label='Κόμβος κινδύνου'),
    mpatches.Patch(color='#2E7D32', label='Έξοδος (απόφαση)'),
]
ax.legend(handles=legend_items, loc='lower left', fontsize=12,
          framealpha=0.9, edgecolor='#ccc')

# ax.set_title('Δίκτυο Bayes — Αξιολόγηση Πιστωτικού Ρίσκου', fontsize=18,
#              fontweight='bold', pad=10)

fig.tight_layout()
out = 'lectures_material/bayes_credit_net.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'Saved: {out}')
