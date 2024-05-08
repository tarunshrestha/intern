from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<str:user_type>/<int:user_id>/login', views.login_page, name="login"),
    path('register_user', views.register_user, name="register"),

]