# Diabetes Readmission ML Project

A modular, reproducible ML project for analysing 30-day readmission risk in diabetic patients, combining interpretable models with clear feature insights 
to support evidence-based operational decisions in clinical settings.
  
---

## Environment Setup

### Using Mamba (recommended)
```bash
mamba env create -f environment.yml
conda activate diabetes-readmission-ml
```
### After setting up the virtual environment (recommended)
```
python scripts/version_check.py
```
This confirms that installed packages match the pinned versions.

### Initial directory structure
```
diabetes-readmission-ml/
├── notebooks/
├── src/
├── scripts/
│   └── version_check.py
├── environment.yml
├── requirements.txt
└── README.md
```
