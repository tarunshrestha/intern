from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import handler403

handler403 = custom_permission_denied_view


urlpatterns = [
    path('create/', autofeed),
    path('', index),

]
