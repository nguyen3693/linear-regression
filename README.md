# Assignment 3: Git and Improvements to Assignment 2

## Project Description

This project builds a **simple linear regression** model to predict **Salary** from **Years of Experience** using Python and R scripts and executable in Terminal command line. In "manual" folder, I wrote Python and R Jupyter notebooks by hand that walks through my chosen statistical analysis and plot generation.


## Contents

```
linear-regression/
├── README.md    # this file
├── regression_data.csv     # dataset
├── environment.yml     # Conda environment definition
├── requirements.txt
├── setup_env.sh
├── manual/                 
│   ├── linear_model_python.ipynb
│   ├── linear_model_python.html
│   ├── linear_model_python.py
│   ├── regression_plot_python.png
│   ├── linear_model_r.ipynb
│   ├── linear_model_r.html
│   ├── linear_model_r.r
│   └── regression_plot_r.png
└── ai/        # contents of ai folder will be described in "README_AI.md"
```

## Dataset

File: `regression_data.csv`

| Column | Meaning |
|--------|---------|
| `YearsExperience` | Years of work experience (X) |
| `Salary` | Salary amount (Y) |


## Getting Started
1. Clone the Repository

```
git clone https://github.com/nguyen3693/linear-regression.git
cd linear-regression.git
```

2. Create the Conda Environment and activate
```
conda env create -f environment.yml
conda activate 7030_class_1
```

3. Launch Jupyter Lab
```
jupyter lab
```


## Run command-line scripts in Terminal

Navigate Jupyter Terminal. 

Run scripts from inside the `manual/` folder so the output .png is saved in that folder.
`cd ~/linear-regression/manual`

Python and R scripts take exactly **3 arguments**

To run Python script: `python linear_model_python.py ../regression_data.csv YearsExperience Salary`

To run R script: `Rscript linear_model_r.R ../regression_data.csv YearsExperience Salary`

*See individual notebooks for more infomation on each script*

---

## Author

Trang Nguyen  
Data Science for Biomedical Sciences — Assignment 3
