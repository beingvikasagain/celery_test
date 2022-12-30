from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE","celery_test.settings")
app = Celery("celery_test")
app.conf.update(
    {
        "broker_url":"amqp://root:root@rabbitmqserver",
        "task_serializer":"json",
        "task_acks_late":True,
        "result_serializer":"json",
        "result_backend":"django-db",
        "accept_content":["json"],
        "worker_prefetch_multiplier":1,
        "result_extended":True,
        "task_reject_on_worker_lost":True,
    }
)

app.conf.task_routes = {
    "main.tasks.task_check":{"queue":"low_priority"}
}

app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

# app.config_from_object(settings, namespace="CELERY")
app.conf.LOG_LEVEL = 'INFO'
app.conf.LOG_FILE = './log/celery.log'

