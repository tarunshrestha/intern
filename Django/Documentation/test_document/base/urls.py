from django.urls import path, include
from . import views

app_name='polls'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]