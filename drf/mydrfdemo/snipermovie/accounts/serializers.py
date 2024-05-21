from rest_framework import serializers
from .models import CustomUser
# from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'bio', 'location', 'account_type']
    extra_kwargs = {'password': {'write_only': True}}

  # def create(self, validated_data):
  #   user = User.objects.create_user(
  #     username=validated_data['username'],
  #     email=validated_data['email'],
  #     password=validated_data['password']
  #   )
  #   return user