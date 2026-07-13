# Assignment 2: Notebooks and Scripting

*README.md file was written with help of Cursor*

## What this project does

This project builds a **simple linear regression** model to predict **Salary** from **Years of Experience** using two methods.

1. **Part A (Manual)** — typed everything myself in Jupyter Lab (`manual/`)
2. **Part B (AI-assisted)** — rebuilt the same work with AI help (`ai/`)

**Goals:**

- Explore data in a **notebook**
- Export notebooks to **HTML**
- Turn notebook code into **command-line scripts**

---

## Dataset

File: `regression_data.csv`

| Column | Meaning |
|--------|---------|
| `YearsExperience` | Years of work experience (X) |
| `Salary` | Salary amount (Y) |

---

## Project layout

```text
assignment2/
├── README.md
├── regression_data.csv
├── environment.yml
├── requirements.txt
├── setup_env.sh
├── manual/                                 # Part A — done by hand
│   ├── linear_regression_python.ipynb
│   ├── linear_regression_python.html
│   ├── linear_regression_python.py
│   ├── linear_regression_python_output.png
│   ├── linear_regression_r.ipynb
│   ├── linear_regression_r.html
│   ├── linear_regression_r.r
│   └── linear_regression_r_output.png
└── ai/                                     # Part B — AI-assisted
    ├── PROMPTS.md
    ├── linear_regression_python.ipynb
    ├── linear_regression_python.html
    ├── linear_regression_python.py
    ├── linear_regression_python_output.png
    ├── linear_regression_r.ipynb
    ├── linear_regression_r.html
    ├── linear_regression_r.R
    └── linear_regression_r_output.png
```

---

## What each notebook does

Both notebooks (Python and R), in both `manual/` and `ai/`, follow the same steps:

1. **Read** the CSV file
2. **Plot** a scatter plot of YearsExperience vs Salary
3. **Fit** a linear regression model
4. **Draw** the regression line on the plot
5. **Evaluate** the model (for example, R² and error metrics)
6. **Export** the notebook as HTML

---

## How to set up the environment

### Option 1: Conda (recommended)

```bash
conda env create -f environment.yml
conda activate 7030_class_1
```

Or run:

```bash
bash setup_env.sh
```

### Option 2: Python packages only (pip)

```bash
pip install -r requirements.txt
```

You will still need **R** (and ggplot2) installed for the R notebook and R script.  
If you use the conda environment above, R is already included.

---

## How to open the notebooks

1. Activate your environment:

```bash
conda activate 7030_class_1
```

2. Start Jupyter Lab from the project root:

```bash
cd ~/Projects/assignment2
jupyter lab
```

3. Open a notebook and choose the matching kernel:

| Notebook | Kernel |
|----------|--------|
| `manual/linear_regression_python.ipynb` | Python |
| `manual/linear_regression_r.ipynb` | R |
| `ai/linear_regression_python.ipynb` | Python |
| `ai/linear_regression_r.ipynb` | R |

4. To view the HTML versions, open the `.html` files in a browser (same folders as above).

---

## How to run the command-line scripts

Both scripts take **3 arguments**:

```text
<script> <filename> <x_column> <y_column>
```

Run them from inside the `manual/` or `ai/` folder so the output PNG is saved in that folder.

### Part A — Manual

```bash
conda activate 7030_class_1
cd ~/Projects/assignment2/manual

python linear_regression_python.py ../regression_data.csv YearsExperience Salary
Rscript linear_regression_r.r ../regression_data.csv YearsExperience Salary
```

### Part B — AI-assisted

```bash
conda activate 7030_class_1
cd ~/Projects/assignment2/ai

python linear_regression_python.py ../regression_data.csv YearsExperience Salary
Rscript linear_regression_r.R ../regression_data.csv YearsExperience Salary
```

---

## Output images

| Location | Python plot | R plot |
|----------|-------------|--------|
| Manual | `manual/linear_regression_python_output.png` | `manual/linear_regression_r_output.png` |
| AI | `ai/linear_regression_python_output.png` | `ai/linear_regression_r_output.png` |

These plots show the scatter points and the fitted regression line.

---

## Part A vs Part B

### Part A — Manual (`manual/`)

Built by hand in Jupyter Lab:

- Python + R notebooks and HTML exports
- Python + R CLI scripts
- Saved plot images

### Part B — AI-assisted (`ai/`)

Rebuilt with AI help (same deliverables).

Important prompts are listed in:

- `ai/PROMPTS.md`

---

## Tools used

- **Python:** pandas, matplotlib, scikit-learn
- **R:** base R (`lm`), ggplot2
- **Jupyter Lab** for notebooks
- **Conda** for environment management (`7030_class_1`)

---

## Notes for beginners

- A **notebook** (`.ipynb`) is good for exploring and explaining steps.
- A **script** (`.py` / `.R` / `.r`) is better for repeating the analysis from Terminal.
- **HTML export** makes it easy to share notebook results without needing Jupyter.
- Always check that you are in the right folder before running scripts, so the CSV path and output PNG location are correct.
- If R creates an unwanted `Rplots.pdf`, it usually means a plot was printed on screen during `Rscript`. Prefer `ggsave(...)` only in CLI scripts.

---

## Author

Trang Nguyen  
Data Science for Biomedical Sciences — Assignment 2
