from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Checking.......")

def login_page(request):
    
    return HttpResponse("Login-Page")
