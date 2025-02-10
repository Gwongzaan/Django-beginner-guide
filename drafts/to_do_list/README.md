# review the development workflow of django development without unit testing and functional test

modesls
template, views, url config

# Development process

## start rought design by drafting a rough functional test

# Test Driven Development

It is recommended to practice this part using a separate project.

Briefly, the principle of Test Driven Development is **write tests before coding**

```shell
# run all test
python manage.py test

# run a specific test suits of an app
python manage.py test app-name
```

## functional test with selenium

### Install browser

- install browser, here we use google chrome

```shell

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

```

### download and unzip browser driver for selenium

```shell

wget https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

### install selenium

```shell
echo "selenium" >> requirements.txt
pip install -r requirements.txt

```

### `test_landing_page.py`

## unit test in Django

### Setting Up Testting in Django

Django detects test by searching for any file named test\*.py within your app

example structure

```shell


project
└── app
    └── tests
        ├── __init__.py
        ├── test_forms.py
        ├── test_models.py
        └── test_views.py

```

### Creating Unit Tests

use `django.test.TestCase`, which extends Python's `unittest.TestCase`

## Mocking and Fixtures

- **fixtures**: Predefine data you load before tests.
- **Mocking**: Use Python's unittest.mock to mock external dependencies

## Running Tests

## using Coverage

```shell
# installing coverage
echo "coverage" >> requirements.txt
pip install -r requirements.txt


# run tests with coverage
coverage run manage.py test
coverage report
coverage html

```

## difference between functional test and unit test

## TDD workflow and unit-test/code cycle

- FT
- Unit test
- unit-test/code cycle
- refactoring

## TDD rules

- Don nothing until you have a test
- One step at a time
- Don't test constant, unit test is about testing logic, flow control and configuration
- Each test should test one thing

## Testing the database and wiring up form to send a POST request

# Summary

## General Steps of Developing web applications with Django Framework

- **create project** with the command `django-admin startproject PROJECT-NAME PROJECT-PATH`

- **create app** with the command `python manage startapp APP-NAME` or `django-admin startapp APP-NAME`
- designing and implementng the app
  - create models
  - create templates
  - create views
  - URL configurations

## Test Driven Development

# References

https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey
https://docs.djangoproject.com/en/5.1/topics/http/urls/
https://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it

```

```
