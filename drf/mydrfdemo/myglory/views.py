from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from myglory.models import GloryHero
from myglory.serializers import GloryHeroSerializer


class GloryHeroList(GenericAPIView, ListModelMixin, CreateModelMixin):
    
    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer
    
    def get(self, request):
        return self.list(request) # ListModelMixin提供的方法

    def post(self, request):
        return self.create(request) # CreateModelMixin提供的方法
    
    
class GloryHeroDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk) # RetrieveModelMixin提供的方法
    
    def put(self, request, pk):
        print('put : ', request.data)
        return self.update(request, pk) # UpdateModelMixin提供的方法
    
    def delete(self, request, pk):
        return self.destroy(request, pk) # DestroyModelMixin提供的方法