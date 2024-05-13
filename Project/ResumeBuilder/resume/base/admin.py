from django.contrib import admin
from .models import *

admin.site.register([CustomUser, Skill, Language, PersonalInformation, Education, Job, Project, Reference])