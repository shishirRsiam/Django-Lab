# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Install cron
RUN apt-get update && apt-get install -y cron

# Create cron log file
RUN touch /var/log/cron.log

# Give execution rights
RUN chmod +x /app/manage.py

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Entrypoint that starts cron + Django
ENTRYPOINT ["/entrypoint.sh"]
