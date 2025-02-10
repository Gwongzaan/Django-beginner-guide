#!/bin/sh
until cd $APP_HOME
do
    echo "Waiting for server volume..."
done

celery -A project worker --loglevel=info --concurrency 1 -E