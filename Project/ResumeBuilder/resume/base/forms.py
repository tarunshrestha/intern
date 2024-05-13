from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="")
    first_name = forms.CharField(max_length=50, label="")
    last_name = forms.CharField(max_length=50, label="")
    email = forms.EmailField(max_length=254, label="")
    gender = forms.ChoiceField(choices=[('Male',"Male"),('Female', "Female"), ('Others','Others')])
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','address','gender','phone','date_of_birth','email', 'skills', 'languages','profile_picture']


class RegisterForm(forms.Form):
        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)
        username = forms.CharField(max_length=50)
        password = forms.CharField(max_length=50)
        password2 = forms.CharField(max_length=50)
        date_of_birth = forms.DateTimeField()
        address = forms.CharField(max_length=100)
        phone = forms.CharField(max_length=15)

        


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
