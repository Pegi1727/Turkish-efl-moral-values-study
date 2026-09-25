# ==============================================================================
# 01_load_and_inspect_data.R
# Loads generated raw datasets and computes initial contingency tables.
# ==============================================================================

library(dplyr)
library(readr)

# Load datasets
teachers_data <- read_csv("Teachers_Data.csv", show_col_types = FALSE)
students_data <- read_csv("Students_Data.csv", show_col_types = FALSE)

# Inspect Teacher Dataset
cat("=== TEACHER SAMPLE (N =", nrow(teachers_data), ") ===\n")
print(table(teachers_data$Separation_Belief))
print(table(teachers_data$Value_Priority))
print(table(teachers_data$Reported_Obstacle))

# Inspect Student Dataset
cat("\n=== STUDENT SAMPLE (N =", nrow(students_data), ") ===\n")
print(table(students_data$Ethical_Talk_Frequency))
print(table(students_data$Narrative_Theme))
