# Forward 

test it before git commit
# installing virtural box and setting up the docker environment 
if you are new to docker, simply following the instruction, focus on the Django sessions. 

though, it is recommended to learn more about docker, 

# setting up python virtural environment


# install Django with the virtual environment using pip
-	Check Django version ( $ django-admin --version)
```shell
django-admin --version
```

# Brief Summary of Django

don't worry if you don't understand this chapter, 

it supposed to be titled "Instruction", but it is actually a brief summary that you should come back and read it again after you finish the chapter **creating a project and start the first app** 


## core conectps:
Models: handle data access
Templates: what to display and how to display
Views:business logic related to model access and using template, a connect Template and Models 
URL dispatcher

# Forms
URLs config

procedure:
client send request,
	if GET: 
		response with empty form
	if POST:
		if is_valid
			handle form
		else:
			report error





# creating a project and start the first app: 
brief overview of this chapter and instruction of reading this chapter


this chapter will go through the skeleton process of developing a project. 

the steps are not the only standard process, but they give you a good start the the interation of your project development. 

the main body will focus on the process, supplements of each session will give detail explaination to some of the concepts they should know before proceeding to the next chapter, but don't affect following the steps in the chapter



## brief summary/overview of the development process



###  initial and iterative process of building a website using Django
Design
	- Models
	- URLs, Views, Templates, Forms
	
Development
- create a project
- run the project, to see if it is setup correctly. 
- start an app, and register the app
- connect root URLs config and the app URLs config
the following is an iterative process
- building a model, gerenate a migration, and make migrations
- building templete for views
- building views for the app
- configure app URLs 

the order between templates, views and URLs doesn't matter, while all three are required and work closely together. 

# Design


# Development
- creating project
- creating app
- project settings: settings.py, urls.py
- app default files: views.py, models.py, admin.py

## starting project
```shell
django-admin startproject PROJECT-NAME
```
django will create a direcotry having the same name as PROJECT-NAME, with the contents:

![project-structure](images/project-structure.png)


or

```shell
mkdir DEST-DIR
cd DEST-DIR
django-admin startproject PROJECT-NAME DEST-DIR 
```
![project-structure-2](images/project-structure-2.png)
difference between the two methods creating projects


## run the project
usually, if you are developing on your local machine, it is enough to run the folling command
```shell
python manage.py runserver 
```

here we're using virtual box, therefore, we need to do some settings before hand

- add ADDR:PORT to ALLOWED_HOSTS in the file settings.py
- run the following commands
```shell
sudo ufw allow 8000 # setup the firewall
python3 manage.py runserver 0.0.0.0:8000 # specifying 0.0.0.0:8000 , so that it can be access from the host browser

![result-of-cmd](images/run-the-project.png)

```
on the host, open a browser and type ADDR:PORT, should have

![landing-page](images/landing-page.png)

so far we have the default landing page provided by Django

## creating an app and register the app
an app represents a clear function of the project, such as function for payment, for authentication, etc. 

to register the app, add to the INSTALLED_APPS

navigate to where the app will be stored, and run the following command, 
```shell
cd PROJECT-NAME
python3 manage.py startapp NAME-OF-THE-APP 
# or
django-admin startapp NAME-OF-THE-APP
```

django will create a folder named NAME-OF-THE-APP, and create a series of default files

![startapp](images/start-app.png)  
![app-default-files](images/app-default-files.png)

at this point you started a project, and  have an 'empty' app, ready to begin the development of your first app



### supplements
this section explain the project structure created by Django, and the functionality of the default files created

- django-admin and manage.py 
https://docs.djangoproject.com/en/5.0/ref/django-admin/
- cmd django-admin, it is django-admin.py in django/bin
- manage.py, it is a wrapper for django-admin, with its own features, it is created as the project created

review the Django project structure

- management directory (blog-site at the same level of manage.py ), it is usually for project-wide configuration

a Django project has a predefined project structure with some key files created for you

- how to configure the web application via some of those files
- 

Django project contains one or more apps. each app represents a clear function, such as for payment, for authentication, 

creating app and register it inside a django project

there's an inner movie_review folder

explain the purpose of each file

REF: 
G. Lim, D. Correa - Django 4 for the Impatient. Learn the core concepts of Python web development with Django in one weekend (2022) - libgen.li 
page 30/190 

the app folders and files in the folder


#### project configuration
need to register app in settings.py:INSTALLED-APPS before client can access the app

settings.py
https://docs.djangoproject.com/en/5.0/topics/settings/
django.conf import settings:
	- DEBUG
	- ALLOWED_HOSTS
	- INSTALLED_APPS
	- DATABASES
	- LANGUAGE_CODE
	- TIME_ZONE

REF: 
https://docs.djangoproject.com/en/5.0/intro/tutorial01/
https://docs.djangoproject.com/en/5.0/faq/
https://djangosites.org/
# develop your app
Model
view
template
URLs

# Django Models
https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey

creating model for the app  is usually the first step 

each model maps a database table, it contains the fields and behaviors of the data stored. 

we create models, and Django converts models into database tables correspondently

The model provides data from the database.
In Django, the data is delivered as an Object Relational Mapping (ORM),
with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.
The models are usually located in a file called models.py.

model attributes and database fields

## ORM 

https://en.wikipedia.org/wiki/Object-relational_mapping
https://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it

## creating models
to create table(model), go to models.py in the app folder, 
add a table by create a class having the same name as the table, 

each model is class that extends django.db.models.Model
each model attribute represents a database column

## managing migrations
register app before migrations
```shell
python manage.py makemigrations
python manage.py migrate
```



## creating a Views
Django views are python functions or method taht takes http requests and return http response, they are usually put in a file named views.py located in the folder of the app 

A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the result.
The views are usually located in a file called views.py.

![images/empty-views.py.png](empty-view)

create a view for home page and about page, both return simple html heading

typically in views.py


# Django Template and static files
https://docs.djangoproject.com/en/2.1/ref/templates/language/  

https://docs.djangoproject.com/en/2.1/ref/templates/builtins/ 

A template is a file where you describe how the result should be represented.
Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results.
Django uses standard HTML to describe the layout, and uses Django tags to add logic:
The templates of an application is located in a folder named templates.
so far, our Django project have views, and each view is connected with a specific url, but the HTML reponse of each view is hard coded. 

django use *template* to separate the HTML code from Django view code.

in this chapter, we will see how Django Template work, how to connect views to template, 

create a *templates* directory inside the app's folder, and create a HTML file, 


app/templates/app/SOME.html

explain how Django look for templates

settings.py
	TEMPLATES
		DIRS & APP_DIRS

https://learndjango.com/tutorials/template-structure#:~:text=By%20default%2C%20the%20Django%20template,pages%20app%20and%20a%20home.
- APP Level
by default, the Django template loaders will look for a *templates* folder within each app, but to avoid namespace issues, you also need to have a subfolder having the same name as the app within th templates folder

- Project level
setting template path in the settings.py, by doing so, it tells Django not only look for templates in each app, but also in the specified path




![file structure](images/template-file-structure.png)

modify the view 

```
def view(request):
	template = loader.get_template('first-template.html')
	return HttpResponse(template)
```

change settings and register the app so that Django can find the template

when do I supposed to migrate? usually after register the app?

passing data into template

managing static files (css, js)
https://docs.djangoproject.com/en/dev/howto/static-files
common static files
STATICFILES_FINDERS
STATICFILES_DIRS

**contexts** middleman between templates and views

tags: block-tag {% %}, var-tag {{ }}
## managing URLs
URL dispatcher
ihttps://docs.djangoproject.com/en/5.0/topics/http/urls/
Django also provides a way to navigate around the different pages in a website.
When a user requests a URL, Django decides which view it will send it to.
This is done in a file called urls.py.
The basic process
When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:
1.	Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
2.	The view, located in views.py, checks for relevant models.
3.	The models are imported from the models.py file.
4.	The view then sends the data to a specified template in the template folder.
5.	The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

the route and entry point to a page is controlled by the URLs

create a file named urls.py in the same folder as the views.py , this file is specific for the app. 

we need to do some routing in the root directory. 

there's a file named urls.py on the project folder, 

add `include` module, and add a path() to its urlpattern list. 

```python
from django.urls import path
from . import views

urlpatterns = [
	path('view/', views.view_name, name='view-name'), 
]
```

![res](images/specific-urls.png) 

how to 
- customize our own landing page, and have different URLs to route to them

- how Django URLs work, and how to define URLs  and Link them to respective Django views. 

urls.py is referenced each time someone types a URL on the website. 

for example 10.0.0.253:8000/hello, it gives an Page Not found error

each time a user type a URL in the browser, the request is passed to urls.py , and see if the URL matches any defined paths so that the Django server can give a proper response.   


- configure URL-config,
- create corresponding views(function view, class-based view) in the app

Django will reload if any changes made


# Form




# Outline
- Data and Schema Migrations
- Use data migrations to add content to the website
- Use Schema migrations to enhance and fix existing behavior

# Chapter Overview

A migration is simply a script that changes out database. 

It is like version control for the database.

Migrations can change anything about the database, since a database is usually structured data, it is typically talking about modifying the structure, or schema of the database, or else about changing the data in the database, or both.

# 10.1 Data Migrations
it is a migration that changes the data within the database and makes no changes to the schema. 

data migration is not used very often

## 10.1.1 Tag Data
1. create a new migration file. 


# 10.2 Schema Migrations

migrations allow us to generate a database schema from the model we defined, once models are changed, new migrations should be created, 

migrations also gives us a trace of the evolutions of our database schema, it is like a version control system. 
migrate

the migrate command runs the migrations of all the installed apps. 

but before making any migrations for the app, run the migrate command, no migrations will be applied for the app, 

therefore we need to use makemigrations command to generate migrations for the app
```shell
python3 manage.py makemigrations [APP-NAME]

ptyhon manage.py migrate [APP-NAME]
```

# Testing


# Django Request and Response Cycle
https://medium.com/@ksarthak4ever/django-request-response-cycle-2626e9e8606e
https://medium.com/@developerstacks/django-request-response-cycle-7165167f54c5


middleware are the key component, all request and responses are handled by the middleware 
