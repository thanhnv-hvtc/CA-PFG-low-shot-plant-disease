# Verified input data and recommended Kaggle layout

The validated original files provided by the authors are:

| Artifact | Original container | Dimensions | Included in GitHub code ZIP? |
|---|---|---:|---|
| DINOv2 PlantDoc | `features_DINOv2.rar` | 8,887 × 384 | No (large array) |
| DINOv2 PlantVillage | `features_DINOv2.rar` | 54,284 × 384 | No (large array) |
| ResNet-50 PlantDoc | `features_ResNet50.zip` | 8,887 × 2,048 | No (large array) |
| ResNet-50 PlantVillage | `features_ResNet50.zip` | 54,284 × 2,048 | No (large array) |
| Oxford102 ResNet-50 | `oxford102_resnet50_features.npy` | 8,189 × 2,048 | No (large array) |

SHA-256 values are in `FEATURE_CACHE_INDEX.json`.

**Kaggle feature dataset:** https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches

**Important:** This link was supplied by the authors; visibility and actual file layout still require verification. The `scripts/verify_kaggle_feature_caches.py` script searches nested directories to accommodate differing Kaggle mount layouts.

## Layout to attach to Kaggle

Place files in a Kaggle Dataset (read-only input) or equivalent accessible location:

```text
input-artifacts/
  manifest_split.csv
  plantdoc_features.npy
  plantvillage_features.npy
  plantdoc_metadata.csv
  plantvillage_metadata.csv
  plantdoc_resnet50_features.npy
  plantvillage_resnet50_features.npy
  plantdoc_resnet50_metadata.csv
  plantvillage_resnet50_metadata.csv
  oxford102_resnet50_features.npy
  oxford102_metadata.csv
```

**Important:** Some notebook versions prefer basename discovery and will choose the first match if ambiguous. When both DINOv2 and ResNet-50 metadata coexist, use their exact distinct filenames, or specify `MANUAL`/`MANUAL_PATHS` where available. Original row order must not be sorted.

The `splits/manifest_split.csv` and sanitized metadata in this repository preserve exact sample keys and splits, but replace absolute Kaggle paths with relative paths. Feature-based re-runs work with the attached caches; from-image re-extraction requires mounting the actual source images and adapting path resolution to that mount. Do not claim that raw-image re-extraction was demonstrated from this release.

## Security and provenance

Original authors' local Kaggle absolute paths are intentionally excluded from the public `splits/` and `metadata/` directories. This is a **portable metadata copy**, not byte-for-byte the same as the author's original CSV files. See `FEATURE_CACHE_INDEX.json` for original-file checksums.

The Oxford `image_path` values have the form `jpg/image_XXXXX.jpg` and refer to files inside the official Oxford Flowers 102 data directory. CA-PFG does not use Oxford-derived statistics; Oxford is only for the DC-Adapted baseline.

## Quick Kaggle inspection

In a Kaggle Notebook with the dataset attached, paste:

```python
from pathlib import Path
import numpy as np
for name in [
    "plantdoc_features.npy", "plantvillage_features.npy",
    "plantdoc_resnet50_features.npy", "plantvillage_resnet50_features.npy",
    "oxford102_resnet50_features.npy",
]:
    matches=list(Path("/kaggle/input").rglob(name))
    print(name, [(str(p), np.load(p, mmap_mode="r").shape) for p in matches])
```

The command reports paths and shapes only; it does not establish the provenance of the arrays. For that, compare SHA-256 hashes with `FEATURE_CACHE_INDEX.json`.
