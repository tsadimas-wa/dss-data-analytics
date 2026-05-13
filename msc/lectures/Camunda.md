# Οδηγός Υλοποίησης Εκτελέσιμης Διαδικασίας στο Camunda 8

Αυτός ο οδηγός περιγράφει τη μετατροπή ενός θεωρητικού διαγράμματος BPMN σε μια πλήρως λειτουργική Web εφαρμογή που περιλαμβάνει φόρμες χρηστών και αυτοματοποιημένη ενημέρωση στο Slack.

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
