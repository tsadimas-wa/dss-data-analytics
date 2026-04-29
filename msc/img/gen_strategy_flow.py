#!/usr/bin/env python3
"""Generate PESTEL → SWOT strategy flow diagram — v4 (larger fonts, fixed overlaps)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

fig, ax = plt.subplots(figsize=(16, 8))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 16)
ax.set_ylim(0, 8)
ax.axis('off')

BLUE_D  = '#1565C0'
BLUE_L  = '#1976D2'
GREEN_D = '#2E7D32'
GREEN_L = '#388E3C'
GREY_D  = '#37474F'
GREY_L  = '#546E7A'
RED_D   = '#BF360C'

def box(ax, x, y, w, h, title, subtitle, fc, ec, tc='white',
        fontsize_t=13, fontsize_s=10):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.08",
                       facecolor=fc, edgecolor=ec, linewidth=2.0, zorder=3)
    ax.add_patch(p)
    if subtitle:
        ax.text(x, y + 0.22, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4)
        ax.text(x, y - 0.26, subtitle, ha='center', va='center',
                fontsize=fontsize_s, color=tc, alpha=0.92, zorder=4,
                multialignment='center')
    else:
        ax.text(x, y, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4,
                multialignment='center')

def step_badge(ax, x, y, num, fc):
    c = Circle((x, y), 0.32, facecolor=fc, edgecolor='white',
               linewidth=2, zorder=6)
    ax.add_patch(c)
    ax.text(x, y, str(num), ha='center', va='center',
            fontsize=13, color='white', fontweight='bold', zorder=7)

def arrow_h(ax, x1, x2, y, color, label, lw=2.2):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=20), zorder=2)
    mx = (x1 + x2) / 2
    # labels go below the arrow to avoid overlapping box titles above
    ax.text(mx, y - 0.38, label, ha='center', va='center',
            fontsize=10, color=color, style='italic', fontweight='bold',
            bbox=dict(facecolor='white', edgecolor='none', pad=2), zorder=5)

def arrow_diag(ax, x1, y1, x2, y2, color, lw=2.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=20), zorder=2)

# ── layout ────────────────────────────────────────────────────────────────────
y_top = 5.9
y_bot = 2.9
y_mid = 4.4
x1, x2, x3, x4 = 2.5, 7.0, 11.0, 14.7
BW, BH = 2.8, 1.3
SW, SH = 2.6, 2.8
TW, TH = 2.0, 1.7

# ── background zones ──────────────────────────────────────────────────────────
for (bx, by, bw, bh, fc, ec, label, lc) in [
    (0.1, 4.8, 9.3, 2.6, '#EEF5FB', BLUE_D,  'Εξωτερικό Περιβάλλον (Macro)', BLUE_D),
    (0.1, 1.6, 9.3, 2.8, '#EEF8EE', GREEN_D, 'Εσωτερικό Περιβάλλον (Micro)', GREEN_D),
]:
    bg = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.05",
                        facecolor=fc, edgecolor=ec, linewidth=1.4,
                        linestyle='--', zorder=1)
    ax.add_patch(bg)
    ax.text(bx + 0.2, by + bh - 0.2, label,
            ha='left', va='center', fontsize=10, color=lc, fontweight='bold')

# ── Step 1: PESTEL ────────────────────────────────────────────────────────────
box(ax, x1, y_top, BW, BH,
    'PESTEL Ανάλυση', 'P · E · S · T · E · L',
    BLUE_D, '#0D47A1', fontsize_t=13, fontsize_s=10)

step_badge(ax, x1 - BW/2 - 0.45, y_top, '1', BLUE_D)
arrow_h(ax, x1 + BW/2, x2 - BW/2, y_top, BLUE_D, 'εξάγει →')

box(ax, x2, y_top, BW, BH,
    'Ευκαιρίες (O)', '& Απειλές (T)',
    BLUE_L, BLUE_D, fontsize_t=13, fontsize_s=11)

# ── Step 2: Εσωτερικός Έλεγχος ───────────────────────────────────────────────
box(ax, x1, y_bot, BW, BH,
    'Εσωτερικός Έλεγχος', 'Πόροι · Ικανότητες · Απόδοση',
    GREEN_D, '#1B5E20', fontsize_t=13, fontsize_s=10)

step_badge(ax, x1 - BW/2 - 0.45, y_bot, '2', GREEN_D)
arrow_h(ax, x1 + BW/2, x2 - BW/2, y_bot, GREEN_D, 'εξάγει →')

box(ax, x2, y_bot, BW, BH,
    'Δυνάμεις (S)', 'Αδυναμίες (W)',
    GREEN_L, GREEN_D, fontsize_t=13, fontsize_s=11)

# ── diagonal arrows → SWOT ───────────────────────────────────────────────────
arrow_diag(ax, x2 + BW/2, y_top - 0.15, x3 - SW/2, y_mid + 0.6, GREY_D)
arrow_diag(ax, x2 + BW/2, y_bot + 0.15, x3 - SW/2, y_mid - 0.6, GREY_D)

ax.text(x2 + BW/2 + 0.7, y_mid, 'συνθέτει',
        ha='left', va='center', fontsize=10, color=GREY_D,
        style='italic', fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='none', pad=3), zorder=5)

# ── Step 3: SWOT box ──────────────────────────────────────────────────────────
swot_bg = FancyBboxPatch((x3 - SW/2, y_mid - SH/2), SW, SH,
                          boxstyle="round,pad=0.08",
                          facecolor=GREY_D, edgecolor='#263238',
                          linewidth=2.5, zorder=3)
ax.add_patch(swot_bg)

ax.text(x3, y_mid + 1.0, 'SWOT', ha='center', va='center',
        fontsize=17, color='white', fontweight='bold', zorder=4)

cell_w, cell_h = 1.1, 0.54
for (lbl, gx, gy, gc) in [
    ('S  Δυνάμεις',  x3 - 0.62, y_mid + 0.30, '#43A047'),
    ('W  Αδυναμίες', x3 + 0.62, y_mid + 0.30, '#EF5350'),
    ('O  Ευκαιρίες', x3 - 0.62, y_mid - 0.45, '#1E88E5'),
    ('T  Απειλές',   x3 + 0.62, y_mid - 0.45, '#FB8C00'),
]:
    cell = FancyBboxPatch((gx - cell_w/2, gy - cell_h/2), cell_w, cell_h,
                          boxstyle="round,pad=0.03",
                          facecolor=gc, edgecolor='white',
                          linewidth=1.2, zorder=4)
    ax.add_patch(cell)
    ax.text(gx, gy, lbl, ha='center', va='center',
            fontsize=9.5, color='white', fontweight='bold', zorder=5)

step_badge(ax, x3 - SW/2 - 0.45, y_mid + SH/2 - 0.35, '3', GREY_L)

# ── Step 4: TOWS ─────────────────────────────────────────────────────────────
# badge placed below-left of TOWS to stay clear of the arrow label
arrow_h(ax, x3 + SW/2, x4 - TW/2, y_mid, GREY_D, 'παράγει →')

box(ax, x4, y_mid, TW, TH,
    'Στρατηγικές\nΑποφάσεις', '(TOWS Matrix)',
    RED_D, '#8D2000', fontsize_t=13, fontsize_s=10)

# badge above the arrow, clear of the label which sits below
step_badge(ax, x3 + SW/2 + 0.5, y_mid + 0.55, '4', RED_D)

# ── title & source ────────────────────────────────────────────────────────────
ax.text(8.0, 7.6, 'Από το Περιβάλλον στη Στρατηγική — Λογική Ακολουθία',
        ha='center', va='center', fontsize=14, color='#212121', fontweight='bold')

ax.text(0.5, 0.03,
        'Πηγή: Johnson, Scholes & Whittington (2008). Exploring Corporate Strategy.',
        ha='center', va='bottom', fontsize=8, color='#888888',
        transform=ax.transAxes)

fig.savefig('/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/pestel_swot_flow.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print("Saved: pestel_swot_flow.png")
