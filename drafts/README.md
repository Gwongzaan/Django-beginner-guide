# Introduction

This repository contains a series of django projects for begginer, each with its own purpose.

Each project comes with documents explained the proejct with as much detail as possible.

Test Driven Development Version

list of projects

- simple single user blog system
- multi-user blog system
- extended multi-user blog system
- online learning platform
- online shipping platform

## pre-requisites

# How to use this begginer tutorial

It is recommended to practice the tutorial at least two times. I am using the word **practice** not **read**, by which I mean implement the project while reading the content.

In the first reading, follow the instruction and implement the project, this reading is to have a hard basic understanding of how Django work, because you will type everyting on your own, and see the effect. It is optional to read **Web Development In General** and **Project Development In General**

In the second reading, try to recap and summarize in your language, it is recommended to do it with the tutorial closed. This give you the opporutnity to internalized the most important knowldge and help you to grow fast ine future, becuase you have built your own knowldge base in your head.

In the meantime, try to have your own version of the project implementation.

start all over and implement the project on your own, try your best not to ref to the original, your own implementation doesn't have to be the same as the original one, tyr your best to go beyond the orignal design
read all the reference documents

form a habbit to read official documents.

# Structure of this begginer tutorial

## Web development in General

### Definition of website

### componenets of website

### classification of website

- information provider,
  such as news website,
  (providing structured information or multi media information, ways and flows of publishing information, amount of information, user management, features are 'simple')
  image for business, image for bands, image for product
- business transactions,
  such as amazaon, ebay,
  centered by orders, display products, generate orders, and execute orders,
  product management, order management, purchase order management, payment management, shipping management, member management,
  customer relationship management, enterprise resource planing, management information system,
  B2C, B2B, C2C

- office backend
  multi-data source api
  user management,
  flexibility for sub-site configuration.

- online gaming

### how website works

- client
- server
- IP
- DNS
- TCP/IP
- HTTP
-

### development flow of a website

- requirement analysis
  type of website, features required, business logic, UI, VPS, DNS, etc.
- static content,
- design
- implementation ( front-end and backend) (HTML, CSS, JavaScript, jQuery, Boostrap, Vue, React, AngularJS) (database, business logic)
- testing and deployment
- maintenance and marketing

### Project Development In General

#### task management ( UI, front-end, backend, testing, deployment, maintenance)

## Short Introduction of Django Web Framework

### short histroy of Django Web Framework

### MTV of Django

#### Model

Data Layer: Data representation, Data Relationship and Data operations

Object Relational Mapping(ORM)

ORM access API

#### Template

Rendering and displaying Data

#### View

Business logic, bridge Model and Template

URL design

### some outher built-in componenets

Form handling

template system

cache system

authetication system

internationalization

backend admin

WSGI server

### WSGI

Web Server Gateway Interface (WSGI) is a general interface protocol between web server and web app/ web Framework

relationship between WSGI, web Framework, and web server

a complete website is made of web server, web application, database,

when a user access a URL, a client send an HTTP request to web server,
then web server transfer the request to Web application using WSGI,
web application handle the horizontal request and return a response to web server via WSGI,
then web server return the response to client, client render and display the response to user

WSGI is divided into two part,
server-end, (uWSGI or Gunicorn), implement the communication between web application and web server( Apache/Nginx)
client-end, (Django or Flask framework)

#### 2-level architecture

usually used in development mode

client
WSGI server (uWSGI, wsgiref), also work as web server
WSGI application (flask, django)

#### 3-level architecture

usually used in production mode

client
proxy agent (Nginx)
WSGI server (uWSGI), used as middleware, bridge web server and application
WSGI application (flask, django)

# Brief Overview of each Project

# Simple Single User Blog System

This is the first project the Django Tutorial Series.

this proejct is for introducing the development process of django development with a simple single user blog application.

It also introduce the development cycle of TDD

after this procject, reader should be able to continue to the second project and learn more about Djang and TDD

This project is to introduce django unit testing,

# Multi-user Blog System

This is the second project of the series

# Extended Multi-user Blog System

# online learning platform

# online shopping platform

# reference

it is mainly reference the official documents. It is the most completed, but not the most well organized for beginner.
the way this begginer guide works is first provide a complete, simple but complex enough project for begginer to grasp How django work,
and reorganize the official documents in a way that bridge begginer to intermediate.

understand inside-out a complete, simple but complex enough project, will definitely boost your ability to understand a more complex system, or even build your own complex system

# TODO

- [ ] Full stack development with beginner front-end
- [ ] TDD for each project
