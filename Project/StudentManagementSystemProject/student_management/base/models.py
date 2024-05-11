from django.db import models
from django_enumfield import enum
from datetime import date


class TypeEnum(enum.Enum):
    Teacher = 1
    Student = 2

    __labels__ = {
        Teacher : 'Teacher',
        Student : 'Student'
    }

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class BaseModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(default=None)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    class Meta:
        abstract = True


class Teacher(BaseModel):
    id_type = enum.EnumField(TypeEnum,default = TypeEnum.Teacher)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(BaseModel):
    id_type = enum.EnumField(TypeEnum,default = TypeEnum.Student)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faculty = models.ManyToManyField(Faculty)
    teacher = models.BooleanField(default=True)
    student = models.BooleanField(default=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    








