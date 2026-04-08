#!/usr/bin/env python3
"""Generate PESTEL → SWOT strategy flow diagram — clean version v3."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis('off')

BLUE_D  = '#1565C0'
BLUE_L  = '#1976D2'
GREEN_D = '#2E7D32'
GREEN_L = '#388E3C'
GREY_D  = '#37474F'
GREY_L  = '#546E7A'
RED_D   = '#BF360C'

# ── helpers ───────────────────────────────────────────────────────────────────

def box(ax, x, y, w, h, title, subtitle, fc, ec, tc='white',
        fontsize_t=11, fontsize_s=8.5):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.08",
                       facecolor=fc, edgecolor=ec, linewidth=2.0, zorder=3)
    ax.add_patch(p)
    if subtitle:
        ax.text(x, y + 0.2, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4)
        ax.text(x, y - 0.22, subtitle, ha='center', va='center',
                fontsize=fontsize_s, color=tc, alpha=0.92, zorder=4,
                multialignment='center')
    else:
        ax.text(x, y, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4,
                multialignment='center')

def step_badge(ax, x, y, num, fc):
    """Numbered badge placed OUTSIDE box, to the left."""
    c = Circle((x, y), 0.3, facecolor=fc, edgecolor='white',
               linewidth=2, zorder=6)
    ax.add_patch(c)
    ax.text(x, y, str(num), ha='center', va='center',
            fontsize=12, color='white', fontweight='bold', zorder=7)

def arrow_h(ax, x1, x2, y, color, label, lw=2.2):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=18), zorder=2)
    # label on white background box above arrow
    mx = (x1 + x2) / 2
    ax.text(mx, y + 0.28, label, ha='center', va='center',
            fontsize=8, color=color, style='italic', fontweight='bold',
            bbox=dict(facecolor='white', edgecolor='none', pad=2), zorder=5)

def arrow_diag(ax, x1, y1, x2, y2, color, lw=2.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=18), zorder=2)

def arrow_label_mid(ax, x1, y1, x2, y2, label, color):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx + 0.25, my, label, ha='left', va='center',
            fontsize=8, color=color, style='italic', fontweight='bold',
            bbox=dict(facecolor='white', edgecolor='none', pad=2), zorder=5)

# ── layout ────────────────────────────────────────────────────────────────────
y_top = 5.1   # macro row
y_bot = 2.4   # micro row
y_mid = 3.75  # SWOT center
x1, x2, x3, x4 = 1.8, 4.7, 8.2, 11.5
BW, BH = 2.4, 1.15
SW, SH = 2.4, 2.5
TW, TH = 2.2, 1.5

# ── background zones ──────────────────────────────────────────────────────────
for (bx, by, bw, bh, fc, ec, label, lc) in [
    (0.1, 4.1, 6.5, 2.5, '#EEF5FB', BLUE_D,  'Εξωτερικό Περιβάλλον (Macro)', BLUE_D),
    (0.1, 1.2, 6.5, 2.5, '#EEF8EE', GREEN_D, 'Εσωτερικό Περιβάλλον (Micro)', GREEN_D),
]:
    bg = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.05",
                        facecolor=fc, edgecolor=ec, linewidth=1.4,
                        linestyle='--', zorder=1)
    ax.add_patch(bg)
    ax.text(bx + 0.2, by + bh - 0.2, label,
            ha='left', va='center', fontsize=8.5, color=lc, fontweight='bold')

# ── Step 1: PESTEL ────────────────────────────────────────────────────────────
box(ax, x1, y_top, BW, BH,
    'PESTEL Ανάλυση',
    'P · E · S · T · E · L',
    BLUE_D, '#0D47A1', fontsize_t=11, fontsize_s=9)

# badge LEFT of box
step_badge(ax, x1 - BW/2 - 0.45, y_top, '1', BLUE_D)

arrow_h(ax, x1 + BW/2, x2 - BW/2, y_top, BLUE_D, 'εξάγει →')

box(ax, x2, y_top, BW, BH,
    'Ευκαιρίες (O)',
    'Απειλές (T)',
    BLUE_L, BLUE_D, fontsize_t=11, fontsize_s=10)

# ── Step 2: Εσωτερικός Έλεγχος ───────────────────────────────────────────────
box(ax, x1, y_bot, BW, BH,
    'Εσωτερικός Έλεγχος',
    'Πόροι · Ικανότητες · Απόδοση',
    GREEN_D, '#1B5E20', fontsize_t=11, fontsize_s=9)

step_badge(ax, x1 - BW/2 - 0.45, y_bot, '2', GREEN_D)

arrow_h(ax, x1 + BW/2, x2 - BW/2, y_bot, GREEN_D, 'εξάγει →')

box(ax, x2, y_bot, BW, BH,
    'Δυνάμεις (S)',
    'Αδυναμίες (W)',
    GREEN_L, GREEN_D, fontsize_t=11, fontsize_s=10)

# ── diagonal arrows → SWOT ───────────────────────────────────────────────────
arrow_diag(ax, x2 + BW/2, y_top - 0.15,
           x3 - SW/2,     y_mid + 0.6, GREY_D)
arrow_diag(ax, x2 + BW/2, y_bot + 0.15,
           x3 - SW/2,     y_mid - 0.6, GREY_D)

# single "συνθέτει" label between the two diagonals
ax.text(x2 + BW/2 + 0.55, y_mid, 'συνθέτει',
        ha='left', va='center', fontsize=8.5, color=GREY_D,
        style='italic', fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='none', pad=3), zorder=5)

# ── Step 3: SWOT box ──────────────────────────────────────────────────────────
swot_bg = FancyBboxPatch((x3 - SW/2, y_mid - SH/2), SW, SH,
                          boxstyle="round,pad=0.08",
                          facecolor=GREY_D, edgecolor='#263238',
                          linewidth=2.5, zorder=3)
ax.add_patch(swot_bg)

ax.text(x3, y_mid + 0.9, 'SWOT', ha='center', va='center',
        fontsize=15, color='white', fontweight='bold', zorder=4)

# 2×2 grid inside SWOT
for (lbl, gx, gy, gc) in [
    ('S  Δυνάμεις',  x3 - 0.57, y_mid + 0.28, '#43A047'),
    ('W  Αδυναμίες', x3 + 0.57, y_mid + 0.28, '#EF5350'),
    ('O  Ευκαιρίες', x3 - 0.57, y_mid - 0.42, '#1E88E5'),
    ('T  Απειλές',   x3 + 0.57, y_mid - 0.42, '#FB8C00'),
]:
    cell = FancyBboxPatch((gx - 0.52, gy - 0.26), 1.04, 0.52,
                          boxstyle="round,pad=0.03",
                          facecolor=gc, edgecolor='white',
                          linewidth=1.2, zorder=4)
    ax.add_patch(cell)
    ax.text(gx, gy, lbl, ha='center', va='center',
            fontsize=8, color='white', fontweight='bold', zorder=5)

step_badge(ax, x3 - SW/2 - 0.45, y_mid + SH/2 - 0.3, '3', GREY_L)

# ── Step 4: TOWS ──────────────────────────────────────────────────────────────
arrow_h(ax, x3 + SW/2, x4 - TW/2, y_mid, GREY_D, 'παράγει →')

box(ax, x4, y_mid, TW, TH,
    'Στρατηγικές\nΑποφάσεις',
    '(TOWS Matrix)',
    RED_D, '#8D2000', fontsize_t=11, fontsize_s=9.5)

step_badge(ax, x4 - TW/2 - 0.45, y_mid + TH/2 - 0.3, '4', RED_D)

# ── title & source ────────────────────────────────────────────────────────────
ax.text(6.5, 6.7, 'Από το Περιβάλλον στη Στρατηγική — Λογική Ακολουθία',
        ha='center', va='center', fontsize=12, color='#212121', fontweight='bold')

ax.text(0.5, 0.03,
        'Πηγή: Johnson, Scholes & Whittington (2008). Exploring Corporate Strategy.',
        ha='center', va='bottom', fontsize=7, color='#888888',
        transform=ax.transAxes)

fig.savefig('/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/pestel_swot_flow.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print("Saved: pestel_swot_flow.png")
