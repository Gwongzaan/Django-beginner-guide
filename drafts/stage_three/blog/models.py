from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    published = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
