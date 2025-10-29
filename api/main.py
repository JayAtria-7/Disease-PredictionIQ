"""
FastAPI Backend for Disease PredictionIQ
REST API to serve model predictions
Author: Jay Prakash
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Dict
import pickle
import numpy as np
import json
import os
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Disease PredictionIQ API",
    description="API for disease prediction based on clinical diagnostic data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and preprocessing components
MODEL_PATH = "models/best_heart_disease_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURE_NAMES_PATH = "models/feature_names.pkl"
METADATA_PATH = "models/model_metadata.json"

# Global variables for model components
model = None
scaler = None
feature_names = None
metadata = None


def load_model_components():
    """Load model and preprocessing components"""
    global model, scaler, feature_names, metadata
    
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        with open(SCALER_PATH, 'rb') as f:
            scaler = pickle.load(f)
        
        with open(FEATURE_NAMES_PATH, 'rb') as f:
            feature_names = pickle.load(f)
        
        with open(METADATA_PATH, 'r') as f:
            metadata = json.load(f)
        
        print("✓ Model components loaded successfully")
    except Exception as e:
        print(f"Error loading model components: {e}")
        raise


# Load components on startup
@app.on_event("startup")
async def startup_event():
    """Load model components when API starts"""
    load_model_components()


# Pydantic models for request/response validation
class PatientData(BaseModel):
    """Patient diagnostic data for prediction"""
    age: int = Field(..., ge=0, le=120, description="Patient age in years")
    sex: int = Field(..., ge=0, le=1, description="Gender (0=Female, 1=Male)")
    chest_pain_type: int = Field(..., ge=0, le=3, description="Type of chest pain (0-3)")
    resting_blood_pressure: int = Field(..., ge=0, le=300, description="Resting blood pressure (mm Hg)")
    cholesterol: int = Field(..., ge=0, le=600, description="Serum cholesterol (mg/dl)")
    fasting_blood_sugar: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl (0=False, 1=True)")
    resting_ecg: int = Field(..., ge=0, le=2, description="Resting ECG results (0-2)")
    max_heart_rate: int = Field(..., ge=0, le=250, description="Maximum heart rate achieved")
    exercise_induced_angina: int = Field(..., ge=0, le=1, description="Exercise induced angina (0=No, 1=Yes)")
    st_depression: float = Field(..., ge=0, le=10, description="ST depression induced by exercise")
    st_slope: int = Field(..., ge=0, le=2, description="Slope of peak exercise ST segment (0-2)")
    num_major_vessels: int = Field(..., ge=0, le=3, description="Number of major vessels (0-3)")
    thalassemia: int = Field(..., ge=0, le=3, description="Thalassemia test result (0-3)")
    
    class Config:
        schema_extra = {
            "example": {
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
        }


class PredictionResponse(BaseModel):
    """Prediction response"""
    prediction: int
    prediction_label: str
    probability_no_disease: float
    probability_disease: float
    risk_level: str
    timestamp: str


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    model_loaded: bool
    model_name: str
    timestamp: str


# API Endpoints

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "Heart Disease Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy" if model is not None else "unhealthy",
        model_loaded=model is not None,
        model_name=metadata.get("model_name", "Unknown") if metadata else "Unknown",
        timestamp=datetime.now().isoformat()
    )


@app.get("/model/info", response_model=Dict)
async def get_model_info():
    """Get model information and metadata"""
    if metadata is None:
        raise HTTPException(status_code=503, detail="Model metadata not available")
    
    return {
        "model_name": metadata.get("model_name"),
        "model_type": metadata.get("model_type"),
        "creation_date": metadata.get("creation_date"),
        "n_features": metadata.get("n_features"),
        "feature_names": metadata.get("feature_names"),
        "performance_metrics": metadata.get("performance_metrics"),
        "training_set_size": metadata.get("training_set_size"),
        "test_set_size": metadata.get("test_set_size")
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict(patient_data: PatientData):
    """
    Make a heart disease prediction for a patient
    
    Returns prediction and probability scores
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert input to array in correct feature order
        input_data = [
            patient_data.age,
            patient_data.sex,
            patient_data.chest_pain_type,
            patient_data.resting_blood_pressure,
            patient_data.cholesterol,
            patient_data.fasting_blood_sugar,
            patient_data.resting_ecg,
            patient_data.max_heart_rate,
            patient_data.exercise_induced_angina,
            patient_data.st_depression,
            patient_data.st_slope,
            patient_data.num_major_vessels,
            patient_data.thalassemia
        ]
        
        # Reshape for single prediction
        input_array = np.array(input_data).reshape(1, -1)
        
        # Scale the input
        input_scaled = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        
        # Determine risk level based on probability
        disease_probability = probabilities[1]
        if disease_probability < 0.3:
            risk_level = "Low"
        elif disease_probability < 0.6:
            risk_level = "Moderate"
        elif disease_probability < 0.8:
            risk_level = "High"
        else:
            risk_level = "Very High"
        
        return PredictionResponse(
            prediction=int(prediction),
            prediction_label="Heart Disease Detected" if prediction == 1 else "No Heart Disease",
            probability_no_disease=float(probabilities[0]),
            probability_disease=float(probabilities[1]),
            risk_level=risk_level,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.post("/predict/batch", response_model=List[PredictionResponse])
async def predict_batch(patients: List[PatientData]):
    """
    Make predictions for multiple patients
    
    Returns list of predictions and probability scores
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    if len(patients) > 100:
        raise HTTPException(status_code=400, detail="Batch size too large (max 100)")
    
    results = []
    for patient_data in patients:
        result = await predict(patient_data)
        results.append(result)
    
    return results


@app.get("/features")
async def get_features():
    """Get list of required features for prediction"""
    if feature_names is None:
        raise HTTPException(status_code=503, detail="Feature names not available")
    
    return {
        "features": feature_names,
        "n_features": len(feature_names),
        "feature_descriptions": {
            "age": "Patient age (years)",
            "sex": "Gender (0=Female, 1=Male)",
            "chest_pain_type": "Type of chest pain (0-3)",
            "resting_blood_pressure": "Resting blood pressure (mm Hg)",
            "cholesterol": "Serum cholesterol (mg/dl)",
            "fasting_blood_sugar": "Fasting blood sugar > 120 mg/dl (0=False, 1=True)",
            "resting_ecg": "Resting ECG results (0-2)",
            "max_heart_rate": "Maximum heart rate achieved",
            "exercise_induced_angina": "Exercise induced angina (0=No, 1=Yes)",
            "st_depression": "ST depression induced by exercise",
            "st_slope": "Slope of peak exercise ST segment (0-2)",
            "num_major_vessels": "Number of major vessels (0-3)",
            "thalassemia": "Thalassemia test result (0-3)"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
