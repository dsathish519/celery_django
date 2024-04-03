#!/bin/bash

echo "apply db migrations"

python manage.py migrate

exec "$@"