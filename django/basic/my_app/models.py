from operator import mod
from django.db import models
from numpy import number

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.IntegerField()

    def __str__(self):
        return self.name