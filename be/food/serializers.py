from rest_framework import serializers
from . import models


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "food_categories", "brand_name", "product_name", "coupang_url"]


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nutrition
        fields = [
            "id",
            "product",
            "s3_url",
            "data",
        ]
