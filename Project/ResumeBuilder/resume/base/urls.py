from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('resume/', views.Fill_profile, name='dada'),

]