# 🫀 Disease PredictionIQ - AI-Powered Disease Prediction System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A comprehensive machine learning web application for predicting heart disease using clinical diagnostic data with 14 advanced classification algorithms and a modern, responsive UI.

**Author:** Jay Prakash Kumar  
**GitHub:** [@JayAtria-7](https://github.com/JayAtria-7)  
**LinkedIn:** [Jay Prakash Kumar](https://www.linkedin.com/in/jay-prakash-kumar-1b534a260)

---

## 🌟 Features

- ✅ **14 ML Classification Models** - Compare Decision Trees, Random Forest, XGBoost, Neural Networks, and more
- 🎨 **Modern Responsive UI** - Beautiful glassmorphism design that works on all devices
- 📊 **Real-time Predictions** - Instant disease risk assessment
- 📈 **Model Comparison Dashboard** - Visual analytics with charts and metrics
- 🔬 **Clinical Data Input** - Easy-to-use form for patient diagnostic data
- 🚀 **Production Ready** - Deployed and accessible online

---

## 📋 Project Overview

This project develops and optimizes machine learning models for disease prediction based on diagnostic test results. The system provides clinical decision support using advanced ML algorithms.

**Author:** Jay Prakash

## 📋 Project Overview

This project develops and optimizes machine learning models for disease prediction based on diagnostic test results. The project simulates a real-world scenario where data scientists work with medical professionals to develop predictive models for clinical decision support.

### Business Context
Heart disease remains one of the leading causes of death globally. Early detection through diagnostic screening can significantly improve patient outcomes and reduce healthcare costs.

### Challenge
Given a patient's diagnostic test results (blood pressure, cholesterol levels, ECG results, exercise capacity, etc.), predict whether the patient has heart disease or not.

## 🎯 Project Goals

### Primary Objectives
1. **Model Development**: Build and compare **12 classification algorithms**
   - **Baseline Models (4)**: Decision Trees, Random Forest, Logistic Regression, SVM
   - **Advanced Models (8)**: XGBoost, LightGBM, Gradient Boosting, AdaBoost, Extra Trees, KNN, Naive Bayes, Neural Network

2. **Performance Optimization**: Use GridSearchCV with k-fold cross-validation to optimize hyperparameters

3. **Model Evaluation**: Assess models using appropriate metrics for medical diagnosis
   - Accuracy
   - Precision
   - Recall (Sensitivity)
   - F1-Score
   - ROC-AUC

4. **Intelligent Model Selection**: Automatically select best model using weighted scoring system

5. **Feature Analysis**: Identify the most important diagnostic indicators for heart disease prediction

## 📊 Dataset Description

### Target Variable
- `heart_disease`: Binary classification (0 = No heart disease, 1 = Heart disease present)

### Features (13 total)

#### Demographic Information
- `age`: Patient age (years)
- `sex`: Gender (0 = Female, 1 = Male)

#### Clinical Measurements
- `chest_pain_type`: Type of chest pain (0-3: Typical angina, Atypical angina, Non-anginal pain, Asymptomatic)
- `resting_blood_pressure`: Resting blood pressure (mm Hg)
- `cholesterol`: Serum cholesterol level (mg/dl)
- `fasting_blood_sugar`: Fasting blood sugar > 120 mg/dl (0 = False, 1 = True)

#### Diagnostic Test Results
- `resting_ecg`: Resting electrocardiographic results (0-2)
- `max_heart_rate`: Maximum heart rate achieved during exercise
- `exercise_induced_angina`: Exercise-induced angina (0 = No, 1 = Yes)
- `st_depression`: ST depression induced by exercise relative to rest
- `st_slope`: Slope of peak exercise ST segment (0-2)
- `num_major_vessels`: Number of major vessels colored by fluoroscopy (0-3)
- `thalassemia`: Thalassemia test result (0-3)

## 🗂️ Project Structure

```
cap2/
├── heart_disease_dataset.csv          # Dataset file
├── requirements.txt                   # Python dependencies for ML
├── requirements-api.txt               # API dependencies
├── README.md                         # Project documentation
├── DEPLOYMENT.md                     # Deployment guide
├── QUICKSTART.md                     # Quick start guide
├── Dockerfile                        # Docker configuration
├── docker-compose.yml                # Docker Compose configuration
├── .dockerignore                     # Docker ignore file
├── test_api.py                       # API testing script
├── notebooks/
│   └── 01_data_exploration_and_preprocessing.ipynb  # Main analysis notebook
├── src/
│   ├── data_preprocessing.py         # Data preprocessing utilities
│   ├── model_training.py             # Model training and tuning
│   └── visualization.py              # Visualization functions
├── api/
│   └── main.py                       # FastAPI application
├── models/                           # Trained models (saved)
│   ├── best_heart_disease_model.pkl  # Best trained model
│   ├── scaler.pkl                    # StandardScaler object
│   ├── feature_names.pkl             # Feature names
│   └── model_metadata.json           # Model metadata
└── reports/                          # Visualizations and reports
    ├── 01_target_distribution.png
    ├── 02_feature_distributions.png
    ├── 03_correlation_heatmap.png
    ├── 04_feature_vs_target.png
    ├── 05_baseline_confusion_matrices.png
    ├── 06_roc_curves.png
    ├── 07_baseline_comparison.png
    ├── 08_optimized_confusion_matrices.png
    ├── 09_optimized_comparison.png
    └── 10_feature_importance.png
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download the project

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Project

1. **Jupyter Notebook** (Recommended):
```bash
jupyter notebook notebooks/01_data_exploration_and_preprocessing.ipynb
```

2. **Run cells sequentially** to:
   - Load and explore the data
   - Perform exploratory data analysis
   - Preprocess and prepare data
   - Train baseline models
   - Evaluate and compare models
   - Perform hyperparameter tuning
   - Analyze feature importance

## 📈 Project Phases

### Phase 1: Data Exploration and Preprocessing
✅ **Completed**
- Load and examine the dataset
- Descriptive statistics analysis
- Data quality checks (missing values, duplicates)
- Target variable distribution analysis
- Correlation analysis with heatmaps
- Feature distributions visualization
- Feature vs target relationships
- Data preprocessing (scaling, train/test split)

**Deliverable**: EDA Report with visualizations

### Phase 2: Baseline Model Development
✅ **Completed**
- Decision Tree Classifier implementation
- Random Forest Classifier implementation
- Logistic Regression implementation
- Support Vector Machine (SVM) implementation
- 5-fold cross-validation evaluation
- Comprehensive metrics calculation
- Confusion matrices for all models
- ROC curves comparison

**Deliverable**: Baseline model comparison report

### Phase 3: Hyperparameter Tuning
✅ **Completed**
- GridSearchCV implementation for all models
- Optimal hyperparameter identification
- Optimized model evaluation
- Performance comparison (baseline vs optimized)
- Best model selection

### Phase 4: Feature Analysis
✅ **Completed**
- Feature importance from tree-based models
- Top predictive features identification
- Clinical significance analysis
- Visualization of feature importance

### Phase 5: Model Deployment
✅ **Completed**
- Model serialization (pickle)
- FastAPI REST API implementation
- Docker containerization
- API testing suite
- Production deployment guide

## 🚀 API Deployment

### Quick Start with Docker

```bash
# Build and run the API
docker-compose up -d

# Test the API
python test_api.py

# Access API docs
open http://localhost:8000/docs
```

### API Endpoints

- `GET /health` - Health check
- `GET /model/info` - Model information
- `POST /predict` - Single prediction
- `POST /predict/batch` - Batch predictions
- `GET /features` - Feature information

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide.

## 📊 Key Results

The notebook provides comprehensive analysis including:
- **Data Quality**: 100% complete dataset with no missing values
- **Model Performance**: All models evaluated with multiple metrics
- **Optimization**: Significant improvements through hyperparameter tuning
- **Feature Insights**: Identification of most important diagnostic indicators
- **Visualizations**: 10+ charts and graphs for analysis

## 🔍 Evaluation Metrics

Models are evaluated using:
- **Accuracy**: Overall correctness
- **Precision**: Positive predictive value
- **Recall (Sensitivity)**: True positive rate - *Critical for medical diagnosis*
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under ROC curve - *Most appropriate for medical classification*

## 💡 Clinical Recommendations

1. **Model Selection**: Prioritize models with highest ROC-AUC scores
2. **Sensitivity Focus**: In medical diagnosis, recall (sensitivity) is crucial to minimize false negatives
3. **Feature Focus**: Pay attention to top predictive features identified
4. **Continuous Monitoring**: Implement ongoing model performance tracking
5. **External Validation**: Test on independent datasets before deployment

## 📚 Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms and tools
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Jupyter**: Interactive development environment

## 📝 Learning Outcomes

Through this project, you will:
- ✅ Master classification algorithms and their use cases
- ✅ Understand hyperparameter tuning and cross-validation
- ✅ Learn to evaluate models in high-stakes domains (healthcare)
- ✅ Practice feature importance analysis and model interpretation
- ✅ Develop skills in presenting analytical findings

## 🤝 Contributing

This is a capstone project. Feel free to fork and extend with:
- Additional classification algorithms
- Deep learning approaches
- Advanced feature engineering
- Ensemble methods
- Model interpretability tools (SHAP, LIME)

## 📄 License

This project is for educational purposes.

## 📧 Contact

For questions or feedback about this project, please refer to the notebook documentation.

---

**Project Status**: ✅ Completed

**Last Updated**: October 2025
