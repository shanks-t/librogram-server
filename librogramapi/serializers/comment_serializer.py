from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', )

class CommentSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ( 'id', 'comment', 'user', 'created_on', )