# Research Overview

## Study
**Integrating Moral Values in Turkish EFL Classrooms: Teachers’ Beliefs, Pedagogical Practices, and Students’ Narrative Responses** examines how values education is positioned and encountered in English as a Foreign Language (EFL) learning in Turkey. The study combines categorical survey summaries with qualitative examination of students’ recalled/reproduced classroom narratives. Its focus is descriptive and interpretive, not experimental or causal.

## Rationale and conceptual framing
Language teaching is not wholly value-neutral: curricular topics, selected materials, interaction norms, and opportunities to discuss disagreement can convey or invite ethical and civic perspectives. EFL classrooms can connect language learning with intercultural understanding and global citizenship, but the phrase *global citizenship* covers diverse orientations and should not be treated as a single, self-evident instructional outcome. Values may also be conveyed through familiar narrative virtues such as kindness and honesty, independently of explicit values objectives.

Three distinctions guide interpretation:

1. **Declared beliefs versus enacted/encountered practice.** Teachers may distinguish formal moral education from language teaching while learners report ethical discussion in English lessons. Neither survey alone establishes what happened in a particular class.
2. **Broad aspiration versus concrete material.** Teachers may prioritize global citizenship while learners recall stories focused on kindness and honesty. These operate at different levels of abstraction and need not be contradictory; narratives may be accessible vehicles for wider civic learning, but the present data do not establish that connection.
3. **Pedagogical intention versus learner reception.** Teachers’ preferred techniques (including debate) and reported barriers (including student resistance) coexist with student accounts of ethical talk and stories. The measures do not link any teacher’s choice to any student’s response; they do not demonstrate efficacy, internalization, or causation.

## Research questions
1. How do Turkish EFL teachers perceive the relationship between English instruction and formal moral education?
2. Which values do teachers prioritize, and which teaching techniques and materials do they prefer for values-oriented instruction?
3. What obstacles do teachers identify when integrating values into EFL lessons?
4. How frequently do students report ethical discussion in English lessons, and what themes do they identify in classroom narratives?
5. What descriptive convergences and divergences appear when the teacher and student findings are considered together?

## Design and cohorts
The study uses a mixed-methods design with parallel, independently collected teacher and student components. The supplied raw files contain **50 teacher records** and **50 student records** (100 records in two cohorts). Recruitment is described in the manuscript as purposive, in Turkish educational institutions, based on direct experience of the EFL curriculum. Teacher records summarize teacher survey selections; student records summarize student-reported discussion frequency and narrative theme.

> **Critical design note: teachers and students are independent cohorts, not paired/dyadic observations.** There are no shared classroom, teacher, or matched respondent identifiers in the supplied CSV schemas. Cross-sample comparison is at aggregate thematic level only. Do not calculate dyadic associations, imply that a particular teacher taught a particular student, or treat the two samples as matched.

## Instruments and evidence
The teacher questionnaire covers role demarcation, value priority, curriculum adequacy, preferred technique, preferred material, and primary obstacle. Open prompts in the supplied questionnaire ask how values are integrated, which methods are effective, how materials are selected, what obstacles arise, and how teachers assess internalization. The raw teacher CSV has only six categorical survey measures plus ID; it does **not** contain free-text answers or an internalization measure.

The student instrument includes a categorical item on frequency of ethical talk and an oral narrative recall/reproduction task. The questionnaire also prompts recall of an activity/story, views on whether English supports understanding other perspectives, and preference for explicit moral teaching versus naturally arising discussion. Students’ narrative examples include familiar fables (e.g., *The Bear and Two Friends*, *The Golden Eggs*, *The Thirsty Crow*, *The Boy Who Cried Wolf*, and *The Honest Woodcutter*). The raw student CSV contains only frequency and a harmonized story-theme category; it does not contain transcripts, audio, verbatim answers, or separate codes for those additional prompts. The supplied narrative theme is **Kindness & Honesty**.

## Analysis workflow
- Validate identifiers, cohort sizes, allowed categories, missingness, and within-item denominators.
- Summarize categorical responses as counts and proportions; use standard errors and two-sided 95% Wilson score intervals to describe proportion precision where appropriate.
- Analyze available narrative material thematically, retaining an audit trail, code definitions, decisions, and negative cases when source transcripts are available. Do not infer individual moral development from story recall.
- Integrate findings through structured comparison of the three tensions above; preserve cohort independence and label evidence by source.

## Reported descriptive findings in the manuscript/data summary
For the **raw N=50 CSVs**, the teacher distributions are: separate EFL/moral education 35/50 (70%), integrated 15/50 (30%); curriculum inadequate 40/50 (80%), adequate 10/50 (20%); global citizenship 35/50 (70%), empathy 7/50 (14%), respect 5/50 (10%), honesty 3/50 (6%); debates 23/50 (46%), storytelling 15/50 (30%), role-playing 7/50 (14%), group work 5/50 (10%); videos 25/50 (50%), news 15/50 (30%), articles 10/50 (20%); student resistance 25/50 (50%), time constraints 15/50 (30%), lack of training 10/50 (20%). Student ethical talk “most of the times” is 20/50 (40%), otherwise 30/50 (60%); story theme Kindness & Honesty is 50/50 (100%). These are category summaries, not paired comparisons or causal effects.

## Data quality and interpretation caveats
- The supplied questionnaire notes contain rough percentages and incomplete/unclear question wording; use the raw CSV schema and verified aggregate summaries as the operational quantitative dataset, and document any discrepancy rather than silently reconciling it.
- The main manuscript and raw CSV summary report N=50 per cohort. Several supplied notebooks, especially `01_Data_Generation_and_Cleaning.ipynb` and `03_Publication_Figures_Generation.ipynb`, contain **appendix/example counts with denominator 20** and additional claims not represented in the raw CSV schema. Do not present those as raw N=50 findings without a documented reconciliation. `05_Comprehensive_Reproducibility_and_Verification.ipynb` also verifies N=20 appendix totals. Resolve this provenance mismatch before publication.
- A 100% thematic category in a coded data file does not prove every student independently generated that theme unless the coding unit and source transcripts are available and verified.
- Small, purposively selected samples limit external generalization. Self-report, summarized categories, absence of direct observation, and no linked pairs limit claims. The data do not measure value internalization or behavioral change.
- The manuscript states consent/assent and anonymization; no ethics approval number is reported. Follow applicable local requirements for any new collection or sharing of audio/transcripts.

## Suggested analytic stance
Use careful language (“reported,” “selected,” “coded,” “in this sample”). Report denominators with percentages, distinguish questionnaire response from thematic interpretation, and treat triangulation as complementary perspective rather than respondent-level validation. Avoid causal, population-wide, or dyadic claims.
