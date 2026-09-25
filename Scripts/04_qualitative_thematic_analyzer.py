"""
04_qualitative_thematic_analyzer.py
Processes and validates student oral narrative transcript codes,
extracting keyword co-occurrences for kindness and honesty.
"""

import pandas as pd
from collections import Counter

# Sample illustrative narrative transcripts
MOCK_NARRATIVES = [
    {"id": "S_01", "text": "The main character chose to return the lost wallet because honesty is important in life."},
    {"id": "S_02", "text": "She was very kind to the poor animal and helped it recover, showing true kindness."},
    {"id": "S_03", "text": "Being honest with his parents helped him avoid bigger trouble in school."},
    {"id": "S_04", "text": "True friendship means treating others with kindness and sharing what you have."}
]

def analyze_narratives(transcripts):
    results = []
    for item in transcripts:
        txt = item['text'].lower()
        has_kindness = 'kind' in txt or 'helped' in txt or 'cared' in txt
        has_honesty = 'honest' in txt or 'truth' in txt or 'wallet' in txt
        
        assigned_theme = "Kindness & Honesty" if (has_kindness or has_honesty) else "Other"
        results.append({
            'Participant_ID': item['id'],
            'Transcript_Excerpt': item['text'],
            'Detected_Theme': assigned_theme
        })
    
    df_res = pd.DataFrame(results)
    df_res.to_csv('Thematic_Coding_Audit.csv', index=False)
    print("Thematic coding audit generated: 'Thematic_Coding_Audit.csv'")
    print(df_res)

if __name__ == '__main__':
    analyze_narratives(MOCK_NARRATIVES)
