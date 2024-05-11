from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello Testing.")


def register_user(request):
    return render(request, "register.html")