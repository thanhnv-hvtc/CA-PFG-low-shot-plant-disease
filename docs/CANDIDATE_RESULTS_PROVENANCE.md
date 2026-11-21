# Candidate-level result provenance (Notebook 10/11)

These files were supplied as `Candidate.zip` after the first public-repository candidate was prepared.
They are **validation candidate tables**, not test summaries. The manuscript's Table 3/4
is reconstructed only from `results/test/main_task_metrics_TEST_ONLY.csv`.

| File | Rows | Tasks | Candidate records/task | Provenance |
|---|---:|---:|---:|---|
| `NB10_DINOv2_candidate_VALIDATION.csv` | 2,520 | 60 | 42 | Notebook 10 frozen confirmatory + exploratory variants |
| `NB11_ResNet50_candidate_VALIDATION.csv` | 1,080 | 60 | 18 | Notebook 11 backbone robustness |
| `NB11_frozen_config.json` | — | — | — | Frozen ResNet-50 configuration from Notebook 11 |
| `NB11_frozen_config_hash.txt` | — | — | — | Recorded configuration identifier |
| `NB11_completion_report.json` | — | 60 | — | Notebook 11 protocol completion report |

Notebook 10 contains `Reliability-v2` and `CF-Scale-NWLR-MO`, which are
**exploratory/controlled ablations** and are not a part of the four
principal variants in the revised manuscript. `PFG-NW` represents the candidate
pool used by both main normalized-influence selectors.

`selected_by` and `selected_as` are single text fields in the original outputs.
When both F1-only and MO select the same row, those fields do not always preserve
both selector names. Do **not** infer selector win counts from the number of
nonempty label strings alone. Refer to the selected task summaries and protocol audit.

Checks: `python scripts/verify_candidates.py`. This verifies schema, coverage,
grid and config consistency; it does not repeat candidate training.
