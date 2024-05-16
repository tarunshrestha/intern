from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import  User
from .forms import *
from django.contrib import messages
from faker import Faker
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('login')  # Redirect to login page or another appropriate page
        
        else:
            # Print the errors to the console for debugging
            print(form.errors)
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request, 'index.html', context={'user':user})     
            else:
                messages.sucess(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    if not request.user.is_authenticated: 
        return render(request, 'index.html')
    logout(request)
    return redirect('home')


def User_profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('home')

    users = CustomUser.objects.filter(pk=user_id).first()
    return render(request, 'user_profile.html', context={'users':users})

def Update_profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('home')
    user = CustomUser.objects.get(pk=user_id)
    link_form = PersonalInformationForm()
    education_form = EducationForm() 
    job_form = JobForm()
    project_form = ProjectForm()
    ref_form = ReferenceForm()
    return render(request, 'update_profile.html', context={
        'users':user, 
        'link_form':link_form, 
        'education_form':education_form, 
        'job_form':job_form,
        'project_form':project_form,
        'ref_form':ref_form
        })


def update_info(request, user_id):
    if request.method == "POST":
        user = CustomUser.objects.get(pk=user_id)
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        summary = request.POST['summary']
        if user.social_media.exists():
            user.social_media.update(linkedin = linkedin, github =github, summary=summary)
            messages.success(request, "Personal information updated successfully.")
        else:
            user.social_media.create(linkedin = linkedin, github =github, summary=summary)
            messages.success(request, "Personal information created.") 
        return redirect('update_profile', user_id=user_id)

        # user = CustomUser.objects.get(pk=user_id)
        # links = PersonalInformation.objects.create(user=user, )


def update_education(request, user_id):
    if request.method == "POST":
        user = CustomUser.objects.get(pk=user_id)
        title = request.POST['title']
        faculty = request.POST['faculty']
        institution_name = request.POST['institution_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        score = request.POST['score']

        user.educations.get_or_create(
            title=int(title),
            faculty=faculty,
            institution_name=institution_name,
            start_date=start_date,
            end_date=end_date,
            score=score
               )
        messages.success(request, "Education updated successfully.")
        return redirect('update_profile', user_id=user_id)



def update_job(request, user_id):
    if request.method == "POST":
        user = CustomUser.objects.get(pk=user_id)
        position = request.POST['position']
        company = request.POST['company']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        form = user.jobs.get_or_create(company = company)
        form.update(
            position=position,
            start_date=start_date,
            end_date=end_date
               )
        messages.success(request, "Jobs updated successfully.")
        return redirect('update_profile', user_id=user_id)


    return redirect('update_profile')

def update_project(request, user_id):
    if request.method == "POST":
        user = CustomUser.objects.get(pk=user_id)
        name = request.POST['name']
        description = request.POST['description']
        form = user.project.get_or_create(name = name)
        form.update(description=description)
        messages.success(request, "Projects updated successfully.")
        return redirect('update_profile', user_id=user_id)

    return redirect('update_profile')

def update_ref(request, user_id):
    if request.method == "POST":
        user = CustomUser.objects.get(pk=user_id)
        reference_text = request.POST['reference_text']
        if user.reference.exists():
            user.reference.first().delete()
        user.reference.get_or_create(reference_text=reference_text)
        return redirect('update_profile', user_id=user_id)



def Create_fake_profile(request):
    faker = Faker()

    for i in range(10):
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = 'fakename' + str(i)
        email = faker.email()
        birth_date = faker.date_of_birth()
        address = faker.address ()
        phone_number = faker.phone_number()
        gender_value = random.randint(1, 3)
        password = faker.password()

        user = User.objects.create(username = username, password=password)
        custom_user = CustomUser.objects.create(
            user_id=user,
            username = username,
            password=password,
            first_name=first_name, 
            last_name=last_name,
            address=address,
            phone=phone_number,
            gender=gender_value,
            email = email,
            date_of_birth=birth_date,
        )
    return HttpResponse("Fake Created")
