from rest_framework import serializers
from . import models

class BiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biodata
        fields = '__all__'

class RisksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Risks
        fields = '__all__'

class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommendaions
        fields = '__all__'

