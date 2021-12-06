from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from librogramapi.models import Book, Reader, ReaderBook, Status

class ReaderBookView(ViewSet):
    """ Rare Categories """
    
    def create(self, request):
        reader = Reader.objects.get(user=request.auth.user)
        book = Book.objects.get(pk=request.data['book'])        
        status = Status.objects.get(pk=request.data['status'])

        try:
            reader_book = ReaderBook.objects.create(
                book = book,
                reader = reader,
                rating=request.data["rating"],
                review=request.data["review"],
                checkout_date=request.data["checkoutDate"],
                status = status

            )
            serializer = BookSerializer(reader_book, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        categories = Book.objects.all()
        serializer = BookSerializer(
            categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            category = Book.objects.get(pk=pk)
            serializer = BookSerializer(category, context={'request': request})
            return Response(serializer.data)

        except Book.DoesNotExist as ex:
            return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        category = Book.objects.get(pk=pk)
        category.label = request.data['label']
        category.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            category = Book.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'reader', 'comment', 'created_on')
        depth = 1

class BookSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'image_path', 'description', 'page_count', 'publisher', 'date_published', 'comments')