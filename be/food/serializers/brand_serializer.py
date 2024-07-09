from rest_framework import serializers
from .. import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ["id", "food_categories", "name"]
