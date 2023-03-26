from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from myglory.models import GloryHero
from myglory.serializers import GloryHeroSerializer


class GloryHeroList(ModelViewSet):
    
    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer
    
    def get_all_heros(self, request):
        return self.list(request)

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