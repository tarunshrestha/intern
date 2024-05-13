from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.user.is_authenticated:  # if user is logged in user gets thrown to home page.
        return render(request, 'index.html')

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username'].lower()
        birth_date = request.POST['birth_date']
        address = request.POST['address'] 
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password !=password2:
            messages.error(request, "Password doesnot match.")
            return redirect('register')
            
        try: 
            user = User.objects.get(username= username)
            messages.error(request,"User already Exists.")
            return redirect('register')
        except:
            user = User.objects.create(username = username, password=password)
            # messages.error(request, "User Created.")
            # return redirect('register')
            # Authenticate
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now registered')
            return redirect('login')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, "User not found.")
                return redirect("login")
            else:

                if user.password != password:
                    messages.error(request, "Wrong Password.")
                    return redirect("login")
                
                request.session['user_id'] = user.id
                return render(request, 'index.html', context={'user':user})
            
            
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    request.session.pop('user_id',None)
    return redirect('home')


def Fill_profile(request):
     redirect('home')