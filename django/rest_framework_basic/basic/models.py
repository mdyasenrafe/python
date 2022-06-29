from django.db import models
import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name 

class User(models.Model):
    now = datetime.datetime.now()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254 , unique=True )
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.email


