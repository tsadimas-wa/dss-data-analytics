---
marp: true
theme: default
paginate: true
header: 'Unit 2: Decision Problem Modelling'
footer: 'University of West Attica (UNIWA) — Intelligent Systems & DSS'
style: |
  section {
    font-size: 22px;
  }
  section.small {
    font-size: 18px;
  }
  /* Slide with diagram only — large image max-height */
  section.diagram img {
    max-height: 500px !important;
    max-width: 94% !important;
    display: block;
    margin: 0 auto;
  }
  /* Slide with diagram + text */
  section.diagram-sm img {
    max-height: 320px !important;
    max-width: 94% !important;
    display: block;
    margin: 0 auto;
  }
---

<div style="text-align:center; margin-bottom:16px;">

![w:280](../img/shared/uniwa_logo.png)

</div>

# Intelligent Systems and Decision Support Systems
**Unit 2: Decision Problem Modelling**
Department of Informatics & Computer Engineering
University of West Attica

**Instructor:** Anargyros Tsadimas (tsadimas@uniwa.gr)

---

<!-- _class: small -->
# Unit 2 — Outline

1. What is a Model?
2. Basic Model Management Concepts
3. Categories of Models
4. Why Use Models in DSS?
5. Classification of Models
6. Desired vs. Feasible Solutions
7. Mathematical Model Categories
8. Types of Analytical Models
9. Development Phases of a Mathematical Model
10. Components of a Quantitative Model
11. Model Validation
12. Mathematical Programming & Linear Programming (LP)
13. LP Example: Furniture Manufacturing
14. Non-Linear Programming (NLP)
15. Sensitivity Analysis
16. What-If Analysis & Goal Seek
17. Comparison: What-If vs. Goal Seek vs. Sensitivity Analysis

---

# What is a Model?

> *"A model is a simplified, abstract representation of reality that captures the essential features of a system or problem."*

**Why simplify?**
* Reality is too complex to be analysed in its entirety.
* A model focuses only on the variables that **matter for the decision**.
* It allows safe experimentation — no real-world cost or risk.

**The utility of a model:**
* Describe and understand a system (Descriptive).
* Predict future states (Predictive).
* Identify the optimal course of action (Prescriptive / Normative).

---

<!-- _class: small -->
# Basic Model Management Concepts

| Concept | Definition |
|---|---|
| **Model** | Abstract representation of a problem or system |
| **Problem** | Situation requiring a decision — gap between current and desired state |
| **Solver** | Algorithm or method that finds a solution (e.g. Simplex, Gradient Descent) |
| **Model Base** | Repository of all available models in a DSS |
| **Modelling Language** | Formal language for defining models (e.g. AMPL, GAMS, MathProg) |
| **Model Directory** | Catalogue describing available models and their use |
| **Model Execution** | Running the solver on a specific instance of the model |

> The **Model Base** in a DSS is analogous to the **Database** for data. It stores, organises and retrieves analytical models on demand.

---

# Categories of Models

**1. Descriptive Models:** *What is the current state?*
* Describe the behaviour of a system without prescribing action.
* *Examples:* Statistical summaries, simulation, regression (as a description tool).

**2. Predictive Models:** *What will happen?*
* Forecast future values based on historical patterns.
* *Examples:* Regression, Time-series forecasting, Machine Learning classifiers.

**3. Normative / Prescriptive Models:** *What should we do?*
* Identify the optimal decision given objectives and constraints.
* *Examples:* Linear Programming, Integer Programming, Goal Programming.

> In a DSS, all three categories coexist: we *describe* the situation, *predict* future states, and *prescribe* the best action.

---

# Why Use Models in DSS?

Models are the analytical engine of a DSS. Their advantages:

* **Abstraction:** Strip away irrelevant complexity; keep only the variables that drive the decision.
* **Speed:** Evaluate thousands of scenarios in seconds (impossible manually).
* **Risk-free experimentation:** Test policies before committing real resources.
* **Repeatability:** The same model applied consistently — no cognitive bias per run.
* **Communication:** A shared model aligns stakeholders on assumptions and trade-offs.

> *"All models are wrong, but some are useful."* — George Box

The goal is not a perfect replica of reality, but a **useful approximation** that supports better decisions.

---

<!-- _class: small -->
# Classification of Models (I): By Representation

| Type | Description | Example |
|---|---|---|
| **Iconic** | Physical replica, scaled up or down | Scale model of a building, flight simulator |
| **Analogue** | Uses one set of properties to represent another | Map (distance → colour), thermometer |
| **Symbolic / Mathematical** | Uses symbols and equations | LP formulation, regression equation |

> DSS models are almost exclusively **symbolic** — they live in code and mathematics, not physical form.

**By Determinism:**

| Type | Description |
|---|---|
| **Deterministic** | All inputs are known with certainty; one output per input set |
| **Stochastic** | Inputs have probability distributions; outputs are distributions |

**By Time:**

| Type | Description |
|---|---|
| **Static** | A snapshot — no time dimension (e.g. LP optimisation) |
| **Dynamic** | Evolves over time; models sequences of decisions (e.g. simulation) |

---

# Desired vs. Feasible Solutions

In optimisation models, we must distinguish between:

**Feasible Solution:**
* Satisfies *all* constraints of the problem.
* The **feasible region** is the set of all feasible solutions.
* A problem with no feasible solutions is **infeasible**.

**Desired / Optimal Solution:**
* The feasible solution that maximises (or minimises) the objective function.
* May be unique, multiple (degenerate), or non-existent (unbounded).

> The solver's job: search the feasible region and find the point of optimal objective value.

---

<!-- _class: small -->
# Bell et al. (1985) — Model Classification Framework

Bell, Keeney & Raiffa (1985) propose a classification based on **purpose and structure**:

| Class | Purpose | Method |
|---|---|---|
| **Optimisation** | Find the best feasible solution | LP, IP, NLP, DP |
| **Simulation** | Imitate system behaviour over time | Monte Carlo, Agent-based |
| **Heuristics** | Find good (not guaranteed optimal) solutions quickly | Genetic Algorithms, Tabu Search |
| **Decision Analysis** | Evaluate alternatives under uncertainty | Decision Trees, Expected Utility |
| **Statistical / Econometric** | Estimate relationships from data | Regression, ANOVA, Time Series |

> This taxonomy is still widely referenced in DSS literature as a foundation for **Model Base design**.

---

<!-- _class: small -->
# Mathematical Model Categories (Mitra, 1988)

Mitra (1988) organises quantitative DSS models into three major families:

**1. Mathematical Programming**
* Optimise an objective function subject to constraints.
* Sub-types: Linear (LP), Integer (IP), Mixed-Integer (MIP), Non-Linear (NLP), Dynamic (DP).

**2. Simulation**
* Imitate the probabilistic behaviour of a real system.
* Sub-types: Discrete-Event, Continuous, Monte Carlo.
* Useful when a closed-form analytical solution is not available.

**3. Decision Analysis**
* Structure decisions involving uncertainty and multiple objectives.
* Tools: Decision Trees, Influence Diagrams, Multi-Criteria Decision Analysis (MCDA).

> **Davis (1988)** extends this taxonomy further with statistical/forecasting models as a fourth family.

---

<!-- _class: small -->
# Types of Analytical Models

**Prescriptive (Normative) Models — Optimisation**
* Define an objective (maximise profit / minimise cost) and find the best solution.
* Require well-defined constraints.
* *Typical solvers:* Simplex, Interior Point, Branch & Bound.

**Predictive Models — Forecasting**
* Use historical data to estimate future values.
* *Examples:* Multiple Regression, ARIMA, Neural Networks, Random Forests.
* Output: probability or point estimate of a future state.

**Descriptive Models — Simulation**
* Imitate system behaviour; answer "what would happen if...".
* *Examples:* Monte Carlo simulation, System Dynamics, Discrete-Event Simulation.
* No single optimal answer — produce a distribution of outcomes.

---

<!-- _class: small -->
# Example: GPS Navigation as a Model

A GPS navigator illustrates all three model types working together:

| Model Type | GPS Function |
|---|---|
| **Descriptive** | Road network graph — represents current traffic state |
| **Predictive** | Estimates arrival time based on speed and historical traffic patterns |
| **Prescriptive** | Optimises the route — minimises travel time subject to road constraints |

**Key insight:**
* The GPS map is *not* reality — it is a **symbolic model** of reality.
* It omits irrelevant detail (building colours, weather) and retains only decision-relevant structure (nodes, edges, weights).
* This is exactly how DSS models work: **purposeful simplification**.

---

<!-- _class: small -->
# Development Phases of a Mathematical Model

Building a sound quantitative model follows a structured lifecycle:

| Phase | Activity |
|---|---|
| **1. Problem Formulation** | Define the decision variables, objective, and constraints in words |
| **2. Mathematical Formulation** | Translate into formal notation (equations, inequalities) |
| **3. Data Collection** | Gather the parameter values needed by the model |
| **4. Solution** | Apply the appropriate solver algorithm |
| **5. Validation** | Check that model outputs match known reality (back-testing) |
| **6. Sensitivity Analysis** | Examine how the solution changes with parameter variation |
| **7. Implementation** | Embed the model in the DSS; communicate results to decision-makers |

> Phase 6 (Sensitivity Analysis) is not an afterthought — it is an essential step for building trust in the model's recommendations.

---

<!-- _class: small -->
# Components of a Quantitative Model

Every mathematical model for decision-making consists of:

**Decision Variables (Controllable):**
* Quantities the decision-maker can set or change.
* *Example:* How many units of each product to manufacture?

**Objective Function:**
* The criterion to optimise (maximise or minimise).
* *Example:* Maximise total profit.

**Constraints:**
* Limits imposed by resources, regulations, or logic.
* *Example:* Available machine hours, budget cap, non-negativity.

**Parameters / Uncontrollable Variables:**
* Data given exogenously — the decision-maker cannot change them.
* *Example:* Market prices, material costs, demand forecasts.

> The art of modelling lies in identifying *which* variables are controllable and *which* constraints are truly binding.

---

<!-- _class: small -->
# Example: EOQ — Economic Order Quantity

**Problem:** A retailer orders stock periodically. How much should they order each time to minimise total annual cost?

**Decision Variable:** Q = order quantity (units per order)

**Objective Function (minimise total annual cost):**

$$TC(Q) = \frac{D}{Q} \cdot S + \frac{Q}{2} \cdot H$$

Where:
* D = Annual demand (units) — *uncontrollable*
* S = Fixed ordering cost per order (€) — *parameter*
* H = Annual holding cost per unit (€) — *parameter*

**Optimal Solution (EOQ formula):**

$$Q^* = \sqrt{\frac{2DS}{H}}$$

**Lesson:** Even a simple, elegant model requires careful identification of decision variables, parameters, and the objective.

---

# Model Validation

A model that is mathematically correct but behaviourally wrong is **dangerous** — it produces confident wrong answers.

**Validation Methods:**

* **Face Validity:** Do domain experts agree the model structure is plausible?
* **Back-Testing (Historical Validation):** Does the model reproduce known past outcomes?
* **Sensitivity Validation:** Do outputs react to inputs in the expected direction and magnitude?
* **Extreme Condition Testing:** Does the model behave sensibly at boundary values (e.g. demand = 0)?

> *Verification* asks "did we build the model right?" (no bugs).
> *Validation* asks "did we build the right model?" (correct structure).

Both are essential before a model is deployed in a decision support context.

---

<!-- _class: small -->
# Examples: Decision Variables by Domain

| Domain | Decision Variables (Controllable) | Result Variable | Uncontrollable Variables |
|---|---|---|---|
| **Manufacturing** | Production quantities per product | Total profit | Raw material prices, demand |
| **Finance** | Investment allocation per asset | Portfolio return | Market returns, interest rates |
| **Logistics** | Order quantity, reorder point | Total inventory cost | Lead time, demand variability |
| **Marketing** | Advertising budget per channel | Sales revenue | Competitor actions, seasonality |
| **Healthcare** | Drug dosage, treatment schedule | Patient outcome | Patient genetics, disease severity |

> The distinction between *controllable* and *uncontrollable* variables is the **first and most important** modelling decision.

---

<!-- _class: small -->
# Mathematical Programming & Optimisation

**Mathematical Programming** is the family of techniques that find the optimal value of an objective function subject to constraints.


> Optimise f(x)
> Subject to: g_i(x) ≤ b_i for all i
> and: x ≥ 0

Where:
* **f(x)** = objective function (profit, cost, time, …)
* **x** = vector of decision variables
* **g_i(x) ≤ b_i** = resource/logical constraints

**Sub-families:**

| Type | Linearity | Variable Type |
|---|---|---|
| **LP** | Linear | Continuous |
| **IP / MIP** | Linear | Integer / Mixed |
| **NLP** | Non-linear | Continuous |
| **DP** | Any | Stage-based |

---

<!-- _class: small -->
# Linear Programming (LP) Models

**Conditions for LP:**
1. **Proportionality:** The contribution of each variable to the objective and constraints is proportional to its value.
2. **Additivity:** The total objective is the sum of individual contributions.
3. **Divisibility:** Decision variables can take fractional values.
4. **Certainty:** All coefficients are known with certainty.

**Standard form:**

> Maximise (or Minimise): c₁x₁ + c₂x₂ + … + cₙxₙ
> Subject to:
> a₁₁x₁ + a₁₂x₂ + … ≤ b₁
> …
> x₁, x₂, … ≥ 0

**Solution methods:** Graphical (2 variables), Simplex algorithm (general), Interior Point methods (large-scale).

---

<!-- _class: small -->
# LP Example: Furniture Manufacturing (1/3)

**Problem (EPIPLOTECHNIKI Co.):**
A furniture manufacturer produces **Tables** and **Chairs**.

| Resource | Table (per unit) | Chair (per unit) | Available |
|---|---|---|---|
| **Wood (m²)** | 5 | 2 | 240 |
| **Labour (hours)** | 4 | 3 | 210 |
| **Paint (litres)** | 1 | 2 | 100 |

**Profit:** Table = 70€, Chair = 50€

**Formulation:**
* Decision Variables: x₁ = Tables produced, x₂ = Chairs produced
* Objective: **Maximise** Z = 70x₁ + 50x₂
* Constraints:
  * 5x₁ + 2x₂ ≤ 240 (Wood)
  * 4x₁ + 3x₂ ≤ 210 (Labour)
  * x₁ + 2x₂ ≤ 100 (Paint)
  * x₁, x₂ ≥ 0

---

# LP Example: Furniture Manufacturing (2/3)

**Graphical Solution:**

The feasible region is the intersection of all constraints (the polygon satisfying all inequalities simultaneously).

**Corner-point method:** The optimal solution of an LP always lies at a **vertex (corner point)** of the feasible region.

Evaluating the objective function at each corner:

| Vertex (x₁, x₂) | Z = 70x₁ + 50x₂ |
|---|---|
| (0, 0) | 0 |
| (48, 0) | 3,360 |
| **(30, 30)** | **3,600** ✅ |
| (0, 50) | 2,500 |

**Optimal solution:** Produce **30 Tables** and **30 Chairs** → Profit = **3,600€**

---

<!-- _class: small -->
# LP Example: Furniture Manufacturing (3/3)

**Interpretation and Binding Constraints:**

At the optimal point (30, 30):
* **Wood:** 5(30) + 2(30) = 210 ≤ 240 → **slack = 30 m²** (not fully used)
* **Labour:** 4(30) + 3(30) = 210 = 210 → **binding** (fully consumed)
* **Paint:** 30 + 2(30) = 90 ≤ 100 → **slack = 10 litres** (not fully used)

**Binding constraint = the bottleneck.** Labour is the limiting resource.

**Managerial insight:**
* Adding more wood or paint will *not* improve profit — those resources are already in surplus.
* To increase profit beyond 3,600€, the manager must acquire **more labour hours**.

> This is exactly the kind of insight that Sensitivity Analysis and Shadow Prices quantify.

---

# Non-Linear Programming (NLP)

When the objective function or constraints are **non-linear**, we use NLP.

**When does non-linearity arise?**
* Economies of scale (cost per unit decreases with volume).
* Diminishing returns (advertising spend vs. sales lift).
* Risk-return trade-offs (portfolio variance is quadratic).

**Example — Advertising ROI:**
> Maximise: Revenue(x) = 200√x − x
> Subject to: x ≤ 50,000 (budget cap), x ≥ 0

Where x = advertising spend (€).

**Challenges:**
* Multiple local optima — the solver may find a local, not global, maximum.
* Requires specialised algorithms: Gradient Descent, Sequential Quadratic Programming (SQP).
* Solution is not guaranteed to be at a corner point.

---

# Sensitivity Analysis

**Definition:**
Sensitivity Analysis examines *how much* the optimal solution changes when **model parameters** vary — while holding all other parameters fixed.

**Key questions it answers:**
* By how much can a cost/profit coefficient change before the optimal *basis* changes?
* What is the **shadow price** (dual value) of each constraint — the marginal value of relaxing it by one unit?
* What are the **right-hand side ranges** within which the current basis remains optimal?

**Outputs from an LP solver:**
* **Ranging report:** Allowable increase/decrease for each objective coefficient and RHS.
* **Shadow prices:** Change in optimal Z per unit increase in constraint b_i.

> Sensitivity Analysis transforms a single-point answer into a **robust decision**: the manager knows *when* the recommendation changes — not just *what* it is.

---

# Sensitivity Analysis — Tornado Chart

The **Tornado Chart** is the most common visualisation for sensitivity results in a DSS:

* Each bar represents one input parameter.
* Bar **length** = range of output variation caused by that parameter.
* Parameters are sorted by impact — most influential at the top (wide end of the "tornado").

**Reading a Tornado Chart:**
* The **longest bars** identify the critical assumptions.
* Focus further data collection and risk management on these variables.
* Short bars = parameters where uncertainty has negligible impact on the decision.

> In the hotel cancellations lab: the Tornado Chart revealed that **lead time** and **deposit type** were the dominant cancellation drivers — outweighing seasonality and room type.

---

<!-- _class: small -->
# What-If Analysis

**Definition:**
What-If Analysis (also called scenario analysis or parametric analysis) evaluates how the **output** of a model changes when one or more **input values** are varied manually by the decision-maker.

**Procedure:**
1. Fix a baseline scenario (current best estimates).
2. Change one input at a time (or a combination).
3. Record and compare outputs across scenarios.

**Example:**
> *"What happens to annual profit if raw material costs rise by 15%?"*
> *"What if we increase the sales force by 10 people?"*

**Tools:** Excel Data Tables, Python simulations, Power BI what-if slicers.

> What-If is *exploratory* — the analyst drives it. Sensitivity Analysis is *systematic* — it covers the full parameter space automatically.

---

<!-- _class: small -->
# Goal Seek

**Definition:**
Goal Seek is the **inverse** of What-If Analysis. Instead of asking *"what output results from this input?"*, it asks:

> *"What input value is required to achieve a specific target output?"*

**Procedure:**
1. Set a target value for the output (e.g. profit = 500,000€).
2. Select the input variable to adjust (e.g. selling price).
3. The solver finds the input value that achieves the target.

**Practical examples:**

| Goal | Input to find |
|---|---|
| Reduce cancellation rate to ≤ 20% | Maximum lead time to accept |
| Break even (profit = 0) | Minimum units to sell |
| Achieve 15% ROI | Minimum project revenue required |

**Tools:** Excel Goal Seek, Python `scipy.optimize.brentq`, Solver add-in.

---

<!-- _class: small -->
# Comparison: What-If vs. Goal Seek vs. Sensitivity Analysis

| Feature | What-If Analysis | Goal Seek | Sensitivity Analysis |
|---|---|---|---|
| **Question** | *Output if input = X?* | *Input needed to get output = Y?* | *How sensitive is Z to each parameter?* |
| **Direction** | Input → Output | Output → Input | Systematic (all parameters) |
| **User control** | Manual, exploratory | Target-driven | Automated by solver |
| **Scope** | One scenario at a time | One target, one variable | Full parameter ranges |
| **Output** | Single scenario result | Single input value | Ranging report, shadow prices |
| **Best for** | Exploring alternatives | Setting targets & benchmarks | Identifying critical assumptions |
| **Typical tool** | Excel Data Table, Python | Excel Goal Seek, Solver | LP Solver ranging, Tornado Chart |

> In a well-designed DSS, all three techniques are available and complementary. The analyst uses them in sequence: **What-If** to explore, **Sensitivity** to identify critical parameters, and **Goal Seek** to set actionable targets.

---

<!-- _class: small -->
# Summary — Key Takeaways

| # | Concept | One-line reminder |
|---|---|---|
| 1 | Model definition | Purposeful simplification of reality for decision support |
| 2 | Model types | Descriptive · Predictive · Prescriptive |
| 3 | Representation | Iconic → Analogue → Symbolic (DSS uses symbolic) |
| 4 | Determinism | Deterministic (certain) vs. Stochastic (probabilistic) |
| 5 | LP conditions | Proportionality, Additivity, Divisibility, Certainty |
| 6 | LP solution | Optimal always at a corner point of the feasible region |
| 7 | NLP challenge | Multiple local optima — no corner-point guarantee |
| 8 | Binding constraint | The bottleneck — where investment yields marginal return |
| 9 | Shadow price | Marginal value of relaxing a constraint by one unit |
| 10 | Tornado chart | Ranks parameters by impact on output — reveals critical assumptions |
| 11 | What-If vs. Goal Seek | Forward (explore outputs) vs. Backward (target inputs) |

---

# References

- Bell, D.E., Keeney, R.L. & Raiffa, H. (1985). *Conflicting Objectives in Decisions.* Wiley.
- Davis, G.B. (1988). *Management Information Systems.* McGraw-Hill.
- Mitra, G. (1988). *Mathematical Models for Decision Support.* Springer.
- Simon, H.A. (1960). *The New Science of Management Decision.* Harper & Row.
- Turban, E., Aronson, J.E. & Liang, T.P. (2007). *Decision Support Systems and Intelligent Systems* (8th ed.). Pearson.
- Dantzig, G.B. (1963). *Linear Programming and Extensions.* Princeton University Press.
- Winston, W.L. (2004). *Operations Research: Applications and Algorithms* (4th ed.). Thomson/Brooks Cole.
