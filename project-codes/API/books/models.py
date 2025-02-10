from django.db import models
from users.models import UserProfile

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    rate = models.FloatField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title