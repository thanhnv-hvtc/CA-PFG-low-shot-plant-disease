# External feature caches — author-provided Kaggle Dataset

Dataset URL: https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches

**Status:** The author supplied this Kaggle Dataset link. The public page and exact file listing could not be independently retrieved during this review. Confirm that it is set to **Public** (if redistribution is permitted), and verify that all five `.npy` caches are present using the companion script before referring to it as a publicly available reproducibility resource.

## Expected array inventory

| Backbone | Dataset | Expected cache filename | Shape |
|---|---|---|---|
| DINOv2-Small | PlantDoc | `plantdoc_features.npy` | `(8887, 384)` |
| DINOv2-Small | PlantVillage | `plantvillage_features.npy` | `(54284, 384)` |
| ResNet-50 | PlantDoc | `plantdoc_resnet50_features.npy` | `(8887, 2048)` |
| ResNet-50 | PlantVillage | `plantvillage_resnet50_features.npy` | `(54284, 2048)` |
| ResNet-50 | Oxford Flowers 102 | `oxford102_resnet50_features.npy` | `(8189, 2048)` |

**Checksum reference:** `docs/FEATURE_CACHE_INDEX.json`. Use `scripts/verify_kaggle_feature_caches.py --root /kaggle/input --full-hash` to confirm file identity. If the caches are archived, Kaggle often extracts ZIP archives automatically but paths may retain nested folders. The script searches recursively.

Original PlantDoc, PlantVillage and Oxford images are not part of this cache release. Verify the underlying datasets' license/terms before choosing a license for derived features. Do not claim an independent Oxford-target image-hash overlap audit; it has not been performed.

## Remaining owner checks

- [ ] Dataset visibility is Public (or the manuscript accurately states restricted access).
- [ ] The five feature files, expected dimensions and SHA-256 checksums match.
- [ ] Metadata are available from this GitHub repository and can be paired with the feature arrays.
- [ ] Dataset license/description are compatible with sharing derived features.
- [ ] Public GitHub repository link is confirmed after switching it from Private.
