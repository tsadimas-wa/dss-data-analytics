---
marp: true
theme: default
paginate: true
math: katex
header: 'Ενότητα 4: Business Analytics, Big Data & Process Mining'
footer: 'Πανεπιστήμιο Δυτικής Αττικής (ΠΑΔΑ) — Συστήματα Αποφάσεων, Διαχείριση Διεργασιών και Επιχειρηματική Ανάλυση'
style: |
  section {
    font-size: 22px;
  }
  section.small {
    font-size: 18px;
  }

  section.xsmall {
    font-size: 16px;
  }

  section.xxsmall {
    font-size: 14px;
  }

  /* Three-column layout */
  .columns3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
  }


  /* Two-column layout */
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  /* Slide με μόνο διάγραμμα — μεγάλο max-height εικόνας */
  section.diagram img {
    max-height: 500px !important;
    max-width: 94% !important;
    display: block;
    margin: 0 auto;
  }
  /* Slide με διάγραμμα + κείμενο */
  section.diagram-sm img {
    max-height: 320px !important;
    max-width: 94% !important;
    display: block;
    margin: 0 auto;
  }
  /* Case Study slides */
  section.casestudy {
    background: #fff7ed;
    color: #1e293b;
  }
  section.casestudy h1 {
    color: #c2410c;
    border-bottom: 2px solid #f97316;
    padding-bottom: 4px;
  }
  section.casestudy strong {
    color: #9a3412;
  }
  section.casestudy em {
    color: #b45309;
  }
  section.casestudy blockquote {
    border-left: 4px solid #f97316;
    background: rgba(249,115,22,0.08);
    color: #374151;
  }
  section.casestudy table th {
    background: #ea580c;
    color: #ffffff;
  }
  section.casestudy table td {
    border-color: #fed7aa;
    color: #1e293b;
  }
  section.casestudy table tr:nth-child(even) td {
    background: rgba(249,115,22,0.06);
  }
  section.casestudy header, section.casestudy footer {
    color: #9a3412;
  }
  /* Company logo — top-right corner of case study slides */
  .slide-logo {
    position: absolute;
    top: 58px;
    right: 20px;
    width: 62px;
    border-radius: 50%;
    opacity: 0.92;
    z-index: 10;
  }
---

<div style="text-align:center; margin-bottom:16px;">

![w:280](../../img/shared/uniwa_logo.png)

</div>

# Συστήματα Αποφάσεων, Διαχείριση Διεργασιών και Επιχειρηματική Ανάλυση
**Ενότητα 4: Business Analytics, Big Data & Process Mining**

Πανεπιστήμιο Δυτικής Αττικής

**Διδάσκων:** Ανάργυρος Τσαδήμας (<tsadimas@uniwa.gr>)

---

<!-- _class: xsmall -->
# Ενότητα 4 — Περίγραμμα

1. **Εισαγωγή & Ιστορική Εξέλιξη** — Από τα MIS & DSS στη Σύγχρονη Τεχνητή Νοημοσύνη
2. **Το Οικοσύστημα των Δεδομένων** — Data Warehouses, ERP & Κινητήριες Δυνάμεις DSS
3. **Από τα RDBMS στα Big Data** — Τα 5 V's των Μεγάλων Δεδομένων
4. **Ταξινομία της Αναλυτικής** — Descriptive, Predictive & Prescriptive Analytics
5. **Process Mining** — Ανακάλυψη, Συμμόρφωση & Βελτίωση (Ξυπνώντας τα Δεδομένα)
6. **Η Σύγκλιση (Convergence)** — AI, Data Science & Robotic Process Automation (RPA)

---

<!-- _class: xxsmall -->
# Η Ιστορική Εξέλιξη: Από το Reporting στην Τεχνητή Νοημοσύνη

Η ορολογία και οι δυνατότητες των συστημάτων υποστήριξης αποφάσεων εξελίχθηκαν ραγδαία τα τελευταία 50 χρόνια:

![h:200](../img/lec4/bi-evolution.png)
<div class="columns">
<div>

* **1970s — Θεμέλια (MIS & DSS):** 
  Μετάβαση από τις απλές αναφορές ρουτίνας στα Πληροφοριακά Συστήματα Διοίκησης (MIS) και στα πρώτα Συστήματα Υποστήριξης Αποφάσεων (DSS). Εστίαση σε ημι-δομημένα προβλήματα και μαθηματικά μοντέλα Επιχειρησιακής Έρευνας (OR).
* **1980s — Ενοποίηση & Έμπειρα Συστήματα:** 
  Εγκατάλειψη των απομονωμένων αρχείων χάρη στα Συστήματα Σχεσιακών Βάσεων Δεδομένων (RDBMS) και τα πρώτα ERP (ενιαία πηγή αλήθειας). Εμφάνιση των Έμπειρων Συστημάτων (Rule-based Expert Systems).
* **1990s — Αποθήκες Δεδομένων (DW) & EIS:** 
  Δημιουργία Data Warehouses για να μην επιβαρύνονται τα transactional συστήματα (ERP) από τις αναλύσεις. Ανάπτυξη Executive Information Systems (EIS) με γραφικά Dashboards και Scorecards.

</div>
<div>

* **2000s — Business Intelligence (BI):** 
  Τα συστήματα μετονομάζονται σε BI. Άνθιση της εξόρυξης δεδομένων και κειμένου (Data & Text Mining) για ανακάλυψη γνώσης. Ανάπτυξη μοντέλων Cloud / SaaS, κάνοντας την ανάλυση προσιτή σε μικρομεσαίες επιχειρήσεις.
* **2010s — Η Έκρηξη των Big Data:** 
  Νέες πηγές μη-δομημένων δεδομένων (Social Media, RFID, IoT). Εισαγωγή νέων τεχνολογιών υλισμικού και λογισμικού (όπως Hadoop, MapReduce, NoSQL, MPP) για τη διαχείριση του τεράστιου όγκου και της πολυπλοκότητας.
* **2020s+ — AI, Deep Learning & Αυτοματοποίηση:** 
  Streaming Analytics, ενσωμάτωση του IoT με Deep Learning (αναγνώριση εικόνας/φωνής), Smart Assistants (π.χ. Alexa) και παραγωγική ΤΝ (ChatGPT) που αλλάζουν ριζικά τον τρόπο αλληλεπίδρασης και λήψης αποφάσεων.

</div>
</div>

---

<!-- _class: xsmall -->
# Επιχειρηματική Ευφυΐα (Business Intelligence - BI)

Η **Επιχειρηματική Ευφυΐα (BI)** είναι ένας όρος-ομπρέλα που συνδυάζει αρχιτεκτονικές, εργαλεία, βάσεις και μεθοδολογίες για τη διαδραστική **μετατροπή δεδομένων σε πληροφορία, αποφάσεις και δράσεις**.

<div class="columns">
<div>

**Εξέλιξη & Κινητήριες Δυνάμεις**
* **Ιστορία:** Ξεκίνησε από τα στατικά MIS (70s) και τα EIS (80s). Ο όρος καθιερώθηκε από την Gartner (90s). Από το 2005+ ενσωματώνει δυνατότητες AI.
* **Ανάγκη για Ταχύτητα:** Οι εξαιρετικά συμπιεσμένοι επιχειρηματικοί κύκλοι απαιτούν τη "σωστή πληροφορία, τη σωστή στιγμή, στο σωστό μέρος".
* **Κανονιστική Συμμόρφωση:** Νομοθετικές απαιτήσεις (π.χ. Sarbanes-Oxley Act) υποχρεώνουν τις διοικήσεις να τεκμηριώνουν τις αποφάσεις τους με αξιόπιστα δεδομένα.

</div>
<div>

**Η Αρχιτεκτονική του BI (4 Πυλώνες)**

1. 🗄️ **Αποθήκη Δεδομένων (Data Warehouse - DW):** Η κεντρική, ενοποιημένη πηγή των ιστορικών και τρεχόντων δεδομένων.
2. ⚙️ **Business Analytics:** Εργαλεία για επεξεργασία, εξόρυξη (data mining) και βαθιά ανάλυση των δεδομένων.
3. 📈 **BPM (Business Performance Management):** Συστήματα για την παρακολούθηση και ανάλυση της επιχειρησιακής απόδοσης.
4. 💻 **Διεπαφή Χρήστη (User Interface):** Διαδραστικά εργαλεία οπτικοποίησης (π.χ. Dashboards & Scorecards) για άμεση πρόσβαση από τους decision makers.

</div>
</div>

---

# 1. Το Οικοσύστημα των Δεδομένων

* **Από το ERP στις Αποθήκες Δεδομένων (Data Warehouses):**
  * Το ERP (π.χ. SAP) καταγράφει τις συναλλαγές (OLTP). 
  * Για να κάνουμε ανάλυση, τα δεδομένα μεταφέρονται σε **Data Warehouses** και **Data Lakes**, όπου καθαρίζονται και ενοποιούνται.
* **Το «Ψηφιακό Αποτύπωμα» (Digital Footprint):**
  * Κάθε δραστηριότητα στο σύστημα αφήνει ίχνη. Απαραίτητα στοιχεία για ανάλυση:
    1. **Ποια υπόθεση;** (Case ID / π.χ. Αρ. Παραγγελίας)
    2. **Τι έγινε;** (Activity / π.χ. Έγκριση)
    3. **Πότε έγινε;** (Timestamp)

---

<!-- _class: xsmall -->
# 1.1 Κινητήριες Δυνάμεις Ανάπτυξης των DSS και της Αναλυτικής

Πέρα από την προφανή εξέλιξη σε υλισμικό (Hardware), λογισμικό (Software) και δίκτυα, οι παρακάτω παράγοντες έχουν επιταχύνει καθοριστικά τη χρήση Συστημάτων Υποστήριξης Αποφάσεων (DSS) και Business Analytics:

<div class="columns">
<div>

* 🤝 **Ομαδική Επικοινωνία & Συνεργασία:** Απομακρυσμένη λήψη αποφάσεων από ομάδες, εργαλεία συνεργασίας και άμεσος διαμοιρασμός δεδομένων σε πραγματικό χρόνο στην εφοδιαστική αλυσίδα.
* 🗄️ **Βελτιωμένη Διαχείριση Δεδομένων:** Γρήγορη, οικονομική και ασφαλής αποθήκευση/μετάδοση πολύπλοκων και ετερογενών δεδομένων (κείμενο, ήχος, βίντεο) εντός και εκτός οργανισμού.
* 🐘 **Διαχείριση Big Data & Data Warehouses:** Νέες τεχνολογίες (Cloud, Hadoop/Spark, παράλληλη επεξεργασία) ρίχνουν το κόστος και επιτρέπουν την ανάλυση τεράστιων όγκων δεδομένων.
* 🧠 **Υπέρβαση Γνωστικών Ορίων (Cognitive Limits):** Ο ανθρώπινος εγκέφαλος έχει περιορισμένη ικανότητα επεξεργασίας (Simon, 1977). Τα συστήματα ξεπερνούν αυτά τα όρια εξαλείφοντας τα λάθη.

</div>
<div>

* 📈 **Ενισχυμένη Αναλυτική Υποστήριξη:** Γρήγορη αξιολόγηση εναλλακτικών, βελτιωμένες προβλέψεις, ανάλυση ρίσκου και εκτέλεση πολύπλοκων προσομοιώσεων και σεναρίων.
* 📚 **Διαχείριση Γνώσης (Knowledge Management):** Αξιοποίηση εσωτερικής πληροφορίας και αλληλεπιδράσεων (π.χ. μέσω Text Analytics) για την παραγωγή αξίας και υποστήριξης των managers.
* 📱 **Υποστήριξη Παντού & Πάντα (Anywhere, Anytime):** Mobile τεχνολογίες επιτρέπουν την άμεση πρόσβαση σε δεδομένα και την ταχύτατη λήψη αποφάσεων εν κινήσει.
* 🤖 **Καινοτομία & Τεχνητή Νοημοσύνη (AI):** Η πολυπλοκότητα απαιτεί καινοτομία. Η ΤΝ ενσωματώνεται στην αναλυτική, δημιουργώντας ισχυρές συνέργειες σε κάθε βήμα λήψης αποφάσεων.

</div>
</div>

---

# 2. Από τα RDBMS στα Big Data (Τα 5 V's)

Τα παραδοσιακά συστήματα έφτασαν στα όριά τους. Τα **Big Data** δεν είναι απλώς "πολλά δεδομένα". Ορίζονται (Sharda et al., 2023) από τα **5 V's**:

1. **Volume (Όγκος):** Terabytes και Petabytes δεδομένων (π.χ. αισθητήρες IoT).
2. **Velocity (Ταχύτητα):** Δεδομένα σε πραγματικό χρόνο (streaming data).
3. **Variety (Ποικιλία):** 80-85% των δεδομένων είναι *μη-δομημένα* (κείμενα, βίντεο, audio, social media).
4. **Veracity (Αξιοπιστία):** Η διαχείριση του "θορύβου" και των λαθών (Garbage in, Garbage out).
5. 🏆 **Value (Αξία):** Τα δεδομένα είναι άχρηστα αν δεν μετατραπούν σε επιχειρηματική αξία και στρατηγικό πλεονέκτημα.

---

<!-- _class: xsmall -->
# 3. Η Ταξινομία της Αναλυτικής (Analytics Taxonomy)

Ο όρος **Αναλυτική (Analytics)** αντικαθιστά σταδιακά το BI. Σύμφωνα με την INFORMS, είναι ο συνδυασμός τεχνολογίας, διοικητικής επιστήμης και στατιστικής για την εξαγωγή στοχευμένων δράσεων. Χωρίζεται σε **3 αλληλένδετα επίπεδα**:

<div class="columns">
<div>

📊 **1. Περιγραφική Αναλυτική (Descriptive)**
* **Ερωτήσεις:** *Τι συνέβη; Τι συμβαίνει τώρα;*
* **Σκοπός:** Κατανόηση της τρέχουσας κατάστασης και των τάσεων μέσω της ενοποίησης ιστορικών δεδομένων (από DWs).
* **Εργαλεία:** Αναφορές, Dashboards, Οπτικοποίηση Δεδομένων.
* **Case Study (Silvaris):** Χρησιμοποίησε το Tableau για real-time οπτικοποίηση των logistics της, γλιτώνοντας 100άδες σελίδες αναφορών και βελτιώνοντας την στόχευση πελατών.

</div>
<div>

🎯 **2. Προβλεπτική Αναλυτική (Predictive)**
* **Ερωτήσεις:** *Τι θα συμβεί; Γιατί θα συμβεί;*
* **Σκοπός:** Ακριβείς προβλέψεις για το μέλλον (π.χ. customer churn, ανταπόκριση σε προσφορές, πιστωτικό ρίσκο).
* **Εργαλεία:** Data/Text Mining, Forecasting, Machine Learning (Αλγόριθμοι ταξινόμησης & ομαδοποίησης).

🚀 **3. Καθοδηγητική Αναλυτική (Prescriptive)**
* **Ερωτήσεις:** *Τι πρέπει να κάνω;*
* **Σκοπός:** Λήψη των βέλτιστων δυνατών αποφάσεων (actionable insights) βάσει των προβλέψεων.
* **Εργαλεία:** Βελτιστοποίηση (Optimization), Προσομοίωση, Έμπειρα Συστήματα.

</div>
</div>

---

# 4. Process Mining: Ξυπνώντας τα Δεδομένα

Η Επιστήμη Δεδομένων συναντά το BPM. Το Process Mining διαβάζει τα Event Logs και παράγει *αυτόματα* τα διαγράμματα:

* 🔍 **Discovery (Ανακάλυψη):** Το εργαλείο ανακαλύπτει τη *στυγνή αλήθεια*. Παράγει το "Spaghetti Model" – βλέπουμε παρακάμψεις που δεν υπάρχουν σε κανένα οργανόγραμμα.
* ⚖️ **Conformance Checking (Έλεγχος Συμμόρφωσης):** 
* Συγκρίνουμε το "Ιδανικό" BPMN με τα Πραγματικά Δεδομένα.
  * *Στόχος:* Εντοπισμός απάτης, Maverick Buying (αγορές εκτός διαδικασίας) και παραβιάσεων κανονισμών.
* ⏱️ **Enhancement (Βελτίωση & Ανάλυση Αιτιών):**
  * Εισαγωγή χρόνου και κόστους στο μοντέλο. Εντοπισμός των πραγματικών **Bottlenecks**.

---

# 5. Η Σύγκλιση: AI, Data Science & Process Automation

Το τελικό στάδιο του ψηφιακού μετασχηματισμού:

* **Cognitive Analytics & AI:** Συστήματα που μαθαίνουν από τα δεδομένα και κατανοούν πλαίσιο (context).
* **Από τη Γνώση στη Δράση (Actionable Insights):**
  * Όταν το Predictive μοντέλο προβλέψει ένα bottleneck στη διαδικασία, τι γίνεται;
  * Το σύστημα πυροδοτεί **Αυτοματοποιημένες Αποφάσεις (Automated Decision Making)**.
* **RPA (Robotic Process Automation):** Ψηφιακά «ρομποτάκια» που αναλαμβάνουν αυτόματα τα επαναλαμβανόμενα βήματα της διαδικασίας που εντοπίστηκαν μέσω του Process Mining, δουλεύοντας 24/7.

---

<!-- _class: xsmall -->
# Ενότητα 4 — Σύνοψη

| Θέμα | Βασικές Έννοιες |
|---|---|
| **Ιστορική Εξέλιξη & BI** | MIS, DSS, Data Warehouses, Business Intelligence, 4 Πυλώνες BI |
| **Οικοσύστημα & DSS** | Κινητήριες δυνάμεις (Συνεργασία, Cognitive limits, Cloud, Big Data, AI) |
| **Big Data** | Τα 5 V's: Volume, Velocity, Variety, Veracity, Value |
| **Analytics Taxonomy** | Descriptive (Τι έγινε;), Predictive (Τι θα γίνει;), Prescriptive (Τι να κάνω;) |
| **Process Mining** | Εξαγωγή γνώσης από Event Logs, Discovery, Conformance, Enhancement |
| **Σύγκλιση (Convergence)**| Συνδυασμός AI, Predictive Models και RPA για αυτοματοποίηση αποφάσεων |

---

<!-- _class: xsmall -->
# Ενότητα 4 — Βιβλιογραφία

**Κύρια Συγγράμματα:**
* **Sharda, R., Delen, D., & Turban, E.** (2023). *Analytics, Data Science, & Artificial Intelligence: Systems for Decision Support* (11th ed.). Pearson.

**Συμπληρωματικές Πηγές:**
* **Simon, H. A.** (1977). *The New Science of Management Decision*. Prentice-Hall. (Γνωστικά όρια στη λήψη αποφάσεων)
* **van der Aalst, W.** (2016). *Process Mining: Data Science in Action*. Springer.
* **Gorry, G. A., & Scott-Morton, M. S.** (1971). *A Framework for Management Information Systems*. Sloan Management Review.
* **Keen, P. G. W., & Scott-Morton, M. S.** (1978). *Decision Support Systems: An Organizational Perspective*. Addison-Wesley.