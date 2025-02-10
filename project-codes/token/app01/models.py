from django.db import models

# Create your models here.a
class Administrator(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)