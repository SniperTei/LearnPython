from rest_framework import serializers
from snipermovie.user_s.models import User_S
# from django.contrib.auth.models import User

class User_SSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_S
    fields = '__all__'