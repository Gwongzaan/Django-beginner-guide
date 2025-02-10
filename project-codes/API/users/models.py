from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    APIkey = models.CharField(max_length=30)
    balance = models.FloatField()

    def __str__(self):
        return self.username