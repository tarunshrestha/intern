from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="")
    last_name = forms.CharField(max_length=50, label="")
    email = forms.EmailField(max_length=254, label="")
    gender = forms.ChoiceField(choices=[('Male',"Male"),('Female', "Female"), ('Others','Others')])

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','address','gender','phone','date_of_birth','email', 'skills', 'languages','profile_picture']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)

        fields =['username','phone','password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
