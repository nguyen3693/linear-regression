dataset <- read.csv("../regression_data.csv")

# if want to generate simple plot --> 'plot(dataset$YearsExperience, dataset$Salary, col="red")'

model <- lm(Salary ~ YearsExperience, data=dataset)

library(ggplot2)
plot <- ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

summary(model)
ggsave("linear_regression_r_output.png", plot)

# to run script on Terminal --> 'Rscript linear_regression_r.R ../regression_data.csv YearsExperience Salary'