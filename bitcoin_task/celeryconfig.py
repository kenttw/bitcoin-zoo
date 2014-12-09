from datetime import timedelta

# List of modules to import when celery starts.
CELERY_IMPORTS = ('bitcoin_task.tasks', )

# Result store settings.
# CELERY_RESULT_BACKEND = 'database'
# CELERY_RESULT_DBURI = 'sqlite:///mydatabase.db'

# Broker settings.
# BROKER_TRANSPORT = 'redis'
# BROKER_HOST = 'redis://localhost/'
# BROKER_PORT = 5672
# BROKER_VHOST = '/'
# BROKER_USER = 'guest'
# BROKER_PASSWORD = 'guest'

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'bitcoin_task.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    },
                       
    #query_transactions                       
#     'add-every-30-seconds': {
#         'task': 'bitcoin_task.tasks.query_transactions',
#         'schedule': timedelta(seconds=10),
#         'args': (16, 16)
#     },
}

## Worker settings
# CELERYD_CONCURRENCY = 1
# CELERYD_TASK_TIME_LIMIT = 20
# CELERYD_LOG_FILE = 'celeryd.log'
# CELERYD_LOG_LEVEL = 'DEBUG'