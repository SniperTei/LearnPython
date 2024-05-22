# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MovieView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        # 如果校验没过
        # if not request.user.is_authenticated:
        #     return Response("用户未登录")
        # 获取所有电影
        movies = Movie.objects.all()
        # 序列化
        serializer = MovieSerializer(movies, many=True)
        return Response({
            "msg": "success",
            "code": "000000",
            "data": serializer.data
        })
        # return Response(serializer.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
