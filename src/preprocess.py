"""
preprocess.py

Impute missing values, convert categorical features to numeric encodings, scale numerical features, return cleaned DataFrame ready for modelling.
"""

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_impute_scale_encode(df, target_col):
    """
    Given a raw DataFrame, apply preprocessing steps:
      - impute missing values
      - scale numerical features, convert categorical features to numeric encodings 
    Returns a cleaned DataFrame ready for modelling.
    """
    # Identify numeric & categorical columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    numeric_cols = [col for col in numeric_cols if col != 'rowID']

    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Define preprocessing for numeric features
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # --- Fix mixed-type categorical data ---

    # Replace literal question marks with NaN
    df = df.replace('?', np.nan)

    # Ensure all categorical columns are strings (to avoid mixed types)
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str)    

    # Define preprocessing for categorical features
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Combine transformers into a ColumnTransformer
    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

    y = df[target_col].copy()
    df = df.drop(columns=[target_col], errors='ignore')

    # Fit and transform the data
    transformed_array = preprocessor.fit_transform(df)

    # Get feature names
    feature_names = preprocessor.get_feature_names_out()

    # Return as DataFrame with original index
    df_preprocessed = pd.DataFrame(transformed_array,
                            index=df.index,
                            columns=feature_names)
    
    # Reattach target column
    df_preprocessed[target_col] = y

    return df_preprocessed


if __name__ == "__main__":  
    pass
