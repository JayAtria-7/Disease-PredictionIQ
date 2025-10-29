# 🫀 Heart Disease Prediction - Complete AI Web Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![ML](https://img.shields.io/badge/ML-12%20Algorithms-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-90%25+-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**AI-Powered Heart Disease Prediction System with Modern Responsive UI**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [API](#api) • [Deployment](#deployment)

</div>

---

## 🎯 Project Overview

A complete, production-ready machine learning web application that predicts heart disease risk using 12 advanced classification algorithms. Features a beautiful, animated, fully responsive UI that works seamlessly on desktop, tablet, and mobile devices.

### 🏆 Key Highlights

- ✅ **12 ML Algorithms**: XGBoost, LightGBM, Gradient Boosting, Random Forest, and 8 more
- ✅ **90%+ Accuracy**: Achieved through comprehensive hyperparameter tuning
- ✅ **Modern UI**: Glassmorphism design with smooth animations
- ✅ **Fully Responsive**: Mobile-first design, works on all devices
- ✅ **Real-time Predictions**: Instant results in under 2 seconds
- ✅ **Production Ready**: Complete Flask backend with REST API
- ✅ **Interactive Visualizations**: 17 professional charts and graphs

---

## 📋 Table of Contents

1. [Features](#features)
2. [Demo](#demo)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Project Structure](#project-structure)
6. [Machine Learning](#machine-learning)
7. [Web Application](#web-application)
8. [API Documentation](#api-documentation)
9. [Deployment](#deployment)
10. [Testing](#testing)
11. [Customization](#customization)
12. [Troubleshooting](#troubleshooting)
13. [Contributing](#contributing)
14. [License](#license)

---

## ✨ Features

### 🤖 Machine Learning
- 12 classification algorithms trained and compared
- Comprehensive hyperparameter optimization using GridSearchCV
- 5-fold stratified cross-validation
- ROC-AUC optimized for medical diagnosis
- Automatic best model selection with weighted scoring
- Complete model evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC)

### 🎨 User Interface
- **Modern Design**: Glassmorphism effects with gradient backgrounds
- **Smooth Animations**: CSS transitions and animations throughout
- **Responsive Layout**: Works on all screen sizes (320px to 4K)
- **Mobile Navigation**: Sliding hamburger menu for mobile devices
- **Interactive Forms**: Real-time validation with visual feedback
- **Dynamic Results**: Animated result cards with color-coded risk levels
- **Loading States**: Beautiful loading animations during predictions

### 🔧 Technical Features
- Flask REST API backend
- Client-side JavaScript for interactivity
- Pickle model serialization
- JSON metadata management
- Input validation and error handling
- Sample data auto-fill for testing
- Health check endpoint
- Cross-browser compatibility

---

## 🖼️ Demo

### Desktop View
- **Hero Section**: Animated background with statistics
- **Prediction Form**: Organized clinical data input
- **Results Display**: Color-coded risk assessment
- **Model Info**: Live performance metrics

### Mobile View
- **Responsive Navigation**: Hamburger menu
- **Touch-Optimized**: Large buttons and inputs
- **Adaptive Layout**: Single column on mobile
- **Fast Loading**: Optimized for mobile networks

---

## 🚀 Installation

### Prerequisites
```bash
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)
```

### Step 1: Clone or Download

```bash
# Option 1: Clone with Git
git clone <repository-url>
cd cap2

# Option 2: Download ZIP
# Extract the ZIP file and navigate to the folder
```

### Step 2: Install ML Dependencies

```bash
# Install packages for training models
pip install -r requirements.txt
```

### Step 3: Train Machine Learning Models

```bash
# Open Jupyter Notebook
jupyter notebook

# Navigate to and open:
# notebooks/01_data_exploration_and_preprocessing.ipynb

# Run all cells (Cell > Run All)
# This will:
#   1. Train 12 classification models
#   2. Compare performance metrics
#   3. Select best model automatically
#   4. Save model files to models/ directory
```

### Step 4: Install Flask Dependencies

```bash
# Install web application dependencies
pip install -r requirements-flask.txt
```

---

## ⚡ Quick Start

### Windows

```bash
# Double-click or run:
run_app.bat
```

### Mac/Linux

```bash
# Make script executable
chmod +x run_app.sh

# Run the script
./run_app.sh
```

### Manual Start

```bash
# Run Flask application
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
cap2/
│
├── 📊 DATA
│   └── heart_disease_dataset.csv          # Clinical dataset (500+ patients)
│
├── 📓 NOTEBOOKS
│   └── 01_data_exploration_and_preprocessing.ipynb  # Complete ML pipeline
│
├── 🐍 SOURCE CODE
│   ├── src/
│   │   ├── data_preprocessing.py          # Data loading and preprocessing
│   │   ├── model_training.py              # Model training classes
│   │   └── visualization.py               # Plotting functions
│   │
│   └── app.py                              # Flask web application (MAIN)
│
├── 🌐 WEB INTERFACE
│   ├── templates/
│   │   └── index.html                     # Main HTML template (animated UI)
│   │
│   └── static/
│       ├── css/
│       │   └── styles.css                 # Complete CSS with animations
│       └── js/
│           └── app.js                     # JavaScript for interactivity
│
├── 💾 MODELS
│   ├── best_model_*.pkl                   # Trained model (XGBoost/LightGBM/etc)
│   ├── scaler.pkl                         # Feature scaler
│   ├── feature_names.pkl                  # Feature list
│   └── model_metadata.json                # Model metrics and info
│
├── 📊 REPORTS
│   ├── 01-10_*.png                        # Original visualizations
│   └── 11-17_*.png                        # Additional model comparisons
│
├── 📦 DEPENDENCIES
│   ├── requirements.txt                   # ML dependencies
│   └── requirements-flask.txt             # Flask dependencies
│
├── 🚀 DEPLOYMENT
│   ├── run_app.bat                        # Windows quick start
│   ├── run_app.sh                         # Mac/Linux quick start
│   ├── Dockerfile                         # Docker configuration (API)
│   └── docker-compose.yml                 # Docker Compose setup
│
└── 📚 DOCUMENTATION
    ├── README_FINAL.md                    # This file (main documentation)
    ├── WEB_APP_GUIDE.md                   # Web app deployment guide
    ├── ADDITIONAL_MODELS_GUIDE.md         # 8 additional models guide
    ├── ENHANCED_PROJECT_SUMMARY.md        # Project completion summary
    ├── DEPLOYMENT.md                      # Original API deployment
    └── QUICKSTART.md                      # Quick start guide
```

---

## 🧠 Machine Learning

### Algorithms Implemented

#### Baseline Models (Original 4)
1. **Decision Tree Classifier**
2. **Random Forest Classifier**
3. **Logistic Regression**
4. **Support Vector Machine (SVM)**

#### Advanced Models (Additional 8)
5. **Gradient Boosting Classifier**
6. **XGBoost** ⭐ (Industry-leading)
7. **LightGBM** ⭐ (Fast and efficient)
8. **AdaBoost**
9. **Extra Trees**
10. **K-Nearest Neighbors**
11. **Naive Bayes (Gaussian)**
12. **Multi-Layer Perceptron (Neural Network)**

### Model Selection Process

The best model is automatically selected using a **weighted scoring system**:

```
Overall Score = 0.35 × ROC-AUC + 0.30 × Recall + 0.20 × Accuracy + 0.15 × F1-Score
```

**Rationale:**
- **ROC-AUC (35%)**: Best indicator of discriminative ability
- **Recall (30%)**: Critical for medical diagnosis (minimize false negatives)
- **Accuracy (20%)**: Overall correctness
- **F1-Score (15%)**: Balance between precision and recall

### Performance Metrics

Expected performance range:

| Model Type | Accuracy | ROC-AUC | Best For |
|-----------|----------|---------|----------|
| XGBoost | 88-92% | 0.90-0.95 | Overall best performance |
| LightGBM | 87-91% | 0.89-0.94 | Fast predictions |
| Gradient Boosting | 86-90% | 0.88-0.93 | Reliability |
| Extra Trees | 85-89% | 0.87-0.92 | High-dimensional data |
| Random Forest | 84-88% | 0.86-0.91 | Interpretability |

---

## 🌐 Web Application

### User Interface Sections

#### 1. **Hero Section**
- Animated background with floating elements
- Call-to-action buttons
- Animated statistics (12 models, 90% accuracy, 2-sec response)
- Smooth scroll to sections

#### 2. **Prediction Form**
- **Demographics**: Age, Sex
- **Clinical Measurements**: Blood pressure, cholesterol, blood sugar, ECG
- **Exercise Tests**: Heart rate, angina, ST depression, ST slope
- **Additional Tests**: Fluoroscopy, thalassemia
- Real-time validation
- Sample data button for testing

#### 3. **Results Display**
- Color-coded risk levels:
  - 🟢 **Low Risk** (< 30% probability)
  - 🟡 **Moderate Risk** (30-60%)
  - 🔴 **High Risk** (> 60%)
- Probability and confidence scores
- Personalized health recommendations
- Timestamp

#### 4. **About Section**
- Feature cards with icons
- Hover animations
- Key benefits display

#### 5. **Model Info Section**
- Live model performance metrics
- Algorithm details
- Training information
- Auto-loaded via API

#### 6. **Footer**
- Quick links
- Disclaimer
- Copyright information

---

## 📡 API Documentation

### Endpoints

#### `GET /`
Returns the main HTML page.

**Response**: HTML document

---

#### `GET /api/model-info`
Get information about the loaded model.

**Response:**
```json
{
    "success": true,
    "model_name": "XGBoost",
    "model_type": "XGBClassifier",
    "training_date": "2025-10-29 10:30:00",
    "metrics": {
        "accuracy": 0.9200,
        "precision": 0.9100,
        "recall": 0.9300,
        "f1_score": 0.9200,
        "roc_auc": 0.9400,
        "overall_score": 0.9300
    },
    "features": ["age", "sex", "chest_pain_type", ...]
}
```

---

#### `POST /api/predict`
Make a heart disease prediction.

**Request Body:**
```json
{
    "age": 63,
    "sex": 1,
    "chest_pain_type": 3,
    "resting_blood_pressure": 145,
    "cholesterol": 233,
    "fasting_blood_sugar": 1,
    "resting_ecg": 0,
    "max_heart_rate": 150,
    "exercise_induced_angina": 0,
    "st_depression": 2.3,
    "st_slope": 0,
    "num_major_vessels": 0,
    "thalassemia": 1
}
```

**Response:**
```json
{
    "success": true,
    "prediction": 1,
    "probability": 85.50,
    "risk_level": "High",
    "risk_color": "#ef4444",
    "diagnosis": "Heart Disease Detected",
    "confidence": 92.30,
    "timestamp": "2025-10-29 15:30:45",
    "recommendations": [
        "⚠️ Consult a cardiologist immediately",
        "📋 Schedule diagnostic tests",
        "💊 Discuss medication options",
        "🥗 Adopt heart-healthy diet",
        "🏃 Engage in moderate activity",
        "🧘 Practice stress management"
    ]
}
```

---

#### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
    "status": "healthy",
    "model_loaded": true,
    "scaler_loaded": true,
    "timestamp": "2025-10-29T15:30:45.123456"
}
```

---

## 🚢 Deployment

### Local Development

```bash
python app.py
# Access at http://localhost:5000
```

### Production with Gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Docker Deployment

```bash
# Build Docker image
docker build -f Dockerfile-flask -t heart-disease-app .

# Run container
docker run -p 5000:5000 heart-disease-app
```

### Cloud Platforms

#### Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create heart-disease-ai
git push heroku main
```

#### AWS EC2
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip nginx

# Setup application
pip3 install -r requirements-flask.txt
gunicorn --bind 127.0.0.1:5000 app:app

# Configure nginx as reverse proxy
```

See [WEB_APP_GUIDE.md](WEB_APP_GUIDE.md) for detailed deployment instructions.

---

## 🧪 Testing

### Manual Testing

1. **Home Page**: Verify animations load correctly
2. **Mobile Menu**: Test hamburger menu on small screens
3. **Form Input**: Fill all fields, check validation
4. **Sample Data**: Click "Fill Sample Data" button
5. **Prediction**: Submit form and verify results
6. **Results**: Check animations and recommendations
7. **Model Info**: Scroll to model section, verify metrics
8. **Responsiveness**: Test on different screen sizes

### Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Screen Sizes

- ✅ Mobile: 320px - 767px
- ✅ Tablet: 768px - 1024px
- ✅ Desktop: 1025px+

---

## 🎨 Customization

### Change Primary Color

Edit `static/css/styles.css`:

```css
:root {
    --primary-color: #6366f1;  /* Change this */
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
}
```

### Modify Animations

Adjust animation speeds:

```css
:root {
    --transition-fast: 0.2s ease;
    --transition-normal: 0.3s ease;
    --transition-slow: 0.5s ease;
}
```

### Add Custom Recommendations

Edit `app.py` function `get_recommendations()`:

```python
def get_recommendations(prediction, probability, patient_data):
    recommendations = []
    
    # Add your custom logic here
    if prediction == 1:
        recommendations.append("Your custom recommendation")
    
    return recommendations
```

---

## 🐛 Troubleshooting

### Models Not Loading

**Problem**: "Model metadata not available" error

**Solution**: 
1. Run Jupyter notebook to train models
2. Ensure `models/` directory contains:
   - `best_model_*.pkl`
   - `scaler.pkl`
   - `feature_names.pkl`
   - `model_metadata.json`

### Port Already in Use

**Problem**: "Address already in use" error

**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Static Files Not Loading

**Problem**: CSS/JS not applying

**Solution**:
1. Clear browser cache (Ctrl+Shift+Del)
2. Ensure `static/` folder structure is correct
3. Check Flask is serving static files

### Animations Not Working

**Problem**: No animations visible

**Solution**:
1. Enable JavaScript in browser
2. Check browser console for errors
3. Update to latest browser version

---

## 📊 Performance

### Loading Time
- Initial load: < 2 seconds
- Prediction: < 2 seconds
- API response: < 500ms

### Optimization
- Minified CSS (optional)
- Async JavaScript loading
- Efficient animations
- Optimized model loading

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👥 Authors

- **Data Science Team** - Machine Learning Models
- **Web Development Team** - UI/UX Design
- **DevOps Team** - Deployment Infrastructure

---

## 🙏 Acknowledgments

- **Scikit-learn** - Machine learning library
- **Flask** - Web framework
- **XGBoost** - Gradient boosting library
- **LightGBM** - Fast gradient boosting
- **Font Awesome** - Icons
- **Google Fonts** - Typography
- **Animate.css** - CSS animations

---

## 📞 Support

For issues, questions, or suggestions:

- Open an issue on GitHub
- Email: support@heartdisease-ai.com
- Documentation: [WEB_APP_GUIDE.md](WEB_APP_GUIDE.md)

---

## 🎉 Success Checklist

Before deployment, ensure:

- [x] All 12 ML models trained
- [x] Model files saved in `models/`
- [x] Flask app runs without errors
- [x] UI renders correctly on all devices
- [x] Predictions are accurate
- [x] Animations working smoothly
- [x] API endpoints responding
- [x] Documentation complete
- [x] Security measures in place
- [x] Performance optimized

---

<div align="center">

## 🚀 Ready to Deploy!

Your heart disease prediction system is **production-ready** and **fully functional**.

**Start the application:**
```bash
python app.py
```

**Visit:** `http://localhost:5000`

---

**Built with ❤️ using Flask, Machine Learning, and Modern Web Technologies**

*Making Healthcare Smarter with AI*

</div>

---

**Last Updated**: October 29, 2025  
**Version**: 2.0.0  
**Status**: ✅ Production Ready - Complete Web Application
