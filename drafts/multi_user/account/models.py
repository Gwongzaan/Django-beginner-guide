from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"user {self.user.username}"


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    school = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f"user {self.user.username}"
