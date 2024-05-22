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

# 注册
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": "000000",
                "message": "success",
                "data": serializer.data
            })
        return Response({
            "code": "100001",
            "message": "fail",
            "data": serializer.errors
        })

