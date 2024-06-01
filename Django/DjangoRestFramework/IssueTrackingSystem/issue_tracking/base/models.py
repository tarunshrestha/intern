from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Groups(Group):
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

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
    company = models.ManyToManyField(Company, default="", blank=True)
    groups = models.ManyToManyField(Group, default="", blank=True)
    email = models.EmailField(unique=True) 
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)


    def __str__(self):
       return self.username



class Ticket(models.Model):
    created_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='token')
    recent_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='token_editor', default=None)
    solved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='token_solver', default=None)
    company = models.ManyToManyField(Company)
    title = models.CharField(max_length=150, unique=True)
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Forwarded', 'Forwarded'),
        ('Resolved', 'Resolved')
            ),default='Pending')
    severity = models.CharField(max_length=20, choices=(
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
            ),default='Low')
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)
    assigned_to = models.ManyToManyField(Group, default="", blank=True)
    company = models.ManyToManyField(Company, default="", blank=True)

    
    def __str__(self):
        return self.title 

