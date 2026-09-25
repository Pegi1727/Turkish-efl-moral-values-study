"""
01_generate_raw_datasets.py
Generates simulated anonymized raw datasets (N=50 Teachers, N=50 Students)
matching the exact statistical distributions reported in the study.
"""

import pandas as pd
import numpy as np

def generate_teacher_data():
    np.random.seed(42)
    n = 50
    
    # 1. Separation Belief: 35 Separate (70%), 15 Integrate (30%)
    sep_beliefs = ['Separate'] * 35 + ['Integrate'] * 15
    
    # 2. Core Value: Global Citizenship (35), Empathy (7), Respect (5), Honesty (3)
    values = ['Global Citizenship'] * 35 + ['Empathy'] * 7 + ['Respect'] * 5 + ['Honesty'] * 3
    
    # 3. Curriculum Adequacy: 40 Inadequate (80%), 10 Adequate (20%)
    curriculum = ['Inadequate'] * 40 + ['Adequate'] * 10
    
    # 4. Pedagogical Methods: Debates (23), Storytelling (15), Role-playing (7), Group work (5)
    methods = ['Debates'] * 23 + ['Storytelling'] * 15 + ['Role-playing'] * 7 + ['Group work'] * 5
    
    # 5. Media/Materials: Videos (25), News (15), Articles (10)
    media = ['Videos'] * 25 + ['News'] * 15 + ['Articles'] * 10
    
    # 6. Obstacles: Student Resistance (25), Time Constraints (15), Lack of Training (10)
    obstacles = ['Student Resistance'] * 25 + ['Time Constraints'] * 15 + ['Lack of Training'] * 10
    
    df_teachers = pd.DataFrame({
        'Participant_ID': [f'T_{i:02d}' for i in range(1, n + 1)],
        'Separation_Belief': sep_beliefs,
        'Value_Priority': values,
        'Curriculum_Adequacy': curriculum,
        'Primary_Method': methods,
        'Primary_Media': media,
        'Reported_Obstacle': obstacles
    })
    
    # Shuffle independently to reflect survey responses
    for col in df_teachers.columns[1:]:
        df_teachers[col] = np.random.permutation(df_teachers[col].values)
        
    df_teachers.to_csv('Teachers_Data.csv', index=False)
    print("Saved 'Teachers_Data.csv' (N=50)")

def generate_student_data():
    np.random.seed(42)
    n = 50
    
    # Ethical talk frequency: 20 Most of the time (40%), 30 Sometimes/Rarely/Never (60%)
    freq = ['Most of the time'] * 20 + ['Sometimes/Rarely/Never'] * 30
    
    # Narrative theme: 50 Kindness & Honesty (100%)
    themes = ['Kindness & Honesty'] * 50
    
    df_students = pd.DataFrame({
        'Participant_ID': [f'S_{i:02d}' for i in range(1, n + 1)],
        'Ethical_Talk_Frequency': np.random.permutation(freq),
        'Narrative_Theme': themes
    })
    
    df_students.to_csv('Students_Data.csv', index=False)
    print("Saved 'Students_Data.csv' (N=50)")

if __name__ == '__main__':
    generate_teacher_data()
    generate_student_data()
