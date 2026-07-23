#!/usr/bin/env python3
"""
Linear regression CLI script (AI-assisted).

Usage:
    python linear_model_python.py <filename> <x_column> <y_column>

Example:
    python linear_model_python.py ../regression_data.csv YearsExperience Salary
"""

import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():
    if len(sys.argv) != 4:
        print("Usage: python linear_model_python.py <filename> <x_column> <y_column>")
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

    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y, y_pred)

    lin_stats = linregress(data[x_col], data[y_col])
    p_value = lin_stats.pvalue
    std_err = lin_stats.stderr

    print(f"Slope: {slope:.2f}")
    print(f"Intercept: {intercept:.2f}")
    print(f"Equation: {y_col} = {intercept:.2f} + {slope:.2f} * {x_col}")
    print(f"R-squared: {r2:.4f}")
    print(f"p-value: {p_value:.6f}")
    print(f"Standard error: {std_err:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(data[x_col], data[y_col], color="red", label="Data points")
    plt.plot(data[x_col], y_pred, color="blue", linewidth=2, label="Regression line")

    annotation = (
        f"y = {slope:.2f}x + {intercept:.2f}\n"
        f"R² = {r2:.2f}\n"
        f"MSE = {mse:.2f}"
    )
    plt.text(
        0.05,
        0.95,
        annotation,
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )

    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path = "linear_model_python_output.png"
    plt.savefig(output_path, dpi=150)
    print(f"Saved plot: {output_path}")


if __name__ == "__main__":
    main()
