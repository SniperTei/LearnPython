from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from myglory.models import GloryHero
from myglory.serializers import GloryHeroSerializer


class GloryHeroList(ModelViewSet):
    
    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_all_heros(self, request):
        print("request.user ", request.user.id)
        if request.user.id is None:
            return Response("未登录用户：游客")
        else:
            return self.list(request)
            # return Response(f"已登录用户：{request.user}")


    def add_one_hero(self, request):
        return self.create(request)


class GloryHeroDetail(ModelViewSet):

    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer

    def get_one_hero(self, request, pk):
        return self.retrieve(request, pk)

    def edit_one_hero(self, request, pk):
        return self.update(request, pk)

    def delete_one_hero(self, request, pk):
        return self.destroy(request, pk) # DestroyModelMixin提供的方法