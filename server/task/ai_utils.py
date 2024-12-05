import joblib
import numpy as np

# Load model and vectorizer
model = joblib.load("task/models/priority_model.pkl")
vectorizer = joblib.load("task/models/vectorizer.pkl")

def predict_priority(hours_until_deadline, description):
    # Vectorize the description
    description_vector = vectorizer.transform([description])

    # Combine features (ensure 2D shape for hours_until_deadline)
    hours_array = np.array([[hours_until_deadline]])  # Reshape to (1, 1)
    features = np.hstack((hours_array, description_vector.toarray()))

    # Predict priority
    priority = model.predict(features)
    return priority[0]
