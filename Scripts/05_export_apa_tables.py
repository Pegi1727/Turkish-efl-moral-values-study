"""
05_export_apa_tables.py
Exports Tables 1 to 4 formatted strictly according to APA 7th Edition guidelines.
"""

import pandas as pd

def generate_tables():
    t1 = """Table 1
Teachers' Beliefs on Moral Pedagogy and Curricular Guidance (N = 50)
---------------------------------------------------------------------------------------------------------
Item / Dimension                           Category          n      %     SE (%)     95% Wilson CI
---------------------------------------------------------------------------------------------------------
Pedagogical Stance                         Separate         35    70.0      6.48     [56.25, 80.90]
                                           Integrate        15    30.0      6.48     [19.10, 43.75]
Curricular Guidance Adequacy               Inadequate       40    80.0      5.66     [67.03, 88.80]
                                           Adequate         10    20.0      5.66     [11.20, 32.97]
---------------------------------------------------------------------------------------------------------
Note. SE = Standard Error; CI = Confidence Interval.
"""

    t2 = """Table 2
Distribution of Core Moral Value Priorities Prioritized by Teachers (N = 50)
---------------------------------------------------------------------------------------------------------
Rank    Moral Value Dimension              n      %     SE (%)     95% Wilson CI
---------------------------------------------------------------------------------------------------------
1       Global Citizenship                35    70.0      6.48     [56.25, 80.90]
2       Empathy                            7    14.0      4.91     [ 7.00, 26.15]
3       Respect                            5    10.0      4.24     [ 4.35, 21.36]
4       Honesty                            3     6.0      3.36     [ 2.07, 16.22]
---------------------------------------------------------------------------------------------------------
Note. Teachers selected their primary instructional value orientation.
"""

    t3 = """Table 3
Pedagogical Methods, Materials, and Instructional Barriers Reported by Teachers (N = 50)
---------------------------------------------------------------------------------------------------------
Dimension                Category                  n      %     SE (%)     95% Wilson CI
---------------------------------------------------------------------------------------------------------
Teaching Methods         Debates                  23    46.0      7.05     [32.97, 59.67]
                         Storytelling             15    30.0      6.48     [19.10, 43.75]
                         Role-playing              7    14.0      4.91     [ 7.00, 26.15]
                         Group work                5    10.0      4.24     [ 4.35, 21.36]

Instructional Media      Videos                   25    50.0      7.07     [36.63, 63.37]
                         News Stories             15    30.0      6.48     [19.10, 43.75]
                         Articles                 10    20.0      5.66     [11.20, 32.97]

Primary Barriers         Student Resistance       25    50.0      7.07     [36.63, 63.37]
                         Time Constraints         15    30.0      6.48     [19.10, 43.75]
                         Lack of Training         10    20.0      5.66     [11.20, 32.97]
---------------------------------------------------------------------------------------------------------
"""

    t4 = """Table 4
Student Perceptions of Classroom Ethical Talk and Narrative Themes (N = 50)
---------------------------------------------------------------------------------------------------------
Variable                                   Category          n      %     SE (%)     95% Wilson CI
---------------------------------------------------------------------------------------------------------
Frequency of Ethical Discussions           Most of the time 20    40.0      6.93     [27.61, 53.82]
                                           Sometimes/Rarely 30    60.0      6.93     [46.18, 72.39]
Narrative Retelling Themes                 Kindness & Honesty 50 100.0      0.00     [92.86, 100.00]
---------------------------------------------------------------------------------------------------------
Note. Narrative responses reflect qualitative thematic extraction from oral retelling tasks.
"""

    with open('Tables_1_to_4_APA7.txt', 'w', encoding='utf-8') as f:
        f.write(t1 + "\n\n" + t2 + "\n\n" + t3 + "\n\n" + t4)
    print("Saved 'Tables_1_to_4_APA7.txt'")

if __name__ == '__main__':
    generate_tables()
