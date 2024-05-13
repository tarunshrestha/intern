from django.db import models
from .enums import *
from django_enumfield import enum 

from datetime import datetime, timedelta
from django.utils import timezone 
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class CustomUser(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    
    gender = enum.EnumField(Gender_choice, default=Gender_choice.Others)
    email = models.EmailField("Enter email address", default="")
    phone = models.CharField(unique = True, max_length=12)
    date_of_birth = models.DateField(default = None, null=True)
    profile_picture = models.ImageField(null=True, upload_to='static/', blank=True)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.username 

    @property
    def get_age(self):
        today_date = timezone.now().date()
        age = relativedelta(today_date, self.date_of_birth).years
        return age


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class PersonalInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_media')
    linkedin = models.URLField()
    github = models.URLField()
    descibe = models.TextField()
    
class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='educations')
    title =  enum.EnumField(Education_choice)
    faculty = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    score =models.FloatField()

    def __str__(self):
        return self.title


class Job(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='jobs')
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    
    def __str__(self):
        return self.name 

class Project(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='project')
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name 

class Reference(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reference')
    reference_text = models.CharField(max_length=255)

    def __str__(self):
        return self.reference_text 
    

