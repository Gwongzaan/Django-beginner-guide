from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORY_LEVEL = (
        (1, 'level one category'), 
        (2, 'level two category'),
        (3, 'level three category'),
        (4, 'level four category'),
    )

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    level = models.IntegerField(choices=CATEGORY_LEVEL)
    parent_cat = models.ForeignKey('self', related_name='sub_cat', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Type1(models.Model):
    name = models.CharField(max_length=50, default='')
    add_time = models.DateTimeField(auto_now_add=True)

class Type2(models.Model):
    parent = models.ForeignKey(Type1, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, default='')
    add_time = models.DateTimeField(auto_now_add=True)

class Type3(models.Model):
    parent = models.ForeignKey(Type2, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, default='')
    add_time = models.DateTimeField(auto_now_add=True)

class Type4(models.Model):
    parent = models.ForeignKey(Type3, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, default='')
    add_time = models.DateTimeField(auto_now_add=True)