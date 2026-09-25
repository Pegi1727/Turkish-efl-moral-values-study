# ==============================================================================
# 03_ggplot2_publication_figures.R
# Generates publication-ready vector and PNG plots with ggplot2.
# ==============================================================================

library(ggplot2)
library(patchwork)

# Data preparation
df_values <- data.frame(
  Value = factor(c("Global Citizenship", "Empathy", "Respect", "Honesty"),
                 levels = rev(c("Global Citizenship", "Empathy", "Respect", "Honesty"))),
  Percentage = c(70, 14, 10, 6)
)

# Plot Figure 1B: Values
p1 <- ggplot(df_values, aes(x = Percentage, y = Value, fill = Value)) +
  geom_col(show.legend = FALSE, fill = "#3182bd") +
  geom_text(aes(label = paste0(Percentage, "%")), hjust = -0.2, size = 4) +
  scale_x_continuous(limits = c(0, 85)) +
  labs(title = "Teachers' Value Priorities (N=50)", x = "Percentage (%)", y = "") +
  theme_minimal(base_size = 12) +
  theme(plot.title = element_text(face = "bold"))

# Data for Obstacles
df_obstacles <- data.frame(
  Obstacle = factor(c("Student Resistance", "Time Constraints", "Lack of Training"),
                    levels = rev(c("Student Resistance", "Time Constraints", "Lack of Training"))),
  Percentage = c(50, 30, 20)
)

# Plot Figure 3B: Barriers
p2 <- ggplot(df_obstacles, aes(x = Percentage, y = Obstacle)) +
  geom_col(fill = "#de2d26") +
  geom_text(aes(label = paste0(Percentage, "%")), hjust = -0.2, size = 4) +
  scale_x_continuous(limits = c(0, 65)) +
  labs(title = "Reported Instructional Obstacles (N=50)", x = "Percentage (%)", y = "") +
  theme_minimal(base_size = 12) +
  theme(plot.title = element_text(face = "bold"))

# Combine with patchwork
combined_plot <- p1 / p2
ggsave("R_Combined_Publication_Figure.png", combined_plot, width = 8, height = 7, dpi = 300)
cat("Saved 'R_Combined_Publication_Figure.png'\n")
