from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primo.settings')

app = Celery('primo', broker='amqp://guest@localhost//')
#app = Celery('primo')
#app = Celery('primo', broker='amqp://guest@localhost//', backend='amqp')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Si tenemos nuestras tareas en un fichero de nombre tasks.py, esto nos permite indicarle a celery que encuentre automáticamente dicho módulo dentro del proyecto.
# De este modo no tenemos que añadirlo a la variable CELERY_IMPORTS del settings
app.autodiscover_tasks()