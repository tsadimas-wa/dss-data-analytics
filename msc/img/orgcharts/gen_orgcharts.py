#!/usr/bin/env python3
"""Generate org chart PNG images using matplotlib for Marp slides."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

BG      = 'white'
LINE    = '#999999'
TITLE   = '#1a1a1a'
SOURCE  = '#888888'
ANNOT   = '#444444'

# ── helpers ──────────────────────────────────────────────────────────────────

def draw_box(ax, x, y, w, h, label, color='#1a3e6e', text_color='white',
             fontsize=9, sublabel=None):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.02",
                         facecolor=color, edgecolor='white', linewidth=1.5,
                         zorder=2)
    ax.add_patch(box)
    if sublabel:
        ax.text(x, y + 0.05, label, ha='center', va='center',
                fontsize=fontsize, color=text_color, fontweight='bold',
                wrap=True, zorder=3)
        ax.text(x, y - 0.12, sublabel, ha='center', va='center',
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


# ── 1. Alphabet / Google ──────────────────────────────────────────────────────

def make_alphabet():
    fig, ax = plt.subplots(figsize=(15, 8.5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 15); ax.set_ylim(0, 8.5)
    ax.axis('off')
    ax.set_title("Alphabet Inc. — Εταιρική Δομή (Holding)", color=TITLE,
                 fontsize=13, fontweight='bold', pad=12)

    # ── CEO ──
    draw_box(ax, 7.5, 7.8, 3.2, 0.72,
             "Sundar Pichai — CEO, Alphabet & Google",
             color='#1a3e6e', fontsize=9)

    # ── Level 2: Google LLC | Other Bets ──
    # Google centered over left cluster (x≈3.5), Other Bets over right (x≈11.5)
    draw_box(ax, 3.5, 6.5, 2.8, 0.68,
             "Google LLC\n(Core Business)", color='#1565C0', fontsize=9)
    draw_box(ax, 11.5, 6.5, 2.8, 0.68,
             "Other Bets\n(Moonshots)", color='#6A1B9A', fontsize=9)
    draw_line(ax, 7.5, 7.44, 3.5, 6.84)
    draw_line(ax, 7.5, 7.44, 11.5, 6.84)

    # ── Google divisions: 5 boxes, step = 1.4, box_w = 1.25 ──
    # centers: 0.8, 2.2, 3.6, 5.0, 6.4  → gap = 0.15 between each
    gdiv = [
        (0.8,  "Search &\nAds",     '#1976D2'),
        (2.2,  "YouTube",           '#1976D2'),
        (3.6,  "Android /\nChrome", '#1976D2'),
        (5.0,  "Google Cloud",      '#0277BD'),
        (6.4,  "Maps &\nHardware",  '#1976D2'),
    ]
    for x, label, col in gdiv:
        draw_box(ax, x, 5.1, 1.25, 0.7, label, color=col, fontsize=7.8)
        draw_line(ax, 3.5, 6.16, x, 5.45)

    # ── Other Bets: 3 boxes, step = 1.7, box_w = 1.4 ──
    # centers: 9.9, 11.6, 13.3 → gap = 0.3
    obets = [
        (9.9,  "Waymo\n(Self-driving)", '#8E24AA'),
        (11.6, "Verily\n(Life Sciences)",'#8E24AA'),
        (13.3, "DeepMind\n(AI Research)",'#7B1FA2'),
    ]
    for x, label, col in obets:
        draw_box(ax, x, 5.1, 1.4, 0.7, label, color=col, fontsize=7.8)
        draw_line(ax, 11.5, 6.16, x, 5.45)

    # ── Support functions: 4 boxes under Google, step = 1.65, box_w = 1.5 ──
    # centers: 0.9, 2.55, 4.2, 5.85 → gap = 0.15
    support = [
        (0.9,  "Finance &\nStrategy"),
        (2.55, "People\nOps (HR)"),
        (4.2,  "Legal &\nCompliance"),
        (5.85, "Engineering\n& Research"),
    ]
    for x, label in support:
        draw_box(ax, x, 3.6, 1.5, 0.7, label, color='#455A64', fontsize=7.5)

    ax.text(3.4, 2.95,
            "── Υπηρεσίες Υποστήριξης Google LLC ──",
            ha='center', va='center', fontsize=7.5, color=ANNOT, style='italic')

    # ── Legend — πάνω δεξιά, εκτός κουτιών ──
    legend_items = [
        mpatches.Patch(color='#1565C0', label='Google Core'),
        mpatches.Patch(color='#0277BD', label='Google Cloud'),
        mpatches.Patch(color='#8E24AA', label='Other Bets'),
        mpatches.Patch(color='#455A64', label='Support Functions'),
    ]
    ax.legend(handles=legend_items, loc='upper right', fontsize=8,
              facecolor='#f5f5f5', labelcolor='#222222', edgecolor='#cccccc',
              framealpha=1.0, bbox_to_anchor=(0.99, 0.52))

    ax.text(0.01, 0.02,
            "Πηγή: Alphabet Inc. 10-K Annual Report 2023 · alphabet.com",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/alphabet_org.png')


# ── 2. Amazon ────────────────────────────────────────────────────────────────

def make_amazon():
    fig, ax = plt.subplots(figsize=(13, 7.5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 13); ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title("Amazon — Divisional + Two-Pizza Teams", color=TITLE,
                 fontsize=13, fontweight='bold', pad=12)

    # CEO
    draw_box(ax, 6.5, 7.0, 3.0, 0.65,
             "Andy Jassy — CEO", color='#BF360C', fontsize=9)

    # S-Team (top divisions)
    divisions = [
        (1.3,  "Amazon\nNorth America\n(Retail)", '#E64A19'),
        (3.2,  "Amazon\nInternational\n(Retail)", '#E64A19'),
        (5.1,  "Amazon Web\nServices\n(AWS)",     '#1565C0'),
        (7.0,  "Advertising\n& Prime\nVideo",     '#2E7D32'),
        (8.9,  "Alexa &\nDevices",                '#6A1B9A'),
        (10.8, "Logistics &\nFulfillment\n(Amazon Air)", '#455A64'),
        (12.2, "Amazon\nHealth &\nPhysical Stores",'#00695C'),
    ]
    for x, label, col in divisions:
        draw_box(ax, x, 5.5, 1.6, 0.9, label, color=col, fontsize=7)
        draw_line(ax, 6.5, 6.68, x, 5.95)

    # Two-pizza team explanation box
    box_bg = FancyBboxPatch((0.3, 2.9), 5.5, 1.8,
                            boxstyle="round,pad=0.05",
                            facecolor='#FFF8E1', edgecolor='#FB8C00', linewidth=1.8,
                            zorder=2)
    ax.add_patch(box_bg)
    ax.text(3.05, 4.5, "Two-Pizza Team Rule (Bezos)",
            ha='center', fontsize=9, color='#E65100', fontweight='bold', zorder=3)
    ax.text(3.05, 4.1,
            "Κάθε ομάδα πρέπει να μπορεί να ταϊστεί\n"
            "με 2 πίτσες (~6–10 άτομα).\n"
            "Αυτόνομη, με πλήρη ownership του service.",
            ha='center', fontsize=7.5, color='#333333', linespacing=1.5, zorder=3)

    # Mini team diagram
    team_y = 2.3
    team_xs = [1.5, 2.5, 3.5, 4.5, 5.5]
    team_labels = ["PM", "SDE 1", "SDE 2", "UX", "Data\nEngineer"]
    draw_box(ax, 3.5, team_y + 0.7, 1.5, 0.5,
             "Team Lead", color='#E65100', fontsize=8)
    for x, lbl in zip(team_xs, team_labels):
        draw_box(ax, x, team_y, 0.8, 0.5, lbl, color='#1976D2', fontsize=7)
        draw_line(ax, 3.5, team_y + 0.45, x, team_y + 0.25)

    # AWS sub-structure
    aws_box = FancyBboxPatch((6.5, 2.5), 6.0, 2.2,
                             boxstyle="round,pad=0.05",
                             facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=1.5,
                             zorder=2)
    ax.add_patch(aws_box)
    ax.text(9.5, 4.5, "AWS — Διαιρετική Δομή ανά Υπηρεσία",
            ha='center', fontsize=8.5, color='#0D47A1', fontweight='bold', zorder=3)

    aws_services = [
        (7.3,  "Compute\n(EC2, Lambda)"),
        (8.8,  "Storage\n(S3, EBS)"),
        (10.3, "AI/ML\n(SageMaker)"),
        (11.8, "Database\n(RDS, DynamoDB)"),
    ]
    for x, lbl in aws_services:
        draw_box(ax, x, 3.2, 1.35, 0.7, lbl, color='#1565C0', fontsize=7)

    ax.text(0.1, 0.02,
            "Πηγή: Amazon.com Inc. 2023 Annual Report · Bezos Letters to Shareholders 1997–2021",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/amazon_org.png')


# ── 3. Apple ─────────────────────────────────────────────────────────────────

def make_apple():
    fig, ax = plt.subplots(figsize=(13, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 13); ax.set_ylim(2.8, 7)
    ax.axis('off')
    ax.set_title("Apple Inc. — Λειτουργική Δομή (Functional)", color=TITLE,
                 fontsize=13, fontweight='bold', pad=12)

    # CEO
    draw_box(ax, 6.5, 6.4, 3.2, 0.7,
             "Tim Cook — CEO", color='#212121', fontsize=9.5)

    # Direct reports (C-suite / VPs)
    level2 = [
        (1.0,  "SVP\nSoftware Eng.\n(Craig Federighi)", '#1A237E'),
        (2.8,  "SVP\nHardware Eng.\n(John Ternus)",     '#1A237E'),
        (4.6,  "SVP\nMarketing &\nComms",               '#1A237E'),
        (6.4,  "CFO\n(Luca Maestri)",                   '#1B5E20'),
        (8.2,  "SVP\nRetail &\nPeople",                 '#1A237E'),
        (10.0, "SVP\nServices\n(Eddy Cue)",             '#1A237E'),
        (11.8, "SVP\nOperations\n(Jeff Williams)",      '#1A237E'),
    ]
    for x, label, col in level2:
        draw_box(ax, x, 5.0, 1.6, 0.85, label, color=col, fontsize=6.8)
        draw_line(ax, 6.5, 6.05, x, 5.43)

    # Software sub-teams
    sw_teams = [
        (0.6, "iOS /\niPadOS"),
        (1.6, "macOS /\nXcode"),
        (2.6, "AI &\nSiri"),
    ]
    for x, lbl in sw_teams:
        draw_box(ax, x, 3.7, 0.9, 0.55, lbl, color='#283593', fontsize=6.8)
        draw_line(ax, 1.0, 4.58, x, 3.98)

    # Hardware sub-teams
    hw_teams = [
        (2.5, "iPhone\nHW"),
        (3.4, "Mac /\nM-series"),
        (4.3, "Wearables\nAW, AirPods"),
    ]
    for x, lbl in hw_teams:
        draw_box(ax, x, 3.7, 0.85, 0.55, lbl, color='#B71C1C', fontsize=6.8)
        draw_line(ax, 2.8, 4.58, x, 3.98)

    # Services sub-teams
    svc_teams = [
        (9.3,  "App Store\n& iCloud"),
        (10.4, "Apple TV+\n& Music"),
        (11.5, "Apple Pay\n& Wallet"),
    ]
    for x, lbl in svc_teams:
        draw_box(ax, x, 3.7, 0.9, 0.55, lbl, color='#1B5E20', fontsize=6.8)
        draw_line(ax, 10.0, 4.58, x, 3.98)

    ax.text(0.1, 0.02,
            "Πηγή: Apple Inc. Proxy Statement 2023 · Isaacson W. (2011) Steve Jobs · Lashinsky A. (2012) Inside Apple",
            ha='left', va='bottom', fontsize=6.5, color=SOURCE,
            transform=ax.transAxes)

    save(fig, '/home/rg/Teaching/uniwa/dss-data-analytics/msc/img/orgcharts/apple_org.png')


if __name__ == '__main__':
    print("Generating org charts...")
    make_alphabet()
    make_amazon()
    make_apple()
    print("Done.")
