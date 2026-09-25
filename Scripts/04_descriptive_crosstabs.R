# ==============================================================================
# 04_descriptive_crosstabs.R
# Examines within-cohort cross-tabulations and distributions.
# ==============================================================================

library(dplyr)
library(readr)

t_df <- read_csv("Teachers_Data.csv", show_col_types = FALSE)

cat("=== Cross-Tabulation: Separation Belief vs. Reported Obstacle ===\n")
tab_belief_obs <- table(t_df$Separation_Belief, t_df$Reported_Obstacle)
print(tab_belief_obs)

cat("\n=== Row Proportions ===\n")
print(round(prop.table(tab_belief_obs, 1) * 100, 2))

cat("\n=== Cross-Tabulation: Preferred Method vs. Primary Media ===\n")
tab_method_media <- table(t_df$Primary_Method, t_df$Primary_Media)
print(tab_method_media)
