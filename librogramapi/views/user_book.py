from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action


from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from librogramapi.models import Book, Reader, UserBook, Status

class UserBookView(ViewSet):
    
    def create(self, request):
        user = User.objects.get(username=request.auth.user)
        book = Book.objects.get(pk=request.data['book'])        
        status = Status.objects.get(pk=request.data['status'])

        try:
            user_book = UserBook.objects.create(
                user=user,
                book=book,
                status=status,
                rating=request.data["rating"],
                review=request.data["review"],
                start_date=request.data["startDate"],
                current_page=request.data["currentPage"],
            )
            serializer = UserBookSerializer(user_book, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user_books = UserBook.objects.all()
        serializer = UserBookSerializer(
            user_books, many=True, context={'request': request}
        )
        return Response(serializer.data)

    @action(methods=['PATCH'], detail=True)
    def updateUserBook(self, request, pk=None):

        user_book = UserBook.objects.get(pk=pk)
        user = User.objects.get(user=request.auth.user)


        try:

            user_book = UserBook.objects.get(pk=pk)
        except UserBook.DoesNotExist:
            return Response(
                {'message': 'Post does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user == user_book.user:
            try:
                user_book.status = request.data['statusId']
                user_book.rating = request.data['rating']
                user_book.review = request.data['review']
                user_book.start_date = request.data['startDate']
                user_book.finish_date = request.data['finishDate']
                user_book.current_page = request.data['currentPage']
                user_book.save()
                return Response({'you did it'}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({'wrong user': ex.args[0]})

    # def retrieve(self, request, pk=None):

    #     try:
    #         category = Book.objects.get(pk=pk)
    #         serializer = BookSerializer(category, context={'request': request})
    #         return Response(serializer.data)

    #     except Book.DoesNotExist as ex:
    #         return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, pk=None):
    #     category = Book.objects.get(pk=pk)
    #     category.label = request.data['label']
    #     category.save()
        
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk=None):
    #     try:
    #         category = Book.objects.get(pk=pk)
    #         category.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    #     except Book.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff' )

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class UserBookSerializer(serializers.ModelSerializer):

    status = StatusSerializer()
    book = BookSerializer()
    user = UserSerializer()
    class Meta:
        model = UserBook
        fields = ('id', 'user', 'rating', 'review', 'checkout_date', 'start_date', 'current_page', 'status', 'book')