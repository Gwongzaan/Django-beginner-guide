from django.contrib import admin

from blog import models

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )


admin.site.register(models.Blog, BlogAdmin)
