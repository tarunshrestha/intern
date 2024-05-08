from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *

# Create your views here.
def index(request):
    
    return render(request, "index.html")

def login_page(request,user_id):
    form = LoginForm()
    if request.method == "Post":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, "index.html")
    return render(request, "login.html", context={'form':form})

def register_user(request):
    faculty = Faculty.objects.all()
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        birth_date = request.POST['birth_date']
        phone_number = request.POST['phone_number']
        user_type = request.POST['user_type']
        password = request.POST['password']
        password2 = request.POST['password2']
        faculty = request.POST['faculty']
        
        print("-----------------------Tarun-----------------------------",faculty)
        return HttpResponse("Chalyo")
    else:
        form = RegisterForm()
        return render(request, "register.html", context={'form':form, 'faculty':faculty})
