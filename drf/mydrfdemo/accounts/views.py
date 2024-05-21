from rest_framework import viewsets
from .models import CustomUser
# APIView
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.response import Response

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

# ModelViewSet
# class CustomUserView(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
