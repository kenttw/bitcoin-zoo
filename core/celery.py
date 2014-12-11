# -*- coding: utf-8 -*-
'''
Created on 2014年12月9日

@author: kent
'''
from __future__ import absolute_import
from celery import Celery
import os
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
CELERY_RDB_HOST = '127.0.0.1'
CELERY_RDB_PORT = 6899
CELERY_TIMEZONE = 'UTC'

app = Celery('bitcoin_task',
             broker='redis://localhost/',
#             backend='amqp://',
             include=['bitcoin_task.tasks'])

# app.config_from_object('bitcoin_task.celeryconfig')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)
app.conf.update(
    CELERY_RESULT_BACKEND='redis://localhost/',
)
# app.conf.update(
#     CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend',
# )


#celery setting
from datetime import timedelta
CELERY_IMPORTS = ('bitcoin_task.tasks', )
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'bitcoin_task.tasks.query_transactions',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()