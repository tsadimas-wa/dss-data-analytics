---
marp: true
theme: default
paginate: true
header: 'Unit 1: Foundations & Decision Theory'
footer: 'University of West Attica (UNIWA) — Intelligent Systems & DSS'
style: |
  section {
    font-size: 22px;
  }
  section.small {
    font-size: 18px;
  }
---

# Intelligent Systems & Decision Support Systems (DSS)
## Unit 1: Foundations & Decision Theory

**Professor:** Anargyros Tsadimas
**Institution:** University of West Attica (UNIWA)
**Programme:** MSc / Postgraduate — Data Analytics & Intelligent Systems

---

# Unit 1 — Outline

1. The Knowledge Hierarchy (DIKW Pyramid)
2. Explicit vs. Tacit Knowledge
3. What is a "Decision"?
4. The 6 Steps of Rational Decision Making
5. Good Decision vs. Good Outcome
6. Types of Decisions (By Structure)
7. Decisions by Degree of Certainty
8. Dependent vs. Independent Decisions
9. MIS vs. DSS
10. Herbert Simon's Decision Model
11. Architecture of a DSS: The 3 Pillars
12. The Power of DSS: Dynamic Analysis
13. Connecting Theory to Practice

---

# 1. The Knowledge Hierarchy (DIKW Pyramid)

Before making decisions, we must understand how raw data evolves into actionable wisdom:

| Level | Definition | Example |
|---|---|---|
| **Data** | Unprocessed facts, no context | `"37"` |
| **Information** | Data + context/meaning | `"Body temperature is 37°C"` |
| **Understanding** | Answers *why* — patterns & causes | `"37°C is normal; 39°C means fever"` |
| **Knowledge** | Understanding accumulated over time | `"Fever often signals infection"` |
| **Wisdom** | Applying knowledge to novel, complex problems | `"Don't over-prescribe antibiotics"` |

> 💡 A DSS operates at the **Information → Knowledge** transition: it turns raw data into actionable intelligence for decision-makers.

---

# 2. Types of Knowledge: Explicit vs. Tacit

| | Explicit Knowledge | Tacit Knowledge |
|---|---|---|
| **Definition** | Codified, transferable, documented | Personal, experiential, hard to articulate |
| **Transfer** | Easy — manuals, databases, courses | Difficult — apprenticeship, practice |
| **Storage** | Documents, ERP systems | Human minds |
| **Example** | Assembly manual for a computer | A mechanic diagnosing engine fault by sound |

> *(Polanyi, 1966 — "The Tacit Dimension")*

> 💡 A DSS scales **explicit knowledge** (rules, models, data). Tacit knowledge — the expert's intuition — is the human's irreplaceable contribution. DSS **augments** the expert; it does not replace them.

---

# 3. What Exactly is a "Decision"?

A true decision requires **three fundamental elements**:

1. **Alternatives (The Crossroads)**
   There must be at least two available and feasible courses of action.
   *"I had no choice" is not a decision — it is a constraint.*

2. **Cognitive Process**
   Involves thinking, gathering data, evaluating criteria, and comparing trade-offs.

3. **Human Accountability**
   Decisions are made by humans who bear responsibility for their consequences.
   DSS are **supporting tools**, not decision-makers.

> ⚠️ A decision requires aligning stakeholders and evaluating the **"domino effect"** — how today's choice reshapes tomorrow's options.

---

<!-- _class: small -->
# 4. The 6 Steps of Rational Decision Making

Rationality means systematically removing bias and emotion:

| Step | Action | Key Question |
|---|---|---|
| 1 | **Define the Problem** (or Opportunity) | What exactly needs to be decided? |
| 2 | **Determine the Criteria** | What are our constraints and goals? |
| 3 | **Assign Weights to Criteria** | Which criterion matters most? |
| 4 | **Generate Alternatives** | What are all feasible options? |
| 5 | **Evaluate Alternatives** | How does each option score per criterion? |
| 6 | **Select the Optimal Decision** | Which option maximises expected value? |

> 💡 Steps 3–6 can be modelled mathematically using **Multi-Criteria Decision Analysis (MCDA)** — a core technique in DSS.

---

# 5. A Good Decision vs. A Good Outcome

> *"A decision can be brilliant and still fail. It can be foolish and still succeed. Luck is not skill."*

**The Casino Example:**
Imagine selling your house, betting everything on "Red" at the roulette table — and winning.

| | |
|---|---|
| **The Outcome** | ✅ Excellent — doubled your money |
| **The Decision** | ❌ Terrible — exposed everything to a ~47% chance |

**Why the distinction matters:**
- Judging decisions by outcomes alone rewards **reckless behaviour** that happened to work.
- A rational decision is judged by **information quality + risk assessment at the time**, not by luck.
- DSS audit the **reasoning** behind decisions, not just their results.

---

# 6. Types of Decisions (By Structure)

| Type | Characteristics | Can be Automated? | Example |
|---|---|---|---|
| **Structured** | Routine, repetitive, clear rules | ✅ Fully | Payroll calculation, VAT invoicing |
| **Semi-structured** | Part algorithm, part human judgment | ⚠️ Partially | Bank loan approval, inventory reorder |
| **Unstructured** | Complex, rare, high uncertainty | ❌ Not yet | Acquiring a rival company, crisis response |

> 🎯 **DSS targets semi-structured decisions** — where data models can narrow the options but human judgment is still essential for the final call.

A conventional MIS handles structured problems well. The value of a DSS is precisely in the **grey area** of semi-structured complexity.

---

<!-- _class: small -->
# 7. Decisions by Degree of Certainty

How much do we know about the future?

| Condition | What we know | DSS Strategy | Example |
|---|---|---|---|
| 🟢 **Certainty** | 100% outcome of each choice | Mathematical Optimisation | Linear programming for logistics |
| 🟡 **Risk** | Possible outcomes **and** their probabilities | Predictive Analytics / ML | Credit scoring model |
| 🔴 **Uncertainty** | Possible outcomes, but **not** probabilities | What-If Scenarios & Heuristics | Entering a new uncharted market |

> Most real business decisions live in the **Risk** or **Uncertainty** zone — precisely why DSS are valuable.
> Moving a decision from *Uncertainty* → *Risk* → *Certainty* (by gathering better data) is one of the **primary goals of a DSS**.

---

# 8. Dependent vs. Independent Decisions

| Type | Scope | Impact | Example |
|---|---|---|---|
| **Independent** | Single department | Limited | Ordering office supplies |
| **Dependent** | Cross-departmental | High — Butterfly Effect | Pricing, product launches |

**The Uncoordinated Flash Sale:**
Marketing launches a 50% discount — without telling anyone.
- 🏭 Logistics runs out of stock
- 💻 IT servers crash
- 💰 Finance margin collapses
- 😤 Customers get failed orders

> Dependent decisions require a **shared information platform** — exactly what a DSS provides.

---

<!-- _class: small -->
# 9. MIS vs. DSS — What's the Difference?

| Dimension | MIS | DSS |
|---|---|---|
| **Primary focus** | Efficiency — *doing things right* | Effectiveness — *doing the right things* |
| **Time orientation** | Reports on the **past** | Guides the **future** |
| **Problem type** | Structured, routine | Semi/unstructured, complex |
| **Output** | Standardised reports & dashboards | Models, scenarios, recommendations |
| **User** | Operational managers | Strategic & middle management |
| **Interaction** | Passive — pull a report | Active — run a what-if experiment |

> ℹ️ MIS and DSS are **complementary**, not competing. An MIS feeds data into the DSS. The DSS turns that data into decisions.

---

# 10. Herbert Simon's Decision Model

**Bounded Rationality** — we cannot process infinite variables due to time and cognitive limits. *(Nobel Prize in Economics, 1978)*

Instead of optimising, humans practise **Satisficing**: finding a "good enough" solution given available resources.

| Stage | Activity | DSS Role |
|---|---|---|
| 🔍 **Intelligence** | Identify problem; gather & clean data | Dashboards, data warehouse |
| 🔧 **Design** | Build alternative models & scenarios | Statistical models, simulations |
| ✅ **Choice** | Select best alternative; sensitivity analysis | Tornado charts, what-if tools |
| 🚀 **Implementation** | Apply solution; monitor & learn | KPI tracking, feedback loops |

> 💡 The lab follows Simon's model step-by-step on real hotel booking data.

---

<!-- _class: small -->
# 11. Architecture of a DSS: The 3 Pillars

```
┌──────────────────────────────────────────────────────┐
│                   USER INTERFACE                     │
│          Dashboards · NLP · Reports · Alerts         │
└───────────────────────┬──────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
┌───────────────────┐       ┌───────────────────────┐
│  DATA MANAGEMENT  │       │  MODEL MANAGEMENT     │
│  (The Memory)     │       │  (The Brain)          │
│                   │       │                       │
│ • Internal (ERP)  │       │ • Statistical models  │
│ • External market │       │ • Financial models    │
│ • Personal data   │       │ • Optimisation (LP)   │
│ • Data Warehouse  │       │ • Monte Carlo sims    │
│ • Data Marts      │       │ • ML models           │
└───────────────────┘       └───────────────────────┘
```

> The **User Interface** is the most underrated pillar — even a perfect model fails if the decision-maker cannot understand or interact with it.

---

<!-- _class: small -->
# 12. The Power of DSS: Dynamic Analysis

A DSS does not deliver static reports — it enables **active experimentation** in a risk-free environment:

| Technique | Question it answers | Example |
|---|---|---|
| **What-If Analysis** | What happens if inputs change? | "What if raw material costs rise 15%?" |
| **Sensitivity Analysis** | Which variable has the biggest impact? | Tornado chart showing top cancellation drivers |
| **Goal Seek** | What input is needed to hit a target? | "What lead-time cap gives us ≤20% cancellations?" |
| **Scenario Planning** | How do outcomes differ across futures? | Optimistic / base / pessimistic demand forecasts |
| **Data Visualisation** | How do we communicate complex patterns? | Heatmaps, time-series, Tornado charts |

> 🧠 The human brain processes **visual patterns** up to 60,000× faster than raw numbers. Visualisation is not decoration — it is a cognitive tool.

---

# 13. Connecting Theory to Practice

Case study: **119,390 hotel bookings** (Portugal, 2015–2017)

| Simon's Stage | Lab activity |
|---|---|
| 🔍 **Intelligence** | Load & clean `hotel_bookings.csv` with pandas |
| 🔧 **Design** | Correlation, OHE, segmentation, seasonality |
| ✅ **Choice** | Tornado chart, What-if, Goal Seek — rank policies |
| 🚀 **Implementation** | 6 concrete cancellation-reduction policies |

> *"Which factors most strongly predict a cancellation — and what deposit/pricing policies should the hotel adopt?"*

📓 `lab1_greek.ipynb` · `lab1_english.ipynb`

---

# Summary — Key Takeaways (1/2)

| # | Concept | One-line reminder |
|---|---|---|
| 1 | DIKW Pyramid | Data → Information → Knowledge → Wisdom |
| 2 | Tacit Knowledge | DSS amplifies experts; it cannot replace intuition |
| 3 | Decision definition | Alternatives + Cognition + Human accountability |
| 4 | Rational process | 6 steps from problem definition to optimal choice |
| 5 | Decision vs. Outcome | Good luck ≠ good reasoning |
| 6 | Decision structure | DSS targets the semi-structured middle ground |

---

# Summary — Key Takeaways (2/2)

| # | Concept | One-line reminder |
|---|---|---|
| 7 | Certainty spectrum | Data reduces uncertainty; DSS moves decisions left |
| 8 | Butterfly Effect | Dependent decisions demand shared information |
| 9 | MIS vs. DSS | Past efficiency vs. future effectiveness |
| 10 | Simon's model | Intelligence → Design → Choice → Implementation |
| 11 | DSS architecture | Memory + Brain + Bridge |
| 12 | Dynamic analysis | What-if · Sensitivity · Goal Seek · Visualisation |

---

<!-- _class: small -->
# References

- Simon, H.A. (1960). *The New Science of Management Decision.* Harper & Row.
- Simon, H.A. (1978). Nobel Memorial Prize Lecture: *Rational Decision-Making in Business Organizations.*
- Polanyi, M. (1966). *The Tacit Dimension.* Routledge.
- Sprague, R.H. & Carlson, E.D. (1982). *Building Effective Decision Support Systems.* Prentice-Hall.
- Turban, E., Aronson, J.E. & Liang, T.P. (2007). *Decision Support Systems and Intelligent Systems* (8th ed.). Pearson.
- Antonio, N., de Almeida, A. & Nunes, L. (2019). *Hotel booking demand datasets.* Data in Brief, 22, 41–49.