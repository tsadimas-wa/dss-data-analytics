import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 4.5))

# Output linguistic terms and their representative values
terms = {
    'Inactive\n(0%)':   {'rep': 0,   'fire': 0.000, 'color': '#9E9E9E'},
    'Low\n(25%)':       {'rep': 25,  'fire': 0.000, 'color': '#9E9E9E'},
    'Medium\n(50%)':    {'rep': 50,  'fire': 0.000, 'color': '#9E9E9E'},
    'Strong\n(75%)':    {'rep': 75,  'fire': 0.150, 'color': '#FF9800'},
    'Full\n(100%)':     {'rep': 100, 'fire': 0.600, 'color': '#F44336'},
}

# Draw bars for each term
for label, t in terms.items():
    color = t['color']
    alpha = 1.0 if t['fire'] > 0 else 0.25
    ax.bar(t['rep'], t['fire'], width=14, color=color, alpha=alpha,
           edgecolor='white', linewidth=1.5, zorder=3)
    ax.text(t['rep'], t['fire'] + 0.025, f"{t['fire']:.3f}",
            ha='center', va='bottom', fontsize=11,
            color=color if t['fire'] > 0 else '#9E9E9E',
            fontweight='bold' if t['fire'] > 0 else 'normal')

# Representative value labels below bars
for label, t in terms.items():
    ax.text(t['rep'], -0.07, label, ha='center', va='top', fontsize=9,
            color='#333333')

# Centroid calculation
P_star = (0.150 * 75 + 0.600 * 100) / (0.150 + 0.600)  # = 95

# Mark centroid
ax.axvline(x=P_star, color='#1565C0', lw=2.5, ls='--', zorder=5)
ax.annotate(f'P* = {P_star:.1f}%\n(centroid)',
            xy=(P_star, 0.45), xytext=(P_star - 32, 0.55),
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=2),
            fontsize=12, color='#1565C0', fontweight='bold')

# Balance beam annotation
ax.annotate('', xy=(100, 0.08), xytext=(75, 0.08),
            arrowprops=dict(arrowstyle='<->', color='#555', lw=1.2))
ax.text(87.5, 0.10, '×0.60', ha='center', fontsize=9, color='#F44336')

ax.annotate('', xy=(75, 0.05), xytext=(P_star, 0.05),
            arrowprops=dict(arrowstyle='<->', color='#555', lw=1.2))
ax.text((75 + P_star) / 2, 0.065, '×0.15', ha='center', fontsize=9, color='#FF9800')

# Formula box
formula = r'$P^* = \frac{0.15 \times 75 + 0.60 \times 100}{0.15 + 0.60} = \frac{71.25}{0.75} = 95\%$'
ax.text(38, 0.70, formula, fontsize=12,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#E3F2FD', edgecolor='#1565C0', lw=1.5))

ax.set_xlim(-15, 120)
ax.set_ylim(-0.15, 0.90)
ax.set_xlabel('AC Power P (%)', fontsize=12)
ax.set_ylabel('fire strength (weight)', fontsize=12)
ax.set_title('Defuzzification — Centroid (weighted average)', fontsize=13, fontweight='bold')
ax.set_xticks([0, 25, 50, 75, 95, 100])
ax.set_xticklabels(['0', '25', '50', '75', '95\n(P*)', '100'])
ax.set_yticks([0, 0.15, 0.30, 0.45, 0.60, 0.75])
ax.tick_params(labelsize=10)
ax.grid(True, axis='y', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

active = mpatches.Patch(color='#FF9800', label='Active rule (fire > 0)')
inactive = mpatches.Patch(color='#9E9E9E', alpha=0.4, label='Inactive rule (fire = 0)')
ax.legend(handles=[active, inactive], fontsize=10, loc='upper left')

fig.tight_layout()
out = 'lectures_material/defuzzification_en.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f'Saved: {out}')
