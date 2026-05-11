"""Generates score_dist_roc_en.png — score distributions with TP/TN/FP/FN bars + ROC."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from sklearn.metrics import roc_curve, roc_auc_score
from scipy.stats import norm

np.random.seed(42)

# ── Synthetic predicted probabilities ────────────────────────────────────────
n0, n1 = 300, 200
scores0 = np.clip(norm.rvs(loc=0.30, scale=0.13, size=n0), 0.01, 0.99)  # Stay
scores1 = np.clip(norm.rvs(loc=0.65, scale=0.14, size=n1), 0.01, 0.99)  # Churn
scores = np.concatenate([scores0, scores1])
labels  = np.array([0]*n0 + [1]*n1)

fpr_all, tpr_all, thresh_all = roc_curve(labels, scores)
auc = roc_auc_score(labels, scores)

thresholds = [0.25, 0.40, 0.50, 0.65, 0.80]
colors_t   = ['#6A1B9A', '#1565C0', '#2E7D32', '#E65100', '#C62828']
bins = np.linspace(0, 1, 32)

# ── 4 colours for TP / TN / FP / FN ─────────────────────────────────────────
C_TN = '#1565C0'   # blue   — correct negative
C_FP = '#FF8F00'   # orange — false alarm
C_FN = '#E91E63'   # pink   — missed churner
C_TP = '#B71C1C'   # dark red — caught churner

def draw_panel(ax, t, tc):
    # Split scores into the 4 groups
    TN_scores = scores0[scores0 < t]
    FP_scores = scores0[scores0 >= t]
    FN_scores = scores1[scores1 < t]
    TP_scores = scores1[scores1 >= t]

    # Draw 4 histograms — stacked look via same bins, different colors
    ax.hist(TN_scores, bins=bins, color=C_TN, alpha=0.85, label=f'TN={len(TN_scores)}')
    ax.hist(FN_scores, bins=bins, color=C_FN, alpha=0.75, label=f'FN={len(FN_scores)}')
    ax.hist(TP_scores, bins=bins, color=C_TP, alpha=0.85, label=f'TP={len(TP_scores)}')
    ax.hist(FP_scores, bins=bins, color=C_FP, alpha=0.75, label=f'FP={len(FP_scores)}')

    # Threshold line
    ax.axvline(t, color=tc, lw=2.4, linestyle='--', zorder=6)

    # Region labels
    ymax = 58
    ax.set_ylim(0, ymax)
    ax.text(t/2,      ymax*0.92, '← Prediction: Stay',
            ha='center', fontsize=7.5, color='#333', style='italic')
    ax.text((t+1)/2,  ymax*0.92, 'Prediction: Churn →',
            ha='center', fontsize=7.5, color='#333', style='italic')

    # Compute metrics
    TP = len(TP_scores); TN = len(TN_scores)
    FP = len(FP_scores); FN = len(FN_scores)
    tpr = TP/(TP+FN) if (TP+FN) > 0 else 0
    fpr = FP/(FP+TN) if (FP+TN) > 0 else 0

    ax.set_title(f't = {t}  →  TPR={tpr:.2f},  FPR={fpr:.2f}',
                 fontsize=9.5, fontweight='bold', color=tc)
    ax.set_xlabel('P(Churn)', fontsize=8.5)
    ax.set_ylabel('Number of samples', fontsize=8)
    ax.set_xlim(0, 1)
    ax.legend(fontsize=7.5, loc='upper center', ncol=4, framealpha=0.9,
              handlelength=1.0, columnspacing=0.6)

# ── Layout: 2×3, last cell = ROC ─────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
fig.patch.set_facecolor('white')
fig.suptitle('From Score Distributions to the ROC Curve', fontsize=13,
             fontweight='bold')

panel_positions = [(0,0), (0,1), (0,2), (1,0), (1,1)]
for (r, c), t, tc in zip(panel_positions, thresholds, colors_t):
    draw_panel(axes[r, c], t, tc)

# Global legend for colors
legend_patches = [
    Patch(color=C_TN, label='TN — Stay, correctly predicted'),
    Patch(color=C_FN, label='FN — Churn, NOT detected (missed)'),
    Patch(color=C_TP, label='TP — Churn, correctly detected'),
    Patch(color=C_FP, label='FP — Stay, incorrectly flagged'),
]
fig.legend(handles=legend_patches, loc='lower center', ncol=4,
           fontsize=8.5, framealpha=0.95, bbox_to_anchor=(0.38, -0.02))

# ── ROC panel ─────────────────────────────────────────────────────────────────
ax_roc = axes[1, 2]
ax_roc.plot(fpr_all, tpr_all, color='#1A237E', lw=2.2, zorder=2,
            label=f'ROC (AUC={auc:.2f})')
ax_roc.plot([0,1],[0,1], color='#999', lw=1.2, linestyle=':', label='Random')
ax_roc.fill_between(fpr_all, tpr_all, alpha=0.07, color='#1A237E')

for t, tc in zip(thresholds, colors_t):
    idx = np.argmin(np.abs(thresh_all - t))
    fx, tx = fpr_all[idx], tpr_all[idx]
    ax_roc.plot(fx, tx, 'o', color=tc, ms=11, zorder=5, label=f't={t}')
    ax_roc.annotate(f't={t}', xy=(fx, tx), xytext=(fx+0.05, tx-0.06),
                    fontsize=8.5, color=tc, fontweight='bold')

ax_roc.plot(0, 1, 'k*', ms=13, zorder=6)
ax_roc.set_xlabel('FPR (False Alarms)', fontsize=9)
ax_roc.set_ylabel('TPR = Recall', fontsize=9)
ax_roc.set_title('ROC Curve\nEach point = one threshold', fontsize=10, fontweight='bold')
ax_roc.legend(fontsize=8, framealpha=0.95, loc='lower right', ncol=2)
ax_roc.set_xlim(-0.02, 1.02)
ax_roc.set_ylim(-0.02, 1.05)
ax_roc.grid(alpha=0.22)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/score_dist_roc_en.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
