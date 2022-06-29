from rest_framework import serializers
from basic.models import Contact


class contact_serializer(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = ['name' , 'email' , 'message']

        
