"""
Model Training Module for Disease PredictionIQ
Implements baseline models and hyperparameter tuning
Author: Jay Prakash
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, roc_auc_score, confusion_matrix, roc_curve, auc)
import warnings
warnings.filterwarnings('ignore')


class BaselineModels:
    """
    Class to train and evaluate baseline classification models.
    """
    
    def __init__(self, random_state=42):
        """
        Initialize baseline models.
        
        Args:
            random_state (int): Random seed for reproducibility
        """
        self.random_state = random_state
        self.models = {}
        self.results = []
        self.cv_results = {}
        
    def train_decision_tree(self, X_train, y_train, cv_folds=5):
        """
        Train Decision Tree Classifier with cross-validation.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            cv_folds (int): Number of cross-validation folds
            
        Returns:
            dict: Model and evaluation results
        """
        print("\n" + "="*60)
        print("Decision Tree Classifier")
        print("="*60)
        
        model = DecisionTreeClassifier(random_state=self.random_state)
        model.fit(X_train, y_train)
        
        # Cross-validation scores
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv_folds, 
                                    scoring='accuracy')
        print(f"Cross-validation scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        self.models['Decision Tree'] = model
        self.cv_results['Decision Tree'] = {
            'cv_scores': cv_scores,
            'mean_cv_score': cv_scores.mean(),
            'std_cv_score': cv_scores.std()
        }
        
        return {'model': model, 'cv_scores': cv_scores}
    
    def train_random_forest(self, X_train, y_train, cv_folds=5):
        """
        Train Random Forest Classifier with cross-validation.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            cv_folds (int): Number of cross-validation folds
            
        Returns:
            dict: Model and evaluation results
        """
        print("\n" + "="*60)
        print("Random Forest Classifier")
        print("="*60)
        
        model = RandomForestClassifier(n_estimators=100, random_state=self.random_state)
        model.fit(X_train, y_train)
        
        # Cross-validation scores
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv_folds, 
                                    scoring='accuracy')
        print(f"Cross-validation scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        self.models['Random Forest'] = model
        self.cv_results['Random Forest'] = {
            'cv_scores': cv_scores,
            'mean_cv_score': cv_scores.mean(),
            'std_cv_score': cv_scores.std()
        }
        
        return {'model': model, 'cv_scores': cv_scores}
    
    def train_logistic_regression(self, X_train, y_train, cv_folds=5):
        """
        Train Logistic Regression with cross-validation.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            cv_folds (int): Number of cross-validation folds
            
        Returns:
            dict: Model and evaluation results
        """
        print("\n" + "="*60)
        print("Logistic Regression")
        print("="*60)
        
        model = LogisticRegression(max_iter=1000, random_state=self.random_state)
        model.fit(X_train, y_train)
        
        # Cross-validation scores
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv_folds, 
                                    scoring='accuracy')
        print(f"Cross-validation scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        self.models['Logistic Regression'] = model
        self.cv_results['Logistic Regression'] = {
            'cv_scores': cv_scores,
            'mean_cv_score': cv_scores.mean(),
            'std_cv_score': cv_scores.std()
        }
        
        return {'model': model, 'cv_scores': cv_scores}
    
    def train_svm(self, X_train, y_train, cv_folds=5, kernel='rbf'):
        """
        Train Support Vector Machine with cross-validation.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            cv_folds (int): Number of cross-validation folds
            kernel (str): SVM kernel type
            
        Returns:
            dict: Model and evaluation results
        """
        print("\n" + "="*60)
        print(f"Support Vector Machine (kernel={kernel})")
        print("="*60)
        
        model = SVC(kernel=kernel, probability=True, random_state=self.random_state)
        model.fit(X_train, y_train)
        
        # Cross-validation scores
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv_folds, 
                                    scoring='accuracy')
        print(f"Cross-validation scores: {cv_scores}")
        print(f"Mean CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        self.models['SVM'] = model
        self.cv_results['SVM'] = {
            'cv_scores': cv_scores,
            'mean_cv_score': cv_scores.mean(),
            'std_cv_score': cv_scores.std()
        }
        
        return {'model': model, 'cv_scores': cv_scores}
    
    def train_all_baseline_models(self, X_train, y_train, cv_folds=5):
        """
        Train all baseline models.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            cv_folds (int): Number of cross-validation folds
        """
        self.train_decision_tree(X_train, y_train, cv_folds)
        self.train_random_forest(X_train, y_train, cv_folds)
        self.train_logistic_regression(X_train, y_train, cv_folds)
        self.train_svm(X_train, y_train, cv_folds, kernel='rbf')
    
    def evaluate_models(self, X_test, y_test):
        """
        Evaluate all trained models on test set.
        
        Args:
            X_test (pd.DataFrame): Test features
            y_test (pd.Series): Test target
            
        Returns:
            pd.DataFrame: Evaluation metrics for all models
        """
        print("\n" + "="*80)
        print("MODEL EVALUATION ON TEST SET")
        print("="*80)
        
        results = []
        
        for model_name, model in self.models.items():
            print(f"\n{model_name}:")
            print("-" * 60)
            
            # Predictions
            y_pred = model.predict(X_test)
            
            # Get probability predictions (for AUC)
            if hasattr(model, 'predict_proba'):
                y_pred_proba = model.predict_proba(X_test)
            else:
                y_pred_proba = model.decision_function(X_test)
                y_pred_proba = np.column_stack([1 - y_pred_proba, y_pred_proba])
            
            # Calculate metrics
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, zero_division=0)
            recall = recall_score(y_test, y_pred, zero_division=0)
            f1 = f1_score(y_test, y_pred, zero_division=0)
            
            # ROC-AUC
            try:
                roc_auc = roc_auc_score(y_test, y_pred_proba[:, 1])
            except:
                roc_auc = roc_auc_score(y_test, y_pred)
            
            print(f"Accuracy:  {accuracy:.4f}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall:    {recall:.4f}")
            print(f"F1-Score:  {f1:.4f}")
            print(f"ROC-AUC:   {roc_auc:.4f}")
            
            results.append({
                'Model': model_name,
                'Accuracy': accuracy,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1,
                'ROC-AUC': roc_auc,
                'y_pred': y_pred,
                'y_pred_proba': y_pred_proba
            })
        
        self.results = pd.DataFrame(results)
        return self.results
    
    def get_results_summary(self):
        """
        Get summary of evaluation results.
        
        Returns:
            pd.DataFrame: Summary of results
        """
        if len(self.results) == 0:
            print("No results available. Please evaluate models first.")
            return None
        
        summary = self.results[['Model', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']].copy()
        summary = summary.sort_values('Accuracy', ascending=False)
        
        print("\n" + "="*80)
        print("BASELINE MODEL COMPARISON SUMMARY")
        print("="*80)
        print(summary.to_string(index=False))
        
        return summary
    
    def get_feature_importance(self, model_name):
        """
        Get feature importance from tree-based models.
        
        Args:
            model_name (str): Name of the model
            
        Returns:
            dict: Feature importance dictionary
        """
        if model_name not in self.models:
            print(f"Model '{model_name}' not found")
            return None
        
        model = self.models[model_name]
        
        if not hasattr(model, 'feature_importances_'):
            print(f"Model '{model_name}' does not have feature importance")
            return None
        
        return model.feature_importances_


class HyperparameterTuning:
    """
    Class for hyperparameter tuning using GridSearchCV.
    """
    
    def __init__(self, random_state=42, cv_folds=5):
        """
        Initialize hyperparameter tuning.
        
        Args:
            random_state (int): Random seed
            cv_folds (int): Number of cross-validation folds
        """
        self.random_state = random_state
        self.cv_folds = cv_folds
        self.best_models = {}
        self.grid_results = {}
    
    def tune_decision_tree(self, X_train, y_train):
        """
        Tune Decision Tree hyperparameters.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            GridSearchCV: Best model
        """
        print("\n" + "="*60)
        print("Tuning Decision Tree Classifier")
        print("="*60)
        
        param_grid = {
            'max_depth': [5, 10, 15, 20],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        dt = DecisionTreeClassifier(random_state=self.random_state)
        grid_search = GridSearchCV(dt, param_grid, cv=self.cv_folds, 
                                  scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        self.best_models['Decision Tree'] = grid_search.best_estimator_
        self.grid_results['Decision Tree'] = grid_search
        
        return grid_search
    
    def tune_random_forest(self, X_train, y_train):
        """
        Tune Random Forest hyperparameters.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            GridSearchCV: Best model
        """
        print("\n" + "="*60)
        print("Tuning Random Forest Classifier")
        print("="*60)
        
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        rf = RandomForestClassifier(random_state=self.random_state)
        grid_search = GridSearchCV(rf, param_grid, cv=self.cv_folds, 
                                  scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        self.best_models['Random Forest'] = grid_search.best_estimator_
        self.grid_results['Random Forest'] = grid_search
        
        return grid_search
    
    def tune_logistic_regression(self, X_train, y_train):
        """
        Tune Logistic Regression hyperparameters.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            GridSearchCV: Best model
        """
        print("\n" + "="*60)
        print("Tuning Logistic Regression")
        print("="*60)
        
        param_grid = {
            'C': [0.001, 0.01, 0.1, 1, 10],
            'penalty': ['l2'],
            'solver': ['lbfgs']
        }
        
        lr = LogisticRegression(max_iter=1000, random_state=self.random_state)
        grid_search = GridSearchCV(lr, param_grid, cv=self.cv_folds, 
                                  scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        self.best_models['Logistic Regression'] = grid_search.best_estimator_
        self.grid_results['Logistic Regression'] = grid_search
        
        return grid_search
    
    def tune_svm(self, X_train, y_train):
        """
        Tune SVM hyperparameters.
        
        Args:
            X_train (pd.DataFrame): Training features
            y_train (pd.Series): Training target
            
        Returns:
            GridSearchCV: Best model
        """
        print("\n" + "="*60)
        print("Tuning Support Vector Machine")
        print("="*60)
        
        param_grid = {
            'C': [0.1, 1, 10],
            'kernel': ['rbf', 'poly'],
            'gamma': ['scale', 'auto']
        }
        
        svm = SVC(probability=True, random_state=self.random_state)
        grid_search = GridSearchCV(svm, param_grid, cv=self.cv_folds, 
                                  scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        self.best_models['SVM'] = grid_search.best_estimator_
        self.grid_results['SVM'] = grid_search
        
        return grid_search
