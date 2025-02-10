# managing and displayibng posts

every website should have content,

classified by how content are generated

- user generated content, such as YouTube, X,
- profession generate content, such as some personal blog site

in this project, we are developing a website which is user-gerenated-content

this kind of website has two part, where the front end is for visitors, the backend is of user managing their content

- manageing columns

# managing volumes

- create article app
- setup volume ( data model, form, function view, )
- edit volume
- delte volume

data model

```python

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ArticleColumn(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_column"
    )
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column
```

column form

```python

from django import forms

from .models import ArticleColumn


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)
```

function view

```python

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import ArticleColumn


@login_required()
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)
    return render(request, "articvl/column/article_column.html", {"column": columns})
```

url configuration

```python

    path("article/", include("article.urls", namespace="article")),

from django.urls import path

from . import views


app_name = "article"
urlpatterns = [
    path("article-column/", views.article_column, name="article_column"),
]
```

template

`articvle/template/article/header.html`

```html


{% load static%}
<div class="container">
    <nav class="navbar navbar-default" role="navigation">
        <div class="navbar-header">
            <a class="navbar-brand" href="">
                <img width="100px" src="{% static 'images/logo.png' %}">
            </a>
        </div>
        <div>
            <ul class="nav navbar-nav" role="tablist">
                <li><a href="{% url 'article:article_column' %}">manage articles</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right" style="margin-right:10px">
                <li><a href="{% url 'blog:blog_title' %}">landing page</a></li>
                <li><span>{{ user.username }}</li>
                <li><a href="{% url 'account:user_logout' %}">Logout</a></li>
            </ul>
        </div>
    </nav>
</div>
```

update `templates/header.html` with the following code

```html

```

`leftslider.html`

```html
<div class="text-center" style="margin-top: 5px">
  <p><a href="{% url 'article:article_column'%}">managing column</a></p>
</div>
```

`article/base.html`

```html
{% load static%}
<! DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" />
  </head>
  <body>
    <div class="container">
      {% include 'article/header.html' %}
      <div class="col-md-2">{% include 'article/leftslider.html' %}</div>
      <div class="col-md-10">{% block content %} {% endblock %}</div>
      {% include 'footer.html' %}
    </div>
  </body>
</html>
```

`article_column.html`

```html
{% extends "article/base.html" %}
<br />
{% load staticfiles %}
<br />
{% block title %}article column{% endblock %}
<br />
{% block content %}
<div>
  <p class="text-right"><button class="btn btn-primary">add column</button></p>
  <table class="table table-hover">
    <tr>
      <td>ID</td>
      <td>column</td>
      <td>operation</td>
    </tr>
    {% for column in columns %}
    <tr>
      <td>{{ forloop.counter }}</td>
      <td>{{ column.column }}</td>
      <td>--</td>
    </tr>
    {% empty %}
    <p>no column sets。</p>
    {% endfor %}
  </table>
</div>
{% endblock %}
```

add column
edit `articl_column.html`

```html
<p class="text-right">
  <button id="add_column" onclick="add_column()" class="btn btn-primary">
    add column
  </button>
</p>
```

`views.py`

```python


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ArticleColumnForm
from .models import ArticleColumn


@login_required()
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(
            request,
            "article/column/article_column.html",
            {"columns": columns, "column_form": column_form},
        )
    if request.method == "POST":
        column_name = request.POST["column"]
        columns = ArticleColumn.objects.filter(
            user_id=request.user.id, column=column_name
        )
        if columns:
            return HttpResponse("2")
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")
```

`articl_column.html`

```html
{% extends "article/base.html" %}
<br />
{% load static%}
<br />
{% block title %}article column{% endblock %}
<br />
{% block content %}
<script type="text/javascript" src='{% static "js/jquery.js" %}'></script>
<script type="text/javascript" src="{% static 'js/layer.js'%}"></script>
<script type="text/javascript">
  function add_column() {
    var index = layer.open({
      type: 1,
      skin: "layui-layer-rim",
      area: ["400px", "200px"],
      title: "add column",
      content: `<div class="text-center" style="margin-top:20px">
                            <p>column name</p>
<p>{{column_form.column}}</p>
                          </div>`,
      btn: ["confirm", "cancel"],
      yes: function (index, layero) {
        column_name = $("#id_column").val();
        $.ajax({
          url: "{% url 'article:article_column' %}",
          type: "POST",
          data: { column: column_name },
          success: function (e) {
            if (e == "1") {
              parent.location.reload();
              layer.msg("ok");
            } else {
              layer.msg("column exisits");
            }
          },
        });
      },
      btn2: function (index, layero) {
        layer.close(index);
      },
    });
  }
</script>

<div>
  <p class="text-right">
    <button id="add_column" onclick="add_column()" class="btn btn-primary">
      add column
    </button>
  </p>
  <table class="table table-hover">
    <tr>
      <td>ID</td>
      <td>column</td>
      <td>operation</td>
    </tr>
    {% for column in columns %}
    <tr>
      <td>{{ forloop.counter }}</td>
      <td>{{ column.column }}</td>
      <td>--</td>
    </tr>
    {% empty %}
    <p>no column sets。</p>
    {% endfor %}
  </table>
</div>

{% endblock %}
```

editing column

publish and display posts

## slug

in general, we can locate a post by its id, or we can locate it by its title, but a title usually contains whtespace,
which will be represedted as %20% in th URL, this is not a friendly URL, therefore, we use `-` as a connector

`slug`

```python
from django.utils.text import slugify
slugify("learn python in 30 days")
# Learn-python-in-30-days

```

the buitl in slugify method is limited,

```shell
pip install awesome-slugify
```

you can test it with django in interactive mode

## data model

```python


@login_required()
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(
                    id=request.POST["column_id"]
                )
                new_article.save()
                return HttpResponse("1")

            except:
                return HttpResponse("2")

        else:
            article_post_form = ArticlePostForm()
            article_columns = request.user.article_column.all()
            return render(
                request,
                "article/column/article_post.html",
                {
                    "article_post_form": article_post_form,
                    "article_column": article_columns,
                },
            )
```

`url.py`

```python

    path("article-posst/", views.article_post, name="article_post"),
```

```html
{% extends "article/base.html" %}
<br />
{% load staticfiles %}
<br />
{% block title %}article column{% endblock %}
<br />
{% block content %}
<div style="margin-left: 10px">
  <form class="form-horizontal" action="." method="post">
    {% csrf_token %}
    <div class="row" style="margin-top: 10px">
      <div class="col-md-2 text-right"><span>title：</span></div>
      <div class="col-md-10 text-left">{{article_post_form.title}}</div>
    </div>
    <div class="row" style="margin-top: 10px">
      <div class="col-md-2 text-right"><span>column：</span></div>
      <div class="col-md-10 text-left">
        <select id="which_column">
          {% for column in article_columns %}
          <option value="{{column.id}}">{{column.column}}</option>
          {% endfor %}
        </select>
      </div>
    </div>
    <div class="row" style="margin-top: 10px">
      <div class="col-md-2 text-right"><span>内容：</span></div>
      <div class="col-md-10 text-left">{{article_post_form.body}}</div>
    </div>
    <div class="row">
      <input
        type="button"
        class="btn btn-primary btn-lg"
        value="发布"
        onclick="publish_article()"
      />
    </div>
  </form>
</div>
<script type="text/javascript" src='{% static "js/jquery.js" %}'></script>
<script type="text/javascript" src="{% static 'js/layer.js'%}"></script>
<script type="text/javascript">
  function publish_article() {
    var title = $("#id_title").val();
    var column_id = $("#which_column").val();
    var body = $("#id_body").val();
    $.ajax({
      url: "{% url 'article:article_post' %}",
      type: "POST",
      data: { title: title, body: body, column_id: column_id },
      success: function (e) {
        if (e == "1") {
          layer.msg("successful");
        } else if (e == "2") {
          layer.msg("sorry.");
        } else {
          layer.msg("it could not be empty。");
        }
      },
    });
  }
</script>
{% endblock %}
```

using Markdown

git clone plugin from github to stat

ihttps://github.com/qiwsir/editor.md

listing article title

display article

display format

```html
{% extends "article/base.html" %} {% block title %}articles list{% endblock %}
{% block content %}
<div>
  <h1>{{ article.title }}</h1>
  <p>{{ user.username }}</p>
  <div>{{ article.body }}</div>
</div>
{% endblock %}
```

```html

{% extends "article/base.html" %}
<br>
{% load static %}
<br>
{% block title %}articles list{% endblock %}
<br>
{% block content %}
<div>
    <header>
        <h1>{{ article.title }}</h1>
        <p>{{ user.username }}</p>
    </header>

    <link rel="stylesheet" href="{% static 'editor/css/editormd.preview.css' %}" />
    <div id='editormd-view'>
        <textarea id="append-test" style="display:none;">
{{ article.body }}
        </textarea>
    </div>
</div>
<script src='{% static "js/jquery.js" %}'></script>
<script src='{% static "editor/lib/marked.min.js" %}'></script>
<script src='{% static "editor/lib/prettify.min.js" %}'></script>
<script src='{% static "editor/lib/raphael.min.js" %}'></script>
<script src='{% static "editor/lib/underscore.min.js" %}'></script>
<script src='{% static "editor/lib/sequence-diagram.min.js" %}'></script>
<script src='{% static "editor/lib/flowchart.min.js" %}''></script>
<script src='{% static "editor/lib/jquery.flowchart.min.js" %}'></script>
<script src='{% static "editor/editormd.js" %}'></script>
<script type="text/javascript">
$(function(){
    editormd.markdownToHTML("editormd-view", {
        htmlDecode: "style, script, iframe",
        emoji: true,
        taskList:true,
        tex:true,
        flowChart:true,
        sequenceDiagram : true,
    });
});
</script>
{% endblock %}
```

redirection ato article list arfter it is posted

`article_post.html`

```javascript
    <script type="text/javascript">
        function publish_article(){
            success: function(e){
                if(e=="1"){
                    layer.msg("successful");
                    location.href = "{% url 'article:article_list' %}";
                }
    </script>
```

in the function view, article is saved at the backend, and frontend use javascript to catche feedback and determine

deleting articles and editing articles

`edit_article.html`

```html
{% extends "article/base.html" %}
<br />
{% load static %}
<br />
{% block title %}article column{% endblock %}
<br />
{% block content %}
<link rel="stylesheet" href="{% static 'editor/css/style.css' %}" />
<link rel="stylesheet" href="{% static 'editor/css/editormd.css' %}" />
<div class="container">
  <div class="col-md-10">
    <div style="margin-left: 10px">
      <form class="form-horizontal" action="." method="post">
        {% csrf_token %}
        <div class="row" style="margin-top: 10px">
          <div class="col-md-2 text-right"><span>title</span></div>
          <div class="col-md-10 text-left">{{this_article_form.title}}</div>
        </div>
        <div class="row" style="margin-top: 10px">
          <div class="col-md-2 text-right"><span>column</span></div>
          <div class="col-md-10 text-left">
            <select id="which_column">
              {% for column in article_columns %} {% if column ==
              this_article_column.column %} #②
              <option value="{{column.id}}" selected="selected">
                {{column.column}}
              </option>
              #③ {% else %}
              <option value="{{column.id}}">{{column.column}}</option>
              {% endif %} {% endfor %}
            </select>
          </div>
        </div>
        <div class="row" style="margin-top: 10px">
          <div class="col-md-2 text-right"><span>content</span></div>
          <div id="editormd" class="col-md-10 text-left">
            <! --{{article_post_form.body}}-->
            <textarea style="display: none" id="id_body">
    {{article.body}}   
                  </textarea
            >
          </div>
        </div>
        <div class="row">
          <input
            type="button"
            class="btn btn-primary btn-lg"
            value="发布"
            onclick="redit_article()"
          />
        </div>
      </form>
    </div>
  </div>
</div>
<script type="text/javascript" src='{% static "js/jquery.js" %}'></script>
<script
  type="text/javascript"
  src='{% static "editor/editormd.min.js" %}'
></script>
<script type="text/javascript" src="{% static 'js/layer.js'%}"></script>
<script type="text/javascript">
  $(function () {
    var editor = editormd("editormd", {
      width: "100%",
      height: 640,
      //syncScrolling : "single",
      path: "{% static 'editor/lib/' %}",
    });
  });
</script>
{% endblock %}
```

pagination

```python

```

optimize list of title

- function views do not has to be defined in the `views.py`

`list_views.py`

``

# summary

# reference

[Templats](https://docs.djangoproject.com/en/5.1/topics/templates/)
[QuerySet API reference](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)
[django-queryset-csv](https://pypi.python.org/pypi/django-queryset-csv)
[url resolvers](https://docs.djangoproject.com/en/5.1/ref/urlresolvers/)
[path and repath](htpps://docs.djangoproject.com/en/5.1/ref/urls/)
[slug](https://docs.djangoproject.com/en/5.1/_modules/django/db/models/fields/#SlugField)
[many to one relationship](https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/)
[ForeignKey](https://docs.djangoproject.com/en/5.1/ref/models/fields/#foreignke)
[making queries](https://docs.djangoproject.com/en/5.1/topics/db/queries/)
[jquery pagination plugin](https://github.com/esimakin/twbs-pagination)
[django-markdown](https://pypi.python.org/pypi/django-markdown)
[Query Set API reference](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)
[built in template filter and tags](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)
[working with forms](https://docs.djangoproject.com/en/5.1/topics/forms)
[django.urls utility functions](https://docs.djangoproject.com/en/5.1/ref/urlresolvers/)
