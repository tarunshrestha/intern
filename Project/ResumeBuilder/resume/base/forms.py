from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="")
    first_name = forms.CharField(max_length=50, label="")
    last_name = forms.CharField(max_length=50, label="")
    email = forms.EmailField(max_length=254, label="")
    gender = forms.ChoiceField(choices=[('Male',"Male"),('Female', "Female"), ('Others','Others')])
    # password = forms.CharField(max_length=50)
    # password2 = forms.CharField(max_length=50)

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'address', 'gender', 
            'phone', 'date_of_birth', 'email', 'skills', 'languages', 
            'profile_picture'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['skills'].widget = forms.CheckboxSelectMultiple()
        self.fields['languages'].widget = forms.CheckboxSelectMultiple()
        self.fields['skills'].queryset = Skill.objects.all()
        self.fields['languages'].queryset = Language.objects.all()

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.save()
        self.save_m2m()  # This ensures the many-to-many fields are saved
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class RegisterForm(forms.Form):
        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)
        username = forms.CharField(max_length=50)
        password = forms.CharField(max_length=50)
        password2 = forms.CharField(max_length=50)
        # date_of_birth = forms.DateTimeField()  Test@123
        address = forms.CharField(max_length=100)
        phone = forms.CharField(max_length=15)


        



class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['linkedin','github','summary']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        ### not displaying the user field in each form
        widgets = {
            'user': forms.HiddenInput(),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
        }


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
        }
