# Codebook and Instruments

## Scope and coding conventions
This document distinguishes (a) questions/prompts visible in the supplied questionnaire/manuscript, (b) columns actually present in the two raw CSVs, and (c) qualitative code suggestions. Raw IDs are anonymized row identifiers, not linkage keys. All substantive CSV response fields are nominal categorical variables stored as text. No scale total, Likert score, or validated psychometric score is supplied. The teacher and student cohorts are independent (**N=50 each; not paired/dyadic**).

### Teacher survey: raw CSV variables (`Teachers_Data.csv`, N=50)
| Field / instrument domain | Operational meaning and response options | Type / coding / scoring |
|---|---|---|
| `Teacher_ID` | Record identifier, observed form `T_01`…`T_50`. | String nominal key; unique; no score. |
| `Perception_Role_Separation` | Position on whether EFL and formal moral education should be separate: `Separate (Agree)`; `Integrated (Disagree)`. | Nominal, binary categorical; category count and share. “Disagree” denotes disagreement with separation, not disagreement with moral education. |
| `Core_Value_Priority` | Single recorded priority: `Global Citizenship`, `Empathy`, `Respect`, `Honesty`. | Nominal; one selected category per record in file; frequencies, percentages. Not an ordered ranking. |
| `Curriculum_Adequacy` | Perceived adequacy of curriculum guidance/space: `Inadequate`, `Adequate`. | Nominal binary; frequency/share. |
| `Preferred_Technique` | Recorded preferred technique: `Debates`, `Storytelling`, `Role-playing`, `Group work`. | Nominal; one recorded category; no efficacy score. |
| `Preferred_Material` | Recorded preferred material: `Videos`, `News`, `Articles`. | Nominal; one recorded category. “News” and “Articles” are distinct raw values. |
| `Primary_Obstacle` | Most salient recorded obstacle: `Student resistance`, `Time constraints`, `Lack of training`. | Nominal; one recorded category; not a severity scale. |

**Teacher instrument prompts/domains in source documents:** (1) responsibility of English teachers for promoting moral values and whether EFL should be separate from moral education; (2) most essential values (examples include respect, honesty, empathy, global citizenship); (3) whether the official Turkish English curriculum offers sufficient guidance/space; (4) how values are integrated, with a recent example; (5) effective techniques (role-play, storytelling, debate, group work); (6) material selection (texts, videos, news articles); (7) obstacles (examples include time, resistance, training); and (8) how teachers assess internalization. The exact supplied questionnaire text is incomplete/edited and not all prompts have corresponding CSV variables. In particular, `Teachers_Data.csv` has no separate responsibility scale, open-text responses, lesson examples, assessment method, or internalization outcome. Do not invent or impute these.

### Student instrument and raw CSV (`Students_Data.csv`, N=50)
| Field / instrument domain | Operational meaning and response options | Type / coding / scoring |
|---|---|---|
| `Student_ID` | Record identifier, observed form `S_01`…`S_50`. | String nominal key; unique; not linkable to teachers. |
| `Ethical_Talk_Frequency` | Self-reported frequency of values/ethical discussion by English teacher: `Yes, most of the times`; `Sometimes / Rarely / Never`. | Nominal, dichotomized categorical response. The latter category combines three distinct frequencies; do not disaggregate it. Not an interval scale. |
| `Reported_Story_Theme` | Harmonized reported narrative theme; observed value `Kindness & Honesty`. | Nominal thematic category. Raw CSV has one value only, so no between-category variation can be estimated from this file. 50 identical values describe stored coding, not necessarily 50 independently auditable transcripts. |

**Student prompts/domains visible in questionnaire:** whether teachers discuss values/ethics/being a good person; recall of an activity/story and its moral value; whether English helps understand other cultural perspectives/values; and preference for explicit moral instruction or naturally emerging discussion, with rationale. An oral reproduction/retelling task is described in the manuscript. The CSV contains no transcript, audio path, story identity, response to perspective-taking/preference prompts, or narrative-length/quality score. Do not report these unrepresented measures as if they were in the CSV.

## Qualitative coding framework (proposed, not a claim of fully observed codes)
Use the following sensitizing codes only when the relevant source text/audio/transcript is available. Code at the response or meaning-unit level; allow multiple codes per response if justified; retain excerpts and coder decision notes.

| Axis | Candidate code | Inclusion guidance / evidence source |
|---|---|---|
| Perceptions | Responsibility; Professional Duty | Explicit attribution of values education responsibility to EFL teachers or another subject. Teacher open response. |
| Perceptions | Curriculum Gap | Explicit lack of guidance, space, or resources. Teacher response; distinguish from general dissatisfaction. |
| Perceptions | Cultural Necessity | Explicit reference to Turkish/local context, interculturality, or contextual need. Do not infer from a value label alone. |
| Strategies | Storytelling; Debate; Role-play; Group Work | Method named or described as used/preferred. Distinguish selection/preference from observed implementation. |
| Strategies | Socratic Questioning; Material Adaptation; Modeling | Use only when described in actual source response/lesson material; these are suggested analytic codes, not raw CSV options. |
| Constraints | Time Pressure; Student Resistance; Lack of Training; Linguistic Barrier; Cultural Conflict | Explicitly described constraint. The raw CSV supports the first three categories only. |
| Student Experience | Moral Awareness; Story Recall; Perspective Taking; Emotional Response | Code explicit learner account; does not establish durable learning. |
| Impact / Reception | Awareness; Internalization; Disconnect | “Internalization” only where respondents explicitly describe evidence/criteria; do not infer it from a recalled moral story. “Disconnect” requires a stated mismatch, not merely analyst juxtaposition. |
| Narrative theme | Kindness; Honesty; Respect; Responsibility; other emergent theme | Code the narrative content, not the student’s personal character. Multiple themes may co-occur. Existing CSV collapses content to `Kindness & Honesty`. |

## Scoring, missingness, and reporting
There is no composite scoring key. For each categorical item, calculate valid-response denominator, count, and proportion; retain missing/invalid values rather than silently recoding. For multi-response questions (if original forms show multiple selections), use item-specific counts and state whether percentages use respondents or total selections; current raw CSV represents one category per respondent for each field. Qualitative codes are interpretive labels and are not numerical scales. Reliability statistics require independently double-coded, linkable qualitative units; the supplied materials do not establish such coding, so do not report a kappa from the demonstration function in a notebook as project reliability.

## Provenance warning
The supplied teacher questionnaire notes include provisional percentages that differ from the raw N=50 CSV (e.g., debates and values). Some notebooks use N=20 appendix data. This codebook treats CSV observed values as the operational schema and does not resolve that discrepancy. Maintain a source/version ledger before combining sources.
