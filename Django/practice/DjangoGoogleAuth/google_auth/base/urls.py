from django.urls import path
from allauth.account.views import LoginView

urlpatterns = [
    path('login/', LoginView),

]