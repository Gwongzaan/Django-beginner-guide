# Introduction

for beginner, the most difficult part is "HOW",

if beginner can see the process, and follow the steps from beginning to the end,
it will boost their learning process, and form their own thinking to tackle problems

this series of tutorial comes up with this mindset,

the

I have been tutoring many students,
I have started up a company, and try to hire
but hard to find qualify people, especially new graduate,
few of them are on the right track.

Beginner Series
begin with Django basic,
advance to TDD
Django Source code

# reference

https://tutorial.djangogirls.org/en/
https://git-scm.com/

# a series of Django Tutorial

- Beginner: backend
- Intermediate : Test Driven
- Advance: Project oriented.
- Advance: the framework itself.

every series with a Reference Chapter, samething

# overview of the book

Project codes of the book can be found in the books git repository
[](https://github.com)

it is not only about how to use Django,

it also talks about logging, exceptions.

I have been looking for a one stop place that I can learn python, project-oriented, deployment, reading source code

therefore I created one,

If you find it valuable, donate and spread the words.

Testing

# Pre-requisite

this book/tutorial assume knowledge of Python.

# How to read the book

Part I is to demonstrate the core features of Django. It is organized to be read linearly

# develop process

define url configuration,
define model
define template
define view

# Starting a New Project Correctly

- URL Scheme
- resources for selecting third-party apps to Django Projects
- Outline a plan

## Preparing a Project

Before writing a single line of code,

- outline your project;
- define behavior,
- data structures,
- URL scheme,
- choose third-party apps to lessen the amount of work needed to do.

### Project Specification

view is the heart of Django, and the purpose of view is to handle HTTP.

the first goal when building a website is always ask:

- What does it do? (what behavior should be defined)
- Then, What data are needed?
- With data in mind, design models.
- when building a model, decide how the data is accessed. the key question is always: Does this model need a slug?
- to fully answer the question of data access, we should always design our URL scheme. The URL scheme forces us to consider the data as well as the behavior. Crucially, we want our URLs to be consistent and to last for as long as possible.
-

### Picking Third-Party Apps

Once you understand what your sites does(what behavior and data structure you need), your next step is to see if someone has already done the work for you.
[awesome-django](http://awesome-django.com)
[django packages](https://djangopackages.org/)

### Testing

https://www.obeythetestinggoat.com/pages/book.html
Test-Driven Development (TDD)
Behavior-Driven Development (BDD)

### Starting with Generic Views

https://ccbv.co.uk/

When building a view, use Django's documentation and https://ccbv.co.uk/ and ask yourself: Does a GCBV already provide the majority of the behavior I want?

in the event the answer is no, then your are left with the choice of building a view with a class-based view (CBV) or else a function view(FV),

# URL reverse Methods

# Optimization

# building REST APIs
