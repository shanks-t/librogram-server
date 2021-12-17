from rest_framework import serializers
from django.contrib.auth.models import User
from librogramapi.models import Status

class StatusSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Status
        fields = ( 'id', 'label', )