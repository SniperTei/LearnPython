# from rest_framework import viewsets
from .models import CustomUser
# APIView
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase

class CustomUserView(APIView):
    def get(self, request):
        # custom_users = CustomUser.objects.all()
        # serializer = CustomUserSerializer(custom_users, many=True)
        # 获取所有用户
        custom_users = CustomUser.objects.all()
        # 序列化
        serializer = CustomUserSerializer(custom_users, many=True)
        # data = {
        #     "message": "This is a custom response",
        #     "status": "success",
        #     "data": {
        #         "example_key": "example_value"
        #     }
        # }
        return Response(serializer.data)
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# token
class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    serializer_class = TokenRefreshSerializer

# ModelViewSet
# class CustomUserView(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# 登录
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from django.contrib.auth import authenticate
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# # from rest_framework_jwt.views import obtain_jwt_token
# # Login
# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         # 获取用户名和密码
#         username = request.data.get('username')
#         # 打印用户名
#         print(username)
#         password = request.data.get('password')
#         print(password)
#         # 验证用户名和密码
#         user = authenticate(username=username, password=password)
#         if user:
#             # 生成token
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
