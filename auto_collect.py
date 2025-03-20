import docker
import pandas as pd
import time

client = docker.from_env()

def collect_snapshot(iteration):
    stats = []
    for container in client.containers.list():
        try:
            data = container.stats(stream=False)
            stats.append({
                'container': container.name,
                'cpu': data['cpu_stats']['cpu_usage']['total_usage'],
                'mem': data['memory_stats']['usage'],
                'net_rx': data['networks']['eth0']['rx_bytes'],
                'net_tx': data['networks']['eth0']['tx_bytes']
            })
        except Exception as e:
            print(f"⚠️ Error collecting from {container.name}: {e}")
    print(f"✅ Snapshot {iteration} collected: {len(stats)} containers")
    return stats

if __name__ == "__main__":
    snapshots = []
    total_iterations = 60
    print(f"🚀 Starting auto-collection for {total_iterations} iterations (approx {total_iterations * 10} seconds)")

    for i in range(1, total_iterations + 1):
        batch = collect_snapshot(i)
        snapshots.extend(batch)
        print(f"📊 Progress: {i}/{total_iterations} iterations complete.")
        time.sleep(10)

    df = pd.DataFrame(snapshots)
    output_file = '/app/data/training_data.csv'
    df.to_csv(output_file, index=False)
    print(f"✅ Training data collected successfully to {output_file}")
