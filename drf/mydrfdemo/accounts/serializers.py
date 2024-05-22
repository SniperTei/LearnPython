from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
#   username = serializers.CharField(
#     max_length=150,
#     min_length=6,
#     error_messages={
#       'max_length': '用户名不能超过150个字符',
#       'min_length': '用户名不能少于6个字符',
#       'required': '用户名是必填的',
#       'blank': '用户名不能为空'
#     }
#   )
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'nickname', 'email', 'mobile', 'menu_permissions']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    token验证
    '''

    def validate(self, attrs):
        print('attrs:', attrs)
        print('self:', self)

        authenticate_kwargs = {
            'username': attrs['username'],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
            print('authenticate_kwargs:', authenticate_kwargs)
        except KeyError:
            pass

        '''
        Checking if the user exists by getting the email(username field) from authentication_kwargs.
        If the user exists we check if the user account is active.
        If the user account is not active we raise the exception and pass the message. 
        Thus stopping the user from getting authenticated altogether. 
        
        And if the user does not exist at all we raise an exception with a different error message.
        Thus stopping the execution righ there.  
        '''
        try:
         user = CustomUser.objects.get(username=authenticate_kwargs['username'])
         if not user.is_active:
             self.error_messages['no_active_account']= (
                 'The account is inactive0'
             )
             raise exceptions.AuthenticationFailed(
                 self.error_messages['no_active_account'],
                 'no_active_account0',
             )
        except CustomUser.DoesNotExist:
          self.error_messages['no_active_account'] = (
              'Account does not exist0')
          raise exceptions.AuthenticationFailed(
              self.error_messages['no_active_account'],
              'no_active_account0',
          )
        
        '''
        We come here if everything above goes well.
        Here we authenticate the user.
        The authenticate function return None if the credentials do not match 
        or the user account is inactive. However here we can safely raise the exception
        that the credentials did not match as we do all the checks above this point.
        '''
        
        # self.user = authenticate(**authenticate_kwargs)
        # if self.user is None:
        #     self.error_messages['no_active_account'] = _(
        #         'Credentials did not match0')
        #     raise exceptions.AuthenticationFailed(
        #         self.error_messages['no_active_account'],
        #         'no_active_account0',
        #     )
        
        data = super().validate(attrs)
        return data

    
        # data = super().validate(attrs)
        # refresh = self.get_token(self.user)

        # data['refresh'] = str(refresh)
        # data['access'] = str(refresh.access_token)
        # data['myname'] = 'mynameisjason'
        # # 打印self.user
        # print('self.user:', self.user)
        # # data['username'] = self.user.username #这个是你的自定义返回的
        # # data['user_id'] = self.user.id #这个是你的自定义返回的
        # return data
    
    def validate_username(self, value):
        print('value:', value)
        return value

