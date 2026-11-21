# Research notebook provenance

| Notebook | Source file from the research workflow | Current package file | Validation status |
|---|---|---|---|
| 10 | CAPFG_10_Frozen_Confirmatory_Evaluation.ipynb | notebooks/10_confirmatory_DINOv2.ipynb | notebook syntax/structure reviewed; **not re-run here** |
| 11 | CAPFG_11_Backbone_Robustness_ResNet50_v1_2.ipynb | notebooks/11_resnet50_robustness.ipynb | notebook syntax/structure reviewed; **not re-run here** |
| 12 v3 | GAPFA_12_v3_Test_Corrected_Statistical_Analysis.ipynb | notebooks/12_test_corrected_statistics.ipynb | corrected CSV output audited against the manuscript |
| 14 | CAPFG_14_Reviewer_Minimal_Posthoc_Analysis_with_ZIP.ipynb | notebooks/14_reviewer_posthoc_analysis.ipynb | ZIP output and audit summaries present |
| 15 v1.1 | CAPFG_15_External_DC_Adapted_Baseline_v1_1_InputFix.ipynb | notebooks/15_dc_adapted_oxford102.ipynb | output from successful 60-task run present |
| 15b v1.2 | CAPFG_15b_v1_2_Full_CGrid_AssertFix.ipynb | notebooks/15b_dc_validation_C_sensitivity.ipynb | corrected grid and count assertions; output from successful 60-task run present |
| 16 | CAPFG_16_Figure2_Figure3_Test_Corrected.ipynb | notebooks/16_figures_2_3_test_corrected.ipynb | figure PNGs and results present |

All notebooks were stripped of outputs/execution counts and nonessential local notebook metadata for public distribution. Their **code cells were not rewritten** as part of this packaging. No notebook was run on GPU or a Kaggle-hosted runtime by the packaging process. Original feature caches, raw images, and original split manifests are not present in this package.

A separate earlier *modular reimplementation* was deliberately excluded: scientific parity with the successful original research notebooks had not been established, and publishing it as the official source could have undermined reproducibility.
