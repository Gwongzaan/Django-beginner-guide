#!/bin/sh

until cd $APP_HOME
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A project beat --loglevel=info