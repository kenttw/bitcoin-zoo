# -*- coding: utf-8 -*-
'''
Created on 2014年12月9日

@author: kent
'''
from __future__ import absolute_import
from celery import shared_task
# from django_bitcoin import tasks
# from celery.contrib import rdb

@shared_task
def query_transactions(x,y):
#     rdb.set_trace()  # <- set breakpoint
#     tasks.query_transactions()
    return x+y





