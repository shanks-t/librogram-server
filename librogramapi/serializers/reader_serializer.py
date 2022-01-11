from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import Reader


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff' )

class ReaderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Reader
        fields = ('user', 'bio', 'profile_image_url', 'background_image_url', 'subscriber', 'current_books', 'goals', 'finished_books')