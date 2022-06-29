from os import stat
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import contact_serializer, user_serializer

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
        serializer = contact_serializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": "success" ,  "data" :  serializer.data})
        else: 
            return Response({"status": "error" ,  "data" :  serializer.errors})
    else:
        return Response({"status": "success" })


@api_view(['GET' , 'POST'])
def userApi(request):
    if request.method == 'POST':
        data = request.data
        serializer = user_serializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": "success" ,  "data" :  serializer.data})
        else :
            return Response({"status": "error" ,  "data" :  serializer.errors})
    else:
        return Response({"status": "success" })
      


