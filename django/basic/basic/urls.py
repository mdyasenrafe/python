from django import views
from django.contrib import admin
from django.urls import path , include
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("my_app.urls")),
]