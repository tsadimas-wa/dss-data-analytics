#!/usr/bin/env python3
"""Generate PESTEL → SWOT strategy flow diagram — clean version."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

fig, ax = plt.subplots(figsize=(12, 6.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 12)
ax.set_ylim(0, 6.5)
ax.axis('off')

# ── helpers ───────────────────────────────────────────────────────────────────

def box(ax, x, y, w, h, title, subtitle, fc, ec, tc='white', fontsize_t=11, fontsize_s=8.5):
    p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.08",
                       facecolor=fc, edgecolor=ec, linewidth=2.0, zorder=3)
    ax.add_patch(p)
    if subtitle:
        ax.text(x, y + 0.18, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4)
        ax.text(x, y - 0.28, subtitle, ha='center', va='center',
                fontsize=fontsize_s, color=tc, alpha=0.9, zorder=4,
                multialignment='center')
    else:
        ax.text(x, y, title, ha='center', va='center',
                fontsize=fontsize_t, color=tc, fontweight='bold', zorder=4,
                multialignment='center')

def step_circle(ax, x, y, num, fc, ec):
    c = Circle((x, y), 0.28, facecolor=fc, edgecolor=ec,
               linewidth=2, zorder=5)
    ax.add_patch(c)
    ax.text(x, y, str(num), ha='center', va='center',
            fontsize=11, color='white', fontweight='bold', zorder=6)

def arrow_h(ax, x1, x2, y, color, lw=2.2):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=18),
                zorder=2)

def arrow_diag(ax, x1, y1, x2, y2, color, lw=2.2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=18),
                zorder=2)

# ── layout constants ──────────────────────────────────────────────────────────
# 4-column layout: [Step1] → [Result1]  ↘
#                                          [SWOT] → [TOWS]
#                  [Step2] → [Result2]  ↗

y_top   = 4.6   # macro row
y_bot   = 2.0   # micro row
y_mid   = 3.3   # SWOT vertical center
x1, x2, x3, x4 = 1.5, 4.1, 7.3, 10.5

BW, BH     = 2.2, 1.1   # standard box width/height
RW, RH     = 2.2, 1.1
SW, SH     = 2.2, 2.4   # SWOT box (tall)
TW, TH     = 2.2, 1.4   # TOWS box

BLUE_D  = '#1565C0'
BLUE_L  = '#1976D2'
GREEN_D = '#2E7D32'
GREEN_L = '#388E3C'
GREY_D  = '#37474F'
GREY_L  = '#546E7A'
RED_D   = '#BF360C'
RED_L   = '#E64A19'

# ── background zones ──────────────────────────────────────────────────────────
for (bx, by, bw, bh, fc, ec, label, lc) in [
    (0.15, 3.5,  5.7, 2.3, '#EEF5FB', BLUE_D,  'Εξωτερικό Περιβάλλον (Macro)',  BLUE_D),
    (0.15, 1.0,  5.7, 2.3, '#EEF8EE', GREEN_D, 'Εσωτερικό Περιβάλλον (Micro)', GREEN_D),
]:
    bg = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.05",
                        facecolor=fc, edgecolor=ec, linewidth=1.4,
                        linestyle='--', zorder=1)
    ax.add_patch(bg)
    ax.text(bx + 0.18, by + bh - 0.22, label,
            ha='left', va='center', fontsize=8, color=lc, fontweight='bold')

# ── Step 1: PESTEL ────────────────────────────────────────────────────────────
box(ax, x1, y_top, BW, BH,
    'PESTEL Ανάλυση',
    'Political · Economic\nSocial · Tech · Env · Legal',
    BLUE_D, '#0D47A1', fontsize_t=10.5, fontsize_s=7.5)
step_circle(ax, x1 - BW/2 + 0.28, y_top + BH/2 - 0.28, '1', BLUE_D, '#0D47A1')

arrow_h(ax, x1 + BW/2, x2 - RW/2, y_top, BLUE_D)
ax.text((x1 + BW/2 + x2 - RW/2)/2, y_top + 0.22, 'εξάγει',
        ha='center', va='center', fontsize=7.5, color=BLUE_D, style='italic')

box(ax, x2, y_top, RW, RH,
    'Ευκαιρίες (O)',
    'Απειλές (T)',
    BLUE_L, BLUE_D, fontsize_t=10.5, fontsize_s=9.5)

# ── Step 2: Εσωτερικός Έλεγχος ───────────────────────────────────────────────
box(ax, x1, y_bot, BW, BH,
    'Εσωτερικός Έλεγχος',
    'Πόροι · Ικανότητες\nΑπόδοση · Κουλτούρα',
    GREEN_D, '#1B5E20', fontsize_t=10.5, fontsize_s=7.5)
step_circle(ax, x1 - BW/2 + 0.28, y_bot + BH/2 - 0.28, '2', GREEN_D, '#1B5E20')

arrow_h(ax, x1 + BW/2, x2 - RW/2, y_bot, GREEN_D)
ax.text((x1 + BW/2 + x2 - RW/2)/2, y_bot + 0.22, 'εξάγει',
        ha='center', va='center', fontsize=7.5, color=GREEN_D, style='italic')

box(ax, x2, y_bot, RW, RH,
    'Δυνάμεις (S)',
    'Αδυναμίες (W)',
    GREEN_L, GREEN_D, fontsize_t=10.5, fontsize_s=9.5)

# ── diagonal arrows → SWOT ────────────────────────────────────────────────────
arrow_diag(ax, x2 + RW/2, y_top - 0.1, x3 - SW/2, y_mid + 0.5, GREY_D, lw=2.0)
arrow_diag(ax, x2 + RW/2, y_bot + 0.1, x3 - SW/2, y_mid - 0.5, GREY_D, lw=2.0)

ax.text(x2 + RW/2 + 0.3, (y_top + y_bot)/2, 'συνθέτει',
        ha='left', va='center', fontsize=8, color=GREY_D, style='italic', rotation=-5)

# ── Step 3: SWOT ──────────────────────────────────────────────────────────────
swot_bg = FancyBboxPatch((x3 - SW/2, y_mid - SH/2), SW, SH,
                          boxstyle="round,pad=0.08",
                          facecolor=GREY_D, edgecolor='#263238',
                          linewidth=2.5, zorder=3)
ax.add_patch(swot_bg)

ax.text(x3, y_mid + 0.8, 'SWOT', ha='center', va='center',
        fontsize=14, color='white', fontweight='bold', zorder=4)

# 2×2 mini grid
for (lbl, gx, gy, gc) in [
    ('S  Δυνάμεις',   x3 - 0.52, y_mid + 0.25, '#43A047'),
    ('W  Αδυναμίες',  x3 + 0.52, y_mid + 0.25, '#EF5350'),
    ('O  Ευκαιρίες',  x3 - 0.52, y_mid - 0.38, '#1E88E5'),
    ('T  Απειλές',    x3 + 0.52, y_mid - 0.38, '#FB8C00'),
]:
    cell = FancyBboxPatch((gx - 0.48, gy - 0.24), 0.96, 0.48,
                          boxstyle="round,pad=0.03",
                          facecolor=gc, edgecolor='white',
                          linewidth=1.2, zorder=4)
    ax.add_patch(cell)
    ax.text(gx, gy, lbl, ha='center', va='center',
            fontsize=7.5, color='white', fontweight='bold', zorder=5)

step_circle(ax, x3 - SW/2 + 0.28, y_mid + SH/2 - 0.28, '3', GREY_L, '#263238')

# ── Step 4 arrow + TOWS ───────────────────────────────────────────────────────
arrow_h(ax, x3 + SW/2, x4 - TW/2, y_mid, GREY_D, lw=2.2)
ax.text((x3 + SW/2 + x4 - TW/2)/2, y_mid + 0.22, 'παράγει',
        ha='center', va='center', fontsize=7.5, color=GREY_D, style='italic')

box(ax, x4, y_mid, TW, TH,
    'Στρατηγικές\nΑποφάσεις',
    '(TOWS Matrix)',
    RED_D, '#8D2000', fontsize_t=10.5, fontsize_s=9)
step_circle(ax, x4 - TW/2 + 0.28, y_mid + TH/2 - 0.28, '4', RED_D, '#8D2000')

# ── title ─────────────────────────────────────────────────────────────────────
ax.text(6, 6.15, 'Από το Περιβάλλον στη Στρατηγική: Λογική Ακολουθία',
        ha='center', va='center', fontsize=11, color='#212121', fontweight='bold')

fig.savefig('/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/pestel_swot_flow.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print("Saved: pestel_swot_flow.png")
