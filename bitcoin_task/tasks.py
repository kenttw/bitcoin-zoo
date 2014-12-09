# -*- coding: utf-8 -*-
'''
Created on 2014年12月9日

@author: kent
'''
from __future__ import absolute_import
from celery.contrib import rdb

from bitcoin_task.celery import app
# from django_bitcoin.tasks import query_transactions

@app.task
def add(x, y):
#     query_transactions()
    rdb.set_trace()  # <- set breakpoint
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

