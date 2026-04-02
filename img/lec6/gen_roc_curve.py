"""Generates roc_curve.png — ROC curve illustration with multiple models."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

np.random.seed(42)

def make_roc(auc_target, n=300):
    """Synthetic ROC curve that integrates to approximately auc_target."""
    t = np.linspace(0, 1, n)
    # parametric curve: FPR = t, TPR shaped by power
    power = np.log(0.5) / np.log(1 - auc_target + 1e-9) if auc_target != 1 else 0.01
    fpr = t
    tpr = t ** max(power, 0.05)
    tpr = np.clip(tpr, 0, 1)
    return fpr, tpr

fig, ax = plt.subplots(figsize=(6.5, 5.2))
fig.patch.set_facecolor('white')

# Random classifier diagonal
ax.plot([0, 1], [0, 1], color='#999999', lw=1.4, linestyle=':', label='Τυχαίο μοντέλο (AUC = 0.50)')

# Decision Tree only
fpr_dt, tpr_dt = make_roc(0.82)
ax.plot(fpr_dt, tpr_dt, color='#E65100', lw=2.2, linestyle='-', label='Decision Tree  (AUC = 0.82)')
ax.fill_between(fpr_dt, tpr_dt, alpha=0.10, color='#E65100')

# Ideal point annotation
ax.plot(0, 1, 'k*', markersize=14, zorder=5)
ax.annotate('Ιδανικό μοντέλο\n(FPR=0, TPR=1)',
            xy=(0, 1), xytext=(0.12, 0.85),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.3),
            fontsize=9, color='#333')

ax.set_xlabel('False Positive Rate (FPR)\n← Λιγότεροι λάθος συναγερμοί', fontsize=10)
ax.set_ylabel('True Positive Rate (TPR = Recall)\n← Περισσότερες σωστές ανιχνεύσεις', fontsize=10)
ax.set_title('Καμπύλη ROC — Decision Tree', fontsize=12, fontweight='bold')
ax.legend(loc='lower right', fontsize=9.5, framealpha=0.9)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.05)
ax.grid(alpha=0.25)

# Threshold direction arrows
ax.annotate('', xy=(0.05, 0.72), xytext=(0.22, 0.55),
            arrowprops=dict(arrowstyle='->', color='#555', lw=1.2))
ax.text(0.23, 0.50, 'threshold ↑\n(αυστηρότερο)', fontsize=8, color='#555')
ax.annotate('', xy=(0.28, 0.60), xytext=(0.12, 0.77),
            arrowprops=dict(arrowstyle='->', color='#555', lw=1.2))
ax.text(0.04, 0.79, 'threshold ↓\n(χαλαρότερο)', fontsize=8, color='#555')

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss/dss-data-analytics/img/lec6/roc_curve.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
