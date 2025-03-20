# 📜 Dockerfile
FROM python:3.12-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y gcc libffi-dev python3-dev \
    && pip install --no-cache-dir pandas scikit-learn docker fastapi uvicorn joblib
# Установим cron
RUN apt-get update && apt-get install -y cron
COPY crontab /etc/cron.d/anomaly-cron
RUN chmod 0644 /etc/cron.d/anomaly-cron && crontab /etc/cron.d/anomaly-cron

# Копируем код
WORKDIR /app
COPY . /app

# Экспонируем порт FastAPI
EXPOSE 8000

# Команда запуска FastAPI + Cron Detection (опционально)
CMD ["uvicorn", "dashboard.app:app", "--host", "0.0.0.0", "--port", "8000"]
