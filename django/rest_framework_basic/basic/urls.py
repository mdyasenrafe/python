from basic import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("", views.first_view , name="first_view"),
    path("contact", views.contactApi , name="contact_api"),
]