"""Generates entr-gini_en.png — Entropy, Gini, and Misclassification Error comparison."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt

p = np.linspace(0.001, 0.999, 500)

entropy = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
gini    = 2 * p * (1 - p)          # scaled: 1 - p^2 - (1-p)^2 = 2p(1-p)
misclass = 1 - np.maximum(p, 1 - p)  # E(t) = 1 - max(p, 1-p)

fig, ax = plt.subplots(figsize=(7, 4.5))
fig.patch.set_facecolor('white')

ax.plot(p, entropy,  color='#1565C0', lw=2.4, linestyle='-',  label='Entropy  $H(t) = -\\sum p_c \\log_2 p_c$  [0, 1]')
ax.plot(p, gini,     color='#C62828', lw=2.4, linestyle='--', label='Gini  $G(t) = 1 - \\sum p_c^2$  [0, 0.5]')
ax.plot(p, misclass, color='#2E7D32', lw=2.4, linestyle=':',  label='Misclassification Error  $E(t) = 1 - \\max p_c$  [0, 0.5]')

# Mark the maximum impurity point (p=0.5)
ax.axvline(0.5, color='#999', lw=1.0, linestyle='--', alpha=0.6)
ax.plot(0.5, 1.0,  'o', color='#1565C0', ms=7, zorder=5)
ax.plot(0.5, 0.5,  'o', color='#C62828', ms=7, zorder=5)
ax.plot(0.5, 0.5,  'o', color='#2E7D32', ms=7, zorder=5)

ax.text(0.52, 0.02, 'Pure\nnode\n(p=0 or 1)', fontsize=8, color='#555')
ax.text(0.36, 0.74, 'Maximum\nimpurity\n(p=0.5)', fontsize=8, color='#555', ha='center')

ax.set_xlabel('Probability of class 1  ($p$)', fontsize=10)
ax.set_ylabel('Impurity Measure', fontsize=10)
ax.set_title('Comparison of Impurity Measures', fontsize=12, fontweight='bold')
ax.legend(fontsize=9, framealpha=0.95, loc='upper center',
          bbox_to_anchor=(0.5, -0.18), ncol=1)
ax.set_xlim(0, 1)
ax.set_ylim(-0.02, 1.08)
ax.grid(alpha=0.25)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/entr-gini_en.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
