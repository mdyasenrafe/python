from os import stat
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import contact_serializer

from basic.models import Contact

# Create your views here.
@api_view(['GET' , 'POST'])
def first_view(request):
    if request.method == 'POST':
        return Response({"status": "success" ,  "data" :  request.data})
    else:
        return Response({"status": "success"  , 'message': 'Hello World'})

@api_view(['GET' , 'POST'])
def contactApi(request):
    if request.method == 'POST':
        data = request.data
        name = data['name']
        email = data['email']
        message = data['message']
        contact = Contact(name = name , email = email  , message = message)
        contact.save()
        return Response({"status": "success" ,  "data" : data})
    else:
        return Response({"status": "success" })

      


