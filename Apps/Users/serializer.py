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
