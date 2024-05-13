from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.session != None :
        redirect ('login')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST['username'].lower()
        try:
            user = CustomUser.objects.get(username= username)
        except:
            messages.error(request,"User already exists.")
            return redirect('register')
        
        if form.is_valid():
            form.save()
            return HttpResponse("Registered")
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                user = CustomUser.objects.get(username=username)
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