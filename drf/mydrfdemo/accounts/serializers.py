from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'nickname', 'email', 'mobile', 'menu_permissions']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    token验证
    '''
    def validate(self, attrs):
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

