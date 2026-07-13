import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()

#!/usr/bin/env python
# coding: utf-8

# # This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# ## Import external packages and libraries
# 
# Required libraries:
# - pandas (for working with tables of data)
# - matplotlib (for creating plots and charts)
# - scikit-learn (for building models)
# 
# Import commands:
# 
# `import pandas as pd                                 # enables DataFrame support`
# 
# `import matplotlib.pyplot as plt                     # enables plotting`
# 
# `from sklearn.linear_model import LinearRegression   # enables regression modeling`

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# ## Read "regression_data.csv" dataset file

# In[2]:


dataset = pd.read_csv("../regression_data.csv")


# ## Create scatter plot
# 
# command = `plt.scatter`
# 
# (x,y) arguments = `(dataset["YearsExperience"], dataset["Salary"])`
# 
# make dots red = `color="red"`
# 

# In[3]:


plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# ## Fit linear model
# 
# command = `model = LinearRegression()`
# 
# fit specific dataset = `model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])`
# 
# output LinearRegression table with list of parameters

# In[4]:


model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# ## Overlay the regression line
# 
# plot regression line and make it blue 
# 
# `plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")`
# 
# Title graph and x- and y-axis
# 
# `plt.title("Salary vs Experience")
# plt.xlabel("Years of Experience")
# plt.ylabel("Salary")`
# 
# Show table
# 
# `plt.show()`

# In[5]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# ## Evaluate the model
# 
# Calculate R^2 value of data
# 
# `model.score(dataset[["YearsExperience"]], dataset[["Salary"]])`

# In[6]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]]) #R-squared

# ## Run script from Terminal
#
# After exporting Jupyter notebook "linear_regression_python.ipynb" to ".py" file, go to Terminal, cd to `manual/` directory and run `python linear_regression_python.py ../regression_data.csv YearsExperience Salary`