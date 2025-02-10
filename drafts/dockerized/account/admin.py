from django.contrib import admin

from account.models import userProfile, UserInfo


# Register your models here.
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone', )
    list_filter = ('phone', )

admin.site.register(userProfile, userProfileAdmin)

class userInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'profession', 'address', 'aboutme', 'photo')
    list_filter = ('school', 'company', 'profession')

admin.site.register(UserInfo, userInfoAdmin)