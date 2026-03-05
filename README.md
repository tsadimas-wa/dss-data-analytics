# Εργαστήριο 1: Σύστημα Υποστήριξης Αποφάσεων (DSS) με Python

## Περιεχόμενα

- [Περιγραφή](#-περιγραφή)
- [Μαθησιακοί Στόχοι](#-μαθησιακοί-στόχοι)
- [Προαπαιτούμενα](#-προαπαιτούμενα)
- [Εγκατάσταση](#-εγκατάσταση)
- [Εκτέλεση στο VS Code](#-εκτέλεση-στο-vs-code)
- [Δεδομένα](#-δεδομένα)
- [Δομή Project](#-δομή-project)
- [Βιβλιοθήκες](#-βιβλιοθήκες-που-χρησιμοποιούνται)
- [Στατιστικές Έννοιες](#-στατιστικές-έννοιες-που-καλύπτονται)
- [Δομή Εργαστηρίου](#-δομή--περιεχόμενο-εργαστηρίου)
- [Ασκήσεις & Βαθμολόγηση](#-ασκήσεις--βαθμολόγηση)
- [Troubleshooting](#-troubleshooting)
- [Tips](#-tips)
- [Μαθηματικοί Τύποι](#-μαθηματικοί-τύποι-που-χρησιμοποιούνται)
- [Επιπλέον Πόροι](#-επιπλέον-πόροι)

---

##  Περιγραφή

Αυτό το εργαστήριο εφαρμόζει το μοντέλο λήψης αποφάσεων του Herbert Simon (Intelligence → Design → Choice) για την ανάλυση ακυρώσεων κρατήσεων ξενοδοχείων.

**Στόχος:** Μέσω της ανάλυσης δεδομένων, θα εντοπίσουμε τους παράγοντες που οδηγούν σε ακυρώσεις και θα προτείνουμε πολιτικές για τη μείωσή τους.

## 🎯 Μαθησιακοί Στόχοι

Μετά την ολοκλήρωση του εργαστηρίου, θα μπορείτε να:

1. **Φορτώνετε και καθαρίζετε** μεγάλα datasets με την Pandas
2. **Υπολογίζετε βασικά στατιστικά μέτρα** (mean, median, std, correlation)
3. **Δημιουργείτε οπτικοποιήσεις** (histograms, heatmaps, scatter plots)
4. **Εφαρμόζετε τεχνικές DSS**:
   - Correlation Analysis (Pearson & Spearman)
   - What-If Analysis (προσομοιώσεις σεναρίων)
   - Sensitivity Analysis (εύρεση κρίσιμων παραγόντων)
   - Goal Seek Analysis (αντίστροφος υπολογισμός)
5. **Ερμηνεύετε αποτελέσματα** και προτείνετε επιχειρηματικές πολιτικές
6. **Εφαρμόζετε το μοντέλο Simon** (Intelligence → Design → Choice)

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
- **119,390 εγγραφές** (κρατήσεις από 2015-2017)
- **32 χαρακτηριστικά** (features)
- **2 ξενοδοχεία:** City Hotel & Resort Hotel (Πορτογαλία)

**Βασικά Χαρακτηριστικά:**
- `is_canceled`: Η target μεταβλητή (0 = όχι ακύρωση, 1 = ακύρωση)
- `lead_time`: Ημέρες μεταξύ κράτησης και άφιξης
- `adr`: Average Daily Rate (μέση ημερήσια τιμή)
- `deposit_type`: Τύπος εγγύησης (No Deposit, Non Refund, Refundable)
- `previous_cancellations`: Προηγούμενες ακυρώσεις πελάτη
- `arrival_date_month`: Μήνας άφιξης

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

- **pandas:** Χειρισμός και ανάλυση δεδομένων (DataFrames)
- **numpy:** Αριθμητικοί υπολογισμοί
- **matplotlib:** Δημιουργία γραφημάτων
- **seaborn:** Στατιστική οπτικοποίηση (heatmaps, distributions)
- **jupyter:** Περιβάλλον Notebook
- **scipy:** (Προαιρετικό) Για προχωρημένη ανάλυση

## 📊 Στατιστικές Έννοιες που Καλύπτονται

Το εργαστήριο εισάγει και εφαρμόζει βασικές στατιστικές έννοιες:

### Μέτρα Κεντρικής Τάσης & Διασποράς
- **Μέσος Όρος (Mean), Διάμεσος (Median), Επικρατούσα Τιμή (Mode)**
- **Τυπική Απόκλιση (Std Dev), Διακύμανση (Variance), Εύρος (Range)**
- Χρήση του `df.describe()` για περιληπτική στατιστική

### Ανάλυση Κατανομών
- **Ιστογράμματα (Histograms):** Οπτικοποίηση κατανομών
- **Binning/Discretization:** Μετατροπή συνεχών μεταβλητών σε κατηγορίες με `pd.cut()` και `pd.qcut()`
- **Ασύμμετρες κατανομές (Skewness):** Εντοπισμός outliers

### Συσχέτιση & Σχέσεις Μεταβλητών
- **Συντελεστής Pearson (r):** Γραμμική συσχέτιση
- **Συντελεστής Spearman (ρ):** Μονοτονική συσχέτιση
- **Heatmaps:** Οπτικοποίηση πίνακα συσχέτισης
- **Scatter Plots:** Εντοπισμός μη-γραμμικών σχέσεων

### Χρονοσειρές & Εξομάλυνση
- **Rolling Average (Κινητός Μέσος Όρος):** Εξομάλυνση θορύβου σε δεδομένα
- **Εποχικότητα:** Ανάλυση μηνιαίων προτύπων

> ⚠️ **Σημαντικό:** Συσχέτιση ≠ Αιτιότητα. Το ότι δύο μεταβλητές συσχετίζονται δεν σημαίνει ότι η μία *προκαλεί* την άλλη.

## 🎯 Δομή & Περιεχόμενο Εργαστηρίου

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
5. **Διαβάστε τα Markdown Cells:** Περιέχουν θεωρία και επεξηγήσεις για κάθε ανάλυση
6. **Εκτελέστε τα Cells με Σειρά:** Ξεκινήστε από το πρώτο cell και προχωρήστε σταδιακά

## 📐 Μαθηματικοί Τύποι που Χρησιμοποιούνται

### Συντελεστής Pearson
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i-\bar{x})^2} \cdot \sqrt{\sum(y_i-\bar{y})^2}} \quad \in [-1, +1]$$

### Κινητός Μέσος Όρος (Rolling Average)
$$\bar{x}_t^{(w)} = \frac{1}{w} \sum_{i=t-w+1}^{t} x_i$$

Όπου:
- $w$ = window size (πλήθος παρατηρήσεων για εξομάλυνση)
- $t$ = τρέχουσα χρονική στιγμή

### Φάση 1️⃣: Intelligence (Κατανόηση του Προβλήματος)
- **Φόρτωση Dataset:** Import του `hotel_bookings.csv` (119,390 κρατήσεις)
- **Data Inspection:** Έλεγχος τύπων δεδομένων, ελλείπουσες τιμές, outliers
- **Data Cleaning:** Χειρισμός missing values, αφαίρεση ακραίων τιμών
- **Περιγραφική Στατιστική:** Υπολογισμός μέσων, τυπικών αποκλίσεων, κατανομών

### Φάση 2️⃣: Design (Ανάλυση & Μοντελοποίηση)
**Α. Correlation Analysis (Ανάλυση Συσχέτισης)**
- Pearson & Spearman correlation matrices
- Heatmap οπτικοποίηση
- Tornado Chart για ιεράρχηση παραγόντων επιρροής

**Β. What-If Analysis**
- Προσομοίωση σεναρίων: "Τι θα συμβεί αν αλλάξει ο `lead_time`;"
- Επίδραση μεταβολών σε βασικές μεταβλητές

**Γ. Sensitivity Analysis**
- Εύρεση των πιο "ευαίσθητων" παραγόντων
- Binning με `pd.cut()` και `pd.qcut()`

**Δ. Goal Seek Analysis**
- Αντίστροφος υπολογισμός: "Ποιο `lead_time` χρειάζεται για 30% ακυρώσεις;"

**Ε. Πρόσθετες Αναλύσεις**
- **Εποχικότητα:** Ανάλυση μηνιαίων τάσεων
- **Market Segments:** Σύγκριση Online vs Offline κρατήσεων
- **Customer Loyalty:** Επίδραση επαναλαμβανόμενων επισκέψεων
- **ADR (Average Daily Rate) Analysis:** Σχέση τιμής-ακύρωσης

### Φάση 3️⃣: Choice (Λήψη Απόφασης)
- **Ερμηνεία Αποτελεσμάτων:** Κατανόηση των παραγόντων που οδηγούν σε ακυρώσεις
- **Policy Recommendations:** Προτάσεις για μείωση ακυρώσεων
  - Πολιτικές εγγύησης (deposit policies)
  - Διαχείριση `lead_time` (όρια προκράτησης)
  - Στρατηγικές τιμολόγησης (dynamic pricing)
  - Customer loyalty programs

## 🎓 Ασκήσεις & Βαθμολόγηση

Το εργαστήριο περιλαμβάνει **5 κύριες ασκήσεις** (20 μόρια η καθεμία = 100 μόρια):

1. **Άσκηση 1-2:** Intelligence Phase (Data Cleaning & Inspection)
2. **Άσκηση 3:** Correlation & Tornado Chart
3. **Άσκηση 4:** Sensitivity & Goal Seek Analysis
4. **Άσκηση 5:** What-If Analysis & Binning
5. **Άσκηση 6 (Bonus):** Pearson vs Spearman (+10 μόρια)

**Κριτήρια Αξιολόγησης:**
- ✅ Σωστός κώδικας Python
- ✅ Γραφήματα με τίτλους και ετικέτες αξόνων
- ✅ Σχολιασμός/ερμηνεία αποτελεσμάτων σε markdown ή `print()`

## 🤝 Συνεισφορά

Για προτάσεις ή διορθώσεις, επικοινωνήστε με τον διδάσκοντα.

##  Επιπλέον Πόροι

### Τεκμηρίωση Βιβλιοθηκών
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Μάθηση Python & Data Science
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Kaggle Learn](https://www.kaggle.com/learn) - Δωρεάν courses
- [Real Python Tutorials](https://realpython.com/)

### Decision Support Systems
- Herbert Simon - "The New Science of Management Decision"
- Ralph Sprague & Eric Carlson - "Building Effective Decision Support Systems"

## License

Αυτό το εκπαιδευτικό υλικό προορίζεται για ακαδημαϊκή χρήση.

---

**Happy Analyzing! 📊🎓**
