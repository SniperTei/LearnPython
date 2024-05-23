# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MovieView(APIView):
    """
    电影视图
    """
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        print('movie request ; ', request)
        # simplejwt的token校验用户是否有登录
        print('request.user:', request.user)
        if request.user.is_anonymous:
            return Response({
                'code': '200000',
                'msg': '请先登录'
            })
        # 获取所有电影
        movies = Movie.objects.all()
        # 序列化
        serializer = MovieSerializer(movies, many=True)
        result_data = {
            'list': serializer.data,
            'total': len(serializer.data),
        }
        return Response(result_data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
