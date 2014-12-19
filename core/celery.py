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

app = Celery('core')


# read celery setting from another files
# don't put those settings in this file
# and hard wirting them in app function call
# ex.
#     app = Celery('xx', borker='..', ..)
#
app.config_from_object('core.celeryconfig')
# this will autodiscover the task (the file name is tasks under each directory)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
