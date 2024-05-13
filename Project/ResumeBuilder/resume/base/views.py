from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("Hello Testing.")


def register_user(request):
    if request.user.is_authenticated:  # if user is logged in user gets thrown to home page.
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now registered')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})