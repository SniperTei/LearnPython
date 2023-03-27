from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from myglory.models import GloryHero
from myglory.serializers import GloryHeroSerializer


class GloryHeroView(ModelViewSet):
    
    queryset = GloryHero.objects.all()
    serializer_class = GloryHeroSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_all_heros(self, request):
        print("request.user ", request.user.id)
        return self.list(request)

    def add_one_hero(self, request):
        return self.create(request)

    def get_one_hero(self, request, pk):
        return self.retrieve(request, pk)

    def edit_one_hero(self, request, pk):
        return self.update(request, pk)

    def delete_one_hero(self, request, pk):
        return self.destroy(request, pk) # DestroyModelMixin提供的方法