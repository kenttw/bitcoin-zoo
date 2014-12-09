# -*- coding: utf-8 -*-
'''
Created on 2014年12月9日

@author: kent
'''
from __future__ import absolute_import

from celery import Celery





CELERY_TIMEZONE = 'UTC'

app = Celery('bitcoin_task',
             broker='redis://localhost/',
             backend='amqp://',
             include=['bitcoin_task.tasks'])

app.config_from_object('bitcoin_task.celeryconfig')

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()