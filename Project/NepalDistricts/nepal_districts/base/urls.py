from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('municipality/', MunicipalityApi.as_view({'get':'list', 'retrieve':'retrieve'})),
    path('municipality/update/<int:pk>', MunicipalityApi.as_view({'get':'retrieve', 'post':'create'})),

    # path('add/', add_districts, name='add-districts'),
    path('export/', export_data, name='export'),



]