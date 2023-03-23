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
    
    def put(self, request):
        # serializer = GloryHeroSerializer(data=request.data)
        # try:
        #     serializer.is_valid(raise_exception=True)
        #     print(serializer.validated_data)
        #     gloryheros = GloryHero.objects.get(id=id).update(**serializer.validated_data)
        #     print("gloryheros: ", gloryheros)
            # serializer = GloryHeroSerializer(gloryheros)
            return Response({"aaa":"123"}, status=200)
        # except Exception as e:
        #     return Response(serializer.errors, status=200)
    
    # def put(self, request, id):
    #     print("put id: ", id)
    #     serializer = GloryHeroSerializer(data=request.data)
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #         print(serializer.validated_data)
    #         gloryheros = GloryHero.objects.get(id=id).update(**serializer.validated_data)
    #         print("gloryheros: ", gloryheros)
    #         # serializer = GloryHeroSerializer(gloryheros)
    #         return Response(serializer.data, status=200)
    #     except Exception as e:
    #         return Response(serializer.errors, status=200)
    
    def delete(self, request, id):
        gloryheros = GloryHero.objects.get(id=id)
        gloryheros.delete()
        return Response(status=200)
    