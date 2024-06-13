from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        room = request.POST['room']

        get_room = Room.objects.get_or_create(room_name = room)
        print(get_room)
        return redirect('room',room_name = room, username=username)

    return render(request, 'index.html')

def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    get_message = Message.objects.filter(room=room)

    return render(request, 'message.html', context={
        'messages':get_message,
        'user':username,
        "room_name":room
    })