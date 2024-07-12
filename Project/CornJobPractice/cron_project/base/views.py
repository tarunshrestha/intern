from django.shortcuts import render
from django.http import HttpResponse
from .models import Test

# Create your views here.
def autofeed(request): 
    data = ["Test", "Choice", "me"]   
    try:
        for i in data:
            instance = Test.objects.get_or_create(name=i)
        return HttpResponse("DONE")
    except Exception as e :
        return HttpResponse(f'Error: {e}')
    