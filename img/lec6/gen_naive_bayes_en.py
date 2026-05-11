"""Generates naive_bayes_illustration_en.png — Gaussian NB distributions + spam example."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('white')

# ── Panel 1: Gaussian likelihood per class ────────────────────────────────────
x = np.linspace(-1, 9, 400)

# P(feature | class) — e.g. "Monthly Charges"
mu0, sig0 = 3.5, 1.0   # Stay
mu1, sig1 = 6.0, 1.1   # Churn

pdf0 = norm.pdf(x, mu0, sig0)
pdf1 = norm.pdf(x, mu1, sig1)

ax1.fill_between(x, pdf0, alpha=0.25, color='#1565C0')
ax1.fill_between(x, pdf1, alpha=0.25, color='#C62828')
ax1.plot(x, pdf0, color='#1565C0', lw=2.2, label='P(x | Stay)')
ax1.plot(x, pdf1, color='#C62828', lw=2.2, label='P(x | Churn)')

# New point to classify
xq = 5.2
pq0 = norm.pdf(xq, mu0, sig0)
pq1 = norm.pdf(xq, mu1, sig1)
ax1.axvline(xq, color='#F9A825', lw=2.0, linestyle='--', label=f'New sample x={xq}€')
ax1.plot(xq, pq0, 'o', color='#1565C0', ms=9, zorder=5)
ax1.plot(xq, pq1, 'o', color='#C62828', ms=9, zorder=5)

# Annotations
winner = 'Churn' if pq1 > pq0 else 'Stay'
w_color = '#C62828' if pq1 > pq0 else '#1565C0'
ax1.annotate(
    f'P(x|Stay)  = {pq0:.3f}\nP(x|Churn) = {pq1:.3f}\n→ {winner}',
    xy=(xq, max(pq0, pq1)), xytext=(6.5, 0.32),
    arrowprops=dict(arrowstyle='->', color='#555', lw=1.2),
    fontsize=8.5, color=w_color,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFDE7', edgecolor='#F9A825', alpha=0.9)
)

ax1.set_xlabel('Monthly Charges (€)', fontsize=10)
ax1.set_ylabel('Probability Density', fontsize=10)
ax1.set_title('Gaussian Naive Bayes — Likelihood per Class', fontsize=11, fontweight='bold')
ax1.legend(fontsize=9, framealpha=0.9)
ax1.grid(alpha=0.25)

# ── Panel 2: Spam filter — bar chart of word probabilities ───────────────────
words = ['free', 'you won', 'click here', 'dear', 'order', 'invoice']
p_spam = [0.82, 0.75, 0.68, 0.30, 0.20, 0.12]
p_ham  = [0.05, 0.04, 0.10, 0.55, 0.60, 0.70]

x_pos = np.arange(len(words))
width = 0.35

bars1 = ax2.bar(x_pos - width/2, p_spam, width, color='#C62828', alpha=0.8, label='Spam')
bars2 = ax2.bar(x_pos + width/2, p_ham,  width, color='#1565C0', alpha=0.8, label='Normal email')

ax2.set_xticks(x_pos)
ax2.set_xticklabels(words, rotation=20, ha='right', fontsize=9)
ax2.set_ylabel('P(word | class)', fontsize=10)
ax2.set_title('Example: Spam Filter\nWord Occurrence Probability per Class', fontsize=11, fontweight='bold')
ax2.legend(fontsize=9, framealpha=0.9)
ax2.set_ylim(0, 1.0)
ax2.grid(axis='y', alpha=0.25)

# Highlight "naive" assumption note
ax2.text(0.5, -0.22,
         '"Naive": we assume each word appears independently of the others',
         transform=ax2.transAxes, ha='center', fontsize=8.5,
         color='#555', style='italic')

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/naive_bayes_illustration_en.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
