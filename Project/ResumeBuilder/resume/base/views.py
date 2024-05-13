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
        username = request.POST['username']
        email = request.POST['email']
        birth_date = request.POST['birth_date']
        address = request.POST['address'] 
        phone_number = request.POST['phone_number']
        # gender_value = request.POST['gender']
        password = request.POST['password']
        password2 = request.POST['password2']

        # user = User.objects.get(username=username) # delete user to check 
        # custom_user = CustomUser.objects.get(username=username) # delete customuser to check 
        # user.delete()
        # custom_user.delete()

        if password !=password2:
            messages.error(request, "Password doesnot match.")
            return redirect('register')
            
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "User already exists.")
            return redirect('register')

        user = User.objects.create(username = username, password=password)
        print("--------------------------------------------------------------------------")
        # print(gender_value)
        # gender = str(gender_value)
        custom_user = CustomUser.objects.create(
            user_id=user,
            username = username,
            password=password,
            first_name=first_name, 
            last_name=last_name,
            address=address,
            phone=phone_number,
            # gender=gender_value,
            email = email,
            date_of_birth=birth_date,
        )
        
        # Authenticate
        # user = authenticate(username=username, password=password)
        # login(request, user)
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
                user = User.objects.get(username__iexact=username)
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
    if not request.user.is_authenticated: 
        return render(request, 'index.html')
    logout(request)
    return redirect('home')


def User_profile(request, user_id):
    users = User.objects.filter(pk=user_id)
    personal_info = users.prefetch_related('custom_user_set').get(pk=user_id)
    return render(request, 'user_profile.html', context={'user':users, "personal_info":personal_info})

def Update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'update_profile.html', context={'user':user})