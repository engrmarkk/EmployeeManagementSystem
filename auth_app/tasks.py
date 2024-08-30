from celery import shared_task
from datetime import datetime


@shared_task
def add(x, y):
    return x + y


@shared_task
def test_task():
    print("Test task executed")


@shared_task
def my_scheduled_task():
    print(datetime.now(), "Cronjob Task Executed Date")
    print("Cronjob Task Executed")
