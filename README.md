# Εργαστήριο 1: Σύστημα Υποστήριξης Αποφάσεων (DSS) με Python

## 📋 Περιγραφή

Αυτό το εργαστήριο εφαρμόζει το μοντέλο λήψης αποφάσεων του Herbert Simon (Intelligence → Design → Choice) για την ανάλυση ακυρώσεων κρατήσεων ξενοδοχείων.

**Στόχος:** Μέσω της ανάλυσης δεδομένων, θα εντοπίσουμε τους παράγοντες που οδηγούν σε ακυρώσεις και θα προτείνουμε πολιτικές για τη μείωσή τους.

## 🔧 Προαπαιτούμενα

- **Python 3.10+** (συνιστάται Python 3.14)
- **VS Code** με την επέκταση Python
- **Git** (προαιρετικό)

## 📦 Εγκατάσταση

### Βήμα 1: Clone ή Download του Project

```bash
# Αν χρησιμοποιείτε Git:
git clone <repository-url>
cd lab1

# Ή κατεβάστε το .zip και εξάγετέ το
```

### Βήμα 2: Δημιουργία Virtual Environment

Ανοίξτε terminal στο VS Code (`Ctrl + ~` ή `View → Terminal`) και εκτελέστε:

#### Για Linux/macOS:
```bash
# Δημιουργία virtual environment
python3 -m venv lab1venv

# Ενεργοποίηση
source lab1venv/bin/activate
```

#### Για Windows:
```cmd
# Δημιουργία virtual environment
python -m venv lab1venv

# Ενεργοποίηση
lab1venv\Scripts\activate
```

### Βήμα 3: Εγκατάσταση Dependencies

Μετά την ενεργοποίηση του virtual environment:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Χρόνος εγκατάστασης:** ~2-3 λεπτά (ανάλογα με τη σύνδεσή σας)

## 🚀 Εκτέλεση στο VS Code

### Μέθοδος 1: Jupyter Notebook (Συνιστάται)

1. **Άνοιγμα του Notebook:**
   - Ανοίξτε το αρχείο `lab1.ipynb` στο VS Code

2. **Επιλογή Kernel:**
   - Κάντε κλικ στο **"Select Kernel"** (πάνω δεξιά)
   - Επιλέξτε **"Python Environments"**
   - Επιλέξτε το `lab1venv` (θα εμφανιστεί ως `Python 3.x.x ('lab1venv')`)

3. **Εκτέλεση Cells:**
   - Πατήστε `Shift + Enter` για να τρέξετε κάθε cell
   - Ή πατήστε **"Run All"** για να τρέξετε όλα τα cells

### Μέθοδος 2: Python Script (Εναλλακτική)

Αν θέλετε να μετατρέψετε το notebook σε Python script:

```bash
# Εγκατάσταση του nbconvert (αν δεν υπάρχει)
pip install nbconvert

# Μετατροπή notebook σε Python script
jupyter nbconvert --to script lab1.ipynb

# Εκτέλεση
python lab1.py
```

## 📊 Δεδομένα

Το dataset `hotel_bookings.csv` περιέχει ιστορικά δεδομένα κρατήσεων ξενοδοχείων με:
- **119,390 εγγραφές** (κρατήσεις)
- **32 χαρακτηριστικά** (π.χ. lead_time, deposit_type, is_canceled)

**Πηγή:** [Hotel Booking Demand Dataset - Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

## 🗂️ Δομή Project

```
lab1/
├── lab1.ipynb              # Κύριο Jupyter Notebook
├── hotel_bookings.csv      # Dataset
├── requirements.txt        # Python dependencies
├── README.md              # Αυτό το αρχείο
└── lab1venv/              # Virtual environment (δημιουργείται από εσάς)
```

## 📚 Βιβλιοθήκες που Χρησιμοποιούνται

- **pandas:** Χειρισμός και ανάλυση δεδομένων
- **numpy:** Αριθμητικοί υπολογισμοί
- **matplotlib:** Δημιουργία γραφημάτων
- **seaborn:** Στατιστική οπτικοποίηση
- **jupyter:** Περιβάλλον Notebook
- **scipy:** (Προαιρετικό) Για προχωρημένη ανάλυση

## 🐛 Troubleshooting

### Πρόβλημα: Δεν βρίσκει το Python virtual environment

**Λύση:**
1. Πατήστε `Ctrl + Shift + P` (ή `Cmd + Shift + P` στο Mac)
2. Γράψτε: `Python: Select Interpreter`
3. Επιλέξτε το `lab1venv/bin/python` (ή `lab1venv\Scripts\python.exe` στα Windows)

### Πρόβλημα: "Module not found" error

**Λύση:**
```bash
# Βεβαιωθείτε ότι το venv είναι ενεργοποιημένο (θα δείτε (lab1venv) στο terminal)
# Εγκαταστήστε ξανά τα dependencies:
pip install -r requirements.txt
```

### Πρόβλημα: Το Jupyter Kernel δεν ξεκινάει

**Λύση:**
```bash
# Εγκαταστήστε ξεχωριστά το ipykernel:
pip install ipykernel
python -m ipykernel install --user --name=lab1venv
```

### Πρόβλημα: Λείπει το αρχείο hotel_bookings.csv

**Λύση:**
Κατεβάστε το dataset από [εδώ](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) και τοποθετήστε το στο φάκελο `lab1/`.

## 💡 Tips

1. **Αποθηκεύστε συχνά:** Πατήστε `Ctrl + S` μετά από κάθε αλλαγή
2. **Clear Output:** Αν το notebook γίνει βαρύ, πατήστε `Ctrl + Shift + P` → `Clear All Outputs`
3. **Restart Kernel:** Αν κολλήσει, πατήστε το κουμπί "Restart" δίπλα στο kernel selector
4. **Ξεσχολιάστε κώδικα:** Μερικά cells έχουν σχολιασμένο κώδικα (`#`) - ξεσχολιάστε τον για να δείτε επιπλέον αναλύσεις

## 📖 Δομή του Notebook

### 1️⃣ Intelligence Phase
- Φόρτωση δεδομένων
- Έλεγχος ποιότητας (Data Inspection)
- Καθαρισμός δεδομένων (Data Cleaning)

### 2️⃣ Design Phase
- Ανάλυση συσχέτισης (Correlation)
- What-if Analysis
- Sensitivity Analysis
- Goal Seek Analysis
- Εποχικότητα, Market Segments, Loyalty

### 3️⃣ Choice Phase
- Συμπεράσματα
- Προτάσεις πολιτικής (Policy Recommendations)

## 🤝 Συνεισφορά

Για προτάσεις ή διορθώσεις, επικοινωνήστε με τον διδάσκοντα.

## 📝 License

Αυτό το εκπαιδευτικό υλικό προορίζεται για ακαδημαική χρήση.

---

**Happy Analyzing! 📊🎓**
