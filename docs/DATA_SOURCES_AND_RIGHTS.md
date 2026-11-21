# Datasets, source statistics, licensing and attribution

| Dataset | Manuscript reference | Role in this work | Source |
|---|---|---|---|
| PlantDoc (cropped) | [20] D. Singh et al., *PlantDoc: A Dataset for Visual Plant Disease Detection* (2020) | 27 target classes; target support, validation, held-out test | See paper and original dataset repository; precise cropping/manifest must be supplied by authors |
| PlantVillage | [21] D. P. Hughes and M. Salathé (2015) | 38 target classes; target support, validation, held-out test | See original publication/repository |
| **Oxford Flowers 102** | **[24] M.-E. Nilsback and A. Zisserman, *Automated Flower Classification over a Large Number of Classes*, ICVGIP 2008** | **102 labeled auxiliary source classes, 8,189 images used solely for adapted Distribution Calibration source statistics** | **https://www.robots.ox.ac.uk/~vgg/data/flowers/102/** |

**Oxford implementation:** The released `notebooks/15_dc_adapted_oxford102.ipynb` uses the Oxford archive of flower images plus `imagelabels.mat` and computes source-class statistics with frozen ResNet-50 features. The original Oxford train/validation/test division is **not** the PlantDoc/PlantVillage evaluation split. In this experiment, all 8,189 labeled Oxford images are source data; no Oxford images serve as target held-out evaluation examples. The use of Oxford is specific to DC-Adapted, **not** the proposed support-only CA-PFG main model.

The original Oxford project page describes the dataset and available files but is not a blanket license for redistribution. **Do not include the Oxford, PlantDoc or PlantVillage raw images in this repository** before confirming legal redistribution terms. Likewise, pretrained model weights are not redistributed. Derived feature caches can be stored off-Git (author-controlled archive) after reviewing terms. The source protocol audit records that Oxford–target image-hash overlap was **not** checked, so do not claim verified instance-level non-overlap.

Dataset reference [24] is already used by Section 4.6 of the revised manuscript; the Data Availability Statement should ALSO cite [24] and link to the official page.
