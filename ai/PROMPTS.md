Important Cursor prompts used for ai portion of Assignment 2:

1. Time to work on part B, the ai assisted portion of the assignment. Pretend you don't know the manual work I did in part A. Use existing conda environment 7030_class_1. We will work together to build linear regression apps in Python and R using Jupyter Notebooks, then convert them to standalone CLI scripts. In ai/ folder, create the following notebooks and HTML files
- Jupyter Notebook using the Python kernel
- Jupyter Notebook using the R kernel
The dataset: regression_data.csv
Exported HTML versions of both notebooks (.html)
Each notebook must:
- Read the CSV file
- Create a scatter plot
- Fit a linear model
- Overlay the regression line
- Evaluate the model
- Be saved as both .ipynb and .html
Command-line scripts:
linear_regression_python.py, converted from the Python notebook
linear_regression_r.R, converted from the R notebook
Both scripts must:
Accept command-line arguments: <filename> <x_column> <y_column>
Generate and save a plot image (linear_regression_python_output.png, linear_regression_r_output.png)
