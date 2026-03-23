# Assignment: Build Your Own Ontology

## Description

Now that you understand the process from design to code execution, it's time to apply your knowledge independently!

**Goal:** Design, build, and query your own ontology from start to finish.

---

## A. Choose a Domain

Choose **one** of the following suggested domains, or propose your own:

1. **E-commerce:** Customers, Orders, Products, Categories (e.g. Electronics, Clothing), Reviews.
2. **Cinema/Movies:** Films, Actors, Directors, Genres, Theaters.
3. **Healthcare (Hospital):** Doctors (by specialty), Patients, Diseases, Medications/Treatments.
4. **Library:** Books, Authors, Publishers, Members, Loans.
5. **Tourism/Hotels:** Hotels, Rooms, Customers, Services (Amenities), Reservations.

---

## B. Protégé Requirements

Build your ontology in Protégé making sure it contains **at least**:

### B.1 Classes
- **4–5 classes** with hierarchy (e.g. Subclasses).
- Use **Disjoint** where appropriate (e.g. two subclasses that cannot overlap).

### B.2 Object Properties
- **3 Object Properties** with defined **Domain** and **Range**.
- Apply at least one logical characteristic (e.g. *Inverse Of*, *Functional*, *Transitive*, *Symmetric*).

### B.3 Data Properties
- **3 Data Properties** (e.g. names, prices, dates, ages) with the appropriate data type (`xsd:string`, `xsd:integer`, `xsd:float`).

### B.4 Individuals
- **5–10 Individuals** connected to each other via the Object & Data Properties you created.

### B.5 SWRL Rule (Optional)
- **1 SWRL rule** of the "IF... THEN..." type.
- Example: "If a book has more than 500 pages, it is a `LargeBook`".

### B.6 Validation & Export
- Run the **Reasoner (HermiT)** in Protégé to make sure there are no logical errors (Inconsistencies).
- Save the ontology in **OWL/XML** format (e.g. `my_ontology.owl`).

---

## C. Introduction to SPARQL

**SPARQL** (SPARQL Protocol and RDF Query Language) is the official query language for RDF data and OWL ontologies. It works similarly to SQL, but targets Knowledge Graphs.

### Basic query structure

```sparql
PREFIX ex: <http://example.org/ontology#>

SELECT ?subject ?property ?object
WHERE {
    ?subject ?property ?object .
}
```

- **PREFIX**: defines shorthand aliases for namespaces.
- **SELECT**: specifies which variables to return.
- **WHERE**: defines the **triple patterns** (subject–predicate–object) that must match.

### Examples

**1. Get all individuals of a class:**
```sparql
PREFIX ex: <http://example.org/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?person
WHERE {
    ?person rdf:type ex:Customer .
}
```

**2. Get individuals with a specific property value:**
```sparql
SELECT ?customer ?room
WHERE {
    ?customer ex:hasBooked ?room .
    ?room ex:price ?price .
    FILTER(?price > 100)
}
```

**3. Using SPARQL with `owlready2` in Python:**
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

> **Note:** `default_world.sparql()` executes SPARQL queries over the ontology loaded into `owlready2`'s `default_world`.

---

## D. Python Requirements (`owlready2`)

Write a Python script (e.g. `ontology_test.py`) or a Jupyter Notebook (`.ipynb`) that:

1. **Loads** your `.owl` file using the `owlready2` library.
2. **Prints** a list of all classes in the ontology.
3. **Runs the Reasoner** via Python (`sync_reasoner_hermit()`) to check ontology consistency.
4. **Executes a SPARQL query** via `default_world.sparql()` that returns a meaningful result.
   - Example: "Get all customers who booked a room costing more than 100€".

---

## Deliverables

| File | Description |
|---|---|
| `my_ontology.owl` | Your ontology in OWL/XML format |
| `ontology_test.py` or `ontology_test.ipynb` | Python code with loading, reasoner and SPARQL |

---

## Submission

- **Platform:** eclass, via the assignment **"Ontology Assignment"**
- **Deadline:** April 4, 2026
- This is an **individual** assignment.
- The assignment is **not graded**, but you will receive **feedback** on your work.
