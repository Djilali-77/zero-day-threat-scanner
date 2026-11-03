from fastapi import FastAPI, HTTPException, UploadFile, File
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# 1. Start the server 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the model in the RAM 
print("Loading AI models...")
preprocessor = joblib.load("models/preprocessor.pkl")

detector = joblib.load("models/isolation_forest.pkl")
print("Models loaded successfully!")

# 3. Endpoint check
@app.get("/")
def health_check():
    return {"status": "success", "message": "Zero-Day API is running!"}

# 4. POST Endpoint
@app.post("/predict")
def predict_anomaly(traffic: dict):
    try:
        # 1. THE SENIOR TRICK: Ghost Packet Baseline
        baseline_normal = {
            "logged_in": 1,
            "same_srv_rate": 1.0,
            "dst_host_same_srv_rate": 1.0,
            "dst_host_srv_count": 255,
            "srv_count": 8
        }
        
        full_traffic = {**baseline_normal, **traffic}
        df_input = pd.DataFrame([full_traffic])
        X_processed = preprocessor.transform_predict(df_input)
        prediction = detector.predict(X_processed)
        is_anomaly = True if prediction[0] == -1 else False
        if is_anomaly:
            return {"status": "danger", "message": "ZERO-DAY ATTACK DETECTED!"}
        else:
            return {"status": "success", "message": "NORMAL TRAFFIC"}
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict-batch")
def predict_batch_csv(file: UploadFile = File(...)):
    try:
        # 1. from csv to dataframe
        df_input = pd.read_csv(file.file)
        
        # 2. Ghost Packet Baseline
        baseline_normal = {
            "logged_in": 1,
            "same_srv_rate": 1.0,
            "dst_host_same_srv_rate": 1.0,
            "dst_host_srv_count": 255,
            "srv_count": 8
        }
        
        for col, val in baseline_normal.items():
            if col not in df_input.columns:
                df_input[col] = val

        # ==========================================
        
        X_processed = preprocessor.transform_predict(df_input)
        predictions = detector.predict(X_processed)        
        total_packets = len(predictions)
        anomalies_count = int((predictions == -1).sum())
        normal_count = int((predictions == 1).sum())
        
        return {
            "status": "success",
            "total_scanned": total_packets,
            "anomalies_found": anomalies_count,
            "normal_traffic": normal_count,
            "message": f"Scan complete. Found {anomalies_count} threats in {total_packets} packets."
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing CSV: {str(e)}")