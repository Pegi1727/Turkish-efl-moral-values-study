# Data Dictionary

These schemas describe the supplied raw files `Teachers_Data.csv` and `Students_Data.csv` as inspected. Both are UTF-8-compatible comma-separated tables with a header row. Each row is one anonymized respondent; each substantive field is stored as text. No missing values or duplicate IDs were observed in the supplied files. Valid enumerations below describe observed/expected categories, not a license to coerce unknown future values.

## `Teachers_Data.csv`
**Observed size:** 50 rows × 7 columns; one row per teacher; ID pattern `T_01`–`T_50`.

| Column (exact spelling) | Storage / conceptual type | Allowed observed values / constraint | Description |
|---|---|---|---|
| `Teacher_ID` | String; nominal identifier | Unique nonempty `T_` plus two-digit sequence; observed T_01–T_50. | Anonymous respondent key. No student linkage. |
| `Perception_Role_Separation` | String; nominal binary | `Separate (Agree)`; `Integrated (Disagree)`. | Position on separation versus integration of EFL and moral education. |
| `Core_Value_Priority` | String; nominal, single category | `Global Citizenship`; `Empathy`; `Respect`; `Honesty`. | Reported core-value priority. No ranking scale. |
| `Curriculum_Adequacy` | String; nominal binary | `Inadequate`; `Adequate`. | Perceived adequacy of curriculum support. |
| `Preferred_Technique` | String; nominal | `Debates`; `Storytelling`; `Role-playing`; `Group work`. | Preferred method category. Exact capitalization is meaningful in raw data. |
| `Preferred_Material` | String; nominal | `Videos`; `News`; `Articles`. | Preferred material category; preserve News/Articles distinction. |
| `Primary_Obstacle` | String; nominal | `Student resistance`; `Time constraints`; `Lack of training`. | Primary reported obstacle. |

### Teacher constraints / verified aggregate frequencies
One nonmissing category per column per respondent; expected `n=50` per item. Observed: separation 35/15; values global citizenship 35, empathy 7, respect 5, honesty 3; curriculum inadequate 40/adequate 10; techniques debates 23, storytelling 15, role-playing 7, group work 5; materials videos 25, news 15, articles 10; obstacles resistance 25, time 15, training 10. These sum to 50 in each item. Percentages are `count / 50 × 100`.

## `Students_Data.csv`
**Observed size:** 50 rows × 3 columns; one row per student; ID pattern `S_01`–`S_50`.

| Column (exact spelling) | Storage / conceptual type | Allowed observed values / constraint | Description |
|---|---|---|---|
| `Student_ID` | String; nominal identifier | Unique nonempty `S_` plus two-digit sequence; observed S_01–S_50. | Anonymous key; no teacher matching field. |
| `Ethical_Talk_Frequency` | String; nominal, collapsed category | `Yes, most of the times`; `Sometimes / Rarely / Never`. | Student-reported frequency of ethical/value discussion. Second level combines sometimes, rarely, and never; cannot distinguish them. |
| `Reported_Story_Theme` | String; nominal thematic code | Observed `Kindness & Honesty`. | Harmonized theme for reported/reproduced classroom story. The single observed category yields no variation in this file. |

### Student constraints / verified aggregate frequencies
Expected `n=50` per field. Frequency: 20 `Yes, most of the times`, 30 `Sometimes / Rarely / Never`; theme 50 `Kindness & Honesty`. All percentages use 50 as denominator. Do not interpret one-category coding as an independently verified transcript-level finding without source records and coding documentation.

## General validation rules
- Preserve column names and category strings exactly; trim accidental whitespace only with an explicit logged cleaning step.
- IDs must be unique/nonmissing within each file. They are cohort-specific and must not be joined across files.
- For expected complete files, each category-valued field must be nonmissing and each item’s frequency total must equal 50. If future data include missing or invalid answers, report a valid-response denominator and retain a missing/invalid audit.
- Enforce enumerations by validation, not silent recoding. Unknown values should fail validation and be reviewed.
- Data types are nominal; no ordinal ordering should be inferred from the labels.
- Detailed prompts in the questionnaire are not all represented in these CSVs. There are no columns for free text, teacher assessment of internalization, cultural perspective responses, story identity, transcripts, or audio paths.

## Provenance discrepancy
The supplied notebooks include generated/appendix summary data with denominator 20, while the two raw files described here each contain 50 rows. Those are distinct analytical artifacts. Do not overwrite or conflate these schemas or present N=20 notebook figures as raw CSV results until provenance has been reconciled.
