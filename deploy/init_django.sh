#!/usr/bin/env bash

python manage.py makemigrations django_survey
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@d1g1t.com', '@pacoca123')" | python manage.py shell
python manage.py runserver 0.0.0.0:9000