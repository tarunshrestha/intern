from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('accounts/profile/', UserAPI.as_view()),
    # path('logout', UserLogout.as_view()),
    path('accounts/register/', RegisterAPI.as_view()),

    path('example/', ExampleView.as_view()),


    # path('dashboard/', UserTicketApi.as_view()),
    path('accounts/ticket/', UserTicketApi.as_view(),  name="user_ticket"),
    path('developer/ticket/', DevUserApi.as_view(), name="developer_ticket"),
    path('comment/', CommentApi.as_view()),

    

]