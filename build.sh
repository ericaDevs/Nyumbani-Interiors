#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata initial_data.json || true
python manage.py fill_slugs || true
python manage.py setup_admin || true
