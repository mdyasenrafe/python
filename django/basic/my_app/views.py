from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello World!")

def blogs(request):
    diction = {}
    return render(request, "my_app/index.html", context=diction)