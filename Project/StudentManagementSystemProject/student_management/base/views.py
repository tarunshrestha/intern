from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout



# Create your views here.
def index(request):
    
    return render(request, "index.html")


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out.....')
    return redirect('home')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username'].lower
        password = request.POST['password']
        user_type = request.POST['user_type']

        try : 
            if (Teacher.objects.get(username = username) != None) or (Student.objects.get(username = username) != None) :
                if user_type == "Teacher":
                    user = Teacher.objects.get(username=username)
                else:
                    user = Student.objects.get(username=username)
        except:
            messages.error(request,'Username doesnot exists.')
            return redirect('login')
            
                    
        if password == user.password:
            pass
        else:
            messages.error(request,'Password match garena, Try again.')
            return redirect('login')

        print(user.username)
        messages.success(request,f'Hi {username}, welcome back!')
        return render(request, 'home')

        # if user:
        #     login(request, user)
        #     messages.success(request,f'Hi {username.title()}, welcome back!')
        #     return redirect('home')
    else:
        form = LoginForm()
        # messages.success(request,f'Hi, welcome back!')
        return render(request, "login.html", {'form':form})

def register_user(request):
    faculty = Faculty.objects.all()
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username'].lower()
        birth_date = request.POST['birth_date']
        address = request.POST['address'] 
        phone_number = request.POST['phone_number']
        user_type = request.POST['user_type']
        password = request.POST['password']
        password2 = request.POST['password2']
        faculty = request.POST['faculty']
        # print('-----------------------------------',user_type)


        if first_name == '' or last_name == '' or address == '' or username == '' or phone_number == '' or password == '':
            messages.error(request,'All Fields should be filled.')
            return  redirect('register')

        if password != password2:
            messages.error(request,'Password doesnot match with Password2.')
            return  redirect('register')
        else:
            if len(password) < 8:
                messages.error(request,'Password should contain special charecters and have 8 letters.')
                return  redirect('register')
    
        try : 
            if (Teacher.objects.get(username = username) != None) or (Student.objects.get(username = username) != None) :
                pass
        except:
            pass
        else:
            messages.error(request,'Username already exists.')
            return  redirect('register')
        
        if user_type == "teacher":
            user = Teacher.objects.create(first_name=first_name,
                                           last_name=last_name, 
                                           username=username, 
                                           password=password, 
                                           birth_date=birth_date, 
                                           address=address,
                                           phone_number=phone_number, 
                                           faculty=Faculty.objects.get(name=faculty))
        else:
            user = Student.objects.create(first_name=first_name,
                                           last_name=last_name, 
                                           username=username, 
                                           password=password, 
                                           birth_date=birth_date, 
                                           address=address,
                                           phone_number=phone_number, 
                                           faculty=Faculty.objects.get(name=faculty))
        user.save()
        # user = LoginForm(username=username, password=password)
        # LoginForm(request, user)
        # messages.success(request, 'You are now registered')
        return redirect("home")
    else:
        # form = RegisterForm()
        return render(request, "register.html", context={'faculty':faculty})
