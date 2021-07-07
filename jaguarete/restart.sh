#!/bin/bash

python manage.py makemigrations 
python manage.py migrate
python manage.py thumbnail cleanup
python manage.py runserver