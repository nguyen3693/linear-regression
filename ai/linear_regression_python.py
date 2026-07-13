#!/usr/bin/env python3
"""
Linear regression CLI script (AI-assisted).

Usage:
    python linear_regression_python.py <filename> <x_column> <y_column>

Example:
    python linear_regression_python.py ../regression_data.csv YearsExperience Salary
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np


def main():
    if len(sys.argv) != 4:
        print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
        sys.exit(1)

    filename = sys.argv[1]
    x_col = sys.argv[2]
    y_col = sys.argv[3]

    data = pd.read_csv(filename)

    if x_col not in data.columns or y_col not in data.columns:
        print(f"Error: columns must be one of {list(data.columns)}")
        sys.exit(1)

    X = data[[x_col]]
    y = data[y_col]

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    print(f"Intercept: {model.intercept_:.2f}")
    print(f"Slope: {model.coef_[0]:.2f}")
    print(f"Equation: {y_col} = {model.intercept_:.2f} + {model.coef_[0]:.2f} * {x_col}")
    print(f"R-squared: {r2_score(y, y_pred):.4f}")
    print(f"MSE: {mean_squared_error(y, y_pred):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y, y_pred)):.2f}")
    print(f"MAE: {mean_absolute_error(y, y_pred):.2f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(data[x_col], data[y_col], color="red", label="Data points")
    plt.plot(data[x_col], y_pred, color="blue", linewidth=2, label="Regression line")
    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path = "linear_regression_python_output.png"
    plt.savefig(output_path, dpi=150)
    print(f"Saved plot: {output_path}")


if __name__ == "__main__":
    main()
