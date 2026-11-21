# Missing inputs and final author actions

## 1. Updated data-artifact status (validated 2026-11-21)

- [x] Exact `manifest_split.csv` received; public copy omits Kaggle absolute/mounted paths.
- [x] DINOv2-Small and ResNet-50 feature metadata received and aligned by `image_id`, `sha1`, `class_id`, split and feature row for **all 63,171 images**.
- [x] DINOv2 and ResNet-50 target `.npy` caches have been received in source archives; **not included in public source-code ZIP**.
- [x] Oxford102 ResNet-50 feature `.npy` and source metadata received. Feature SHA-256 matches Notebook 15 provenance.
- [x] Notebook 10/11 candidate-level validation records and Notebook 11 frozen config/completion report received from Candidate.zip and audited. Full candidate predictions are not included.
- [ ] Decide the legally permitted distribution channel for large derived feature arrays; add public artifact links and optionally record checksums in a release.
- [ ] Optionally verify cross-source image identity/near-duplicate overlap using actual images; **not performed**.
- [ ] Test a fresh Kaggle run using the public portable manifest and attached private `.npy` feature caches.

The repository verifies CSV results and metadata integrity; it is **not claimed to be an end-to-end fresh run from images**.

## 2. Before publishing the GitHub release

- [ ] Confirm publication repository slug and choose a public code license with all authors.
- [ ] Confirm that the original Kaggle notebooks (especially 10/11) match the version used to obtain the reported results.
- [ ] Run `python scripts/verify_release.py` successfully.
- [ ] If producing model/feature caches from scratch, document exact encoder weights, preprocessing, package versions and random seeds; capture Kaggle environment export.
- [ ] Review notebook inputs and notes for privacy or accidental user-specific paths; no personal Kaggle input files should be committed.
- [ ] Fill the GitHub URL in the manuscript **only after the repository is live** and revision artifacts have been verified.
- [ ] Optionally deposit a versioned release to an archive service and cite its permanent identifier when actually available.
