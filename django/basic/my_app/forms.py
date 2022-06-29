from django import forms
from .models import students

class student_form(forms.Form):
    # name = forms.CharField(max_length=50)
    # age = forms.IntegerField()
    # email = forms.EmailField()
    # number = forms.IntegerField()
        class Meta:
            model = students
            fields = "__all__"

# class Student_form(forms.Form):

        
