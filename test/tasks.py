# -*- coding: utf-8 -*-
'''
Created on 2014年11月28日

@author: kent
'''
from celery import Celery
from celery import task

app = Celery('tasks', broker='redis://localhost/')

@app.task
def add(x, y):
    return x + y