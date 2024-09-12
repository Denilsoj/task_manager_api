from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name'] 

        extra_kwargs = {
        'username': {'required': True},
        'email':{'required': True},
        'password': {'write_only': True, 'required': True},     
        'first_name': {'write_only': True, 'required': True},   
        'last_name': {'write_only': True, 'required': True}     
         }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password']) 
        user.save()
 
        return user
class UserLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    user = UserLimitedSerializer(read_only=True)
    class Meta: 
        model = Task
        fields = ['id', 'title', 'description', 'date', 'time_start', 'time_end', 'google_event_id', 'user']

        extra_kwargs = {
            'title': {'required': True},
            'date': {'required': True},
            
        }