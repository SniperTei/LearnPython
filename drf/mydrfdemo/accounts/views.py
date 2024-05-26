# from rest_framework import viewsets
from .models import CustomUser
from django.contrib.auth import get_user_model
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
            "token": token,
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "nickname": user.nickname,
        })

class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    serializer_class = TokenRefreshSerializer

# 注册
class RegisterView(APIView):
    def post(self, request):
        # serializer = CustomUserSerializer(data=request.data)
        username = request.data.get('username')
        # 判断用户是否存在
        user = CustomUser.objects.filter(username=username)
        # 用户名不能为空
        if not username:
            return Response({
                "code": "100001",
                "msg": "用户名不能为空",
            })

        # 用户名要大于6位
        if len(username) < 6:
            return Response({
                "code": "100004",
                "msg": "用户名不能小于6位",
            })

        if user:
            return Response({
                "code": "100002",
                "msg": "用户已存在",
            })
        
        password = request.data.get('password')

        # 密码不能为空
        if not password:
            return Response({
                "code": "100003",
                "msg": "密码不能为空",
            })
        
        email = request.data.get('email')
        if not email:
            return Response({
                "code": "100005",
                "msg": "邮箱不能为空",
            })
        user = CustomUser.objects.create_user(
            username=username, 
            password=password, 
            email=email,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        user.save()
        return Response({
            "username": username,
        })
        # 将user反序列化然后存到数据库中
        # serializer = CustomUserSerializer(instance=user)
        # if serializer.is_valid():
        #     # serializer.save()
        #     return Response({
        #         "code": "000000",
        #         "msg": "success",
        #         "data": serializer.data
        #     })
        # return Response({
        #     "code": "100006",
        #     "msg": "注册失败",
        # })


class UnRegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        user = CustomUser.objects.filter(username=username)
        if not user:
            return Response({
                "code": "100007",
                "msg": "用户不存在",
            })
        user.delete()
        return Response({})
