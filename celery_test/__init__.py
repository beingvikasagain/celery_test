import warnings

from .celery import app as celery_app

warnings.filterwarnings(action='ignore')

__all__ = ("celery_app",)

