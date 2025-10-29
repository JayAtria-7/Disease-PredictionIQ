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

## 7) Backend — Flask (UI + API)

Entrypoint: `app.py`

Load sequence:
- On startup, the app prints an initializing banner and invokes `load_model_components()` to load model, scaler, feature names, and metadata from `models/`.

Flask routes:
- GET `/` — Render UI (template `index.html`)
- GET `/api/health` — Health check (model presence, timestamp)
- GET `/api/model-info` — Model name/type/date, metrics (accuracy, precision, recall, F1, ROC-AUC, overall score)
- POST `/api/predict` — Single prediction; returns prediction label, risk level, probabilities, timestamp
- GET `/api/models-comparison` — Comparison data for all trained models (as provided by metadata)

Production serving:
- Gunicorn: `gunicorn app:app --bind 0.0.0.0:$PORT`

Note: A separate FastAPI service exists at `api/main.py` with similar capabilities for serverless or API-only deployments (endpoints differ; see Section 9).

---

## 8) Frontend — UI/UX

- Template: `templates/index.html`
  - Navigation (desktop + mobile), hero section, prediction form, results card, Model Comparison section, footer with developer links
  - External assets: Google Fonts, Font Awesome, Animate.css
- Styles: `static/css/styles.css`, `static/css/comparison.css`, `static/css/footer-enhanced.css`
  - Glassmorphism cards, gradients, animations, responsive breakpoints
- Script: `static/js/app.js`
  - Smooth scrolling, mobile menu, counters
  - Prediction form submission with loading overlay and fetch to `/api/predict`
  - Model comparison fetch from `/api/models-comparison` and chart rendering

---

## 9) Backend — FastAPI (Alternative API)

Entrypoint: `api/main.py` (headless API variant)

Key elements:
- Pydantic model `PatientData` with strict field validation and examples
- Startup event loads model artifacts
- Endpoints (subset):
  - GET `/` → JSON root info
  - GET `/health`
  - GET `/model/info`
  - GET `/features`
  - POST `/predict` (single)
  - POST `/predict/batch` (batch)

Note: Endpoint paths here differ slightly from the Flask ones (e.g., no `/api` prefix); the included `test_api.py` targets this FastAPI variant by default and expects the service on `http://localhost:8000` (see its `BASE_URL`).

---

## 10) API Reference (Flask UI Service)

Base URL (local): `http://127.0.0.1:5000`

- GET `/api/health`
  - 200 OK → `{ status, model_loaded, model_name, timestamp }`
- GET `/api/model-info`
  - 200 OK → `{ model_name, model_type, creation_date, metrics{ accuracy, precision, recall, f1_score, roc_auc, overall_score } }`
- POST `/api/predict`
  - Body (JSON): 13 numeric fields matching training features
  - 200 OK → `{ prediction, prediction_label, probability_no_disease, probability_disease, risk_level, timestamp }`
- GET `/api/models-comparison`
  - 200 OK → list or dict with all trained models and their metrics (from metadata)

Alternative API (FastAPI) endpoints are documented in Section 9.

---

## 11) Local Setup

Prerequisites:
- Python 3.10+
- Git

Create and activate a virtual environment, then install dependencies:

```bat
:: Windows (cmd)
py -3.10 -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

If running only the web app for deployment parity:

```bat
pip install -r requirements-deploy.txt
```

---

## 12) Running Locally

Flask UI (development):

```bat
set FLASK_ENV=development
python app.py
```

Then open `http://127.0.0.1:5000`.

Production-like (Gunicorn):

```bat
set PORT=5000
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:%PORT% --workers 2 --threads 2 --timeout 120
```

FastAPI alternative (API-only):

```bat
pip install -r requirements-api.txt
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 13) Configuration & Environment

- `PORT` — Port to bind (default 5000 for Flask UI; 8000 for FastAPI examples)
- `FLASK_ENV` — `development` or `production`; toggles debug
- Python version pin for Render: `PYTHON_VERSION: 3.10.0` (in `render.yaml`)

Model artifact paths (both backends rely on):
- `models/best_heart_disease_model.pkl`
- `models/scaler.pkl`
- `models/feature_names.pkl`
- `models/model_metadata.json`

Ensure these files are present in production (they are tracked in Git in this repo).

---

## 14) Deployment

Primary: Render (Flask UI)
- Config: `render.yaml`
- Build: `pip install -r requirements-deploy.txt`
- Start: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120`
- Guides: `DEPLOYMENT_GUIDE.md`, `FRESH_DEPLOY_GUIDE.md`, `RENDER_FIX.md`, `RENDER_FLASK_FIX.md`

Vercel (serverless):
- Config: `vercel.json`
- Uses `@vercel/python` to serve `app.py` directly (serverless constraints apply; Flask may be limited—see `VERCEL_DEPLOYMENT.md`)

Other options: Railway, Fly.io, Koyeb, PythonAnywhere; see `FREE_DEPLOYMENT_OPTIONS.md` and `DEPLOYMENT.md`.

Important: Docker files were renamed to avoid platform auto-detect conflicts. Render uses Python buildpack for Flask UI.

---

## 15) Testing

- API test script for FastAPI variant: `test_api.py`
  - Expects API at `http://localhost:8000`
  - Run the FastAPI server (Section 12), then:

```bat
python test_api.py
```

- Interactive prediction mode:

```bat
python test_api.py --interactive
```

- For Flask endpoints, use curl/Postman/Thunder Client to hit `/api/*` routes at `http://127.0.0.1:5000`.

---

## 16) Troubleshooting

- App starts but model not loaded:
  - Ensure `models/*.pkl` and `model_metadata.json` exist in `models/` (they are in Git).
  - Check working directory: app expects relative `models/` path.
- Getting FastAPI JSON on Render instead of Flask UI:
  - Use `render.yaml` and ensure Docker files are renamed (see `RENDER_FLASK_FIX.md`).
- 500 errors on predict:
  - Verify request JSON has all 13 features with correct numeric types.
  - Confirm scaler and feature names alignment with inputs.
- Vercel serverless issues:
  - See `VERCEL_DEPLOYMENT.md`; serverless cold start or file system constraints can affect model loading.

---

## 17) Performance & Optimization

- Preload model artifacts at startup to avoid per-request IO.
- Keep model objects small; avoid heavyweight frameworks at inference.
- Use `workers/threads` in Gunicorn to match container memory/CPU.
- Frontend bundles are plain HTML/CSS/JS; leverage caching headers via platform.
- Consider pruning models/metadata for serverless footprints.

---

## 18) Security, Compliance, and Roadmap

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
