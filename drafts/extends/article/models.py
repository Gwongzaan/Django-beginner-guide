from django.contrib.auth.models import User
from django.db import models
from django.db.models import Index
from django.urls import reverse
from django.utils import timezone
from slugify import slugify

# Create your models here.


class ArticleColumn(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_column"
    )
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


class ArticlTag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tag")
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag


class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(
        ArticleColumn, on_delete=models.CASCADE, related_name="article_column"
    )
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name="articles_like", blank=True)

    article_tag = models.ManyToManyField(
        ArticlTag, related_name="article_tag", blank=True
    )

    class Meta:
        ordering = ("title",)
        indexes = [Index(fields=["id", "slug"])]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("article:article_detail", args=[self.id, self.slug])
        return reverse("article:article_content", args=[self.id, self.slug])


class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost, on_delete=models.CASCADE, related_name="comments"
    )

    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"comment by {self.commentator.username} on {self.article}"
