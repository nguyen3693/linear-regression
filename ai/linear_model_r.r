#!/usr/bin/env Rscript
# Linear regression CLI script (AI-assisted).
#
# Usage:
#   Rscript linear_model_r.r <filename> <x_column> <y_column>
#
# Example:
#   Rscript linear_model_r.r ../regression_data.csv YearsExperience Salary

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 3) {
  stop("Usage: Rscript linear_model_r.r <filename> <x_column> <y_column>")
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
summary_model <- summary(model)

y_actual <- data[[y_col]]
y_pred <- predict(model)

intercept <- coef(model)[1]
slope <- coef(model)[2]
r2 <- summary_model$r.squared
adj_r2 <- summary_model$adj.r.squared
p_value <- summary_model$coefficients[2, 4]
std_err <- summary_model$coefficients[2, 2]
mse <- mean((y_actual - y_pred)^2)
rmse <- sqrt(mse)
mae <- mean(abs(y_actual - y_pred))

cat(sprintf("Slope: %.2f\n", slope))
cat(sprintf("Intercept: %.2f\n", intercept))
cat(sprintf("Equation: %s = %.2f + %.2f * %s\n", y_col, intercept, slope, x_col))
cat(sprintf("R-squared: %.4f\n", r2))
cat(sprintf("Adjusted R-squared: %.4f\n", adj_r2))
cat(sprintf("p-value: %.6f\n", p_value))
cat(sprintf("Standard error: %.2f\n", std_err))
cat(sprintf("Mean Squared Error (MSE): %.2f\n", mse))
cat(sprintf("Root Mean Squared Error (RMSE): %.2f\n", rmse))
cat(sprintf("Mean Absolute Error (MAE): %.2f\n", mae))

x_vals <- data[[x_col]]
y_vals <- data[[y_col]]

output_path <- "linear_model_r_output.png"
png(output_path, width = 800, height = 500, res = 150)
plot(
  x_vals,
  y_vals,
  pch = 19,
  col = "red",
  main = paste(y_col, "vs", x_col),
  xlab = x_col,
  ylab = y_col
)
abline(model, col = "blue", lwd = 2)
legend(
  "bottomright",
  legend = c("Data points", "Regression line"),
  col = c("red", "blue"),
  pch = c(19, NA),
  lty = c(NA, 1),
  lwd = c(NA, 2)
)
annotation <- sprintf(
  "y = %.2fx + %.2f\nR² = %.2f\nMSE = %.2f",
  slope, intercept, r2, mse
)
text(
  x = min(x_vals),
  y = max(y_vals),
  labels = annotation,
  adj = c(0, 1),
  cex = 0.9
)
dev.off()
cat(sprintf("Saved plot: %s\n", output_path))
