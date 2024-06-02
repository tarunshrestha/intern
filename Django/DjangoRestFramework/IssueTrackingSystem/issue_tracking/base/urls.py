from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('userinfo/', UserAPI.as_view()),
    path('logout', UserLogout.as_view()),
    path('register/', RegisterAPI.as_view()),

    # path('dashboard/', UserTicketApi.as_view()),
    path('user_ticket/', UserTicketApi.as_view()),
    path('developer_ticket/', DevUserApi.as_view()),
    path('comment/', CommentApi.as_view()),

    

]