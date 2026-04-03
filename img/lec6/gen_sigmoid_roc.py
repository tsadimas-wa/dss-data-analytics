"""Generates sigmoid_roc.png — sigmoid with thresholds (left) + resulting ROC points (right)."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.datasets import make_classification

np.random.seed(42)

# ── Synthetic dataset ─────────────────────────────────────────────────────────
X, y = make_classification(n_samples=400, n_features=1, n_informative=1,
                            n_redundant=0, n_clusters_per_class=1,
                            flip_y=0.15, random_state=42)
clf = LogisticRegression().fit(X, y)
proba = clf.predict_proba(X)[:, 1]

# ── ROC curve ─────────────────────────────────────────────────────────────────
fpr_all, tpr_all, thresholds_all = roc_curve(y, proba)

# ── Thresholds to highlight ───────────────────────────────────────────────────
highlight = [0.2, 0.35, 0.5, 0.65, 0.8]
colors     = ['#6A1B9A', '#1565C0', '#2E7D32', '#E65100', '#C62828']
markers    = ['o', 's', 'D', '^', 'v']

# Find closest ROC point for each threshold
def roc_point(t):
    idx = np.argmin(np.abs(thresholds_all - t))
    return fpr_all[idx], tpr_all[idx]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
fig.patch.set_facecolor('white')

# ── Panel 1: Sigmoid with threshold lines ────────────────────────────────────
z = np.linspace(-6, 6, 400)
sig = 1 / (1 + np.exp(-z))

ax1.plot(z, sig, color='#333333', lw=2.5, label='Sigmoid $P(\\text{Ακύρωση})$')

for t, c, m in zip(highlight, colors, markers):
    z_t = np.log(t / (1 - t))          # inverse sigmoid
    ax1.axhline(t, color=c, lw=1.4, linestyle='--', alpha=0.85)
    ax1.axvline(z_t, color=c, lw=1.0, linestyle=':', alpha=0.6)
    ax1.plot(z_t, t, m, color=c, ms=9, zorder=5,
             label=f't = {t}')

ax1.set_xlabel('z  =  w₀ + w₁x₁ + … + wₙxₙ', fontsize=10)
ax1.set_ylabel('P(Ακύρωση)', fontsize=10)
ax1.set_title('Sigmoid — Διαφορετικά Κατώφλια', fontsize=11, fontweight='bold')
ax1.legend(fontsize=9, framealpha=0.95, loc='upper left')
ax1.set_ylim(-0.05, 1.08)
ax1.grid(alpha=0.22)

# Annotations
ax1.annotate('Χαμηλό t → περισσότεροι\nταξινομούνται ως Ακύρωση\n↑ Recall, ↓ Precision',
             xy=(-4, 0.2), xytext=(-5.8, 0.55),
             arrowprops=dict(arrowstyle='->', color='#6A1B9A', lw=1.1),
             fontsize=8, color='#6A1B9A')
ax1.annotate('Υψηλό t → λιγότεροι\nταξινομούνται ως Ακύρωση\n↑ Precision, ↓ Recall',
             xy=(3.5, 0.8), xytext=(1.2, 0.97),
             arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.1),
             fontsize=8, color='#C62828')

# ── Panel 2: ROC curve + highlighted points ───────────────────────────────────
ax2.plot(fpr_all, tpr_all, color='#1A237E', lw=2.2, label='Καμπύλη ROC', zorder=2)
ax2.plot([0, 1], [0, 1], color='#999', lw=1.3, linestyle=':', label='Τυχαίο μοντέλο')
ax2.fill_between(fpr_all, tpr_all, alpha=0.07, color='#1A237E')

for t, c, m in zip(highlight, colors, markers):
    fx, tx = roc_point(t)
    ax2.plot(fx, tx, m, color=c, ms=11, zorder=5,
             label=f't = {t}  (FPR={fx:.2f}, TPR={tx:.2f})')
    ax2.annotate(f't={t}', xy=(fx, tx),
                 xytext=(fx + 0.04, tx - 0.06),
                 fontsize=8, color=c)

ax2.plot(0, 1, 'k*', ms=13, zorder=6)
ax2.annotate('Ιδανικό\n(FPR=0, TPR=1)', xy=(0, 1), xytext=(0.08, 0.88),
             arrowprops=dict(arrowstyle='->', color='#333', lw=1.1),
             fontsize=8.5, color='#333')

ax2.set_xlabel('False Positive Rate (FPR)', fontsize=10)
ax2.set_ylabel('True Positive Rate (TPR = Recall)', fontsize=10)
ax2.set_title('Καμπύλη ROC — Κάθε Σημείο = Ένα Threshold', fontsize=11, fontweight='bold')
ax2.legend(fontsize=8.5, framealpha=0.95, loc='lower right')
ax2.set_xlim(-0.02, 1.02)
ax2.set_ylim(-0.02, 1.05)
ax2.grid(alpha=0.22)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/sigmoid_roc.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
