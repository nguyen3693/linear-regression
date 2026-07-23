# Assignment 3: AI-Assisted Linear Regression

## Project Description

This folder contains the **AI-assisted** portion of Assignment 3. It uses Python and R to fit a simple linear regression model that predicts **Salary** from **YearsExperience**, prints diagnostic statistics (including mean squared error), and saves an annotated scatter plot with a regression line overlay.

The workflow is:

1. Read `regression_data.csv`
2. Fit a linear model
3. Print statistics
4. Create and save an annotated plot

---

## Contents

```
ai/
├── README_AI.md                      # this file
├── CODE_REVIEW.md                    # comparison of manual/ vs ai/
├── linear_model_python.ipynb         # Python Jupyter notebook
├── linear_model_python.html          # exported HTML
├── linear_model_python.py            # executable Python script
├── linear_model_python_output.png    # saved plot (Python)
├── linear_model_r.ipynb              # R Jupyter notebook
├── linear_model_r.html               # exported HTML
├── linear_model_r.r                  # executable R script
└── linear_model_r_output.png         # saved plot (R)
```

---

## Dataset

File: `../regression_data.csv` (one folder up from `ai/`)

| Column | Meaning |
|--------|---------|
| `YearsExperience` | Years of work experience (X) |
| `Salary` | Salary amount (Y) |

---

## Environment

Use the conda environment **`7030_class_1`** from the project root:

```bash
conda activate 7030_class_1
```

**Python packages used:** pandas, matplotlib, numpy, scikit-learn, scipy

**R packages used:** base R graphics and stats (the R notebook uses `plot()`, `abline()`, and `lm()` — not ggplot2)

---

## Getting Started

### 1. Clone and enter the project

```bash
git clone https://github.com/nguyen3693/linear-regression.git
cd linear-regression
```

### 2. Activate the environment

```bash
conda activate 7030_class_1
```

### 3. Open Jupyter Lab

```bash
jupyter lab
```

Open the notebooks in the `ai/` folder:

- `linear_model_python.ipynb` (Python kernel: `7030_class_1`)
- `linear_model_r.ipynb` (R kernel: `ir_7030_class_1`)

---

## Run from Terminal

Navigate into the `ai/` folder first so output `.png` files save there:

```bash
cd ai
```

Both scripts take exactly **3 arguments**:

```bash
<filename> <x_column> <y_column>
```

### Python

```bash
python linear_model_python.py ../regression_data.csv YearsExperience Salary
```

### R

```bash
Rscript linear_model_r.r ../regression_data.csv YearsExperience Salary
```

---

## What the analysis does

### Model

Simple linear regression:

```text
Salary = intercept + slope × YearsExperience
```

### Statistics printed

Both Python and R print:

- Slope and intercept
- Regression equation
- R-squared
- p-value
- Standard error
- **Mean Squared Error (MSE)**
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

R also prints **Adjusted R-squared**.

### Example output (Python)

```text
Slope: 8285.29
Intercept: 29203.52
Equation: Salary = 29203.52 + 8285.29 * YearsExperience
R-squared: 0.7852
Mean Squared Error (MSE): 17523844.08
Saved plot: linear_model_python_output.png
```

---

## Plots

Each notebook and script creates a scatter plot with:

- Red data points
- Blue regression line
- On-plot annotation showing equation, R², and MSE

**Output files:**

| Language | PNG file |
|----------|----------|
| Python | `linear_model_python_output.png` |
| R | `linear_model_r_output.png` |

---

## HTML exports

Static HTML versions of the notebooks are included for viewing without Jupyter:

- `linear_model_python.html`
- `linear_model_r.html`

---

## Related files

- **`../README.md`** — main project README (manual work and overall setup)
- **`CODE_REVIEW.md`** — side-by-side review of `manual/` vs `ai/`

---

## Author

Trang Nguyen  
Data Science for Biomedical Sciences — Assignment 3 (AI-assisted)
