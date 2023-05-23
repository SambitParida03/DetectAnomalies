#!/bin/sh

gunicorn --worker-class gevent --workers 3 --bind 0.0.0.0:5001 wsgi:app --timeout 1000000
# gunicorn --conf ./gunicorn_conf.py --bind 0.0.0.0:5001 wsgi:app
