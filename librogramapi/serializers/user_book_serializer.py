from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import Status, Comment, Book, UserBook, Tag
from librogramapi.serializers.comment_serializer import CommentSerializer
from librogramapi.serializers.status_serializer import StatusSerializer



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff')


class BookSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'image_path', 'description',
                  'page_count', 'publisher', 'date_published', 'checkout_date', 'tags', 'comments')


class UserBookSerializer(serializers.ModelSerializer):

    status = StatusSerializer()
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = UserBook
        fields = ('id', 'user', 'rating', 'review', 'start_date',
                  'finish_date', 'current_page', 'status', 'book')