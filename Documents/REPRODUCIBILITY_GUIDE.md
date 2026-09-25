# Reproducibility Guide

## Repository layout and scope
Run commands from the repository root (the directory containing the data, notebooks, scripts, and `analysis_outputs/`). The supplied workspace included `Teachers_Data.csv`, `Students_Data.csv`, `Teacher_Stats.csv`, `Student_Stats.csv`, `Processed_Data_English.xlsx`, five numbered Jupyter notebooks (`01`–`05`), and `build_appendices.py`. No R (`.R`/`.Rmd`) scripts were present in the inspected workspace. Thus there is no project R entry point to document or execute; do not assume an R workflow exists. If one is added, record its file path, dependencies, inputs, and outputs here.

## 1. Establish the environment
Use Python 3.10+ (the notebooks use standard Python, pandas, NumPy, and Matplotlib). From repository root:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib jupyter ipykernel python-docx openpyxl
```

For stronger repeatability, pin the tested package versions in a project-owned requirements/lock file after validating the environment; none was present in the inspected files. Avoid installing unnecessary packages. `build_appendices.py` requires `python-docx`.

## 2. Validate raw CSVs before analysis
From the repository root, a minimal integrity check is:

```bash
python - <<'PY'
import pandas as pd
T = pd.read_csv('Teachers_Data.csv')
S = pd.read_csv('Students_Data.csv')
assert T.shape == (50, 7) and S.shape == (50, 3)
assert T.Teacher_ID.is_unique and S.Student_ID.is_unique
assert T.notna().all().all() and S.notna().all().all()
print(T.columns.tolist(), len(T), T['Preferred_Technique'].value_counts().to_dict())
print(S.columns.tolist(), len(S), S['Ethical_Talk_Frequency'].value_counts().to_dict())
PY
```

Check exact category sets against `DATA_DICTIONARY.md`, calculate item-specific totals, and save any cleaned/derived files to a separate output folder rather than replacing raw inputs.

## 3. Run the Jupyter notebooks
Launch Jupyter in the repository root so relative paths resolve:

```bash
jupyter lab
```

Execute notebooks in order only after reviewing the provenance caveat below:

1. `01_Data_Generation_and_Cleaning.ipynb` — generates appendix-style summary tables in `analysis_outputs/`.
2. `02_Wilson_Confidence_Intervals_and_SE.ipynb` — demonstrates SE and Wilson intervals.
3. `03_Publication_Figures_Generation.ipynb` — generates teacher/student figures under `analysis_outputs/`.
4. `04_Qualitative_Thematic_Coding_and_Audit.ipynb` — provides a proposed codebook/audit template and agreement-function smoke test.
5. `05_Comprehensive_Reproducibility_and_Verification.ipynb` — executes assertions and prints checksums for notebooks it finds in its current working directory.

Headless execution (requires `nbconvert`) may use:

```bash
python -m pip install nbconvert
jupyter nbconvert --to notebook --execute --inplace 01_Data_Generation_and_Cleaning.ipynb
```

Repeat for notebooks as needed. Be aware that `--inplace` changes notebook outputs and therefore changes its checksum; keep a clean source copy or execute to a distinct output path for archival runs.

### Critical provenance warning before reproducing figures
The available raw `Teachers_Data.csv` and `Students_Data.csv` each have N=50 and the observed summaries in `DATA_DICTIONARY.md`. Some notebooks instead contain constructed appendix data with denominator **20**, including extra variables/claims absent from the raw CSVs. In particular, notebooks `01`, `03`, and `05` are not a direct reproduction of the N=50 raw-data summary. Treat their outputs as separate appendix/demo artifacts until a documented reconciliation identifies source, selection, and denominators. Do not cite their N=20 graphics/tables as N=50 results. `02` also uses example item counts with n=20; its formulas are reusable, but its example values are not raw-file estimates. Notebook `04` states that project inter-rater reliability is not estimable without double-coded records; the included kappa test is synthetic only.

## 4. Python scripts and R scripts
`build_appendices.py` creates `Appendices_and_Questionnaires.docx` in its current working directory. Run only if that output is intended and back up any existing output first:

```bash
python build_appendices.py
```

The script is a document-generation utility, not the CSV statistical-analysis pipeline. No R scripts were present in the repository inspected for this guide; there are consequently no valid `Rscript ...` commands or package requirements to give. If R scripts are supplied later, run from root with `Rscript path/to/script.R` after installing documented dependencies and verify outputs against independent checks.

## 5. Independent statistical checks
Use the equations in `STATISTICAL_METHODS.md`. Validate edge cases `x=0` and `x=n`, check proportions and category totals, and compare output against counts in the data dictionary. For N=50 key checks: debates `23/50=46%`; videos `25/50=50%`; ethical talk most of the time `20/50=40%`; story theme `50/50=100%`. A Wilson interval at 100% must have upper bound exactly 1 and lower bound below 1.

## 6. Verify file checksums
A SHA-256 digest identifies exact file bytes. Run from repository root; store the manifest separately and refresh only when inputs are intentionally revised:

```bash
sha256sum Teachers_Data.csv Students_Data.csv > checksums.sha256
sha256sum -c checksums.sha256
```

On Windows PowerShell:

```powershell
Get-FileHash Teachers_Data.csv, Students_Data.csv -Algorithm SHA256
```

For notebooks, scripts, and outputs, list the exact filenames explicitly when producing a manifest. A checksum verifies byte identity, not scientific correctness, authorship, or the validity of a result. Do not hash a file while another process is modifying it. Keep raw-input hashes, software versions, command lines, timestamp, and output hashes with each release.

## 7. Verify output artifacts
- Confirm each expected file exists, has nonzero size, and opens (e.g., parse CSV with pandas, notebook as JSON, generated DOCX with `python-docx`, figures with an image viewer).
- Verify table dimensions, category enumerations, and totals against raw source counts.
- Inspect plots for denominator labels and ensure they match the dataset actually used.
- Keep generated files in `analysis_outputs/` and preserve the raw inputs. Never regard a successful notebook execution alone as confirmation that an output is based on the correct cohort.

## 8. Recommended run record
For each reproducible run, record Git commit (if applicable), Python/R and package versions, OS, input SHA-256 values, executed command/notebook order, random seeds (if used), output filenames and hashes, and any exclusions or cleaning. The supplied notebooks’ outputs may contain pre-existing execution history; clear/re-execute in a clean environment for a controlled run, while preserving the original notebooks and their checksums.
