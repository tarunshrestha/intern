from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('snippet/', snippet_list, name='list'),
    path('snippet/<int:pk>', snippet_detail),

]