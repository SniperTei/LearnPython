from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.response import Response
from .models import CustomUser
import re

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'nickname', 'email', 'mobile', 'menu_permissions']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # def get_token(cls, user):
    #     # super()--->代指父类对象--》
    #     # 对象调用类的绑定方法--->会自动把对象的类传入到方法的第一个参数
    #     token = super().get_token(user)
    #     print('token:', token)
    #     # Add custom claims
    #     token['username'] = user.username
    #     return token

    '''
    token验证
    '''
    def validate(self, attrs):
        print('attrs:', attrs)

        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['myname'] = 'mynameisjason'
        # 打印self.user
        print('self.user:', self.user)
        # data['username'] = self.user.username #这个是你的自定义返回的
        # data['user_id'] = self.user.id #这个是你的自定义返回的
        return data
    
    def validate_username(self, value):
        print('value:', value)
        return value

