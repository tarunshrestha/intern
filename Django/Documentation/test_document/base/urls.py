from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('<int:question_id>/result', views.result),
    path('<int:question_id>/vote', views.vote),
]