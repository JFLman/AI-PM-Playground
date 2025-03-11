from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

class SafetyPredictor:
    def __init__(self, data_path="data/telemetry_data.csv"):
        self.model = None
        self.scaler = StandardScaler()
        self.data_path = data_path
        self.train_model()

    def train_model(self):
        data = pd.read_csv(self.data_path)
        X = data[['engine_temp', 'pressure', 'stress_level']]
        y = data['failure']
        X = self.scaler.fit_transform(X)
        self.model = LogisticRegression()
        self.model.fit(X, y)

    def predict_failure(self, engine_temp, pressure, stress_level):
    # Create a DataFrame with the same column names as during training
        input_data = pd.DataFrame([[engine_temp, pressure, stress_level]], 
                        columns=['engine_temp', 'pressure', 'stress_level'])
        input_data = self.scaler.transform(input_data)
        probability = self.model.predict_proba(input_data)[0][1]
        prediction = self.model.predict(input_data)[0]
        recommendation = "Inspect immediately" if prediction else "No action needed"
        return prediction, probability, recommendation