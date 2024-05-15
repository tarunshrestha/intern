from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register([CustomUser, Skill, Language, PersonalInformation, Education, Job, Project, Reference])