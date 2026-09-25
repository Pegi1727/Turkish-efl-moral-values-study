"""
02_calculate_wilson_ci.py
Calculates Frequencies, Percentages, Standard Errors (SE), and 95% Wilson Score CIs.
"""

import numpy as np
import pandas as pd

def wilson_score_interval(count, nobs, confidence=0.95):
    if nobs == 0:
        return (0.0, 0.0)
    z = 1.959963984540054  # Normal critical value for 95%
    p = count / nobs
    denom = 1.0 + (z**2) / nobs
    center = (p + (z**2) / (2.0 * nobs)) / denom
    margin = (z * np.sqrt((p * (1.0 - p) + (z**2) / (4.0 * nobs)) / nobs)) / denom
    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)
    return lower * 100, upper * 100

def compute_variable_stats(series, variable_name):
    nobs = len(series)
    counts = series.value_counts()
    records = []
    
    for category, count in counts.items():
        pct = (count / nobs) * 100
        se = np.sqrt((pct/100) * (1 - (pct/100)) / nobs) * 100
        ci_low, ci_high = wilson_score_interval(count, nobs)
        records.append({
            'Variable': variable_name,
            'Category': category,
            'Count (n)': count,
            'Percentage (%)': round(pct, 2),
            'SE (%)': round(se, 2),
            '95% Wilson CI Lower (%)': round(ci_low, 2),
            '95% Wilson CI Upper (%)': round(ci_high, 2)
        })
    return records

def main():
    df_t = pd.read_csv('Teachers_Data.csv')
    df_s = pd.read_csv('Students_Data.csv')
    
    all_results = []
    # Teachers stats
    for col in df_t.columns[1:]:
        all_results.extend(compute_variable_stats(df_t[col], f'Teacher: {col}'))
        
    # Students stats
    for col in df_s.columns[1:]:
        all_results.extend(compute_variable_stats(df_s[col], f'Student: {col}'))
        
    res_df = pd.DataFrame(all_results)
    res_df.to_csv('Statistical_Summary_Wilson_CI.csv', index=False)
    print("Statistical summary with Wilson CIs generated: 'Statistical_Summary_Wilson_CI.csv'")
    print(res_df.head(10))

if __name__ == '__main__':
    main()
