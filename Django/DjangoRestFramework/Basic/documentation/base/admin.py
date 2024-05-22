from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ["email", "username",]

admin.site.register([CustomUser, Todo])
# admin.site.register([Todo])

