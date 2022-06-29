from pyexpat import model
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
    # student_form = forms.student_form()
    
    student_form = forms.student_form()
    # diction = {"new_form": student_form}
    if(request.method == "POST"):
        studen_model = students(request.POST)
        if(student_form.is_valid()):
            studen_model.save(commit=True)
            return student(request)
        else:
            print("Error")
    diction = {"form": student_form}
    return render(request, "my_app/form.html", context=diction)
    
            