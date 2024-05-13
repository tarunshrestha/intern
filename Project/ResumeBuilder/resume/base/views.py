from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.
def index(request):
    return HttpResponse("Hello Testing.")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.Post)
    else:
        form = SignUpForm()
        return render(request, "register.html")