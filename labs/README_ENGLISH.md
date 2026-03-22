# Lab 1: Decision Support System (DSS) with Python

## Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running in VS Code](#-running-in-vs-code)
- [Data](#-data)
- [Project Structure](#-project-structure)
- [Libraries](#-libraries-used)
- [Statistical Concepts](#-statistical-concepts-covered)
- [Lab Structure](#-lab-structure--content)
- [Troubleshooting](#-troubleshooting)
- [Tips](#-tips)
- [Mathematical Formulas](#-mathematical-formulas-used)
- [Additional Resources](#-additional-resources)

---

## Description

This lab applies Herbert Simon's decision-making model (Intelligence → Design → Choice) for analysing hotel booking cancellations.

**Goal:** Through data analysis, we will identify the factors that lead to cancellations and propose policies to reduce them.

## 🎯 Learning Objectives

After completing this lab, you will be able to:

1. **Load and clean** large datasets with Pandas
2. **Calculate basic statistical measures** (mean, median, std, correlation)
3. **Create visualisations** (histograms, heatmaps, scatter plots)
4. **Apply DSS techniques**:
   - Correlation Analysis (Pearson & Spearman)
   - What-If Analysis (scenario simulations)
   - Sensitivity Analysis (finding critical factors)
   - Goal Seek Analysis (reverse calculation)
5. **Interpret results** and propose business policies
6. **Apply the Simon model** (Intelligence → Design → Choice)

## 🔧 Prerequisites

- **Python 3.10+** (Python 3.14 recommended)
- **VS Code** with the Python extension
- **Git** (optional)

## 📦 Installation

### Step 1: Clone or Download the Project

```bash
# If using Git:
git clone <repository-url>
cd lab1

# Or download the .zip and extract it
```

### Step 2: Create a Virtual Environment

Open a terminal in VS Code (`Ctrl + ~` or `View → Terminal`) and run:

#### For Linux/macOS:
```bash
# Create virtual environment
python3 -m venv lab1venv

# Activate
source lab1venv/bin/activate
```

#### For Windows:
```cmd
# Create virtual environment
python -m venv lab1venv

# Activate
lab1venv\Scripts\activate
```

### Step 3: Install Dependencies

After activating the virtual environment:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Installation time:** ~2–3 minutes (depending on your connection)

## 🚀 Running in VS Code

### Method 1: Jupyter Notebook (Recommended)

1. **Open the Notebook:**
   - Open `lab1_greek.ipynb` in VS Code

2. **Select Kernel:**
   - Click **"Select Kernel"** (top right)
   - Choose **"Python Environments"**
   - Select `lab1venv` (it will appear as `Python 3.x.x ('lab1venv')`)

3. **Run Cells:**
   - Press `Shift + Enter` to run each cell
   - Or click **"Run All"** to run all cells

### Method 2: Python Script (Alternative)

If you want to convert the notebook to a Python script:

```bash
# Install nbconvert (if not available)
pip install nbconvert

# Convert notebook to Python script
jupyter nbconvert --to script lab1_greek.ipynb

# Run
python lab1.py
```

## 📊 Data

The `hotel_bookings.csv` dataset contains historical hotel booking data with:
- **119,390 records** (bookings from 2015–2017)
- **32 features**
- **2 hotels:** City Hotel & Resort Hotel (Portugal)

**Key Features:**
- `is_canceled`: Target variable (0 = not cancelled, 1 = cancelled)
- `lead_time`: Days between booking and arrival
- `adr`: Average Daily Rate (average daily price)
- `deposit_type`: Deposit type (No Deposit, Non Refund, Refundable)
- `previous_cancellations`: Customer's previous cancellations
- `arrival_date_month`: Month of arrival

**Source:** [Hotel Booking Demand Dataset - Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

## 🗂️ Project Structure

```
lab1/
├── lab1_greek.ipynb        # Main Jupyter Notebook
├── hotel_bookings.csv      # Dataset
├── requirements.txt        # Python dependencies
├── README.md              # This file (Greek)
├── README_ENGLISH.md      # This file (English)
└── lab1venv/              # Virtual environment (created by you)
```

## 📚 Libraries Used

- **pandas:** Data manipulation and analysis (DataFrames)
- **numpy:** Numerical computations
- **matplotlib:** Chart creation
- **seaborn:** Statistical visualisation (heatmaps, distributions)
- **jupyter:** Notebook environment
- **scipy:** (Optional) For advanced analysis

## 📊 Statistical Concepts Covered

The lab introduces and applies fundamental statistical concepts:

### Measures of Central Tendency & Dispersion
- **Mean, Median, Mode**
- **Standard Deviation, Variance, Range**
- Using `df.describe()` for descriptive statistics

### Distribution Analysis
- **Histograms:** Visualising distributions
- **Binning/Discretization:** Converting continuous variables into categories with `pd.cut()` and `pd.qcut()`
- **Skewed distributions (Skewness):** Identifying outliers

### Correlation & Variable Relationships
- **Pearson Coefficient (r):** Linear correlation
- **Spearman Coefficient (ρ):** Monotonic correlation
- **Heatmaps:** Visualising the correlation matrix
- **Scatter Plots:** Identifying non-linear relationships

### Time Series & Smoothing
- **Rolling Average:** Smoothing noise in data
- **Seasonality:** Analysing monthly patterns

> ⚠️ **Important:** Correlation ≠ Causation. The fact that two variables are correlated does not mean one *causes* the other.

## 🎯 Lab Structure & Content

## 🐛 Troubleshooting

### Problem: Python virtual environment not found

**Solution:**
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac)
2. Type: `Python: Select Interpreter`
3. Select `lab1venv/bin/python` (or `lab1venv\Scripts\python.exe` on Windows)

### Problem: "Module not found" error

**Solution:**
```bash
# Make sure the venv is activated (you will see (lab1venv) in the terminal)
# Reinstall dependencies:
pip install -r requirements.txt
```

### Problem: Jupyter Kernel won't start

**Solution:**
```bash
# Install ipykernel separately:
pip install ipykernel
python -m ipykernel install --user --name=lab1venv
```

### Problem: Missing hotel_bookings.csv file

**Solution:**
Download the dataset from [here](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) and place it in the `lab1/` folder.

## 💡 Tips

1. **Save frequently:** Press `Ctrl + S` after each change
2. **Clear Output:** If the notebook becomes slow, press `Ctrl + Shift + P` → `Clear All Outputs`
3. **Restart Kernel:** If it freezes, click the "Restart" button next to the kernel selector
4. **Uncomment code:** Some cells have commented-out code (`#`) — uncomment it to see additional analyses
5. **Read the Markdown Cells:** They contain theory and explanations for each analysis
6. **Run Cells in Order:** Start from the first cell and proceed sequentially

## 📐 Mathematical Formulas Used

### Pearson Coefficient
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i-\bar{x})^2} \cdot \sqrt{\sum(y_i-\bar{y})^2}} \quad \in [-1, +1]$$

### Rolling Average
$$\bar{x}_t^{(w)} = \frac{1}{w} \sum_{i=t-w+1}^{t} x_i$$

Where:
- $w$ = window size (number of observations for smoothing)
- $t$ = current time step

### Phase 1️⃣: Intelligence (Understanding the Problem)
- **Load Dataset:** Import `hotel_bookings.csv` (119,390 bookings)
- **Data Inspection:** Check data types, missing values, outliers
- **Data Cleaning:** Handle missing values, remove extreme values
- **Descriptive Statistics:** Calculate means, standard deviations, distributions

### Phase 2️⃣: Design (Analysis & Modelling)

**A. Correlation Analysis**
- Pearson & Spearman correlation matrices
- Heatmap visualisation
- Tornado Chart for ranking influential factors

**B. What-If Analysis**
- Scenario simulation: "What happens if `lead_time` changes?"
- Effect of changes in key variables

**C. Sensitivity Analysis**
- Finding the most "sensitive" factors
- Binning with `pd.cut()` and `pd.qcut()`

**D. Goal Seek Analysis**
- Reverse calculation: "What `lead_time` is needed for 30% cancellations?"

**E. Additional Analyses**
- **Seasonality:** Analysis of monthly trends
- **Market Segments:** Comparing Online vs Offline bookings
- **Customer Loyalty:** Effect of repeat visits
- **ADR (Average Daily Rate) Analysis:** Price-cancellation relationship

### Phase 3️⃣: Choice (Decision Making)
- **Interpreting Results:** Understanding the factors driving cancellations
- **Policy Recommendations:** Proposals to reduce cancellations
  - Deposit policies
  - Lead time management (pre-booking limits)
  - Pricing strategies (dynamic pricing)
  - Customer loyalty programs

## 🤝 Contributing

For suggestions or corrections, contact the instructor.

## Additional Resources

### Library Documentation
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Python & Data Science Learning
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Kaggle Learn](https://www.kaggle.com/learn) - Free courses
- [Real Python Tutorials](https://realpython.com/)

### Decision Support Systems
- Herbert Simon - "The New Science of Management Decision"
- Ralph Sprague & Eric Carlson - "Building Effective Decision Support Systems"

## License

This educational material is intended for academic use.

---

**Happy Analyzing! 📊🎓**
