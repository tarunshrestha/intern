from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    # path('snippet/', snippet_list, name='list'), 
    # path('snippet/<int:pk>', snippet_detail), 

    path('user/', UserAPI.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetailAPI.as_view(), name='user-detail'), 

    path('snippet/', SnippetList.as_view(), name='snippet-list'), 
    path('snippet/<int:pk>', SnippetDetail.as_view(), name='snippet-detail'), 
    path('snippet/<int:pk>/hightlight/', SnippetHighlight.as_view(), name='snippet-highlight'), 

#   
    path('api-auth/', include('rest_framework.urls')),

    path('', api_root),

]

urlpatterns= format_suffix_patterns(urlpatterns)
# json suffix : http://127.0.0.1:8000/snippet.json