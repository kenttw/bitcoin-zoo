BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# In Debug Mode this value be setting true 
CELERY_ALWAYS_EAGER = True


#celery setting
from datetime import timedelta
# CELERY_IMPORTS = ('bitcoin_task' , 'django_bitcoin' , )
CELERYBEAT_SCHEDULE = {
#     'add-every-1-seconds': {
#         'task': 'bitcoin_task.tasks.query_transactions',
#         'schedule': timedelta(seconds=10),
#         'args': (16, 16)
#     },
    'query_transactions': {
        'task': 'django_bitcoin.tasks.query_transactions',
        'schedule': timedelta(seconds=10),
#         'args': (16, 16)
    },
}