from django.contrib import admin
from django.urls import URLPattern, path
from my_app import views

urlpatterns = [
    path("", views.home , name="home"),
    path("students", views.student , name="blogs"),
    path("forms", views.form , name="form"),
]