from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout, name="logout"),

    path('register_user', views.register_user, name="register"),

]