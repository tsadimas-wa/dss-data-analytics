import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Output membership functions (Mamdani style, evenly spaced over [0,100])
# Δυνατό: tri(50, 75, 100)
# Πλήρες: trap(75, 100, 100, 100)

x = np.linspace(0, 100, 1000)

def tri_mf(x, a, b, c):
    y = np.zeros_like(x, dtype=float)
    rising = (x >= a) & (x <= b)
    falling = (x > b) & (x <= c)
    y[rising] = (x[rising] - a) / (b - a)
    y[falling] = (c - x[falling]) / (c - b)
    return y

def trap_mf(x, a, b, c, d):
    y = np.zeros_like(x, dtype=float)
    r = (x >= a) & (x < b)
    p = (x >= b) & (x <= c)
    f = (x > c) & (x <= d)
    if b > a: y[r] = (x[r] - a) / (b - a)
    y[p] = 1.0
    if d > c: y[f] = (d - x[f]) / (d - c)
    return y

# Unclipped output MFs
mu_dynamic_full = tri_mf(x, 50, 75, 100)
mu_full_full    = trap_mf(x, 75, 100, 100, 100)

# Fire strengths from our example
fire_dynamic = 0.15  # R6
fire_full    = 0.60  # R7

# Clipped MFs (Mamdani: clip at fire strength)
mu_dynamic_clipped = np.minimum(mu_dynamic_full, fire_dynamic)
mu_full_clipped    = np.minimum(mu_full_full, fire_full)

# Aggregated (union = max)
mu_agg = np.maximum(mu_dynamic_clipped, mu_full_clipped)

# Centroid of aggregated area
centroid_mamdani = np.trapezoid(x * mu_agg, x) / np.trapezoid(mu_agg, x)

# Singleton centroid for reference
centroid_singleton = (fire_dynamic * 75 + fire_full * 100) / (fire_dynamic + fire_full)

print(f"Mamdani centroid: {centroid_mamdani:.2f}%")
print(f"Singleton centroid: {centroid_singleton:.2f}%")

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# ---- Left: Mamdani ----
ax = axes[0]

# Fill aggregated area
ax.fill_between(x, mu_agg, alpha=0.20, color='#7B1FA2', label='Αθροισμένη περιοχή')

# Unclipped MFs (dashed)
ax.plot(x, mu_dynamic_full, '--', color='#FF9800', lw=1.5, alpha=0.5, label='Δυνατό MF (πλήρης)')
ax.plot(x, mu_full_full,    '--', color='#F44336', lw=1.5, alpha=0.5, label='Πλήρες MF (πλήρης)')

# Clipped MFs
ax.plot(x, mu_dynamic_clipped, color='#FF9800', lw=2.5, label=f'Δυνατό clipped @ {fire_dynamic}')
ax.plot(x, mu_full_clipped,    color='#F44336', lw=2.5, label=f'Πλήρες clipped @ {fire_full}')

# Centroid
ax.axvline(x=centroid_mamdani, color='#1565C0', lw=2.5, ls='-.',
           label=f'Centroid = {centroid_mamdani:.1f}%')
ax.annotate(f'P* = {centroid_mamdani:.1f}%',
            xy=(centroid_mamdani, 0.35), xytext=(centroid_mamdani - 28, 0.45),
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.8),
            fontsize=12, color='#1565C0', fontweight='bold')

ax.set_title('Mamdani\n(centroid αθροισμένης περιοχής)', fontsize=12, fontweight='bold')
ax.set_xlabel('Ισχύς P (%)', fontsize=11)
ax.set_ylabel('μ', fontsize=12)
ax.set_xlim(0, 105)
ax.set_ylim(-0.05, 0.85)
ax.set_xticks([0, 25, 50, 75, centroid_mamdani, 100])
ax.set_xticklabels(['0', '25', '50', '75', f'{centroid_mamdani:.1f}*', '100'])
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3)

# ---- Right: Singleton (Sugeno) ----
ax = axes[1]

terms = {'Ανενεργό': 0, 'Χαμηλό': 25, 'Μέτριο': 50, 'Δυνατό': 75, 'Πλήρες': 100}
fires = {'Ανενεργό': 0, 'Χαμηλό': 0, 'Μέτριο': 0, 'Δυνατό': fire_dynamic, 'Πλήρες': fire_full}
colors = {'Ανενεργό': '#9E9E9E', 'Χαμηλό': '#9E9E9E', 'Μέτριο': '#9E9E9E',
          'Δυνατό': '#FF9800', 'Πλήρες': '#F44336'}

for name, val in terms.items():
    fire = fires[name]
    color = colors[name]
    alpha = 1.0 if fire > 0 else 0.3
    ax.vlines(val, 0, fire, color=color, lw=6, alpha=alpha)
    ax.plot(val, fire, 'o', color=color, ms=10, alpha=alpha, zorder=5)
    if fire > 0:
        ax.text(val, fire + 0.02, f'{fire}', ha='center', fontsize=10,
                color=color, fontweight='bold')

ax.axvline(x=centroid_singleton, color='#1565C0', lw=2.5, ls='-.',
           label=f'Centroid = {centroid_singleton:.1f}%')
ax.annotate(f'P* = {centroid_singleton:.1f}%',
            xy=(centroid_singleton, 0.35), xytext=(centroid_singleton - 30, 0.45),
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.8),
            fontsize=12, color='#1565C0', fontweight='bold')

ax.set_title('Sugeno / Singleton\n(σταθμισμένος μέσος σημείων)', fontsize=12, fontweight='bold')
ax.set_xlabel('Ισχύς P (%)', fontsize=11)
ax.set_ylabel('fire strength (βάρος)', fontsize=12)
ax.set_xlim(-10, 115)
ax.set_ylim(-0.05, 0.85)
ax.set_xticks([0, 25, 50, 75, centroid_singleton, 100])
ax.set_xticklabels(['0', '25', '50', '75', f'{centroid_singleton:.0f}*', '100'])
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3)

fig.suptitle('Defuzzification: Mamdani vs Sugeno/Singleton', fontsize=13, fontweight='bold', y=1.01)
fig.tight_layout()
out = 'lectures_material/mamdani_vs_singleton.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'Saved: {out}')
