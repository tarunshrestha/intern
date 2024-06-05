from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('accounts/profile/', UserAPI.as_view()),
    # path('logout', UserLogout.as_view()),
    path('register/', RegisterAPI.as_view()),

    path('example/', ExampleView.as_view()),


    # path('dashboard/', UserTicketApi.as_view()),
    re_path(r'^user/ticket(?:/(?P<pk>\d+))?/$', UserTicketApi.as_view({'patch': 'partial_update'}),name="user_ticket"),
    re_path(r'^developer/ticket(?:/(?P<pk>\d+))?/$', DevUserApi.as_view({'patch': 'partial_update'}), name="developer_ticket"),
    path('comment/', CommentApi.as_view()),

    

]