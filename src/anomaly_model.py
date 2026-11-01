from sklearn.ensemble import IsolationForest
import numpy as np
import joblib

class AnomalyDetector:
    def __init__(self, contamination: float = 0.05):
        self.model = IsolationForest(
            contamination=contamination,
            verbose=1,
            random_state=42
        )
    
    def train(self, X: np.ndarray):
        self.model.fit(X)
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        predict_y = self.model.predict(X)
        return predict_y

    def save(self, file_path: str):
        joblib.dump(self.model, file_path)