from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    Authors = Author.objects.all().order_by('name')
    entry = Entry.objects.all()
    return render(request, 'index.html', {'Authors': Authors, "Entry":entry})
