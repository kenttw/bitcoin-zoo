# bitcoin-zoo

## How to Install

```
sudo apt-get install build-essential python-dev libmysqlclient-dev
sudo pip install -r requirement.txt
python manage.py  schemamigration django_bitcoin --initial
python manage.py syncdb
python manage.py migrate
python manage.py  runserver_plus 0.0.0.0:8000
python manage.py check_permissions
# this line is for userena bug
# Permission matching query does not exist
[open http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)
```

## How to Use