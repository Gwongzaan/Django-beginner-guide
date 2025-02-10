# Key development process

```shell
mdkir API && cd API
django-admin startproject books .
python manage.py startapp users
python manage.py startapp book

# create model UserProfile,
# configure settings.AUTH_USER_MODEL='users.UserProfile'

python manage.py makemigrations
# create test cases
```

one CRUD one API, with different method: GET/POST/PUT/DELETE/PATCH
resources oriented, using nouns, not verbs,
versioning,
responsive status code
add parameters to API
return value
error info

# [Building an API](https://blog.postman.com/how-to-build-an-api/)

tools : postman

RESTAPI

API design and implementation

you can think of it as a command sets for user to interact with your database

# Development

## [API Design](https://www.postman.com/api-platform/api-design/)

- determine API's use case. What to do with the API, what resources are being used.
- determine structure of API. Understand how resources are related to each other, Determine on data format.

## Implementation

- Framework
- Language
- create models and migrations
- Define routes
- Build controllers. Implement logic to handle requests and interact with your models

## TEST

[DRF](https://www.django-rest-framework.org/)
10 common components

## KEY

- serialization

# wrapping views

`mixins.ListModelMixin` + `GenericAPIView`
