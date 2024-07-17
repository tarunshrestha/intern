from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView,TokenRefreshView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index, name='home'),
    # path('post_todo/', post_todo, name='post_todo'),
    # path('get_todo/', get_todo, name='get_todo'),
    # path('get/', get_individual, name='get_individual'),
    # path('patch_todo/', patch_todo, name='patch_todo'),

    path('todo/', TodoView.as_view()),
    path('register/', RegisterAPI.as_view({'post':'create'}), name='register'),
    path('verify/', VerifyOTP.as_view()),
    path('login/', LoginUser.as_view()),
    path('userinfo/', UserAPI.as_view()),
    path('logout', UserLogout.as_view()),
    

    #Token
    # path('api/toekn/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += staticfiles_urlpatterns()