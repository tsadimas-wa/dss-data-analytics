# Lectures — Οδηγός Δημιουργίας HTML & PDF

Ο κατάλογος περιέχει τις διαλέξεις σε μορφή [Marp](https://marp.app/) Markdown με ενσωματωμένα **Mermaid** διαγράμματα.  
Δύο scripts μετατρέπουν κάθε `.md` αρχείο σε αυτόνομο **HTML** (για παρουσίαση στο browser) ή σε **PDF** (για εκτύπωση/διανομή).

---

## Απαιτήσεις

| Εργαλείο | Έλεγχος | Εγκατάσταση |
|---|---|---|
| Python 3.10+ | `python3 --version` | συνήθως προεγκατεστημένο |
| Node.js 20 (μέσω nvm) | `nvm use 20` | `nvm install 20` |
| Marp CLI | `marp --version` | `npm i -g @marp-team/marp-cli` |
| Chromium | `which chromium` | `sudo apt install chromium` |
| Σύνδεση internet | — | για render Mermaid μέσω kroki.io |

> **Σημείωση για Node:** Το Marp CLI δεν λειτουργεί σωστά με Node v25+.  
> Χρησιμοποιείστε Node 20 μέσω nvm: `nvm install 20 && nvm use 20`

---

## Μετατροπή Markdown → HTML

```bash
cd lectures/

# Μία διάλεξη
python3 md_to_html.py lecture3_el.md

# Με custom όνομα εξόδου
python3 md_to_html.py lecture3_el.md ../output/lecture3.html

# Όλα τα αρχεία ταυτόχρονα
for f in lecture*.md; do python3 md_to_html.py "$f"; done
```

Το HTML αποθηκεύεται δίπλα στο `.md` (ίδιο όνομα, κατάληξη `.html`).  
Είναι **αυτόνομο** (self-contained): εικόνες, logo και διαγράμματα είναι ενσωματωμένα ως base64 — δεν χρειάζεται internet για να το ανοίξετε.

### Χαρακτηριστικά HTML παρουσίασης

- Πλοήγηση με **βελάκια** ή **Page Up / Page Down**
- **Auto-scale**: το κείμενο συρρικνώνεται αυτόματα αν ξεφεύγει από το slide
- **UNIWA logo** στην πρώτη σελίδα
- Mermaid διαγράμματα ως SVG (pre-rendered μέσω kroki.io)

---

## Μετατροπή Markdown → PDF

```bash
cd lectures/

# Μία διάλεξη
python3 md_to_pdf.py lecture3_el.md

# Με custom όνομα εξόδου
python3 md_to_pdf.py lecture3_el.md ../output/lecture3.pdf

# Όλα τα αρχεία ταυτόχρονα
for f in lecture*.md; do python3 md_to_pdf.py "$f"; done
```

Το PDF αποθηκεύεται δίπλα στο `.md` (ίδιο όνομα, κατάληξη `.pdf`).

### Πώς λειτουργεί το md_to_pdf.py

1. Τρέχει ολόκληρο το pipeline του `md_to_html.py` (mermaid pre-render, logo, auto-scale JS)
2. Εκτυπώνει το HTML σε PDF με **Chromium headless** (`--print-to-pdf`)
3. Το `--virtual-time-budget=5000` δίνει χρόνο στο JavaScript να κλιμακώσει **όλες** τις σελίδες πριν την εκτύπωση

> Η προσέγγιση εγγυάται ότι το PDF αντιστοιχεί ακριβώς στο HTML — το ίδιο rendering engine, τα ίδια fonts, η ίδια κλιμάκωση κειμένου.

---

## Πώς λειτουργεί το md_to_html.py

1. **Pre-renders τα Mermaid blocks** → SVG μέσω [kroki.io](https://kroki.io) API (fallback: mermaid.ink)
2. **Μετατρέπει σε HTML** με `marp --html --allow-local-files` (Node 20 via nvm)
3. **Ενσωματώνει** τις τοπικές εικόνες (π.χ. `uniwa_logo.png`) ως base64 data URIs
4. **Εγχέει** JavaScript auto-scale που συρρικνώνει το font-size ανά slide αν χρειαστεί

---

## Δομή καταλόγου

```
lectures/
├── README.md              ← αυτό το αρχείο
├── md_to_html.py          ← Markdown → HTML (Marp + Mermaid + logo)
├── md_to_pdf.py           ← Markdown → PDF (μέσω HTML + Chromium)
├── lecture1_el.md         ← Ενότητα 1 (ελληνικά)
├── lecture1_en.md         ← Ενότητα 1 (αγγλικά)
├── lecture3_el.md         ← Ενότητα 3 (ελληνικά)
├── lecture3_en.md         ← Ενότητα 3 (αγγλικά)
├── uniwa_logo.png         ← λογότυπο ΠΑΔΑ (ενσωματώνεται ως base64)
└── *.html / *.pdf         ← αρχεία εξόδου
```
