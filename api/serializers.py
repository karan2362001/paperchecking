from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

