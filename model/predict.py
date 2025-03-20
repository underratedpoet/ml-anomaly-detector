# 📂 model/predict.py
import pandas as pd
import joblib
from data_collector.docker_stats import collect_metrics
from alerting.email_alert import send_email_alert

def realtime_detection():
    model = joblib.load('model/isolation_model.pkl')
    metrics = collect_metrics()
    preds = model.predict(metrics[['cpu', 'mem', 'net_rx', 'net_tx']])
    scores = model.decision_function(metrics[['cpu', 'mem', 'net_rx', 'net_tx']])
    
    for idx, pred in enumerate(preds):
        if pred == -1:
            container = metrics.iloc[idx]
            send_email_alert(container['name'], scores[idx])
    
    return metrics.assign(prediction=preds, score=scores)

if __name__ == "__main__":
    realtime_detection()
