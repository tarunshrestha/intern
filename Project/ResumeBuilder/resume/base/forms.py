from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="")
    last_name = forms.CharField(max_length=50, label="")
    email = forms.EmailField(max_length=254, label="")
    gender = forms.ChoiceField(choices=[('Male',"Male"),('Female', "Female"), ('Others','Others')])
