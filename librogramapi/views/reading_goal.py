from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action


from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from librogramapi.models import ReadingGoal
from librogramapi.serializers import ReadingGoalSerializer

class ReadingGoalView(ViewSet):
    
    def create(self, request):
        user = User.objects.get(username=request.auth.user)

        try:
            reading_goal = ReadingGoal.objects.create(
                user=user,
                number_of_pages=request.data.get("numberOfPages", None),
                number_of_books=request.data.get("numberOfBooks", None),
                start_date=request.data.get("startDate", None),
                end_date=request.data.get("endDate", None),
            )
            serializer = ReadingGoalSerializer(reading_goal, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = request.auth.user
        reading_goals = ReadingGoal.objects.filter(user=user)
        serializer = ReadingGoalSerializer(
            reading_goals, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):

        try:
            reading_goal = ReadingGoal.objects.get(pk=pk)
            serializer = ReadingGoalSerializer(reading_goal, context={'request': request})
            return Response(serializer.data)

        except ReadingGoal.DoesNotExist as ex:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PATCH'], detail=True)
    def edit(self, request, pk=None):

        try:

            reading_goal = ReadingGoal.objects.get(pk=pk)
        except ReadingGoal.DoesNotExist:
            return Response(
                {'message': 'Reading Goal does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        reading_goal.number_of_pages = request.data.get('numberOfPages', None)
        reading_goal.number_of_books = request.data.get('numberOfBooks', None)
        reading_goal.start_date = request.data.get('startDate', None)
        reading_goal.end_date = request.data.get('endDate', None)
        reading_goal.save()

        return Response({'message': 'yay'}, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):

        try:
            reading_goal = ReadingGoal.objects.get(pk=pk)
            reading_goal.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ReadingGoal.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)