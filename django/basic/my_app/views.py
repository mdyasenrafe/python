from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from my_app import forms
from .models import students
# Create your views here.

def home(request):
    return HttpResponse("Hello World!")

def student(request):
    # studentsList = students.objects.all()
    studentsList = students.objects.order_by("name")
    diction = {"students": studentsList}
    return render(request, "my_app/index.html", context=diction)

def form (request):
    student_form = forms.student_form()
    diction = {"form": student_form}
    return render(request, "my_app/form.html" , context=diction)