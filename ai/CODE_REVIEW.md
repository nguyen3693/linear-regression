# Code Review: `manual/` vs `ai/` (Assignment 3)

**Branch:** `assignment3`  
**Date:** July 23, 2026  
**Reviewer:** AI-assisted review

---

## Overview

Both folders solve the same problem: read `regression_data.csv`, predict **Salary** from **YearsExperience** using simple linear regression, print statistics (including MSE), and save a scatter plot with a regression line and text annotations.

Each folder contains the same types of files:

| File type | `manual/` | `ai/` |
|-----------|-----------|-------|
| Python notebook | `linear_model_python.ipynb` | `linear_model_python.ipynb` |
| R notebook | `linear_model_r.ipynb` | `linear_model_r.ipynb` |
| HTML exports | `.html` | `.html` |
| CLI scripts | `.py`, `.r` | `.py`, `.r` |
| Plot images | `.png` | `.png` |

---

## Verified results (Python scripts run on same data)

Both Python scripts were run with:

```bash
python linear_model_python.py ../regression_data.csv YearsExperience Salary
```

They produced matching core results:

| Statistic | `manual/` | `ai/` |
|-----------|-----------|-------|
| Slope | 8285.29 | 8285.29 |
| Intercept | 29203.52 | 29203.52 |
| R² | 0.7852 | 0.7852 |
| MSE | 17,523,844.08 | 17,523,844.08 |
| p-value | 0.000641 | 0.000641 |
| Standard error | 1532.33 | 1532.33 |

The `ai/` script also prints RMSE (4186.15) and MAE (3526.26). The underlying regression model is the same in both folders.

---

## Main similarities

### 1. Same data and goal
- Both read `../regression_data.csv`
- Both use **YearsExperience** as X and **Salary** as Y
- Both fit a simple linear regression (one predictor)

### 2. Same visual design
- Red data points
- Blue regression line
- Text on the plot showing equation, R², and MSE

### 3. Same project structure
- Notebooks for step-by-step work
- HTML exports for viewing/sharing
- Scripts intended to run from the terminal with 3 arguments: `<filename> <x_column> <y_column>`

### 4. Same diagnostic topics
Both cover slope, intercept, R², p-value, standard error, and MSE — the Assignment 3 diagnostics requested.

---

## Main differences

### 1. How the code was written

| | `manual/` | `ai/` |
|---|-----------|-------|
| **Authoring** | Written by hand with teaching notes | AI-assisted, more compact |
| **Comments** | Many inline comments explaining each step | Fewer comments; more finished-script style |
| **Notebook length** | More cells and markdown sections | Fewer numbered steps (1–4) |

The **manual** notebooks read like a learning journal. The **ai** notebooks read like a finished analysis template.

---

### 2. Python: statistics and metrics

**Similar:** Both use `pandas`, `matplotlib`, `sklearn`, and `scipy.stats.linregress`.

**Different:**
- **manual** splits work across more steps (fit model → print stats → plot separately)
- **ai** combines fitting and printing in fewer cells
- **ai** also prints **RMSE** and **MAE**; **manual** does not
- **manual** plot label uses `r = ...`; **ai** uses `R² = ...`

---

### 3. Python: plots and file names

| | `manual/` | `ai/` |
|---|-----------|-------|
| **Output PNG** | `regression_plot_python.png` | `linear_model_python_output.png` |
| **Annotation placement** | Fixed coordinates `(1, max(y) - 5000)` | Relative position in a top-left text box |
| **Extra plot features** | Basic plot | Grid, labeled legend, figure size, `dpi=150`, white annotation box |

---

### 4. Python: CLI scripts

**manual `linear_model_python.py`:**
- Exported from the notebook
- Uses a **hardcoded** CSV path (`../regression_data.csv`)
- Runs the full analysis first; CLI argument check is at the **bottom**
- Does **not** use the 3 terminal arguments for the analysis itself
- Calls `plt.show()`, which can open a window and slow down or pause the script (~35 seconds observed in testing)

**ai `linear_model_python.py`:**
- Standalone script with a `main()` function
- Reads filename and column names from command-line arguments
- Validates that columns exist in the CSV
- Saves the plot without requiring a pop-up window

---

### 5. R: plotting library

| | `manual/` | `ai/` |
|---|-----------|-------|
| **Plotting** | **ggplot2** (`geom_point`, `geom_smooth`) | **Base R** (`plot`, `abline`, `text`) |
| **Why** | ggplot2 is the intended/taught tool | ggplot2 could not be installed in the current conda environment (R version conflict) |

Both still produce a scatter plot, regression line, and annotations, but the code and appearance differ.

---

### 6. R: statistics

**manual:**
- Prints slope, intercept, R², and MSE
- Labels MSE output as `"mean standard error"` in one place (wording is misleading)
- In the `.r` script, MSE uses `mean(pred - y)^2`, which is not the standard MSE formula

**ai:**
- Uses the standard MSE formula: `mean((y_actual - y_pred)^2)`
- Also prints adjusted R², p-value, standard error, RMSE, and MAE

---

### 7. R: plots and file names

| | `manual/` | `ai/` |
|---|-----------|-------|
| **Output PNG** | `regression_plot_r.png` | `linear_model_r_output.png` |
| **Annotation** | ggplot `annotate("text", ...)` with scientific notation for MSE | base R `text()` with MSE as a regular decimal |
| **Title** | `"Linear Fit"` | `"Salary vs YearsExperience"` (built from column names) |

PNG file sizes also differ (manual R plot is much larger due to ggplot2 output).

---

### 8. R: CLI scripts

**manual `linear_model_r.r`:**
- Runs analysis on hardcoded data first
- CLI argument check is at the **end** and arguments are **not used** for the analysis

**ai `linear_model_r.r`:**
- Checks arguments **first**
- Uses dynamic column names from the terminal
- Validates columns before running

---

## Side-by-side summary

| Topic | `manual/` | `ai/` |
|-------|-----------|-------|
| **Purpose** | Learn by writing and explaining each step | Produce a working, reusable analysis |
| **Notebook style** | Long, tutorial-like | Short, numbered workflow |
| **Regression results** | Same (verified for Python) | Same (verified for Python) |
| **MSE on plot** | Yes | Yes |
| **Extra metrics (RMSE, MAE)** | No | Yes |
| **R plotting tool** | ggplot2 | base R |
| **PNG naming** | `regression_plot_*.png` | `linear_model_*_output.png` |
| **CLI scripts use args for full analysis?** | No (check only at end) | Yes |
| **Column name flexibility** | Hardcoded | Flexible via arguments |

---

## Bottom line

**Similarities:** Both folders correctly complete Assignment 3's core task — linear regression on the same dataset, with diagnostics and annotated plots. When tested, the Python scripts produced identical model numbers.

**Differences:** The **manual** folder shows your learning process (more explanation, ggplot2 in R, notebook-style scripts). The **ai** folder is more polished and reusable (more metrics, proper CLI scripts, consistent output file names, base R where ggplot2 was unavailable).

For grading or a portfolio, **manual** demonstrates understanding; **ai** demonstrates a runnable version you can compare against or extend.

---

## Optional follow-ups

1. Update **manual** CLI scripts so all 3 terminal arguments drive the full analysis (like **ai**).
2. Fix **manual** R MSE to use `mean((pred - y)^2)`.
3. Align PNG file names across both folders if you want a perfectly parallel structure.
4. Install a compatible **ggplot2** in conda so **ai** R can match **manual**'s plotting style.
