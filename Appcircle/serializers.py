from rest_framework.serializers import ModelSerializer
from .models import Circle, CircleUser
from django.contrib.auth.models import User
from rest_framework import serializers

class CircleUserSerializer(ModelSerializer):
    class Meta:
        model = CircleUser
        fields = ['name', 'role', 'users']

class CircleSerializer(ModelSerializer):
    class Meta:
        model = Circle
        fields = ['circleuser', 'id', 'name', 'description', 'image', 'created_by']