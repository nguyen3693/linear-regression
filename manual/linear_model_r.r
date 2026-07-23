#!/usr/bin/env Rscript
#make sure ggplot2 is installed in environment
#install.packages("ggplot2")


library(ggplot2)

data <- read.csv("../regression_data.csv")

x <- data$YearsExperience
y <- data$Salary

model <- lm(y ~ x)

slope <- coef(model)[2]
intercept <- coef(model)[1]
r_squared <- summary(model)$r.squared
pred <- predict(model)
mse <- mean(pred - y)^2

cat("slope =", slope, "\n")
cat("y-intercept =", intercept, "\n") 
cat("R-squared value =", r_squared, "\n")
cat("mean standard error =", mse, "\n")
cat("y =", round(slope, 2), "* x +", round(intercept, 2), "\n")     #round(___, 2) rounds to two decimal places

df <- data.frame(
  x = x,
  y = y
)

ggplot(df, aes(x = x, y = y)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  annotate(
      "text",
      x = 1.5, 
      y = max(df$y) - 0.5,
      label = paste(
          "y =", round(slope, 2), "x +", round(intercept, 2),
          "\nR-squared =", round(r_squared, 2),
          "\nMSE =", format(mse, scientific = TRUE, digits = 3)
      ),

      size = 4
  ) + 

labs(
    title = "Linear Fit", 
    x = "Years Experience", 
    y = "Salary"
) + 

theme_minimal()

summary(model)

ggsave("regression_plot_r.png")

### Check command script is typed correctly in Terminal 

#**Aka “If the user did not give exactly 3 arguments after the script name, show them the correct usage and quit.”**

#Example: `cd linear-regression/manual` then type in command line `Rscript linear_model_r.R ../regression_data.csv YearsExperience Salary`

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_model_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]
