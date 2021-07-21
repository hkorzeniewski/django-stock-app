# celery.py
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler# default django settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangostockapp.settings')

app = Celery('djangostockapp')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
