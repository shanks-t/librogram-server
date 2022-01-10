from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import Status, Comment, Book, UserBook, Tag
from librogramapi.serializers.status_serializer import StatusSerializer


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

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

    #user = UserSerializer()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'authors', 'image_path', 'description', 'page_count', 'publisher', 'date_published', 'tags', 'comments')