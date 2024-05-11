from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    id_type = forms.ChoiceField(choices=[('teacher',"Teacher"),('student', "Student")])


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    birth_date = forms.DateTimeField()
    address = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    id_type = forms.ChoiceField(choices=[('teacher',"Teacher"),('student', "Student")])
    # faculty = forms.ChoiceField(choices=(Faculty.name))
