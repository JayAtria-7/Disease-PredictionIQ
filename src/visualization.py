"""
Visualization Module for Disease PredictionIQ
Creates visualizations for EDA and model evaluation
Author: Jay Prakash
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc
import os


def setup_plot_style():
    """Configure matplotlib and seaborn for consistent styling."""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_target_distribution(y, filepath=None):
    """
    Visualize the distribution of the target variable.
    
    Args:
        y (pd.Series): Target variable
        filepath (str): Optional path to save the figure
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Count plot
    counts = y.value_counts()
    colors = ['#2ecc71', '#e74c3c']
    axes[0].bar(['No Disease', 'Disease'], counts.values, color=colors)
    axes[0].set_title('Target Variable Distribution (Count)', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Count')
    for i, v in enumerate(counts.values):
        axes[0].text(i, v + 5, str(v), ha='center', fontweight='bold')
    
    # Pie chart
    axes[1].pie(counts.values, labels=['No Disease', 'Disease'], autopct='%1.1f%%',
                colors=colors, startangle=90)
    axes[1].set_title('Target Variable Distribution (%)', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_feature_distributions(df, features_to_plot=None, filepath=None):
    """
    Plot distributions of continuous features.
    
    Args:
        df (pd.DataFrame): Input dataset
        features_to_plot (list): List of features to plot (default: all numerical)
        filepath (str): Optional path to save the figure
    """
    if features_to_plot is None:
        features_to_plot = df.columns.tolist()
    
    # Limit to avoid too many subplots
    features_to_plot = features_to_plot[:12]
    
    n_features = len(features_to_plot)
    n_cols = 3
    n_rows = (n_features + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
    axes = axes.flatten()
    
    for idx, feature in enumerate(features_to_plot):
        axes[idx].hist(df[feature], bins=30, color='#3498db', edgecolor='black', alpha=0.7)
        axes[idx].set_title(f'Distribution of {feature}', fontweight='bold')
        axes[idx].set_xlabel(feature)
        axes[idx].set_ylabel('Frequency')
    
    # Hide empty subplots
    for idx in range(n_features, len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_correlation_heatmap(df, filepath=None):
    """
    Create a correlation heatmap for all features.
    
    Args:
        df (pd.DataFrame): Input dataset
        filepath (str): Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=ax)
    
    ax.set_title('Feature Correlation Matrix', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_target_vs_feature(df, feature, target='heart_disease', filepath=None):
    """
    Plot relationship between a feature and target variable.
    
    Args:
        df (pd.DataFrame): Input dataset
        feature (str): Feature name to plot
        target (str): Target column name
        filepath (str): Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Create box plot
    df.boxplot(column=feature, by=target, ax=ax)
    ax.set_title(f'{feature} by {target}', fontsize=12, fontweight='bold')
    ax.set_xlabel(target)
    ax.set_ylabel(feature)
    plt.suptitle('')  # Remove automatic title
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_confusion_matrix(y_true, y_pred, model_name='Model', filepath=None):
    """
    Plot confusion matrix for a classification model.
    
    Args:
        y_true (array-like): True labels
        y_pred (array-like): Predicted labels
        model_name (str): Name of the model
        filepath (str): Optional path to save the figure
    """
    cm = confusion_matrix(y_true, y_pred)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
                xticklabels=['No Disease', 'Disease'],
                yticklabels=['No Disease', 'Disease'])
    
    ax.set_title(f'Confusion Matrix - {model_name}', fontsize=12, fontweight='bold')
    ax.set_ylabel('True Label')
    ax.set_xlabel('Predicted Label')
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()
    
    return cm


def plot_roc_curves(results_dict, filepath=None):
    """
    Plot ROC curves for multiple models.
    
    Args:
        results_dict (dict): Dictionary with model results
                            {model_name: {'y_test': y_test, 'y_pred_proba': y_pred_proba}}
        filepath (str): Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    
    for idx, (model_name, results) in enumerate(results_dict.items()):
        y_test = results['y_test']
        y_pred_proba = results['y_pred_proba']
        
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
        roc_auc = auc(fpr, tpr)
        
        ax.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc:.3f})',
                linewidth=2, color=colors[idx % len(colors)])
    
    # Plot diagonal line
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
    
    ax.set_xlabel('False Positive Rate', fontsize=11, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=11, fontweight='bold')
    ax.set_title('ROC Curves - Model Comparison', fontsize=13, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_model_comparison(results_df, metric='Accuracy', filepath=None):
    """
    Plot comparison of models across a specific metric.
    
    Args:
        results_df (pd.DataFrame): DataFrame with model results
        metric (str): Metric to compare
        filepath (str): Optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    results_sorted = results_df.sort_values(metric, ascending=False)
    colors = ['#2ecc71' if x == results_sorted[metric].max() else '#3498db' 
              for x in results_sorted[metric]]
    
    ax.barh(results_sorted['Model'], results_sorted[metric], color=colors, edgecolor='black')
    ax.set_xlabel(metric, fontsize=11, fontweight='bold')
    ax.set_title(f'Model Comparison - {metric}', fontsize=13, fontweight='bold')
    
    # Add value labels
    for i, v in enumerate(results_sorted[metric]):
        ax.text(v - 0.02, i, f'{v:.3f}', va='center', ha='right', fontweight='bold')
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def plot_feature_importance(feature_importance_dict, top_n=10, filepath=None):
    """
    Plot feature importance from tree-based models.
    
    Args:
        feature_importance_dict (dict): {feature_name: importance_value}
        top_n (int): Number of top features to display
        filepath (str): Optional path to save the figure
    """
    # Sort and select top features
    sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)
    top_features = sorted_features[:top_n]
    
    feature_names = [f[0] for f in top_features]
    importance_values = [f[1] for f in top_features]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(feature_names, importance_values, color='#9b59b6', edgecolor='black')
    ax.set_xlabel('Importance Score', fontsize=11, fontweight='bold')
    ax.set_title(f'Top {top_n} Feature Importance', fontsize=13, fontweight='bold')
    
    # Add value labels
    for i, v in enumerate(importance_values):
        ax.text(v - 0.01, i, f'{v:.4f}', va='center', ha='right', fontweight='bold')
    
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()


def ensure_reports_directory(base_path='reports'):
    """
    Ensure the reports directory exists for saving visualizations.
    
    Args:
        base_path (str): Path to reports directory
        
    Returns:
        str: Path to reports directory
    """
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    return base_path
