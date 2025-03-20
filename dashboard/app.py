# 📂 dashboard/app.py
from fastapi import FastAPI
from model.predict import realtime_detection
import pandas as pd

app = FastAPI(title="Docker ML Anomaly Detection")

@app.get("/check")
def check_anomalies():
    result: pd.DataFrame = realtime_detection()
    anomalies = result[result['prediction'] == -1][['name', 'score']]
    return {
        "status": "success",
        "anomalies": anomalies.to_dict(orient='records')
    }
