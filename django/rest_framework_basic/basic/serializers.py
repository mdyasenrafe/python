from rest_framework import serializers
from basic.models import Blog, Contact,  User


class contact_serializer(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = ['name' , 'email' , 'message']

class user_serializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['name' , 'email' , 'password']

class user_serializer_one(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        email = serializers.EmailField(max_length=254)
        password = serializers.CharField(max_length=50)

        def create(self, validated_data):
            return User(**validated_data)
    
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.password = validated_data.get('password', instance.password)
            instance.save()
            return instance

class blog_serializer(serializers.ModelSerializer) :
    class Meta:
        model = Blog
        fields = "_all_" 