---
marp: true
paginate: true
theme: default
class: lead
---

# Disease PredictionIQ
AI-Powered Heart Disease Prediction

- Author: Jay Prakash Kumar (@JayAtria-7)
- Tech: Python, Flask, FastAPI, scikit-learn, XGBoost, LightGBM, Pandas, NumPy, HTML/CSS/JS
- Repo: github.com/JayAtria-7/Disease-PredictionIQ

Notes:
- Short intro to the project purpose and what the audience will see: problem, solution, demo, metrics, deployment.

---

## Executive Summary

- Predict heart disease risk from 13 clinical features
- 14 ML models trained; best model persisted and served via web UI + API
- Modern responsive UI + transparent model comparison dashboard
- Multi-platform deployment ready (Render primary, Vercel optional)

Impact
- Early risk stratification → better outcomes, reduced costs
- Reusable ML serving template for other medical prediction tasks

Notes:
- Emphasize breadth (14 models) and production readiness (UI, API, deployment).

---

## Problem & Context

- Heart disease is a leading cause of mortality globally
- Challenge: Predict disease presence from routine diagnostics
- Goal: Fast, interpretable, and accessible risk assessment

Business value
- Decision support for screening workflows
- Consistent triage at point of care

Notes:
- Clarify this is decision support, not a diagnostic replacement.

---

## Dataset Overview

- File: `heart_disease_dataset.csv`
- Target: `heart_disease` (0/1)
- Features (13):
  - Demographic: age, sex
  - Clinical: chest_pain_type, resting_blood_pressure, cholesterol,
    fasting_blood_sugar, resting_ecg, max_heart_rate,
    exercise_induced_angina, st_depression, st_slope,
    num_major_vessels, thalassemia

Data quality steps
- Missing/duplicates check, types, memory usage
- Standardization via StandardScaler

Notes:
- Mention stratified split preserves target proportion.

---

## Solution Architecture

[Architecture Diagram]

- Client: HTML template + CSS + vanilla JS
- Server: Flask (UI + API)  |  Alternative: FastAPI (API-only)
- ML: Preprocessing, training, evaluation (scikit-learn + boosted trees + MLP)
- Artifacts: model, scaler, feature names, metadata in `models/`
- Deployment: Render (Flask) | Vercel (serverless options)

Notes:
- Point to `app.py`, `api/main.py`, `src/*`, and `models/`.

---

## ML Pipeline

- EDA & quality checks
- Train/test split (stratified), scaling
- 14 models: trees, ensembles, SVMs, KNN, naive bayes, XGBoost, LightGBM, MLP, LDA
- Cross-validation + test metrics → select best
- Persist artifacts for inference

Notes:
- Stress reproducibility and cross-validation.

---

## Models Trained

- Baselines: Decision Tree, Logistic Regression, SVM (linear/rbf)
- Ensembles: Random Forest, Extra Trees, GradientBoosting, AdaBoost
- Boosting libs: XGBoost, LightGBM
- Others: KNN, Gaussian NB, LDA, MLP (Neural Net)

Selection
- Weighted evaluation on test metrics; best model persisted

Notes:
- The current best reported: MLP by ROC-AUC (~0.6073).

---

## Evaluation Metrics

- Accuracy, Precision, Recall (Sensitivity), F1-Score, ROC-AUC
- Goal: Balance sensitivity with precision for screening

[Metrics Table/Chart Placeholder]
- Example: Best model ROC-AUC ≈ 0.6073 (recent run metadata)

Notes:
- Explain trade-offs; recall is critical in medical screening.

---

## Persisted Artifacts

- `models/best_heart_disease_model.pkl`
- `models/scaler.pkl`
- `models/feature_names.pkl`
- `models/model_metadata.json`

Runtime
- Artifacts loaded once at startup for low-latency inference

Notes:
- Mention alignment of feature order with scaler and training schema.

---

## Web Application (UI)

- Modern glassmorphism design
- Sections: Home, Prediction form, Model Comparison, Model Info
- JS handles form validation, API calls, and charts

[UI Screenshot Placeholder]

Notes:
- File refs: `templates/index.html`, `static/js/app.js`, `static/css/*.css`.

---

## API (Flask UI Service)

Base: `http://127.0.0.1:5000`
- GET `/api/health` → status, model_loaded, timestamp
- GET `/api/model-info` → metrics + metadata
- POST `/api/predict` → prediction, probabilities, risk level
- GET `/api/models-comparison` → metrics for all models

Notes:
- JSON schema mirrors training feature names and numeric types.

---

## Alternative API (FastAPI)

Base: `http://127.0.0.1:8000`
- Pydantic validation for all 13 fields
- Endpoints: `/`, `/health`, `/model/info`, `/features`, `/predict`, `/predict/batch`
- Test script: `test_api.py`

Notes:
- Use FastAPI for serverless/API-only environments or stricter validation.

---

## Live Demo Plan

Scenario A — Flask UI (local)
1) Activate venv, install `requirements.txt`
2) `python app.py`
3) Open `http://127.0.0.1:5000`, submit example patient

Scenario B — FastAPI (API-only)
1) Install `requirements-api.txt`
2) `uvicorn api.main:app --port 8000`
3) `python test_api.py`

Notes:
- Have example patient JSON ready; show probabilities and risk level.

---

## Deployment

Primary: Render (Flask UI)
- Config: `render.yaml`
- Build: `pip install -r requirements-deploy.txt`
- Start: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 2`

Optional: Vercel (serverless)
- Config: `vercel.json` using `@vercel/python`
- Caveat: serverless cold start & file constraints; see `VERCEL_DEPLOYMENT.md`

Notes:
- Docker files renamed to avoid mis-detection on Render.

---

## Engineering Practices

- Reproducible training w/ CV & fixed seeds
- Clear separation: UI, API, ML, and deployment configs
- Model artifacts versioned in Git for deployment reproducibility

Notes:
- Mention standard Python packaging via requirements files.

---

## Security & Compliance

- Numeric validation (strict via FastAPI)
- No PHI logging; avoid storing patient inputs
- Keep dependencies patched; principle of least privilege

Notes:
- Future: auth for admin routes; rate limiting.

---

## Performance Considerations

- Preload artifacts; avoid per-request disk IO
- Gunicorn workers/threads tuned to platform
- Lightweight inference stack (scikit-learn models)

Notes:
- Frontend caching via platform CDN.

---

## Challenges & Fixes

- Model files missing in deploy → committed `models/` artifacts
- Render serving FastAPI instead of Flask → renamed Docker files, used Python buildpack
- PORT/ENV mismatches → `app.py` respects `PORT` and `FLASK_ENV`

Notes:
- Show resilience and quick iteration.

---

## Roadmap

- Threshold tuning; cost-sensitive optimization
- SHAP explanations in UI; per-feature insights
- Batch CSV upload via UI
- CI pipeline for tests/lint; auth for admin endpoints

Notes:
- Tie roadmap to business value (interpretability, workflow integration).

---

## Call to Action

- Try the live demo / local run
- Review model comparison and discuss operating point (threshold)
- Identify next clinical features to add

Notes:
- Invite feedback from both engineering and clinical stakeholders.

---

## Q&A

Thank you!

Contact: jay.prakash7.kr@gmail.com

Notes:
- Keep backup slides ready.

---

## Backup: API Schemas

Flask `/api/predict` (body)
- 13 numeric fields: age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_induced_angina, st_depression, st_slope, num_major_vessels, thalassemia

FastAPI validation (example ranges)
- age: 0–120, blood pressure: 0–300, cholesterol: 0–600, etc.

---

## Backup: Local Setup (Windows)

```bat
py -3.10 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Flask dev run
```bat
set FLASK_ENV=development
python app.py
```

---

## Backup: Project Structure

```
app.py
api/main.py
src/
  data_preprocessing.py
  model_training.py
  visualization.py
static/
  css/*
  js/app.js
templates/index.html
models/
  best_heart_disease_model.pkl
  scaler.pkl
  feature_names.pkl
  model_metadata.json
```

---

## Backup: Troubleshooting

- 500 on predict: check request schema & types
- Model not found: ensure `models/` exists in working dir
- Render shows API JSON: use `render.yaml`; see `RENDER_FLASK_FIX.md`

---

## Backup: References

- Repo: github.com/JayAtria-7/Disease-PredictionIQ
- Docs: `fullfinaldocu.md`, `FRESH_DEPLOY_GUIDE.md`, `VERCEL_DEPLOYMENT.md`
- Stack: Flask, FastAPI, scikit-learn, XGBoost, LightGBM, Pandas, NumPy
