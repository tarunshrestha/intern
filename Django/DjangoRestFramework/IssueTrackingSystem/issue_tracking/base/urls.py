from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('user/profile/', UserAPI.as_view()),
    # path('logout', UserLogout.as_view()),
    path('register/', RegisterAPI.as_view()),

    path('example/', ExampleView.as_view()),


    # path('dashboard/', UserTicketApi.as_view()),
    re_path(r'^user/ticket(?:/(?P<pk>\d+))?/$', UserTicketApi.as_view({'patch': 'update'}),name="user_ticket"),
    re_path(r'^developer/ticket(?:/(?P<pk>\d+))?/$', DevUserApi.as_view({'patch': 'update'}), name="developer_ticket"),
    path('comment/', CommentApi.as_view()),

    re_path(r'^account/admin(?:/(?P<pk>\d+))?/$', AdminApi.as_view({'get':'get'}), name="admin"),

    

]