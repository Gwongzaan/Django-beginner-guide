# design

barely no UI design

## Features

- creating posts/articles in the admin interfaces
- displaying title of blogs
- dispalying content/detail of each blog

# Test Driven Development and Key Steps

```shell
#
# initialize project
#
cd pure-projects/simple-single-user-blog
django-admin startproject proj .

#
# setup functional test for testing landing page
#
mkdir FT
touch FT/test_landing_page.py

# test landing page,
python manage.py runserver 0.0.0.0:8000
python FT/test_landing_page.py

#
# setup static and media directories
#
mkdir static
cd static
mkdir js css img
mkdir media

#
# setup project-wide templates
#
mkdir templates
touch templates/base.html
touch templates/header.html
touch templates/footer.html

#
# setup application blog
#
python manage.py startapp blog

# application wide templates
mkdir blog/templates/blog
touch blog/templates/blog/titles.html
touch blog/templates/blog/detail.html

# application URLconf
touch blog/urls.py

# tests
rm blog/tests.py
mkdir blog/tests
touch blog/tests/__init__.py


# register application blog
#
# create a model class named Blog
# for testing purpose, makemigrations is enough
#
python manage.py makemigrations

# create test cases and test
touch blog/tests/test_model_blog.py
python manage.py test blog/tests
python manage.py test

```
