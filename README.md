# DSS Data Analytics

Welcome! / Καλώς ήρθατε!

This repository contains lab material, lectures, and assignments for the **Decision Support Systems (DSS) — Data Analytics** course at the University of West Attica (UNIWA).

---

## Repository Structure

```
dss-data-analytics/
├── labs/                    # Lab guides and notebooks
│   ├── lab1_greek.ipynb     # Lab 1 — DSS with Python (Greek)
│   ├── lab1_english.ipynb   # Lab 1 — DSS with Python (English)
│   ├── lab_protege_el.md    # Lab — Protégé & Ontologies (Greek)
│   ├── lab_protege_en.md    # Lab — Protégé & Ontologies (English)
│   ├── ex1.ipynb            # Exercise 1
│   ├── protege/             # Ontology files (.owx, .rdf)
│   └── README_*.md          # Lab-specific instructions
├── lectures/                # Lecture slides (Marp Markdown)
│   ├── lecture*_el.md       # Lectures in Greek
│   ├── lecture*_en.md       # Lectures in English
│   └── README.md            # Build instructions for HTML/PDF
├── assignments/             # Student assignments
│   ├── assignment_protege_el.md
│   └── assignment_protege_en.md
├── datasets/                # CSV datasets
│   ├── hotel_bookings.csv
│   └── SampleSuperstore.csv
├── img/                     # Shared images and diagrams
├── scripts/                 # Utility scripts (md → html, md → pdf)
├── requirements.txt         # Python dependencies
└── lab1venv/                # Virtual environment (not tracked)
```

---

## Choose Your Language / Επιλέξτε Γλώσσα

### Lab 1 — DSS with Python

| Language | Instructions | Notebook |
|---|---|---|
| English | [README_ENGLISH.md](labs/README_ENGLISH.md) | [lab1_english.ipynb](labs/lab1_english.ipynb) |
| Ελληνικά | [README_GREEK.md](labs/README_GREEK.md) | [lab1_greek.ipynb](labs/lab1_greek.ipynb) |

### Lab 5 — Fuzzy Logic (Ασαφής Λογική)

| Language | Notebook |
|---|---|
| Ελληνικά | [lab5_el.ipynb](labs/lab5_el.ipynb) |

### Lab — Protégé & Ontologies

| Language | Guide |
|---|---|
| English | [lab_protege_en.md](labs/lab_protege_en.md) |
| Ελληνικά | [lab_protege_el.md](labs/lab_protege_el.md) |

---

## Quick Start

1. Clone or download this repository
2. Create and activate a virtual environment, install dependencies:

```bash
python3 -m venv lab1venv
source lab1venv/bin/activate        # Linux/macOS
# lab1venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

3. Open the lab notebook of your choice in VS Code

---

## Datasets

- **Hotel Booking Demand** — [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
- **Sample Superstore** — Tableau sample dataset
