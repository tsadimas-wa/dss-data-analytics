#!/usr/bin/env python3
"""Generate management theory evolution timeline."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(1880, 2030)
ax.set_ylim(0, 9)
ax.axis('off')

ax.set_title("Εξέλιξη της Θεωρίας Διοίκησης", color='#1a1a1a',
             fontsize=14, fontweight='bold', pad=14)

# ── timeline axis ─────────────────────────────────────────────────────────────
ax.annotate('', xy=(2028, 1.0), xytext=(1882, 1.0),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2.0))

for yr in [1900, 1920, 1940, 1960, 1980, 2000, 2020]:
    ax.plot([yr, yr], [0.85, 1.15], color='#555555', lw=1.2)
    ax.text(yr, 0.55, str(yr), ha='center', va='center',
            fontsize=8.5, color='#555555')

# ── schools: (name, key_figures, start, end, y_center, color) ─────────────────
schools = [
    ("Επιστημονικό Management",   "Taylor · Smith · Gilbreth",   1890, 2025, 8.0, '#1565C0'),
    ("Διοικητική / Γραφειοκρατία","Fayol · Weber",               1910, 2025, 6.7, '#6A1B9A'),
    ("Ανθρωπίνων Σχέσεων",        "Mayo · Follett · Hawthorne",  1930, 2025, 5.4, '#2E7D32'),
    ("Ποσοτική Προσέγγιση",        "OR · MIS · Simulation",       1950, 2025, 4.1, '#E65100'),
    ("Συστημική Θεωρία",           "von Bertalanffy · Katz",      1960, 2025, 2.8, '#00838F'),
    ("Contingency Theory",         "Burns & Stalker · Lawrence",  1970, 2025, 1.7, '#558B2F'),
]

for name, figures, start, end, yc, color in schools:
    # horizontal bar
    bar_len = end - start
    bar = FancyBboxPatch((start, yc - 0.38), bar_len, 0.76,
                         boxstyle="round,pad=0.04",
                         facecolor=color, edgecolor='white',
                         linewidth=1.2, alpha=0.88, zorder=3)
    ax.add_patch(bar)

    # start dot
    ax.plot(start, yc, 'o', color='white', markersize=7,
            markeredgecolor=color, markeredgewidth=2, zorder=4)

    # label inside bar
    ax.text(start + 2, yc + 0.1, name,
            ha='left', va='center', fontsize=9, color='white',
            fontweight='bold', zorder=5)
    ax.text(start + 2, yc - 0.17, figures,
            ha='left', va='center', fontsize=7.5, color='white',
            alpha=0.92, zorder=5)

    # year label at start
    ax.text(start, yc - 0.58, str(start),
            ha='center', va='center', fontsize=7.5, color=color,
            fontweight='bold')

# ── "σήμερα" marker ───────────────────────────────────────────────────────────
ax.plot([2025, 2025], [1.2, 8.4], color='#BF360C',
        lw=1.5, linestyle='--', zorder=2, alpha=0.6)
ax.text(2025, 8.6, 'Σήμερα', ha='center', va='center',
        fontsize=8, color='#BF360C', fontweight='bold')

ax.text(0.5, 0.04,
        "Πηγή: Robbins & Coulter (2018). Management, 14th ed. Pearson.",
        ha='center', va='bottom', fontsize=7, color='#888888',
        transform=ax.transAxes)

fig.savefig('/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/mgmt_timeline.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print("Saved: mgmt_timeline.png")
