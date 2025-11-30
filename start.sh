#!/bin/bash

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
ENV=${ENV:-development}

python manage.py migrate

if [ "$ENV" = "production" ]; then
    gunicorn entify_project.wsgi:application --bind ${HOST}:${PORT} --workers 3
else
    python manage.py runserver ${HOST}:${PORT}
fi