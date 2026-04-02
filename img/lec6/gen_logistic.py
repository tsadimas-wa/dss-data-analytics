"""Generates logistic_illustration.png — sigmoid curve + decision boundary."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt

np.random.seed(42)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('white')

# ── Panel 1: Sigmoid function ─────────────────────────────────────────────────
z = np.linspace(-7, 7, 400)
sigmoid = 1 / (1 + np.exp(-z))

ax1.plot(z, sigmoid, color='#1565C0', lw=2.5)
ax1.axhline(0.5, color='#888', lw=1.2, linestyle='--', label='Κατώφλι = 0.5')
ax1.axvline(0.0, color='#888', lw=1.0, linestyle=':')

# Shade regions
ax1.fill_between(z, sigmoid, 0.5, where=(sigmoid > 0.5), alpha=0.12,
                 color='#C62828', label='Ακύρωση (P > 0.5)')
ax1.fill_between(z, sigmoid, 0.5, where=(sigmoid < 0.5), alpha=0.12,
                 color='#1565C0', label='Παραμονή (P < 0.5)')

# Annotations
ax1.annotate('P = 1\n(σίγουρα Ακύρωση)', xy=(6, 0.997), xytext=(3.5, 0.82),
             arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.2),
             fontsize=8.5, color='#C62828')
ax1.annotate('P = 0\n(σίγουρα Παραμονή)', xy=(-6, 0.003), xytext=(-6.5, 0.18),
             arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.2),
             fontsize=8.5, color='#1565C0')
ax1.annotate('P = 0.5\n(αβέβαιο)', xy=(0, 0.5), xytext=(1.2, 0.35),
             arrowprops=dict(arrowstyle='->', color='#555', lw=1.2),
             fontsize=8.5, color='#555')

ax1.set_xlabel('z  =  w₀ + w₁x₁ + … + wₙxₙ', fontsize=10)
ax1.set_ylabel('P(Ακύρωση)', fontsize=10)
ax1.set_title('Sigmoid Function — Έξοδος Πιθανότητας', fontsize=11, fontweight='bold')
ax1.legend(loc='center right', fontsize=9, framealpha=0.9)
ax1.set_ylim(-0.05, 1.05)
ax1.grid(alpha=0.25)

# ── Panel 2: 2D decision boundary ────────────────────────────────────────────
n = 40
X0 = np.random.randn(n, 2) + np.array([-1.8,  1.4])   # Παραμονή
X1 = np.random.randn(n, 2) + np.array([ 1.8, -1.4])   # Ακύρωση

ax2.scatter(X0[:, 0], X0[:, 1], color='#1565C0', s=50, label='Παραμονή', alpha=0.8, zorder=3)
ax2.scatter(X1[:, 0], X1[:, 1], color='#C62828', s=50, label='Ακύρωση',  alpha=0.8, zorder=3)

# Decision boundary: w·x = 0  →  x2 = -x1  (approx)
xx = np.linspace(-4.5, 4.5, 200)
yy = xx
ax2.plot(xx, yy, 'k-', lw=2.0, label='Όριο Απόφασης (P=0.5)', zorder=4)

# Gradient fill to suggest probability
from matplotlib.colors import LinearSegmentedColormap
cmap_lr = LinearSegmentedColormap.from_list('lr', ['#BBDEFB', '#FFCDD2'])
xx_grid = np.linspace(-4.5, 4.5, 200)
yy_grid = np.linspace(-4.5, 4.5, 200)
XX, YY = np.meshgrid(xx_grid, yy_grid)
Z = 1 / (1 + np.exp(-(XX - YY) * 0.9))
ax2.contourf(XX, YY, Z, levels=20, cmap=cmap_lr, alpha=0.30, zorder=1)

ax2.set_xlim(-4.8, 4.8)
ax2.set_ylim(-4.8, 4.8)
ax2.set_title('Γραμμικό Όριο Απόφασης', fontsize=11, fontweight='bold')
ax2.legend(loc='lower right', fontsize=9, framealpha=0.9)
ax2.set_xlabel('Χαρακτηριστικό 1', fontsize=9)
ax2.set_ylabel('Χαρακτηριστικό 2', fontsize=9)
ax2.grid(alpha=0.2)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss/dss-data-analytics/img/lec6/logistic_illustration.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
