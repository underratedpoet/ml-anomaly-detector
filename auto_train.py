# 📂 ml-anomaly-detector/auto_train.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

output_file = '/app/data/training_data.csv'
df = pd.read_csv(output_file)
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['cpu', 'mem', 'net_rx', 'net_tx']])
joblib.dump(model, '/app/data/isolation_model.pkl')
print("✅ Model trained and saved.")
