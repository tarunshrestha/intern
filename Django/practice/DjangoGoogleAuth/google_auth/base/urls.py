from django.urls import path
from allauth.account.views import LoginView
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', home)

]