from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import  Comment, Reader, Book, Status

class StatusView(ViewSet):

    # def create(self, request):

    #     reader = Reader.objects.get(user=request.auth.user)
    #     book = Book.objects.get(id=request.data['postId'])

    #     try:
    #         comment = Comment.objects.create(
    #             book = book,
    #             reader = reader,
    #             comment = request.data["comment"],
    #         )
    #         serializer = CommentSerializer(comment, context={'request': request})
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     except ValidationError as ex:
    #         return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):

    #     try:
    #         comment = Status.objects.get(pk=pk)
    #         serializer = StatusSerializer(comment, context={'request': request})
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)

    def list(self, request):
        statuses = Status.objects.all()

        serializer = StatusSerializer(
            statuses, many=True, context={'request': request}
        )
        return Response(serializer.data)

class StatusSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = ( 'label', )