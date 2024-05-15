from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import  User
from .forms import *
from django.contrib import messages
from faker import Faker
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('login')  # Redirect to login page or another appropriate page
        
        else:
            # Print the errors to the console for debugging
            print(form.errors)
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request, 'index.html', context={'user':user})     
            else:
                messages.sucess(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    if not request.user.is_authenticated: 
        return render(request, 'index.html')
    logout(request)
    return redirect('home')


def User_profile(request, user_id):
    users = CustomUser.objects.filter(pk=user_id).first()
    return render(request, 'user_profile.html', context={'users':users})

def Update_profile(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    link_form = PersonalInformationForm()
    education_form = EducationForm() 
    return render(request, 'update_profile.html', context={'user':user, 'link_form':link_form, 'education_form':education_form})

def Create_fake_profile(request):
    faker = Faker()

    for i in range(10):
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = 'fakename' + str(i)
        email = faker.email()
        birth_date = faker.date_of_birth()
        address = faker.address ()
        phone_number = faker.phone_number()
        gender_value = random.randint(1, 3)
        password = faker.password()

        user = User.objects.create(username = username, password=password)
        custom_user = CustomUser.objects.create(
            user_id=user,
            username = username,
            password=password,
            first_name=first_name, 
            last_name=last_name,
            address=address,
            phone=phone_number,
            gender=gender_value,
            email = email,
            date_of_birth=birth_date,
        )
    return HttpResponse("Fake Created")
