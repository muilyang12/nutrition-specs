from rest_framework import serializers

from .. import models
from . import NutritionSerializer


class ProductNutritionSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    nutritions = NutritionSerializer(many=True, read_only=True, source="nutrition_set")

    class Meta:
        model = models.Product
        fields = ["id", "brand_name", "product_name", "coupang_url", "nutritions"]

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None
