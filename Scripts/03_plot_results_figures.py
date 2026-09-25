"""
03_plot_results_figures.py
Generates high-resolution academic figures (Figure 1 to 4) using Matplotlib/Seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams['font.size'] = 11

def plot_figure_1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1A: Beliefs
    labels_a = ['Separate Instruction\n(70%)', 'Integrate Instruction\n(30%)']
    sizes_a = [35, 15]
    colors_a = ['#4C72B0', '#55A868']
    ax1.pie(sizes_a, labels=labels_a, autopct='%1.1f%%', startangle=140, colors=colors_a, wedgeprops=dict(width=0.4))
    ax1.set_title('A. Teacher Moral Pedagogy Stance (N=50)', fontweight='bold')
    
    # 1B: Values
    values = ['Global Citizenship', 'Empathy', 'Respect', 'Honesty']
    pcts = [70, 14, 10, 6]
    sns.barplot(x=pcts, y=values, ax=ax2, palette='Blues_r')
    ax2.set_xlabel('Percentage of Teachers (%)')
    ax2.set_title('B. Core Moral Value Priorities (N=50)', fontweight='bold')
    for i, v in enumerate(pcts):
        ax2.text(v + 1, i, f"{v}%", va='center', fontweight='semibold')
    ax2.set_xlim(0, 85)
    
    plt.tight_layout()
    plt.savefig('Figure_1_Beliefs_and_Values.png', dpi=300)
    plt.close()
    print("Saved Figure_1_Beliefs_and_Values.png")

def plot_figure_2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Methods
    methods = ['Debates', 'Storytelling', 'Role-playing', 'Group work']
    m_pcts = [46, 30, 14, 10]
    sns.barplot(x=m_pcts, y=methods, ax=ax1, palette='mako')
    ax1.set_title('A. Instructional Techniques (N=50)', fontweight='bold')
    ax1.set_xlabel('Percentage (%)')
    for i, v in enumerate(m_pcts):
        ax1.text(v + 1, i, f"{v}%", va='center')
    ax1.set_xlim(0, 55)
    
    # Media
    media = ['Videos', 'News Stories', 'Articles']
    med_pcts = [50, 30, 20]
    sns.barplot(x=med_pcts, y=media, ax=ax2, palette='viridis')
    ax2.set_title('B. Instructional Materials (N=50)', fontweight='bold')
    ax2.set_xlabel('Percentage (%)')
    for i, v in enumerate(med_pcts):
        ax2.text(v + 1, i, f"{v}%", va='center')
    ax2.set_xlim(0, 60)
    
    plt.tight_layout()
    plt.savefig('Figure_2_Pedagogical_Practices.png', dpi=300)
    plt.close()
    print("Saved Figure_2_Pedagogical_Practices.png")

def plot_figure_3_and_4():
    # Figure 3: Barriers & Curriculum
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.pie([80, 20], labels=['Inadequate (80%)', 'Adequate (20%)'], autopct='%1.0f%%',
            colors=['#C44E52', '#8C8C8C'], startangle=90, wedgeprops=dict(width=0.4))
    ax1.set_title('A. Curricular Guidance Adequacy', fontweight='bold')
    
    barriers = ['Student Resistance', 'Time Constraints', 'Lack of Training']
    b_pcts = [50, 30, 20]
    sns.barplot(x=b_pcts, y=barriers, ax=ax2, palette='Reds_r')
    ax2.set_title('B. Primary Instructional Obstacles', fontweight='bold')
    ax2.set_xlabel('Percentage (%)')
    for i, v in enumerate(b_pcts):
        ax2.text(v + 1, i, f"{v}%", va='center')
    ax2.set_xlim(0, 60)
    plt.tight_layout()
    plt.savefig('Figure_3_Curricular_and_Barriers.png', dpi=300)
    plt.close()
    print("Saved Figure_3_Curricular_and_Barriers.png")

    # Figure 4: Student Perception & Narrative
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.pie([40, 60], labels=['Most of the Time (40%)', 'Sometimes/Rarely (60%)'],
            autopct='%1.0f%%', colors=['#4C72B0', '#CCB974'], startangle=90)
    ax1.set_title('A. Student Perception of Ethical Talk', fontweight='bold')
    
    sns.barplot(x=[100], y=['Kindness & Honesty'], ax=ax2, color='#55A868')
    ax2.set_title('B. Narrative Thematic Reproduction (N=50)', fontweight='bold')
    ax2.set_xlabel('Percentage of Students (%)')
    ax2.text(80, 0, '100% (n=50)', color='white', va='center', fontweight='bold')
    ax2.set_xlim(0, 110)
    plt.tight_layout()
    plt.savefig('Figure_4_Student_Perceptions_Narratives.png', dpi=300)
    plt.close()
    print("Saved Figure_4_Student_Perceptions_Narratives.png")

if __name__ == '__main__':
    plot_figure_1()
    plot_figure_2()
    plot_figure_3_and_4()
