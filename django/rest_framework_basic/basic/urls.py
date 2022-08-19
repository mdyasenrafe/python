from basic import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("", views.first_view , name="first_view"),
    path("contact", views.contactApi , name="contact_api"),
    path("registation", views.registation_api , name="registation_api"),
    # path("user" , views.userApi , name="user_api"),
    path("blog" , views.post_create_api.as_view() , name="user_api"),
]