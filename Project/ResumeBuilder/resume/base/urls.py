from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile/<int:user_id>/', views.User_profile, name='profile'),
    path('update/<int:user_id>/', views.Update_profile, name='update_profile'),
    path('update_info/<int:user_id>/', views.update_info, name='update_info'),
    path('update_education/<int:user_id>/', views.update_education, name='update_education'),
    path('update_job/<int:user_id>/', views.update_job, name='update_job'),
    path('update_project/<int:user_id>/', views.update_project, name='update_project'),
    path('update_ref/<int:user_id>/', views.update_ref, name='update_ref'),

    # path('fake', views.Create_fake_profile),

]