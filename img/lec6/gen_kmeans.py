"""Generates kmeans_illustration.png — 4-step convergence + elbow method."""
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
import matplotlib.pyplot as plt

np.random.seed(11)

# ── Generate clustered data ───────────────────────────────────────────────────
centers_true = [(-3, 2), (2, 3), (1, -2.5)]
colors_cls = ['#1565C0', '#2E7D32', '#C62828']
labels_cls = ['Περιστασιακοί', 'Τακτικοί', 'VIP']
n_per = 25

X_all, y_all = [], []
for i, (cx, cy) in enumerate(centers_true):
    pts = np.random.randn(n_per, 2) * 0.8 + np.array([cx, cy])
    X_all.append(pts)
    y_all.extend([i] * n_per)
X = np.vstack(X_all)
y = np.array(y_all)

# ── K-Means iterations ────────────────────────────────────────────────────────
K = 3
# Fixed initial centroids (not too close to true centers to show movement)
centroids = np.array([[-2.5, 3.5], [2.5, 2.5], [0.5, -1.5]], dtype=float)

def assign(X, C):
    dists = np.linalg.norm(X[:, None] - C[None], axis=2)
    return np.argmin(dists, axis=1)

def update(X, labels, K):
    return np.array([X[labels == k].mean(axis=0) for k in range(K)])

steps = []  # (centroids, labels, title)
steps.append((centroids.copy(), None, 'Βήμα 1: Αρχικά Τυχαία Κέντρα'))
for i in range(1, 4):
    labels_iter = assign(X, centroids)
    steps.append((centroids.copy(), labels_iter.copy(),
                  f'Βήμα {i+1}: Ανάθεση & Νέα Κέντρα'))
    centroids = update(X, labels_iter, K)

# Final step
labels_final = assign(X, centroids)
steps.append((centroids.copy(), labels_final.copy(), 'Σύγκλιση'))

fig = plt.figure(figsize=(14, 8))
fig.patch.set_facecolor('white')

# ── Top row: 4 convergence panels ────────────────────────────────────────────
show_steps = [steps[0], steps[1], steps[3], steps[4]]
centroid_colors = ['#E65100', '#6A1B9A', '#00695C']

for col, (cents, lbls, title) in enumerate(show_steps):
    ax = fig.add_subplot(2, 4, col + 1)
    if lbls is None:
        ax.scatter(X[:, 0], X[:, 1], color='#AAAAAA', s=30, alpha=0.6, zorder=2)
    else:
        for k in range(K):
            mask = lbls == k
            ax.scatter(X[mask, 0], X[mask, 1], color=colors_cls[k], s=30, alpha=0.7, zorder=2)
    # Centroids
    for k in range(K):
        ax.scatter(cents[k, 0], cents[k, 1], color=centroid_colors[k],
                   s=180, marker='X', edgecolors='black', linewidths=1.2, zorder=5)
    ax.set_title(title, fontsize=9, fontweight='bold')
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.grid(alpha=0.2)
    ax.set_xticks([])
    ax.set_yticks([])

# Add centroid legend to last convergence panel
from matplotlib.lines import Line2D
legend_els = [Line2D([0], [0], marker='X', color='w', markerfacecolor=centroid_colors[k],
                     markeredgecolor='black', markersize=10, label=f'Centroid {k+1}')
              for k in range(K)]
fig.axes[3].legend(handles=legend_els, fontsize=7.5, loc='lower right', framealpha=0.9)

# ── Bottom row: Final clustering (large) + Elbow method ──────────────────────
ax_final = fig.add_subplot(2, 4, (5, 6))
for k in range(K):
    mask = labels_final == k
    ax_final.scatter(X[mask, 0], X[mask, 1], color=colors_cls[k], s=55,
                     alpha=0.85, label=labels_cls[k], zorder=3)
    ax_final.scatter(centroids[k, 0], centroids[k, 1],
                     color=centroid_colors[k], s=250, marker='X',
                     edgecolors='black', linewidths=1.5, zorder=5)
ax_final.set_title('Τελική Ομαδοποίηση (K=3) — Customer Segmentation',
                   fontsize=10, fontweight='bold')
ax_final.legend(fontsize=9, framealpha=0.9)
ax_final.grid(alpha=0.2)
ax_final.set_xlabel('Χαρακτηριστικό 1', fontsize=9)
ax_final.set_ylabel('Χαρακτηριστικό 2', fontsize=9)

# ── Elbow method ─────────────────────────────────────────────────────────────
ax_elbow = fig.add_subplot(2, 4, (7, 8))
ks = range(1, 9)
inertias = []
for k_val in ks:
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=k_val, n_init=10, random_state=0).fit(X)
    inertias.append(km.inertia_)

ax_elbow.plot(list(ks), inertias, 'ko-', lw=2.0, ms=6)
ax_elbow.axvline(3, color='#C62828', lw=1.8, linestyle='--', label='K=3 (αγκώνας)')
ax_elbow.scatter([3], [inertias[2]], color='#C62828', s=120, zorder=5)
ax_elbow.annotate('Αγκώνας\n(K=3)', xy=(3, inertias[2]), xytext=(4.2, inertias[2] + 15),
                  arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.2),
                  fontsize=9, color='#C62828')
ax_elbow.set_xlabel('Αριθμός Ομάδων K', fontsize=10)
ax_elbow.set_ylabel('Αδράνεια (WCSS)', fontsize=10)
ax_elbow.set_title('Μέθοδος Αγκώνα — Επιλογή K', fontsize=10, fontweight='bold')
ax_elbow.legend(fontsize=9, framealpha=0.9)
ax_elbow.grid(alpha=0.25)

plt.tight_layout()
out = '/home/rg/Teaching/uniwa/dss-data-analytics/img/lec6/kmeans_illustration.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Saved → {out}')
