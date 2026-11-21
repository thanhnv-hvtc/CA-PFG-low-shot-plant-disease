# Author release checklist — do not claim more than verified

- [x] Main results and statistics have been verified from bundled CSVs.
- [x] Supplied candidate-level validation records (NB10 and NB11) are bundled and audited.
- [x] Target manifest, 4 target metadata files, Oxford metadata and feature-cache SHA-256 index are bundled.
- [x] The five original `.npy` inputs have been identified and hash-checked.
- [ ] **Authors approve license** for source code; do not apply a license automatically.
- [ ] **Authors confirm redistributability** of derived image features and source metadata under dataset terms.
- [ ] Make external feature bundle public on approved Kaggle Dataset or Google Drive, if legally permitted.
- [ ] Insert genuine external dataset URL into `docs/EXTERNAL_DOWNLOAD_LINKS.md` and README.
- [ ] **Run at least one end-to-end task in a clean Kaggle runtime** using the public feature bundle; the complete set was run previously, but the portable-input public release has not yet been validated in a clean runtime.
- [ ] If making a full-reproduction claim, verify all 120 tasks and capture new run manifests; otherwise retain the stated limitations.
- [ ] Upload unpacked GitHub package contents to a new repository and validate that README/scripts/CSV links work without authentication.
- [ ] Insert real GitHub URL into manuscript Data Availability and response letter.
- [ ] Confirm author profiles, AI use disclosure, and title in journal manuscript separately.
