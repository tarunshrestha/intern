from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile/<int:user_id>/', views.User_profile, name='profile'),
    path('update/<int:user_id>/', views.Update_profile, name='update_profile'),
    # path('fake', views.Create_fake_profile),

]