from rest_framework import serializers
from Prediction.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"