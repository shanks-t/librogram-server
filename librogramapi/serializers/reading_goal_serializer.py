from rest_framework import serializers
from librogramapi.models import ReadingGoal

class ReadingGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingGoal
        fields = ('id', 'number_of_pages', 'number_of_books', 'start_date', 'end_date', 'status')
