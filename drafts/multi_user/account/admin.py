from django.contrib import admin

from .models import UserInfo, UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth",
        "phone",
    )

    list_filter = ("phone",)


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(UserInfo)
