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
        user = request.auth.user
        user_books = UserBook.objects.filter(user=user)
        serializer = UserBookSerializer(
            user_books, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):

        try:
            user_book = UserBook.objects.get(pk=pk)
            serializer = UserBookSerializer(user_book, context={'request': request})
            return Response(serializer.data)

        except UserBook.DoesNotExist as ex:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PATCH'], detail=True)
    def edit(self, request, pk=None):

        statusId = request.data.get('statusId', None)
        user_status = Status.objects.get(id=statusId)
        try:

            user_book = UserBook.objects.get(pk=pk)
        except UserBook.DoesNotExist:
            return Response(
                {'message': 'UserBook does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_book.status = user_status
        user_book.rating = request.data.get('rating', None)
        user_book.review = request.data.get('review', None)
        user_book.start_date = request.data.get('startDate', None)
        user_book.finish_date = request.data.get('finishDate', None)
        user_book.current_page = request.data.get('currentPage', None)
        user_book.save()

        return Response({'message': 'yay'}, status=status.HTTP_200_OK)

    # def retrieve(self, request, pk=None):

    #     try:
    #         category = Book.objects.get(pk=pk)
    #         serializer = BookSerializer(category, context={'request': request})
    #         return Response(serializer.data)

    #     except Book.DoesNotExist as ex:
    #         return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)


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
        fields = ('id', 'user', 'rating', 'review', 'start_date', 'finish_date', 'current_page', 'status', 'book',)