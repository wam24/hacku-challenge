#!/bin/sh

python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE --noinput \
&& python manage.py collectstatic --noinput


