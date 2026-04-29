#!/usr/bin/env python3
"""Generate additional org chart PNGs: Divisional, Matrix, Flat, Network."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

BG     = 'white'
LINE   = '#999999'
TITLE  = '#1a1a1a'
SOURCE = '#888888'
ANNOT  = '#444444'

def draw_box(ax, x, y, w, h, label, color='#1a3e6e', text_color='white',
             fontsize=9, sublabel=None):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.02",
                         facecolor=color, edgecolor='white', linewidth=1.5,
                         zorder=2)
    ax.add_patch(box)
    if sublabel:
        ax.text(x, y + 0.07, label, ha='center', va='center',
                fontsize=fontsize, color=text_color, fontweight='bold', zorder=3)
        ax.text(x, y - 0.14, sublabel, ha='center', va='center',
                fontsize=fontsize - 1.5, color=text_color, style='italic', zorder=3)
    else:
        ax.text(x, y, label, ha='center', va='center',
                fontsize=fontsize, color=text_color, fontweight='bold',
                multialignment='center', zorder=3)

def draw_line(ax, x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color=LINE, linewidth=1.2, zorder=1)

def save(fig, path):
    fig.savefig(path, dpi=150, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  Saved: {path}")


# ── 1. Divisional — Samsung ───────────────────────────────────────────────────

def make_divisional():
    fig, ax = plt.subplots(figsize=(14, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 14); ax.set_ylim(3.0, 7.5)
    ax.axis('off')
    ax.set_title("Τμηματική Δομή (Divisional) — Samsung Electronics",
                 color=TITLE, fontsize=13, fontweight='bold', pad=12)

    # CEO
    draw_box(ax, 7, 7.0, 3.4, 0.7,
             "Jong-Hee Han — Vice Chairman & CEO",
             color='#1a3e6e', fontsize=9)

    # 3 Divisions
    divs = [
        (2.4,  "MX Division\n(Mobile eXperience)",    '#1565C0'),
        (7.0,  "DS Division\n(Device Solutions)",     '#B71C1C'),
        (11.6, "VD/DA Division\n(Consumer Electronics)",'#2E7D32'),
    ]
    for x, label, col in divs:
        draw_box(ax, x, 5.5, 3.2, 0.78, label, color=col, fontsize=9)
        draw_line(ax, 7, 6.65, x, 5.89)

    # MX sub-units
    mx = [
        (1.0, "Smartphones\n& Tablets"),
        (2.4, "Wearables\n(Galaxy Watch)"),
        (3.8, "MX\nMarketing"),
    ]
    for x, label in mx:
        draw_box(ax, x, 4.0, 1.2, 0.7, label, color='#1976D2', fontsize=7.5)
        draw_line(ax, 2.4, 5.11, x, 4.35)

    # DS sub-units
    ds = [
        (5.6, "Memory\n(DRAM, NAND)"),
        (7.0, "System LSI\n(Chips, Sensors)"),
        (8.4, "Foundry\n(Contract Mfg)"),
    ]
    for x, label in ds:
        draw_box(ax, x, 4.0, 1.2, 0.7, label, color='#C62828', fontsize=7.5)
        draw_line(ax, 7.0, 5.11, x, 4.35)

    # VD/DA sub-units
    vd = [
        (10.4, "Visual Display\n(TV, Monitors)"),
        (11.8, "Digital Appliances\n(Washing, Fridge)"),
        (13.2, "VD/DA\nMarketing"),
    ]
    for x, label in vd:
        draw_box(ax, x, 4.0, 1.2, 0.7, label, color='#388E3C', fontsize=7.5)
        draw_line(ax, 11.6, 5.11, x, 4.35)

    ax.text(0.01, 0.01,
            "Πηγή: Samsung Electronics Annual Report 2023 · Chandler (1962), Strategy and Structure",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/divisional_org.png')


# ── 2. Matrix — Generic (McKinsey style) ──────────────────────────────────────

def make_matrix():
    fig, ax = plt.subplots(figsize=(13, 8))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title("Μητρωική Δομή (Matrix) — Γενικό Παράδειγμα (McKinsey & Co. style)",
                 color=TITLE, fontsize=13, fontweight='bold', pad=12)

    # Functional managers (top row — columns)
    func_heads = [
        (3.5, "Engineering\nManager"),
        (5.8, "Design\nManager"),
        (8.1, "Finance\nManager"),
        (10.4, "Marketing\nManager"),
    ]
    for x, label in func_heads:
        draw_box(ax, x, 7.0, 2.0, 0.72, label, color='#1565C0', fontsize=9)
        # vertical line down
        ax.plot([x, x], [6.64, 1.0], color='#90CAF9', linewidth=1.5,
                linestyle='--', zorder=1)

    # Project managers (left column — rows)
    proj_y = [5.5, 4.1, 2.7]
    proj_labels = ["Project A\n(Manager)", "Project B\n(Manager)", "Project C\n(Manager)"]
    proj_colors = ['#4CAF50', '#FF9800', '#9C27B0']
    for y, label, col in zip(proj_y, proj_labels, proj_colors):
        draw_box(ax, 1.2, y, 1.9, 0.72, label, color=col, fontsize=9)
        # horizontal line right
        ax.plot([2.15, 11.5], [y, y], color='#CCCCCC', linewidth=1.5,
                linestyle='--', zorder=1)

    # Employee nodes at intersections
    emp_color = '#546E7A'
    for y, pcol in zip(proj_y, proj_colors):
        for x, _ in func_heads:
            box = FancyBboxPatch((x - 0.6, y - 0.28), 1.2, 0.56,
                                 boxstyle="round,pad=0.02",
                                 facecolor=emp_color, edgecolor=pcol,
                                 linewidth=2, zorder=3)
            ax.add_patch(box)
            ax.text(x, y, "Εργαζόμενος", ha='center', va='center',
                    fontsize=6.5, color='white', fontweight='bold', zorder=4)

    # Dual reporting arrow annotation
    ax.annotate("", xy=(2.15, 5.5), xytext=(1.75, 6.65),
                arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=2))
    ax.annotate("", xy=(3.5, 6.64), xytext=(2.75, 6.65),
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=2))
    ax.text(0.1, 6.4,
            "⚠ Διπλή αναφορά:\nProject Manager\n+\nFunctional Manager",
            ha='left', fontsize=7.5, color='#C62828',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE',
                      edgecolor='#EF9A9A', linewidth=1))

    # Legend
    legend_items = [
        mpatches.Patch(color='#1565C0', label='Λειτουργικοί Managers (κάθετη εξουσία)'),
        mpatches.Patch(color='#4CAF50', label='Project Managers (οριζόντια εξουσία)'),
        mpatches.Patch(color='#546E7A', label='Εργαζόμενοι (διπλή αναφορά)'),
    ]
    ax.legend(handles=legend_items, loc='lower right', fontsize=8,
              facecolor='#f5f5f5', edgecolor='#cccccc', framealpha=1.0)

    ax.text(0.01, 0.01,
            "Πηγή: Davis & Lawrence (1977), Matrix · Mintzberg (1979), The Structuring of Organizations",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/matrix_org.png')


# ── 3. Flat — Valve Corporation ───────────────────────────────────────────────

def make_flat():
    fig, ax = plt.subplots(figsize=(16, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16); ax.set_ylim(4.8, 8)
    ax.axis('off')
    ax.set_title("Επίπεδη Δομή (Flat) — Valve Corporation",
                 color=TITLE, fontsize=13, fontweight='bold', pad=12)

    # Founder (top center)
    draw_box(ax, 8.0, 7.4, 4.0, 0.72,
             "Gabe Newell — Founder & President",
             color='#37474F', fontsize=9.5)

    # 8 self-managed teams — evenly spaced with step=2.0, box_w=1.7
    nodes = [
        (1.0,  "Steam\nPlatform",         '#1565C0'),
        (3.0,  "Half-Life /\nCS:GO",      '#1565C0'),
        (5.0,  "Dota 2 /\nArtifact",      '#1565C0'),
        (7.0,  "VR &\nValve Index",        '#6A1B9A'),
        (9.0,  "Steam\nHardware",          '#6A1B9A'),
        (11.0, "Anti-Cheat\n& Security",   '#2E7D32'),
        (13.0, "Business Dev\n& Licensing",'#E65100'),
        (15.0, "HR &\nRecruitment",        '#455A64'),
    ]
    for x, label, col in nodes:
        draw_box(ax, x, 5.6, 1.7, 0.82, label, color=col, fontsize=8)
        draw_line(ax, 8.0, 7.04, x, 6.01)

    ax.text(0.01, 0.01,
            "Πηγή: Valve Employee Handbook (2012) · Peters & Waterman (1982) In Search of Excellence",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/flat_org.png')


# ── 4. Network — Nike ─────────────────────────────────────────────────────────

def make_network():
    fig, ax = plt.subplots(figsize=(13, 7.5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title("Δικτυωτή Δομή (Network) — Nike, Inc.",
                 color=TITLE, fontsize=13, fontweight='bold', pad=12)

    # Central core
    core = FancyBboxPatch((4.5, 3.2), 4.0, 2.4,
                          boxstyle="round,pad=0.1",
                          facecolor='#1a3e6e', edgecolor='white', linewidth=2,
                          zorder=3)
    ax.add_patch(core)
    ax.text(6.5, 5.0, "NIKE Core", ha='center', fontsize=11,
            color='white', fontweight='bold', zorder=4)
    ax.text(6.5, 4.6, "(Beaverton, Oregon HQ)", ha='center', fontsize=8,
            color='#BBDEFB', style='italic', zorder=4)
    core_items = ["• Brand & Marketing", "• Product Design", "• Strategy & Finance"]
    for i, item in enumerate(core_items):
        ax.text(6.5, 4.2 - i * 0.32, item, ha='center', fontsize=8,
                color='#E3F2FD', zorder=4)

    # Partner nodes
    partners = [
        # (x, y, label, sublabel, color, arrow_start_xy, arrow_end_xy)
        (1.2, 6.2, "Εργοστάσια\nSunrise (Κίνα)\nYue Yuen (Βιετνάμ)",
         "Contract\nManufacturing", '#C62828'),
        (1.2, 3.8, "Υλικά &\nΠρώτες Ύλες\n(BASF, Lycra)",
         "Raw Materials\nSuppliers", '#E65100'),
        (1.2, 1.4, "Logistics\n(UPS, FedEx,\nDB Schenker)",
         "3PL Partners", '#455A64'),
        (11.8, 6.2, "Αθλητές &\nSponsors\n(LeBron, Ronaldo)",
         "Brand\nAmbassadors", '#1565C0'),
        (11.8, 3.8, "Retailers\n(Foot Locker,\nJD Sports)",
         "Licensed\nRetail Partners", '#2E7D32'),
        (11.8, 1.4, "Digital\n(Nike App,\nSnkrs, NRC)",
         "D2C Digital\nPlatform", '#6A1B9A'),
    ]
    for (x, y, label, sublabel, col) in partners:
        draw_box(ax, x, y, 2.1, 1.3, label, color=col, fontsize=7.5,
                 sublabel=None)
        ax.text(x, y - 0.52, sublabel, ha='center', va='top',
                fontsize=6, color='white', style='italic', zorder=4)
        # Arrow to/from core
        if x < 6:
            ax.annotate("", xy=(4.5, y), xytext=(x + 1.05, y),
                        arrowprops=dict(arrowstyle='->', color=col, lw=1.5))
        else:
            ax.annotate("", xy=(8.5, y), xytext=(x - 1.05, y),
                        arrowprops=dict(arrowstyle='<-', color=col, lw=1.5))

    ax.text(6.5, 0.6,
            "Nike κατέχει μόνο το Brand, το Design και τη Στρατηγική — ΟΛΑ τα υπόλοιπα είναι outsourced",
            ha='center', fontsize=8.5, color='#333333', style='italic',
            fontweight='bold')

    ax.text(0.01, 0.01,
            "Πηγή: Nike Inc. Annual Report 2023 · Miles & Snow (1986) · Castells (1996) The Rise of the Network Society",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/network_org.png')


if __name__ == '__main__':
    print("Generating additional org charts...")
    make_divisional()
    make_matrix()
    make_flat()
    make_network()
    print("Done.")
