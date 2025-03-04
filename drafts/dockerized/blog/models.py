from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-published_date',]

    def __str__(self):
        return self.title