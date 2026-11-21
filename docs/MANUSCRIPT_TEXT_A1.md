# Text for the revised manuscript (A1)

## Where to cite Oxford Flowers 102 [24]

The first appearance of Oxford in **Section 4.6** already cites **[24]**. Keep this citation. Add the same dataset reference in the **Data Availability Statement**, specifying that Oxford serves as a source dataset for the adapted DC baseline only.

**Replace the existing Data Availability Statement with the following, after the repository is public:**

> The PlantDoc (cropped) and PlantVillage image datasets used for target-task evaluation are publicly sourced and are described in [20] and [21], respectively. The Oxford Flowers 102 dataset [24], available from the Visual Geometry Group at the University of Oxford (https://www.robots.ox.ac.uk/~vgg/data/flowers/102/), was used solely to estimate auxiliary labeled source-class statistics for the adapted Distribution Calibration baseline; it was not used to train or select the proposed CA-PFG classifiers. The evaluation uses the specified preprocessing, fixed target validation and test splits, and matched low-shot support tasks. Source code, experiment configurations, task manifests, and task-level results for the revised analyses are available at **[INSERT VERIFIED PUBLIC GITHUB REPOSITORY URL]**. Original dataset images and pretrained model weights are not redistributed; their use remains subject to the relevant providers' terms.

**Important:** The text above presumes that manifests/configuration files really have been added to the public repository. If they have not, change the sentence to explicitly describe the missing pieces instead of claiming release completeness.

If the authors are not yet ready to publish the full files, retain a truthful *available upon reasonable request* statement and separately disclose the public subset after it exists. Never insert a speculative or unused GitHub URL.

**Minimal supplementary addition in Section 4.6, if desired:**

> All 8,189 labeled Oxford images were used as auxiliary source data for estimating the adapted DC base-class statistics; the original Oxford data splits were not treated as target-task evaluation splits. No Oxford images or labels were used in the support-only CA-PFG configuration.
