"""
Data Preprocessing Module for Disease PredictionIQ
Handles data loading, cleaning, and preparation for modeling
Author: Jay Prakash
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def load_data(filepath):
    """
    Load the heart disease dataset from CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully. Shape: {df.shape}")
    return df


def check_data_quality(df):
    """
    Perform initial data quality checks.
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        dict: Dictionary with data quality metrics
    """
    quality_report = {
        'shape': df.shape,
        'missing_values': df.isnull().sum().sum(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes.value_counts().to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # in MB
    }
    
    print("\n=== Data Quality Report ===")
    print(f"Shape: {quality_report['shape']}")
    print(f"Missing values: {quality_report['missing_values']}")
    print(f"Duplicate rows: {quality_report['duplicates']}")
    print(f"Memory usage: {quality_report['memory_usage']:.2f} MB")
    
    return quality_report


def get_descriptive_statistics(df):
    """
    Generate descriptive statistics for the dataset.
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        pd.DataFrame: Descriptive statistics
    """
    stats = df.describe()
    print("\n=== Descriptive Statistics ===")
    print(stats)
    return stats


def preprocess_data(df, target_column='heart_disease', test_size=0.2, random_state=42):
    """
    Preprocess the dataset for model training.
    
    Steps:
    1. Separate features and target
    2. Scale features using StandardScaler
    3. Split into training and testing sets
    
    Args:
        df (pd.DataFrame): Input dataset
        target_column (str): Name of target column
        test_size (float): Proportion of data for testing
        random_state (int): Random seed for reproducibility
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test, feature_names, scaler)
    """
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    feature_names = X.columns.tolist()
    print(f"\nFeatures ({len(feature_names)}): {feature_names}")
    print(f"Target distribution:\n{y.value_counts()}")
    print(f"Target proportion - Class 0: {(y == 0).sum()/len(y)*100:.1f}%, Class 1: {(y == 1).sum()/len(y)*100:.1f}%")
    
    # Split the data (80/20 split)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=test_size,
        random_state=random_state,
        stratify=y  # Preserve class distribution
    )
    
    print(f"\nData split:")
    print(f"Training set size: {X_train.shape[0]} ({X_train.shape[0]/len(df)*100:.1f}%)")
    print(f"Testing set size: {X_test.shape[0]} ({X_test.shape[0]/len(df)*100:.1f}%)")
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to DataFrames for easier handling
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=feature_names, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=feature_names, index=X_test.index)
    
    print("\nFeature scaling completed using StandardScaler")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, feature_names, scaler


def get_feature_correlations(df, target_column='heart_disease'):
    """
    Calculate correlations between features and target variable.
    
    Args:
        df (pd.DataFrame): Input dataset
        target_column (str): Name of target column
        
    Returns:
        pd.Series: Correlation values sorted by absolute value
    """
    correlations = df.corr()[target_column].drop(target_column).sort_values(ascending=False)
    print("\n=== Feature Correlations with Target ===")
    print(correlations)
    return correlations
