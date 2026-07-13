#!/usr/bin/env Rscript
# Linear regression CLI script (AI-assisted).
#
# Usage:
#   Rscript linear_regression_r.R <filename> <x_column> <y_column>
#
# Example:
#   Rscript linear_regression_r.R ../regression_data.csv YearsExperience Salary

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)

if (!(x_col %in% colnames(data)) || !(y_col %in% colnames(data))) {
  stop(paste("Error: columns must be one of", paste(colnames(data), collapse = ", ")))
}

formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)
y_pred <- predict(model)
y_actual <- data[[y_col]]

cat(sprintf("Intercept: %.2f\n", coef(model)[1]))
cat(sprintf("Slope: %.2f\n", coef(model)[2]))
cat(sprintf("Equation: %s = %.2f + %.2f * %s\n",
            y_col, coef(model)[1], coef(model)[2], x_col))
cat(sprintf("R-squared: %.4f\n", summary(model)$r.squared))
cat(sprintf("MSE: %.2f\n", mean((y_actual - y_pred)^2)))
cat(sprintf("RMSE: %.2f\n", sqrt(mean((y_actual - y_pred)^2))))
cat(sprintf("MAE: %.2f\n", mean(abs(y_actual - y_pred))))

library(ggplot2)

plot <- ggplot(data, aes(x = .data[[x_col]], y = .data[[y_col]])) +
  geom_point(color = "red", size = 3) +
  geom_smooth(method = "lm", se = FALSE, color = "blue", linewidth = 1) +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col) +
  theme_minimal()

output_path <- "linear_regression_r_output.png"
ggsave(output_path, plot = plot, width = 8, height = 5, dpi = 150)
cat(sprintf("Saved plot: %s\n", output_path))
