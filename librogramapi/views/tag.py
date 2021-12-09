# """View module for handling requests about game types"""
# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from librogramapi.models import Tag


# class TagView(ViewSet):

#     def retrieve(self, request, pk=None):

#         try:
#             tag = Tag.objects.get(pk=pk)
#             serializer = TagSerializer(tag, context={'request': request})
#             return Response(serializer.data)
#         except Exception as ex:
#             return HttpResponseServerError(ex)

#     def list(self, request):

#         tags = Tag.objects.all()

#         # Note the additional `many=True` argument to the
#         # serializer. It's needed when you are serializing
#         # a list of objects instead of a single object.
#         serializer = TagSerializer(
#             tags, many=True, context={'request': request})
#         return Response(serializer.data)

# class TagSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Tag
#         fields = '__all__' #('id', 'label')