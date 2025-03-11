import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class SafetyPredictor:
    def __init__(self, data_path):
        self.model = None
        self.scaler = StandardScaler()
        self.data_path = data_path
        self.train_model()

    def train_model(self):
        # Load data
        data = pd.read_csv(self.data_path)
        X = data[['engine_temp', 'pressure', 'stress_level']]
        y = data['failure']

        # Preprocess
        X_scaled = self.scaler.fit_transform(X)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Train model
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        # Evaluate
        score = self.model.score(X_test, y_test)
        print(f"Model accuracy: {score:.2f}")

    def predict(self, telemetry_data):
        # Preprocess input
        telemetry_array = np.array([telemetry_data])
        telemetry_scaled = self.scaler.transform(telemetry_array)

        # Predict
        probability = self.model.predict_proba(telemetry_scaled)[0][1]
        prediction = self.model.predict(telemetry_scaled)[0]

        # Recommendation
        recommendation = "No action needed."
        if probability > 0.7:
            recommendation = "High risk: Reduce engine load immediately."
        elif probability > 0.4:
            recommendation = "Moderate risk: Schedule maintenance check."

        return prediction, probability, recommendation