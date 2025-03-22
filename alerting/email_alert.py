# 📂 alerting/email_alert.py
import smtplib
from email.mime.text import MIMEText

def send_email_alert(container_name, score):
    msg = MIMEText(f"🚨 Anomaly detected in container: {container_name}\nAnomaly score: {score}")
    msg['Subject'] = f'🚨 Docker Anomaly Alert: {container_name}'
    msg['From'] = 'monitor@system.local'
    msg['To'] = 'danielmaksimencko@yandex.ru'

    with smtplib.SMTP('mailhog', 1025) as server:
        server.send_message(msg)
    print(f"📨 Email alert sent for {container_name}")
