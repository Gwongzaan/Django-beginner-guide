#!/bin/sh

until cd $APP_HOME
do
    echo "Waiting for server volume..."
done

#source $APP_HOME/config/web/wait_for_it.sh

until python manage.py makemigrations
do
    echo "Waiting for makemigrations"
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 60
done

python manage.py collectstatic --noinput

cat << EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='mog').exists() or User.objects.create_superuser('mog', 'mog@sixdigit.net', '93k67y87s70t')

EOF


# run in production env
gunicorn project.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --reload
