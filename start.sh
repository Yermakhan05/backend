# start.sh
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
daphne backend.asgi:application --port $PORT --bind 0.0.0.0
