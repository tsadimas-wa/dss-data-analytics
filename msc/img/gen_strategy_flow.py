#!/usr/bin/env python3
"""Generate PESTEL → SWOT strategy flow diagram."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.axis('off')

# ── helpers ──────────────────────────────────────────────────────────────────

def box(ax, x, y, w, h, text, fc, ec, fontsize=10, tc='white', bold=False, radius=0.15):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle=f"round,pad=0.05,rounding_size={radius}",
                       facecolor=fc, edgecolor=ec, linewidth=1.8, zorder=3)
    ax.add_patch(p)
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=tc, fontweight=weight, multialignment='center', zorder=4)

def arrow(ax, x1, y1, x2, y2, color='#555555', lw=1.8):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=14),
                zorder=2)

def label_arrow(ax, x, y, text, fontsize=8, color='#555555'):
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=color, style='italic', zorder=4)

# ── background zones ──────────────────────────────────────────────────────────

# Macro zone
macro_bg = FancyBboxPatch((0.2, 4.2), 6.6, 2.4,
                           boxstyle="round,pad=0.1",
                           facecolor='#E3F2FD', edgecolor='#1565C0',
                           linewidth=1.5, linestyle='--', zorder=1)
ax.add_patch(macro_bg)
ax.text(0.55, 6.45, 'Εξωτερικό Περιβάλλον (Macro)',
        ha='left', va='center', fontsize=8.5, color='#1565C0', fontweight='bold')

# Micro zone
micro_bg = FancyBboxPatch((0.2, 1.6), 6.6, 2.4,
                           boxstyle="round,pad=0.1",
                           facecolor='#E8F5E9', edgecolor='#2E7D32',
                           linewidth=1.5, linestyle='--', zorder=1)
ax.add_patch(micro_bg)
ax.text(0.55, 3.85, 'Εσωτερικό Περιβάλλον (Micro)',
        ha='left', va='center', fontsize=8.5, color='#2E7D32', fontweight='bold')

# ── macro row ─────────────────────────────────────────────────────────────────

box(ax, 1.5, 5.5, 2.0, 0.75,
    'PESTEL\nΑνάλυση', '#1565C0', '#0D47A1', fontsize=9.5, bold=True)

ax.text(2.55, 5.5, 'σαρώνει\nP·E·S·T·E·L', ha='left', va='center',
        fontsize=7.5, color='#1565C0', style='italic')

box(ax, 5.5, 5.5, 2.2, 0.75,
    'Ευκαιρίες (O)\nΑπειλές (T)', '#1976D2', '#1565C0', fontsize=9, bold=True)

arrow(ax, 2.5, 5.5, 4.38, 5.5, color='#1565C0')

# ── micro row ─────────────────────────────────────────────────────────────────

box(ax, 1.5, 2.85, 2.2, 0.75,
    'Εσωτερικός\nΈλεγχος', '#2E7D32', '#1B5E20', fontsize=9.5, bold=True)

ax.text(2.65, 2.85, 'πόροι, ικανότητες,\nαπόδοση', ha='left', va='center',
        fontsize=7.5, color='#2E7D32', style='italic')

box(ax, 5.5, 2.85, 2.2, 0.75,
    'Δυνάμεις (S)\nΑδυναμίες (W)', '#388E3C', '#2E7D32', fontsize=9, bold=True)

arrow(ax, 2.6, 2.85, 4.38, 2.85, color='#2E7D32')

# ── arrows into SWOT ──────────────────────────────────────────────────────────

# O/T down
arrow(ax, 5.5, 5.12, 5.5, 4.42, color='#1565C0')
# S/W up
arrow(ax, 5.5, 3.22, 5.5, 3.62, color='#2E7D32')

# horizontal to SWOT
arrow(ax, 5.5, 4.02, 7.18, 4.02, color='#555555', lw=2)

# ── SWOT box ──────────────────────────────────────────────────────────────────

box(ax, 8.1, 4.02, 1.9, 1.1,
    'SWOT\nS · W · O · T', '#37474F', '#263238',
    fontsize=10, bold=True, radius=0.2)

# ── TOWS arrow + box ─────────────────────────────────────────────────────────

arrow(ax, 8.1, 3.47, 8.1, 2.62, color='#555555', lw=2)

box(ax, 8.1, 2.15, 2.3, 0.85,
    'Στρατηγικές\nΑποφάσεις\n(TOWS Matrix)', '#BF360C', '#8D2000',
    fontsize=8.5, bold=True, radius=0.15)

# ── step labels on left ───────────────────────────────────────────────────────
for step_y, num, txt, col in [
    (5.5,  '①', 'Σαρώνω\nεξωτερικό', '#1565C0'),
    (2.85, '②', 'Αξιολογώ\nεσωτερικό', '#2E7D32'),
    (4.02, '③', 'Συνθέτω\nSWOT',       '#555555'),
    (2.15, '④', 'Αποφασίζω\nστρατηγική','#BF360C'),
]:
    ax.text(0.32, step_y, num, ha='center', va='center',
            fontsize=13, color=col, fontweight='bold', zorder=4)

# ── legend ────────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(facecolor='#E3F2FD', edgecolor='#1565C0', label='Εξωτερικό (Macro)'),
    mpatches.Patch(facecolor='#E8F5E9', edgecolor='#2E7D32', label='Εσωτερικό (Micro)'),
    mpatches.Patch(facecolor='#37474F', edgecolor='#263238', label='Σύνθεση (SWOT)'),
    mpatches.Patch(facecolor='#BF360C', edgecolor='#8D2000', label='Στρατηγική (TOWS)'),
]
ax.legend(handles=legend_items, loc='lower left', fontsize=7.5,
          facecolor='#fafafa', edgecolor='#cccccc', framealpha=1.0,
          bbox_to_anchor=(0.0, 0.0))

fig.savefig('/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/pestel_swot_flow.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print("Saved: pestel_swot_flow.png")
