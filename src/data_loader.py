"""
data_loader.py

Minimal utility for loading the diabetes readmission dataset from data/interim/.
"""

import os
import pandas as pd

INTERIM_DIR = "data\\interim"
DIABETES_DATA_CSV = "10kDiabetes.csv"

def load_diabetes_csv(filename, project_root=''):
    """
    Load the extracted diabetes dataset CSV from data/interim/.
    """
    csv_path = os.path.join(project_root, INTERIM_DIR, filename)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    return pd.read_csv(csv_path)


if __name__ == "__main__":
    try:
        df = load_diabetes_csv(DIABETES_DATA_CSV)
        print(df.head())
        
        print("\nLoaded dataset shape:", df.shape)
    except Exception as e:
        print(f"Error loading dataset: {e}")
