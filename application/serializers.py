from rest_framework import serializers
from application.models import ExtractedData

class ExtractedSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExtractedData
        fields="__all__"