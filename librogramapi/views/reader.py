from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from librogramapi.models import  Reader
from librogramapi.serializers.reader_serializer import  ReaderSerializer



class ReaderView(ViewSet):

    @action(methods=['GET'], detail=False)
    def currentuser(self, request):

        reader = Reader.objects.get(user=request.auth.user)
        try:
            serializer = ReaderSerializer(reader, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reader.DoesNotExist:
            return Response(
                [], status=status.HTTP_204_NO_CONTENT
            )
    @action(methods=['PATCH'], detail=True)
    def edit(self, request, pk=None):

        reader = Reader.objects.get(pk=pk)

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        bio = request.data.get('bio', None)
        profile_image_url = request.data.get('profileImageUrl', None)
        background_image_url = request.data.get('backgroundImageUrl', None)
        if bio:
            reader.bio = bio
        if profile_image_url: 
            reader.profile_image_url = profile_image_url
        if background_image_url:
            reader.background_image_url = background_image_url
        reader.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({'yeah yeah yeah'}, status=status.HTTP_204_NO_CONTENT)
