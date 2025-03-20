# 📂 data_collector/docker_stats.py
import docker
import pandas as pd

client = docker.from_env()

def collect_metrics():
    stats = []
    for container in client.containers.list():
        data = container.stats(stream=False)
        stats.append({
            'id': container.id,
            'name': container.name,
            'cpu': data['cpu_stats']['cpu_usage']['total_usage'],
            'mem': data['memory_stats']['usage'],
            'net_rx': data['networks']['eth0']['rx_bytes'],
            'net_tx': data['networks']['eth0']['tx_bytes']
        })
    return pd.DataFrame(stats)
