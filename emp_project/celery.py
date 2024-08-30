# myproject/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emp_project.settings')

app = Celery('emp_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-my-task-every-day': {
        'task': 'auth_app.tasks.my_scheduled_task',
        'schedule': crontab(minute="45", hour="9"),  # Executes every day at 7 AM
    },
}

app.conf.timezone = 'Africa/Lagos'


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
