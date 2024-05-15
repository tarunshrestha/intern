from django.db import models
from .enums import *
from django_enumfield import enum 

from datetime import datetime, timedelta
from django.utils import timezone 
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

# class UserManager(BaseUserManager):
#     def create_user(self, username, person, password=None):
#         if not username:
#             raise ValueError('User must have a valid username')

#         user = self.model(username=username, created=datetime.now(), must_change_password=True, deleted=False, person=person)

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

class CustomUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    # password = models.CharField(max_length=50, null=True)
    gender = enum.EnumField(Gender_choice, default=Gender_choice.Others)
    email = models.EmailField(unique=True) 
    phone = models.CharField(unique=True, max_length=20)
    date_of_birth = models.DateField(default=None, null=True)
    profile_picture = models.ImageField(null=True, upload_to='static/', blank=True)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username


    @property
    def get_age(self):
        today_date = timezone.now().date()
        age = relativedelta(today_date, self.date_of_birth).years
        return age
    
    @property 
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}" #from django.db.models.functions import Concat


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class PersonalInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_media')
    linkedin = models.URLField(null=True)
    github = models.URLField(null=True)
    summary = models.TextField(null=True)
    
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
    

