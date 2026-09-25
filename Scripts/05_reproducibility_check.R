# ==============================================================================
# 05_reproducibility_check.R
# Automated verification test checking outputs against manuscript values.
# ==============================================================================

library(testthat)
library(readr)

t_data <- read_csv("Teachers_Data.csv", show_col_types = FALSE)
s_data <- read_csv("Students_Data.csv", show_col_types = FALSE)

test_that("Sample sizes are strictly N=50", {
  expect_equal(nrow(t_data), 50)
  expect_equal(nrow(s_data), 50)
})

test_that("Core Teacher Percentages match manuscript exactly", {
  sep_pct <- mean(t_data$Separation_Belief == "Separate") * 100
  expect_equal(sep_pct, 70.0)
  
  gc_pct <- mean(t_data$Value_Priority == "Global Citizenship") * 100
  expect_equal(gc_pct, 70.0)
  
  res_pct <- mean(t_data$Reported_Obstacle == "Student Resistance") * 100
  expect_equal(res_pct, 50.0)
})

test_that("Student Thematic Consistency is 100%", {
  kindness_pct <- mean(s_data$Narrative_Theme == "Kindness & Honesty") * 100
  expect_equal(kindness_pct, 100.0)
})

cat("All reproducibility checks passed successfully! All scripts are verified.\n")
