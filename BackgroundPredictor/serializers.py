from rest_framework import serializers
from BackgroundPredictor.models import InputImage

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputImage
        fields = "__all__"