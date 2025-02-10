from django.db import models
from django.contrib.auth.models import User
# Create your models here.a

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth =models.DateField(null=True, blank=True)
    phone =models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"user {self.user.username}"


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school =models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    profession = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    aboutme = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
        return f'user: {self.user.username}'
