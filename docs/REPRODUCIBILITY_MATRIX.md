# Reproducibility matrix

| Task | Public GitHub release | External data bundle | Evidence level |
|---|---|---|---|
| Verify manuscript Table 3/test averages | `results/test`, `scripts/verify_release.py` | Not needed | **Executed and verified** |
| Verify test component effects and DC results | `results/test`, `results/external_dc_*` | Not needed | **Executed and verified** |
| Audit candidate grids and Notebook 11 config | `results/candidates`, `scripts/verify_candidates.py` | Not needed | **Executed and verified** |
| Verify target sample IDs and feature-row metadata | `splits/`, `metadata/`, `scripts/verify_input_metadata.py` | Not needed | **Executed and verified** |
| Regenerate Figures 2–3 | Notebook 16 plus `results/test` | Not needed | Notebook syntax/figure files reviewed; user-side fresh Kaggle run not claimed |
| Refit support-only classifiers on frozen features | NB10/NB11 plus manifest/metadata | **Five `.npy` caches** | Inputs available; full clean-runtime rerun **not yet performed** |
| Refit DC-Adapted, validation C tuning | NB15/NB15b | Oxford + target ResNet-50 `.npy` | Inputs available; full clean-runtime rerun **not yet performed** |
| Extract features again from raw images | Original datasets, model downloads, notebooks | Original raw images / weights | **Not packaged**; data holder licenses apply |

No image-level SHA hash overlap audit between Oxford and the two target image sets has been completed.
The 60 tasks within a dataset reuse the fixed held-out test split, varying support seeds.
