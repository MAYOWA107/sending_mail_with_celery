from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_celery.settings")

app = Celery("dj_celery_project")
app.conf.enable_utc = False
app.config_from_object(settings, namespace="CELERY")

# celery beat settings
app.conf.beat_shedule = {}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
