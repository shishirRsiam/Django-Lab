#!/bin/bash

echo "..................Starting cron service.................."
service cron start

echo "..................Adding Django cron jobs.................."
python manage.py crontab remove  # Clean stale ones
python manage.py crontab add

echo "..................Starting Django server.................."
python manage.py runserver 0.0.0.0:8000
