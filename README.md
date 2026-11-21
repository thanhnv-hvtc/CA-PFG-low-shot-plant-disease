# CA-PFG — reproducibility research artifact

**Manuscript:** *CA-PFG: Calibration-Aware Probabilistic Feature Generation with Normalized Synthetic Influence Control for Low-Shot Plant Disease Classification.*  
**Status:** Manuscript under revision for IJITCS (not accepted or assigned a DOI at the time this archive was prepared).

This repository contains the **research notebook sources supplied for this release**, corrected held-out **test** results, independent external-DC follow-up results, statistical audits, and code to verify the key published summaries. The frozen encoders are DINOv2-Small and ResNet-50; the target datasets are PlantDoc (cropped) and PlantVillage.

## Reproducibility levels (what is actually possible)

| Level | Inputs | Current status |
|---|---|---|
| A. Verify Tables 3, 4, 6 and task counts | Bundled CSVs | **Ready**; run `python scripts/verify_release.py` |
| B. Regenerate Figures 2–3 | Bundled `results/test/main_task_metrics_TEST_ONLY.csv` and Notebook 16 | **Ready** in Kaggle; ready-to-use PNGs in `figures/` |
| C. Re-run all low-shot tasks from frozen features | Notebook 10/11, split manifest and `.npy` caches | **Manifest and portable metadata verified; feature caches are linked via the author-provided Kaggle Dataset (access/file inventory requires a public check)** |
| D. End-to-end re-extraction from original images | Raw datasets, original image-path metadata, model versions | Requires downloading data from its rights holders and following notebook instructions |

This GitHub source-code repository does not itself contain the large `.npy` feature arrays; attach the author-held caches separately. The **original manifest has been obtained and audited**, and its portable public representation in `splits/manifest_split.csv` retains the exact sample IDs, class IDs, splits and SHA-1 values while omitting Kaggle-specific absolute paths. Full experimental reruns using the published portable files have **not yet been tested in a fresh Kaggle session**.

## Feature caches (hosted separately on Kaggle)

**Author-provided dataset:** [https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches](https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches)

The large `.npy` arrays for PlantDoc and PlantVillage (DINOv2-Small and ResNet-50), and the Oxford Flowers 102 ResNet-50 auxiliary cache, are intentionally stored outside GitHub. The intended cache inventory, dimensions, and SHA-256 checksums are documented in `docs/FEATURE_CACHE_INDEX.json`. **The dataset's public visibility, exact directory layout and uploaded file hashes have not yet been independently verified.**

To inspect the mounted Kaggle Dataset without modifying the research data, create a new Kaggle Notebook, use **Add Input** to attach `capfg-feature-caches`, add `docs/FEATURE_CACHE_INDEX.json` if running the repository script outside the repository, and run:

```bash
python scripts/verify_kaggle_feature_caches.py --root /kaggle/input
# Optional strict check (reads all five large arrays):
python scripts/verify_kaggle_feature_caches.py --root /kaggle/input --full-hash
```

See `docs/FEATURE_INPUTS_GUIDE.md` for expected file names. Do not re-sort feature rows when using the task manifests. The raw original image datasets remain under their respective source providers' terms.

## Minimal verification (no Kaggle GPU required)

```bash
python -m pip install numpy pandas
python scripts/verify_release.py
```

This checks 480 matched method–backbone task rows, 60 tasks per backbone, 60 fixed-C DC rows, 300 external-DC validation candidates, 120 post-selection test outcomes, and the descriptive manuscript values. All test-table reconstruction uses columns starting with `test_`.

## Notebook execution order

1. `notebooks/10_confirmatory_DINOv2.ipynb`: initial DINOv2 feature-generation comparison (requires DINOv2 target feature caches, target metadata, split manifest).
2. `notebooks/11_resnet50_robustness.ipynb`: ResNet-50 target feature extraction/evaluation (requires image data or precomputed ResNet caches, target metadata, and split manifest).
3. `notebooks/12_test_corrected_statistics.ipynb`: corrected matched-task test statistics.
4. `notebooks/14_reviewer_posthoc_analysis.ipynb`: exploratory robustness, sensitivity and failure-task analysis.
5. `notebooks/15_dc_adapted_oxford102.ipynb`: external DC adapted to frozen ResNet-50 and source statistics from Oxford Flowers 102; compare 60 target tasks.
6. `notebooks/15b_dc_validation_C_sensitivity.ipynb`: validation-only C-selection of adapted DC; intended grid `[0.01,0.1,1,10,100]` (corrected v1.2).
7. `notebooks/16_figures_2_3_test_corrected.ipynb`: Figure 2 and Figure 3 using corrected held-out test data.

For publication, **do not use Notebook 12 v2**: it selected validation results for the original Tables 3–4. The corrected Notebook 12 v3 and `results/test` files are authoritative for the revised manuscript; see `docs/VALIDATION_TEST_CORRECTION.md`.

## Data usage and limitations

- **Target**: PlantDoc cropped, 27 classes, 8,887 usable images; PlantVillage, 38 classes, 54,284 images.
- **Task protocol**: 5-, 10-, 20-shot; 10 support seeds per dataset–shot; 60 matched tasks per backbone.
- **Auxiliary source**: Oxford Flowers 102, 8,189 labeled source images across 102 classes for **DC-Adapted-Oxford102 only**. All 8,189 images are used as auxiliary source statistics, not as a target held-out test set. Source data are external to the two target datasets; **image-level overlap has not been verified by hashing**.
- **Primary CA-PFG** does not use Oxford labels or Oxford image statistics. The support-only claim refers to target-task distribution fitting; validation is used for configuration selection.
- **DC-Adapted** is a cross-domain adaptation of Distribution Calibration, not a reproduction of the original ICLR 2021 benchmark. It uses additional labeled auxiliary source information not available to CA-PFG and a different classifier configuration-selection budget.
- Published counts from independent paper datasets must not be confused with this manuscript's specific preprocessed counts.

Download datasets from their original sources. No raw images, unpublished original image paths, credentials or backbone model weights are included. See `docs/DATA_SOURCES_AND_RIGHTS.md`.

## Scientific provenance

The original feature-row ordering of both backbones has been cross-checked against the manifest and each other for all 63,171 target examples. The Oxford ResNet-50 cache hash matches Notebook 15 provenance. Feature arrays are intentionally kept out of this GitHub source package.

The bundled corrected test file **was assembled from the original Notebook 12 output**. `results/test/audit_original_task_metrics_VALIDATION_AND_TEST.csv` intentionally retains validation and test columns for error tracing; use `main_task_metrics_TEST_ONLY.csv` for the manuscript evaluation. The 12 main tests are paired by dataset–shot–seed and Holm adjusted; the DC comparison is exploratory, not included in the confirmatory family.

Figures 2–3 and Table 6 are post-revision outputs. Avoid treating repeated support-seed tasks sharing fixed test sets as 60 independent unseen domains.

## Release checklist

Consult `docs/MISSING_BEFORE_FULL_REPRODUCTION.md` for remaining conditional items, verify the source dataset licenses and add a license only after the authors choose one. Source modules reconstructed from the manuscript were deliberately excluded from this archive because exact parity with successful notebooks has not yet been demonstrated. The **actual notebook code** is present.

Public GitHub repository URL and publication DOI: **add only after they exist and have been verified**. The repository is currently being prepared for public release.

## Verified original inputs (revision v2)

This release now includes:

- `splits/manifest_split.csv`: exact original sample membership (63,171 rows), portable redacted representation;
- `metadata/dinov2_small/*.csv` and `metadata/resnet50/*.csv`: feature-row-aligned target metadata;
- `metadata/oxford102/oxford102_metadata.csv`: 8,189 source items, 102 classes, relative image paths;
- `docs/FEATURE_CACHE_INDEX.json`: original feature `.npy` member paths, shapes and SHA-256 checksums, plus source archive hashes;
- `scripts/verify_input_metadata.py`: checks that the manifest and all five metadata files have correct labels, splits and ordering.

**Arrays remain separate from the Git repository.** The author has created a Kaggle Dataset for the feature caches. Its access permissions, license, and five file hashes should be checked before citing it as a public reproduction artifact. To reproduce the original tasks, attach the `.npy` arrays with their unmodified row ordering.

No Oxford-target image-level duplicate audit has been completed, and no end-to-end fresh model re-run is claimed.

## Candidate-level validation files (confirmed additions)

`Candidate.zip` was supplied after version 2. This version includes 2,520
candidate-validation rows from Notebook 10 and 1,080 from Notebook 11,
with Notebook 11 frozen config, hash and completion report.
See `docs/CANDIDATE_RESULTS_PROVENANCE.md` and run
`python scripts/verify_candidates.py`. The additional `Reliability-v2` and
`CF-Scale-NWLR-MO` candidates are **not** principal methods of the paper.

## External feature bundle (separate from GitHub)

The authors have provided a Kaggle Dataset URL: [https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches](https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches).
**Public accessibility and the exact file listing have not yet been independently verified**; see `docs/EXTERNAL_DOWNLOAD_LINKS.md` and run the cache-verification script in a Kaggle notebook. If the dataset is Private, switch sharing to Public only after checking data-use terms and removing unnecessary raw source data. It contains no raw dataset images. The fact that
feature arrays were generated does not in itself grant a right to redistribute
them; authors must confirm dataset-source terms. See
`docs/EXTERNAL_FEATURES_UPLOAD_VI.md`, `docs/EXTERNAL_DOWNLOAD_LINKS.md`
and `docs/REPRODUCIBILITY_MATRIX.md`.

**Uploading the GitHub ZIP file itself as one repository file does not unpack
it.** Unzip on your computer, then add the extracted repository contents
with Git / GitHub Desktop (or GitHub browser folder upload).
