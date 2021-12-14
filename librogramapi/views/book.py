from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from librogramapi.models import Book, Comment, UserBook

class BookView(ViewSet):
    
    def create(self, request):

        user = User.objects.get(username=request.auth.user)
        try:
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
            serializer = BookSerializer(book, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

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
            category = Book.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'created_on')
        depth = 1

class BookSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('id', 'user', 'title', 'subtitle', 'author', 'image_path', 'description', 'page_count', 'publisher', 'date_published', 'comments', 'readers_list')