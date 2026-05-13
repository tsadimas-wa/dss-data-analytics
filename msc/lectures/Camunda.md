# Οδηγός Υλοποίησης Εκτελέσιμης Διαδικασίας στο Camunda 8

Αυτός ο οδηγός περιγράφει τη μετατροπή ενός θεωρητικού διαγράμματος BPMN σε μια πλήρως λειτουργική web εφαρμογή με φόρμες χρηστών και αυτόματη ειδοποίηση Slack.

**Τι θα μάθουμε:**
- Διαφορά μοντέλου (BPMN XML) και instance (εκτέλεση) σε πραγματικό περιβάλλον
- Ανάπτυξη User Tasks με φόρμες στο Tasklist
- Χρήση XOR Gateway για διαφορετικά μονοπάτια (Εγκρίθηκε / Απορρίφθηκε)
- Αυτόματη ενημέρωση Slack μέσω Connector χωρίς κώδικα

---

## 1. Προετοιμασία Περιβάλλοντος

- **Εγγραφή:** Δημιουργήστε δωρεάν λογαριασμό στο [Camunda Cloud](https://camunda.io/).
- **Cluster:** Στην κονσόλα, δημιουργήστε νέο Cluster (Free Tier) — βεβαιωθείτε ότι η κατάσταση είναι **Healthy** πριν συνεχίσετε.

### 1.1 Slack Bot (προαιρετικό)

1. Δημιουργήστε App στο [Slack API](https://api.slack.com/apps).
2. **OAuth & Permissions** → προσθέστε Scope `chat:write` → **Install to Workspace**.
3. Αντιγράψτε το **Bot User OAuth Token** (`xoxb-...`).
4. Στο Slack κανάλι: `/invite @Όνομα_Bot`.

> Αν δεν θέλετε να ρυθμίσετε Slack, παραλείψτε το §1.1 και το §4 — η υπόλοιπη ροή λειτουργεί ανεξάρτητα.

---

## 2. Σχεδίαση Διαγράμματος (BPMN)

Στο **Web Modeler**, δημιουργήστε νέο Project και BPMN διάγραμμα με την εξής ροή:

```
Start Event
  → User Task "Submit Request"         (φόρμα υποβολής)
  → User Task "Manager Approval"       (φόρμα έγκρισης)
  → XOR Gateway "Εγκρίθηκε;"
      [isApproved = true]  → Slack Connector "Notify Team" → End Event "Εγκρίθηκε"
      [isApproved = false] → End Event "Απορρίφθηκε"
```

**Βήματα στον Modeler:**
1. Σύρετε τα στοιχεία από την παλέτα (αριστερά).
2. Ονομάστε κάθε στοιχείο κάνοντας διπλό κλικ.
3. Για το **XOR Gateway**: κάντε κλικ → εικονίδιο ρόμβου με X. Τραβήξτε δύο βέλη εξόδου — ένα προς τον Connector και ένα προς το End Event "Απορρίφθηκε".

---

## 3. Κατασκευή Φορμών (Camunda Forms)

### 3.1 Φόρμα Υποβολής — `SubmitForm`

Νέο → Form. Προσθέστε:

| Τύπος Πεδίου | Label | Key |
|---|---|---|
| Text Field | Όνομα Υπαλλήλου | `empName` |
| Number Field | Ημέρες άδειας | `days` |

### 3.2 Φόρμα Έγκρισης — `ApprovalForm`

| Τύπος Πεδίου | Label | Key | Ρύθμιση |
|---|---|---|---|
| Text Field | Όνομα Υπαλλήλου | `empName` | **Read-only: ✅** |
| Number Field | Ημέρες άδειας | `days` | **Read-only: ✅** |
| Checkbox | Εγκρίνεις; | `isApproved` | — |

> ⚠️ **Σημαντικό:** Τα **Keys** είναι case-sensitive. `empName` ≠ `EmpName`. Τα Read-only πεδία εμφανίζουν τα δεδομένα από την 1η φόρμα.

### 3.3 Σύνδεση Φορμών με Tasks

Για κάθε User Task: κλικ → καρτέλα **Form** → **Camunda Form** → επιλέξτε τη φόρμα → **Link**.

---

## 4. Ρύθμιση XOR Gateway

Κάντε κλικ στο **βέλος** που οδηγεί στον Slack Connector και ορίστε **Condition Expression**:

```
= isApproved = true
```

Στο βέλος προς το End Event "Απορρίφθηκε":

```
= isApproved = false
```

> 💡 Οι εκφράσεις γράφονται σε **FEEL** (Friendly Enough Expression Language) — η γλώσσα εκφράσεων του Camunda. Πάντα ξεκινούν με `=`.

---

## 5. Ρύθμιση Slack Connector

Κάντε κλικ στο task ειδοποίησης → **Template** → **Slack Outbound Connector**:

| Πεδίο | Τιμή |
|---|---|
| **Authentication Token** | `xoxb-...` (το token από §1.1) |
| **Channel** | `#approvals` (το όνομα του καναλιού) |
| **Message** | *(βλ. παρακάτω)* |

Στο πεδίο **Message**, ενεργοποιήστε **Expression mode** (`= fx`) και εισάγετε:

```
= "Η άδεια για τον υπάλληλο " + empName + " εγκρίθηκε για " + string(days) + " ημέρες!"
```

> ⚠️ Χρησιμοποιήστε **μόνο** το πεδίο Message — αφήστε το πεδίο **Blocks κενό**. Η σύνδεση `+` είναι έγκυρη FEEL σύνταξη. Η συνάρτηση `string()` είναι απαραίτητη για αριθμούς.

---

## 6. Deploy και Εκτέλεση

1. **Deploy:** Πατήστε **Deploy** (πάνω δεξιά) → επιβεβαιώστε το cluster.
2. **Start Instance:** Πατήστε **Run → Start Instance** (μπορείτε να αφήσετε κενές τις process variables).
3. **Tasklist** — ανοίξτε από το κεντρικό μενού:
   - Βρείτε το task `Submit Request` → **Assign to me** (το "Claim") → συμπληρώστε τη φόρμα → **Complete**.
   - Βρείτε το task `Manager Approval` → **Assign to me** → συμπληρώστε (τσεκάρετε ή ξετσεκάρετε το "Εγκρίνεις;") → **Complete**.
4. **Operate** — ελέγξτε ότι το instance ολοκληρώθηκε στο σωστό End Event.
5. **Slack** — αν εγκρίθηκε, ελέγξτε το κανάλι για την αυτόματη ειδοποίηση.

> 💡 **"Assign to me" (Claim):** Ένα User Task ανατίθεται συνήθως σε ρόλο — όλοι οι χρήστες του ρόλου το βλέπουν. Με το Claim το "κλειδώνετε" για τον εαυτό σας ώστε κανένας άλλος να μην το επεξεργαστεί παράλληλα.

---

## 7. Συχνά Σφάλματα (Troubleshooting)

| Σφάλμα | Αιτία | Λύση |
|---|---|---|
| Κενά πεδία στη 2η φόρμα | Λανθασμένο Key (case) | Βεβαιωθείτε ότι `empName` είναι ακριβώς ίδιο και στις δύο φόρμες |
| `Invalid Expression` κατά Deploy | Η FEEL expression δεν ξεκινά με `=` | Βεβαιωθείτε ότι οι conditions αρχίζουν με `= isApproved = true` |
| Connector Error (Blocks field) | Χρησιμοποιήθηκε το πεδίο Blocks | Αφήστε το Blocks κενό — χρησιμοποιήστε μόνο το Message |
| `string() not found` | Αριθμός χωρίς μετατροπή | Χρησιμοποιήστε `string(days)` αντί για `days` στο FEEL |
| Gateway — token δεν προχωρά | Καμία condition δεν ικανοποιείται | Ελέγξτε ότι `isApproved` επιστρέφει `true`/`false` (boolean, όχι string) |
| Instance δεν εμφανίζεται στο Tasklist | Φόρμα δεν συνδέθηκε | Ελέγξτε καρτέλα Form στο User Task — πρέπει να λέει "Linked Form" |


---

## 1. Προετοιμασία Περιβάλλοντος

- **Εγγραφή:** Δημιουργήστε έναν δωρεάν λογαριασμό στο [Camunda Cloud](https://camunda.io/).
- **Cluster:** Στην κονσόλα, δημιουργήστε ένα νέο Cluster (Free Tier) και βεβαιωθείτε ότι η κατάσταση είναι **Healthy**.

### Slack Bot

1. Δημιουργήστε ένα App στο [Slack API](https://api.slack.com/apps).
2. Στα **OAuth & Permissions**, προσθέστε το Scope `chat:write`.
3. Κάντε **Install** στο Workspace και αντιγράψτε το **Bot User OAuth Token** (`xoxb-...`).
4. Προσθέστε το Bot στο κανάλι σας στο Slack (`/invite @Όνομα_Bot`).

---

## 2. Σχεδίαση Διαγράμματος (BPMN)

Στο **Web Modeler**, δημιουργήστε ένα νέο Project και ένα BPMN διάγραμμα με την εξής ροή:

1. **Start Event** — Έναρξη της διαδικασίας.
2. **User Task** `Submit Request` — Ο υπάλληλος υποβάλλει την αίτηση.
3. **User Task** `Manager Approval` — Ο προϊστάμενος εγκρίνει ή απορρίπτει.
4. **Slack Connector** `Notify Team` — Αυτόματη ενημέρωση για την έγκριση.
5. **End Event** — Ολοκλήρωση.

---

## 3. Κατασκευή Φορμών (Camunda Forms)

### Φόρμα Υποβολής — `SubmitForm`

Δημιουργήστε μια νέα φόρμα και προσθέστε:

| Τύπος Πεδίου | Label | Key |
|---|---|---|
| Text Field | Employee Name | `empName` |
| Number Field | Days requested | `days` |

### Φόρμα Έγκρισης — `ApprovalForm`

Δημιουργήστε μια δεύτερη φόρμα:

| Τύπος Πεδίου | Label | Key | Ρύθμιση |
|---|---|---|---|
| Text Field | Employee Name | `empName` | Read-only |
| Number Field | Days requested | `days` | Read-only |
| Checkbox | Approve? | `isApproved` | — |

> **Προσοχή:** Τα **Keys** πρέπει να είναι πανομοιότυπα (case-sensitive) για να μεταφέρονται τα δεδομένα μεταξύ των Tasks.

---

## 4. Ρύθμιση του Slack Connector

Επιλέξτε το Task της ειδοποίησης και ρυθμίστε το ως **Slack Connector**:

- **Method:** Post a message
- **Channel:** Το όνομα του καναλιού (π.χ. `approvals`)
- **Message:** Ενεργοποιήστε το Expression mode (`fx`) και εισάγετε το json:

```json
[
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "Η άδεια για τον υπάλληλο *" + empName + "* εγκρίθηκε για *" + string(days) + "* ημέρες! :tada:"
    }
  }
]
```

- **Authentication:** Επικολλήστε το Slack Token (`xoxb-...`).

---

## 5. Deployment και Εκτέλεση

1. **Σύνδεση Φορμών:** Στο BPMN, επιλέξτε κάθε User Task και στην καρτέλα **Forms** αντιστοιχίστε τη σωστή φόρμα (`SubmitForm` και `ApprovalForm`).
2. **Deploy:** Πατήστε το κουμπί **Deploy** πάνω δεξιά.
3. **Start Instance:** Πατήστε **Run → Start Instance**.
4. **Tasklist:**
   - Μεταβείτε στο **Tasklist** από το κεντρικό μενού.
   - Κάντε **Claim** και ολοκληρώστε το πρώτο Task.
   - Κάντε το ίδιο για το δεύτερο Task.
5. **Επαλήθευση:** Ελέγξτε το κανάλι σας στο Slack για την αυτόματη ειδοποίηση.

---

## Συχνά Σφάλματα (Troubleshooting)

| Σφάλμα | Αιτία / Λύση |
|---|---|
| Κενά πεδία στη 2η φόρμα | Ελέγξτε αν τα Keys των πεδίων είναι ολόιδια (case-sensitive) |
| Deploy error — `Invalid Expression` | Το FEEL Expression στο Slack πρέπει να ξεκινά με `"` και όχι με `=` |
| Connector Error (Block section) | Χρησιμοποιήστε το πεδίο **Message** και αφήστε το πεδίο **Blocks** κενό |
