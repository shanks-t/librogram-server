from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from librogramapi.models import Book, Comment, UserBook, Tag
from librogramapi.serializers.book_serializer import BookSerializer

class BookView(ViewSet):
    
    def create(self, request):

        user = User.objects.get(username=request.auth.user)
        book = Book.objects.create(
            user=user,
            title=request.data["title"],
            author=request.data["author"],
            image_path=request.data["imagePath"],
            description=request.data["description"],
            page_count=request.data["pageCount"],
            publisher=request.data["publisher"],
            date_published=request.data["datePublished"],
        )
        UserBook.objects.create(
            user=user,
            book=book
        )

        request_tags = request.data['tags']

        if request_tags:
            for rt in request_tags:
                book.tags.get_or_create(label=rt)


        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    


    def list(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(
            books, many=True, context={'request': request}
        )
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, context={'request': request})
            return Response(serializer.data)

        except Book.DoesNotExist as ex:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, pk=None):
    #     category = Book.objects.get(pk=pk)
    #     category.label = request.data['label']
    #     category.save()
        
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



