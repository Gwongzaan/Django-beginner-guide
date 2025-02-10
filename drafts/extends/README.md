'CRUD' are the four basic operations o system,
but more requirements will come after these operations,

# summerizing functions we had built so fart

- Navigation bar
- login and redirect
- register and redirect

# modifying Navigation bar

# modifying redirection after login/sign up

templateView

`simeple/urls.py`
path('home/')

`LOGIN_REDIRECT_URL`

redirection after registration:

# search for articles of a paticular author

`article/list/article_detail.html`

# give thumb up to an article

an article can be read and liked by many other users, that is many-to-many relationship

how many times an article was read and redis

install Redis

wget https://download.redis.io/releases/redis-7.4.1.tar.gz
tar xzvf redis-7.4.1.tar.gz
mv redis-7.4.1 /usr/local
cd /usr/local/redis-7.4.1/
make install
cd src
./redis-server

./redis-cli

use redis in python

```shell

pip install redis
```

`settings.py`

```python

REDIS_HOST
REDIS_PORT
REDIS_DB
```

- dispaly the hottest article

# comment

- model and formo

# statistics

- totla posts of each user
- list of latest posts
- list of posts with most comments

self-defined template tagp

`<app>/templatetags/` the directly name are requred to be restrictly the same, however the file in it is not

- simple_tag
- inclusion_tag
- assignment_tag

`{% load article_tags %}`

- mocst commented artiless

self-defined template filter

- manageing article tags

- display tags in the article

# ref

[settings](https://docs.djangoproject.com/en/5.1/ref/settings/)
[Django Sttings](https://docs.djangoproject.com/en/5.1/topics/settings/)
[Database](https://docs.djangoproject.com/en/5.1/ref/databases/)
[Multiple Database](https://docs.djangoproject.com/en/5.1/topics/db/multi-db/)
[add() for many-to-many relationship](https://docs.djangoproject.com/en/5.1/ref/models/relations/#django.db.models.fields.related.RelatedManager.add)
[many-to-many relationship](https://docs.djangoproject.com/en/5.1/topics/db/examples/many-to-many/)
[django-like](https://github.com/goinnn/django-like)
[cacheing in django with redis](https://realpython.com/blog/python/cacheing-in-django-with-redis/)
[Model Meta options](https://docs.djangoproject.com/en/5.1/ref/models/options/)
[metaclass in Python](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
[simaple_tag](https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/#simple-tags)
[inclusion_tag](https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/#includsion-tags)
[customer template tags and filter](https://docs.djangoproject.com/en/5.1/howto/customer-template-tags/)
[working with forms](https://docs.djangoproject.com/en/5.1/topics/forms)
[value list](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#values-list)
[django-taggit](http://django-taggit.readthedocs.io/en/latest/forms.html)
