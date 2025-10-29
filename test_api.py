"""
API Testing Script for Disease PredictionIQ API
Tests all endpoints with various scenarios
Author: Jay Prakash
"""

import requests
import json
from typing import Dict, List

# API Base URL
BASE_URL = "http://localhost:8000"


def print_response(title: str, response: requests.Response):
    """Pretty print API response"""
    print(f"\n{'='*80}")
    print(f"{title}")
    print(f"{'='*80}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))


def test_root():
    """Test root endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print_response("TEST: Root Endpoint", response)
    return response.status_code == 200


def test_health_check():
    """Test health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print_response("TEST: Health Check", response)
    return response.status_code == 200


def test_model_info():
    """Test model info endpoint"""
    response = requests.get(f"{BASE_URL}/model/info")
    print_response("TEST: Model Information", response)
    return response.status_code == 200


def test_features():
    """Test features endpoint"""
    response = requests.get(f"{BASE_URL}/features")
    print_response("TEST: Feature List", response)
    return response.status_code == 200


def test_single_prediction_positive():
    """Test single prediction - likely heart disease case"""
    patient_data = {
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
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=patient_data
    )
    print_response("TEST: Single Prediction (High Risk Case)", response)
    return response.status_code == 200


def test_single_prediction_negative():
    """Test single prediction - likely healthy case"""
    patient_data = {
        "age": 35,
        "sex": 0,
        "chest_pain_type": 0,
        "resting_blood_pressure": 120,
        "cholesterol": 180,
        "fasting_blood_sugar": 0,
        "resting_ecg": 0,
        "max_heart_rate": 180,
        "exercise_induced_angina": 0,
        "st_depression": 0.0,
        "st_slope": 1,
        "num_major_vessels": 0,
        "thalassemia": 2
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=patient_data
    )
    print_response("TEST: Single Prediction (Low Risk Case)", response)
    return response.status_code == 200


def test_batch_prediction():
    """Test batch prediction endpoint"""
    patients = [
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
        },
        {
            "age": 45,
            "sex": 0,
            "chest_pain_type": 1,
            "resting_blood_pressure": 130,
            "cholesterol": 200,
            "fasting_blood_sugar": 0,
            "resting_ecg": 1,
            "max_heart_rate": 165,
            "exercise_induced_angina": 0,
            "st_depression": 0.8,
            "st_slope": 1,
            "num_major_vessels": 0,
            "thalassemia": 2
        },
        {
            "age": 55,
            "sex": 1,
            "chest_pain_type": 2,
            "resting_blood_pressure": 140,
            "cholesterol": 250,
            "fasting_blood_sugar": 1,
            "resting_ecg": 0,
            "max_heart_rate": 140,
            "exercise_induced_angina": 1,
            "st_depression": 1.5,
            "st_slope": 2,
            "num_major_vessels": 1,
            "thalassemia": 2
        }
    ]
    
    response = requests.post(
        f"{BASE_URL}/predict/batch",
        json=patients
    )
    print_response("TEST: Batch Prediction (3 patients)", response)
    return response.status_code == 200


def test_invalid_input():
    """Test API with invalid input data"""
    # Missing required field
    invalid_data = {
        "age": 50,
        "sex": 1
        # Missing other required fields
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=invalid_data
    )
    print_response("TEST: Invalid Input (Missing Fields)", response)
    return response.status_code == 422  # Validation error expected


def test_out_of_range_values():
    """Test API with out-of-range values"""
    invalid_data = {
        "age": 200,  # Invalid age
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
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=invalid_data
    )
    print_response("TEST: Out-of-Range Values", response)
    return response.status_code == 422  # Validation error expected


def run_all_tests():
    """Run all API tests"""
    print("\n" + "="*80)
    print("HEART DISEASE PREDICTION API - TEST SUITE")
    print("="*80)
    
    tests = [
        ("Root Endpoint", test_root),
        ("Health Check", test_health_check),
        ("Model Information", test_model_info),
        ("Feature List", test_features),
        ("Single Prediction (High Risk)", test_single_prediction_positive),
        ("Single Prediction (Low Risk)", test_single_prediction_negative),
        ("Batch Prediction", test_batch_prediction),
        ("Invalid Input Handling", test_invalid_input),
        ("Out-of-Range Value Handling", test_out_of_range_values)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, "✓ PASSED" if passed else "✗ FAILED"))
        except Exception as e:
            print(f"\n{'='*80}")
            print(f"ERROR in {test_name}: {str(e)}")
            print(f"{'='*80}")
            results.append((test_name, f"✗ ERROR: {str(e)}"))
    
    # Print summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    for test_name, result in results:
        print(f"{result:12} {test_name}")
    
    passed_count = sum(1 for _, r in results if "PASSED" in r)
    total_count = len(results)
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    print("="*80)


def interactive_prediction():
    """Interactive mode for making predictions"""
    print("\n" + "="*80)
    print("INTERACTIVE PREDICTION MODE")
    print("="*80)
    print("\nEnter patient data (or press Enter for example values):\n")
    
    # Use example values if user presses Enter
    default_patient = {
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
    
    patient_data = {}
    for key, default_value in default_patient.items():
        value = input(f"{key} [{default_value}]: ").strip()
        if value:
            try:
                if isinstance(default_value, int):
                    patient_data[key] = int(value)
                else:
                    patient_data[key] = float(value)
            except ValueError:
                print(f"Invalid value, using default: {default_value}")
                patient_data[key] = default_value
        else:
            patient_data[key] = default_value
    
    # Make prediction
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=patient_data
        )
        
        print(f"\n{'='*80}")
        print("PREDICTION RESULT")
        print(f"{'='*80}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\nPrediction: {result['prediction_label']}")
            print(f"Risk Level: {result['risk_level']}")
            print(f"\nProbabilities:")
            print(f"  No Disease: {result['probability_no_disease']:.2%}")
            print(f"  Disease:    {result['probability_disease']:.2%}")
            print(f"\nTimestamp: {result['timestamp']}")
        else:
            print(f"Error: Status Code {response.status_code}")
            print(response.json())
        
        print(f"{'='*80}")
        
    except Exception as e:
        print(f"\nError making prediction: {str(e)}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_prediction()
    else:
        print("\nMake sure the API is running: uvicorn api.main:app --reload")
        print("Or with Docker: docker-compose up\n")
        
        try:
            run_all_tests()
            print("\n\nRun 'python test_api.py --interactive' for interactive prediction mode")
        except requests.exceptions.ConnectionError:
            print("\n❌ ERROR: Cannot connect to API at", BASE_URL)
            print("Please make sure the API is running!")
