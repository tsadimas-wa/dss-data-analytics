# Semester Project: Design and Development of a Decision Support System (DSS)

## Purpose of the Project
The purpose of this project is to gain hands-on experience in the design and development of a **complete Decision Support System (DSS)**. You are asked to combine Knowledge Representation (Ontologies) with other methods covered in the course (e.g. Machine Learning, Optimisation, Fuzzy Logic, Generative AI) to build a system that solves a practical problem.

## Core Idea
You are asked to develop a Decision Support System whose mandatory core is a **Knowledge Base** grounded in an ontology, extended with **at least one additional technique** from those covered in the course.

---

## Part A: The Knowledge Base (Mandatory)
To build the Knowledge Base, you may choose **one** of the following two paths:

### Option A.1: Extending an Existing Ontology
**Goal:** Extend the ontology you submitted for **Assignment 1** and use it as the foundation of your DSS.

**Requirements:**
1.  **Enrichment (Instantiation):**
    *   Add at least **15 new Individuals** to the existing ontology.
    *   Make sure they cover different classes and are connected to each other via Object Properties.
    > 📌 **Help:** [Protégé Lab §5.6 — Individuals](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#56-creating-individuals) · [Lec 4 — TBox/ABox](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture4_en.md)
2.  **Knowledge Inference:** Use a Reasoner to derive new, implicit knowledge.
    > 📌 **Help:** [Protégé Lab §5.7 — Reasoner](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#57-running-the-reasoner--verification) · [Protégé Lab §6.6 — Reasoner from Python](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#66-inferring-implicit-prerequisites-transitivity-with-reasoner) · [owlready2 docs](https://owlready2.readthedocs.io/en/latest/reasoning.html)
3.  **Querying:** Prepare SPARQL queries that retrieve the knowledge your DSS needs.
    > 📌 **Help:** [Protégé Lab §5.9 — SPARQL in Protégé](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#59-running-sparql-queries-in-protégé) · [Protégé Lab §6.8 — SPARQL from Python](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#68-sparql-queries) · [SPARQL 1.1 Reference](https://www.w3.org/TR/sparql11-query/)

### Option A.2: Designing & Building a New Ontology from Scratch
**Goal:** Design and build a new ontology for a domain of your choice (e.g. E-commerce, Tourism, Healthcare, Logistics).

**Requirements:**
1.  **Class Hierarchy:**
    *   Create at least **10–15 Classes**.
    *   They must have a logical hierarchy (Superclasses – Subclasses) and Disjoint rules where appropriate.
    > 📌 **Help:** [Protégé Lab §5.1 — Design](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#51-ontology-design) · [Protégé Lab §5.3 — Classes](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#53-creating-classes) · [Protégé User Guide](https://protegewiki.stanford.edu/wiki/Protege4UserDocs)
2.  **Properties:**
    *   Define at least **7 Object Properties** (e.g. `works_in`, `has_manager`) with the corresponding Domain, Range, and Inverse properties.
    *   Define at least **5 Data Properties** (e.g. `has_age`, `has_price`).
    > 📌 **Help:** [Protégé Lab §5.4 — Object Properties](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#54-creating-object-properties) · [Protégé Lab §5.5 — Data Properties](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#55-creating-data-properties) · [OWL 2 Property docs](https://www.w3.org/TR/owl2-primer/#Property_Restrictions)
3.  **Individuals:**
    *   Add at least **10 realistic Individuals** to your system and connect them to each other.
    > 📌 **Help:** [Protégé Lab §5.6 — Individuals](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#56-creating-individuals) · [Protégé Lab §6.9 — New Individual from Python](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#69-creating-a-new-individual-from-python)
4.  **SWRL Rule (Optional but recommended):**
    *   Create **at least 1 SWRL rule** of the "IF… THEN…" type that derives new knowledge or classifies individuals into a class.
    > 📌 **Help:** [Protégé Lab §5.8 — SWRL Rules](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#58-writing-swrl-rules) · [SWRL Reference](https://www.w3.org/Submission/SWRL/)

---

## Part B: DSS Extension (Choose 1+ idea)
Once you have built the Knowledge Base, you are asked to extend it by incorporating **at least one** of the following methodologies.

### Idea 1: DSS with Predictive Analytics (Machine Learning)
*   **Description:** Combine the ontology with a Machine Learning model (e.g. Decision Tree, Random Forest) to make predictions.
*   **Example (Loan Approval):**
    1.  **Ontology:** Models concepts such as `Customer`, `LoanApplication`, `Collateral`. A Reasoner can classify a customer as `LowRiskProfile` based on rules (e.g. has a stable job and property).
    2.  **ML Model:** A model (e.g. XGBoost) is trained on historical data to predict the probability of default (`P(default)`).
    3.  **DSS:** The system presents both results: "The ML model predicts an 85% probability of default. This is consistent with our knowledge base, as the customer is classified as `HighRisk` because they have no stable employment." Use **XAI** (SHAP/LIME) to explain the ML prediction.

> 📌 **Help:**
> *   Decision Trees & Random Forest: [Lab 6](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab6_en.ipynb) · [Lec 6](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture6_en.md) · [scikit-learn docs](https://scikit-learn.org/stable/supervised_learning.html)
> *   XGBoost: [Lab 7](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab7_en.ipynb) · [XGBoost docs](https://xgboost.readthedocs.io/en/stable/)
> *   SHAP/LIME (XAI): [Lab 7 §3](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab7_en.ipynb) · [Lec 7](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture7_en.md) · [SHAP docs](https://shap.readthedocs.io/en/latest/) · [LIME docs](https://lime-ml.readthedocs.io/en/latest/)

### Idea 2: DSS with Fuzzy Logic
*   **Description:** Use a Fuzzy Inference System (FIS) to evaluate qualitative, imprecise criteria.
*   **Example (Supplier Selection):**
    1.  **Ontology:** Models suppliers and their products with quantitative attributes (e.g. `deliveryTime`, `defectRate`).
    2.  **Fuzzy System:** Build a FIS that takes the quantitative values as input and converts them into fuzzy terms ("Cost" → `Low`, "Reliability" → `High`). The output is an overall, fuzzy "Supplier Score".
    3.  **DSS:** The user requests the best suppliers. The system retrieves candidates from the ontology, scores them via the FIS, and presents them ranked.

> 📌 **Help:**
> *   Fuzzy Logic / FIS: [Lab 5](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab5_en.ipynb) · [Lec 5](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture5_en.md)
> *   scikit-fuzzy: [scikit-fuzzy docs](https://scikit-fuzzy.readthedocs.io/en/latest/) · [API Reference](https://scikit-fuzzy.readthedocs.io/en/latest/api/skfuzzy.control.html)

### Idea 3: DSS with Optimisation (Evolutionary Algorithms)
*   **Description:** Use a metaheuristic algorithm (e.g. Genetic Algorithm, ACO) to find the optimal solution to a combinatorial problem.
*   **Example (Vehicle Routing):**
    1.  **Ontology:** Models locations, vehicles, and constraints (e.g. a `RefrigeratedTruck` can only carry `PerishableGoods`).
    2.  **Optimisation Algorithm:** A Genetic Algorithm (GA) or Ant Colony Optimisation (ACO) takes a list of delivery points and finds the optimal route (solution to TSP/VRP).
    3.  **DSS:** The user defines the goal ("deliver all perishable goods"). The system queries the ontology to find the relevant locations and available vehicles. This list feeds the GA/ACO, which returns the optimal route map.

> 📌 **Help:**
> *   Genetic Algorithms / ACO: [Lab 8](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab8_en.ipynb) · [Lec 8](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture8_en.md)
> *   PyGAD: [PyGAD docs](https://pygad.readthedocs.io/en/latest/) · [PyGAD API](https://pygad.readthedocs.io/en/latest/pygad.html)

### Idea 4: DSS with Generative AI
*   **Description:** Leverage a Large Language Model (LLM) to generate personalised content, using the ontology as a knowledge source (RAG pattern).
*   **Example (Personalised Marketing):**
    1.  **Ontology:** Models customer profiles, their purchase history, and interests (e.g. a Reasoner classifies a customer as `TechEnthusiast`).
    2.  **Generative AI:** An LLM (e.g. via the GPT or Claude API) is used to compose text.
    3.  **DSS (RAG):** The manager wants to send an email to all "Tech Enthusiasts". The system retrieves from the ontology the list of those customers and their recent purchases. It then constructs a prompt for the LLM: *"You are a marketing expert. Write an email to a customer who recently bought a 'Gaming Laptop' and is a 'Tech Enthusiast'. Recommend a 'Mechanical Keyboard' that is on sale."*

> 📌 **Help:**
> *   LLMs & RAG: [Lab 7 §4](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab7_en.ipynb) · [Lec 7 — Generative AI & RAG](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/lectures/lecture7_en.md)
> *   OpenAI API: [openai Python library](https://platform.openai.com/docs/quickstart) · [API Reference](https://platform.openai.com/docs/api-reference/chat)
> *   Anthropic (Claude) API: [Getting started](https://docs.anthropic.com/en/api/getting-started) · [Messages API](https://docs.anthropic.com/en/api/messages)
> *   Prompt Engineering: [OpenAI Prompt Guide](https://platform.openai.com/docs/guides/prompt-engineering)

---

## Practical Guide & Integration Examples

A common question is: *"How exactly does the Ontology communicate with the algorithm?"*
The Ontology (Protégé) does **not** execute code (ML, Fuzzy, etc.). It works exclusively as your **Smart Knowledge Base**. The "Conductor" that connects everything is your **Python script**.

Let's look at a **unified example** centred on an **E-commerce store**, to understand how each idea is applied:

**The Knowledge Base (Ontology — Part A):**
You have classes `Customer`, `Product`, and `Order`. The Reasoner has SWRL rules that automatically decide whether a customer is a `VIP_Customer` based on their purchases.

**How the Extensions fit in (Part B):**
*   **Idea 1 (Machine Learning — Predictive):**
    *   *Note:* You do not train the ML model on the 15 Individuals in your Ontology (not enough data!).
    *   *Implementation:* In the Python script, train a model (e.g. Random Forest) using an external CSV dataset (e.g. "Customer Churn"). The script then "asks" the ontology for the attributes of a new `VIP_Customer`. Those attributes are passed to the trained ML model for inference, and the DSS suggests: *"The VIP customer is at risk of churning (Churn=Yes) — a discount offer is recommended!"*
*   **Idea 2 (Fuzzy Logic):**
    *   *Implementation:* Products in the ontology have numeric Data Properties (e.g. `hasRating`=4.2, `hasPrice`=850€). Python reads these numbers, feeds them into a Fuzzy Logic System (e.g. the `scikit-fuzzy` library), which applies rules (e.g. *IF Price=High AND Rating=Very Good THEN ValueForMoney=Medium*). The DSS displays the fuzzy score to the manager.
*   **Idea 3 (Optimisation):**
    *   *Implementation:* The ontology contains 15 `Products` with weight and value. The manager has a limited budget. Python retrieves the list of available products via SPARQL. A Genetic Algorithm (GA) runs in Python to find the ideal product combination (Knapsack Problem) that maximises the profit of a campaign.
*   **Idea 4 (Generative AI / RAG):**
    *   *Implementation:* The script queries the ontology: *"What did Customer X recently buy?"*. The answer is `Gaming_Laptop`. Python automatically composes a prompt and calls an LLM API (e.g. OpenAI): *"Write a friendly email to a VIP customer who bought a Gaming Laptop, recommending a Gaming Mouse."*

**Execution Workflow (Python):**
1. **Load:** `onto = get_ontology("my_ontology.owl").load()`
2. **Retrieve:** Fetch data from the ontology (e.g. `onto.Customer.instances()` or via SPARQL).
3. **Transform:** Store the data in variables, lists, or a Pandas DataFrame.
4. **Run Extension:** Call the method (ML prediction / Fuzzy computation / LLM API).
5. **Present:** Print the final decision support output on screen for the end user.

> 📌 **Help:** [Protégé Lab §6 — Python & owlready2](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#6-using-the-ontology-from-python) · [Protégé Lab §6.10 — Complete Script](https://github.com/tsadimas-wa/dss-data-analytics/blob/main/labs/lab_protege_en.md#610-complete-script) · [owlready2 docs](https://owlready2.readthedocs.io/en/latest/)

---

## General System Architecture

The diagram below illustrates the general architecture of the Decision Support System you are asked to implement. The central "brain" is your Python script, which orchestrates the data flow between the Knowledge Base and the specialised method you choose.

![General DSS Architecture](https://raw.githubusercontent.com/tsadimas-wa/dss-data-analytics/main/img/assignments/dss_architecture_en.svg)

---

## Deliverables (For both options)

You must submit a compressed `.zip` file containing **all** of the following:

1.  **The Ontology file:** In `.owl` or `.rdf` format, exported from Protégé.
2.  **The Python script/notebook (`.py` or `.ipynb`):** The code implementing the complete Decision Support System.
3.  **Technical Report (PDF, minimum 20 pages):** A thorough report that must include:
    *   **Introduction:** Description of the problem your DSS solves and the approach you followed.
    *   **System Architecture:** A diagram showing how the components are connected (e.g. Ontology, ML Model, Fuzzy System).
    *   **Knowledge Modelling:** Description of the ontology (main classes, properties, rules).
    *   **Extension Implementation:** Description of the second method you used (e.g. training the ML model, designing the FIS).
    *   **Decision Support:** A usage example showing how a manager would use your system to make a decision.
    *   **Conclusions & Future Work.**

---

## Grading Criteria

| Criterion | Weight | Description |
|---|---|---|
| **Complete DSS Implementation** | 40% | Functionality of the Python script and successful integration of the Knowledge Base with the second methodology. |
| **Correctness of Knowledge Modelling** | 30% | Correct ontology design (hierarchy, properties, rules). Absence of logical errors. |
| **Report Quality & Documentation** | 20% | Clarity, structure, and completeness of the technical report and code. |
| **Originality & Complexity** | 10% | The originality of the idea and the complexity of the technical implementation. |

---

## Grading & Presentation

For **Erasmus students**, the final project accounts for **100%** of the overall course grade. There is no written exam.

The **project presentation** is **mandatory** and will take place on a date to be announced.

---

## Submission

The project (the compressed `.zip` file) must be submitted on eclass via the following link: [Submit Project](https://eclass.uniwa.gr/modules/work/index.php?course=ICE254&id=53401).

**Submission deadline:** 21 June 2026
