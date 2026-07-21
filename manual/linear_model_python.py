#!/usr/bin/env python
# coding: utf-8

# # This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# ## Import external packages and libraries
# 
# Required libraries:
# - sys
# - pandas (for working with tables of data)
# - matplotlib (for creating plots and charts)
# - scikit-learn (for building models, e.g. linear regression, linear regression statistics, and mean squared error)
# 

# In[1]:


import sys                                                # enables Python variables and functions
import pandas as pd                                       # enables DataFrame support and defined as "pd"
import matplotlib.pyplot as plt                           # enables plotting and defined as "plt"
import numpy as np

from sklearn.linear_model import LinearRegression         # enables regression modeling
from scipy.stats import linregress                        # enables linear regression statistics
from sklearn.metrics import mean_squared_error            # enables mean squared error


# ## Read data and define x and y variables
# Read data from "regression_data.csv" file using pandas.
# 
# Reminder, data file is one folder back.
# 
# Use ../ for code to work.
# 
# **Define x** = "Years Experience"
# 
# **Define y** = "Salary"

# In[2]:


data = pd.read_csv("../regression_data.csv")
x = ["YearsExperience"]
y = ["Salary"]


# ## Calculate regression line and calculate R-squared value
# 

# In[3]:


model = LinearRegression()
model.fit(data[x], data[y])                                # fit regression line
model.score(data[x], data[y])                              # R-squared


# ## Statistics
# 
# Redefine x, y-variables to include data.
# 
# Analyze and print statistics for linear regression analysis:
# - slope
# - y-axis intercepts
# - r-squared value
# - p-value
# - standard error
# - mean squared error

# In[8]:


x = data["YearsExperience"]
y = data["Salary"]
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

def my_script():
    print("slope =", slope)        #fix this
    print("y-intercept =", intercept)
    print("r-squared =", r_value**2)
    print(f"y = {slope:.2f}x + {intercept:.2f}")
    print("p_value =", p_value)
    print("standardd error of linear regression =", std_err)
    print("mse =", mean_squared_error(y, y_pred))

my_script()


# ## Make a scatter plot
# 
# **Make scatter plot:** `plt.scatter()`
# - define x and y data inside ( )
# - make dots red: `color="red"`
# 
# plt.scatter(data[x], data[y], color="red")          # graph data onto scatter plot
# 
# 
# ## Overlay regression line and label graph
# 
# **Make line graph from x and y values:** `plt.plot()`
# - define x and y values based on prediction model
# - make line blue: `color="blue"`
#   
# **Label plot title and x- and y-axis:**
# title, xlabel, ylabel
# 
# 
# ## Show and save generated plot as new file
# 
# Save figure into folder and label file as "linear_regression_python_output.png"
# 
# Pop up window of generated graph

# In[5]:


plt.scatter(x, y, color="red")          # graph data onto scatter plot
plt.plot(x, y_pred, color="blue", label='Fitted Line')
plt.text(1, max(y) - 5000,              # draw functions text box at position (x,y) on graph
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value**2:.2f}\nMSE = {mse:.2f}",
         fontsize=9)

plt.title("Regression")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.legend()

plt.savefig("regression_plot_python.png")       # show and save graph
plt.show()


# ## Check command script is typed correctly in Terminal 
# 
# **Aka “If the user did not give exactly 3 arguments after the script name, show them the correct usage and quit.”**
# 
# Example: `cd linear-regression/manual` then type in command line `python linear_model_python.py ../regression_data.csv YearsExperience Salary
# `
# 
# `sys.argv` list of words from Terminal command, [1] [2] and [3]
# 
# `!= 4:` script expects exactly 4 items (script name + 3 arguments)
# 
# **Print a reminder on Terminal** of how to correctly run python script:
# 
# `print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")` 
# 
# `sys.exit(1)` Stops the program right away, (1) means "this ended because of an error and was not a successful run"
# 
#  **Define the arguments:** script expects exactly 3 arguments


if len(sys.argv) != 4:
     print("Usage: python linear_model_python.py <filename> <x_column> <y_column>")
     sys.exit(1)
 
filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

