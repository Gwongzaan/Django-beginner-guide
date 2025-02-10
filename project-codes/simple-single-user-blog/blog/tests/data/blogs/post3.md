# Multi-user blog-system

# location of templates and static files

- defining location of tempaltes. project-wide, app-wide
- admin templates
- base templates, tempalte inhreitance, header.html, footer.html, base.html
- defining location of static files
- defining static files, files such as java scripts, css files,

# definiing location for themlates

edit `settings.py`,

look for `TEMPLATES` IN THE FILE,

read the following codde snipet take from the file

create a fdirectory named `templates` right in the project root

and add the path in to the list of `DIRS`

In General, there are two ways of setting up the templates
_project-wise_ and _app-wise_

configuration is done in `settings.py`

```python

TEMPLATES = {
    'DIRS': [],
    "APP": True
}
```

by default, Django will look at the `BASE_DIR/templates` directorty first,
then look at the `templates` directory in each apps until it finds the template
if tempelate not found, it will raise and exception/error.

### project-wise example

```shell

BASE_DIR/templates/base.html
BASE_DIR/templates/footer.html
BASE_DIR/templates/*.html

BASE*DIR/templates/app1/*.html
BASE*DIR/templates/app2/*.html

```

### app-wise example

```shell

BASE_DIR/app/templates/app/*.html
```

in our example, we'll both suing project-wise and app-wise
for the project-wide templates,
such as the base.html, header.html, footer.html, we'll place it in the Project templates

for those close related to each app, we'll have it in the app templates
to avoid name conflict, structure the templates as `BASE_DIR/templates/app-name/*.html`

```python


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
# 'DIRS' defineds search paths for Django to look for templates
    # 'BAS_DIR is the path of the project root'
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],

# if `APP_DIRS` is False, Django will not search for templates in the app/templates
# by setting it to True, Django will search for templates in the  applications templates directory as well
    # if you configure a application wide templates , then you will need to set it True,
    # other wise, django will not be able to search for templates defined in the app/templates

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

common ptractise of setting up templates structure
root templates at the project root for templates defined for projdect wides
app/templates/app/ for app specifict templates
the reason of adding a directory `app` in the app/templates/ is to areduce naming conflicts
say both app1 and app2 hhave a template named base.html, if not uisng the middle directory, it will
cause naming confilcts

play with it and see different result, ssuch as setting `APP_DIRS` TO False

restart the Django server

# defining location for static files

In web development, we will usually called CSS files, java scripts files and images being displayed as staic files.

the locations for static files are defined by the variable `STATICFILES_DIR` in `settings.py`

look at code snippet from `settings.py`

```python


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# by default, STATIC_URL  IS 'static/', by you can change it per your requirement:
# by setting up this variables, you can access statid files via user like
# http://your-site-domain/static/your-static-file-name
STATIC_URL = "static/"

# in our tutorial we are placing all static files in sa static foloer  right in the project root
# thereore, we'll add the following variable to defined search path of static files for Django
# if you have more than one path for static files, you can add to `STATICFILES_DIRS`, then
# django will search for tiles in these path defined in the variables

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

```

test it out by placing a file named `test.txt` or any file you want, and type 'localhost:8000/static/test.txt'

you should see the conntent of the file

by default, Django uses varialbe `STATICFILES_FINDERS` to define how to search for static files, by setting it to

```python
STATICFILES_FINDERS = [

    'django.contrib.staticfiles.finders.FileSystemFinders',
    'django.caution.staticfiles.finders.AppDirectoriesFinders',
]
```

with this definition/configuration,

Django will first search for static files per `STATICFILES_DIRS`

in ptractise, static files are usually put in one directory, and split files into diffeent sub-directory
for different purpose

# puting booststrap static files local

go to the official website of booststrap and download the bundle(css, js), extract to the static directory

# layout of your webpage

in general, a webpage can be divided into three part,

- header
- content
- footer

header.html

- {% load static %}

```html
{% load static %}

<div class="container">
  <nav class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="https://www.google.com">
        <img src="{% static '/images/logo.png' %}" width="100px" />
      </a>
    </div>
    <div>
      <ul class="nav navbar-nav" role="navigation">
        <li><a href="{% url 'blog:titles' %}">BLOG</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">LOGIN</a></li>
      </ul>
    </div>
  </nav>
</div>
```

footer.html

```html
<div class="container">
  <hr />
  <p class="text-center">copy right</p>
</div>
```

base.html

```html
{% load static %}
<! DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" />
  </head>
  <body>
    {% include "header.html" %}
    <div class="container">{% block content %}{% endblock %}</div>
    {% include "footer.html" %} {% block javascript %}{% endblock %}
  </body>
</html>
```

## URLconf

there are two way of URLconf

````python


### two way of URLconf

```python

# method 1
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    ]

# blog/urls.py
    urlpatterns = [
        path('', views.titles, name='titles'),
        path('<int:article_id>/', views.post, name='post'),
    ]

# method 2
    urlpatterns = [
        path('admin/', admin.site.urls),
        #path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
        path('blog/', include('blog.urls', namespace='blog')),
    ]

# blog/urls.py
    app_name = "blog"
    urlpatterns = [
        path('', views.titles, name='titles'),
        path('<int:article_id>/', views.post, name='post'),
    ]
````

# user login

we have admin page for admin login, but with a multi-user blog system, we also need user login for common user

- `account` app
- form, form class, response to a form request, binded form, unbind form
- login view

## create `account` app

## urlconf

```python


# simple/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
    path("account", include(("account.urls", "account"), namespace="account")),
]

# accounyt/urls.py

from account import views
from django.urls import path

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
]
```

# understanding Form class

execute the following in interactive mode to have a feel of Form

requext-response cycle of FORM

client request pages contain form
server decide if it is GET or POST,
if it is GET request, response a unbinded form to client, and client fill out the form, and submit the form
if it is POST request, it means client fileed out and submit the form, serer validate the data,
if invalid data, return error message to client
if valid, save the data and return succe3sfully or redirect

```python

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
```

```python
from account.forms import LoginForm
# not passing parameters, this kind of form is unbinded form
login_form = LoginForm()
print(Login_form)

```

`username=forms.CharField()` map to `<input name='username' type='text'...>`

`dir(login_form)` to see other attributes and methods

if we pass parameters to the form, it is binded form

```python
login_data = {'username': "laksdjfsd", 'password': 'aslkdfjalsf'}
login_form = LoginForm(login_data)
login_form.is_bound

login_form.cleaned_data


error_data = {"username": "jlkasdf", 'password':''}
error = LoginForm(error_data)
error.is_valid()


```

# login function view

rlogin procedure

two type of request, GET, POST

- client request
- if request if GET, return LoginForm,
- if request is POST, validate login data
- if login_daqta invalid, return to loginform with error message
- otherwise login succe3sfully

```python

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

# Create your views here.


def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            user = authenticate(
                username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user:
                login(request, user)
                return HttpResponse("Welocome")

            else:
                return HttpResponse("username or password is not right")

        else:
            return HttpResponse("Invalid login")
```

user management is complex, but Django has some built-in application for user management
such as `authenticate()` , `login()`

```html
{% extends "base.html" %}
<br />

{% block title %}Login{% endblock %}
<br />

{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Login</h1>
  <p>Input your username and password</p>
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <br />
    {{ form.as_p}}
    <input type="submit" value="Login" />
  </form>
</div>
{% endblock %}
```

then you will need to create a user for testing. login as superuser, and create a suer

edit the header.html so the `Login` is can lead you to the login page

```html
{% load static %}

<div class="container">
  <nav class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="https://www.google.com">
        <img src="{% static '/images/logo.png' %}" width="100px" />
      </a>
    </div>
    <div>
      <ul class="nav navbar-nav" role="navigation">
        <li><a href="{% url 'blog:titles' %}">BLOG</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="{% url 'account:user_login' %}">LOGIN</a></li>
      </ul>
    </div>
  </nav>
</div>
```

make the login page pretty, it is on you to try it out

```html
{% extends "base.html" %}
<br />
{% load static%}
<br />
{% block title %}Login{% endblock %} {% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Login</h1>
  <p>Input your username and password</p>
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <! -- {{ form.as_p}}-->
    <div class="form-group">
      <label
        for="{{ form.username.id_for_label }}"
        class="col-md-5 control-label"
        style="color:red"
      >
        <span class="glyphicon glyphicon-user"></span>Username</label
      >
      <div class="col-md-6 text-left">{{ form.username }}</div>
    </div>
    <div class="form-group">
      <label
        for="{{ form.password.id_for_label }}"
        class="col-md-5 control-label"
        style="color:blue"
      >
        <span class="glyphicon glyphicon-floppy-open"></span>Password</label
      >
      <div class="col-md-6 text-left">{{ form.password }}</div>
    </div>
    <input type="submit" class="btn btn-primary btn-lg" value="Login" />
  </form>
</div>
{% endblock %}
```

# implementing login and logout using the built-in medhod

LoginView, LogoutView

edit `account/urls.py`

```python

from account import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # path("login/", views.user_login, name="user_login"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login2.html"),
        name="user_login",
    ),
]
```

```html
{% extends "base.html" %}
<br />
{% load static%}
<br />
{% block title %}Login{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Login</h1>

  {% if form.errors %} #①
  <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  <p>Input your username and password</p>
  <form
    class="form-horizontal"
    action="{% url 'account:user_login' %}"
    method="post"
  >
    {% csrf_token %}
    <div class="form-group">
      <label
        for="{{ form.username.id_for_label }}"
        class="col-md-5 control-label"
        style="color: red"
      >
        <span class="glyphicon glyphicon-user"></span>Username</label
      >
      <div class="col-md-6 text-left">{{ form.username }}</div>
    </div>
    <div class="form-group">
      <label
        for="{{ form.password.id_for_label }}"
        class="col-md-5 control-label"
        style="color: blue"
      >
        <span class="glyphicon glyphicon-floppy-open"></span>Password</label
      >
      <div class="col-md-6 text-left">{{ form.password }}</div>
    </div>
    <input type="submit" class="btn btn-primary btn-lg" value="Login" />
  </form>
</div>
{% endblock %}
```

you will also need to configure `settings.py`

```python
LOGIN_REDIRECT_URL = "/blog/"

```

# determine if user is login or not

edit `header.html`

```html

{% load static %}

<div class="container">
  <nav class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="https://www.google.com">
        <img src="{% static '/images/logo.png' %}" width="100px" />
      </a>
    </div>
    <div>
      <ul class="nav navbar-nav" role="navigation">
        <li><a href="{% url 'blog:titles' %}">BLOG</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
<!-- determine if user login-->
        {% if user.is_authenticated %}
          <li><a href="#"{{user.username}}</a></li>
          <form method='post' action="{% url account:user_logout %}" id="logout">

          <li><a href="#" onclick="document.getElementByID('logout).submit();">Logout</a></li>
        </form>

        {% else %}
        <li><a href="{% url 'account:user_login' %}">LOGIN</a></li>
        {% endif %}
      </ul>
    </div>
  </nav>
</div>
```

### built-in logout method

```python
# account/urls.py
    path("logout/", auth_views.LogoutView.as_view(), name="user_logout"),


```

edit `header.html`

define 'logout.html'

```html
{% extends "base.html" %}
<br />
{% block title %}Logout{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <p>You have log out.</p>
  <p>You can <a href="{% url 'account:user_login'%}">login</a> again</p>
</div>
{% endblock %}
```

```python

    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="account/logout.html"),
        name="user_logout",
    ),
```

### simple regirstration

it is a little bit more complex than the Loginform we created

```python

# by importing django built-in User model, we don't need to create our own User model
from django.contrib.auth.models import User


# difference bwtween forms.ModelForm and forms.Form
# in general, if data from the form are to be stored in the database, use ModelForm
# otherwise inherit Form is enough

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

  # inner class
  # it declared what model is used by this form, and what fields of the model are used
    class meta:
        model = User
        fields = ('username', 'email')

  # check if the password match,

    def clearn_passwords(self):
        cd = self.clearned_data
        if cd]'password' != cd['password2']:
            raise forms.ValidationError("passwords do not match")
        return cd['password2']
```

`views.py`

```python


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
      # ModelForm aand its subclass have `save()` method, it is to saved the form data in database
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return HttpResponse("register successfully")

        else:
            return HttpResponse("failed to register")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form})
```

extend the RegistrationForm

```python


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"user {self.user.username}"
```

```shell
python manage.py makemigrations account
python manage.py migrate account
```

```python


class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "phone",
            "birth",
        )
```

```python



def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        user_profile_form = userProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = new_user
            user_profile.save()
            return HttpResponse("register successfully")

        else:
            return HttpResponse("failed to register")
    else:
        user_form = RegistrationForm()
        user_profile_form = userProfileForm()
        return render(request, "account/register.html", {"form": user_form})
```

```html
{% extends "base.html" %}
<br />
{% load static %}
<br />
{% block title %}register user{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Register</h1>
  <p>
    If you are a user,
    <strong><a href="{% url 'account:user_login' %}">Login</a> </strong>, please
  </p>
  <p>or register.</p>
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <div class="form-group">
      <label
        for="{{ form.username.id_for_label }}"
        class="col-md-5 control-label"
      >
        Username</label
      >
      <div class="col-md-6 text-left">{{ form.username }}</div>
    </div>
    <div class="form-group">
      <label for="{{ form.email.id_for_label }}" class="col-md-5 control-label">
        Email</label
      >
      <div class="col-md-6 text-left">{{ form.email }}</div>
    </div>
    <div class="form-group">
      <label
        for="{{ form.password.id_for_label }}"
        class="col-md-5 control-label"
      >
        Password</label
      >
      <div class="col-md-6 text-left">{{ form.password }}</div>
    </div>
    <div class="form-group">
      <label
        for="{{ form.password.id_for_label }}"
        class="col-md-5 control-label"
      >
        Confirm Password</label
      >
      <div class="col-md-6 text-left">{{ form.password2 }}</div>
    </div>

    <div class="form-group">
      <label for="{{profile.birth.id_for_label}}" class="col-md-6 text-left"
        >Birth Date</label
      >
      <div class="col-md-6 text-left">{{profile.birth}}</div>
    </div>
    <div class="form-group">
      <label for="{{profile.phone.id_for_label}}" class="col-md-6 text-left"
        >Phone</label
      >
      <div class="col-md-6 text-left">{{profile.phone}}</div>
    </div>
    <input type="submit" class="btn btn-primary btn-lg" value="REGISTER" />
  </form>
</div>
{% endblock %}
```

manage extended registriation content

```python

# account/admin.py

from django.contrib import admin

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth",
        "phone",
    )

    list_filter = ("phone",)


admin.site.Register(UserProfile, UserProfileAdmin)
```

## ref

[user registration](https://django-registration.readthedocs.io/en/stable/)
[Django social auth](https://github.com/omab/django-social-auth)
[modle field reference](https://docs.djangoproject.com/en/5.1/ref/models/fields)

# operation related to password

- change password
- reset password
- email
- third party app

- change password

1. determine if user is login, only those login can change password
2. display page to change password,`password_change_form.html`
3. submit new password `password_change_done.html`
4. feedback to client, if password is changed successflly

we are using built-in function to change password, so there is no need to code a view for it.

we will implement the webpage for submitting new password first.

that is create `password_cange_form.html`

```html
<!-- page to submit password -->
{% extends "base.html" %}
<br />
{% block title %}passowrd change{% endblock %}
<br />
{% block content %}

<div class="row text-center vertical-middle-sm">
  <h1>Change Password</h1>
  <p>
    Please enter your old password, for security's sake, and then enter your new
    password twice so we can verify you typed it in correctly.
  </p>
  {% if form.new_password1.help_text %}
  <div class="text-left" style="margin-left: 400px">
    <p>{{ form.new_password1.help_text|safe }}</p>
  </div>
  {% endif %}
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <div class="form-group">
      <label class="col-md-5 control-label text-right">
        {{ form.old_password.label_tag }}
      </label>
      <div class="col-md-6 text-left">{{ form.old_password }}</div>
    </div>

    <div class="form-group">
      <label class="col-md-5 control-label text-right">
        {{ form.new_password1.label_tag }}
      </label>
      <div class="col-md-6 text-left">{{ form.new_password1 }}</div>
    </div>

    <div class="form-group">
      <label class="col-md-5 control-label text-right">
        {{ form.new_password2.label_tag }}
      </label>
      <div class="col-md-6 text-left">{{ form.new_password2 }}</div>
    </div>
    <input
      type="submit"
      value="Change my password"
      class="btn btn-primary btn-lg"
    />
  </form>
</div>
{% endblock %}
```

then we will implement the webpage of password-changed

`password_change_done.html`

```html
{% extends "base.html" %}
<br />
{% block title %}password change done{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <p>Your password was changed.</p>
</div>
{% endblock %}
```

then configure the URL

what if user not login and want to change password, the `?=next=`
when user login, redirect to the `next` url

in the `settings.py` add `LOGIN_URL='/account/login/`

to make it redirect correctly, we'll need to modify `login2.html`

the paattern of 'vist a page' -> 'redirect to login' -> 'redirect after login' are useful not only in this scenario

```html

{% extends "base.html" %}
<br />
{% load static%}
<br />
{% block title %}Login{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Login</h1>

  {% if form.errors %} #①
  <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  <p>Input your username and password</p>

  {% if next %}
<form
    class='form-horizontal'
action="{% url 'account:user_login' %}?next={{next}}"
    method='post'
    >

    {% else%}


  <form
    class="form-horizontal"
    action="{% url 'account:user_login' %}"
    method="post"
  >
    {% endif%}
    {% csrf_token %}
    <div class="form-group">
      <label
        for="{{ form.username.id_for_label }}"
        class="col-md-5 control-label"
        style="color: red"
      >
        <span class="glyphicon glyphicon-user"></span>Username</label
      >
      <div class="col-md-6 text-left">{{ form.username }}</div>
    </div>
    <div class="form-group">
      <label
        for="{{ form.password.id_for_label }}"
        class="col-md-5 control-label"
        style="color: blue"
      >
        <span class="glyphicon glyphicon-floppy-open"></span>Password</label
      >
      <div class="col-md-6 text-left">{{ form.password }}</div>
    </div>
    <input type="submit" class="btn btn-primary btn-lg" value="Login" />
  </form>
</div>
{% endblock %}
```

edit `header.html`

```html
{% load static %}

<div class="container">
  <nav class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="https://www.google.com">
        <img src="{% static '/images/logo.png' %}" width="100px" />
      </a>
    </div>
    <div>
      <ul class="nav navbar-nav" role="navigation">
        <li><a href="{% url 'blog:titles' %}">BLOG</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        {% if user.is_authenticated %}
        <li><a href="#">{{user.username}}</a></li>

        <li>
          <a href="{% url 'account:password_change' %}">chnage password</a>
        </li>

        <form
          id="logout"
          action="{% url 'account:user_logout' %}"
          method="post"
        >
          {% csrf_token %}
          <li>
            <a
              href=""
              onclick="document.getElementById('logout').submit();return false;"
              >Logout</a
            >
          </li>
        </form>

        {% else %}
        <li><a href="{% url 'account:user_login' %}">LOGIN</a></li>
        {% endif %}
      </ul>
    </div>
  </nav>
</div>
```

reset password

for security reason, password stored in the database are encrypte3d, so it is usually not possible for user to retrive their password,
but to reset it.

Django also provide a built-in method to reset password

the standard procedure of reseting passsword would be the following

request to reset password
enter your email address(password-reset)
send email and prompt user (password-reset-done)
click the link in the eemail(password-reset-confirm)
reset password (password-reset-complete)
done

`urls.py`

```python


from account import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse

urlpatterns = [
    # path("login/", views.user_login, name="user_login"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login2.html"),
        name="user_login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="account/logout.html"),
        name="user_logout",
    ),
    path("register/", views.register, name="user_register"),
    path(
        "password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="account/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="account/password_change_form.html",
            # success_url=reverse("account:password_change_done"),
            success_url="/account/password-change-done/",
        ),
        name="password_change",
    ),
    path(
        "password-reset",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset_form.html",
            email_template_name="account/password_reset_email.html",
            success_url="/account/password-reset-done/",
        ),
        name="passwrod_reset",
    ),
]
```

`password_reset_form.html`

```html
{% extends "base.html" %}
<br />
{% block title %}password reset{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Forgotten your password? Reset, please.</h1>
  <p>Enter your email to set a new password.</p>
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <div class="form-group">
      <label class="col-md-5 control-label text-right">Email</label>
      <div class="col-md-6 text-left">{{ form.email }}</div>
    </div>
    <input type="submit" value="Send email" class="btn btn-primary btn-lg" />
  </form>
</div>
{% endblock %}
```

`passwrod_reset_email.html`

```html
<p>
  You're receiving this email because you requested a password reset for your
  user account at <a href="#">your site</a>
</p>
<p>Please go to the following page and choose a new password:</p>
{{ protocol }}://{{ domain }}{% url 'account:password_reset_confirm' uidb64=uid
token=token %}
<p>Your username, in case you've forgotten:{{ user.get_username }}</p>
<p>Thanks for using our site!</p>
<p>The itdiffer.com team</p>
```

`password_reset_done.html`

```html
{% extends "base.html" %}
<br />
{% block title %}password reset{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Reset your password</h1>
  <p>
    We've emailed you instructions for setting your password, if an account
    exists with the email you entered. You should receive them shortly.
  </p>
  <p>
    If you don't receive an email, please make sure you've entered the address
    you registered with, and check your spam folder.
  </p>
</div>
{% endblock %}
```

`urls.py`

```python


    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
            success_url="/account/password-reset-complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
```

`passwrod_reset_confirm.html`

```html
{% extends "base.html" %}
<br />
{% block title %}password reset{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Reset Password</h1>
  <p>
    Please enter your new password twice so we can verify you typed it in
    correctly.
  </p>
  <form class="form-horizontal" method="post">
    {% csrf_token %}
    <div class="form-group">
      <label class="col-md-5 control-label text-right">New password</label>
      <div class="col-md-6 text-left">{{ form.new_password1 }}</div>
    </div>
    <div class="form-group">
      <label class="col-md-5 control-label text-right">Confirm password</label>
      <div class="col-md-6 text-left">{{ form.new_password2 }}</div>
    </div>
    <input
      type="submit"
      value="Change my password"
      class="btn btn-primary btn-lg"
    />
  </form>
</div>
{% endblock %}
```

`urls.py`

```python


    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
```

`password_reset_complete.htmlo`

```html
{% extends "base.html" %}
<br />
{% block title %}password reset{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>Reset your password</h1>
  <p>
    Your password has been set. You may go ahead and
    <a href="{% url 'account:user_login' %}">log in now</a>.
  </p>
</div>
{% endblock %}
```

configuration Django to send email

email backend
`settings.py`

```python

```

maintaining personal information

data model
form
view personal information
edit personal information
upload and corp profile icon

```python


# data model
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    school = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"user {self.user.username}"

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("shcool",)

# username is not in the form, abecasue once the field is binded to the form, it can not cachange easily

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ('email', )
```

display personal information

the function view shold be able to handle two types of request, POST and GET

in the database, the following table are interrelated to personal infor

- account_userinfo
- account_userprofile
- auth_user

```python




@login_required()
def personal_info(request):
    user_profile = (
        UserProfile.objects.get(user=request.user)
        if hasattr(request.user, "user_pro9file")
        else UserProfile.objects.create(user=request.user)
    )
    user_info = (
        UserInfo.objects.get(user=request.user)
        if hasattr(request.user, "user_info")
        else UserInfo.objects.create(user=request.user)
    )
    return render(
        request,
        "account/personal_info.html",
        {"user": request.user, "user_info": user_info, "user_profile": user_profile},
    )
```

`psersonal_info.html`

```html


{% extends "base.html" %}
<br />
{% block title %}my information{% endblock %}
<br />
{% block content %}
<div class="row text-center vertical-middle-sm">
  <h1>My Information</h1>
  <div class="row">
    <div class="col-md-6">
      <div class="row">
        <div class="col-md-4 text-right"><span>username:</span></div>
        <div class="col-md-8 text-left">{{user.username}}</div>
      </div>

      <div class="row">
        <div class="col-md-4 text-right"><span>emali:</span></div>
        <div class="col-md-8 text-left">{{user.email}}</div>
      </div>

      <div class="row">
        <div class="col-md-4 text-right"><span>school:</span></div>
        <div class="col-md-8 text-left">{{user_info.school}}</div>
      </div>
    </div>
  </div>
</div{% endblock %}
```

`urls.py`

```python

    path("info", views.personal_info, name="personal_info"),,
```

edit personal infor

`personal_info.html`

```html
<a href="{% url 'account:edit_info' %}">
  <button class="btn btn-primary btn-lg">edit my information</button>
</a>
```

`edit_info.html`

upload and edit profile picture

`personal_info.html`

```html
<div class="col-md-6">
  {% load static%}
  <div style="margin-right:100px">
    {% if userinfo.photo %}
    <img
      src="{{ userinfo.photo | striptags }}"
      class="img-circle"
      id="my_photo"
      name="user_face"
    />
    {% else %}
    <img
      name="user_face"
      src="{% static 'images/newton.jpg' %}"
      class="img-circle"
      id="my_photo"
    />
    {% endif %}
  </div>
  <div style="margin-right:100px">
    <button
      class="btn btn-primary btn-lg"
      id="upload_image"
      onclick="upload_image_layer()"
    >
      upload my photo
    </button>
  </div>
</div>
```

cropbox.js
cropbox-min.js
imagecrop.css

```python

def user_image(request):
    return render(request, "account/imagecrop.html")
```

`settings.py`
enabling the imagecrop frame
https://docs.djangoproject.com/en/5.0/ref/clickjacking/

```python

if DEBUG:
    MIDDLEWARE += [
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    X_FRAME_OPTIONS = 'SAMEORIGIN'
```

edit data model

```python


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    school = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(bland=True)

    def __str__(self):
        return f"user {self.user.username}"
```

```python


@login_required()
def user_image(request):
    if request.method == "POST":
        img = request.POST["img"]
        user_info = UserInfo.objects.get(user=request.user.id)
        user_info.photo = img
        user_info.save()
        return HttpResponse("1")
    else:
        return render(request, "account/imagecrop.html")
```

manage personal information in the admin page

# summary

more details about templates

the concepts of template context

# refs

[managing static files](https://docs.djangoproject.com/en/5.1/howto/static-files/)

[The Django template language](https://docs.djangoproject.com/en/dev/ref/templates/language/)

[Built-in template tags and filters](https://docs.djangoproject.com/en/dev/ref/templates/builtins/)

[Using the Django authenticattion system](https://docs.djangoproject.com/en/5.1/topics/auth/default/)

[LOGIN_REDIRECT_URL](https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-LOGIN_REDIRECT_UR)

[request and response objects](https://docs.djangoproject.com/en/5.1/ref/request-response/)

[AJAX with Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html)

[password-reset](https://django-password-reset.readthedocs.io/en/latest/)

[password management in Django](https://docs.djangoproject.com/en/dev/topics/auth/passwords/)

[A django application that provide a login form with a remember me checkbokx ](https://github.com/jimfmunro/django-remember_me)

[one to one relationship](https://docs.djangoproject.com/en/5.1/topics/db/examples/one_to_one/)

[django ajax](https://github.com/yceruto/django-ajax)

[how to integrate ajax with django applications](http://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications)
