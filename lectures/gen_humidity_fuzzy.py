import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

H = np.linspace(0, 100, 500)

def trap(x, a, b, c, d):
    y = np.zeros_like(x, dtype=float)
    for i, xi in enumerate(x):
        if xi <= a or xi >= d:
            y[i] = 0.0
        elif xi < b:
            y[i] = (xi - a) / (b - a) if b != a else 1.0
        elif xi <= c:
            y[i] = 1.0
        else:
            y[i] = (d - xi) / (d - c) if d != c else 1.0
    return y

def tri(x, a, b, c):
    return trap(x, a, b, b, c)

mu_low    = trap(H, 0,  0,  30, 50)
mu_medium = tri( H, 35, 55, 75)
mu_high   = trap(H, 60, 80, 100, 100)

h_val = 72
mu_low_72    = 0.0
mu_medium_72 = (75 - h_val) / (75 - 55)   # 0.15
mu_high_72   = (h_val - 60) / (80 - 60)   # 0.60

fig, ax = plt.subplots(figsize=(9, 4.5))

ax.plot(H, mu_low,    color='#2196F3', lw=2.5, label='Χαμηλή  — trap(0,0,30,50)')
ax.plot(H, mu_medium, color='#FF9800', lw=2.5, label='Μέτρια  — tri(35,55,75)')
ax.plot(H, mu_high,   color='#4CAF50', lw=2.5, label='Υψηλή   — trap(60,80,100,100)')

ax.axvline(x=h_val, color='#E91E63', lw=1.8, ls='--', label=f'H = {h_val}%')

ax.plot(h_val, mu_medium_72, 'o', color='#FF9800', ms=10, zorder=5)
ax.plot(h_val, mu_high_72,   'o', color='#4CAF50', ms=10, zorder=5)
ax.plot(h_val, mu_low_72,    'o', color='#2196F3', ms=10, zorder=5)

ax.annotate(f'μ_Μέτρια = {mu_medium_72:.2f}',
            xy=(h_val, mu_medium_72), xytext=(h_val - 22, mu_medium_72 + 0.12),
            arrowprops=dict(arrowstyle='->', color='#FF9800', lw=1.5),
            fontsize=11, color='#FF9800', fontweight='bold')

ax.annotate(f'μ_Υψηλή = {mu_high_72:.2f}',
            xy=(h_val, mu_high_72), xytext=(h_val + 4, mu_high_72 + 0.12),
            arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=1.5),
            fontsize=11, color='#4CAF50', fontweight='bold')

ax.annotate('μ_Χαμηλή = 0.00\n(εκτός εύρους)',
            xy=(h_val, 0.0), xytext=(h_val + 4, 0.10),
            arrowprops=dict(arrowstyle='->', color='#2196F3', lw=1.5),
            fontsize=10, color='#2196F3')

ax.set_xlabel('Υγρασία H (%)', fontsize=13)
ax.set_ylabel('Βαθμός συμμετοχής μ', fontsize=13)
ax.set_title('Fuzzification — Υγρασία H = 72%', fontsize=14, fontweight='bold')
ax.set_xlim(0, 100)
ax.set_ylim(-0.05, 1.15)
ax.set_xticks([0, 30, 35, 50, 55, 60, 72, 75, 80, 100])
ax.set_yticks([0, 0.15, 0.3, 0.6, 0.75, 1.0])
ax.tick_params(labelsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right', fontsize=10)

fig.tight_layout()
out = 'lectures/humidity_fuzzification.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'Saved: {out}')
