# Disease PredictionIQ — Comprehensive Project Documentation

Author: Jay Prakash Kumar  
Repository: https://github.com/JayAtria-7/Disease-PredictionIQ  
Date: 2025-10-29

---

## 1) Project Overview

Disease PredictionIQ is a production-ready machine learning web application that predicts heart disease risk from clinical diagnostic inputs. It provides a modern, responsive UI built with HTML/CSS/JavaScript, a Python backend (Flask for the web app with UI; FastAPI alternative for headless API), and an ML pipeline trained on a curated heart disease dataset. The system compares 14 classification models and exposes a clean REST API plus interactive visualizations.

Core value:
- Clinical decision support using interpretable metrics (accuracy, precision, recall, F1, ROC-AUC)
- Real-time single-patient prediction with confidence breakdowns
- Model comparison dashboard for transparent model selection
- Multi-platform deployment support (Render, Vercel, Railway, etc.)

Key files:
- Backend (Flask UI): `app.py`
- Alternative API (FastAPI): `api/main.py`
- Frontend: `templates/index.html`, `static/js/app.js`, `static/css/*.css`
- ML pipeline: `src/data_preprocessing.py`, `src/model_training.py`, `src/visualization.py`
- Models: `models/` (pickles + metadata JSON)

---

## 2) Features

- 14 ML classification algorithms trained and compared (trees, ensembles, SVMs, KNN, Naive Bayes, XGBoost, LightGBM, MLP, LDA)
- Best model auto-selection with persisted artifacts: model, scaler, feature names, metadata
- Responsive glassmorphism UI with animated interactions and mobile-friendly navigation
- Real-time single prediction with risk level and probability split
- Model Comparison section: stats, tables, and charts
- REST API endpoints for health, model info, predictions, and models comparison
- Multiple deployment configurations (Render primary, Vercel, etc.)

---

## 3) Architecture

- Presentation (Client):
  - HTML template: `templates/index.html`
  - Styling: `static/css/styles.css`, `static/css/comparison.css`, `static/css/footer-enhanced.css`
  - Interactivity: `static/js/app.js`
- Application (Server):
  - Flask app for UI+API: `app.py`
  - FastAPI alternative (headless API): `api/main.py`
- ML Layer:
  - Data preprocessing: `src/data_preprocessing.py`
  - Model training and evaluation: `src/model_training.py`
  - Visualization/EDA: `src/visualization.py`
- Persisted Artifacts:
  - `models/best_heart_disease_model.pkl` (MLP best model by ROC-AUC based on current metadata)
  - `models/scaler.pkl` (StandardScaler)
  - `models/feature_names.pkl`
  - `models/model_metadata.json` (performance metrics, model info)
- Config/Deployment:
  - Render: `render.yaml`, `Procfile`
  - Vercel: `vercel.json`
  - Requirements: `requirements.txt`, `requirements-deploy.txt`, `requirements-flask.txt`, `requirements-api.txt`

Runtime ports and mode:
- Flask UI uses PORT from env (default 5000) and sets debug based on `FLASK_ENV`.

---

## 4) Dataset

Source: `heart_disease_dataset.csv` (CSV in repo). 13 features + binary target `heart_disease`.
- Demographics: `age`, `sex`
- Clinical/Diagnostics: `chest_pain_type`, `resting_blood_pressure`, `cholesterol`, `fasting_blood_sugar`, `resting_ecg`, `max_heart_rate`, `exercise_induced_angina`, `st_depression`, `st_slope`, `num_major_vessels`, `thalassemia`
- Target: `heart_disease` (0=no disease, 1=disease)

See `src/data_preprocessing.py` for quality checks, descriptive statistics, and scaling.

---

## 5) ML Pipeline

- Load and inspect data (`load_data`, `check_data_quality`, `get_descriptive_statistics`).
- Split (stratified) into train/test; scale features using `StandardScaler` (`preprocess_data`).
- Train multiple models with cross-validation (see `BaselineModels` and advanced models in `src/model_training.py`).
- Evaluate with accuracy, precision, recall, F1, ROC-AUC; select best model.
- Persist artifacts to `models/` for inference in the web app/API.
- Optional visualizations (correlations, ROC curves, confusion matrices) in `src/visualization.py` and the notebook `notebooks/01_data_exploration_and_preprocessing.ipynb`.

---

## 6) Model Training & Evaluation

Implemented classifiers (selection from code; total ~14):
- Decision Tree, Random Forest, Logistic Regression
- SVM (RBF, Linear)
- KNN, Gaussian Naive Bayes
- Gradient Boosting, AdaBoost, Extra Trees
- XGBoost, LightGBM
- MLP (Neural Network), LDA

Scoring:
- Cross-validation on training folds
- Final test metrics tracked in `model_metadata.json`
- Best model (current) indicated in metadata; repository notes MLP had best ROC-AUC (~0.6073) in recent runs

Artifacts:
- `best_heart_disease_model.pkl`
- `scaler.pkl`
- `feature_names.pkl`
- `model_metadata.json` (contains performance_metrics and metadata like model name, creation date)

---



## 6) Security, Compliance, and Roadmap

Security & privacy:
- Accept only numeric fields; the FastAPI variant enforces validation. For Flask, validate on server side before scaling/predicting.
- Never log PHI; retain minimal request data. Do not persist patient inputs unless compliance-review approved.
- Keep dependencies updated (`requirements-*.txt`).

Roadmap:
- Add threshold tuning and cost-sensitive metrics (e.g., maximize recall subject to precision).
- Add SHAP-based explanations and feature importance visualization in UI.
- Implement batch upload through the UI with CSV parsing.
- Introduce authentication for write/admin endpoints.
- CI for linting and API contract tests.

Credits & License:
- Author: Jay Prakash Kumar (@JayAtria-7)
- Stack: Python, Flask, FastAPI, scikit-learn, XGBoost, LightGBM, Pandas, NumPy, HTML/CSS/JS
- License: MIT (see `LICENSE` if present)

---

Appendix — File Map (selected):
- `app.py` — Flask app (UI + API)
- `api/main.py` — FastAPI alternative API
- `templates/index.html` — Main UI
- `static/js/app.js` — Frontend logic & charts
- `static/css/*.css` — Styling (core, comparison, footer)
- `src/data_preprocessing.py` — Data loading and scaling
- `src/model_training.py` — Model training and evaluation
- `src/visualization.py` — EDA and plots
- `models/` — Model artifacts
- `render.yaml`, `vercel.json` — Deployment configs
- `README.md`, `FRESH_DEPLOY_GUIDE.md`, `VERCEL_DEPLOYMENT.md` — Docs
