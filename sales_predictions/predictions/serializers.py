# predictions/serializers.py
from rest_framework import serializers

class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField()