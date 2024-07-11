from rest_framework import serializers

from .. import models


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nutrition
        fields = [
            "id",
            "product",
            "s3_key",
            "data",
        ]
