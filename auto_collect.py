# 📂 ml-anomaly-detector/auto_collect.py
import docker
import pandas as pd
import time

client = docker.from_env()

def collect_snapshot():
    stats = []
    for container in client.containers.list():
        try:
            data = container.stats(stream=False)
            stats.append({
                'cpu': data['cpu_stats']['cpu_usage']['total_usage'],
                'mem': data['memory_stats']['usage'],
                'net_rx': data['networks']['eth0']['rx_bytes'],
                'net_tx': data['networks']['eth0']['tx_bytes']
            })
        except Exception as e:
            print(f"⚠️ Error collecting from {container.name}: {e}")
    return stats

if __name__ == "__main__":
    snapshots = []
    for _ in range(60):  # Собираем 60 замеров раз в 10 секунд (~10 мин нормального поведения)
        snapshots.extend(collect_snapshot())
        time.sleep(10)

    df = pd.DataFrame(snapshots)
    df.to_csv('training_data.csv', index=False)
    print("✅ Training data collected to training_data.csv")
