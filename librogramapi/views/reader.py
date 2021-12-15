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

