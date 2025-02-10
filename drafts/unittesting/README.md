# Unit Test in Django

# Setting Up Testting in Django

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

# Testing Views

## Testing a Simple View

```python
# views.py
from django.http import HttpResponse

def my_view(request):

```

#### Testing a View with a Template

```python
# views.py
from django.http import HttpResponse


def my_view(request):
    return HttpResponse(request, "Hello, world")

# tests/test_views.py

# test_views.py
from django.test import TestCase
from django.urls import reverse


class SimpleViewTestCase(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse("my_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world")
```

#### Testing a View with Query parameters

#### Testing a View with Form submission

#### Testing Login Protected View

#### Testing API Views (JSON Response)

#### Testing Views with Context Data

#### common Assertions in View Tests

- Response status
- Redirect URL
- Template usage
- String in response
- JSON response

# Testing Models

## Basic Structure for Model Tests

## Testing Model Field Values

## Testing `save()` behavior

if you've overriden the `save` method, ensure it's tested

## testing Custome Model Methods

if your model includes custoemr methods, write tests to validate their behavior.

## Testing `__str__` Representation

the `__str__` defines how a model installing is displayed as a string

## Testing Constraints

ensure the validate database constraints if there's any

## Testing Signals

test signal behavior, such as `post_save`, `pre_save`

## Testing Querysets

Vtest customized queryset behavior

## using fixtures for data

## Common assertions in Model Tests

```python
# check equality of values

# ensure and instance exists

# count items in the database

# check if a query raises an exceptions

```

# Testing Forms

## basic structure for form tests

## Testing form validation

## Testing form cleaning logic

## Testing models forms

## testing form rendering

## Testing initial data

## testing file upload forms

## common assertions in form tests

```python

# check if the form is valid

# check erros on specific fields

# check non-filed errors

# validates cleaned data
```

# Mocking and Fixtures

- **fixtures**: Predefine data you load before tests.
- **Mocking**: Use Python's unittest.mock to mock external dependencies

# Running Tests

# using Coverage

```shell
# installing coverage
echo "coverage" >> requirements.txt
pip install -r requirements.txt


# run tests with coverage
coverage run manage.py test
coverage report
coverage html

```
