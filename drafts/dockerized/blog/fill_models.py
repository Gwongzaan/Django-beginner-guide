# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

def fill_model_post():
    Post(title='stasdfasdfasdesti',
         published_date=timezone.now(),
         body='j;laksjdfasdlkfjasdlfjaslkdjfasdlkfjasdlkjfasd\nl;sdjaf\n',
         author=User.objects.get(id=1),
         ).save()


    Post(title='stestifasdfasdqwerqwerqwrqwet[',
         published_date=timezone.now(),
         body='jasldkfjaslkdfjasdlk\naslkdjlajerlqwejlkrjdf',
         author=User.objects.get(id=1),
         ).save()

    Post(title='stestiaslk93ltw',
         published_date=timezone.now(),
         body='jasldkfjaslkdfjasdlk\naslkdjlajerlqwejlkrjdf',
         author=User.objects.get(id=1),
         ).save()

    Post(title='stestiasksd39jdktj',
         published_date=timezone.now(),
         body='jasldkfjaslkdfjasdlk\naslkdjlajerlqwejlkrjdf',
         author=User.objects.get(id=1),
         ).save()
    Post(title='stesti,aslkdjwek',
         published_date=timezone.now(),
         body='jasldkfjaslkdfjasdlk\naslkdjlajerlqwejlkrjdf',
         author=User.objects.get(id=1),
         ).save()

    Post(title='stesti,lsdkll,,elkjek',
         published_date=timezone.now(),
         body='jasldkfjaslkdfjasdlk\naslkdjlajerlqwejlkrjdf',
         author=User.objects.get(id=1),
         ).save()
