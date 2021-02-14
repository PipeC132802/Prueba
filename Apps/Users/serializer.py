from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']


class UserActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=20)
    password1 = serializers.CharField(max_length=20)
    password2 = serializers.CharField(max_length=20)
