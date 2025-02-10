django-admin startproject <project_name>
cd <project_name>
python manage.py migrate
python manage.py runserver
python manage.py startapp books
python manage.py makemigrations <app>
python manage.py migrate

Model -> View -> URL -> template

python manage.py collectstatic

build a basic skeleton, then deploy to the web, and IC

SPAs(Single Page Apps)

CORS (Corss-Origin Resource Sharing):
refers to the fact that
whenever a client interfaces with an API hosted on a different domain or port there are potential security issues.

CORS requires the web server to include specific HTTP headers that allow for the client to determine if and when
cross-domain requests should be allowed. Because we are using
a SPA architecture the front-end will be on a different local port during development and a
completely different domain once deployed!

CSRF
when dealing with forms

security at project-level, view-level, individual model level

User Authentication

- Basic Authentication
  - when a client makes an HTTP request, it is forced to send an approved authentication credential before access is granted
- session
- token
- default
