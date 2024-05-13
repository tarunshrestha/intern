from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("Hello Testing.")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
             messages.error(request, "Please check the form again.")
             return redirect('register')
             
    else:
        form = SignUpForm()
        return render(request, "register.html")