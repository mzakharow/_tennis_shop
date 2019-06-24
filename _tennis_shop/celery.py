import os
from celery import Celery
from django.conf import settings
# Основыне настройки Django для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_tennis_shop.settings')
app = Celery('_tennis_shop')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)