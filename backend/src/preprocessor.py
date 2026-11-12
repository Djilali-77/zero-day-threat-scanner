import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.train_columns = None 

    def remove_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna()

    def fit_transform_train(self, df: pd.DataFrame):
        y = df['label']
        X = df.drop(columns=['label', 'difficulty_level']) 
        X_encoded = pd.get_dummies(X)
        
        self.train_columns = X_encoded.columns
        
        X_scaled = self.scaler.fit_transform(X_encoded)
        return X_scaled, y

    def transform_test(self, df: pd.DataFrame):
        y = df['label']
        X = df.drop(columns=['label', 'difficulty_level']) 
        X_encoded = pd.get_dummies(X)
        
        X_encoded = X_encoded.reindex(columns=self.train_columns, fill_value=0)
        
        X_scaled = self.scaler.transform(X_encoded)
        
        return X_scaled, y

    def transform_predict(self, df: pd.DataFrame):
        X_encoded = pd.get_dummies(df)        
        X_encoded = X_encoded.reindex(columns=self.train_columns, fill_value=0)
        X_scaled = self.scaler.transform(X_encoded)
        return X_scaled
    
    def save(self, file_path: str):
        joblib.dump(self, file_path)