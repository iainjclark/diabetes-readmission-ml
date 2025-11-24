"""
preprocess.py

Impute missing values, convert categorical features to numeric encodings, scale numerical features, return cleaned DataFrame ready for modelling.
"""

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_impute_scale_encode(df):
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

    # Fit and transform the data
    transformed_array = preprocessor.fit_transform(df)

    # Get feature names
    feature_names = preprocessor.get_feature_names_out()

    # Return as DataFrame with original index
    return pd.DataFrame(transformed_array,
                            index=df.index,
                            columns=feature_names)

if __name__ == "__main__":  
    pass
