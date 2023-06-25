from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Links

admin.site.register(Links)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','email','sex', 'birth_date', 'is_online')

admin.site.register(User, UserProfileAdmin)
