import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

data = {
    "hours_until_deadline": [10, 5, 24, 48, 1],
    "description": [
        "Finish the project proposal",
        "Prepare slides for the meeting",
        "Write a blog post",
        "Plan the team outing",
        "Fix critical bug in the app"
    ],
    "priority_score": [0.8, 0.7, 0.6, 0.5, 0.9]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
description_vector = vectorizer.fit_transform(df["description"])

X = np.hstack((df["hours_until_deadline"].values.reshape(-1,1), description_vector.toarray()))
y = df["priority_score"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "task/models/priority_model.pkl")
joblib.dump(vectorizer, "task/models/vectorizer.pkl")