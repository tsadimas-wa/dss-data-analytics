"""Generates svm_illustration.png — two-panel SVM figure (linear + kernel trick)."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

np.random.seed(7)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('white')

# ── Panel 1: Linear SVM with margin ──────────────────────────────────────────
# Two linearly separable classes
n = 30
X1 = np.random.randn(n, 2) + np.array([-1.8, 1.5])   # class 0 (blue)
X2 = np.random.randn(n, 2) + np.array([1.8, -1.5])   # class 1 (red)

ax1.scatter(X1[:, 0], X1[:, 1], color='#1565C0', s=50, label='Παραμονή', zorder=3, alpha=0.8)
ax1.scatter(X2[:, 0], X2[:, 1], color='#C62828', s=50, label='Ακύρωση', zorder=3, alpha=0.8)

# Decision boundary: w·x + b = 0  →  y = -x (approx)
xx = np.linspace(-4.5, 4.5, 200)
yy_boundary = -xx  # hyperplane
yy_upper = -xx + 1.4  # margin upper
yy_lower = -xx - 1.4  # margin lower

ax1.plot(xx, yy_boundary, 'k-', lw=2.0, label='Hyperplane', zorder=4)
ax1.plot(xx, yy_upper,   'k--', lw=1.4, alpha=0.6, zorder=4)
ax1.plot(xx, yy_lower,   'k--', lw=1.4, alpha=0.6, zorder=4)
ax1.fill_between(xx, yy_lower, yy_upper, color='gray', alpha=0.12, zorder=1)

# Mark support vectors (manually chosen close to margin)
sv_blue = np.array([[-1.2, 2.6], [-0.4, 1.6]])
sv_red  = np.array([[1.2, -2.6], [0.4, -1.6]])
ax1.scatter(sv_blue[:, 0], sv_blue[:, 1], color='#1565C0', s=120,
            edgecolors='black', linewidths=1.8, zorder=5)
ax1.scatter(sv_red[:, 0],  sv_red[:, 1],  color='#C62828', s=120,
            edgecolors='black', linewidths=1.8, zorder=5)

# Margin width arrow
ax1.annotate('', xy=(-3.5, 3.5 - 1.4), xytext=(-3.5, 3.5 + 1.4),
             arrowprops=dict(arrowstyle='<->', color='#333', lw=1.4))
ax1.text(-4.2, 3.5, 'Margin', fontsize=9, color='#333', va='center')

ax1.set_xlim(-4.8, 4.8)
ax1.set_ylim(-5, 5)
ax1.set_title('Γραμμικό SVM — Μεγιστοποίηση Margin', fontsize=11, fontweight='bold')
ax1.legend(loc='lower right', fontsize=9, framealpha=0.9)
ax1.set_xlabel('Χαρακτηριστικό 1', fontsize=9)
ax1.set_ylabel('Χαρακτηριστικό 2', fontsize=9)
ax1.grid(alpha=0.2)

# ── Panel 2: Kernel trick — non-linear data ───────────────────────────────────
theta = np.linspace(0, 2 * np.pi, n)
# Inner ring: class 0
r_inner = 1.0 + 0.25 * np.random.randn(n)
X_inner = np.column_stack([r_inner * np.cos(theta), r_inner * np.sin(theta)])
# Outer ring: class 1
r_outer = 2.5 + 0.25 * np.random.randn(n)
X_outer = np.column_stack([r_outer * np.cos(theta), r_outer * np.sin(theta)])

ax2.scatter(X_inner[:, 0], X_inner[:, 1], color='#1565C0', s=50, label='Παραμονή', zorder=3, alpha=0.8)
ax2.scatter(X_outer[:, 0], X_outer[:, 1], color='#C62828', s=50, label='Ακύρωση', zorder=3, alpha=0.8)

# Decision boundary: circle with RBF kernel (radius ≈ 1.75)
circle_theta = np.linspace(0, 2 * np.pi, 300)
r_boundary = 1.75
ax2.plot(r_boundary * np.cos(circle_theta), r_boundary * np.sin(circle_theta),
         'k-', lw=2.0, label='Hyperplane (RBF)', zorder=4)
ax2.fill_between(
    r_boundary * np.cos(circle_theta),
    r_boundary * np.sin(circle_theta) - 0.0,
    alpha=0.0
)
# Margin band
for dr, alpha in [(0.25, 0.12), (-0.25, 0.12)]:
    r = r_boundary + dr
    ax2.plot(r * np.cos(circle_theta), r * np.sin(circle_theta),
             'k--', lw=1.2, alpha=0.5, zorder=3)

ax2.text(0, 0, 'Kernel\nTrick', ha='center', va='center',
         fontsize=10, color='#555', fontstyle='italic')
ax2.set_xlim(-3.8, 3.8)
ax2.set_ylim(-3.8, 3.8)
ax2.set_aspect('equal')
ax2.set_title('Kernel Trick (RBF) — Μη-Γραμμικός Χωρισμός', fontsize=11, fontweight='bold')
ax2.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax2.set_xlabel('Χαρακτηριστικό 1', fontsize=9)
ax2.set_ylabel('Χαρακτηριστικό 2', fontsize=9)
ax2.grid(alpha=0.2)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/svm_illustration.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
