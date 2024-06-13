from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('room/<str:room_name>?<str:username>/', MessageView, name='room'),


]