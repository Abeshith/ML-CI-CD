import pytest
import pickle
import numpy as np
from app import app  # Ensure this imports your Flask app instance

# Load the wine model
with open("model/wine_model.pkl", "rb") as f:
    wine_model = pickle.load(f)

def test_wine_model_prediction():
    # Example wine data input (based on sklearn's wine dataset features)
    input_data = [13.2, 2.77, 2.51, 18.5, 98.0, 2.24, 2.19, 0.3, 1.85, 5.0, 1.04, 3.47, 710.0]
    prediction = wine_model.predict([input_data])
    
    assert prediction is not None
    assert isinstance(prediction[0], (int, np.integer))  # Should be an integer class label

def test_flask_wine_predict():
    # Create a test client for the Flask app
    with app.test_client() as client:
        # Form data must match the names expected in the Flask form
        form_data = {
            'alcohol': 13.2,
            'malic_acid': 2.77,
            'ash': 2.51,
            'alcalinity_of_ash': 18.5,
            'magnesium': 98.0,
            'total_phenols': 2.24,
            'flavanoids': 2.19,
            'nonflavanoid_phenols': 0.3,
            'proanthocyanins': 1.85,
            'color_intensity': 5.0,
            'hue': 1.04,
            'od280/od315_of_diluted_wines': 3.47,
            'proline': 710.0
        }

        response = client.post('/predict', data=form_data)

        assert response.status_code == 200
        assert 'Predicted Wine Class' in response.get_data(as_text=True)

