# myapp/cron.py
from datetime import datetime
from django.utils import timezone


def my_scheduled_job():
    with open('/app/cron_log.txt', 'a') as f:
        f.write(f"Cron ran at {datetime.now()}\n")

    print("Running cron job")
    print(f"Running cron job at {timezone.now()}")
    print('\n' * 3)
    # Do your scheduled task here
