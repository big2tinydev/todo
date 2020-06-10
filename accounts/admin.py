from django.contrib import admin

from accounts.models import Account
from accounts.models import UserProfile

admin.site.site_header = 'Dashboard'
admin.site.site_title = 'Dashboard'


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    exclude = ['slug']


admin.site.register(Account, AccountAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']
    list_filter = ['user', 'location']
    exclude = ['slug']


admin.site.register(UserProfile, UserProfileAdmin)
