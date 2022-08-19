from os import stat
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import blog_serializer, contact_serializer, user_serializer, user_serializer_one
from rest_framework.generics import CreateAPIView
from basic.models import Blog, Contact
from django.contrib.auth.models import User


# registation
@api_view(["POST"])

def registation_api(request):
    if request.method == "POST" :
        username =  request.data["username"]
        email = request.data["email"]
        name = request.data["name"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]
        if User.objects.filter(username = username).exists():
            return Response({"error" : "An User with that username already exists!"})
        if(password1 != password2) :
              return Response({"error" : "Two Password did not matched!"})
        user = User()
        user.username= username
        user.email = email
        user.name = name
        user.is_active = True 
        user.set_password(raw_password=password1)
        user.save()

        return ({"status" : "sucess" })

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


# @api_view(['GET' , 'POST' , 'PUT'])
# def userApi(request):
#     if request.method == 'POST':
#         data = request.data
#         serializer = user_serializer(data = data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response({"status": "success" ,  "data" :  serializer.data})
#         else :
#             return Response({"status": "error" ,  "data" :  serializer.errors})
    # elif  request.method == 'PUT':
    #     data = request.data
    #     user = User.objects.get(email = data['email'])
    #     userSerializer = user_serializer_one(data = data , instance=user)
    #     if userSerializer.is_valid() :
    #         obj = userSerializer.save()
    #         return Response({"status": "success" ,  "data" :  obj})
    #     else :
    #         return Response({"status": "error" ,  "data" :  userSerializer.errors})
    # else:
    #     query = User.objects.all()
    #     userSerializer = user_serializer(query, many=True)
    #     return Response({"status": "success" ,  "data" :  userSerializer.data})

class post_create_api(CreateAPIView) :
    permission_classes =["IsAuthenticated",]
    queryset = Blog.objects.all()
    serializer_class = blog_serializer