"""Generates knn_illustration_en.png — two-panel k-NN figure (k=1 vs k=5 + decision boundary)."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

np.random.seed(3)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('white')

# ── Shared data ───────────────────────────────────────────────────────────────
n = 20
X0 = np.random.randn(n, 2) * 0.9 + np.array([-1.5,  1.5])  # Stay (blue)
X1 = np.random.randn(n, 2) * 0.9 + np.array([ 1.5, -1.5])  # Churn (red)
new_point = np.array([0.2, 0.3])  # query point

# ── Panel 1: k=1 vs k=5 voting ───────────────────────────────────────────────
for ax, k, title in [(ax1, 5, 'k-NN  (k=5) — Majority Voting')]:
    ax.scatter(X0[:, 0], X0[:, 1], color='#1565C0', s=60, label='Stay',
               alpha=0.8, zorder=3)
    ax.scatter(X1[:, 0], X1[:, 1], color='#C62828', s=60, label='Churn',
               alpha=0.8, zorder=3)

    # Query point
    ax.scatter(*new_point, color='#F9A825', s=200, marker='*',
               edgecolors='black', linewidths=1.2, zorder=6, label='New sample')

    # Find k nearest neighbors
    all_X = np.vstack([X0, X1])
    all_y = np.array([0] * n + [1] * n)
    dists = np.linalg.norm(all_X - new_point, axis=1)
    nn_idx = np.argsort(dists)[:k]

    # Draw circle enclosing k neighbors
    r = dists[nn_idx[-1]] * 1.05
    circle = Circle(new_point, r, fill=False, edgecolor='#F9A825',
                    lw=2.0, linestyle='--', zorder=4)
    ax.add_patch(circle)

    # Draw lines to neighbors
    votes = {0: 0, 1: 0}
    for idx in nn_idx:
        color = '#1565C0' if all_y[idx] == 0 else '#C62828'
        ax.plot([new_point[0], all_X[idx, 0]],
                [new_point[1], all_X[idx, 1]],
                color=color, lw=1.4, linestyle='-', alpha=0.7, zorder=4)
        votes[all_y[idx]] += 1

    # Vote annotation
    result = 'Stay' if votes[0] > votes[1] else 'Churn'
    res_color = '#1565C0' if votes[0] > votes[1] else '#C62828'
    ax.annotate(
        f'k={k}: {votes[0]}× Stay, {votes[1]}× Churn\n→ {result}',
        xy=new_point, xytext=(0.8, 2.2),
        arrowprops=dict(arrowstyle='->', color='#555', lw=1.2),
        fontsize=9, color=res_color,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFDE7', edgecolor='#F9A825', alpha=0.9)
    )

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9, framealpha=0.9)
    ax.set_xlabel('Feature 1', fontsize=9)
    ax.set_ylabel('Feature 2', fontsize=9)
    ax.grid(alpha=0.2)

# ── Panel 2: decision boundary for k=1 and k=9 ───────────────────────────────
from matplotlib.colors import ListedColormap

all_X = np.vstack([X0, X1])
all_y = np.array([0] * n + [1] * n)

xx = np.linspace(-4, 4, 300)
yy = np.linspace(-4, 4, 300)
XX, YY = np.meshgrid(xx, yy)
grid = np.c_[XX.ravel(), YY.ravel()]

for k_val, ax, title in [(1, ax1, 'k=1 — Overfitting'), (9, ax2, 'k=9 — Smoother Boundary')]:
    dists_grid = np.linalg.norm(grid[:, None, :] - all_X[None, :, :], axis=2)
    nn_grid = np.argsort(dists_grid, axis=1)[:, :k_val]
    preds = np.array([np.bincount(all_y[nn_grid[i]], minlength=2).argmax()
                      for i in range(len(grid))])
    Z = preds.reshape(XX.shape)

    cmap_bg = ListedColormap(['#BBDEFB', '#FFCDD2'])
    ax.contourf(XX, YY, Z, cmap=cmap_bg, alpha=0.30, zorder=1)
    ax.contour(XX, YY, Z, colors='black', linewidths=1.5, zorder=2)

    ax.scatter(X0[:, 0], X0[:, 1], color='#1565C0', s=50, label='Stay',
               alpha=0.85, zorder=3)
    ax.scatter(X1[:, 0], X1[:, 1], color='#C62828', s=50, label='Churn',
               alpha=0.85, zorder=3)
    ax.scatter(*new_point, color='#F9A825', s=180, marker='*',
               edgecolors='black', linewidths=1.2, zorder=6)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9, framealpha=0.9)
    ax.set_xlabel('Feature 1', fontsize=9)
    ax.set_ylabel('Feature 2', fontsize=9)
    ax.grid(alpha=0.2)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/knn_illustration_en.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
