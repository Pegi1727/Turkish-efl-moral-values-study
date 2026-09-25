# ==============================================================================
# 02_wilson_confidence_intervals.R
# Computes exact Wilson Score Confidence Intervals and Standard Errors in R.
# ==============================================================================

compute_wilson_table <- function(counts, total_n, var_label) {
  df <- data.frame(
    Variable = var_label,
    Category = names(counts),
    Count = as.numeric(counts),
    stringsAsFactors = FALSE
  )
  
  df$Percentage <- round((df$Count / total_n) * 100, 2)
  p <- df$Count / total_n
  df$SE <- round(sqrt(p * (1 - p) / total_n) * 100, 2)
  
  # Calculate Wilson CI using prop.test
  ci_matrix <- t(sapply(df$Count, function(x) {
    test <- prop.test(x, total_n, conf.level = 0.95, correct = FALSE)
    c(test$conf.int[1] * 100, test$conf.int[2] * 100)
  }))
  
  df$CI_Lower_95 <- round(ci_matrix[, 1], 2)
  df$CI_Upper_95 <- round(ci_matrix[, 2], 2)
  
  return(df)
}

# Example execution for Beliefs and Barriers
t_data <- read.csv("Teachers_Data.csv")
t_n <- nrow(t_data)

res_belief <- compute_wilson_table(table(t_data$Separation_Belief), t_n, "Separation Belief")
res_values <- compute_wilson_table(table(t_data$Value_Priority), t_n, "Moral Values")
res_obstacles <- compute_wilson_table(table(t_data$Reported_Obstacle), t_n, "Obstacles")

final_summary <- rbind(res_belief, res_values, res_obstacles)
print(final_summary)
write.csv(final_summary, "R_Wilson_CI_Summary.csv", row.names = FALSE)
cat("\nSaved 'R_Wilson_CI_Summary.csv'\n")
