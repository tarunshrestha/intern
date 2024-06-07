from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from datetime import datetime, timedelta
from django.utils import timezone 


# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(unique=True, max_length=20)
    date_of_birth = models.DateField(default=None, null=True)
    profile_picture = models.ImageField(null=True, upload_to='static/img/', blank=True)
    gender = models.CharField(max_length=8, choices=(
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ),default='Others')
    
    email = models.EmailField(unique=True) 
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)


    def __str__(self):
       return self.username
    


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

class BaseModel(models.Model):
    url_id = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todo')
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def title_and_des(self):
        return f'{self.title}: {self.description}'
