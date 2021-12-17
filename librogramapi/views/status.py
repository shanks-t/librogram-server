from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import  Comment, Reader, Book, Status

class StatusView(ViewSet):

    def list(self, request):
        statuses = Status.objects.all()

        serializer = StatusSerializer(
            statuses, many=True, context={'request': request}
        )
        return Response(serializer.data)

class StatusSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Status
        fields = ( 'id', 'label', )