# 📂 model/train.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_model(data):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data)
    joblib.dump(model, 'model/isolation_model.pkl')
    print("✅ Model trained and saved.")

if __name__ == "__main__":
    df = pd.read_csv('training_data.csv')
    train_model(df[['cpu', 'mem', 'net_rx', 'net_tx']])
