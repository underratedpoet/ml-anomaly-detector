# 📂 ml-anomaly-detector/auto_train.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv('training_data.csv')
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['cpu', 'mem', 'net_rx', 'net_tx']])
joblib.dump(model, 'isolation_model.pkl')
print("✅ Model trained and saved.")
