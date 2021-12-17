from rest_framework import serializers
from librogramapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ( 'id', 'comment', 'user', 'created_on', )