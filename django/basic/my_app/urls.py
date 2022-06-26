from django.contrib import admin
from django.urls import URLPattern, path
from my_app import views

urlpatterns = [
    path("", views.home , name="home"),
    path("blogs", views.blogs , name="blogs"),
]