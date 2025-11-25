import os
import pandas as pd
from src.data_loader import load_diabetes_csv

INTERIM_DIR = os.path.join("data", "interim")

def test_csv_exists():
    """Ensure the CSV file is present in data\interim"""
    files = os.listdir(INTERIM_DIR)
    assert any(f.endswith(".csv") for f in files), "No CSV file found in data\\interim"

def test_load_csv():
    """Ensure the CSV loads correctly as a pandas DataFrame."""
    # Find the CSV file in interim dir
    csv_files = [f for f in os.listdir(INTERIM_DIR) if f.endswith(".csv")]
    assert len(csv_files) > 0, "No CSV file to load."

    df = load_diabetes_csv(csv_files[0])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0, "Loaded DataFrame is empty."
    print(f"Loaded file {csv_files[0]} DataFrame shape: {df.shape}")