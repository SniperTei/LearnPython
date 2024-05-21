from django.shortcuts import render
# import APIView
from rest_framework.views import APIView
# import Response
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

class MovieView(APIView):
    def get(self, request):
        # 获取所有电影
        movies = Movie.objects.all()
        # 序列化
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)