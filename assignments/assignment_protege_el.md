# Εργασία: Αναπτύξτε τη δική σας Οντολογία

## Περιγραφή

Τώρα που κατανοήσατε τη διαδικασία από τον σχεδιασμό μέχρι την εκτέλεση κώδικα, ήρθε η ώρα να εφαρμόσετε τις γνώσεις σας αυτόνομα!

**Στόχος:** Να σχεδιάσετε, να κατασκευάσετε και να ερωτήσετε μια δική σας οντολογία από την αρχή μέχρι το τέλος.

---

## Α. Επιλογή Πεδίου (Domain)

Επιλέξτε **ένα** από τα παρακάτω ενδεικτικά πεδία, ή προτείνετε ένα δικό σας:

1. **Ηλεκτρονικό Κατάστημα (E-commerce):** Πελάτες, Παραγγελίες, Προϊόντα, Κατηγορίες (π.χ. Ηλεκτρονικά, Ρούχα), Κριτικές.
2. **Κινηματογράφος (Cinema/Movies):** Ταινίες, Ηθοποιοί, Σκηνοθέτες, Είδη (Genres), Αίθουσες.
3. **Σύστημα Υγείας (Hospital):** Γιατροί (ανά ειδικότητα), Ασθενείς, Ασθένειες, Φάρμακα/Θεραπείες.
4. **Βιβλιοθήκη (Library):** Βιβλία, Συγγραφείς, Εκδοτικοί Οίκοι, Μέλη, Δανεισμοί.
5. **Τουρισμός (Tourism/Hotels):** Ξενοδοχεία, Δωμάτια, Πελάτες, Υπηρεσίες (Παροχές), Κρατήσεις.

---

## Β. Απαιτήσεις στο Protégé

Κατασκευάστε την οντολογία σας στο Protégé φροντίζοντας να περιέχει **τουλάχιστον**:

### Β.1 Κλάσεις (Classes)
- **4–5 κλάσεις** με ιεραρχία (π.χ. Subclasses).
- Χρήση **Disjoint** όπου έχει νόημα (π.χ. δύο υποκλάσεις που δεν μπορούν να επικαλύπτονται).

### Β.2 Object Properties
- **3 Object Properties** με ορισμένα **Domain** και **Range**.
- Εφαρμόστε τουλάχιστον ένα λογικό χαρακτηριστικό (π.χ. *Inverse Of*, *Functional*, *Transitive*, *Symmetric*).

### Β.3 Data Properties
- **3 Data Properties** (π.χ. ονόματα, τιμές, ημερομηνίες, ηλικίες) με τον κατάλληλο τύπο δεδομένων (`xsd:string`, `xsd:integer`, `xsd:float`).

### Β.4 Individuals (Στιγμιότυπα)
- **5–10 Individuals** συνδεδεμένα μεταξύ τους μέσω των Object & Data Properties που δημιουργήσατε.

### Β.5 SWRL Rule (Προαιρετικό)
- **1 κανόνας SWRL** τύπου "IF... THEN...".
- Παράδειγμα: "Αν ένα βιβλίο έχει πάνω από 500 σελίδες, είναι `LargeBook`".

### Β.6 Έλεγχος & Εξαγωγή
- Τρέξτε τον **Reasoner (HermiT)** στο Protégé για να βεβαιωθείτε ότι δεν υπάρχουν λογικά σφάλματα (Inconsistencies).
- Αποθηκεύστε την οντολογία σε μορφή **OWL/XML** (π.χ. `my_ontology.owl`).

---

## Γ. Εισαγωγή στη SPARQL

Η **SPARQL** (SPARQL Protocol and RDF Query Language) είναι η επίσημη γλώσσα ερωτημάτων για δεδομένα RDF και οντολογίες OWL. Λειτουργεί παρόμοια με την SQL, αλλά απευθύνεται σε γράφους γνώσης (Knowledge Graphs).

### Βασική δομή ερωτήματος

```sparql
PREFIX ex: <http://example.org/ontology#>

SELECT ?subject ?property ?object
WHERE {
    ?subject ?property ?object .
}
```

- **PREFIX**: ορίζει συντομογραφίες για namespaces.
- **SELECT**: επιλέγει τις μεταβλητές που θέλουμε να επιστραφούν.
- **WHERE**: ορίζει τα **triple patterns** (υποκείμενο–κατηγόρημα–αντικείμενο) που πρέπει να ταιριάζουν.

### Παραδείγματα

**1. Φέρε όλα τα individuals μιας κλάσης:**
```sparql
PREFIX ex: <http://example.org/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?person
WHERE {
    ?person rdf:type ex:Customer .
}
```

**2. Φέρε individuals με συγκεκριμένη ιδιότητα:**
```sparql
SELECT ?customer ?room
WHERE {
    ?customer ex:hasBooked ?room .
    ?room ex:price ?price .
    FILTER(?price > 100)
}
```

**3. Χρήση με `owlready2` στην Python:**
```python
from owlready2 import *

onto = get_ontology("my_ontology.owl").load()

results = list(default_world.sparql("""
    PREFIX ex: <http://example.org/ontology#>
    SELECT ?customer
    WHERE { ?customer a ex:Customer . }
"""))

for r in results:
    print(r)
```

> **Σημείωση:** Το `default_world.sparql()` εκτελεί SPARQL ερωτήματα πάνω στην οντολογία που έχει φορτωθεί στο `default_world` της `owlready2`.

---

## Δ. Απαιτήσεις στην Python (`owlready2`)

Γράψτε ένα Python script (π.χ. `ontology_test.py`) ή ένα Jupyter Notebook (`.ipynb`) το οποίο:

1. **Φορτώνει** το `.owl` αρχείο σας χρησιμοποιώντας τη βιβλιοθήκη `owlready2`.
2. **Εκτυπώνει** μια λίστα με όλες τις κλάσεις της οντολογίας.
3. **Εκτελεί τον Reasoner** μέσω Python (`sync_reasoner_hermit()`) για να ελέγξει τη συνέπεια της οντολογίας.
4. **Εκτελεί ένα SPARQL ερώτημα** μέσω `default_world.sparql()` που να φέρνει ένα ουσιαστικό αποτέλεσμα.
   - Παράδειγμα: "Φέρε μου όλους τους πελάτες που έκαναν κράτηση σε δωμάτιο που κοστίζει πάνω από 100€".

---

## Παραδοτέα

| Αρχείο | Περιγραφή |
|---|---|
| `my_ontology.owl` | Η οντολογία σας σε μορφή OWL/XML |
| `ontology_test.py` ή `ontology_test.ipynb` | Ο κώδικας Python με φόρτωση, reasoner και SPARQL |

---

## Υποβολή

- **Πλατφόρμα:** eclass, μέσω της εργασίας **"Εργασία στις οντολογίες"**
- **Προθεσμία:** 4 Απριλίου 2026
- Η εργασία είναι **ατομική**.
- Η εργασία **δεν βαθμολογείται**, αλλά θα λάβετε **feedback** για τη δουλειά σας.
