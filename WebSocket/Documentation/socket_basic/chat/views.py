from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test")


def room(request, room_name):
    return render(request, 'chat_temp/room.html', {'room_name':room_name})
