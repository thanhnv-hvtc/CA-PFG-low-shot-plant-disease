# Publishing the CA-PFG repository on GitHub (Windows)

The delivered archive is a **repository source ZIP**, NOT an archive for GitHub
to unpack automatically. Upload its **extracted contents**, not the ZIP itself.

## Option A: GitHub Desktop (recommended for Windows)

1. On github.com, create an empty **Public** repository named `CA-PFG-low-shot-plant-disease`.
   Do not initialize it with another README, `.gitignore`, or license.
2. Unzip `CA-PFG_GitHub_PUBLISH_v3.zip` and open the inner folder `CA-PFG_GitHub_PUBLISH_v3`.
3. Open GitHub Desktop → **File → Clone repository** and clone your newly created empty repo.
4. Copy the **contents** (README, `notebooks/`, `results/`, `metadata/`, `splits/`, `docs/`, `scripts/`, etc.)
   from the unzipped folder into the local clone folder. Do not copy the ZIP as a single file.
5. In GitHub Desktop, confirm `.npy`, `.rar`, dataset images or large caches are NOT staged.
6. Commit to main (e.g. `Initial verified CA-PFG research artifact`) and **Push origin**.
7. Open the repository URL and verify that `README.md` and `results/test/main_task_metrics_TEST_ONLY.csv` render.

## Option B: Git command line

Open a terminal **inside the unzipped top-level folder** and run:

```bash
git init
git add .
git status
git commit -m "Publish CA-PFG verified research artifact"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CA-PFG-low-shot-plant-disease.git
git push -u origin main
```

Create the remote repository first, empty. Authentication is via GitHub Desktop/CLI or Git Credential Manager;
do not put passwords or access tokens in the repository.

## Before posting the repository link to the journal

1. Run:

```bash
python -m pip install numpy pandas
python scripts/verify_release.py
python scripts/verify_input_metadata.py
python scripts/verify_candidates.py
```

2. Make a code-license decision with all authors; this package does **not** assume MIT or another license.
3. Review `docs/AUTHOR_FINAL_CHECKLIST.md`, particularly redistributing feature caches.
4. Put large frozen-feature caches in a separate Kaggle/Drive archive, if permitted; check download from a separate browser session.
5. Replace link placeholders with **real**, tested URLs. Do not invent a DOI or journal acceptance information.
6. Submit the corrected Data Availability statement and truthful disclosure of the validation/test correction.

GitHub browser upload limits: 25 MiB **per individual file**, 100 files per operation (as of Nov. 2026).
This source package contains fewer than 100 files and each individual file is below that per-file limit,
but GitHub Desktop is safer for preserving nested directories.
