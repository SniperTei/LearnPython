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
        return Response({
            "list": serializer.data,
        })
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# class LoginView(APIView):
#     def post(self, request):
#         # 获取token
#         serializer = MyTokenObtainPairSerializer(data=request.data)
#         token = serializer.get_token()
#         print("serializer: ", serializer)
#         if serializer.is_valid():
#             return Response({
#                 "token": '1'
#             })
#         return Response({
#             "code": "100001",
#             "msg": serializer.errors,
#         })

# token
class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    serializer_class = MyTokenObtainPairSerializer
    # 如果需要自定义返回的数据，可以重写post方法
    def post(self, request, *args, **kwargs):
        # 调用父类的post方法
        response = super().post(request, *args, **kwargs)
        # 获取token
        token = response.data.get('access')
        # 获取用户信息
        user = CustomUser.objects.get(username=request.data.get('username'))
        print("user: " , user)
        # 返回数据
        return Response({
            "token": token
        })

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

