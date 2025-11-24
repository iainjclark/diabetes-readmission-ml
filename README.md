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
### Verify Package Versions within the Virtual Environment (optional; highly recommended)
```
python scripts/version_check.py
```
This confirms that installed packages match the pinned versions.

### Enable Jupyter Notebook Support (optional; recommended)
```
conda activate diabetes-readmission-ml
mamba install -c conda-forge notebook
python -m pip install ipykernel ipywidget
python -m ipykernel install --user --name diabetes-readmission-ml --display-name "Python (diabetes-readmission-ml)"
jupyter notebook
```
A notebook called version_check.ipynb is provided within notebooks/ and serves as a good starting 
point to verify that your environment is functioning correctly.

### Initial Directory Structure
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


