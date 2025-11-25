"""
extract_diag.py

Extract whatever information we can from the diag_1, diag_2, diag_3 attributes, return cleaned DataFrame ready for modelling.
"""

import os
import pandas as pd

def normalize_icd(code):
    """
    Normalise ICD-9 code into one of:
      - integer parent for numeric codes
      - original string for V/E codes
      - None otherwise
    """
    if pd.isna(code):
        return None
    
    code = str(code).strip()
    if code.startswith(("V", "E")):
        return code
    try:
        return int(float(code)) # Note you can't go directly to int as int('250.01') will fail. Hence the double-tap.
    except Exception:
        return None

def extract_diag_features(diag):
    """
    Given a sequence of ICD-9 diagnostic codes
    normalise them and extract:
      - parent codes
      - V/E flags
      - diagnostic count
    """
    # Normalise all codes
    norm = [normalize_icd(code) for code in diag]

    # Flags
    has_V = int(any(isinstance(c, str) and c.startswith("V") for c in norm))
    has_E = int(any(isinstance(c, str) and c.startswith("E") for c in norm))

    # Unique non-null trunks/codes
    diag_count = len({c for c in norm if c is not None})

    # parent codes expand naturally
    parents = {
        f"diag_{i+1}_norm": norm[i] for i in range(len(norm))
    }

    # return everything together
    return {
        **parents,
        "has_V": has_V,
        "has_E": has_E,
        "diag_count": diag_count,
    }

def preprocess_extract_diag(df, target_col):
    """
    Given a raw DataFrame, apply preprocessing steps:
    - Extract reduced information from the diag_1, diag_2, diag_3 attributes
    Returns a cleaned DataFrame ready for modelling.
    """

    diag_cols = ["diag_1", "diag_2", "diag_3"]

    # Apply feature extractor row-wise
    feats_series = df[diag_cols].apply(
        lambda row: extract_diag_features(row.tolist()),
        axis=1
    )

    # Convert list-of-dicts into a DataFrame
    feats_df = pd.DataFrame(feats_series.tolist())

    # Concatenate and clean up
    df = pd.concat([df, feats_df], axis=1)

    # Optional: drop originals
    df = df.drop(columns=diag_cols)

    return df


if __name__ == "__main__":  
    pass
