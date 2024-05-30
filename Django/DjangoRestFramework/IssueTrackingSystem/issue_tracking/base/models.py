from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
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

class Company(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='token')
    company = models.ManyToManyField(Company)
    title = models.CharField(max_length=150, unique=True)
    status_code = models.IntegerField()
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Forwarded', 'Forwarded'),
        ('Resolved', 'Resolved')
            ),default='Pending')
    description = models.TextField()
    allocation = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title 

