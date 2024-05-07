from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login_page', views.login_page, name="login"),
]