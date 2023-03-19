from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from myglory.models import GloryHero
from myglory.serializers import GloryHeroSerializer


class GloryHeroList(APIView):
    
    def get(self, request):
        gloryheros = GloryHero.objects.all()
        serializer = GloryHeroSerializer(gloryheros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GloryHeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=200)
    
    