from rest_framework import serializers

from .. import models
from . import NutritionSerializer, ProductIngredientSerializer


class ProductDatailSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    nutritions = NutritionSerializer(many=True, read_only=True)
    ingredients = ProductIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = [
            "id",
            "brand_name",
            "product_name",
            "coupang_url",
            "nutritions",
            "ingredients",
        ]

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None
