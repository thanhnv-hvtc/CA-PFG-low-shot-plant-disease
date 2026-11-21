# Validation/test correction record

The original submitted Tables 3–4 were assembled from metrics assigned by a normalizer that prioritized generic `macro_f1`, `nll`, `ece`, and `brier` column names. In the original input these generic columns reflected **validation** outcomes, although `test_macro_f1`, `test_nll`, `test_ece`, and `test_brier` were present.

**Correction:** Notebook 12 v3 was explicitly restricted to held-out `test_*` columns, with independent cross-checks against the Notebook 14 results. The revised manuscript Tables 3–4 and Figures 2–3 use the corrected test results. The method/task splits and trained models were not retrospectively selected by inspecting test metrics.

Source files:
- `notebooks/12_test_corrected_statistics.ipynb`
- `results/test/main_task_metrics_TEST_ONLY.csv`: curated test-only columns, 480 rows.
- `results/test/audit_original_task_metrics_VALIDATION_AND_TEST.csv`: original corrected output with **both** validation and test columns for provenance (generic `macro_f1/nll/ece/brier` aliases equal test columns in this corrected export).

Do not mix validation-only tolerance sensitivity with the held-out confirmatory testing family. An explicit correction explanation should accompany the revision response to the journal.
