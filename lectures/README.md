# Lectures — Οδηγός Μετατροπής σε PDF

Ο κατάλογος περιέχει τις διαλέξεις σε μορφή Markdown (Marp) με ενσωματωμένα **Mermaid** διαγράμματα.

## Απαιτήσεις

| Εργαλείο | Έλεγχος | Εγκατάσταση |
|---|---|---|
| Python 3.10+ | `python3 --version` | συνήθως προεγκατεστημένο |
| Chromium | `which chromium` | `sudo apt install chromium` |
| Σύνδεση internet | — | για render των Mermaid διαγραμμάτων (kroki.io) |

## Μετατροπή Markdown → PDF

```bash
# Από τον κατάλογο lectures/
cd lectures/

# Μία διάλεξη
python3 md_to_pdf.py lecture3_el.md

# Με custom όνομα εξόδου
python3 md_to_pdf.py lecture3_el.md ../output/lecture3.pdf

# Όλα τα αρχεία .md ταυτόχρονα (bash)
for f in *.md; do [[ "$f" != "README.md" ]] && python3 md_to_pdf.py "$f"; done
```

Το PDF αποθηκεύεται δίπλα στο `.md` αρχείο (ίδιο όνομα, κατάληξη `.pdf`), εκτός αν οριστεί custom path.

## Πώς λειτουργεί το script

1. **Αφαιρεί το Marp frontmatter** (`--- ... ---`) από το αρχείο
2. **Pre-renders τα Mermaid διαγράμματα** στέλνοντας κάθε block στο [kroki.io](https://kroki.io) API — λαμβάνει SVG και το ενσωματώνει απευθείας στο HTML
3. **Μετατρέπει το Markdown σε HTML** με `marked.js` (CDN)
4. **Εκτυπώνει σε PDF** με `chromium --headless --print-to-pdf`

> Με αυτή την προσέγγιση τα διαγράμματα είναι ήδη SVG όταν φορτώνει το Chromium — δεν υπάρχει καθυστέρηση JavaScript rendering.

## Δομή καταλόγου

```
lectures/
├── README.md            ← αυτό το αρχείο
├── md_to_pdf.py         ← script μετατροπής
├── lecture1_en.md       ← Ενότητα 1 (αγγλικά)
├── lecture3_el.md       ← Ενότητα 3 (ελληνικά)
└── *.pdf                ← αρχεία εξόδου
```
