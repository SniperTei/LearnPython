from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookListView(APIView):
    def get(self, request):
        book_lists = Book.objects.all()
        return Response(book_lists)

    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # 删除一本书
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response('删除成功')

    # 更新一本书
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)