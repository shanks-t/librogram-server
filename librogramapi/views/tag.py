"""View module for handling requests about game types"""
from django.http import HttpResponseServerError

from rest_framework import status

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from librogramapi.models import Tag


class TagView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        tags = Tag.objects.filter()

        # Note the additional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        try:
            tag = Tag.objects.get(pk=pk)
            id = tag.id
            tag.delete()

            return Response({f'deleted tag {id}'}, status=status.HTTP_204_NO_CONTENT)

        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
