from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def home(request):
    dests=Destination.objects.all()

    return render(request, "index.html",{'dests':dests})
