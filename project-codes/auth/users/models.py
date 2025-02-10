from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    is_developer = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class ApplicationKey(models.Model):
    developer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=10)
    app_key = models.CharField(max_length=32)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app_key
    