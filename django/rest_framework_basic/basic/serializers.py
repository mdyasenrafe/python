from rest_framework import serializers
from basic.models import Contact,  User


class contact_serializer(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = ['name' , 'email' , 'message']

class user_serializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['name' , 'email' , 'password']